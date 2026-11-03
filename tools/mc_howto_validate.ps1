<#
.SYNOPSIS
  MS_SOC - checks the PowerShell blocks of site/data/mc-howto.json (CLAUDE.md 5gf, 3 XI 2026). Author: Piotr Wisniewski.
.DESCRIPTION
  For every block: the PowerShell parser finds no error; every *-Mg* cmdlet exists in the installed Microsoft Graph
  PowerShell SDK modules; every named parameter exists on that cmdlet (common parameters included); a block marked
  "write" carries -WhatIf on each New-/Set-/Update-/Remove-Mg* call; a block marked "read" calls no such cmdlet.
  Nothing connects to a tenant. Exit code = number of problems.
.EXAMPLE
  pwsh -NoProfile -File tools/mc_howto_validate.ps1 -Path site/data/mc-howto.json -ModulePath ./mods
#>
[CmdletBinding()]
param(
    [string]$Path = (Join-Path $PSScriptRoot '..\site\data\mc-howto.json'),
    [string]$ModulePath = ''
)
if ($ModulePath) { $env:PSModulePath = (Resolve-Path $ModulePath).Path + [IO.Path]::PathSeparator + $env:PSModulePath }
$data = Get-Content -Raw -Path $Path | ConvertFrom-Json
$common = [System.Management.Automation.PSCmdlet]::CommonParameters + [System.Management.Automation.PSCmdlet]::OptionalCommonParameters
$problems = 0; $checked = 0
foreach ($note in $data.notes) {
    foreach ($b in @($note.blocks)) {
        $checked++
        $tokens = $null; $errors = $null
        $ast = [System.Management.Automation.Language.Parser]::ParseInput([string]$b.code, [ref]$tokens, [ref]$errors)
        foreach ($e in $errors) { $problems++; "FAIL [$($note.key)] '$($b.t)': parse - $($e.Message)" }
        $calls = $ast.FindAll({ param($n) $n -is [System.Management.Automation.Language.CommandAst] }, $true)
        foreach ($c in $calls) {
            $name = $c.GetCommandName()
            if (-not $name -or $name -notmatch '^[A-Za-z]+-Mg') { continue }
            $cmd = Get-Command -Name $name -ErrorAction SilentlyContinue
            if (-not $cmd) { $problems++; "FAIL [$($note.key)] '$($b.t)': $name not found in the installed Microsoft Graph modules"; continue }
            $params = @($c.CommandElements | Where-Object { $_ -is [System.Management.Automation.Language.CommandParameterAst] } | ForEach-Object { $_.ParameterName })
            foreach ($p in $params) {
                $hit = $cmd.Parameters.Keys | Where-Object { $_ -ieq $p -or $_ -ilike "$p*" }
                $alias = $cmd.Parameters.Values | Where-Object { $_.Aliases -icontains $p }
                if (-not $hit -and -not $alias -and ($common -notcontains $p)) { $problems++; "FAIL [$($note.key)] '$($b.t)': $name has no parameter -$p" }
            }
            $isWrite = $name -match '^(New|Set|Update|Remove)-Mg'
            if ($isWrite -and $b.kind -eq 'read') { $problems++; "FAIL [$($note.key)] '$($b.t)': read block calls $name" }
            if ($isWrite -and $b.kind -eq 'write' -and ($params -notcontains 'WhatIf')) { $problems++; "FAIL [$($note.key)] '$($b.t)': $name without -WhatIf" }
            "ok   [$($note.key)] $name ($($cmd.Source) $($cmd.Version)) -" + ($params -join ' -')
        }
    }
}
"mc_howto_validate: $checked blocks, $problems problem(s)"
exit $problems

<#
.SYNOPSIS
    Grants the read-only application permissions the Graph radar needs (CLAUDE.md 5fs) to the app
    "MS-SOC Dev tenant reader" in the developer tenant, and lists them on the app registration.

.DESCRIPTION
    Author: Piotr Wiśniewski.
    The Graph radar (tools/graph_radar.py, workflow "Graph radar") reads tenant-wide configuration objects
    (authentication methods, authorization, cross-tenant access, security defaults, organization, Intune
    service settings...) with GET only and keeps the NAMES of the properties the service returns - never a
    value - to find properties Microsoft has not published in $metadata yet.

    For every permission below the script:
      1. adds it to the app registration's "Configured permissions" (requiredResourceAccess) when missing -
         without this step the Entra admin center lists the grant under "Other permissions granted"
         (owner, 30 X 2026);
      2. grants it (an app role assignment on the service principal = admin consent) when missing.
    It prints what the app held before, what it added and what was already there. Safe to run again.
    Run it as a Global Administrator, or as Privileged Role Administrator + an owner of the app registration,
    in the developer tenant. One sign-in: an existing Microsoft Graph session for the tenant with the needed
    scopes is reused.

.PARAMETER TenantId
    The developer tenant (GUID or domain). Not stored anywhere.

.PARAMETER AppDisplayName
    Display name of the app (default: MS-SOC Dev tenant reader).

.EXAMPLE
    ./Grant-GraphRadarPermissions.ps1 -TenantId contoso.onmicrosoft.com
#>
[CmdletBinding(SupportsShouldProcess)]
param(
    [Parameter(Mandatory)] [string] $TenantId,
    [string] $AppDisplayName = 'MS-SOC Dev tenant reader'
)

$ErrorActionPreference = 'Stop'
$needed = @(
    'Policy.Read.All',                          # authorization, authentication flows, cross-tenant access, security defaults...
    'Policy.Read.AuthenticationMethod',         # authenticationMethodsPolicy and every method configuration
    'Policy.Read.PermissionGrant',              # permissionGrantPolicies (30 X 2026: Policy.Read.All gave 403)
    'Organization.Read.All',                    # organization and its settings
    'OnPremDirectorySynchronization.Read.All',  # directory/onPremisesSynchronization (features)
    'DeviceManagementConfiguration.Read.All',   # Intune settings objects
    'DeviceManagementServiceConfig.Read.All'    # Intune service configuration (enrollment, settings)
)
$graphAppId = '00000003-0000-0000-c000-000000000000'

foreach ($m in 'Microsoft.Graph.Authentication', 'Microsoft.Graph.Applications') {
    if (-not (Get-Module -ListAvailable -Name $m)) { throw "Module $m is missing: Install-Module Microsoft.Graph -Scope CurrentUser" }
}

# one sign-in (owner, 30 X 2026: "I had to sign in twice"): reuse a session for this tenant that has the scopes
$scopes = 'Application.ReadWrite.All', 'AppRoleAssignment.ReadWrite.All'
$ctx = Get-MgContext
$sameTenant = $ctx -and ($ctx.TenantId -eq $TenantId -or ($ctx.Account -and $ctx.Account -like "*@$TenantId"))
$hasScopes = $ctx -and -not ($scopes | Where-Object { $ctx.Scopes -notcontains $_ })
if ($sameTenant -and $hasScopes) { Write-Host "Using the existing Microsoft Graph session ($($ctx.Account))" }
else { Connect-MgGraph -TenantId $TenantId -Scopes $scopes -NoWelcome }

$graph = Get-MgServicePrincipal -Filter "appId eq '$graphAppId'"
$sp = @(Get-MgServicePrincipal -Filter "displayName eq '$AppDisplayName'")
if ($sp.Count -ne 1) { throw "Expected one service principal named '$AppDisplayName', found $($sp.Count)" }
$sp = $sp[0]
$app = Get-MgApplication -Filter "appId eq '$($sp.AppId)'"
if (-not $app) { throw "The app registration of '$AppDisplayName' was not found in this tenant" }

$have = @(Get-MgServicePrincipalAppRoleAssignment -ServicePrincipalId $sp.Id -All |
          Where-Object ResourceId -eq $graph.Id | ForEach-Object AppRoleId)
$before = @($graph.AppRoles | Where-Object { $have -contains $_.Id } | ForEach-Object Value | Sort-Object)
# one name per line (owner, 30 X 2026: "lists written in one run are hard to read")
function Write-List([string] $Title, $Items) {
    Write-Host $Title
    if (-not $Items -or @($Items).Count -eq 0) { Write-Host "    -"; return }
    foreach ($i in @($Items)) { Write-Host "    $i" }
}
Write-List "Before: $AppDisplayName holds $($before.Count) Microsoft Graph application permission(s):" $before
Write-Host ""

# 1. configured permissions (requiredResourceAccess) - so the admin center lists them under "Configured permissions"
$rra = @($app.RequiredResourceAccess)
$graphRra = $rra | Where-Object ResourceAppId -eq $graphAppId
$configured = @($graphRra.ResourceAccess | Where-Object Type -eq 'Role' | ForEach-Object Id)
$toConfigure = @()
foreach ($p in $needed) {
    $role = $graph.AppRoles | Where-Object { $_.Value -eq $p -and $_.AllowedMemberTypes -contains 'Application' }
    if ($role -and $configured -notcontains $role.Id) { $toConfigure += $role }
}
if ($toConfigure.Count) {
    $access = @($graphRra.ResourceAccess | ForEach-Object { @{ id = $_.Id; type = $_.Type } })
    $access += @($toConfigure | ForEach-Object { @{ id = $_.Id; type = 'Role' } })
    $newRra = @($rra | Where-Object ResourceAppId -ne $graphAppId | ForEach-Object {
        @{ resourceAppId = $_.ResourceAppId; resourceAccess = @($_.ResourceAccess | ForEach-Object { @{ id = $_.Id; type = $_.Type } }) } })
    $newRra += @{ resourceAppId = $graphAppId; resourceAccess = $access }
    if ($PSCmdlet.ShouldProcess($AppDisplayName, "list $($toConfigure.Count) permission(s) as configured")) {
        Update-MgApplication -ApplicationId $app.Id -RequiredResourceAccess $newRra
        foreach ($r in $toConfigure) { Write-Host "CONF $($r.Value) (added to Configured permissions)" }
    }
}

# 2. admin consent (app role assignment)
$added = @(); $kept = @()
foreach ($p in $needed) {
    $role = $graph.AppRoles | Where-Object { $_.Value -eq $p -and $_.AllowedMemberTypes -contains 'Application' }
    if (-not $role) { Write-Warning "$p - Microsoft Graph in this tenant has no application permission with this name"; continue }
    if ($have -contains $role.Id) { Write-Host "OK   $p (already granted)"; $kept += $p; continue }
    if ($PSCmdlet.ShouldProcess($AppDisplayName, "grant $p")) {
        New-MgServicePrincipalAppRoleAssignment -ServicePrincipalId $sp.Id -PrincipalId $sp.Id `
            -ResourceId $graph.Id -AppRoleId $role.Id | Out-Null
        Write-Host "ADD  $p"; $added += $p
    }
}

$other = @($before | Where-Object { $needed -notcontains $_ })
Write-Host ""
Write-Host "Summary for $AppDisplayName"
Write-List "  Admin consent granted now:" $added
Write-List "  Admin consent already there:" $kept
Write-List "  Added to Configured permissions now:" @($toConfigure | ForEach-Object Value)
Write-List "  Other permissions of the app (not needed by the radar, not touched):" $other
Write-Host ""
Write-Host "Done. The Graph radar picks the permissions up on its next run (tokens refresh within an hour)."

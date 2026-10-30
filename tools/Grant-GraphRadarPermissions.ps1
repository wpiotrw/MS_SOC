<#
.SYNOPSIS
    Grants the read-only application permissions the Graph radar needs (CLAUDE.md 5fs) to the app
    "MS-SOC Dev tenant reader" in the developer tenant.

.DESCRIPTION
    Author: Piotr Wiśniewski.
    The Graph radar (tools/graph_radar.py, workflow "Graph radar") reads tenant-wide configuration objects
    (authentication methods, authorization, cross-tenant access, security defaults, organization, Intune
    service settings...) with GET only and keeps the NAMES of the properties the service returns - never a
    value - to find properties Microsoft has not published in $metadata yet.
    This script adds the application permissions below to the app's service principal (an app role
    assignment = admin consent). Run it as a Global Administrator or Privileged Role Administrator
    of the developer tenant. It changes nothing else and is safe to run again (skips what is granted).

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
    'Organization.Read.All',                    # organization and its settings
    'OnPremDirectorySynchronization.Read.All',  # directory/onPremisesSynchronization (features)
    'DeviceManagementConfiguration.Read.All',   # Intune settings objects
    'DeviceManagementServiceConfig.Read.All'    # Intune service configuration (enrollment, settings)
)

foreach ($m in 'Microsoft.Graph.Authentication', 'Microsoft.Graph.Applications') {
    if (-not (Get-Module -ListAvailable -Name $m)) { throw "Module $m is missing: Install-Module Microsoft.Graph -Scope CurrentUser" }
}
Connect-MgGraph -TenantId $TenantId -Scopes 'Application.Read.All', 'AppRoleAssignment.ReadWrite.All' -NoWelcome

$graph = Get-MgServicePrincipal -Filter "appId eq '00000003-0000-0000-c000-000000000000'"
$sp = @(Get-MgServicePrincipal -Filter "displayName eq '$AppDisplayName'")
if ($sp.Count -ne 1) { throw "Expected one service principal named '$AppDisplayName', found $($sp.Count)" }
$sp = $sp[0]
$have = @(Get-MgServicePrincipalAppRoleAssignment -ServicePrincipalId $sp.Id -All |
          Where-Object ResourceId -eq $graph.Id | ForEach-Object AppRoleId)

foreach ($p in $needed) {
    $role = $graph.AppRoles | Where-Object { $_.Value -eq $p -and $_.AllowedMemberTypes -contains 'Application' }
    if (-not $role) { Write-Warning "$p - no such application permission in Microsoft Graph"; continue }
    if ($have -contains $role.Id) { Write-Host "OK   $p (already granted)"; continue }
    if ($PSCmdlet.ShouldProcess($AppDisplayName, "grant $p")) {
        New-MgServicePrincipalAppRoleAssignment -ServicePrincipalId $sp.Id -PrincipalId $sp.Id `
            -ResourceId $graph.Id -AppRoleId $role.Id | Out-Null
        Write-Host "ADD  $p"
    }
}
Write-Host "Done. The Graph radar picks the permissions up on its next run (tokens refresh within an hour)."

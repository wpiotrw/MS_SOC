#Requires -Version 7
<#
.SYNOPSIS
  Tworzy (albo uzupelnia) aplikacje Entra "MS-SOC First-party apps reader" dla workflow fpa-tenant.yml.

.DESCRIPTION
  Autor: Piotr Wisniewski - APN Promise S.A.
  Jedno logowanie kodem urzadzenia (device code) jako administrator tenanta, przez publicznego klienta
  "Microsoft Graph Command Line Tools" (14d82eec-204b-4c2f-b7e8-296a70dab67e), potem zwykle wywolania REST
  Microsoft Graph tym jednym tokenem. Nie wymaga modulow Microsoft.Graph ani okna WAM, wiec dziala tez
  z procesu bez okna (np. uruchomionego przez asystenta).

  Skrypt jest idempotentny - mozna go uruchomic ponownie:
    1. aplikacja (single tenant) z uprawnieniami aplikacyjnymi Graph: Application.Read.All
       i DelegatedPermissionGrant.Read.All - tworzy albo poprawia requiredResourceAccess,
    2. service principal,
    3. poswiadczenie federacyjne GitHub OIDC (repo:<Repo>:ref:refs/heads/<Branch>) - bez sekretu,
    4. zgoda administratora = przypisanie obu rol aplikacyjnych do service principala.
  Wynik trafia na ekran i do pliku JSON ($OutFile). Wartosci tenantId i appId wpisz w env:
  pliku .github/workflows/fpa-tenant.yml (README.md, rozdz. 5.3).

  Potrzebne role konta: Cloud Application Administrator (kroki 1-3) oraz Privileged Role Administrator
  albo Global Administrator (krok 4). Zakresy delegowane, o ktore prosi logowanie:
  Application.ReadWrite.All, AppRoleAssignment.ReadWrite.All.

.EXAMPLE
  pwsh -NoProfile -File tools/New-FpaReaderApp.ps1 -TenantId 833fd6f2-76f2-4750-b776-b9228da14a4e
#>
param(
  [Parameter(Mandatory)] [ValidatePattern('^[0-9a-fA-F-]{36}$')] [string] $TenantId,
  [string] $Name    = 'MS-SOC First-party apps reader',
  [string] $Repo    = 'wpiotrw/MS_SOC',
  [string] $Branch  = 'main',
  [string] $OutFile = (Join-Path ([IO.Path]::GetTempPath()) 'ms-soc-fpa-app.json')
)
$ErrorActionPreference = 'Stop'
$Subject = "repo:${Repo}:ref:refs/heads/$Branch"
$Client  = '14d82eec-204b-4c2f-b7e8-296a70dab67e'
$Scope   = 'https://graph.microsoft.com/Application.ReadWrite.All https://graph.microsoft.com/AppRoleAssignment.ReadWrite.All openid profile offline_access'
$Auth    = "https://login.microsoftonline.com/$TenantId/oauth2/v2.0"

# --- logowanie kodem urzadzenia (jeden token na caly przebieg) ---
$dc = Invoke-RestMethod -Method POST -Uri "$Auth/devicecode" -Body @{ client_id = $Client; scope = $Scope }
Write-Output "KOD: $($dc.user_code)  STRONA: $($dc.verification_uri)"
$deadline = (Get-Date).AddSeconds([int]$dc.expires_in); $tok = $null
while (-not $tok -and (Get-Date) -lt $deadline) {
  Start-Sleep -Seconds ([int]$dc.interval)
  try { $tok = Invoke-RestMethod -Method POST -Uri "$Auth/token" -Body @{ grant_type = 'urn:ietf:params:oauth:grant-type:device_code'; client_id = $Client; device_code = $dc.device_code } }
  catch { $e = ($_.ErrorDetails.Message | ConvertFrom-Json -ErrorAction SilentlyContinue).error; if ($e -notin 'authorization_pending', 'slow_down') { throw "Logowanie: $e" } }
}
if (-not $tok) { throw 'Kod wygasl bez logowania' }
Write-Output 'ZALOGOWANO'

$H = @{ Authorization = "Bearer $($tok.access_token)" }
$G = 'https://graph.microsoft.com/v1.0'
function Gr($m, $u, $b) {
  if ($b) { Invoke-RestMethod -Method $m -Uri "$G$u" -Headers $H -Body ($b | ConvertTo-Json -Depth 6) -ContentType 'application/json' }
  else    { Invoke-RestMethod -Method $m -Uri "$G$u" -Headers $H }
}

$org = (Gr GET '/organization?$select=id,displayName,verifiedDomains').value[0]
if ($org.id -ne $TenantId) { throw "Zalogowano do innego tenanta: $($org.id)" }
$me = Gr GET '/me?$select=userPrincipalName'

# --- 1. aplikacja z uprawnieniami ---
$graph = (Gr GET "/servicePrincipals?`$filter=appId eq '00000003-0000-0000-c000-000000000000'&`$select=id,appId,appRoles").value[0]
$roles = @($graph.appRoles | Where-Object { $_.value -in 'Application.Read.All', 'DelegatedPermissionGrant.Read.All' })
if ($roles.Count -ne 2) { throw "Nie znaleziono obu rol Graph (znaleziono $($roles.Count))" }
$rra = @(@{ resourceAppId = $graph.appId; resourceAccess = @($roles | ForEach-Object { @{ id = $_.id; type = 'Role' } }) })
$app = (Gr GET "/applications?`$filter=displayName eq '$Name'").value | Select-Object -First 1
if (-not $app) { $app = Gr POST '/applications' @{ displayName = $Name; signInAudience = 'AzureADMyOrg'; requiredResourceAccess = $rra }; $created = $true }
else { Gr PATCH "/applications/$($app.id)" @{ requiredResourceAccess = $rra } | Out-Null; $created = $false }
Write-Output "APLIKACJA: $($app.appId) (nowa: $created)"

# --- 2. service principal (replikacja katalogu bywa opozniona - ponawiamy) ---
$sp = (Gr GET "/servicePrincipals?`$filter=appId eq '$($app.appId)'").value | Select-Object -First 1
for ($i = 0; -not $sp -and $i -lt 12; $i++) { try { $sp = Gr POST '/servicePrincipals' @{ appId = $app.appId } } catch { Start-Sleep -Seconds 5 } }
if (-not $sp) { throw 'Nie udalo sie utworzyc service principala' }

# --- 3. poswiadczenie federacyjne GitHub OIDC ---
$fics = (Gr GET "/applications/$($app.id)/federatedIdentityCredentials").value
if (-not ($fics | Where-Object { $_.subject -eq $Subject })) {
  Gr POST "/applications/$($app.id)/federatedIdentityCredentials" @{
    name = "github-$($Repo.Split('/')[1].ToLower() -replace '_','-')-$Branch"; issuer = 'https://token.actions.githubusercontent.com'
    subject = $Subject; audiences = @('api://AzureADTokenExchange') } | Out-Null
}

# --- 4. zgoda administratora (przypisanie rol aplikacyjnych) ---
$have = (Gr GET "/servicePrincipals/$($sp.id)/appRoleAssignments").value
$grant = foreach ($r in $roles) {
  if ($have | Where-Object { $_.appRoleId -eq $r.id }) { "$($r.value)=juz nadane"; continue }
  try { Gr POST "/servicePrincipals/$($graph.id)/appRoleAssignedTo" @{ principalId = $sp.id; resourceId = $graph.id; appRoleId = $r.id } | Out-Null; "$($r.value)=nadane" }
  catch { "$($r.value)=BLAD: $($_.ErrorDetails.Message)" }
}

$fic = (Gr GET "/applications/$($app.id)/federatedIdentityCredentials").value | Where-Object { $_.subject -eq $Subject }
$res = [ordered]@{
  tenantId = $org.id; tenantName = $org.displayName; defaultDomain = ($org.verifiedDomains | Where-Object isDefault).name
  account = $me.userPrincipalName; created = $created; appName = $Name; appId = $app.appId
  appObjectId = $app.id; spObjectId = $sp.id; ficName = $fic.name; ficSubject = $fic.subject; grants = @($grant)
}
$res | ConvertTo-Json -Depth 4 | Set-Content -Path $OutFile -Encoding utf8
$res | ConvertTo-Json -Depth 4
Write-Output "AZURE_TENANT_ID: $($org.id)"
Write-Output "AZURE_CLIENT_ID: $($app.appId)"

---
layout: Reference
monikers:
- entra-powershell
defaultMoniker: entra-powershell
versioningType: Ranged
title: New-EntraApplication (Microsoft.Entra.Applications) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/powershell/module/microsoft.entra.applications/new-entraapplication?view=entra-powershell
config_moniker_range: entra-powershell
uid: Microsoft.Entra.Applications.New-EntraApplication
module: Microsoft.Entra.Applications
description: This article provides details on the New-EntraApplication command.
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /powershell/entra-powershell/breadcrumb/toc.json
ms.devlang: powershell
ms.service: entra-powershell
author: msewaweru
ms.author: eunicewaweru
ms.topic: reference
feedback_system: Standard
feedback_product_url: https://github.com/microsoftgraph/entra-powershell/issues/new/choose
toc_preview: true
document type: cmdlet
external help file: Microsoft.Entra.Applications-Help.xml
HelpUri: https://learn.microsoft.com/powershell/module/Microsoft.Entra.Applications/New-EntraApplication
Locale: en-us
manager: mwongerapk
Module Name: Microsoft.Entra.Applications
ms.date: 2025-04-26T00:00:00.0000000Z
ms.reviewer: stevemutungi
PlatyPS schema version: 2024-05-01T00:00:00.0000000Z
document_id: 1ac33066-527e-7269-6be8-4b75c3b2a1ea
document_version_independent_id: e8f4dee8-b63b-ff8b-783b-062b7b6e7222
original_content_git_url: https://github.com/MicrosoftDocs/entra-powershell-docs-pr/blob/live/docs/reference/v1.0/Microsoft.Entra.Applications/New-EntraApplication.md
default_moniker: entra-powershell
site_name: Docs
depot_name: MSDN.reference
in_right_rail: h2h3
page_type: powershell
page_kind: command
toc_rel: ../entra-powershell/toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: module/microsoft.entra.applications/new-entraapplication
moniker_range_name: b41933a8c477651a7e44b237a8130c32
monikers:
- entra-powershell
item_type: Content
source_path: docs/reference/v1.0/Microsoft.Entra.Applications/New-EntraApplication.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c0439c36-80e3-415f-8e4c-6951e3f1b136
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/2812d699-d85f-4a7f-839d-44e218b35d24
platformId: cd4bdcc7-479a-b570-aaee-1278616ec1c2
---

# New-EntraApplication

- Module:
    - [Microsoft.Entra.Applications Module v1.3](./)

Creates a new application registration in Microsoft Entra ID.

## Syntax

### CreateApplication (Default)

```Syntax
New-EntraApplication
    -DisplayName <String>
    [-SignInAudience <String>]
    [-IdentifierUris <List[String]>]
    [-IsDeviceOnlyAuthSupported <Boolean>]
    [-IsFallbackPublicClient <Boolean>]
    [-AppRoles <List[MicrosoftGraphAppRole]>]
    [-RequiredResourceAccess <MicrosoftGraphRequiredResourceAccess[]>]
    [-Api <MicrosoftGraphApiApplication>]
    [-PublicClient <MicrosoftGraphPublicClientApplication>]
    [-Web <MicrosoftGraphWebApplication>]
    [-InformationalUrl <MicrosoftGraphInformationalUrl>]
    [-ParentalControlSettings <MicrosoftGraphParentalControlSettings>]
    [-OptionalClaims <MicrosoftGraphOptionalClaims>]
    [-AddIns <Object[]>]
    [-KeyCredentials <Object[]>]
    [-PasswordCredentials <MicrosoftGraphPasswordCredential[]>]
    [-Tags <List[String]>]
    [-GroupMembershipClaims <String>]
    [-TokenEncryptionKeyId <String>]
    [-WhatIf]
    [-Confirm]
    [<CommonParameters>]
```

### CreateWithAdditionalProperties

```Syntax
New-EntraApplication
    -AdditionalProperties <Hashtable>
    [-DisplayName <String>]
    [-WhatIf]
    [-Confirm]
    [<CommonParameters>]
```

## Description

The `New-EntraApplication` cmdlet creates a new application registration in Microsoft Entra ID. Applications can be configured for different authentication scenarios, including single-tenant or multitenant, and can use various credential types.

## Examples

### Example 1: Create a basic application

```powershell
Connect-Entra -Scopes 'Application.ReadWrite.All'
New-EntraApplication -DisplayName 'Contoso HR App'
```

```Output
DisplayName               Id                                   AppId                                SignInAudience PublisherDomain
-----------               --                                   -----                                -------------- ---------------
Contoso HR Onboarding App dddd3333-ee44-5555-66ff-777777aaaaaa 22223333-cccc-4444-dddd-5555eeee6666 AzureADMyOrg   contoso.com
```

This command creates a basic application registration with default settings.

### Example 2: Create a multitenant application

```powershell
Connect-Entra -Scopes 'Application.ReadWrite.All'
New-EntraApplication -DisplayName 'Contoso Partner API' -SignInAudience 'AzureADMultipleOrgs'
```

```Output
DisplayName               Id                                   AppId                                SignInAudience PublisherDomain
-----------               --                                   -----                                -------------- ---------------
Contoso Partner API   dddd3333-ee44-5555-66ff-777777aaaaaa 22223333-cccc-4444-dddd-5555eeee6666 AzureADMyOrg   contoso.com
```

This command creates an application that can be used by accounts from any Microsoft Entra ID tenant.

### Example 3: Create an application with application password (client secret)

```powershell
Connect-Entra -Scopes 'Application.ReadWrite.All'
$passwordCred = [Microsoft.Graph.PowerShell.Models.MicrosoftGraphPasswordCredential]@{
    DisplayName = 'AI automation Cred'
    StartDateTime = [DateTime]::UtcNow
    EndDateTime = [DateTime]::UtcNow.AddYears(1)
}

$app = New-EntraApplication -DisplayName 'Contoso Automation App' -PasswordCredentials @($passwordCred)
$app.PasswordCredentials.SecretText
```

This command creates an application with a password credential (client secret). The secret value is returned in the response.

### Example 4: Create an application with API permissions

```powershell
Connect-Entra -Scopes 'Application.ReadWrite.All'
$msGraphAccess = @{
    ResourceAppId = "00000003-0000-0000-c000-000000000000"  # Microsoft Graph
    ResourceAccess = @(
        @{
            Id = "e1fe6dd8-ba31-4d61-89e7-88639da4683d"  # User.Read
            Type = "Scope"
        },
        @{
            Id = "df021288-bdef-4463-88db-98f22de89214"  # User.ReadWrite.All
            Type = "Role"
        }
    )
}

New-EntraApplication -DisplayName "User Management App" -RequiredResourceAccess @($msGraphAccess)
```

This command creates an application with specified Microsoft Graph API permissions.

### Example 5: Create an application with add-ins details

```powershell
Connect-Entra -Scopes 'Application.ReadWrite.All'
$addIn = @{
    Id         = "00000002-0000-0ff1-ce00-000000000000"  # Outlook's service principal ID
    Type       = "messageReadCommandSurface"          # UI surface
    Properties = @(
        @{ Key = "extensionId"; Value = "Contoso.EmailInsights" },
        @{ Key = "sourceLocation"; Value = "https://contoso.com/addin/home.html" },
        @{ Key = "supportedLocales"; Value = "en-US" }
    )
}

New-EntraApplication -DisplayName "Contoso Email Insights" -AddIns $addIn
```

This example registers the Contoso Email Insights add-in with Microsoft Entra ID so it can integrate with Outlook on the web and be sideloaded or published through AppSource.

### Example 6: Create an application with app roles

```powershell
Connect-Entra -Scopes 'Application.ReadWrite.All'
$appRoles = @(
    @{
        id = [Guid]::NewGuid()
        allowedMemberTypes = @("User", "Application")
        description = "Read-only access to HR data"
        displayName = "HR Reader"
        isEnabled = $true
        value = "HRReader"
        origin = "Application"
    },
    @{
        id = [Guid]::NewGuid()
        allowedMemberTypes = @("User", "Application")
        description = "Manage HR data"
        displayName = "HR Manager"
        isEnabled = $true
        value = "HRManager"
        origin = "Application"
    }
)

# Create the new application registration with AppRoles
New-EntraApplication -DisplayName "Contoso Sandbox" -AppRoles $appRoles
```

This example registers a multi-tenant API called `Contoso Sandbox` and defines two custom roles: `HRReader` for `read-only` access and `HRManager` for `full access` to employee data.

### Example 7: Create a web application with identifier URIs

```powershell
Connect-Entra -Scopes 'Application.ReadWrite.All'
New-EntraApplication -DisplayName 'Contoso App' -IdentifierUris 'https://myselfserve.contoso.com'
```

This command creates an application with identifier URIs.

### Example 8: Create an application using AdditionalProperties

```powershell
Connect-Entra -Scopes 'Application.ReadWrite.All'
$props = @{
    displayName = "Advanced Configuration App"
    signInAudience = "AzureADMyOrg"
    api = @{
        oauth2PermissionScopes = @(
            @{
                id = [Guid]::NewGuid().ToString("D")
                adminConsentDescription = "Allow the app to access resources on user's behalf"
                adminConsentDisplayName = "Access resources"
                isEnabled = $true
                type = "Admin"
                value = "access"
            }
        )
    }
}

New-EntraApplication -AdditionalProperties $props
```

This command creates an application using the AdditionalProperties parameter for advanced configuration.

### Example 9: Create an application with tagging details

```powershell
Connect-Entra -Scopes 'Application.ReadWrite.All'
New-EntraApplication -DisplayName "Contoso Tagged App" `
    -SignInAudience "AzureADMultipleOrgs" `
    -Tags @(
        "WindowsAzureActiveDirectoryIntegratedApp",
        "HideApp",
        "CertifiedApp"
    )
```

This example creates a multi-tenant enterprise app and adds tags to support Microsoft Partner Center discovery and admin consent filtering.

### Example 10: Create a public client application

```powershell
Connect-Entra -Scopes 'Application.ReadWrite.All'

# Define the PublicClient object with redirect URIs
$publicClient = @{
    redirectUris = @("https://login.microsoftonline.com/common/oauth2/nativeclient")
}

New-EntraApplication -DisplayName "Contoso PowerShell Client" `
    -SignInAudience "AzureADMyOrg" `
    -PublicClient $publicClient
```

This example shows how to register a public client app with a redirect URI for local testing, such as for Android or iOS apps that authenticate users interactively.

### Example 11: Create an application with custom scopes

```powershell
Connect-Entra -Scopes 'Application.ReadWrite.All'

# Define custom scopes for the API
$api = @{
    oauth2PermissionScopes = @(
        @{
            id = [Guid]::NewGuid()
            adminConsentDescription = "Allow the app to read user profiles."
            adminConsentDisplayName = "Read user profiles"
            isEnabled = $true
            type = "User"
            value = "Employee.Read"
        },
        @{
            id = [Guid]::NewGuid()
            adminConsentDescription = "Allow the app to write user profiles."
            adminConsentDisplayName = "Write user profiles"
            isEnabled = $true
            type = "User"
            value = "Employee.Write"
        }
    )
}

New-EntraApplication -DisplayName "Contoso API App" -Api $api
```

This example shows how to register an application and define its available permissions using the `-Api` parameter.

### Example 12: Create an application with RequiredResourceAccess details

```powershell
Connect-Entra -Scopes 'Application.ReadWrite.All'
# Define the RequiredResourceAccess for Microsoft Graph API
$graphResourceAccess = @{
    ResourceAppId = '00000003-0000-0000-c000-000000000000'  # Microsoft Graph API AppID
    ResourceAccess = @(
        @{
            Id = 'e1fe6dd8-ba31-4d61-89e7-88639da4683d'  # GUID for 'User.Read' permission
            Type = 'Scope'  # Type of permission
        }
    )
}

# Define the RequiredResourceAccess for Azure Service Management API
$serviceManagementResourceAccess = @{
    ResourceAppId = '797f4846-ba00-4fd7-ba43-dac1f8f63013'  # Azure Service Management API ID
    ResourceAccess = @(
        @{
            Id = '41094075-9dad-400e-a0bd-54e686782033'  # GUID for 'user_impersonation'
            Type = 'Scope'  # Type of permission
        }
    )
}

# Combine both resource accesses into an array
$RequiredResourceAccess = @($graphResourceAccess, $serviceManagementResourceAccess)

# Create a new application with the required resource access
New-EntraApplication -DisplayName 'Contoso Service App' -RequiredResourceAccess $RequiredResourceAccess
```

This example creates a new application called `Contoso Service App` and grants it delegated permissions to call both `Microsoft Graph` (e.g., User.Read) and `Azure Service Management API` (user\_impersonation) by specifying the required resource access during registration.

### Example 13: Create a web application with redirect URIs

```powershell
Connect-Entra -Scopes 'Application.ReadWrite.All'
$web = @{
    redirectUris = @("https://contoso.com/auth", "https://contoso.com/auth/callback")
    implicitGrantSettings = @{
        enableAccessTokenIssuance = $true
        enableIdTokenIssuance = $true
    }
    logoutUrl = "https://contoso.com/logout"
}

New-EntraApplication -DisplayName "Contoso Web App" -Web $web
```

This command creates a web application with redirect URIs and implicit grant settings.

### Example 14: Create a web application with support and marketing URIs

```powershell
Connect-Entra -Scopes 'Application.ReadWrite.All'

$informationalUrl = @{
    marketingUrl = "https://contoso.com/marketing"
    privacyStatementUrl = "https://contoso.com/privacy"
    supportUrl = "https://contoso.com/support"
    termsOfServiceUrl = "https://contoso.com/terms"
}

New-EntraApplication -DisplayName "Contoso Pay Portal" -InformationalUrl $informationalUrl
```

This command creates an application with support and marketing URLs to help users and admins identify and trust the app during consent or in the Microsoft Entra portal.

### Example 15: Create an application with optional claims

```powershell
Connect-Entra -Scopes 'Application.ReadWrite.All'

$optionalClaims = @{
    idToken = @(
        @{
            name = "email"
            source = $null # user, directory, $null
            essential = $true
            additionalProperties = @{}
        }
    )
    accessToken = @(
        @{
            name = "roles"
            source = $null # user, directory, $null
            essential = $false
            additionalProperties = @{}
        }
    )
}

New-EntraApplication -DisplayName "Contoso Claims App" -OptionalClaims $optionalClaims
```

This command creates an application with optional claims, such as email, upn (userPrincipalName) claims in ID tokens and the sid (session ID) claim in access tokens for custom session tracking and user identity resolution.

### Example 16: Create an application with parental control settings

```powershell
Connect-Entra -Scopes 'Application.ReadWrite.All'

# Define parental control settings
$parentalControlSettings = @{
    countriesBlockedForMinors = @("DE", "FR")   # ISO country codes
    legalAgeGroupRule = "RequireConsentForMinors"
}

# Create the app with parental control settings
New-EntraApplication -DisplayName "Contoso Kids Stream" `
    -SignInAudience "AzureADandPersonalMicrosoftAccount" `
    -ParentalControlSettings $parentalControlSettings
```

This command creates an application with parental control settings. For example, it can restrict access to a streaming app like "Contoso Kids Stream" for children in specific countries such as Germany and France to meet compliance requirements.

### Example 17: Create an application with a certificate credential

```powershell
Connect-Entra -Scopes 'Application.ReadWrite.All'
$cert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2("C:\Certificates\MyCertificate.cer")
$thumbprint = $cert.Thumbprint
$base64Cert = [Convert]::ToBase64String($cert.RawData)

$keyCred = @{
    CustomKeyIdentifier = $thumbprint
    Type = "AsymmetricX509Cert"
    Usage = "Verify"
    Key = $base64Cert
    DisplayName = "App Certificate"
    StartDateTime = [DateTime]::UtcNow
    EndDateTime = [DateTime]::UtcNow.AddYears(1)
}

New-EntraApplication -DisplayName "Contoso Certificate App" -KeyCredentials @($keyCred)
```

This command creates an application with a certificate credential.

## Parameters

### -AddIns

Defines custom behavior extensions for the application.

#### Parameter properties

| Type: | System.Object[] |
| --- | --- |
| Default value: | None |
| Supports wildcards: | False |
| DontShow: | False |

#### Parameter sets

 CreateApplication 

| Position: | Named |
| --- | --- |
| Mandatory: | False |
| Value from pipeline: | False |
| Value from pipeline by property name: | False |
| Value from remaining arguments: | False |

### -AdditionalProperties

Custom properties to send directly to the Microsoft Graph API.

#### Parameter properties

| Type: | Hashtable |
| --- | --- |
| Default value: | None |
| Supports wildcards: | False |
| DontShow: | False |
| Aliases: | Body, Properties, BodyParameter |

#### Parameter sets

 CreateWithAdditionalProperties 

| Position: | Named |
| --- | --- |
| Mandatory: | True |
| Value from pipeline: | False |
| Value from pipeline by property name: | False |
| Value from remaining arguments: | False |

### -Api

The API settings for the application, including OAuth2 permission scopes and app roles.

#### Parameter properties

| Type: | Microsoft.Graph.PowerShell.Models.MicrosoftGraphApiApplication |
| --- | --- |
| Default value: | None |
| Supports wildcards: | False |
| DontShow: | False |

#### Parameter sets

 CreateApplication 

| Position: | Named |
| --- | --- |
| Mandatory: | False |
| Value from pipeline: | False |
| Value from pipeline by property name: | False |
| Value from remaining arguments: | False |

### -AppRoles

The collection of application roles defined for the application.

#### Parameter properties

| Type: | System.Collections.Generic.List`1[Microsoft.Graph.PowerShell.Models.MicrosoftGraphAppRole] |
| --- | --- |
| Default value: | None |
| Supports wildcards: | False |
| DontShow: | False |

#### Parameter sets

 CreateApplication 

| Position: | Named |
| --- | --- |
| Mandatory: | False |
| Value from pipeline: | False |
| Value from pipeline by property name: | False |
| Value from remaining arguments: | False |

### -DisplayName

The display name of the application in Microsoft Entra ID.

#### Parameter properties

| Type: | String |
| --- | --- |
| Default value: | None |
| Supports wildcards: | False |
| DontShow: | False |

#### Parameter sets

 CreateApplication 

| Position: | 0 |
| --- | --- |
| Mandatory: | True |
| Value from pipeline: | False |
| Value from pipeline by property name: | False |
| Value from remaining arguments: | False |

### -GroupMembershipClaims

Configures the groups claim issued in a user or OAuth 2.0 access token. Valid values: `None`, `SecurityGroup`, `All`.

#### Parameter properties

| Type: | String |
| --- | --- |
| Default value: | None |
| Supports wildcards: | False |
| DontShow: | False |

#### Parameter sets

 CreateApplication 

| Position: | Named |
| --- | --- |
| Mandatory: | False |
| Value from pipeline: | False |
| Value from pipeline by property name: | False |
| Value from remaining arguments: | False |

### -IdentifierUris

URIs that uniquely identify the application within Azure AD.

#### Parameter properties

| Type: | System.Collections.Generic.List`1[System.String] |
| --- | --- |
| Default value: | None |
| Supports wildcards: | False |
| DontShow: | False |

#### Parameter sets

 CreateApplication 

| Position: | Named |
| --- | --- |
| Mandatory: | False |
| Value from pipeline: | False |
| Value from pipeline by property name: | False |
| Value from remaining arguments: | False |

### -InformationalUrl

URLs with more information about the application (marketing, terms of service, privacy, etc.).

#### Parameter properties

| Type: | Microsoft.Graph.PowerShell.Models.MicrosoftGraphInformationalUrl |
| --- | --- |
| Default value: | None |
| Supports wildcards: | False |
| DontShow: | False |

#### Parameter sets

 CreateApplication 

| Position: | Named |
| --- | --- |
| Mandatory: | False |
| Value from pipeline: | False |
| Value from pipeline by property name: | False |
| Value from remaining arguments: | False |

### -IsDeviceOnlyAuthSupported

Specifies whether this application supports device authentication without a user.

#### Parameter properties

| Type: | System.Nullable`1[System.Boolean] |
| --- | --- |
| Default value: | None |
| Supports wildcards: | False |
| DontShow: | False |

#### Parameter sets

 CreateApplication 

| Position: | Named |
| --- | --- |
| Mandatory: | False |
| Value from pipeline: | False |
| Value from pipeline by property name: | False |
| Value from remaining arguments: | False |

### -IsFallbackPublicClient

Specifies whether the application is a public client. If not set, the default behavior is `false`.

#### Parameter properties

| Type: | System.Nullable`1[System.Boolean] |
| --- | --- |
| Default value: | None |
| Supports wildcards: | False |
| DontShow: | False |

#### Parameter sets

 CreateApplication 

| Position: | Named |
| --- | --- |
| Mandatory: | False |
| Value from pipeline: | False |
| Value from pipeline by property name: | False |
| Value from remaining arguments: | False |

### -KeyCredentials

The collection of certificate credentials associated with the application. Each credential should contain:

- CustomKeyIdentifier: (Optional) Certificate thumbprint
- DisplayName: (Optional) Friendly name for the credential
- EndDateTime: Expiration date and time in UTC
- Key: Base64-encoded certificate data
- StartDateTime: Start date and time in UTC
- Type: Type of the credential, typically "AsymmetricX509Cert"
- Usage: Purpose of the credential, typically "Verify"

#### Parameter properties

| Type: | System.Object[] |
| --- | --- |
| Default value: | None |
| Supports wildcards: | False |
| DontShow: | False |

#### Parameter sets

 CreateApplication 

| Position: | Named |
| --- | --- |
| Mandatory: | False |
| Value from pipeline: | False |
| Value from pipeline by property name: | False |
| Value from remaining arguments: | False |

### -OptionalClaims

The optional claims configuration that is included in access and ID tokens.

#### Parameter properties

| Type: | Microsoft.Graph.PowerShell.Models.MicrosoftGraphOptionalClaims |
| --- | --- |
| Default value: | None |
| Supports wildcards: | False |
| DontShow: | False |

#### Parameter sets

 CreateApplication 

| Position: | Named |
| --- | --- |
| Mandatory: | False |
| Value from pipeline: | False |
| Value from pipeline by property name: | False |
| Value from remaining arguments: | False |

### -ParentalControlSettings

Specifies parental control settings for an application.

#### Parameter properties

| Type: | Microsoft.Graph.PowerShell.Models.MicrosoftGraphParentalControlSettings |
| --- | --- |
| Default value: | None |
| Supports wildcards: | False |
| DontShow: | False |

#### Parameter sets

 CreateApplication 

| Position: | Named |
| --- | --- |
| Mandatory: | False |
| Value from pipeline: | False |
| Value from pipeline by property name: | False |
| Value from remaining arguments: | False |

### -PasswordCredentials

The collection of password credentials associated with the application.

#### Parameter properties

| Type: | Microsoft.Graph.PowerShell.Models.MicrosoftGraphPasswordCredential[] |
| --- | --- |
| Default value: | None |
| Supports wildcards: | False |
| DontShow: | False |

#### Parameter sets

 CreateApplication 

| Position: | Named |
| --- | --- |
| Mandatory: | False |
| Value from pipeline: | False |
| Value from pipeline by property name: | False |
| Value from remaining arguments: | False |

### -PublicClient

Settings for a public client application (mobile or desktop).

#### Parameter properties

| Type: | Microsoft.Graph.PowerShell.Models.MicrosoftGraphPublicClientApplication |
| --- | --- |
| Default value: | None |
| Supports wildcards: | False |
| DontShow: | False |

#### Parameter sets

 CreateApplication 

| Position: | Named |
| --- | --- |
| Mandatory: | False |
| Value from pipeline: | False |
| Value from pipeline by property name: | False |
| Value from remaining arguments: | False |

### -RequiredResourceAccess

The API permissions required by the application to other resources such as Microsoft Graph.

#### Parameter properties

| Type: | Microsoft.Graph.PowerShell.Models.MicrosoftGraphRequiredResourceAccess[] |
| --- | --- |
| Default value: | None |
| Supports wildcards: | False |
| DontShow: | False |

#### Parameter sets

 CreateApplication 

| Position: | Named |
| --- | --- |
| Mandatory: | False |
| Value from pipeline: | False |
| Value from pipeline by property name: | False |
| Value from remaining arguments: | False |

### -SignInAudience

Defines which accounts are supported for this application. Valid values: `AzureADMyOrg`, `AzureADMultipleOrgs`, `AzureADandPersonalMicrosoftAccount`, `PersonalMicrosoftAccount`.

#### Parameter properties

| Type: | String |
| --- | --- |
| Default value: | None |
| Supports wildcards: | False |
| DontShow: | False |

#### Parameter sets

 CreateApplication 

| Position: | Named |
| --- | --- |
| Mandatory: | False |
| Value from pipeline: | False |
| Value from pipeline by property name: | False |
| Value from remaining arguments: | False |

### -Tags

Custom tags that can be used to categorize and identify the application.

#### Parameter properties

| Type: | System.Collections.Generic.List`1[System.String] |
| --- | --- |
| Default value: | None |
| Supports wildcards: | False |
| DontShow: | False |

#### Parameter sets

 CreateApplication 

| Position: | Named |
| --- | --- |
| Mandatory: | False |
| Value from pipeline: | False |
| Value from pipeline by property name: | False |
| Value from remaining arguments: | False |

### -TokenEncryptionKeyId

Specifies the keyId of a public key from the keyCredentials collection for token encryption.

#### Parameter properties

| Type: | String |
| --- | --- |
| Default value: | None |
| Supports wildcards: | False |
| DontShow: | False |

#### Parameter sets

 CreateApplication 

| Position: | Named |
| --- | --- |
| Mandatory: | False |
| Value from pipeline: | False |
| Value from pipeline by property name: | False |
| Value from remaining arguments: | False |

### -Web

Settings for a web application, including redirect URIs and logout URL.

#### Parameter properties

| Type: | Microsoft.Graph.PowerShell.Models.MicrosoftGraphWebApplication |
| --- | --- |
| Default value: | None |
| Supports wildcards: | False |
| DontShow: | False |

#### Parameter sets

 CreateApplication 

| Position: | Named |
| --- | --- |
| Mandatory: | False |
| Value from pipeline: | False |
| Value from pipeline by property name: | False |
| Value from remaining arguments: | False |

### CommonParameters

This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable, -InformationAction, -InformationVariable, -OutBuffer, -OutVariable, -PipelineVariable, -ProgressAction, -Verbose, -WarningAction, and -WarningVariable. For more information, see [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216).

## Inputs

### None

This cmdlet doesn't accept pipeline input.

## Outputs

### PSCustomObject

Returns a custom object representing the created Microsoft Entra application.

## Notes

- This cmdlet requires the 'Application.ReadWrite.All' permission scope.
- When using certificate credentials, ensure proper certificate management practices:
    - Use strong key sizes (RSA 2048-bit or higher)
    - Store private keys securely
    - Implement certificate rotation before expiration
- Password credentials (client secrets) should be used only when certificates can't be used.
- For security best practices, consider:
    - Using the least privilege principle when assigning API permissions
    - Limiting application roles to only what's necessary
    - Using conditional access policies for sensitive applications
    - Implementing proper credential rotation processes

## Related Links

- [Get-EntraApplication](get-entraapplication)
- [Remove-EntraApplication](remove-entraapplication)
- [Set-EntraApplication](set-entraapplication)
- [Microsoft Entra application management documentation](/en-us/entra/identity-platform/quickstart-register-app)
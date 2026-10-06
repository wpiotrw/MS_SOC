---
layout: Conceptual
title: How to troubleshoot delivery of Extended Security Updates for Windows Server through Azure Arc - Azure Arc | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/azure-arc/servers/troubleshoot-extended-security-updates
breadcrumb_path: ../../breadcrumb/azure-management/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/146/azure-arc/
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/5c778dec-0625-ec11-b6e6-000d3a4f0858
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure
ms.suite: office
zone_pivot_group_filename: zone-pivots/azure-management/zone-pivot-groups.json
author: davidsmatlak
learn_banner_products:
- azure
ms.reviewer: davidsmatlak
ms.author: davidsmatlak
ms.service: azure-arc
ms.subservice: servers-azure-arc
description: Learn how to troubleshoot delivery of Extended Security Updates (ESU) for Windows Server 2012 and Windows Server 2016 through Azure Arc.
ms.topic: troubleshooting
ms.date: 2026-09-11T00:00:00.0000000Z
zone_pivot_groups: extended-security-updates-windows-server
locale: en-us
document_id: 5265708c-f38d-e961-cd0c-bfb00fb8dad7
document_version_independent_id: a0f2fa8d-09aa-d083-d0f1-ea7a00193129
original_content_git_url: https://github.com/MicrosoftDocs/azure-management-docs-pr/blob/live/articles/azure-arc/servers/troubleshoot-extended-security-updates.md
site_name: Docs
depot_name: Learn.azure-management
page_type: conceptual
toc_rel: toc.json
asset_id: azure-arc/servers/troubleshoot-extended-security-updates
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/azure-arc/servers/troubleshoot-extended-security-updates.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/beac614b-f66d-40ed-a947-3996de709333
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/fc3f72c2-fb6f-4cea-95ee-b444e52254ee
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9da05372-4706-43ec-a899-f436adab380d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/f12cf087-582d-48ac-a085-0c19adf1e391
platformId: cffa7622-cec4-b3c1-3af5-a7c0c55bf901
---

# How to troubleshoot delivery of Extended Security Updates for Windows Server through Azure Arc - Azure Arc | Microsoft Learn

This article explains how to identify and resolve problems when enabling [Extended Security Updates (ESU) for Windows Server](deliver-extended-security-updates) through Azure Arc-enabled servers.

::: zone pivot="windows-server-2012"

Use these troubleshooting steps to address common issues with ESU licensing, enrollment, resource provider registration, and patch delivery for Windows Server 2012 and 2012 R2.

Important

The Windows Server 2012 and Windows Server 2012 R2 ESU period ends on October 13, 2026. The October 13, 2026, security update is the final update provided through ESUs. At midnight Coordinated Universal Time (UTC) on October 14, 2026, ESU licenses enabled by Azure Arc deactivate and stop providing update eligibility. A deactivated license after this time is expected behavior, not an enrollment error. Troubleshooting can't restore eligibility for security updates released after October 13, 2026.

::: zone-end

::: zone pivot="windows-server-2016"

Use these troubleshooting steps to address common issues with ESU licensing, enrollment, resource provider registration, and patch delivery for Windows Server 2016.

::: zone-end

## License provisioning issues

If you can't provision a Windows Server ESU license for Azure Arc-enabled servers, verify you meet these conditions:

- **Permissions:** Verify you have sufficient permissions (**Contributor** role or higher) within the scope of ESU provisioning and linking.
- **Core minimums:** Verify that you specified sufficient cores for the ESU license. Physical core-based licenses require a minimum of 16 cores per machine, and virtual core-based licenses require a minimum of eight cores per virtual machine (VM).
- **Conventions:** Verify that you selected an appropriate subscription and resource group and provided a unique name for the ESU license.

## ESU enrollment issues

If you can't link your Azure Arc-enabled server to an activated ESU license, verify that you meet these conditions:

::: zone pivot="windows-server-2012"

- **Connectivity:** Azure Arc-enabled server is **Connected**. For information about viewing the status of Azure Arc-enabled machines, see [Agent status](overview#agent-status).
- **Agent version:** Connected Machine agent is a supported version. For Windows Server 2012 ESUs, the agent must be version 1.34 or higher. If the agent version is less than 1.34, update it to this version or higher.
- **Operating system:** Only Azure Arc-enabled servers running Windows Server 2012 or Windows Server 2012 R2 are eligible to enroll in ESU.
- **License properties:** Verify the license is activated and allocated sufficient physical or virtual cores to support the intended scope of servers.

::: zone-end

::: zone pivot="windows-server-2016"

- **Connectivity:** Azure Arc-enabled server is **Connected**. For information about viewing the status of Azure Arc-enabled machines, see [Agent status](overview#agent-status).
- **Agent version:** Connected Machine agent is a supported version. For Windows Server 2016 ESUs, the agent must be version 1.62 or higher. If the agent version is less than 1.62, update it to this version or higher.
- **Operating system:** Only Azure Arc-enabled servers running Windows Server 2016 are eligible to enroll in ESU.
- **License properties:** Verify the license is activated and allocated sufficient physical or virtual cores to support the intended scope of servers.

::: zone-end

## Resource providers

If you can't enable this service offering, review the resource providers registered on the subscription. If you receive an error while attempting to register the resource providers, validate the role assignments on the subscription. Also review any potential Azure policies that might be set with a **Deny** policy, preventing the enablement of these resource providers:

- **Microsoft.HybridCompute:** This resource provider is essential for Azure Arc-enabled servers, and it allows you to onboard and manage on-premises servers in the Azure portal.
- **Microsoft.GuestConfiguration:** Enables Guest Configuration policies, which are used to assess and enforce configurations on your Arc-enabled servers for compliance and security.
- **Microsoft.Compute:** This resource provider is required for Azure Update Management, which is used to manage updates and patches on your on-premises servers, including ESU updates.
- **Microsoft.Security:** Enabling this resource provider is crucial for implementing security-related features and configurations for both Azure Arc and on-premises servers.
- **Microsoft.OperationalInsights:** This resource provider is associated with **Azure Monitor and Log Analytics**, which is used for monitoring and collecting telemetry data from your hybrid infrastructure, including on-premises servers.
- **Microsoft.Sql:** If you're managing on-premises SQL Server instances and require ESU for SQL Server, you need to enable this resource provider.
- **Microsoft.Storage:** Enabling this resource provider is important for managing storage resources, which might be relevant for hybrid and on-premises scenarios.

## ESU patch issues

::: zone pivot="windows-server-2012"

### ESU patch status

To detect whether your Azure Arc-enabled servers are patched with the most recent Windows Server 2012 (R2) ESU, use Azure Update Manager or Azure Policy. The [(Preview): Extended Security Updates should be installed on Windows Server 2012 Arc machines](https://portal.azure.com/#view/Microsoft_Azure_Policy/PolicyDetail.ReactView/id/%2Fproviders%2FMicrosoft.Authorization%2FpolicyDefinitions%2F14b4e776-9fab-44b0-b53f-38d2458ea8be/version%7E/null/scopes%7E/%5B%22%2Fsubscriptions%2F4fabcc63-0ec0-4708-8a98-04b990085bf8%22%5D) policy checks whether the most recent Windows Server 2012 ESU patches were received.

Both of these options are available at no additional cost for Azure Arc-enabled servers enrolled in Windows Server 2012 ESU enabled by Azure Arc.

::: zone-end

### ESU prerequisites

::: zone pivot="windows-server-2012"

Ensure that you download both the licensing package and servicing stack update (SSU) for the Azure Arc-enabled server as documented in [KB5031043: Procedure to continue receiving security updates after extended support ended on October 10, 2023](https://support.microsoft.com/topic/kb5031043-procedure-to-continue-receiving-security-updates-after-extended-support-has-ended-on-october-10-2023-c1a20132-e34c-402d-96ca-1e785ed51d45). Make sure you follow all of the networking prerequisites as documented in [Prepare to deliver Extended Security Updates for Windows Server](prepare-extended-security-updates#networking).

::: zone-end

::: zone pivot="windows-server-2016"

Ensure that you download any required licensing package and servicing stack update (SSU) for the Azure Arc-enabled server as documented in the applicable Microsoft Knowledge Base article for Windows Server 2016. Make sure you follow all of the networking prerequisites as documented in [Prepare to deliver Extended Security Updates for Windows Server](prepare-extended-security-updates#networking).

::: zone-end

## Troubleshooting errors

### Error: Trying to check IMDS again (HRESULT 12002 or 12029)

When you install the ESU enabled by Azure Arc and it fails with the following Instance Metadata Service (IMDS) errors:

```error
ESU: Trying to Check IMDS Again LastError=HRESULT_FROM_WIN32(12002)

ESU: Trying to Check IMDS Again LastError=HRESULT_FROM_WIN32(12029)
```

You might need to update the intermediate certificate authorities trusted by your computer by using one of the following methods.

Important

If you're running the [latest version of the Azure Connected machine agent](agent-release-notes), you don't need to install the intermediate CA certificates or allow access to the Public Key Infrastructure (PKI) URL. However, if you assigned a license before the agent was upgraded, it can take up to 15 days for the older license to be replaced. During this time, the intermediate cert is still required. After upgrading the agent, you can delete the license file `%ProgramData%\AzureConnectedMachineAgent\certs\license.json` to force it to refresh.

#### Option 1: Allow access to the PKI URL

Configure your network firewall and proxy server to allow access from your Windows Server machines to `http://www.microsoft.com/pkiops/certs` and `https://www.microsoft.com/pkiops/certs` (both TCP 80 and 443). This configuration enables the machines to automatically retrieve any missing intermediate CA certificates from Microsoft.

```powershell
# Define firewall rule name
$ruleNameHttp = "Allow_HTTP_to_MicrosoftPKI"
$ruleNameHttps = "Allow_HTTPS_to_MicrosoftPKI"

# Allow outgoing traffic to any IP address on TCP port 80 (HTTP)
New-NetFirewallRule -DisplayName $ruleNameHttp `
    -Direction Outbound `
    -Action Allow `
    -Protocol TCP `
    -RemotePort 80 `
    -Profile Any `
    -Description "Allow outbound HTTP traffic to Microsoft PKI OPS"

# Allow outgoing traffic to any IP address on TCP port 443 (HTTPS)
New-NetFirewallRule -DisplayName $ruleNameHttps `
    -Direction Outbound `
    -Action Allow `
    -Protocol TCP `
    -RemotePort 443 `
    -Profile Any `
    -Description "Allow outbound HTTPS traffic to Microsoft PKI OPS"
```

After you make the network changes to allow access to the PKI URL, try installing the Windows updates again. You might need to reboot your computer for the automatic installation of certificates and validation of the license to take effect.

#### Option 2: Manually download and install the intermediate CA certificates

If you can't allow access to the PKI URL from your servers, manually download and install the certificates on each machine.

1. On any computer with internet access, download these intermediate CA certificates:

    1. [Microsoft Azure RSA TLS Issuing CA 03](https://www.microsoft.com/pkiops/certs/Microsoft%20Azure%20RSA%20TLS%20Issuing%20CA%2003%20-%20xsign.crt)
    2. [Microsoft Azure RSA TLS Issuing CA 04](https://www.microsoft.com/pkiops/certs/Microsoft%20Azure%20RSA%20TLS%20Issuing%20CA%2004%20-%20xsign.crt)
    3. [Microsoft Azure RSA TLS Issuing CA 07](https://www.microsoft.com/pkiops/certs/Microsoft%20Azure%20RSA%20TLS%20Issuing%20CA%2007%20-%20xsign.crt)
    4. [Microsoft Azure RSA TLS Issuing CA 08](https://www.microsoft.com/pkiops/certs/Microsoft%20Azure%20RSA%20TLS%20Issuing%20CA%2008%20-%20xsign.crt)
2. Copy the certificate files to your Windows Server machines.
3. Run any one set of the following commands in an elevated command prompt or PowerShell session to add the certificates to the "Intermediate Certificate Authorities" store for the local computer. Run the command from the same directory as the certificate files. These commands are safe to run multiple times and if the certificate is already installed, nothing changes.

    ```powershell
    certutil -addstore CA "Microsoft Azure RSA TLS Issuing CA 03 - xsign.crt"
    certutil -addstore CA "Microsoft Azure RSA TLS Issuing CA 04 - xsign.crt"
    certutil -addstore CA "Microsoft Azure RSA TLS Issuing CA 07 - xsign.crt"
    certutil -addstore CA "Microsoft Azure RSA TLS Issuing CA 08 - xsign.crt"
    ```
4. Try installing the Windows updates again. You might need to reboot your computer for the validation logic to recognize the newly imported intermediate CA certificates.

### Error: Not eligible (HRESULT 1633)

If you encounter the error `ESU: not eligible HRESULT_FROM_WIN32(1633)`, run the following command:

```powershell
Remove-Item "$env:ProgramData\AzureConnectedMachineAgent\Certs\license.json" -Force
Restart-Service HIMDS
```

If you have other issues receiving ESU after successfully enrolling the server through Arc-enabled servers, or you need more information about issues that affect ESU deployment, see [Troubleshoot issues in ESU](/en-us/troubleshoot/windows-client/windows-7-eos-faq/troubleshoot-extended-security-updates-issues).
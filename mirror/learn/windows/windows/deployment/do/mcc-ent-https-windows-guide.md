---
layout: Conceptual
title: Configure HTTPS Support for Windows | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/deployment/do/mcc-ent-https-windows-guide
recommendations: true
adobe-target: true
ms.collection:
- tier2
breadcrumb_path: /windows/resources/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-Windows
feedback_system: Standard
feedback_product_url: https://support.microsoft.com/windows/send-feedback-to-microsoft-with-the-feedback-hub-app-f59187f8-8739-22d6-ba93-f66612949332
description: Details on how to configure HTTPS support for Microsoft Connected Cache for Enterprise and Education cache nodes on Windows.
ms.service: windows-client
ms.subservice: itpro-updates
ms.topic: how-to
manager: naengler
ms.author: adityamiddha
author: adityamiddha
ms.date: 2026-06-24T00:00:00.0000000Z
ai-usage: ai-assisted
locale: en-us
document_id: 68998538-8b96-bd67-3d4c-54fc896a4d6f
document_version_independent_id: 68998538-8b96-bd67-3d4c-54fc896a4d6f
original_content_git_url: https://github.com/MicrosoftDocs/windows-docs-pr/blob/live/windows/deployment/do/mcc-ent-https-windows-guide.md
site_name: Docs
depot_name: TechNet.win-deployment
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/TechNet.win-deployment/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: do/mcc-ent-https-windows-guide
moniker_range_name: 
monikers: []
item_type: Content
source_path: windows/deployment/do/mcc-ent-https-windows-guide.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
platformId: 06493ccf-b4ed-0dba-1ea3-8e5437fe9229
---

# Configure HTTPS Support for Windows | Microsoft Learn

This article provides instructions for enabling HTTPS support on Microsoft Connected Cache for Enterprise and Education nodes running on a Windows host machine.

The setup process requires generating a Certificate Signing Request (CSR) on your host machine, signing the CSR using enterprise or public PKI, and then importing back to the host machine.

## Prerequisites

Before setting up HTTPS functionality, ensure the following requirements are met:

- **Cache node is on the GA software version**

    1. Open Azure portal and navigate to the Connected Cache for Enterprise resource that houses your cache nodes.
    2. Under **Cache Node Management**, find the cache node you wish to enable HTTPS on.
    3. Verify that the node is on the GA version - should show "Yes" or "N/A" in the **Migrated** column.
    4. If not on GA version ("No" in the **Migrated** column), select the cache node, navigate to the **Deployment** tab, and follow the instructions to redeploy Connected Cache.
- **Access to a Certificate Authority (CA)**

    You'll need access to either your enterprise PKI or a public CA. If using enterprise PKI, check your organization's requirements for submitting a CSR to CA.
- **Document client connection methods**

    Note the IP address or hostname (FQDN) that your clients use to connect to your Connected Cache server. This value will be used as a Subject Alternative Name (SAN) input during the process of generating a CSR.
- **Ensure port 443 availability**

    In order to establish an HTTPS connection with Connected Cache, port 443 needs to be available on your host machine. Run the following command to check:

    ```powershell
    netstat -an | findstr :443
    ```

    Review the output:

    - **No output** — Port 443 isn't in use. Proceed with HTTPS setup.
    - **Output contains `LISTENING`** (for example, `TCP 0.0.0.0:443 0.0.0.0:0 LISTENING`) — Port 443 is open and listening for incoming connections. Proceed with HTTPS setup.
    - **Output contains `ESTABLISHED`** (for example, `TCP 192.168.1.10:443 10.0.0.5:52674 ESTABLISHED`) — Port 443 is actively being used by another service. Identify and stop the conflicting service before Connected Cache can use port 443.

    Tip

    To identify a service using port 443, run `netstat -ano | findstr :443` to find the process ID (PID) in the last column. Then run `tasklist /fi "pid eq <PID>"` (replacing `<PID>` with the actual number) to see the process name. Common services that use port 443 include IIS, other web servers, and VPN software. Stop or reconfigure the conflicting service before continuing.
- **Verify corporate proxy configuration**

    If your firewall or corporate proxy intercepts HTTPS traffic to your Connected Cache server (for example, via TLS inspection), certificate validation will always fail regardless of certificate configuration.

For more information on any of the prerequisites, see the [HTTPS on Windows reference page](mcc-ent-https-windows-reference).

## Generate a Certificate Signing Request (CSR)

Important

Each cache node needs its own CSR/certificate (cannot share):

- Use consistent naming: mcc-node1.company.com, mcc-node2.company.com, etc.
- Document which certificate belongs to which node
- **Wildcard certificates will not work**. The CSR/certificate used for HTTPS connection to Connected Cache is uniquely tied to each cache node for security purposes.

1. Open PowerShell as Administrator and navigate to the Connected Cache folder that contains its PowerShell scripts.

    Run the following command to navigate to this Connected Cache scripts folder:

    ```powershell
       cd (deliveryoptimization-cli mcc-get-scripts-path)
    ```
2. Configure the parameters for `generateCsr.ps1` and run the script with your specified values.

    **Basic Syntax**

    ```powershell
       .\generateCsr.ps1 [Required Parameters] [Subject Parameters] [SAN Parameters]
    ```

    **Required Parameters**

    | Parameter | Description |
    | --- | --- |
    | `-algo` | Certificate algorithm: `RSA`, `EC`, `ED25519`, or `ED448` |
    | `-keySizeOrCurve` | For RSA: key size (`2048`, `3072`, `4096`). For EC: curve name (`prime256v1`, `secp384r1`). For ED25519 and ED448: no key size needed. |
    | `-csrName` | Name desired for the CSR file |
    | `-mccRunTimeAccount` | The account that runs the Connected Cache software. This should be a PowerShell variable containing the username of the account you intend to designate as the Connected Cache runtime account. For example, `$User = "LocalMachineName\Username"` for a local user account. If you're using a Group Managed Service Account (gMSA), it should be formatted as `"Domain\Username$"`. |
    | `-mccLocalAccountCredential` | A PowerShell credential object for the Connected Cache runtime account. **This is only needed if you're using a local user account, domain user account, or service account**. The command `$myLocalAccountCredential = Get-Credential` can be used to queue the credential retrieval GUI. |

    Note

    The `-mccRunTimeAccount` parameter is available in Connected Cache Windows application **v1.0.26.0** and later. If you're using the earlier **v1.0.24.0** application, use `-RunTimeAccountName` for local user, domain user, and service accounts, or `-RunTimeAccount` for Group Managed Service Accounts (gMSA).

    **Subject Parameters**

    | Parameter | Required | Description | Example |
    | --- | --- | --- | --- |
    | `-subjectCommonName` | Yes | Common name for the certificate | `"localhost"`, `"example.com"` |
    | `-subjectCountry` | No | Two-letter country code | `"US"`, `"CA"`, `"GB"` |
    | `-subjectState` | No | State or province | `"WA"`, `"TX"`, `"Ontario"` |
    | `-subjectOrg` | No | Organization name | `"MyCompany"`, `"ACME Corp"` |

    Warning

    The SAN configuration is critical for certificate validation. Your certificate must match exactly how clients connect to your Connected Cache, otherwise the clients bypass the cache node.

    For example, if your clients connect via IP address `192.168.1.100` but your certificate only has `-sanDns "server.local"`, certificate validation fails.

    **Subject Alternative Names (at least one required)**

    | Parameter | Description | Example |
    | --- | --- | --- |
    | `-sanDns` | DNS names (comma-separated) | `"localhost,example.com,api.example.com"` |
    | `-sanIp` | IP addresses (comma-separated) | `"127.0.0.1,192.168.1.100"` |
    | `-sanUri` | URIs (comma-separated) | `"https://example.com,http://localhost"` |
    | `-sanEmail` | Email addresses (comma-separated) | `"admin@example.com,user@domain.com"` |
    | `-sanRid` | Registered IDs (comma-separated) |  |
    | `-sanDirName` | Directory names (comma-separated) |  |
    | `-sanOtherName` | Other names (comma-separated) |  |

    For more detail and scenario-based examples on CSR script parameters, see [HTTPS on Windows reference](mcc-ent-https-windows-reference)
3. Validate that the CSR generation process completed successfully.

    If you encounter errors, locate the timestamped `GenerateCsr.log` file in the folder specified in the script output. Look for the output line that starts with "Check logs for detailed error information:" The directory ends with (...\Certificates\logs).

    - **File format:** GenerateCsr\_YYYYMMDD-HHMMSS.log
    - **Example:** GenerateCsr\_20251201\_143022.log is a file created December 1, 2025 at 2:30:22 PM
4. Locate the generated CSR file in your **Certificates folder** on your host machine and transfer it if necessary

    The location of the **Certificates folder** is specified in the script output, starting with "CSR file created at: ...". The directory ends with (...\Certificates\certs).

## Sign the CSR

1. Select a Certificate Authority (CA) to sign the CSR.

    Important

    The CA signature must match a root certificate in the client's trusted root store.

    - **Enterprise PKI**: Most customers use their organization's internal PKI infrastructure to sign the CSR. Check with your IT or security team on your organization's process for submitting a CSR to your internal CA.
    - **Public CA**: If you don't have an enterprise PKI, you can use a public CA. The following resources can help you get started:

        - [DigiCert Certificate Utility](https://www.digicert.com/kb/util/import-code-signing-certificate-digicert-utility.htm)
        - [Let's Encrypt CSR Process](https://community.letsencrypt.org/t/how-to-obtain-a-ssl-certificate-from-lets-encrypt-with-a-csr/15942)
2. Submit the CSR to your chosen CA and save the signed certificate.

    Your signed certificate must be a PEM-encoded X.509 certificate with a .crt extension (Base64 text beginning with -----BEGIN CERTIFICATE-----). DER/binary certificates must be converted to PEM -- see [HTTPS on Windows reference](mcc-ent-https-windows-reference) on how to convert to .crt format.

    Note

    Connected Cache does **not currently support password-protected formats** (.pfx, .p12, .p7b). Support for these will be added soon as part of our certificate automation roadmap.
3. Verify that signed certificate is in the correct format.

    Confirm PEM encoding:

    ```powershell
    Get-Content "xxxx.crt" | Select-String "BEGIN CERTIFICATE"
    ```

    Expected successful output:

    ```powershell
    -----BEGIN CERTIFICATE-----
    ```
4. Move your signed certificate to the **Certificates folder** on your Windows host machine.

    This will be the same folder where you initially found your CSR after it generated: (...\Certificates\certs).

Caution

Do not share private keys, Connected Cache only requires the signed certificate.

## Import signed TLS certificate

1. Open PowerShell as Administrator and navigate to the Connected Cache folder that contains its PowerShell scripts.
2. Configure the parameters for `importCert.ps1` and run the script with your specified values.

    **Basic Syntax**

    ```powershell
      .\importCert.ps1 [Required Parameters]
    ```

    **Required Parameters**

    | Parameter | Description |
    | --- | --- |
    | `-certName` | Complete filename of your signed TLS certificate (with or without .crt extension) |
    | `-mccRunTimeAccount` | The account that runs the Connected Cache software. This should be a PowerShell variable containing the username of the account you intend to designate as the Connected Cache runtime account. For example, `$User = "LocalMachineName\Username"` for a local user account. If you're using a Group Managed Service Account (gMSA), it should be formatted as `"Domain\Username$"`. |
    | `-mccLocalAccountCredential` | A PowerShell credential object for the Connected Cache runtime account. **This is only needed if you're using a local user account, domain user account, or service account**. For example, `$myLocalAccountCredential = Get-Credential`. |

    Note

    The `-mccRunTimeAccount` parameter is available in Connected Cache Windows application **v1.0.26.0** and later. If you're using the earlier **v1.0.24.0** application, use `-RunTimeAccountName` for local user, domain user, and service accounts, or `-RunTimeAccount` for Group Managed Service Accounts (gMSA).

    Note

    The v1.0.24.0 Connected Cache Windows application doesn't support running `importCert.ps1` on Windows Server 2022 or Windows Server 2025 with a gMSA runtime account. Use the v1.0.26.0 application or later to run this script in those environments.

    **Example**

    ```powershell
      .\importCert.ps1 `
        -mccRunTimeAccount $myLocalAccountCredential.Username `
        -mccLocalAccountCredential $myLocalAccountCredential `
        -certName "myTlsCert.crt"
    ```
3. Validate that the import process completed successfully.

    If you encounter errors, locate the timestamped `ImportCert.log` file in the folder specified in the script output. Look for the output line that starts with "You can find logs here: ..."

    - **File format:** ImportCert\_YYYYMMDD-HHMMSS.log
    - **Example:** ImportCert\_20251201\_143022.log is a file created December 1, 2025 at 2:30:22 PM
4. Verify that the correct certificate was imported by running the `ShowCertDetails.ps1` script.

    Note

    The `ShowCertDetails.ps1` script is available starting with Windows deployment application v1.0.26.

    ```powershell
    .\ShowCertDetails.ps1
    ```

    This script displays the certificate thumbprint and expiration date for the TLS certificate currently imported to the cache node.
5. Ensure Connected Cache is accessible to external clients via port 443.

    Note

    Verify again that port 443 is available before configuring port forwarding: `netstat -an | findstr :443`

    **Forward Port 443 Traffic**

    Use the following command to bridge traffic from your Windows host machine to the Connected Cache container:

    ```powershell
     $ipFilePath = Join-Path ([System.Environment]::GetEnvironmentVariable("MCC_INSTALLATION_FOLDER", "Machine")) "wslIp.txt"
     $ipAddress = (Get-Content $ipFilePath | Select-Object -First 1).Trim()
     netsh interface portproxy add v4tov4 listenport=443 listenaddress=0.0.0.0 connectport=443 connectaddress=$ipAddress
    ```

    This sets up a port proxy so that incoming traffic on port 443 is redirected to the container’s internal IP.

    **Open Port 443 in the Firewall**

    Even with port forwarding in place, Windows Firewall might block incoming or outgoing traffic on port 443. Use the following commands to ensure that HTTPS traffic can flow freely to and from your Connected Cache.

    ```powershell
     [void](New-NetFirewallRule -DisplayName "WSL2 Port Bridge (HTTPS)" -Direction Inbound -Action Allow -Protocol TCP -LocalPort "443")
     [void](New-NetFirewallRule -DisplayName "WSL2 Port Bridge (HTTPS)" -Direction Outbound -Action Allow -Protocol TCP -LocalPort "443")
    ```

For instructions on how to further validate the certificate import, see the [HTTPS on Windows validation page](mcc-ent-https-windows-validation).

## Disable HTTPS support

If you need to revert your Connected Cache to HTTP-only communication, follow these steps. This process won't delete anything in the Certificates folder, including CSR files, certificates, and logs.

1. Open PowerShell as Administrator and navigate to the PowerShell scripts folder.
2. Configure the parameters for `disableTls.ps1` and run the script with your specified values.

    **Basic Syntax**

    ```powershell
      .\disableTls.ps1 [Required Parameters]
    ```

    **Required Parameters**

    | Parameter | Description |
    | --- | --- |
    | `-mccRunTimeAccount` | The account that runs the Connected Cache software. This should be a PowerShell variable containing the username of the account you intend to designate as the Connected Cache runtime account. For example, `$User = "LocalMachineName\Username"` for a local user account. If you're using a Group Managed Service Account (gMSA), it should be formatted as `"Domain\Username$"`. |
    | `-mccLocalAccountCredential` | A PowerShell credential object for the Connected Cache runtime account. **This is only needed if you're using a local user account, domain user account, or service account**. For example, `$myLocalAccountCredential = Get-Credential`. |

    Note

    The `-mccRunTimeAccount` parameter is available in Connected Cache Windows application **v1.0.26.0** and later. If you're using the earlier **v1.0.24.0** application, use `-RunTimeAccountName` for local user, domain user, and service accounts, or `-RunTimeAccount` for Group Managed Service Accounts (gMSA).

    **Example**

    ```powershell
      .\disableTls.ps1 `
        -mccRunTimeAccount $myLocalAccountCredential.Username `
        -mccLocalAccountCredential $myLocalAccountCredential `
    ```
3. Validate that the disable process completed successfully.
4. After HTTPS is disabled, HTTP requests should work while HTTPS requests should fail. See the [HTTPS on Windows validation page](mcc-ent-https-windows-validation) for instructions on how to test this.
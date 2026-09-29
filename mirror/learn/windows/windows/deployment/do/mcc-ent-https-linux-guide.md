---
layout: Conceptual
title: Configure HTTPS Support for Linux | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/deployment/do/mcc-ent-https-linux-guide
recommendations: true
adobe-target: true
ms.collection:
- tier2
breadcrumb_path: /windows/resources/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-Windows
feedback_system: Standard
feedback_product_url: https://support.microsoft.com/windows/send-feedback-to-microsoft-with-the-feedback-hub-app-f59187f8-8739-22d6-ba93-f66612949332
description: Details on how to configure HTTPS support for Microsoft Connected Cache for Enterprise and Education cache nodes on Linux.
ms.service: windows-client
ms.subservice: itpro-updates
ms.topic: how-to
manager: naengler
ms.author: adityamiddha
author: adityamiddha
ms.date: 2026-06-24T00:00:00.0000000Z
ai-usage: ai-assisted
locale: en-us
document_id: 149ca727-a549-dd15-83cd-d93d4c0fd0c9
document_version_independent_id: 149ca727-a549-dd15-83cd-d93d4c0fd0c9
original_content_git_url: https://github.com/MicrosoftDocs/windows-docs-pr/blob/live/windows/deployment/do/mcc-ent-https-linux-guide.md
site_name: Docs
depot_name: TechNet.win-deployment
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/TechNet.win-deployment/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: do/mcc-ent-https-linux-guide
moniker_range_name: 
monikers: []
item_type: Content
source_path: windows/deployment/do/mcc-ent-https-linux-guide.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/a3955c7b-f5ee-420d-aff5-d7119738f38b
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/b31948f4-2f38-404b-ac93-c3c8c5b3ae33
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: fa590920-a76d-c538-0c42-b03afcdbe6f5
---

# Configure HTTPS Support for Linux | Microsoft Learn

This article provides step-by-step instructions for enabling HTTPS support on Microsoft Connected Cache for Enterprise nodes running on a Linux host machine.

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

    ```bash
    sudo ss -tulpn | grep :443
    ```

    Review the output:

    - **No output** — Port 443 isn't in use. Proceed with HTTPS setup.
    - **Output contains `LISTEN`** (for example, `tcp LISTEN 0 128 0.0.0.0:443 0.0.0.0:* users:(("nginx",pid=1234,fd=6))`) — Port 443 is already in use by another service. Identify and stop the conflicting service before Connected Cache can use port 443.

    Tip

    The `ss` output shows the process name and PID in the last column. In the example above, `nginx` (PID 1234) is using port 443. Stop or reconfigure the conflicting service before continuing. For example, run `sudo systemctl stop nginx` to stop nginx.
- **Verify firewall configuration**

    If your firewall or corporate proxy intercepts HTTPS traffic to your Connected Cache server (for example, via TLS inspection), certificate validation will always fail regardless of certificate configuration.

For more information on any of the prerequisites, see the [HTTPS on Linux reference page](mcc-ent-https-linux-reference).

## Generate a Certificate Signing Request (CSR)

Important

Each cache node needs its own CSR/certificate (cannot share):

- Use consistent naming: mcc-node1.company.com, mcc-node2.company.com, etc.
- Document which certificate belongs to which node
- **Wildcard certificates will not work**. The CSR/certificate used for HTTPS connection to Connected Cache is uniquely tied to each cache node for security purposes.

1. Open a terminal and navigate to the folder containing the extracted deployment package.
2. Add execute permissions to the CSR generation script:

    ```bash
    sudo chmod +x ./generateCsr.sh
    ```
3. Configure the parameters for `generateCsr.sh` and run the script with your specified values.

    **Basic Syntax**

    ```bash
    sudo ./generateCsr.sh [Required Parameters] [Subject Parameters] [SAN Parameters]
    ```

    **Required Parameters**

    | Parameter | Type | Description |
    | --- | --- | --- |
    | `-algo` | String | Certificate algorithm: `RSA`, `EC`, `ED25519`, or `ED448` |
    | `-keySizeOrCurve` | String | For RSA: key size (`2048`, `3072`, `4096`). For EC: curve name (`prime256v1`, `secp384r1`) |
    | `-csrName` | String | Name for the generated CSR file |

    **Subject Parameters**

    | Parameter | Required | Description | Example |
    | --- | --- | --- | --- |
    | `-subjectCommonName` | Yes | Common name for the certificate | `"localhost"`, `"example.com"` |
    | `-subjectCountry` | No | Two-letter country code | `"US"`, `"CA"`, `"GB"` |
    | `-subjectState` | No | State or province | `"WA"`, `"TX"`, `"Ontario"` |
    | `-subjectOrg` | No | Organization name | `"MyCompany"`, `"ACME Corp"` |

    Warning

    The Subject Alternative Name (SAN) configuration is critical for certificate validation. Your certificate must match exactly how clients connect to your Connected Cache, otherwise the clients bypass the cache node.

    For example, if your clients connect via IP address `192.168.1.100` but your certificate only has `-sanDns "server.local"`, certificate validation fails.

    **SAN Parameters (at least one required)**

    | Parameter | Description | Example |
    | --- | --- | --- |
    | `-sanDns` | DNS names (comma-separated) | `"localhost,example.com,api.example.com"` |
    | `-sanIp` | IP addresses (comma-separated) | `"127.0.0.1,192.168.1.100"` |
    | `-sanUri` | URIs (comma-separated) | `"https://example.com,http://localhost"` |
    | `-sanEmail` | Email addresses (comma-separated) | `"admin@example.com,user@domain.com"` |
    | `-sanRid` | Registered IDs (comma-separated) |  |
    | `-sanDirName` | Directory names (comma-separated) |  |
    | `-sanOtherName` | Other names (comma-separated) |  |

    For more detail and scenario-based examples on CSR script parameters, see the [HTTPS on Linux reference page](mcc-ent-https-linux-reference).
4. Validate that the CSR generation process completed successfully.

    If you encounter errors, locate the timestamped `GenerateCsr.log` file in the folder specified in the script output. Look for the output line that starts with "You can find logs here: ..."

    - **File format:** GenerateCsr\_YYYYMMDD-HHMMSS.log
    - **Example:** GenerateCsr\_20251201\_143022.log is a file created December 1, 2025 at 2:30:22 PM
5. Locate the generated CSR file in your **Certificates folder** on your host machine and transfer it if necessary.

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

    ```bash
    grep "BEGIN CERTIFICATE" xxxx.crt
    ```

    Expected successful output:

    ```bash
    -----BEGIN CERTIFICATE-----
    ```
4. Move your signed certificate to the **Certificates folder** on your Linux host machine.

    This will be the same folder where you initially found your CSR after it generated.

Caution

Do not share private keys, Connected Cache only requires the signed certificate.

## Import signed TLS certificate

1. Open a terminal and navigate to the location of the Connected Cache installer.
2. Add execute permissions to the certificate import script:

    ```bash
    sudo chmod +x ./importCert.sh
    ```
3. Configure the parameters for `importCert.sh` and run the script with your specified values.

    **Basic Syntax**

    ```bash
    sudo ./importCert.sh [Required Parameters]
    ```

    **Required Parameters**

    | Parameter | Type | Description |
    | --- | --- | --- |
    | `-certName` | String | Complete filename of your signed TLS certificate (with or without .crt extension) |

    **Example**

    ```bash
    sudo ./importCert.sh -certName "myTlsCert.crt"
    ```
4. Validate that the import process completed successfully.

    If you encounter errors, locate the timestamped `ImportCert.log` file in the folder specified in the script output. Look for the output line that starts with "You can find logs here: ..."

    - **File format:** ImportCert\_YYYYMMDD-HHMMSS.log
    - **Example:** ImportCert\_20251201\_143022.log is a file created December 1, 2025 at 2:30:22 PM
5. Verify that the correct certificate was imported by running the `ShowCertDetails.sh` script.

    Note

    The `ShowCertDetails.sh` script is available starting with Linux deployment package v1.10.

    Add execute permissions to the script:

    ```bash
    sudo chmod +x ./ShowCertDetails.sh
    ```

    Run the script:

    ```bash
    sudo ./ShowCertDetails.sh
    ```

    This script displays the certificate thumbprint and expiration date for the TLS certificate currently imported to the cache node.

For instructions on how to further validate the certificate import, see the [HTTPS on Linux validation page](mcc-ent-https-linux-validation).

## Disable HTTPS support

If you need to revert your Connected Cache to HTTP-only communication, follow these steps. This process won't delete anything in the Certificates folder - CSR files, certificates, or logs.

1. On your Linux host, open a terminal and navigate to the folder containing the extracted deployment package.
2. Add execute permissions to the TLS disable script:

    ```bash
    sudo chmod +x ./disableTls.sh
    ```
3. Run the disable script (no parameters required):

    ```bash
    sudo ./disableTls.sh
    ```
4. Validate that the disable process completed successfully.
5. After HTTPS is disabled, HTTP requests should work while HTTPS requests should fail. See the [HTTPS on Linux validation page](mcc-ent-https-linux-validation) for instructions on how to test this.
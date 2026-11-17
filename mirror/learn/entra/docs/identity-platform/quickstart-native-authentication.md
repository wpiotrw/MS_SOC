---
layout: Conceptual
title: 'Quickstart: Sign in with Embedded native authentication - Microsoft identity platform | Microsoft Learn'
canonicalUrl: https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-native-authentication
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: /entra/identity-platform/developer-support-help-options
author: cilwerner
ms.author: cwerner
ms.service: identity-platform
description: Configure the React Next.js sample for Embedded native authentication with the JavaScript SDK and CORS at a tenant-verified custom-domain edge.
ms.topic: quickstart
ms.custom: msecd-doc-authoring-1030
ms.date: 2026-11-13T00:00:00.0000000Z
ai-usage: ai-generated
locale: en-us
document_id: feab9dde-5587-6187-86da-e91c6960b29e
document_version_independent_id: feab9dde-5587-6187-86da-e91c6960b29e
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/identity-platform/quickstart-native-authentication.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: identity-platform/quickstart-native-authentication
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/identity-platform/quickstart-native-authentication.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5287f575-02f0-405f-92b7-800456526b0c
- https://authoring-docs-microsoft.poolparty.biz/devrel/5f286262-a4cb-47f4-92d3-dc24f172492b
- https://authoring-docs-microsoft.poolparty.biz/devrel/1e31b9be-b6e9-4221-a20b-d1460dbd5dfa
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/06e86142-34c2-4b94-ab9c-9477c21f7152
- https://authoring-docs-microsoft.poolparty.biz/devrel/90571f66-8410-4272-8117-79ce87fc2dcc
- https://authoring-docs-microsoft.poolparty.biz/devrel/8d63a4c4-4889-43b4-a98e-8e50dbfdb083
platformId: bdbb6f3a-a64c-3270-435a-e5bc080fe0b2
---

# Quickstart: Sign in with Embedded native authentication - Microsoft identity platform | Microsoft Learn

**Applies to**: ![Green circle with a white check mark symbol that indicates the following content applies to external tenants.](../external-id/media/common/applies-to-yes.png) External tenants ([learn more](/en-us/entra/external-id/tenant-configurations))

**Authentication approach:** Embedded native authentication.

In this quickstart, you configure a React Next.js sample for Embedded native authentication with Microsoft Authentication Library (MSAL) for JavaScript 5.29.0. The email-and-password journey uses a tenant-verified custom domain with Cross-Origin Resource Sharing (CORS) at the edge.

Important

The Native Authentication API V2 is in preview. The [Native Authentication API V1](reference-native-authentication-api-v1) remains generally available. See the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) for legal terms that apply to preview features.

## Prerequisites

- An external tenant and a public client application configured for Embedded native authentication. Complete [Configure an application](how-to-native-authentication-configure-app).
- A tenant-verified custom domain, the application ID, and the directory tenant GUID.
- CORS at the custom-domain edge configured for the sample's browser origin, `http://localhost:3000`. Apply the [shared proxy contract](concept-native-authentication-cors#proxy-contract) for origins, preflight, SDK headers, and success and error responses.
- A customer account with email and password. If tenant policy requires multifactor authentication (MFA), prepare an enabled email or SMS factor for this sample journey.
- Node.js 20.9.0 or later, npm, Git, and a code editor.
- Port 3000 available for the application.

## Get the sample

The sample has a unified launcher for V1 and V2. Use the pinned revision and SDK version below to follow this quickstart:

1. Clone the repository, check out the sample revision, and open its React Next.js application:

    ```bash
    git clone https://github.com/Azure-Samples/ms-identity-ciam-native-javascript-samples
    cd ms-identity-ciam-native-javascript-samples
    git checkout --detach 49c4e250a1e6eb97e2b813e9fce6670c996a2808
    cd typescript/native-auth/react-nextjs-sample
    ```
2. Install the exact SDK version with the sample dependencies:

    ```bash
    npm install --save-exact "@azure/msal-browser@5.29.0"
    ```

## Configure the application

Use `https://<tenant-verified-custom-domain>/<tenant-GUID>` for both the service authority and the SDK API transport base in this edge route. Keep opaque absolute HAL links for that authority unchanged. Don't add a client secret to browser configuration.

1. Open `src/config/auth-config.ts`.
2. Replace `Enter_the_Application_Id_Here` with the application ID.
3. Replace the complete `auth.authority` value with `https://<tenant-verified-custom-domain>/<tenant-GUID>`, substituting your verified hostname and tenant GUID.
4. Add `auth.knownAuthorities` as an array containing the verified hostname, without a scheme or path.
5. Set the required `customAuth.authApiProxyUrl` string to the same full `https://<tenant-verified-custom-domain>/<tenant-GUID>` authority. Include the tenant GUID in both SDK URL settings.
6. Save the configuration file. The V2 sample uses the SDK's default scopes without custom claims. MFA requirements come from your tenant policy, not from selecting V2.

## Run the sample

Run the application from the sample directory. This custom-domain edge configuration doesn't use the sample's local CORS proxy:

1. Start the application:

    ```bash
    npm run dev
    ```
2. Open `http://localhost:3000` in a browser and select **V2**. Keep the application process running while you test.

## Sign in the test customer

Use the sample's unified launcher to test only methods enabled for the current transaction.

1. Enter the test customer's email address and select **Sign In**.
2. If the service offers multiple first-factor methods, select the password method. Enter the password when requested and select **Sign In**.
3. If the service requests MFA, select a returned email or SMS method and enter its verification code.
4. Confirm that the sample reports completed sign-in. Don't expose tokens in screenshots, logs, or support output.

Email one-time passcode sign-in uses a customer account and user flow configured for that method. This quickstart follows the email-and-password journey.

## Clean up the session

End the local test without deleting shared tenant configuration.

Signing out of the sample doesn't terminate other application or browser sessions.

1. Sign out of the sample and clear the account-related application UI.
2. Stop the application process in its terminal.
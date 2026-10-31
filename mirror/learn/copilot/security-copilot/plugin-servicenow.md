---
layout: Conceptual
title: ServiceNow plugin for Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-servicenow
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn how to use the ServiceNow plugin for Microsoft Security Copilot.
ms.date: 2025-08-17T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: concept-article
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom: 
ms.reviewer: shivanpatel
search.audiencetype: Admin
locale: en-us
document_id: 30d4d1b7-6c30-c808-8892-fa60f7867e24
document_version_independent_id: 30d4d1b7-6c30-c808-8892-fa60f7867e24
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-servicenow.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-servicenow
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-servicenow.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 460ed1bc-0a60-42f3-6c3f-c4f5728494d2
---

# ServiceNow plugin for Microsoft Security Copilot | Microsoft Learn

Important

Some information in this article relates to a prereleased product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

ServiceNow is an enterprise app ecosystem designed to connect and automate business processes, delivered as a SaaS application. Many security operation centers (SOCs) use ServiceNow as part of their incident management flow, and often extend the core functionality with customizations, integrations, and security-specific applications.

The Copilot for Security plugin for ServiceNow enables connectivity between a Security Copilot session and a ServiceNow incident queue. Users can import a ServiceNow incident into Copilot for Security. Users can easily correlate data from Microsoft security products such as Defender for Endpoint, enrich with external threat intelligence, and persist the results of their investigation in ServiceNow. These capabilities, combined with the narrative prompt and generative AI powered by Azure OpenAI help speed incident resolution. These capabilities also help up-skill team members, and provide more comprehensive views into any security incident.

## Know before you begin

### Prerequisites

- Supported Products (Cloud):
    - ServiceNow IT Service Management (ITSM) package – Incident Response application
    - ServiceNow Security Operations (SecOps) package – Security Incident Response application
- Access to your ServiceNow instance, with permissions to create new users
- Permissions to set up plugins
- Available ServiceNow API quota

### ServiceNow setup

There are two connectivity methods to ServiceNow:

- OAuth authorization code grant flow
- HTTP Basic auth

Choose the one that suits your needs.

#### OAuth authorization code grant flow (ServiceNow inbound integration) - Recommended

Note

Before you begin, ensure you have the ServiceNow admin permission and the Security Copilot Owner or Contributor permission.

1. Make sure the [OAuth plugin](https://www.servicenow.com/docs/bundle/yokohama-platform-security/page/administer/security/task/t_ActivateOAuth.html) is active and the [OAuth activation property](https://www.servicenow.com/docs/bundle/yokohama-platform-security/page/administer/security/task/t_SetTheOAuthProperty.html) is set to true. Follow the links to activate both if they aren't activated by default.
2. Access your ServiceNow instance and create a new Application Registry object by following these steps:

    1. Navigate to **System OAuth &gt; Application Registry**, select **New**.
    2. Select **Create an OAuth API endpoint for external clients**.

        ![Image of what kind of OAuth application](media/oauth-application.png)
    3. Enter a name that identifies the Security Copilot integration.
    4. Enter the redirect URI corresponding to the Security Copilot instance, for example `https://securitycopilot.microsoft.com/auth/v1/callback`.
    5. Assign an auth scope corresponding to your access control needs. The user account scope would suffice.
    6. Save the Application Registry object.
    7. From the newly created object, note the client ID and client secret.
    8. This OAuth setup should only be done once per ServiceNow instance. The resulting OAuth Application Registry object can be used multiple times by different users.

#### HTTP Basic auth

1. Access your ServiceNow instance and locate the option to create a new user:

    1. Navigate to **Discovery &gt; Credentials** in the ServiceNow platform.
    2. Select **New** to create a new credential record.
    3. Select **Basic Auth**as the credential type. Enter the following details:
        1. **Name:** Descriptive name for the credential.
        2. **Username:** Username for authentication.
        3. **Password:** Password for authentication.
        4. Save the credentials.
2. Assign the `itil` and `rest_api_explorer` roles to the username:

    1. Navigate to **User Administration &gt; Users**.
    2. Search for and select the username created.
    3. In the **Roles** related list, select **Edit**.
    4. Add `itil` and `rest_api_explorer` roles from the available roles list.
    5. Save the role assignments.
3. Note the credentials and the ServiceNow instance URL.

### Security Copilot connection

1. Sign in to [Microsoft Security Copilot](https://securitycopilot.microsoft.com/).
2. Access **Manage Plugins** by selecting the **Sources** button from the prompt bar.

    ![Image of setting up ServiceNow in manage resources panel](media/manage-sources-snow-plugin.png)
3. Next to **ServiceNow**, select **Set up**.

    ![Image of setting up ServiceNow part 1](media/service-now-settings-1.png)

    Note

    Be sure to scroll all the way down to reach other fields such as Scopes.

    ![Image of setting up ServiceNow part 2](media/service-now-settings-1.png)
4. Grant consent to the Security Copilot application so that you can access your ServiceNow instance.

    ![Image of granting consent to connection.](media/service-now-instance.png)
5. OAuth authorization\_code instructions

    1. Enter auth parameters corresponding to the Application Registry object you created earlier.
    2. The instance URL, client ID, and client secret correspond to values of the same name in the Application Registry object. To determine what to enter for each value, refer to the following table:

    | Setting name | Description | Example |
    | --- | --- | --- |
    | Default Incident Type | Incident type to default to when the type isn't provided within prompts. Must be one of: INC or SIR | INC or SIR |
    | Instance | Set to the ServiceNow instance URL | `https://xyz.service-now.com/` |
    | ClientId | Set to client ID in ServiceNow Application Registry object |  |
    | ClientSecret | Set to client secret in ServiceNow Application Registry object |  |
    | AuthorizationEndpoint | Set to `https://<service-now-instance-domain>/oauth_auth.do`. | `https://xyz.service-now.com/` oauth\_auth.do |
    | TokenEndpoint | Set to `https://<service-now-instance-domain>/oauth_token.do.` | `https://xyz.service-now.com/` oauth\_token.do |
    | Scopes | Set to the scopes defined in the ServiceNow Application Registry object. Comma-separate multiple scopes. | user account |
    | AuthorizationContentType | Should be left unchanged from default application/x-www-form-urlencoded | application/x-www-form-urlencoded |
    | Resource | Resource ID | Can be left blank |
6. Select **Save** or **Connect** to complete the setup.

    Note

    Currently, the system doesn't validate your credentials when you save your settings. If they aren't correct, you'll see an error later when Security Copilot attempts to invoke the ServiceNow plugin.
7. Close the plugins window.

## Sample ServiceNow prompts

Security Copilot operates primarily with natural language prompts. When you're ready to load an incident into your Security Copilot session or search for related ServiceNow incidents, you'll submit a prompt that guides Security Copilot to select the ServiceNow skill set and invoke the proper skill.

When you word your prompt, ensure you mention ServiceNow as the preferred source of your incident. Security Copilot can connect to several systems that each provide incidents, and it benefits from guidance on which source you prefer.

### Example prompts for incident queries:

- "Load ServiceNow incident INC12345"
- "What ServiceNow incidents refer to IP address 10.0.0.1?"
- "Show me recent high severity ServiceNow incidents"
- "Show details on the third incident"
- "What is the MDTI reputation score for those IP addresses?"
- "Write a link to this Copilot investigation to ServiceNow incident INC12345"
- "Write the following text to that ServiceNow incident: Investigated with Security Copilot and deployed new detection logic."
- "Write a summary of this investigation to ServiceNow incident INC12345"
- "Summarize this investigation and write it as a comment on the ServiceNow incident."

#### Appending comments to ServiceNow incidents

If enabled with appropriate permissions, the ServiceNow connector can append comments to ServiceNow incidents. The comment text can be provided by the user, or sourced from Security Copilot features, such as session sharing links or pinned prompt investigation summaries.

Example prompts include:

- "Write a link to this Copilot investigation to ServiceNow incident INC12345"

*After loading an incident:*

- "Write the following text to that ServiceNow incident: Investigated with Security Copilot and deployed new detection logic."

*After pinning a few prompts:*

- "Write a summary of this investigation to ServiceNow incident INC12345" or if the session is already loaded "Summarize this investigation and write it as a comment on the ServiceNow incident."

Note

The current version of the plugin appends comments to the ServiceNow incident. Future versions may provide the option of writing to the work notes instead.

## Troubleshoot the ServiceNow plugin

Ensure the relevant IPs for your region from the following list are allowed. For more information, see [Egress IP addresses for Microsoft Security Copilot](/en-us/copilot/security/plugin-ip-address).

Steps to add Allowed IPs:

1. Sign in to your ServiceNow Instance:

    - Use an account with administrative privileges.
2. Navigate to the IP Access Control Settings. ServiceNow documentation on the steps: [IP Address Access Control](https://www.servicenow.com/docs/bundle/washingtondc-platform-security/page/administer/login/task/t_AccessControl.html):

    - In the left navigation pane, search for "IP Access Control" or go to: **System Security &gt; IP Access Control**

    Review the IP addresses from this list and select the appropriate one for your region and add it to the allowlist with direction Type as inbound:

    ![Image of IP range based authentication](media/service-now-ip-range.png)

### Errors occur

If you encounter errors, such as *Couldn't complete your request*, or *An unknown error occurred*, make sure the plugin is turned on. If the issue persists, sign out of Security Copilot, and then sign back in.

### Prompts aren't invoking the correct capabilities

If prompts aren't invoking the correct capabilities, or prompts are invoking some other capability set, you might have custom plugins or other plugins that have similar functionality as the capability set you want to use. You can either use the product name ServiceNowSIR in your prompts, or type the name of a specific capability, like &lt;&gt; instead.

## Provide feedback

To provide feedback, contact ServiceNow product management.
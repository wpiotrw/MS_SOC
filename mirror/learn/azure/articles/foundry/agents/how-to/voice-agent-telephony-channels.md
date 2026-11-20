---
layout: Conceptual
title: Integrate telephony channels with a voice agent - Microsoft Foundry | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/voice-agent-telephony-channels
breadcrumb_path: ../../../breadcrumb/azure-ai/toc.json
feedback_help_link_url: https://learn.microsoft.com/answers/tags/133/azure
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/79b1327d-d925-ec11-b6e6-000d3a4f06a4
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure-ai-foundry
ms.suite: office
zone_pivot_group_filename: zone-pivots/azure-ai/zone-pivot-groups.json
author: sdgilley
learn_banner_products:
- azure
manager: mcleans
ms.author: sgilley
ms.collection: ce-skilling-ai-copilot
ms.update-cycle: 90-days
ms.service: microsoft-foundry
description: Use Teams Phone extensibility or Twilio with a Microsoft Foundry voice agent to receive phone calls and place outbound calls through the API.
ms.subservice: foundry-agent-service
ms.topic: how-to
ms.date: 2026-11-19T00:00:00.0000000Z
ms.custom: doc-kit-assisted
ai-usage: ai-assisted
zone_pivot_groups: voice-agent-telephony-method
locale: en-us
document_id: 2d94f0ca-2fbc-eb2d-4b9a-215b266545c8
document_version_independent_id: 709c89fd-73a3-f9b2-c770-98fac2c784bf
original_content_git_url: https://github.com/MicrosoftDocs/azure-ai-docs-pr/blob/live/articles/foundry/agents/how-to/voice-agent-telephony-channels.md
site_name: Docs
depot_name: Learn.azure-ai
page_type: conceptual
toc_rel: ../../toc.json
asset_id: foundry/agents/how-to/voice-agent-telephony-channels
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/foundry/agents/how-to/voice-agent-telephony-channels.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/64b65f6c-101f-411a-9b83-9f577fab52d0
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/b5267373-9b61-4d5a-a4ac-5d03f8f8800f
- https://authoring-docs-microsoft.poolparty.biz/devrel/54fcef21-b24a-4ef4-9c4a-a525c23ee9a3
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1a667fd1-8145-4b11-af0f-9f5de205a6e5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/bcd4f3ef-c612-47a8-aa4a-7f9bedc3a98c
- https://authoring-docs-microsoft.poolparty.biz/devrel/8ab60220-e56b-41ff-a8bf-45b8d7ab716f
platformId: e7238e76-94cc-920c-8b79-6dea2afe3253
---

# Integrate telephony channels with a voice agent - Microsoft Foundry | Microsoft Learn

Use [Teams Phone extensibility (TPE)](/en-us/azure/communication-services/concepts/interop/tpe/teams-phone-extensibility-overview) or Twilio to connect a phone number to your Microsoft Foundry voice agent. Receive inbound calls and place outbound calls through the call-job API.

Use **Choose a configuration method** at the top of this article to select your interface. Then select your provider in the tabs below. Your provider selection applies throughout the article. For SIP connectivity, see [Connect a voice agent through SIP](voice-agent-telephony-channels-sip).

For complete examples, follow the [inbound support workflow](voice-agent-system-tools#handle-an-inbound-support-call) or the [outbound reminder workflow](voice-agent-outbound-calls).

Voice agents are generally available, with some features still in preview. See [General availability and preview features](../overview#general-availability-and-preview-features).

Caution

Teams Phone extensibility and Twilio telephony channels aren't currently supported for voice agents in network-isolated projects, such as projects that use virtual network injection or a Foundry resource with public network access disabled.

## Prerequisites

- A saved voice-based agent in a Foundry project that passes browser testing. See [Quickstart: Create a voice-based prompt agent](../quickstarts/prompt-voice-agent).
- [Foundry User role](../../concepts/rbac-foundry) on the project, to create and manage telephony bindings.

    Important

    The Foundry RBAC roles were recently renamed. **Foundry User**, **Foundry Owner**, **Foundry Account Owner**, and **Foundry Project Manager** were previously named Azure AI User, Azure AI Owner, Azure AI Account Owner, and Azure AI Project Manager. You might still see the previous names in some places while the rename rolls out. The role IDs and core permissions are unchanged by the rename.
- Permission to update the agent and its channels, manage project connections, and create or update telephony bindings.

::: zone pivot="azd"

- Azure Developer CLI (`azd`) version 1.37.0 or later and the `azure.ai.agents` extension version 1.2.0 or later. See [Install the Azure Developer CLI Foundry extensions](install-cli-foundry-extensions).
- The `azd` project and environment that deploy your voice agent. The voice service uses `host: azure.ai.agent` and `kind: voice` or `kind: prompt-voice`. To create one, follow the [Azure Developer CLI quickstart](../quickstarts/prompt-voice-agent?pivots=azd).

::: zone-end

# [Teams Phone extensibility](#tab/teams-phone)
### Teams Phone extensibility prerequisites

For the Teams Phone extensibility path, you need:

- A Teams Phone service number assigned to a resource account. See [Get Microsoft Teams Calling Plan phone numbers for your tenant](/en-us/microsoftteams/getting-phone-numbers-for-your-users).
- The setup in Prepare Teams Phone extensibility, completed with a Teams or Microsoft 365 administrator.
- Access to the selected Azure Communication Services resource.
- For inbound calls, Event Grid write permission on that resource.
- Help from a tenant administrator when secure webhook setup requires Microsoft Entra application or app-role changes.

The current project-managed-identity flow requires the Foundry project and Azure Communication Services resource to be in the same Microsoft Entra tenant.

# [Twilio](#tab/twilio)
### Twilio prerequisites

For the Twilio path, you need:

- A [Twilio](https://www.twilio.com/phone-numbers) account with at least one active, voice-capable phone number for inbound calls.
- A Twilio project connection, or the **Account SID** and **Primary Auth Token** to create one.

Twilio doesn't require an Azure Communication Services resource, Teams resource account, or Event Grid subscription. Store the Auth Token in the project connection, not in binding requests, logs, screenshots, or support requests.

---

## Compare the channel integrations

Choose the provider that owns your number.

| Path | Use it when | What you provide in Foundry |
| --- | --- | --- |
| Teams Phone extensibility | Your organization owns a service number in Teams and routes it through a Teams resource account to Azure Communication Services. | An Azure Communication Services project connection and the resource-account object ID as a GUID, without the `28:orgid:` prefix. |
| Twilio | Your organization owns one or more active voice-capable numbers in Twilio. | An existing Twilio project connection, or the Account SID and Primary Auth Token for a new connection. |

The Twilio option appears only in supported public-cloud environments.

::: zone pivot="azd"

In `azure.yaml`, the Teams identifier includes the `28:orgid:` prefix. The CLI converts it to the GUID required by the API. See Connect a number with Azure Developer CLI.

::: zone-end

## Understand the call path

The channel integration determines how an inbound call reaches the agent.

```text
Caller
  -> Teams resource-account number or Twilio number
  -> telephony provider
  -> Foundry project telephony endpoint
  -> telephony binding
  -> voice-based agent
```

# [Teams Phone extensibility](#tab/teams-phone)
For Teams Phone extensibility, your Teams tenant keeps ownership of the number and Azure Communication Services provides the call automation and media path:

1. A caller dials the Teams phone number.
2. Teams routes the call to your resource account.
3. The resource account routes the call to your Communication Services resource.
4. Communication Services raises a `Microsoft.Communication.IncomingCall` event through Event Grid to your agent's telephony callback endpoint.
5. Foundry matches the callee to a telephony binding, answers the call on your Communication Services resource, and streams the audio to the agent.

Because the Teams number stays in Teams, the agent can act as one destination among others in your existing call flow. You can leave auto attendants and call queues in place and route selected paths to the agent.

# [Twilio](#tab/twilio)
For Twilio, Foundry uses the selected project connection to discover the numbers in your Twilio account and create a binding for each number you select. You don't create an Azure Communication Services resource or Event Grid subscription for the Twilio path.

---

## Set up your preferred interface

Use **Choose a configuration method** at the top of this article to select **Foundry portal**, **Python SDK**, **REST API**, or **Azure Developer CLI**. The Python examples share a client and variables across sections.

::: zone pivot="foundry-portal"

Open your project in the [Foundry portal](https://ai.azure.com). You don't need the Python packages or a manually acquired bearer token for the portal steps.

::: zone-end

::: zone pivot="python"

Use Python 3.10 or later and install the packages:

```bash
python -m pip install "azure-ai-projects>=2.11.0" azure-identity
```

For local development, sign in with `az login` before using `DefaultAzureCredential`. Replace the endpoint and agent name, then run this setup once in your Python session:

```python
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

endpoint = "https://<account>.services.ai.azure.com/api/projects/<project>"
agent_name = "my-voice-agent"
credential = DefaultAzureCredential()
project_client = AIProjectClient(endpoint=endpoint, credential=credential)
telephony = project_client.voice_agents.telephony
```

Reference: [AIProjectClient](/en-us/python/api/azure-ai-projects/azure.ai.projects.aiprojectclient) | [DefaultAzureCredential](/en-us/python/api/azure-identity/azure.identity.defaultazurecredential).

The client uses `api-version=v1`. Teams Phone extensibility and Twilio operations don't need a preview opt-in. To use SIP features, which are in preview, create the client with `allow_preview=True` so that it sends `Foundry-Features: VoiceAgents=V1Preview`.

Examples that need response headers use the `cls` callback to return the model and raw HTTP headers together. After running the examples you need, close `project_client` and `credential` with their `close()` methods.

::: zone-end

::: zone pivot="rest"

1. Sign in with the Azure CLI and obtain a Microsoft Entra access token:

    ```azurecli
    az login
    az account get-access-token --scope https://ai.azure.com/.default --query accessToken -o tsv
    ```
2. Replace `{projectEndpoint}` with your Foundry project endpoint and `{agentName}` with the voice agent's name. Use the token as `<access-token>` in the `Authorization: Bearer <access-token>` header.
3. The examples use `api-version=v1`. Teams Phone extensibility and Twilio requests don't need a preview opt-in. Send `Foundry-Features: VoiceAgents=V1Preview` for SIP binding, call, and call-job writes, and when configuring SIP transfer destinations. All campaign operations require that opt-in.

::: zone-end

::: zone pivot="azd"

Run the commands from the directory that contains your project's `azure.yaml`. Check that the CLI and agent extension meet the version requirements:

```azurecli
azd version
azd ai agent version
```

Reference: [Verify the Foundry extensions](install-cli-foundry-extensions#verify-the-installation).

Sign in and select the existing environment that contains your voice agent. Replace `<environment-name>` with that environment's name:

```azurecli
azd auth login
azd env select <environment-name>
```

Reference: [azd auth login](/en-us/azure/developer/azure-developer-cli/reference#azd-auth-login) | [azd env select](/en-us/azure/developer/azure-developer-cli/reference#azd-env-select).

This workflow deploys inbound bindings declared in your voice service. Use Python or REST for outbound jobs, live-call operations, and independent binding management. Teams Phone extensibility and Twilio bindings don't require a voice preview opt-in with these extension versions.

::: zone-end

## Configure a provider connection

Use a project connection for your provider. The portal number setup flow can create it for you. For CLI, SDK, or REST requests, create or select the connection first.

# [Teams Phone extensibility](#tab/teams-phone)
### Prepare Teams Phone extensibility

A Teams or Microsoft 365 administrator usually completes these steps.

1. Follow [Teams Phone System extensibility quick start](/en-us/azure/communication-services/quickstarts/tpe/teams-phone-extensibility-quickstart) to provision the application, bot, resource account, and Azure Communication Services association.
2. Create or select the Azure Communication Services resource that receives calls for the resource account.
3. Create the Teams resource account with the Phone Extensibility application ID.
4. Associate the resource account with the Azure Communication Services resource, and synchronize the resource account.
5. Acquire a Teams service number and assign it to the resource account. The number can use Calling Plan, Operator Connect, or Direct Routing according to your Teams telephony configuration.
6. Assign the **Microsoft Teams Phone Resource Account** license when required.
7. Provide Azure Communication Services server consent for the exact tenant and resource-account object ID.
8. For inbound calls, place a controlled call and confirm that Azure Communication Services emits `Microsoft.Communication.IncomingCall`.

Provide the Foundry owner with the callable Teams number, Azure Communication Services ARM resource ID, and resource-account object ID. For inbound setup, also confirm that Azure Communication Services received the test call.

### Create a connection to Communication Services

For Teams, use the category `AzureCommunicationServices`. Set `target` to the resource's HTTPS endpoint, such as `https://<resource-name>.communication.azure.com`, not its Azure resource ID. Store the matching resource ID in `ResourceId` metadata.

Choose an authentication type supported by the connection:

| Authentication | `authType` | What you provide |
| --- | --- | --- |
| Project managed identity | `ProjectManagedIdentity` | Grant the project identity access to the Communication Services resource. |
| Account managed identity | `AccountManagedIdentity` | Grant the Foundry account identity access to the resource. |
| User-assigned managed identity | `RegistryIdentity` | Identity resource ID and client ID, with access to the resource. |
| Service principal | `ServicePrincipal` | Tenant ID, client ID, and client secret, with access to the resource. |
| Connection string | `CustomKeys` | The Communication Services connection string in the `connectionString` credential key. |

For a managed identity or service principal, grant the required Communication Services permissions before creating a binding or placing calls.

# [Twilio](#tab/twilio)
### Configure the Twilio project connection

For Twilio, use these settings:

| Setting | Value |
| --- | --- |
| `category` | `Twilio`. |
| `target` | Your Twilio Account SID, not a Twilio API URL or phone number. |
| `authType` | `ApiKey`. |
| Credential `key` | Your Twilio Primary Auth Token. |

---

Use the connection's name as `connection_name` in binding and outbound requests. Don't include provider credentials in those requests.

::: zone pivot="azd"

Use the existing project connection's name in the YAML `connection` field. The `telephony` declaration doesn't create a provider account, phone number, project connection, or Teams Event Grid subscription.

::: zone-end

## Understand telephony bindings

A binding routes inbound calls to one agent. You don't need a binding for outbound call jobs.

# [Teams Phone extensibility](#tab/teams-phone)
| Property | Purpose |
| --- | --- |
| `id` | Service-generated binding ID for later reads, updates, and deletion. |
| `provider` | `teams_phone_extensibility`. |
| `connection_name` | Foundry project connection name. Secrets stay in the connection. |
| `resource_account_object_id` | Required Teams resource-account GUID, without `28:orgid:`. |
| `phone_number` | Optional display phone number for the Teams resource account. |
| `label` | Optional display label. |
| `incoming_call_url` | Service-generated incoming-call delivery URL. |

# [Twilio](#tab/twilio)
| Property | Purpose |
| --- | --- |
| `id` | Service-generated binding ID for later reads, updates, and deletion. |
| `provider` | `twilio`. |
| `connection_name` | Foundry project connection name. Secrets stay in the connection. |
| `phone_number` | Required owned E.164 number. |
| `label` | Optional display label. |
| `incoming_call_url` | Service-generated incoming-call delivery URL. |

Creating a Twilio binding updates the number's voice URL and status callback, replacing its existing inbound voice routing. Use a number you want to route to this agent.

---

Create and list bindings at `{projectEndpoint}/agents/{agentName}/telephony/bindings`. Append `/{bindingId}` to read, update, or delete one. Use the latest ETag for conditional updates and deletion.

::: zone pivot="foundry-portal"

## Connect a number in the Foundry portal

Connect your number through the agent's **Phone numbers** channel.

### Open the phone-number channel

# [Teams Phone extensibility](#tab/teams-phone)
1. In Foundry, select **Build** &gt; **Agents**.
2. Select the voice-based agent.
3. Open **Channels**.
4. In **Phone numbers**, select **Add a number**.
5. Select **Microsoft Teams**.

# [Twilio](#tab/twilio)
1. In Foundry, select **Build** &gt; **Agents**.
2. Select the voice-based agent.
3. Open **Channels**.
4. In **Phone numbers**, select **Add a number**.
5. Select **Twilio**.

---

# [Teams Phone extensibility](#tab/teams-phone)
### Connect a Microsoft Teams number

The Teams Phone extensibility flow creates or updates the Azure Communication Services project connection and telephony binding. Depending on the secure-delivery option, Foundry can also configure the webhook application and IncomingCall Event Grid subscription.

#### Choose secure incoming-call delivery

When **Secure incoming-call delivery** is shown, choose the approved mode.

| Option | Use it when |
| --- | --- |
| **Automatic configuration (Recommended)** | Use when the tenant allows Foundry to create or update the webhook app, app-role assignments, and Event Grid subscription. |
| **Manual configuration** | Use an approved customer-managed application, or select an existing Event Grid and app-registration configuration. |

Under **Manual configuration**, choose the option that matches your setup:

- **Use a customer-managed app registration and let Foundry configure Event Grid**: Use a dedicated single-tenant application that you own, or ask an administrator to complete the changes.
- **Event Grid and app registration are already configured**: Use only when authenticated Event Grid delivery to the exact Foundry webhook is complete. Foundry skips that bootstrap work.

For a customer-managed application:

1. Select an eligible single-tenant app registration.
2. Enter any governance reference required by your organization.
3. If the application isn't listed, confirm that you're an owner and refresh.
4. Ask a tenant administrator to complete required API permissions and app-role assignments.

Never disable authentication to work around a webhook validation error.

#### Select Azure Communication Services

In **Azure Communication Services resource**, select the resource that receives the calls.

If it isn't listed:

- Confirm the tenant and subscription.
- Confirm you can read the resource.
- Confirm the expected resource provider is registered.
- Ask an Azure administrator to correct RBAC.

Foundry creates or updates the project connection to the Azure Communication Services endpoint and uses the project managed identity. Don't enter an Azure Communication Services key or connection string.

#### Enter the Teams number details

Enter the **Resource account object ID** that the Teams administrator provides. Foundry constructs:

```text
28:orgid:<resource-account-object-id>
```

# [Twilio](#tab/twilio)
### Connect a Twilio number

1. In **Phone numbers**, select **Add a number** &gt; **Twilio**.
2. Select a compatible existing Twilio connection. If none is available, select **Create a new Twilio connection**.
3. To create a connection, enter:
    - A unique **Connection name**.
    - The Twilio **Account SID**. It starts with `AC` and contains 34 characters.
    - The Twilio **Primary Auth Token**.
4. Select **Connect** or **Continue**.
5. Select one or more voice-capable phone numbers discovered from the Twilio account. You can't select numbers without the Voice capability.
6. Select **Continue**.
7. Review the agent, connection, masked Account SID, and selected numbers.
8. Optionally change the display label for each number.
9. Select **Add selected numbers**.
10. Review the result for each number. Retry any number that has a failed or unconfirmed result.
11. Select **Done** after all binding operations finish.

Foundry stores the Twilio credentials in the project connection and creates a separate telephony binding for each selected number.

If you don't find any voice-capable numbers, get a number in the Twilio Console and retry discovery.

---

### Manage a connected number

The **Phone numbers** card shows each connected number, its optional label, and its provider.

# [Teams Phone extensibility](#tab/teams-phone)
1. Open the number's actions menu.
2. Select **View details**.
3. Select **Edit** if the binding supports updates.
4. Update the displayed phone number or label. The resource-account object ID and connection are read-only.
5. Select **Save**.

# [Twilio](#tab/twilio)
1. Open the number's actions menu.
2. Select **View details**.
3. Select **Edit** if the binding supports updates.
4. Update the label. The phone number and connection are read-only.
5. Select **Save**.

---

::: zone-end

::: zone pivot="python"

## Connect a number with the Python SDK

Use the client from Set up your preferred interface and your provider connection. Prepare the request model for your selected provider, and then create the binding.

# [Teams Phone extensibility](#tab/teams-phone)
For **Teams Phone extensibility**, use your resource-account GUID. The phone number is optional display metadata.

```python
from azure.ai.projects.models import (
    TeamsPhoneExtensibilityTelephonyBinding,
)

binding_request = TeamsPhoneExtensibilityTelephonyBinding(
    connection_name="my-acs-connection",
    resource_account_object_id="aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
    phone_number="+12065550123",
    label="Support line",
)
```

Reference: [Azure AI Projects client library for Python](https://aka.ms/azsdk/azure-ai-projects-v2/python/code).

# [Twilio](#tab/twilio)
Use an owned, voice-capable E.164 number.

```python
from azure.ai.projects.models import TwilioTelephonyBinding

binding_request = TwilioTelephonyBinding(
    connection_name="my-twilio-connection",
    phone_number="+12065550123",
    label="Support line",
)
```

Reference: [Azure AI Projects client library for Python](https://aka.ms/azsdk/azure-ai-projects-v2/python/code).

---

After running the request-model snippet for your provider, create its binding:

```python
binding = telephony.create_binding(
    agent_name=agent_name,
    binding=binding_request,
)
binding_id = binding.id
print(binding_id, binding.incoming_call_url)
```

Reference: [Azure AI Projects client library for Python](https://aka.ms/azsdk/azure-ai-projects-v2/python/code).

Save `binding_id` for later requests.

# [Teams Phone extensibility](#tab/teams-phone)
Use `incoming_call_url` to register the Event Grid subscription.

# [Twilio](#tab/twilio)
Foundry configures the number's voice callbacks automatically.

---

To update the binding's label, read its latest ETag and pass it to `update_binding` with `MatchConditions.IfNotModified`:

```python
from azure.ai.projects.models import UpdateTelephonyBindingRequest
from azure.core import MatchConditions

binding, binding_headers = telephony.get_binding(
    agent_name=agent_name,
    binding_id=binding_id,
    cls=lambda response, result, _: (result, response.http_response.headers),
)
binding = telephony.update_binding(
    agent_name=agent_name,
    binding_id=binding_id,
    body=UpdateTelephonyBindingRequest(label="Customer support"),
    etag=binding_headers["ETag"],
    match_condition=MatchConditions.IfNotModified,
)
```

Reference: [Azure AI Projects client library for Python](https://aka.ms/azsdk/azure-ai-projects-v2/python/code) | [MatchConditions](/en-us/python/api/azure-core/azure.core.matchconditions).

Read the latest ETag before every update. The binding update rules apply to either interface.

::: zone-end

::: zone pivot="rest"

## Connect a number by using the API

Use your provider connection and the authentication headers from Set up your preferred interface.

### Create the binding

# [Teams Phone extensibility](#tab/teams-phone)
For **Teams Phone extensibility**, set `connection_name` to your ACS connection and `resource_account_object_id` to your Teams resource-account GUID. The optional `phone_number` is display metadata, not the routing identifier.

```http
POST {projectEndpoint}/agents/{agentName}/telephony/bindings?api-version=v1
Authorization: Bearer <access-token>
Content-Type: application/json

{
  "provider": "teams_phone_extensibility",
  "connection_name": "my-acs-connection",
  "resource_account_object_id": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
  "phone_number": "+12065550123",
  "label": "Support line"
}
```

# [Twilio](#tab/twilio)
Create the binding with your Twilio connection and number:

```http
POST {projectEndpoint}/agents/{agentName}/telephony/bindings?api-version=v1
Authorization: Bearer <access-token>
Content-Type: application/json

{
  "provider": "twilio",
  "connection_name": "my-twilio-connection",
  "phone_number": "+12065550123",
  "label": "Support line"
}
```

Reference: [Python telephony models](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/ai/azure-ai-projects/azure/ai/projects/models/_models.py).

---

Replace the example connection name, identifiers, and phone numbers with your values.

The service returns `201 Created`, the binding's `id` and `incoming_call_url`, and an `ETag` header. Save the binding ID.

# [Teams Phone extensibility](#tab/teams-phone)
Register the Event Grid subscription with the returned `incoming_call_url`.

# [Twilio](#tab/twilio)
Foundry configures the number's voice callbacks automatically.

---

### Read or update the binding

Read the binding to get its current properties and `ETag`:

```http
GET {projectEndpoint}/agents/{agentName}/telephony/bindings/{bindingId}?api-version=v1
Authorization: Bearer <access-token>
```

Use `PATCH` with `application/merge-patch+json` to update the binding. For example, change its display label:

```http
PATCH {projectEndpoint}/agents/{agentName}/telephony/bindings/{bindingId}?api-version=v1
Authorization: Bearer <access-token>
Content-Type: application/merge-patch+json
If-Match: <etag-from-latest-binding-read>

{
  "label": "Customer support"
}
```

Read the latest `ETag` before each update. Don't reuse an ETag after another change.

::: zone-end

::: zone pivot="azd"

## Connect a number with Azure Developer CLI

Add a binding to the existing voice service, then deploy that service. Deployment also applies the agent's local configuration, so review its model, instructions, and audio settings before continuing.

### Declare the binding

In `azure.yaml`, locate your voice service under `services`. Add `telephony` at the same indentation level as `kind`, `model`, and `name`.

Preserve the existing agent settings and any bindings you want to keep. For a service defined through `$ref`, edit its referenced definition instead.

# [Teams Phone extensibility](#tab/teams-phone)
Use `provider: acs` and prefix your Teams resource-account GUID with `28:orgid:`. Replace the GUID and connection name with your values:

```yaml
telephony:
  bindings:
    - provider: acs
      identifier: "28:orgid:aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"
      connection: my-acs-connection
```

Reference: [Telephony YAML configuration](../concepts/azure-yaml-reference#telephony-bindings).

The CLI sends `provider: teams_phone_extensibility` and the GUID as `resource_account_object_id` to the API. Don't use an ACS-purchased-number identifier such as `4:+14255550123`; this workflow doesn't support that format.

# [Twilio](#tab/twilio)
Use your owned, voice-capable Twilio number in E.164 format. Replace the number and connection name with your values:

```yaml
telephony:
  bindings:
    - provider: twilio
      identifier: "+14255550123"
      connection: my-twilio-connection
```

Reference: [Telephony YAML configuration](../concepts/azure-yaml-reference#telephony-bindings).

The CLI sends `identifier` as the API's `phone_number`. Creating the binding replaces the number's existing inbound voice routing, so use a number intended for this agent.

---

### Deploy and inspect the binding

1. Deploy the voice service. Replace `<service-name>` with the key under `services` in `azure.yaml`. This key can differ from the agent's Foundry name:

    ```azurecli
    azd deploy <service-name>
    ```

    Reference: [azd deploy](/en-us/azure/developer/azure-developer-cli/reference#azd-deploy).

    Deployment creates missing bindings and accepts matching active bindings. It fails on conflicting configuration or duplicate matches rather than changing existing routing. It uses `api-version=v1` and service-generated binding IDs.
2. Read the deployed bindings through REST. `azd` doesn't expose a standalone binding-list command. Complete the [REST authentication setup](voice-agent-telephony-channels?pivots=rest#set-up-your-preferred-interface), then send:

    ```http
    GET {projectEndpoint}/agents/{agentName}/telephony/bindings?api-version=v1
    Authorization: Bearer <access-token>
    ```

    Reference: [Telephony binding API operations](https://github.com/Azure/azure-dev/blob/azd-ext-azure-ai-agents_1.2.0/cli/azd/extensions/azure.ai.agents/internal/pkg/agents/agent_api/telephony_operations.go).

    Find the binding by its provider and phone number or Teams resource-account GUID. If `has_more` is `true`, repeat the request with `&after={lastId}`, using the URL-encoded `last_id` from the response. Save the returned `id` and `incoming_call_url`; don't construct the ID from the provider or number.
3. Complete incoming-call delivery, then test the call. For Teams, use `incoming_call_url` when configuring Event Grid. For Twilio, Foundry configures the number's voice callbacks when it creates the binding.

::: zone-end

### Binding update rules

Both providers support updates to `label`. To stop routing incoming calls to the agent, disconnect the number.

::: zone pivot="azd"

`azd deploy` doesn't update or delete existing bindings. Select **Python SDK** or **REST API** for those operations. If deployment reports configuration drift, inspect and reconcile the existing binding before deploying again.

::: zone-end

# [Teams Phone extensibility](#tab/teams-phone)
Teams bindings also support changes to `connection_name` and the display `phone_number`. The provider and resource-account object ID are immutable.

# [Twilio](#tab/twilio)
To change the phone number or connection, delete and recreate the binding.

---

## Configure incoming-call delivery

After creating a binding, complete the callback setup for your provider.

# [Teams Phone extensibility](#tab/teams-phone)
### Register the Event Grid subscription

For inbound calls, create an Event Grid subscription on the Communication Services resource that targets the binding's `incoming_call_url`. If the portal already configured secure delivery, don't create a duplicate subscription.

Before running the Bash example, sign in with `az login` and set these variables:

| Variable | Value |
| --- | --- |
| `eventSubscriptionName` | A name for the Event Grid event subscription. |
| `acsResourceId` | The Azure resource ID of the Communication Services resource. |
| `webhook` | The `incoming_call_url` returned when you create the binding. |
| `webhookTenantId` | The tenant ID configured for the webhook application. |
| `webhookApplicationIdOrUri` | The webhook application's client ID or Application ID URI. |

Complete the application and role setup in [Deliver events to Microsoft Entra protected endpoints](/en-us/azure/event-grid/secure-webhook-delivery) first. Obtain the webhook tenant and audience from the administrator who configures secure incoming-call delivery. The webhook application identifies the token audience; it isn't the Microsoft Event Grid first-party application.

```azurecli
az eventgrid event-subscription create \
  --name "$eventSubscriptionName" \
  --source-resource-id "$acsResourceId" \
  --endpoint-type webhook \
  --endpoint "$webhook" \
  --included-event-types Microsoft.Communication.IncomingCall \
  --event-delivery-schema eventgridschema \
  --azure-active-directory-tenant-id "$webhookTenantId" \
  --azure-active-directory-application-id-or-uri "$webhookApplicationIdOrUri"
```

Reference: [az eventgrid event-subscription create](/en-us/cli/azure/eventgrid/event-subscription#az-eventgrid-event-subscription-create).

During creation, Event Grid sends a validation event that the endpoint answers automatically.

Foundry validates the Microsoft Entra token that Event Grid attaches to each delivery and matches the event to a binding's project, agent, Communication Services resource, and callee.

Event Grid allows up to 500 event subscriptions per system topic. Plan incoming-call delivery within the [Event Grid quotas and limits](/en-us/azure/event-grid/quotas-limits).

# [Twilio](#tab/twilio)
### Use the configured Twilio callbacks

Foundry configures the number's voice callbacks when you create the binding. Use the Twilio Console to review the number's voice URL and status callback.

---

## Place outbound calls by using the API

To place an outbound call, create a call job through the API. A call job uses your provider's project connection and doesn't need an inbound binding, so you can use a connection that you created in the portal.

[Place outbound calls and manage campaigns](voice-agent-outbound-calls) covers the complete workflow:

- [Choose the caller and destination](voice-agent-outbound-calls#choose-the-caller-and-destination) for Teams Phone extensibility, Twilio, or SIP.
- [Create one call job](voice-agent-outbound-calls#create-one-call-job) and [monitor the job](voice-agent-outbound-calls#monitor-the-job).
- [Schedule calls and retries](voice-agent-outbound-calls#schedule-calls-and-retries).
- [Cancel a call job](voice-agent-outbound-calls#cancel-a-call-job).

The call-job ID tracks the outbound request and its attempts. To transfer or end a connected call, use the call ID from the Calls API, as described in Manage a live call.

::: zone pivot="azd"

`azd deploy` doesn't place outbound calls. Use the Python or REST examples in the outbound-call guide.

::: zone-end

## Configure transfer to a person

Configure named transfer targets so your application can route an active call to a support representative. The application selects a target by name when it calls the transfer API. For agent-selected transfers, configure the separate [`transfer` system tool](voice-agent-system-tools#configure-a-transfer-target).

The examples use phone-number destinations.

::: zone pivot="foundry-portal"

Select **Python SDK** or **REST API** at the top of this article for the transfer-target configuration examples.

::: zone-end

::: zone pivot="azd"

Use **Python SDK** or **REST API** for the target-management examples in this section. Optional YAML `transferTargets` declarations can populate an empty agent-level target list only when the same deployment creates a binding. The CLI doesn't overwrite a nonempty target list or apply a changed list when no binding is created.

::: zone-end

::: zone pivot="python"

Read the current target list and its ETag, and then replace the list. Include every target you want to keep. An empty list clears the target list.

```python
from azure.core import MatchConditions

targets, target_headers = telephony.get_transfer_targets(
    agent_name=agent_name,
    cls=lambda response, result, _: (result, response.http_response.headers),
)
targets = telephony.replace_transfer_targets(
    agent_name=agent_name,
    body={
        "transfer_targets": [
            {
                "name": "billing",
                "description": "Billing and payment questions",
                "destination": {
                    "type": "phone_number", "value": "+14255550111"
                },
            },
            {
                "name": "operator",
                "description": "A person at the front desk",
                "destination": {
                    "type": "phone_number", "value": "+14255550112"
                },
            },
        ]
    },
    etag=target_headers["ETag"],
    match_condition=MatchConditions.IfNotModified,
)
```

Reference: [Azure AI Projects client library for Python](https://aka.ms/azsdk/azure-ai-projects-v2/python/code).

Replace the example destinations with your approved targets.

::: zone-end

::: zone pivot="rest"

First, read the current target list and its `ETag` response header:

```http
GET {projectEndpoint}/agents/{agentName}/telephony/transfer_targets?api-version=v1
Authorization: Bearer <access-token>
```

Replace the target list with `PUT`, using the returned `ETag` in `If-Match`. Include every target you want to keep: this operation replaces the entire list, and an empty array clears it.

```http
PUT {projectEndpoint}/agents/{agentName}/telephony/transfer_targets?api-version=v1
Authorization: Bearer <access-token>
Content-Type: application/json
If-Match: <etag-from-latest-transfer-targets-read>

{
  "transfer_targets": [
    {
      "name": "billing",
      "description": "Billing and payment questions",
      "destination": { "type": "phone_number", "value": "+14255550111" }
    },
    {
      "name": "operator",
      "description": "A person at the front desk",
      "destination": { "type": "phone_number", "value": "+14255550112" }
    }
  ]
}
```

::: zone-end

Use these destination types in REST requests for provider-specific routing:

# [Teams Phone extensibility](#tab/teams-phone)
| Destination`type` | Value |
| --- | --- |
| `phone_number` | E.164 phone number. |
| `teams` | Teams user or resource-account GUID, optionally prefixed with `28:orgid:`. |

For a Teams recipient, use the `teams` destination type with the recipient's Teams object GUID.

# [Twilio](#tab/twilio)
| Destination`type` | Value |
| --- | --- |
| `phone_number` | E.164 phone number. |
| `sip` (preview) | SIP or SIPS URI. Requires `Foundry-Features: VoiceAgents=V1Preview`. |

---

Use the same `type` and `value` address fields in the Python request dictionary and REST body.

Give each target a `description` that explains its purpose, such as billing support or a front-desk operator. Your application uses the configured target name in its transfer request.

Transfer requests select a target from this API collection. The `transfer` system tool uses the targets in the agent definition.

## Manage a live call

Use the Calls API to find a call and request a transfer or end action while it is active. These actions apply to inbound and outbound calls with a call record. Complete Set up your preferred interface before running the examples.

Your application selects the action and supplies the call ID. Use these call management APIs for supervisor controls or actions triggered by your application:

| Action | REST request | Python SDK method |
| --- | --- | --- |
| Find calls | `GET /agents/{agentName}/telephony/calls` | `list_calls` |
| Inspect one call | `GET /agents/{agentName}/telephony/calls/{callId}` | `get_call` |
| Transfer an active call | `POST /agents/{agentName}/telephony/calls/{callId}:transfer` with a configured `target` | `transfer_call` |
| End an active call | `POST /agents/{agentName}/telephony/calls/{callId}:end` | `end_call` |

For the [outbound example](voice-agent-outbound-calls#create-one-call-job), filter the call list by provider and time, then match the returned phone numbers to your call. Use the matching record's `id` for call control. The call-job ID tracks the outbound request and its attempts. See Inspect call records and conversations for query filters and diagnostics.

::: zone pivot="foundry-portal,azd"

Select **Python SDK** or **REST API** at the top of this article to list calls or send a transfer or end-call request.

::: zone-end

::: zone pivot="python"

1. List calls in progress and select the ID of the call you want to manage. The SDK retrieves more pages as you iterate:

    ```python
    for call in telephony.list_calls(
        agent_name=agent_name, status="in_progress", limit=20
    ):
        print(call.id, call.status, call.phase)
    ```

    Reference: [Azure AI Projects client library for Python](https://aka.ms/azsdk/azure-ai-projects-v2/python/code).
2. Replace `<active-call-id>` with the selected call ID and read its current details:

    ```python
    call_id = "<active-call-id>"
    call = telephony.get_call(agent_name=agent_name, call_id=call_id)
    print(call.status, call.phase)
    ```

    Reference: [Azure AI Projects client library for Python](https://aka.ms/azsdk/azure-ai-projects-v2/python/code).

    The status `in_progress` includes calls still being set up. Transfer and end-call actions require an active call. Check its phase and current details before sending an action.
3. Choose one action for the call. To transfer it to the configured `operator` target:

    ```python
    call = telephony.transfer_call(
        agent_name=agent_name, call_id=call_id, target="operator"
    )
    ```

    Reference: [Azure AI Projects client library for Python](https://aka.ms/azsdk/azure-ai-projects-v2/python/code).

    To end the call instead, send an end-call request:

    ```python
    call = telephony.end_call(agent_name=agent_name, call_id=call_id)
    ```

    Reference: [Azure AI Projects client library for Python](https://aka.ms/azsdk/azure-ai-projects-v2/python/code).
4. Inspect the returned call record. Both actions return the updated record. Read it again to check its subsequent status and lifecycle events:

    ```python
    call = telephony.get_call(agent_name=agent_name, call_id=call_id)
    print(call.status, call.phase, call.end_reason)
    for event in call.events or []:
        print(event.sequence, event.name, event.outcome, event.reason)
    ```

    Reference: [Azure AI Projects client library for Python](https://aka.ms/azsdk/azure-ai-projects-v2/python/code).

    Check the provider's call status to confirm the transfer outcome.

::: zone-end

::: zone pivot="rest"

1. List calls in progress. Match the call's phone numbers and start time, and copy its `id` into `{callId}` for subsequent requests:

    ```http
    GET {projectEndpoint}/agents/{agentName}/telephony/calls?api-version=v1&status=in_progress&limit=20
    Authorization: Bearer <access-token>
    ```
2. Read the selected call. Check its current status and lifecycle details to confirm that it is active:

    ```http
    GET {projectEndpoint}/agents/{agentName}/telephony/calls/{callId}?api-version=v1
    Authorization: Bearer <access-token>
    ```
3. Choose the action for this call. To transfer it, first configure an API transfer target, then send its name in `target`. This example uses `operator`:

    ```http
    POST {projectEndpoint}/agents/{agentName}/telephony/calls/{callId}:transfer?api-version=v1
    Authorization: Bearer <access-token>
    Content-Type: application/json
    
    { "target": "operator" }
    ```

    To end the call instead, send an end request with an empty body:

    ```http
    POST {projectEndpoint}/agents/{agentName}/telephony/calls/{callId}:end?api-version=v1
    Authorization: Bearer <access-token>
    ```
4. Inspect the returned call record. Both actions return `200 OK` with the updated record. Use the same GET request to read its subsequent status and lifecycle events. Check the provider's call status to confirm the transfer outcome.

::: zone-end

## Configure audio for phone calls

Phone networks carry narrowband audio, so tune the agent for the channel:

- Use `azure_deep_noise_suppression_headset` when background speech causes false turns or interruptions in phone calls. For single-caller sessions with competing nearby speakers, use `azure_personal_noise_suppression`. Keep `azure_deep_noise_suppression` for general-purpose background-noise suppression.
- Increase `silence_duration_ms`. Callers on a phone pause more than callers at a keyboard.
- Add `phrase_list` hints for the identifiers callers read aloud, such as order or policy numbers.
- Attach the `end_conversation` system tool so the agent can end a completed call.

See [Configure a voice agent](configure-voice-agent).

## Test the call

::: zone pivot="azd"

`azd ai agent invoke` doesn't start voice conversations or phone calls. Use a controlled phone call to verify the binding and provider routing.

::: zone-end

Allow time for your provider configuration changes to propagate before testing the number.

1. Wait for the selected provider and binding changes to propagate.
2. From a controlled caller, call the configured number.
3. Confirm the agent answers.
4. Complete a short conversation.
5. Interrupt the agent.
6. Use one safe tool or knowledge path.
7. Test the approved human-handoff behavior.
8. End the call.
9. Confirm that monitoring and trace data appear.

Record:

- Test timestamp and time zone.
- Called number.
- Callee identifier.
- Telephony provider and provider call ID, such as an Azure Communication Services correlation ID or Twilio Call SID.
- Agent name and version.

# [Teams Phone extensibility](#tab/teams-phone)
Also record the Azure Communication Services resource ID and Event Grid delivery result.

# [Twilio](#tab/twilio)
Also record the Foundry project connection name.

---

For an outbound test, create a job for an approved test recipient and record the job ID, status, attempt count, and reason. Don't treat `202 Accepted` as proof that the call connected.

## Trace phone calls

When a call arrives through telephony, the session's root trace span records the provider, the provider's call ID, and the dialed and calling numbers. You can correlate a Foundry session with a record in your telephony provider.

Caller and callee phone numbers are personal data. Review who can read your project's Application Insights resource before you enable content capture. See [Voice agent tracing, monitoring, and evaluation](../concepts/voice-agent-observability).

## Inspect call records and conversations

Use the Calls API for call records and live-call actions, the call-job API for outbound requests and retries, and conversation APIs for stored dialogue. Complete the interface setup for Python or REST. Use the project endpoint and agent name from your call setup.

::: zone pivot="foundry-portal,azd"

To run the query examples in this section, select **Python SDK** or **REST API** under **Choose a configuration method** at the top of this article.

::: zone-end

Choose the record that matches the question you want to answer:

| Question | Query | Identifier to save |
| --- | --- | --- |
| What happened during a call? | List and get `/agents/{agentName}/telephony/calls`. | The call's service-generated `id`. |
| How is an outbound call progressing? | [Read the call job](voice-agent-outbound-calls#monitor-the-job). | The job `id`, `attempt_count`, and any `terminal_reason`. |
| How is a recipient batch progressing? | [Read the campaign and validation operation](voice-agent-outbound-calls#poll-validation-and-read-execution-progress), then list jobs by `campaign_name`. | The campaign name, operation ID, and recipient job IDs. |
| What did the caller and agent say? | Read the agent's stored voice conversation and items. | The `conversation_id`. |
| Which stage caused a delay or failure? | Inspect the call's lifecycle events and the linked Foundry trace. | `trace.trace_id` and `provider_call_id`, when available. |

Keep these identifiers with your application's request records. Each identifies a different resource: pass a call ID to the Calls API, a job ID to the call-job API, and a conversation ID to the conversation API.

### Find a call record

The Calls API returns call records, including calls that ended before a voice session became ready. Call history is available independently of conversation storage. For outbound work, also query the call job to track its schedule and attempts.

::: zone pivot="python"

1. List failed calls in your investigation window. The SDK accepts UTC `datetime` values and retrieves more pages as you iterate:

    ```python
    from datetime import datetime, timedelta, timezone
    
    end_time = datetime.now(timezone.utc)
    start_time = end_time - timedelta(hours=1)
    for call in telephony.list_calls(
        agent_name=agent_name,
        status="failed",
        started_after_time=start_time,
        started_before_time=end_time,
        order="desc",
        limit=20,
    ):
        print(call.id, call.provider, call.status, call.phase)
    ```

    Reference: [Azure AI Projects client library for Python](https://aka.ms/azsdk/azure-ai-projects-v2/python/code).
2. Select the call by its time and provider, and replace `<call-id>` with its returned `id`. Read the record and print its lifecycle events in sequence:

    ```python
    call_id = "<call-id>"
    call = telephony.get_call(agent_name=agent_name, call_id=call_id)
    print(call.status, call.phase, call.end_reason)
    print(call.provider_call_id, call.provider_message)
    for event in sorted(call.events or [], key=lambda item: item.sequence):
        print(event.sequence, event.name, event.outcome, event.reason)
    if call.trace:
        print(call.trace.trace_id, call.trace.conversation_id)
    ```

    Reference: [Azure AI Projects client library for Python](https://aka.ms/azsdk/azure-ai-projects-v2/python/code).

    Use `trace_id` for trace lookup and `conversation_id` to read stored dialogue. These values are available when the call reaches the corresponding stage.

::: zone-end

::: zone pivot="rest"

1. List failed calls for the agent, with the most recent records first:

    ```http
    GET {projectEndpoint}/agents/{agentName}/telephony/calls?api-version=v1&status=failed&order=desc&limit=20
    Authorization: Bearer <access-token>
    ```

    The response contains a `data` array of call summaries and pagination fields. Set `status=in_progress` to find calls still in progress, or omit `status` to include all outcomes. Inspect the milestones to confirm whether a call was answered. A call status of `success` describes the call lifecycle; use conversation or business-service results to assess whether the customer's task succeeded.
2. Narrow the query with the supported filters:

    | Parameter | Usage |
    | --- | --- |
    | `provider` | Select `twilio` or `teams_phone_extensibility` for the providers in this article. |
    | `status` | Select `in_progress`, `success`, or `failed`. |
    | `started_after` | Include calls that started at or after this Unix timestamp in seconds. |
    | `started_before` | Include calls that started at or before this Unix timestamp in seconds. |
    | `limit` | Request 1–100 records per page; the default is 20. |
    | `order` | Use `desc` for newest first or `asc` for oldest first. |

    For example, append `&provider=twilio&started_after={startTime}&started_before={endTime}` to the request. Replace the time placeholders with Unix seconds for your investigation window, with the start at or before the end. Use the project and agent that handled the call.
3. If `has_more` is `true`, copy `last_id` into `after` to read the next page. Keep the same filters and order:

    ```http
    GET {projectEndpoint}/agents/{agentName}/telephony/calls?api-version=v1&status=failed&order=desc&limit=20&after={lastId}
    Authorization: Bearer <access-token>
    ```

    Pass cursor values exactly as returned, URL-encoded when needed. Use either `after` or `before` in a request. To read toward the previous page, use `first_id` as `before`. Results reflect current call state, so active-call lists can change between requests.
4. Copy a call's `id` from `data` and read its detailed record:

    ```http
    GET {projectEndpoint}/agents/{agentName}/telephony/calls/{callId}?api-version=v1
    Authorization: Bearer <access-token>
    ```

    Inspect these fields to identify where the call stopped:

    | Field | What to inspect |
    | --- | --- |
    | `status`, `phase`, `end_reason` | The overall lifecycle result, the phase reached, and the final reason. |
    | `timing` | Milestones for answering, media connection, session readiness, and first caller or agent audio. Present milestones show which stages were observed. |
    | `events` | Read events in `sequence` order. Compare `name`, `outcome`, `reason`, and provider codes to find the failed operation. |
    | `events_truncated` | If `true`, the timeline omits older events. Use the trace and provider logs for additional context. |
    | `provider_call_id`, `provider_status_code`, `provider_sub_code`, `provider_message` | Correlate the result with your provider's call diagnostics. These fields are present when available. |
    | `trace` | Check `status` and use `trace_id` for trace lookup. Use `conversation_id` for stored conversation reads when a voice session was created. |

    Timestamps are Unix seconds; `duration_ms` is milliseconds. Event `observed_at` records when the service observed an event. `occurred_at`, when present, records the provider's event time.

::: zone-end

### Read the conversation and recording

Conversation APIs apply to stored inbound and outbound voice sessions. [Enable `store: true`](configure-voice-agent#persist-conversations) in the agent definition to capture transcripts and audio. For the inbound support example, get the conversation ID from the call record's `trace.conversation_id` when available.

::: zone pivot="python"

1. List stored conversations to find the session you want to inspect:

    ```python
    conversations = project_client.voice_agents.conversations
    for conversation in conversations.list(
        agent_name=agent_name, order="desc", limit=20
    ):
        print(conversation.id, conversation.status)
    ```

    Reference: [AIProjectClient](/en-us/python/api/azure-ai-projects/azure.ai.projects.aiprojectclient).
2. Replace `<conversation-id>` with the selected ID. Read its storage status and items in conversation order:

    ```python
    conversation_id = "<conversation-id>"
    conversation = conversations.get(
        agent_name=agent_name, conversation_id=conversation_id
    )
    print(conversation.status, conversation.last_error)
    for item in conversations.list_items(
        agent_name=agent_name,
        conversation_id=conversation_id,
        order="asc",
        limit=100,
    ):
        print(item.as_dict())
    ```

    Reference: [AIProjectClient](/en-us/python/api/azure-ai-projects/azure.ai.projects.aiprojectclient).
3. To inspect individual model turns, list their responses:

    ```python
    for response in conversations.list_responses(
        agent_name=agent_name,
        conversation_id=conversation_id,
        order="asc",
        limit=20,
    ):
        print(response.as_dict())
    ```

    Reference: [AIProjectClient](/en-us/python/api/azure-ai-projects/azure.ai.projects.aiprojectclient).
4. When the conversation's status is `completed`, read the recording metadata:

    ```python
    recording = conversations.get_audio(
        agent_name=agent_name, conversation_id=conversation_id
    )
    print(recording.as_dict())
    ```

    Reference: [AIProjectClient](/en-us/python/api/azure-ai-projects/azure.ai.projects.aiprojectclient).

    For Foundry-managed storage, stream the WAV to a local file:

    ```python
    with open("conversation.wav", "wb") as audio_file:
        for chunk in conversations.download_audio(
            agent_name=agent_name, conversation_id=conversation_id
        ):
            audio_file.write(chunk)
    ```

    Reference: [AIProjectClient](/en-us/python/api/azure-ai-projects/azure.ai.projects.aiprojectclient).

    For bring-your-own storage, read the returned `blob_uri` with your storage credentials. If the recording is still being prepared, read the conversation status and retry after the response's `Retry-After` interval when provided.

::: zone-end

::: zone pivot="rest"

1. To discover stored conversations, list the agent's conversation collection:

    ```http
    GET {projectEndpoint}/agents/{agentName}/endpoint/protocols/voice/conversations?api-version=v1&order=desc&limit=20
    Authorization: Bearer <access-token>
    ```

    Use the conversation `id` returned by this API. For an outbound investigation, use the agent, calling time, and your application and provider logs to locate the matching trace and conversation. The job response exposes job progress; conversation IDs come from session telemetry or the conversation API.
2. Read a selected conversation to check its storage status:

    ```http
    GET {projectEndpoint}/agents/{agentName}/endpoint/protocols/voice/conversations/{conversationId}?api-version=v1
    Authorization: Bearer <access-token>
    ```

    `status: in_progress` means the call is active or its conversation data is still being saved. `completed` means the stored conversation is ready. For `failed`, inspect `last_error`; any items and per-turn audio already stored remain available.
3. Read the stored items in conversation order:

    ```http
    GET {projectEndpoint}/agents/{agentName}/endpoint/protocols/voice/conversations/{conversationId}/items?api-version=v1&order=asc&limit=100
    Authorization: Bearer <access-token>
    ```

    Inspect each item's type, role, content, and available tool information. Follow `has_more` and `last_id` with `after` to read the complete history. Private collection uses an `output_ref`; verify the outcome in your business service while keeping the collected value private.
4. To inspect model turns, list the conversation's responses:

    ```http
    GET {projectEndpoint}/agents/{agentName}/endpoint/protocols/voice/conversations/{conversationId}/responses?api-version=v1&order=asc&limit=20
    Authorization: Bearer <access-token>
    ```

    A response identifies one model turn. Read a selected response at `/agents/{agentName}/endpoint/protocols/voice/conversations/{conversationId}/responses/{responseId}?api-version=v1`. Its `/items` subresource provides paged output items when you need the full output. Use the same authorization header.
5. After the call ends, retrieve metadata for its merged recording:

    ```http
    GET {projectEndpoint}/agents/{agentName}/endpoint/protocols/voice/conversations/{conversationId}/audio?api-version=v1
    Authorization: Bearer <access-token>
    ```

    The metadata describes the stereo recording, with caller audio on the left and agent audio on the right. For bring-your-own storage, use the returned `blob_uri` with your storage credentials. For Foundry-managed storage, download the WAV through the authenticated content endpoint:

    ```http
    GET {projectEndpoint}/agents/{agentName}/endpoint/protocols/voice/conversations/{conversationId}/audio/content?api-version=v1
    Authorization: Bearer <access-token>
    ```

    For a `409 Conflict`, read the error and conversation status. Retry when the recording is still being prepared, honoring `Retry-After` when supplied. If finalization failed, inspect the conversation's `last_error`. For bring-your-own storage, use `blob_uri` to read the recording directly.

    A `404 Not Found` can indicate that the conversation or audio wasn't stored or is no longer available. Enabling storage affects subsequent sessions. See [Conversation storage and retention](../concepts/voice-agent-observability#read-stored-conversations).

::: zone-end

## Troubleshoot telephony

Use call records, conversation data, and traces to find where a call failed and choose the next troubleshooting step.

1. Record the project, agent name and version, call direction, provider, UTC time window, and available call, job, and operation IDs.
2. For inbound calls, query the call result. Inspect `phase`, `timing`, and `events` to locate the first failing stage. If the record is absent, confirm the project, agent, and query filters, then inspect binding configuration and provider webhook delivery.
3. For outbound calls, query the call-job result. Check `status`, `attempt_count`, `next_attempt_at`, `terminal_reason`, and the schedule. For a campaign, first check its validation operation and [row-level errors](voice-agent-outbound-calls#diagnose-preparation-errors), then inspect the recipient jobs.
4. When the call reaches the agent, read the stored conversation and inspect the model and tool spans in the [Foundry trace view](../concepts/voice-agent-observability#trace-views). Confirm the tool's actual result and the provider or business-service outcome before retrying an action.
5. Use the symptom table to correct the identified configuration, then verify the affected stage with an approved test call. Keep the original and new identifiers so you can compare results.

::: zone pivot="azd"

### Resolve deployment errors

Use the following checks for `azd` errors. For the call-query examples that follow, select **Python SDK** or **REST API**.

| Symptom | What to check |
| --- | --- |
| Voice options aren't available or the extension doesn't load | Check for `azd` version 1.37.0 or later and `azure.ai.agents` version 1.2.0 or later. Follow the [installation guidance](install-cli-foundry-extensions) to update the tools. |
| A binding differs from the declaration, or multiple bindings match | List the current bindings and confirm the intended provider identity and connection. Reconcile the remote configuration with Python or REST before redeploying. |
| Deployment reports an unconfirmed write or partial completion | Read the remote bindings before retrying. Some bindings might already exist even though deployment didn't finish successfully. |
| Transfer targets differ from the declaration | Inspect the agent-level target list. Reconcile it with Python or REST; deployment doesn't overwrite a nonempty list. |

::: zone-end

### Query an inbound call result

Use the Calls API to find a recent inbound call and read its outcome. Complete the interface setup for Python or REST. The response excerpts use illustrative values; use the identifiers returned by your own requests.

::: zone pivot="python"

1. List recent calls and identify the call by its time and provider:

    ```python
    for call in telephony.list_calls(
        agent_name=agent_name, order="desc", limit=20
    ):
        print(call.id, call.provider, call.started_at, call.status)
    ```

    Reference: [Azure AI Projects client library for Python](https://aka.ms/azsdk/azure-ai-projects-v2/python/code).
2. Replace `<call-id>` with that call's ID and inspect its outcome:

    ```python
    call = telephony.get_call(agent_name=agent_name, call_id="<call-id>")
    print(call.status, call.phase, call.end_reason)
    print(call.timing.as_dict() if call.timing else {})
    print(call.provider_status_code, call.provider_sub_code)
    print(call.provider_message)
    ```

    Reference: [Azure AI Projects client library for Python](https://aka.ms/azsdk/azure-ai-projects-v2/python/code).

    For example, `status="failed"` with `end_reason="answer_failed"` directs you to the provider's answer operation. Inspect the provider codes and message, then check credentials and connectivity. Use the detailed call record to examine lifecycle events and trace identifiers.

::: zone-end

::: zone pivot="rest"

1. List recent calls, including both successful and failed calls:

    ```http
    GET {projectEndpoint}/agents/{agentName}/telephony/calls?api-version=v1&order=desc&limit=20
    Authorization: Bearer <access-token>
    ```

    Find the call in the response's `data` array by its start time, provider, and available caller details. For a longer investigation window, use the time filters and pagination. Copy that entry's service-generated `id` into `{callId}`.
2. Read the selected call:

    ```http
    GET {projectEndpoint}/agents/{agentName}/telephony/calls/{callId}?api-version=v1
    Authorization: Bearer <access-token>
    ```

    A successful query returns `200 OK`, even when the call itself failed. For example, this response excerpt shows a failure while answering an inbound call:

    ```json
    {
      "id": "example-inbound-call-id",
      "provider_call_id": "example-provider-call-id",
      "status": "failed",
      "phase": "failed",
      "started_at": 1794211200,
      "ended_at": 1794211202,
      "end_reason": "answer_failed",
      "timing": {
        "received_at": 1794211200,
        "answer_requested_at": 1794211201,
        "ended_at": 1794211202,
        "timestamp_source": "gateway"
      }
    }
    ```
3. Interpret the response body and choose the next check:

    | Result | Interpretation and next step |
    | --- | --- |
    | `status: in_progress` | Setup or conversation activity is still in progress. Read the same call again and inspect its milestones. |
    | `answered_at` is present | The provider reported the call as answered. Check `media_connected_at` and `agent_session_ready_at` for media and agent readiness. |
    | `status: success` | The call lifecycle ended successfully. Read the stored conversation or business-service result to verify the customer's task. |
    | `status: failed` | Read `end_reason`, the lifecycle `events`, and any provider diagnostic fields. Use `provider_call_id` to locate the call in the provider's logs. |

    For an `answer_failed` result, inspect the provider's answer operation. Read `provider_status_code`, `provider_sub_code`, and `provider_message` when returned, then check credentials and provider connectivity. When `trace.trace_id` is available, continue with trace lookup.

::: zone-end

### Query an outbound call result

For a direct outbound call or a campaign recipient, use the call-job ID returned when the job was created. To find a campaign's jobs, [filter the job list by `campaign_name`](voice-agent-outbound-calls#list-or-delete-job-records).

::: zone pivot="python"

Read the job's outcome and attempt count. Replace `<call-job-id>` with the selected job ID:

```python
job = telephony.get_call_job(
    agent_name=agent_name, call_job_id="<call-job-id>"
)
print(job.status, job.attempt_count, job.terminal_reason)
print(job.next_attempt_at)
```

Reference: [Azure AI Projects client library for Python](https://aka.ms/azsdk/azure-ai-projects-v2/python/code).

For example, `status="completed"`, `attempt_count=3`, and `terminal_reason="no_answer"` mean the job ended after three attempts without an answer. For a job still in progress, continue [monitoring it](voice-agent-outbound-calls#monitor-the-job). For a connected conversation, use its call record and trace to read stored dialogue.

::: zone-end

::: zone pivot="rest"

1. Read the job using the same project endpoint and authentication:

    ```http
    GET {projectEndpoint}/agents/{agentName}/telephony_call_jobs/{callJobId}?api-version=v1
    Authorization: Bearer <access-token>
    ```

    This illustrative response excerpt shows a job whose permitted attempts ended without an answer:

    ```json
    {
      "id": "example-call-job-id",
      "agent_name": "contoso-outbound-reminders",
      "status": "completed",
      "attempt_count": 3,
      "retry_policy": {
        "type": "fixed_interval",
        "max_attempts": 3,
        "interval": 300
      },
      "terminal_reason": "no_answer"
    }
    ```
2. Read `status` together with `terminal_reason` and `attempt_count`. Here, the job is complete because all three permitted attempts finished. The `no_answer` reason identifies the calling outcome. `completed` alone doesn't establish that the recipient answered or the reminder was delivered.
3. For a job still in progress, continue reading it using the [polling guidance](voice-agent-outbound-calls#monitor-the-job). For a completed conversation, inspect its stored items and recording. Use job IDs for job queries and Calls API IDs for call records and live-call actions.

::: zone-end

### Find the trace in Azure Monitor

Use this query when the call record provides `trace.trace_id` and your project has a connected Application Insights resource.

1. Open **Logs** in the Log Analytics workspace linked to that Application Insights resource. Set a time range that includes the call and allow time for telemetry ingestion. Your identity needs the [trace-viewing permissions](../concepts/voice-agent-observability#check-access-boundaries).
2. Replace `<trace-id>` with the returned W3C trace ID and run this Kusto Query Language (KQL) query:

    ```kusto
    let callTraceId = "<trace-id>";
    union AppRequests, AppDependencies
    | where OperationId == callTraceId
    | project TimeGenerated, Name, Success, ResultCode, DurationMs,
        OperationId, ParentId, Id
    | order by TimeGenerated asc
    ```

    Reference: [AppRequests table](/en-us/azure/azure-monitor/reference/tables/apprequests) and [AppDependencies table](/en-us/azure/azure-monitor/reference/tables/appdependencies).
3. Inspect the returned request and dependency spans to find failures or long durations. Use the provider call ID in your provider's diagnostics to compare signaling and media events with the Foundry timeline.

This example uses Log Analytics workspace table names. If the query returns no rows, check the selected workspace, time range, trace availability, ingestion delay, and permissions. Conversation storage and trace capture have separate settings.

### Resolve common symptoms

# [Teams Phone extensibility](#tab/teams-phone)
| Symptom | What to check |
| --- | --- |
| Busy signal and no Azure Communication Services event | Teams number activation, license, PSTN connectivity, calling bot channel, TPE association, synchronization, and Azure Communication Services consent. |
| Azure Communication Services receives the call but Foundry reports no binding | Compare `IncomingCall.data.to.rawId` with `28:orgid:<resource_account_object_id>` constructed from the binding's GUID. Keep the prefix out of the REST binding field. |
| Event Grid validation fails | Endpoint, tenant, webhook audience, app-role assignment, delivery identity, and Event Grid write access. |
| Secure setup reports a Graph permission error | Ask a tenant administrator to grant the approved application-management permissions and retry. |
| Azure Communication Services `AnswerCall` returns 401 or 403 | Project connection target, project managed identity, Azure Communication Services role assignment, and RBAC propagation. |

# [Twilio](#tab/twilio)
| Symptom | What to check |
| --- | --- |
| Twilio numbers don't load | Check the connection's `Twilio` category, Account SID target, and `ApiKey` credential containing the current Primary Auth Token. Confirm that you can read the connection credentials. |
| No Twilio numbers can be selected | Confirm the Twilio account owns an active number with the Voice capability. |
| Twilio rejects the credentials | Update or recreate the project connection with the current Account SID and Primary Auth Token. |
| A Twilio number is already bound | Use the existing binding or disconnect it from the other agent before retrying. |
| A Twilio number doesn't reach the agent | Check that the number is active and voice-capable, is bound to the intended agent, and has a voice URL that points to Foundry. Review webhook delivery errors in Twilio. |

---

| Symptom | What to check |
| --- | --- |
| Call connects but is silent | Compare `answered_at`, `media_connected_at`, `agent_session_ready_at`, and first-audio milestones in `timing`. For the stage that stalls, check media reachability and PCM format, model and voice configuration, or the playback path. |
| Call disconnects unexpectedly | Callback reachability, media errors, service limits, and correlation logs. |
| The wrong agent answers | Confirm the agent that owns the binding collection and inspect that agent's active version. |
| The number doesn't appear after refresh | List the agent's bindings and confirm that the number is connected to the intended agent. |
| A binding update, deletion, or transfer-target replacement fails with a precondition error | Read the resource again, review any concurrent changes, and use the latest `ETag` in `If-Match`. |
| Outbound creation returns `400 Bad Request` | Check `connection_name`, the provider-specific `source`, the E.164 destination, required structured inputs, and the `Idempotency-Key` header. |
| Outbound creation returns `409 Conflict` | The idempotency key was used with a different request. Reuse the original request to recover its job, or use a new key for a new call intent. |
| Outbound creation returns `503 Service Unavailable` | Save the response and request details. Contact support if the error persists. |
| Call-job cancellation returns `409 Conflict` | Read the latest job and ETag. Retry with the current ETag only if the call hasn't connected and cancellation is still appropriate. |
| An outbound job is accepted but the destination doesn't ring | Read the job's status, attempt count, schedule, and reason. Check caller authorization and provider connectivity; `202 Accepted` isn't confirmation of a connected call. |
| Calls API returns no matching records | Confirm the project, agent, provider, time window, and pagination. Use the call-job API to inspect outbound work. Check inbound webhook delivery and binding ownership when the expected inbound record is absent. |
| Conversation or audio reads return `404` | Confirm the agent and conversation ID, that conversation storage was enabled for the session, and that the data is within its retention period. Use call history and provider diagnostics for calls that ended before a conversation was created. |
| Merged recording reads return `409` | Inspect the error and conversation status. Retry pending finalization with `Retry-After` when supplied. For failed finalization, inspect `last_error`; for bring-your-own storage, read the returned `blob_uri` with storage credentials. |
| A system tool isn't invoked | Check that the saved agent definition includes the tool in `tools`, sets `tool_choice` to `auto`, and explains when to use it. See [Troubleshoot tool availability](voice-agent-system-tools#troubleshoot-tool-availability). |
| A transfer or SMS result is uncertain | Check the tool result and the provider's call or message status before retrying. |

## Disconnect a number

Remove the inbound mapping when you no longer want the number to route calls to this agent. Outbound jobs don't require a binding; cancel any unwanted jobs separately.

::: zone pivot="azd"

1. Remove the binding's declaration from `azure.yaml` or the referenced service definition so a later deployment doesn't recreate it. If it was the last binding, remove the `telephony` block. This local edit doesn't delete the remote binding.
2. Select **Python SDK** or **REST API** at the top of this article. Follow the deletion steps with the service-generated binding ID and its current ETag.
3. Delete test bindings before deleting their agent. Don't use `azd down` just to disconnect a number; it can delete the environment's Azure resources.

::: zone-end

::: zone pivot="foundry-portal"

1. Open the agent **Channels** tab.
2. In **Phone numbers**, open the number's actions menu.
3. Select **Disconnect number**.
4. Confirm.

::: zone-end

::: zone pivot="python"

Read the binding again and use its current ETag to delete it:

```python
from azure.core import MatchConditions

binding_id = "<binding-id>"
binding, binding_headers = telephony.get_binding(
    agent_name=agent_name,
    binding_id=binding_id,
    cls=lambda response, result, _: (result, response.http_response.headers),
)
telephony.delete_binding(
    agent_name=agent_name,
    binding_id=binding_id,
    etag=binding_headers["ETag"],
    match_condition=MatchConditions.IfNotModified,
)
```

Reference: [Azure AI Projects client library for Python](https://aka.ms/azsdk/azure-ai-projects-v2/python/code).

The method returns `None` on success.

::: zone-end

::: zone pivot="rest"

Read the binding to get its current `ETag`, and then delete it by using that value in `If-Match`.

```http
GET {projectEndpoint}/agents/{agentName}/telephony/bindings/{bindingId}?api-version=v1
Authorization: Bearer <access-token>
```

```http
DELETE {projectEndpoint}/agents/{agentName}/telephony/bindings/{bindingId}?api-version=v1
Authorization: Bearer <access-token>
If-Match: <etag-from-latest-binding-read>
```

A successful deletion returns `204 No Content`.

::: zone-end

# [Teams Phone extensibility](#tab/teams-phone)
Disconnecting removes the Foundry binding. It doesn't:

- Release the Teams number.
- Remove the Teams resource account.
- Delete Azure Communication Services.
- Remove the bot or app registration.
- Revoke Teams Phone extensibility consent.

Coordinate upstream cleanup separately.

# [Twilio](#tab/twilio)
Disconnecting removes the Foundry binding. Your Twilio number, account, and Foundry project connection remain available. Review the number's voice routing before using it with another application.

---

## Security checklist

- Use Microsoft Entra authentication for Foundry API requests.
- Use the exact public Foundry project webhook endpoint.
- Don't persist service-generated call callback or media tokens.
- Confirm the binding target before update or deletion.
- Apply recording, consent, disclosure, retention, and privacy requirements.
- Prevent sensitive caller data from being read aloud or unnecessarily stored.

# [Teams Phone extensibility](#tab/teams-phone)
- Prefer managed identity for the Azure Communication Services connection.
- Don't share Azure Communication Services keys, connection strings, tokens, bot secrets, or portal cookies.
- For inbound calls, validate that the Event Grid topic is the intended Azure Communication Services resource.
- Keep webhook audience and Event Grid delivery identity concepts separate.
- Use a dedicated single-tenant webhook application when governance requires it.

# [Twilio](#tab/twilio)
- Store the Twilio Auth Token in the project connection. If it's exposed, rotate it and update the connection.
- Confirm that the Twilio account owns each inbound number and authorizes each outbound caller number.

---
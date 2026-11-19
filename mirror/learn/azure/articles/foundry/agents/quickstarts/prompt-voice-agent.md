---
layout: Conceptual
title: 'Quickstart: Create a voice-based prompt agent - Microsoft Foundry | Microsoft Learn'
canonicalUrl: https://learn.microsoft.com/en-us/azure/foundry/agents/quickstarts/prompt-voice-agent
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
author: PatrickFarley
learn_banner_products:
- azure
manager: mcleans
ms.author: pafarley
ms.collection: ce-skilling-ai-copilot
ms.update-cycle: 90-days
ms.service: microsoft-foundry
description: Create a managed voice-based prompt agent in Foundry Agent Service by using the Microsoft Foundry portal, a voice agent template, the Microsoft Foundry SDK, or the Azure Developer CLI.
ms.date: 2026-11-11T00:00:00.0000000Z
ms.subservice: foundry-agent-service
ms.topic: quickstart
ms.custom: doc-kit-assisted
ai-usage: ai-assisted
zone_pivot_groups: voice-agent-quickstart-tools
locale: en-us
document_id: 76062fad-c8b1-10bc-4393-30bea6445e63
document_version_independent_id: 9e1421f6-9fda-623f-d539-306bb98a7917
original_content_git_url: https://github.com/MicrosoftDocs/azure-ai-docs-pr/blob/live/articles/foundry/agents/quickstarts/prompt-voice-agent.md
site_name: Docs
depot_name: Learn.azure-ai
page_type: conceptual
toc_rel: ../../toc.json
asset_id: foundry/agents/quickstarts/prompt-voice-agent
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/foundry/agents/quickstarts/prompt-voice-agent.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/64b65f6c-101f-411a-9b83-9f577fab52d0
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1a667fd1-8145-4b11-af0f-9f5de205a6e5
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: e41b0bfe-60a2-1223-768b-fc4ee35ed5cc
---

# Quickstart: Create a voice-based prompt agent - Microsoft Foundry | Microsoft Learn

In this quickstart, you create a voice-based prompt agent, open a live session, complete a spoken turn, and read the conversation back. Foundry Agent Service manages the voice orchestration, so you don't host a speech pipeline of your own.

Choose your development tool. The **Foundry portal** path creates and tests the agent in the browser with no code. The **Foundry portal with templates** path starts from a ready-made agent for a common scenario, such as customer support or appointment scheduling, that you can try before you create it. The **Python SDK** and **JavaScript/TypeScript SDK** paths install the Microsoft Foundry SDK, create the agent in code, and connect to a live session over a WebSocket. The **Azure Developer CLI** path uses `azd` to scaffold, provision, deploy, and test the agent without writing runtime code. The examples start with a managed realtime model. The SDK paths also include an example that uses your own model deployment.

Voice agents are generally available, with some features still in preview. See [General availability and preview features](../overview#general-availability-and-preview-features).

If you already use Voice Live with a Foundry text agent, see [Compare and migrate to Microsoft Foundry voice agents](../how-to/migrate-from-voice-live).

To reuse your own model deployment or choose another model provider, see [Choose a managed or self-deployed model](../how-to/configure-voice-agent#choose-a-managed-or-self-deployed-model).

If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).

## Prerequisites

- A [Foundry project](../../how-to/create-projects).
- [Foundry User role](../../concepts/rbac-foundry) on the project, to create and invoke agents.

    Important

    The Foundry RBAC roles were recently renamed. **Foundry User**, **Foundry Owner**, **Foundry Account Owner**, and **Foundry Project Manager** were previously named Azure AI User, Azure AI Owner, Azure AI Account Owner, and Azure AI Project Manager. You might still see the previous names in some places while the rename rolls out. The role IDs and core permissions are unchanged by the rename.
- A voice model available to your project, such as `gpt-realtime`. Confirm model availability on the **Models** page of your Foundry project.
- Voice-agent availability in your project's region and Azure subscription. See [Supported regions](../concepts/limits-quotas-regions#supported-regions).

::: zone pivot="portal,portal-templates"

- A supported browser with microphone and speaker access.
- A microphone and speaker or headset for testing.

::: zone-end

::: zone pivot="portal-templates"

- Optional: To connect a template to your own systems, an [MCP server connection](../how-to/tools/model-context-protocol) or a [toolbox](../how-to/tools/toolbox) in the same project.

::: zone-end

::: zone pivot="python"

- Python 3.10 or later.
- The Azure CLI, signed in with `az login`.

::: zone-end

::: zone pivot="javascript"

- Node.js 22 or later.
- The Azure CLI, signed in with `az login`.

::: zone-end

::: zone pivot="azd"

- Azure Developer CLI version 1.32.0 or later and the Microsoft Foundry extensions. For the individual installation steps, see [Install the Azure Developer CLI Foundry extensions](../how-to/install-cli-foundry-extensions). To install the complete developer toolset, see [Prepare your development environment](../../how-to/develop/install-cli-sdk).
- An authenticated `azd` session. Run `azd auth login` after you install the extensions.
- The Azure permissions listed in [Install the Azure Developer CLI Foundry extensions](../how-to/install-cli-foundry-extensions#azure-permissions).

Check the installed agent extension version and its initialization options:

```azurecli
azd ai agent version
azd ai agent init --help
```

The initialization help must list `prompt-voice` under `--kind` and expose the `--voice` option. If `--voice` isn't listed, use an extension release that includes voice support before continuing. These CLI voice options don't require a private-preview environment variable.

::: zone-end

::: zone pivot="portal"

## Create the agent

1. Sign in to the [Microsoft Foundry portal](https://ai.azure.com/).
2. Open the project where you want to create the agent.
3. Go to the **Agents** page.
4. Select **Build an agent**. The **Create an agent** dialog opens.
5. In **Agent name**, enter a unique name for the agent.
6. Under **Interaction mode**, select **Voice**:

    - **Text**: Users type messages and receive text responses.
    - **Voice**: Users speak naturally and receive spoken responses in real time.

    Important

    You can't change the interaction mode after you create the agent. If you create a text agent and later need a voice agent, create another agent and select **Voice**.
7. Then select a use case to optimize for. This affects the default instructions for the agent.

Use a stable, recognizable name. The name appears in agent versions, traces and monitoring queries, evaluation target selection, phone-number bindings, and application and SDK references. The name must meet the validation rules shown in the dialog.

### Create and open the agent

Select **Create agent and open playground**. Foundry creates the voice agent and opens it in the agent playground.

Enter the agent instructions directly in the playground, and then review and customize them before testing.

The initial managed voice configuration is designed to start a session immediately and can include a managed realtime model, 24-kHz PCM audio input and output, automatic turn detection, transcription with Azure Speech in Foundry Tools, and a compatible Azure standard voice. The exact defaults can change. Treat the values shown in the portal as authoritative.

## Review the build page

Before testing, identify these areas:

- **Instructions**: Defines the agent's behavior.
- **AI model**: Selects a native speech or text model.
- **Speech recognition** and **Language**: Appear when required by the selected model.
- **Voice**: Selects the spoken output.
- **Avatar**: Adds visual output for supported browser experiences.
- **Tools**: Adds actions and external capabilities.
- **Knowledge bases**: Grounds answers in approved content.
- **Advanced settings**: Configures input audio, transcription, turn detection, and conversational behavior.
- **Playground**: Starts a live browser session.

## Add initial instructions

Replace generic instructions with a small, testable first version. Include:

1. Who the agent is.
2. What tasks it can complete.
3. Who the intended caller is.
4. The required speaking style.
5. What information it must confirm.
6. What it must never disclose or do.
7. When it must transfer or refer the caller to a person.
8. What it says when a tool fails.

Example:

```text
You are a concise appointment assistant.

- Speak in short sentences and ask one question at a time.
- Confirm the caller's name and appointment time before making a change.
- Never read a full account identifier aloud.
- If the caller asks for medical advice, explain that you can only help with scheduling and offer the approved human-support path.
- If a tool fails, apologize, do not claim the change succeeded, and provide the approved next step.
```

For detailed configuration guidance, see [Configure a voice agent](../how-to/configure-voice-agent).

## Save and start a browser session

1. Select **Save**.
2. Select **Start session**.
3. Allow microphone access when the browser prompts you.
4. Say a short greeting and complete a simple scenario.
5. Interrupt the agent while it's speaking to test barge-in behavior.
6. Pause during a sentence to test turn detection.
7. Select **End** when the test is complete.

Note

Configuration controls are disabled during an active voice session. End the session before changing the model, voice, avatar, tools, knowledge, or advanced settings.

## Validate the first session

Confirm that:

- The agent follows its instructions.
- The transcript recognizes your words.
- The voice language and pronunciation are correct.
- The response is short enough to understand by listening.
- The agent waits long enough for natural pauses.
- Interruption stops or redirects the response as expected.
- The agent doesn't claim a tool action succeeded when it didn't.
- The session ends cleanly.

## Troubleshoot creation and first-run issues

| Symptom | Resolution |
| --- | --- |
| **Voice** isn't available as an interaction mode | Confirm voice agents are available for the project, resource, subscription, and region. |
| The agent name is rejected | Follow the name validation shown in the dialog and choose a unique name in the project. |
| The model list is empty | Confirm resource access, supported region, and model availability. Refresh after permissions or deployment changes. |
| The browser can't use the microphone | Allow microphone access for the portal origin and confirm the device isn't exclusively used by another app. |
| The session starts but no audio is heard | Confirm the browser output device, system volume, selected voice compatibility, and that the session isn't muted. |
| The start button is still unavailable | Save required configuration and resolve validation messages in the configuration pane. |

::: zone-end

::: zone pivot="portal-templates"

A voice agent template is a complete agent definition for a common scenario, such as customer support, appointment scheduling, or order tracking. It includes a persona, a greeting, a voice, and tools. Most templates also split the conversation into stages built as [inline subagents](../how-to/use-inline-subagent-voice-agent), each with its own tools. You try the template before you create your own agent, choose which systems the agent connects to, and then customize the agent in the playground.

Important

Templates are examples. Review and test the instructions, tools, and data handling of an agent that you create from a template before you use it in production. If the template uses inline subagents, the agent depends on a preview feature. See [General availability and preview features](../overview#general-availability-and-preview-features).

## What the templates include

Each template is designed for a live phone or web conversation, not only a scripted demo:

- **Stages and handoffs**: Most templates split the call into stages, such as greeting, verification, the main task, and wrap-up. Each stage has its own instructions and only the tools that it needs. The agent hands off between stages without announcing a transfer, so the caller hears one continuous conversation.
- **Low latency**: Templates use a realtime speech model and semantic turn detection, so the agent answers as soon as the caller finishes a thought. While one stage is active, Foundry discovers the MCP tools of the stages that can come next, so a handoff doesn't wait for tool discovery. When the caller corrects something, asks for something, or sounds worried or frustrated, most templates first say a short, specific acknowledgment, such as "Thursday, not Tuesday.", before they hand off, call a tool, or give a result. The caller hears a response right away instead of silence.
- **Caller protections**: Before a tool sends, books, creates, updates, or submits anything, the agent reads the details back and waits for an explicit yes. The agent states only facts from tool results or the template's sample data, and says so when a tool fails instead of claiming success. Industry templates add rules for their domain. For example:
    - **Collections and payment recovery** verifies the account holder before it discusses the balance, and never threatens or harasses the caller, in line with the Fair Debt Collection Practices Act (FDCPA).
    - **Legal intake specialist** never gives legal advice, and it runs a conflict check before it collects case details.
    - **Customer support** confirms the CRM account without reading the caller's contact details aloud.
    - **Marketing lead capture** saves a CRM lead only after separate consent.
- **Real business systems**: Template tools match common business systems, such as Zendesk, Salesforce, Microsoft 365 Calendar and Mail, Microsoft Teams, and Twilio SMS. Start with mock tools, and then connect your own systems through an MCP server or a toolbox. To answer calls on a phone number, connect the agent to Twilio or Teams Phone. For more information, see [Integrate telephony channels with a voice agent](../how-to/voice-agent-telephony-channels).

These rules help callers, but they don't make an agent compliant with the laws and regulations that apply to your business. Review the instructions with your legal and compliance teams before you use an agent with real callers.

## Available templates

The following table lists the voice agent templates and the industry or scenario that each template is built for. The **Agent templates** page in the portal always shows the current list.

| Template | Industry or scenario | What the agent does | Systems it can connect to |
| --- | --- | --- | --- |
| **Appointment scheduler** | Scheduling, clinics | Books, reschedules, or cancels a clinic appointment after it reads the details back. | Microsoft 365 Calendar |
| **Appointment setter** | Sales | Qualifies interest, finds open demo times, books the meeting, and creates a CRM lead for a new prospect. | Microsoft 365 Calendar, Salesforce |
| **Assessment and quiz** | Education, employee training | Gives a spoken 10-question security awareness quiz, scores it with feedback, and saves the score. | Learning records |
| **Collections and payment recovery** | Financial services | Verifies the account holder, explains a past-due balance, captures a payment arrangement, and texts a confirmation. | Salesforce, Twilio SMS |
| **Conference concierge** | Events | Finds Microsoft Ignite 2026 sessions, builds an agenda with clash checks, reports room and time changes, and answers event questions. | Microsoft 365 Calendar |
| **Corporate training role-play coach** | Education, corporate training | Role-plays a difficult customer, sales, employee, or negotiation conversation, and then gives a scored debrief. | Learning records |
| **Customer support** | Customer service | Troubleshoots from help-center articles, confirms the CRM account, and opens a support ticket. | Salesforce, Zendesk |
| **Education and tutoring** | Education | Teaches a topic step by step with practice problems, summarizes progress, and books the next session. | Microsoft 365 Calendar |
| **Front desk receptionist** | Customer service | Answers questions from public support articles. Message recording isn't available. | Front desk tools (required) |
| **Healthcare receptionist** | Healthcare | Books visits, files cancel and reschedule requests as tickets, and answers office questions. | Microsoft 365 Calendar, Zendesk |
| **Hotel reservations** | Hospitality | Checks room availability; books, changes, or cancels a reservation; and answers hotel questions. | Hotel reservation system |
| **Inbound lead qualifier** | Sales | Qualifies a prospect on budget, authority, need, and timeline, books a meeting, and creates a CRM lead. | Microsoft 365 Calendar, Salesforce |
| **Incident response coordinator** | IT operations | Classifies incident severity, texts the on-call owner, and records the incident as a ticket. | Twilio SMS, Zendesk |
| **Insurance advisor** | Insurance | Explores coverage needs, explains typical price ranges, and books a review call with a licensed agent. | Microsoft 365 Calendar, Salesforce |
| **Internal knowledge assistant** | Internal support | Answers internal questions from help-center articles and logs documentation gaps as tickets. | Zendesk |
| **IT access request agent** | IT support | Verifies the employee, classifies an access request against policy, and files the access ticket. | Salesforce, Zendesk |
| **IT help desk** | IT support | Troubleshoots one step at a time from knowledge articles, and escalates by updating or opening a ticket. | Zendesk |
| **Language practice tutor** | Education, language learning | Runs beginner or advanced conversation practice, recaps the session, and books the next lesson. | Microsoft 365 Calendar |
| **Legal intake specialist** | Legal | Collects case facts, saves the intake as a CRM lead for attorney review, and books a consultation. | Microsoft 365 Calendar, Salesforce |
| **Marketing lead capture** | Sales and marketing | Captures a visitor's needs, books a sales call, and creates a CRM lead with separate consent. | Microsoft 365 Calendar, Salesforce |
| **New hire onboarding assistant** | Human resources | Walks a new hire through their role track and benefits, books the first one-on-one with their manager, and texts key contacts. | Microsoft 365 Calendar, Twilio SMS |
| **Order status and tracking** | Customer service, retail | Looks up order status and tracking, logs returns on a support ticket, texts the return details, and notes warranty claims. | Order system, Twilio SMS, Zendesk |
| **Outbound sales representative** | Sales | Pitches with permission, handles objections, books a demo with an account executive, and creates a CRM lead with separate consent. | Microsoft 365 Calendar, Salesforce |
| **Personal voice assistant** | Productivity | Answers quick questions from help-center articles, emails notes, and files follow-up requests for the right team. | Microsoft 365 Mail, Zendesk |
| **Real estate lead follow-up** | Real estate | Follows up a property lead, discusses sample listings, books a showing, and creates a CRM lead with separate consent. | Microsoft 365 Calendar, Salesforce |
| **Receptionist and messaging** | Front desk | Answers company questions, checks a person's presence and texts them, and emails a message to a directory contact. | Microsoft 365 Mail, Microsoft Teams presence, Twilio SMS |
| **Restaurant phone order taker** | Food service | Prepares a pickup or delivery order summary from a sample menu, reads back the total, and texts it. The order isn't submitted. | Twilio SMS |
| **Salon and spa receptionist** | Beauty and wellness | Answers service and price questions, books an appointment, and texts a reminder. | Microsoft 365 Calendar, Twilio SMS |
| **Survey and feedback intake** | Customer feedback | Runs a four-question feedback survey one question at a time and reads the answers back. The answers aren't submitted. | Salesforce |
| **Technical support agent** | Customer service | Troubleshoots from help-center articles, answers verified account questions, and escalates by ticket. | Salesforce, Zendesk |
| **Travel agency trip planner** | Travel | Recommends sample travel packages with ballpark pricing and passes a trip request to a travel agent as a CRM lead. | Salesforce |
| **User research interviewer** | Research | Runs a short discovery interview, adapts to the participant's time, recaps the answers, and saves notes with consent. | Research notes |

## Browse the templates

1. Sign in to the [Microsoft Foundry portal](https://ai.azure.com/).
2. Open your project, and then select **Build** &gt; **Agents**.
3. Select **New agent** &gt; **With agent template**. If the project doesn't have any agents yet, select **Browse templates**.
4. On the **Agent templates** page, search for a template or filter the list by type. Voice templates have the **Voice** tag.

Select a template card to open its details next to the list. The details show what the agent does, the systems it connects to, and a preview that you can talk to.

## Try a template in the preview

Use the **Template preview** to hear how an agent from the template behaves before you configure anything.

When you select a template, Foundry prepares a preview agent in your project. The preview agent uses mock tools that return sample data, so you can try the whole conversation without connecting any system. Preparing the agent can take a few seconds the first time. Start a voice session from the preview and talk to the agent as a caller would.

The preview agent works as follows:

- It's a regular agent in your project, named after the template with a `-preview` suffix, for example `customer-support-preview`. If another agent already uses that name, Foundry adds a number, such as `customer-support-preview-2`.
- Foundry reuses the same preview agent the next time you select the template. It doesn't update or delete the preview agent.
- If you edit the preview agent in the playground, the preview uses your edited version. An edited preview agent might connect to real systems, and it doesn't receive later changes to the template.
- The systems that you choose on the template page apply only to the agent that you create. They don't change the preview agent.

You can delete a preview agent that you no longer need from the **Agents** page. Foundry creates a new one the next time you select the template.

Some templates have no sample data for a system that they require. For these templates, the preview isn't available. Connect the required system, create the agent, and then try it in the playground.

## Choose the systems the agent connects to

Under **Systems this agent connects to**, the template lists each business system that its tools use, such as Salesforce or Zendesk. For each system, choose where the agent's tools come from:

| Option | What the agent uses | When to use it |
| --- | --- | --- |
| **Mock tools** | A shared mock server that returns sample data. No setup is needed. | Try or demo the template. Use only fictional data. |
| **MCP server** | An MCP server connection in your project. | Connect the agent to your own system through a remote MCP server. |
| **Toolbox** | The default version of a toolbox in your project. | Reuse a managed set of tools that other agents also use. |

A system marked **Required** has no mock tools. Connect an MCP server or a toolbox for it before you create the agent.

The tool names in the template's instructions match the tools of the mock server. When you connect your own MCP server or toolbox, make sure that it provides tools with the same purpose, arguments, and results, or update the instructions after you create the agent. A toolbox can add a prefix to tool names. The template instructions already allow for prefixed names.

If a template doesn't connect to any external system, the page shows **No tool configuration needed**. You can add tools after you create the agent.

## Create the agent from the template

1. Under **Name for your new agent**, enter a name, or leave the box empty to generate one. Use up to 63 letters, numbers, and hyphens. The name must start and end with a letter or number, and it can't be the name of an existing agent or of the template's preview agent.
2. Select **Open in playground**.

Foundry creates the agent in your project with the systems that you chose and opens it in the playground. Start a voice session and try the scenario again. If you connected real systems, use test records and confirm the tool calls in the conversation.

## Customize the agent

An agent that you create from a template is a regular voice-based agent. It's not linked to the template, so later changes to the template don't affect it, and your changes don't affect the template.

In the playground, you can change the agent's model, voice, greeting, and instructions. Each save creates a new agent version. For the full set of options, see [Configure a voice agent](../how-to/configure-voice-agent).

Most templates split the conversation into stages, such as identifying the caller's issue, troubleshooting, and escalating. Each stage is an inline subagent with its own instructions, tools, and handoff conditions. The tools that you choose on the template page belong to the stages that use them, not to the agent as a whole. To change what happens in a stage, which tools it can call, or when the conversation moves to another stage, see [Use an inline subagent in a voice-based agent](../how-to/use-inline-subagent-voice-agent).

When you change the instructions, keep the rules that protect callers, such as confirming details before a tool submits anything and verifying identity before sharing account information. To refine the instructions further, see [Optimize voice agent instructions](../how-to/optimize-voice-agent-instructions).

Before you use the agent with real callers:

- Start with mock tools to confirm that the conversation flow fits your scenario, and then connect real systems one at a time.
- Use only fictional data with mock tools. The mock server is shared and isn't meant for real customer information.
- Give an MCP server or toolbox only the permissions that the template's tools need, and test with records that you can safely read and change.
- Test with calls that represent your callers, including corrections, interruptions, and requests that the agent should decline.
- Review the agent's tracing after each test call to confirm which stage answered and which tools it called. For more information, see [Voice agent tracing, monitoring, and evaluation](../concepts/voice-agent-observability).

## Explore related examples on GitHub

The [microsoft/voice-agent](https://github.com/microsoft/voice-agent) repository on GitHub has examples of voice-based agents for many of the same scenarios as the templates. Each example has a folder under [`samples`](https://github.com/microsoft/voice-agent/tree/main/samples), such as [`samples/example5_customer_support`](https://github.com/microsoft/voice-agent/tree/main/samples/example5_customer_support) for a customer support agent. Each folder contains:

- `agent.json`: The agent definition, including the instructions, greeting, voice, stages, and tools.
- `README.md`: What the example does, its stages and tools, and when to use it.

The examples are maintained separately from the templates in the Foundry portal, so their instructions and tools can differ.

Use the examples to:

- See how a complete agent definition organizes stages, tools, and handoff conditions.
- Start a code-first agent from an example definition. To create the agent by using the SDK, select the **Python SDK** or **JavaScript SDK** tab at the top of this quickstart. If the definition uses inline subagents, which are in preview, also add the preview opt-in shown in [Use an inline subagent in a voice-based agent](../how-to/use-inline-subagent-voice-agent).
- Run the examples against the shared mock server or your own tools. The repository explains how to [connect real tools](https://github.com/microsoft/voice-agent/blob/main/docs/05_connect_real_tools.md).

::: zone-end

::: zone pivot="python"

## Install the packages

These examples require version 2.11.0 or later of the Azure AI Projects client library.

Install the `voice` extra, which supplies `websockets` for synchronous connections and `aiohttp` for asynchronous connections.

```bash
python -m pip install "azure-ai-projects[voice]>=2.11.0"
```

Realtime sessions and stored conversations use `project_client.voice_agents`.

## Set environment variables

In Bash:

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<account>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_VOICE_AGENT_NAME="my-voice-agent"
export FOUNDRY_VOICE_AGENT_MODEL="gpt-realtime"
```

In PowerShell:

```powershell
$env:FOUNDRY_PROJECT_ENDPOINT = "https://<account>.services.ai.azure.com/api/projects/<project>"
$env:FOUNDRY_VOICE_AGENT_NAME = "my-voice-agent"
$env:FOUNDRY_VOICE_AGENT_MODEL = "gpt-realtime"
```

Find the project endpoint on the **Overview** page of your project in the Foundry portal.

`FOUNDRY_VOICE_AGENT_MODEL` identifies the service-managed model in the managed example, or your existing deployment in the self-deployed example. The generation example lets the service choose the model.

## Create the voice agent

A voice agent is an agent whose `kind` is `voice`. Its definition holds the model, instructions, and voice configuration. The examples enable conversation storage by setting `store` to `true`, so you can read back the transcript and audio later.

Choose one of the following creation methods, and use a unique agent name. Save the complete example, and then run it as described after the examples.

### Generate from natural language

Describe what the agent should do in `goal`. Foundry uses this natural-language description to generate instructions and creates the agent with a complete voice configuration.

The following script lets the service choose the model and prints the generated instructions for review. It then enables storage in a new version, preserving the generated audio, greeting, tools, and other settings.

```python
import os

from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import (
    AgentKind,
    GenerateVoiceAgentRequest,
    VoiceAgentDefinition,
)
from azure.identity import DefaultAzureCredential

endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
agent_name = os.environ["FOUNDRY_VOICE_AGENT_NAME"]

with (
    DefaultAzureCredential() as credential,
    AIProjectClient(
        endpoint=endpoint, credential=credential
    ) as project_client,
):
    generated = project_client.agents.create_from_prompt(
        GenerateVoiceAgentRequest(
            kind=AgentKind.VOICE,
            name=agent_name,
            goal=(
                "Create a friendly voice assistant that answers general "
                "questions. Keep replies to one or two sentences."
            ),
        )
    )
    definition = generated.versions.latest.definition
    if not isinstance(definition, VoiceAgentDefinition):
        raise TypeError("The generated agent must have a voice definition.")

    print(f"Generated instructions:\n{definition.instructions}")
    definition.store = True
    created = project_client.agents.create_version(
        agent_name=agent_name, definition=definition
    )
    print(f"Created voice agent '{agent_name}', version {created.version}")
```

Reference: [Azure AI Projects client library for Python](https://aka.ms/azsdk/azure-ai-projects-v2/python/code).

Review the printed instructions before talking to the agent. To customize the generated configuration, edit fields on its definition, such as `instructions`, and save another version.

### Create from an explicit definition

Use `VoiceAgentDefinition` when you want to specify the instructions, model, and voice yourself. This model sets `kind="voice"` and `sub_protocol="realtime"` automatically. The following script creates an agent version with an Azure standard voice and conversation storage enabled.

```python
import os

from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import (
    VoiceAgentAudioConfig,
    VoiceAgentAudioOutputConfig,
    VoiceAgentDefinition,
    VoiceModelType,
    VoiceOutputModality,
    VoiceType,
)
from azure.identity import DefaultAzureCredential

endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
agent_name = os.environ["FOUNDRY_VOICE_AGENT_NAME"]
model = os.environ.get("FOUNDRY_VOICE_AGENT_MODEL", "gpt-realtime")

definition = VoiceAgentDefinition(
    model_type=VoiceModelType.MANAGED,
    model=model,
    instructions=(
        "You are a friendly voice assistant. "
        "Keep replies to one or two sentences."
    ),
    audio=VoiceAgentAudioConfig(
        output=VoiceAgentAudioOutputConfig(
            voice="en-US-AvaNeural",
            voice_type=VoiceType.AZURE_STANDARD,
        ),
    ),
    output_modalities=[VoiceOutputModality.AUDIO],
    store=True,
)

with (
    DefaultAzureCredential() as credential,
    AIProjectClient(
        endpoint=endpoint, credential=credential
    ) as project_client,
):
    created = project_client.agents.create_version(
        agent_name=agent_name, definition=definition
    )
    print(f"Created voice agent '{agent_name}', version {created.version}")
```

Reference: [Azure AI Projects client library for Python](https://aka.ms/azsdk/azure-ai-projects-v2/python/code).

### Create with a self-deployed model

Use this example instead of the managed-model example to reuse a compatible deployment in the Foundry resource that contains your project. Set `FOUNDRY_VOICE_AGENT_MODEL` to the **deployment name**, not the provider's model name. Keep the project endpoint and unique agent name from Set environment variables.

For example, change the model setting in Bash:

```bash
export FOUNDRY_VOICE_AGENT_MODEL="<existing-model-deployment-name>"
```

Or in PowerShell:

```powershell
$env:FOUNDRY_VOICE_AGENT_MODEL = "<existing-model-deployment-name>"
```

The deployment must already exist. The following script creates a voice-agent version that uses it; it doesn't create or change the model deployment.

```python
import os

from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import (
    VoiceAgentAudioConfig,
    VoiceAgentAudioOutputConfig,
    VoiceAgentDefinition,
    VoiceModelType,
    VoiceOutputModality,
    VoiceType,
)
from azure.identity import DefaultAzureCredential

endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
agent_name = os.environ["FOUNDRY_VOICE_AGENT_NAME"]
deployment_name = os.environ["FOUNDRY_VOICE_AGENT_MODEL"]

definition = VoiceAgentDefinition(
    model_type=VoiceModelType.SELF_DEPLOYED,
    model=deployment_name,
    instructions="You are a helpful voice assistant. Keep replies short.",
    audio=VoiceAgentAudioConfig(
        output=VoiceAgentAudioOutputConfig(
            voice="en-US-AvaNeural",
            voice_type=VoiceType.AZURE_STANDARD,
        ),
    ),
    output_modalities=[VoiceOutputModality.AUDIO],
    store=True,
)

with (
    DefaultAzureCredential() as credential,
    AIProjectClient(
        endpoint=endpoint, credential=credential
    ) as project_client,
):
    created = project_client.agents.create_version(
        agent_name=agent_name, definition=definition
    )
    print(f"Created voice agent '{agent_name}', version {created.version}")
```

Reference: [Python voice-agent tools sample](https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/python/voice-agents/voice_agent_with_tools.py).

The same creation pattern works with supported realtime and text-model deployments. Confirm that the selected deployment supports the voice settings in this example. For model choices and latency guidance, see [Choose a managed or self-deployed model](../how-to/configure-voice-agent#choose-a-managed-or-self-deployed-model).

### Run your chosen example

Run the file that contains your chosen example.

Save the example as `create_voice_agent.py`.

```bash
python create_voice_agent.py
```

Each create or update action produces a new immutable version. The agent's endpoint is live as soon as the first version exists, with no separate agent deployment step. Continue with the same talk, read-back, and cleanup steps for any creation method.

Cleanup removes the test agent and its conversation, but it doesn't remove your model deployment.

## Talk to the agent

Connect to the agent's realtime session, send a turn, and collect the spoken reply. This script types the turn so it runs without audio hardware, and it saves the agent's spoken response to a WAV file.

If the agent has a startup greeting, the script receives that response before sending the user turn. Only the reply to the user turn is saved in `reply.wav`.

Create a file named `talk_to_voice_agent.py`:

```python
import os
import wave

from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import (
    RealtimeConversationItemMessageUser,
    RealtimeConversationItemMessageUserContent,
    RealtimeConversationItemType,
    RealtimeServerEventError,
    RealtimeServerEventResponseAudioDelta,
    RealtimeServerEventResponseAudioTranscriptDone,
    RealtimeServerEventResponseDone,
    RealtimeServerEventSessionCreated,
    VoiceAgentDefinition,
)
from azure.identity import DefaultAzureCredential

endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
agent_name = os.environ["FOUNDRY_VOICE_AGENT_NAME"]

conversation_id = None

with (
    DefaultAzureCredential() as credential,
    AIProjectClient(
        endpoint=endpoint, credential=credential
    ) as project_client,
):
    agent = project_client.agents.get(agent_name=agent_name)
    latest = agent.versions.latest
    definition = latest.definition
    if not isinstance(definition, VoiceAgentDefinition):
        raise TypeError("The agent must have a voice definition.")

    with project_client.voice_agents.realtime.connect(
        agent_name=agent_name
    ) as conn:

        def receive_response() -> tuple[str | None, list[bytes]]:
            session_conversation_id: str | None = None
            chunks: list[bytes] = []
            while True:
                event = conn.recv(timeout=45)
                if isinstance(event, RealtimeServerEventSessionCreated):
                    session_conversation_id = event.conversation_id
                elif isinstance(event, RealtimeServerEventResponseAudioDelta):
                    chunks.append(event.delta)
                elif isinstance(
                    event, RealtimeServerEventResponseAudioTranscriptDone
                ):
                    print(f"Agent: {event.transcript}")
                elif isinstance(event, RealtimeServerEventError):
                    raise RuntimeError(event.error.message)
                elif isinstance(event, RealtimeServerEventResponseDone):
                    if event.response.status != "completed":
                        raise RuntimeError(
                            f"Response status: {event.response.status}"
                        )
                    return session_conversation_id, chunks

        if definition.greeting is not None:
            # A greeting has its own response.done, before the user's reply.
            conversation_id, _ = receive_response()

        conn.conversation.item.create(
            item=RealtimeConversationItemMessageUser(
                type=RealtimeConversationItemType.MESSAGE,
                content=[
                    RealtimeConversationItemMessageUserContent(
                        type="input_text",
                        text="Hi. In one sentence, what can you help me with?",
                    )
                ]
            )
        )
        conn.response.create()
        response_conversation_id, audio_chunks = receive_response()
        conversation_id = response_conversation_id or conversation_id

if not conversation_id:
    raise RuntimeError("No persisted conversation ID was returned.")
if not audio_chunks:
    raise RuntimeError("No audio was returned for the user turn.")

# The reply arrives as PCM16, mono, 24 kHz.
with wave.open("reply.wav", "wb") as wav:
    wav.setnchannels(1)
    wav.setsampwidth(2)
    wav.setframerate(24000)
    wav.writeframes(b"".join(audio_chunks))

print(f"Saved reply.wav ({len(audio_chunks)} audio chunks)")
print(f"Conversation id: {conversation_id}")
```

Reference: [Azure AI Projects client library for Python](https://aka.ms/azsdk/azure-ai-projects-v2/python/code).

Run the file, and then play `reply.wav`.

```bash
python talk_to_voice_agent.py
```

A few things to note about the session:

- The agent owns the model, instructions, voice, turn detection, and noise suppression on the server, so the client doesn't send a `session.update` event.
- The persisted conversation ID arrives on the `session.created` event, not at the end of the response.
- The reply streams as a series of audio deltas. A production client plays each delta as it arrives instead of buffering the whole response.

For a hands-free version that streams microphone audio and supports interruptions, see the [Python realtime-audio conversation sample](https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/python/voice-agents/voice_agent_realtime_audio_conversation_async.py). It uses server-side turn detection to decide when you finish speaking.

## Read the conversation back

Because you set `store` to `true`, the transcript and audio are saved. Use the conversation ID that the previous script printed to read the transcript in chronological order.

Create a file named `read_conversation.py`:

```python
import os
import sys

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
agent_name = os.environ["FOUNDRY_VOICE_AGENT_NAME"]
conversation_id = sys.argv[1]

with (
    DefaultAzureCredential() as credential,
    AIProjectClient(
        endpoint=endpoint, credential=credential
    ) as project_client,
):
    conversations = project_client.voice_agents.conversations

    conversation = conversations.get(agent_name, conversation_id)
    print(f"Conversation {conversation.id}: status={conversation.status}")

    for item in conversations.list_items(
        agent_name, conversation_id, order="asc"
    ):
        parts = [
            (part.get("transcript") or part.get("text") or "").strip()
            for part in (item.get("content") or [])
        ]
        transcript = " ".join(part for part in parts if part)
        if transcript:
            print(f"  {item.get('role')}: {transcript}")
```

Reference: [Azure AI Projects client library for Python](https://aka.ms/azsdk/azure-ai-projects-v2/python/code).

Run the file with the conversation ID.

```bash
python read_conversation.py <conversation-id>
```

You can also download the merged call recording, with the caller on the left channel and the agent on the right. See [Voice agent tracing, monitoring, and evaluation](../concepts/voice-agent-observability).

## Clean up resources

Delete the stored conversation and agent when you're finished. Deleting them doesn't delete your project.

```python
import os
import sys

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
agent_name = os.environ["FOUNDRY_VOICE_AGENT_NAME"]
conversation_id = sys.argv[1]

with (
    DefaultAzureCredential() as credential,
    AIProjectClient(
        endpoint=endpoint, credential=credential
    ) as project_client,
):
    project_client.voice_agents.conversations.delete(
        agent_name, conversation_id
    )
    project_client.agents.delete(agent_name=agent_name)
```

Reference: [Azure AI Projects client library for Python](https://aka.ms/azsdk/azure-ai-projects-v2/python/code).

Save the example as `clean_up.py`, and run it with the conversation ID:

```bash
python clean_up.py <conversation-id>
```

::: zone-end

::: zone pivot="javascript"

## Install the packages

These examples require version 2.11.0 or later of the Azure AI Projects client library.

In your application directory, install the packages. The client library includes the WebSocket dependencies that `project.voiceAgents.realtime` requires.

```bash
npm init --yes
npm pkg set type=module
npm install "@azure/ai-projects@>=2.11.0" @azure/identity
```

Realtime sessions use `project.voiceAgents.realtime`, and stored conversations use `project.voiceAgents.conversations`.

## Set environment variables

In Bash:

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<account>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_VOICE_AGENT_NAME="my-voice-agent"
export FOUNDRY_VOICE_AGENT_MODEL="gpt-realtime"
```

In PowerShell:

```powershell
$env:FOUNDRY_PROJECT_ENDPOINT = "https://<account>.services.ai.azure.com/api/projects/<project>"
$env:FOUNDRY_VOICE_AGENT_NAME = "my-voice-agent"
$env:FOUNDRY_VOICE_AGENT_MODEL = "gpt-realtime"
```

Find the project endpoint on the **Overview** page of your project in the Foundry portal.

`FOUNDRY_VOICE_AGENT_MODEL` identifies the service-managed model in the managed example, or your existing deployment in the self-deployed example. The generation example lets the service choose the model.

## Create the voice agent

A voice agent is an agent whose `kind` is `voice`. Its definition holds the model, instructions, and voice configuration. The examples enable conversation storage by setting `store` to `true`, so you can read back the transcript and audio later.

Choose one of the following creation methods, and use a unique agent name. Save the complete example, and then run it as described after the examples.

### Generate from natural language

Describe what the agent should do in `goal`. Foundry uses this natural-language description to generate instructions and creates the agent with a complete voice configuration.

The following script lets the service choose the model and prints the generated instructions for review. It then enables storage in a new version, preserving the generated audio, greeting, tools, and other settings.

```javascript
import { AIProjectClient } from "@azure/ai-projects";
import { DefaultAzureCredential } from "@azure/identity";

const projectEndpoint = /** @type {string} */ (
    process.env.FOUNDRY_PROJECT_ENDPOINT
);
const agentName = /** @type {string} */ (
    process.env.FOUNDRY_VOICE_AGENT_NAME
);
if (!projectEndpoint || !agentName) {
    throw new Error(
        "Set FOUNDRY_PROJECT_ENDPOINT and FOUNDRY_VOICE_AGENT_NAME.",
    );
}
async function main() {
    const project = new AIProjectClient(
        projectEndpoint,
        new DefaultAzureCredential(),
    );
    const generated = await project.agents.createFromPrompt(
        {
            kind: "voice",
            name: agentName,
            model_type: "managed",
            use_case: "General assistance",
            goal: "Create a friendly voice assistant that answers general " +
                "questions. Keep replies to one or two sentences.",
        },
    );
    const generatedDefinition = generated.versions.latest.definition;
    if (generatedDefinition.kind !== "voice" ||
        !("sub_protocol" in generatedDefinition) ||
        generatedDefinition.sub_protocol !== "realtime") {
        throw new Error("The generated agent must use the realtime protocol.");
    }
    const definition = /** @type {import("@azure/ai-projects").VoiceAgentDefinition} */ (
        generatedDefinition
    );

    console.log(`Generated instructions:\n${definition.instructions}`);
    definition.store = true;
    const created = await project.agents.createVersion(
        agentName,
        definition,
    );
    console.log(`Created voice agent '${agentName}', version ${created.version}`);
}

main().catch((error) => {
    console.error("Sample failed:", error);
    process.exitCode = 1;
});
```

Reference: [Generate a voice agent JavaScript sample](https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/javascript/voice-agents/generate-voice-agent/app.js).

Review the printed instructions before talking to the agent. To customize the generated configuration, edit fields on its definition, such as `instructions`, and save another version.

### Create from an explicit definition

Use a voice agent definition when you want to specify the instructions, model, and voice yourself. The following script creates an agent version with an Azure standard voice and conversation storage enabled.

```javascript
import { AIProjectClient } from "@azure/ai-projects";
import { DefaultAzureCredential } from "@azure/identity";

const projectEndpoint = /** @type {string} */ (
    process.env.FOUNDRY_PROJECT_ENDPOINT
);
const agentName = /** @type {string} */ (
    process.env.FOUNDRY_VOICE_AGENT_NAME
);
const model = process.env.FOUNDRY_VOICE_AGENT_MODEL || "gpt-realtime";
if (!projectEndpoint || !agentName) {
    throw new Error(
        "Set FOUNDRY_PROJECT_ENDPOINT and FOUNDRY_VOICE_AGENT_NAME.",
    );
}
/** @type {import("@azure/ai-projects").VoiceAgentDefinition} */
const definition = {
    kind: "voice",
    sub_protocol: "realtime",
    model_type: "managed",
    model,
    instructions: "You are a friendly voice assistant. " +
        "Keep replies to one or two sentences.",
    audio: {
        output: {
            voice: "en-US-AvaNeural",
            voice_type: "azure-standard",
        },
    },
    output_modalities: ["audio"],
    store: true,
};

async function main() {
    const project = new AIProjectClient(
        projectEndpoint,
        new DefaultAzureCredential(),
    );
    const created = await project.agents.createVersion(
        agentName,
        definition,
    );
    console.log(`Created voice agent '${agentName}', version ${created.version}`);
}

main().catch((error) => {
    console.error("Sample failed:", error);
    process.exitCode = 1;
});
```

Reference: [Configure a voice agent JavaScript sample](https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/javascript/voice-agents/configure-voice-agent/app.js).

### Create with a self-deployed model

Use this example instead of the managed-model example to reuse a compatible deployment in the Foundry resource that contains your project. Set `FOUNDRY_VOICE_AGENT_MODEL` to the **deployment name**, not the provider's model name. Keep the project endpoint and unique agent name from Set environment variables.

For example, change the model setting in Bash:

```bash
export FOUNDRY_VOICE_AGENT_MODEL="<existing-model-deployment-name>"
```

Or in PowerShell:

```powershell
$env:FOUNDRY_VOICE_AGENT_MODEL = "<existing-model-deployment-name>"
```

The deployment must already exist. The following script creates a voice-agent version that uses it; it doesn't create or change the model deployment.

```javascript
import { AIProjectClient } from "@azure/ai-projects";
import { DefaultAzureCredential } from "@azure/identity";

const projectEndpoint = process.env.FOUNDRY_PROJECT_ENDPOINT;
const agentName = process.env.FOUNDRY_VOICE_AGENT_NAME;
const deploymentName = process.env.FOUNDRY_VOICE_AGENT_MODEL;
if (!projectEndpoint || !agentName || !deploymentName) {
    throw new Error(
        "Set FOUNDRY_PROJECT_ENDPOINT and FOUNDRY_VOICE_AGENT_NAME, " +
        "and set FOUNDRY_VOICE_AGENT_MODEL to your deployment name.",
    );
}

/** @type {import("@azure/ai-projects").VoiceAgentDefinition} */
const definition = {
    kind: "voice",
    sub_protocol: "realtime",
    model_type: "self_deployed",
    model: deploymentName,
    instructions: "You are a helpful voice assistant. Keep replies short.",
    audio: {
        output: {
            voice: "en-US-AvaNeural",
            voice_type: "azure-standard",
        },
    },
    output_modalities: ["audio"],
    store: true,
};

/**
 * @param {string} endpoint
 * @param {string} name
 */
async function main(endpoint, name) {
    const project = new AIProjectClient(
        endpoint,
        new DefaultAzureCredential(),
    );
    const created = await project.agents.createVersion(
        name,
        definition,
    );
    console.log(
        `Created voice agent '${name}', version ${created.version}`,
    );
}

main(projectEndpoint, agentName).catch((error) => {
    console.error("Sample failed:", error);
    process.exitCode = 1;
});
```

Reference: [Voice agent JavaScript sample](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/ai/ai-projects/samples/v2/javascript/agents/agentVoice.js).

The same creation pattern works with supported realtime and text-model deployments. Confirm that the selected deployment supports the voice settings in this example. For model choices and latency guidance, see [Choose a managed or self-deployed model](../how-to/configure-voice-agent#choose-a-managed-or-self-deployed-model).

### Run your chosen example

Run the file that contains your chosen example.

Save the example as `create_voice_agent.js`, and run it with Node.js:

```bash
node create_voice_agent.js
```

Each create or update action produces a new immutable version. The agent's endpoint is live as soon as the first version exists, with no separate agent deployment step. Continue with the same talk, read-back, and cleanup steps for any creation method.

Cleanup removes the test agent and its conversation, but it doesn't remove your model deployment.

## Talk to the agent

Connect to the agent's realtime session, send a turn, and collect the spoken reply. This script types the turn so it runs without audio hardware, and it saves the agent's spoken response as raw PCM audio.

If the agent has a startup greeting, the script receives that response before sending the user turn. Only the reply to the user turn is saved in `reply.pcm`.

Create a file named `talk_to_voice_agent.js`:

```javascript
import { AIProjectClient } from "@azure/ai-projects";
import { DefaultAzureCredential } from "@azure/identity";
import { once } from "node:events";
import { createWriteStream } from "node:fs";
import { finished } from "node:stream/promises";

const projectEndpoint = /** @type {string} */ (
    process.env.FOUNDRY_PROJECT_ENDPOINT
);
const agentName = /** @type {string} */ (
    process.env.FOUNDRY_VOICE_AGENT_NAME
);
if (!projectEndpoint || !agentName) {
    throw new Error(
        "Set FOUNDRY_PROJECT_ENDPOINT and FOUNDRY_VOICE_AGENT_NAME.",
    );
}
const pcmSampleRate = 24_000;

/**
 * @param {import("node:fs").WriteStream} output
 * @param {Uint8Array} audio
 */
async function writeAudio(output, audio) {
    if (!output.write(audio)) {
        await once(output, "drain");
    }
}

/**
 * @param {import("@azure/ai-projects").AgentDefinitionUnion} definition
 * @returns {definition is import("@azure/ai-projects").VoiceAgentDefinition}
 */
function isVoiceAgentDefinition(definition) {
    return definition.kind === "voice" &&
        "sub_protocol" in definition &&
        definition.sub_protocol === "realtime" &&
        "model_type" in definition &&
        (definition.model_type === "managed" ||
            definition.model_type === "self_deployed") &&
        "model" in definition &&
        typeof definition.model === "string";
}

async function main() {
    const project = new AIProjectClient(
        projectEndpoint,
        new DefaultAzureCredential(),
    );
    const agent = await project.agents.get(agentName);
    const definition = agent.versions.latest.definition;
    if (!isVoiceAgentDefinition(definition)) {
        throw new Error("The agent must have a voice definition.");
    }

    const connection = await project.voiceAgents.realtime.connect(
        agentName,
        { store: true },
    );
    const audioOutput = createWriteStream("reply.pcm");
    let audioByteCount = 0;
    let conversationId;
    let userTurnSent = !definition.greeting;

    try {
        await connection.configureSession({
            type: "realtime",
            output_modalities: ["text", "audio"],
            audio: {
                output: {
                    format: { type: "audio/pcm", rate: pcmSampleRate },
                },
            },
        });
        if (userTurnSent) {
            await connection.sendText(
                "Hi. In one sentence, what can you help me with?",
            );
        }

        for await (const event of connection) {
            if (event.type === "session.created") {
                conversationId = event.conversation_id;
            } else if (event.type === "response.output_audio.delta" &&
                userTurnSent) {
                audioByteCount += event.delta.byteLength;
                await writeAudio(audioOutput, event.delta);
            } else if (event.type === "response.output_audio_transcript.done" &&
                userTurnSent) {
                console.log(`Agent: ${event.transcript}`);
            } else if (event.type === "error") {
                throw new Error(
                    `${event.error.code ?? "voice_agent_error"}: ` +
                        event.error.message,
                );
            } else if (event.type === "response.done") {
                if (event.response.status !== "completed") {
                    throw new Error(`Response status: ${event.response.status}`);
                }
                if (!userTurnSent) {
                    userTurnSent = true;
                    await connection.sendText(
                        "Hi. In one sentence, what can you help me with?",
                    );
                } else {
                    await connection.close();
                }
            }
        }
    } finally {
        audioOutput.end();
        try {
            await finished(audioOutput);
        } finally {
            await connection.dispose();
        }
    }

    if (!conversationId) {
        throw new Error("No persisted conversation ID was returned.");
    }
    if (audioByteCount === 0) {
        throw new Error("No audio was returned for the user turn.");
    }
    console.log(`Saved reply.pcm (${audioByteCount} bytes)`);
    console.log(`Audio format: PCM16, ${pcmSampleRate} Hz, mono.`);
    console.log(`Conversation id: ${conversationId}`);
}

main().catch((error) => {
    console.error("Sample failed:", error);
    process.exitCode = 1;
});
```

Reference: [Realtime text and tools JavaScript sample](https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/javascript/voice-agents/realtime-text-and-tools/app.js).

Run the file. The output is PCM16, 24-kHz, mono audio.

```bash
node talk_to_voice_agent.js
```

A few things to note about the session:

- The agent owns the model, instructions, voice, turn detection, and noise suppression on the server. The client uses `configureSession` only to request text and 24-kHz PCM audio output.
- The persisted conversation ID arrives on the `session.created` event, not at the end of the response.
- The reply streams as a series of audio deltas. A production client plays each delta as it arrives instead of buffering the whole response.

For a hands-free version that streams microphone audio and supports interruptions, see the [JavaScript realtime-audio sample](https://github.com/microsoft-foundry/foundry-samples/tree/main/samples/javascript/voice-agents/realtime-audio). This sample uses server-side turn detection to decide when you finish speaking.

## Read the conversation back

Because you set `store` to `true`, the transcript and audio are saved. Use the conversation ID that the previous script printed to read the transcript in chronological order.

Create a file named `read_conversation.js`:

```javascript
import { AIProjectClient } from "@azure/ai-projects";
import { DefaultAzureCredential } from "@azure/identity";

const projectEndpoint = /** @type {string} */ (
    process.env.FOUNDRY_PROJECT_ENDPOINT
);
const agentName = /** @type {string} */ (
    process.env.FOUNDRY_VOICE_AGENT_NAME
);
const conversationId = /** @type {string} */ (process.argv[2]);
if (!projectEndpoint || !agentName || !conversationId) {
    throw new Error(
        "Set the project endpoint and agent name, then pass a conversation ID.",
    );
}
/** @param {import("@azure/ai-projects").RealtimeConversationItemUnion} item */
function summarizeItem(item) {
    if (item.type !== "message" || !("content" in item)) {
        return `[${item.type}]`;
    }
    const text = item.content
        .map((part) => part.text ??
            ("transcript" in part ? part.transcript : undefined) ?? "")
        .filter(Boolean)
        .join(" ");
    return `[${item.role}] ${text || "(no text content)"}`;
}

async function main() {
    const project = new AIProjectClient(
        projectEndpoint,
        new DefaultAzureCredential(),
    );
    const conversations = project.voiceAgents.conversations;
    const conversation = await conversations.get(
        agentName,
        conversationId,
    );
    console.log(`Conversation ${conversation.id}: status=${conversation.status}`);

    for await (const item of conversations.listItems(
        agentName,
        conversationId,
        { order: "asc" },
    )) {
        console.log(`  ${summarizeItem(item)}`);
    }
}

main().catch((error) => {
    console.error("Sample failed:", error);
    process.exitCode = 1;
});
```

Reference: [Voice agent conversation JavaScript sample](https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/javascript/voice-agents/voice-agent-conversations/app.js).

Run the file with the conversation ID.

```bash
node read_conversation.js <conversation-id>
```

You can also download the merged call recording, with the caller on the left channel and the agent on the right. See [Voice agent tracing, monitoring, and evaluation](../concepts/voice-agent-observability).

## Clean up resources

Delete the stored conversation and agent when you're finished. Deleting them doesn't delete your project.

```javascript
import { AIProjectClient } from "@azure/ai-projects";
import { DefaultAzureCredential } from "@azure/identity";

const projectEndpoint = /** @type {string} */ (
    process.env.FOUNDRY_PROJECT_ENDPOINT
);
const agentName = /** @type {string} */ (
    process.env.FOUNDRY_VOICE_AGENT_NAME
);
const conversationId = /** @type {string} */ (process.argv[2]);
if (!projectEndpoint || !agentName || !conversationId) {
    throw new Error(
        "Set the project endpoint and agent name, then pass a conversation ID.",
    );
}
async function main() {
    const project = new AIProjectClient(
        projectEndpoint,
        new DefaultAzureCredential(),
    );
    await project.voiceAgents.conversations.delete(
        agentName,
        conversationId,
    );
    console.log(`Deleted conversation: ${conversationId}`);
    const deleted = await project.agents.delete(agentName);
    console.log(`Deleted: ${deleted.deleted}`);
}

main().catch((error) => {
    console.error("Sample failed:", error);
    process.exitCode = 1;
});
```

Reference: [Manage a voice agent JavaScript sample](https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/javascript/voice-agents/manage-voice-agent/app.js).

Save the example as `clean_up.js`, and run it with the conversation ID:

```bash
node clean_up.js <conversation-id>
```

::: zone-end

::: zone pivot="azd"

## Initialize a prompt-based voice agent

Create an empty working directory, and start the interactive initialization flow:

```azurecli
mkdir voice-agent-quickstart
cd voice-agent-quickstart
azd ai agent init
```

Choose these options:

1. For **How do you want to initialize your agent?**, select **Create a prompt voice agent**.
2. Enter `voice-guide-managed` as the agent name.
3. Select **Create a new Foundry project**.
4. Select your tenant and Azure subscription.
5. Select a region where prompt-based voice agents are available.

Alternatively, specify the agent type, name, model, and output voice in the command. Run this command in the empty working directory in place of `azd ai agent init`:

```powershell
azd ai agent init --kind prompt-voice `
    --agent-name voice-guide-managed `
    --model gpt-realtime `
    --voice en-US-AvaNeural
```

Complete the Foundry project selection when prompted. The `--voice` option applies only when creating a new prompt voice agent. Don't combine this flow with hosted code options such as `--src`, `--runtime`, `--protocol`, or `--deploy-mode`.

When initialization finishes, change to the generated project directory:

```azurecli
cd voice-guide-managed
```

Open `azure.yaml`, and confirm that the agent definition contains these values:

```yaml
kind: prompt-voice
model:
  id: gpt-realtime
modelType: managed
name: voice-guide-managed
```

The `managed` model type tells Foundry to provide the realtime model for the agent. You don't need to create a model deployment separately.

The CLI generates `kind: prompt-voice` for compatibility. `kind: voice` is also accepted; you don't need to rename the generated kind. To use your own model deployment, see [Choose a managed or self-deployed model](../how-to/configure-voice-agent#choose-a-managed-or-self-deployed-model).

## Provision the Foundry project

Provision the Foundry project and its required resources:

```azurecli
azd provision
```

## Deploy the voice agent

Deploy the prompt-based voice agent:

```azurecli
azd deploy voice-guide-managed
```

When deployment finishes, `azd` confirms the agent name, version, and endpoint for the active environment.

## Test the voice agent

`azd ai agent invoke` doesn't start voice conversations. When it recognizes a voice service in `azure.yaml`, it returns an error with guidance to use the Foundry portal, even if you specify `--protocol responses`. Use the playground to test the agent:

1. Open the [Foundry portal](https://ai.azure.com) and sign in.
2. Select the Foundry project that you provisioned.
3. In the left navigation, select **Build** &gt; **Agents**.
4. Select **voice-guide-managed**, and then select **Open in playground**.
5. Start a voice session, and speak to the agent.
6. Confirm that the agent responds with synthesized speech and that the playground doesn't report a runtime error.

## Clean up resources

Run the cleanup command from the project directory:

Warning

If this `azd` environment created the Foundry project, `azd down` permanently deletes the project's resource group and everything in it. If you initialized the agent with an existing project, the command leaves that project and its resources in place.

```azurecli
azd down
```

::: zone-end
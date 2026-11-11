---
layout: Conceptual
title: Use a hosted agent as the conversation engine in a voice agent - Microsoft Foundry | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/foundry/how-to/voice-first-with-hosted-agent
breadcrumb_path: ../../breadcrumb/azure-ai/toc.json
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
author: knitvoger
learn_banner_products:
- azure
manager: mcleans
ms.author: wujin
ms.collection: ce-skilling-ai-copilot
ms.update-cycle: 90-days
ms.service: microsoft-foundry
description: Learn how to create a voice agent in Microsoft Foundry that uses a hosted agent as its conversation engine, including deployment and SDK setup.
ms.date: 2026-11-05T00:00:00.0000000Z
ms.topic: how-to
ms.subservice: foundry-agent-service
ms.custom: preview, doc-kit-assisted
ai-usage: ai-assisted
locale: en-us
document_id: 3c5040c9-e9e7-7df2-a627-78c93550619e
document_version_independent_id: 58fb54bb-4fe8-6caa-a260-434b43d66dd5
original_content_git_url: https://github.com/MicrosoftDocs/azure-ai-docs-pr/blob/live/articles/foundry/how-to/voice-first-with-hosted-agent.md
site_name: Docs
depot_name: Learn.azure-ai
page_type: conceptual
toc_rel: ../toc.json
asset_id: foundry/how-to/voice-first-with-hosted-agent
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/foundry/how-to/voice-first-with-hosted-agent.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/64b65f6c-101f-411a-9b83-9f577fab52d0
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1a667fd1-8145-4b11-af0f-9f5de205a6e5
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: eddbf1ea-d82c-85f0-88e6-671df88141cd
---

# Use a hosted agent as the conversation engine in a voice agent - Microsoft Foundry | Microsoft Learn

In this article, you create a voice agent in Microsoft Foundry that uses a hosted agent as its conversation engine. You keep conversation logic in your application code while Voice Live provides the managed speech experience.

Important

Items marked preview in this article are currently in preview. This preview is provided without a service-level agreement, and Microsoft doesn't recommend it for production workloads. Certain features might not be supported or might have constrained capabilities. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).

## What is a conversation engine?

A conversation engine is the application component that decides how to respond to each user turn. It can call models, execute tools, manage conversation state, or apply deterministic business rules. It doesn't have to use a language model.

In this integration, the conversation engine runs as a separately deployed hosted agent. Voice Live converts caller speech to text and sends that text to the engine. The engine returns response text, which Voice Live converts to speech. Voice Live also manages turn-taking and interruption detection; the engine handles the corresponding control events.

The voice agent has `kind: voice`. Its `conversation_engine` configuration references a separately deployed hosted agent that implements the conversation engine. The value `conversation_engine.type: hosted_agent` selects the engine source; it doesn't change the voice agent's kind.

The conversation engine declares `voice_conversation_engine` version `1.0.0` and receives text and control events at `/voice_conversation_engine`. This endpoint reuses Voice Live Bridge Protocol 1.0; it doesn't introduce a new message format or carry caller audio.

The audio and text follow this flow:

```text
caller audio -> 
Voice Live speech recognition -> 
hosted conversation engine ->
Voice Live speech synthesis -> 
caller audio
```

## When to use a conversation engine

Use a hosted conversation engine when you want your own application code to handle the conversation, with Voice Live handling speech. Typical scenarios include:

- Reuse an existing text agent or orchestration framework behind a voice interface, after adapting it to the conversation engine protocol.
- Control model selection, routing, tool execution, and conversation state in your own runtime.
- Combine deterministic business rules or workflows with model-generated replies, instead of expressing all behavior through a voice model's instructions.

The engine must respond quickly enough for a live conversation and handle interruption, cancellation, and cleanup. You're responsible for deploying and operating its hosted runtime.

Choose a different approach if it better matches your scenario:

- If a model, instructions, and tools cover your conversation logic, start with a [model-backed voice agent](../agents/quickstarts/prompt-voice-agent).
- If the voice agent should keep control of the conversation and delegate only selected tasks, [use a subagent](../agents/how-to/use-subagent-voice-first-agent). A conversation engine handles the user turns instead of acting as a delegate for selected tasks.
- If you need to process raw audio or run your own speech recognition and synthesis inside the container, [build a custom audio pipeline](../agents/how-to/build-voice-agent). The conversation engine protocol in this article carries text and control events, not audio.

For the hosted conversation engine approach, choose a path based on whether the engine is already deployed:

| Starting point | Path |
| --- | --- |
| You need to deploy the voice agent and its hosted conversation engine. | Deploy the conversation engine with the Azure Developer CLI, then create the voice agent with the Python or .NET SDK. |
| You already have a compatible hosted conversation engine in a Foundry project. | Create the voice agent with the Python or .NET SDK. |

Both paths use the same SDK connection.

## Lower latency with a persistent WebSocket connection

A hosted conversation engine keeps a bidirectional WebSocket connection open with Voice Live across conversation turns. Compared with the previous HTTP Invocations integration, this approach reduces latency by about 150 ms on average.

## Prerequisites

- Access to voice agents and hosted agents in the selected Azure subscription and region, with the standalone `voice_conversation_engine` route enabled.
- For an interactive audio test, a microphone and speakers or a headset.
- For the CLI deployment path, Azure Developer CLI version 1.37.0 or later and the [Foundry extensions](../agents/how-to/install-cli-foundry-extensions). This walkthrough was validated with `azd` 1.37.2 and `azure.ai.agents` 1.0.0-beta.23. That extension requires the voice preview switch, including when initializing a template that declares a voice agent.
- For the CLI deployment path, an authenticated `azd` session. Run `azd auth login` before initialization.
- For local sample validation, Python 3.13 and [uv](https://github.com/astral-sh/uv).
- For the CLI deployment path, the [Azure permissions needed to provision Foundry resources](../agents/how-to/install-cli-foundry-extensions#azure-permissions). The basic CE sample doesn't require an LLM deployment or model quota.
- For the SDK creation path, an existing Foundry project and a deployed hosted conversation engine. The engine must declare `voice_conversation_engine` version `1.0.0` and implement Voice Live Bridge Protocol 1.0 at `/voice_conversation_engine`. Have its agent name and, optionally, the version to use.
- For the SDK creation path, the [Foundry User role](../concepts/rbac-foundry) on the project, or equivalent permissions to create and invoke agents.
- For the SDK examples, the Azure CLI, signed in with `az login`, and the language-specific dependencies below. The client can use Python or C# regardless of the hosted conversation engine's implementation language.

Important

The Foundry RBAC roles were recently renamed. **Foundry User**, **Foundry Owner**, **Foundry Account Owner**, and **Foundry Project Manager** were previously named Azure AI User, Azure AI Owner, Azure AI Account Owner, and Azure AI Project Manager. You might still see the previous names in some places while the rename rolls out. The role IDs and core permissions are unchanged by the rename.

# [Python](#tab/python)
Use Python 3.10 or later and version 2.7.0 or later of the Azure AI Projects client library. Install the `voice` extra and Azure Identity:

```console
python -m pip install "azure-ai-projects[voice]>=2.7.0" azure-identity
```

Reference: [Azure AI Projects client library for Python](/en-us/python/api/overview/azure/ai-projects-readme).

The `voice` extra installs the realtime transport dependencies, including `aiohttp` for asynchronous sessions. Your code uses the SDK instead of importing the transport libraries directly.

# [C#](#tab/csharp)
Use the [.NET 8 SDK or later](https://dotnet.microsoft.com/download). Create a console project and install the SDK packages:

```dotnetcli
dotnet new console --name HostedVoiceClient --framework net8.0
cd HostedVoiceClient
dotnet add package Azure.AI.Extensions.OpenAI --version 3.0.0-beta.6
dotnet add package Azure.AI.Projects.Agents --version 3.0.0-beta.6
dotnet add package Azure.AI.Projects --version 3.0.0-beta.6
dotnet add package Azure.Identity --version 1.21.0
```

Reference: [Azure AI Projects client library for .NET](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/ai/Azure.AI.Projects).

Keep the experimental warning suppressions at the top of the C# examples. The connection check doesn't require a local audio library.

---

The Python hosted conversation engine requires an AgentServer SDK with CE support. The CE sample pins `azure-ai-agentserver-invocations==1.3.0b1` and `azure-ai-agentserver-core==2.3.0b2` in its project and lock file. These dependencies run inside the hosted conversation engine, not in the voice client. Keep the sample's committed dependency versions. See the [AgentServer Voice sample](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/agentserver/azure-ai-agentserver-invocations/samples/basic_voice_agent#standalone-conversation-engine) for the runtime and registration requirements.

Confirm that the deployment region supports the dedicated route before deployment. An SDK upgrade alone doesn't enable the public endpoint. The Foundry routing layer and Voice Live must also support `voice_conversation_engine`.

## Deploy the conversation engine with the Azure Developer CLI

Use the [Voice Live conversation engine basic Python sample](https://github.com/microsoft-foundry/foundry-samples/tree/main/samples/python/hosted-agents/bring-your-own/conversation_engine/basic) to deploy the hosted conversation engine. Then create the voice agent with the SDK.

Its `azure.yaml` already declares `voice_conversation_engine:1.0.0` and both agents, with a Python 3.13 runtime for the hosted conversation engine. Each valid user message produces the same thirty-word story, streamed word by word. No LLM client, model deployment, or model-specific environment settings are needed.

Important

In `azure.ai.agents` 1.0.0-beta.23, the voice agent deployment validator still requires the legacy `invocations_ws:1.0.0` protocol and rejects this CE-only target. Don't run an unqualified `azd deploy` for this sample with that release. Deploy only the hosted conversation engine as described in Provision and deploy the conversation engine. Then create the voice agent with the SDK. Don't add legacy protocol declarations or Bridge metadata to bypass the validator.

This path creates a new Foundry project. To reuse an existing project, add `--project-id "<project-resource-id>"` to the initialization command and skip `azd provision`. Use the service-scoped deployment command in Provision and deploy the conversation engine. Reusing an existing agent name creates a new version of that agent; use a separate test project to avoid updating agents in a shared project.

### Initialize the sample

In PowerShell, enable the voice preview switch in the shell where you run `azd`, create an empty directory, and initialize from the public sample manifest:

```powershell
$env:AZD_ALPHA_ENABLE_AGENTS_VOICE = "true"

New-Item -ItemType Directory -Path hosted-voice-quickstart
Set-Location hosted-voice-quickstart

$sample = "https://github.com/microsoft-foundry/foundry-samples/" +
    "blob/main/" +
    "samples/python/hosted-agents/bring-your-own/" +
    "conversation_engine/basic/azure.yaml"
azd ai agent init -t $sample
```

Reference: [Initialize a hosted agent](../agents/how-to/deploy-hosted-agent).

The switch enables CLI functionality only. It doesn't grant service access or enable the regional CE route. Set it again if you open another shell before running `azd`.

When prompted, select your tenant and subscription and a region with CE support. Unless you supply an existing project resource ID, create a new Foundry project.

Change to the generated directory that contains `azure.yaml` by running `Set-Location voice-live-bridge-basic-python`.

### Review the conversation engine

The sample declares two `azure.ai.agent` services, but this walkthrough deploys only the hosted service:

| Service | Responsibility |
| --- | --- |
| `voice-live-bridge-basic-python` | The Python AgentServer runtime that implements the conversation engine. It receives text and control events through Voice Live Bridge Protocol 1.0 over `voice_conversation_engine`, then streams the fixed story as text. |
| `voice-live-bridge-basic-python-voice` | A declarative voice agent (`kind: voice`). Leave this service undeployed with extension 1.0.0-beta.23; the SDK example creates a voice agent named `hosted-conversation-voice-agent` instead. |

The hosted conversation engine already includes this declaration in `azure.yaml`:

```yaml
protocols:
  - protocol: voice_conversation_engine
    version: "1.0.0"
```

Reference: [Hosted service protocols](../agents/concepts/azure-yaml-reference#protocols) | [AgentServer Voice sample](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/agentserver/azure-ai-agentserver-invocations/samples/basic_voice_agent#standalone-conversation-engine).

The sample omits `metadata.voiceLiveCompatible` and `metadata.bridgeProtocolVersion`. The hosted conversation engine doesn't require either flag or an `invocations_ws` declaration.

The voice agent and the hosted agent that implements the conversation engine must have different Foundry agent names. Configure the voice agent's audio and greeting in the following SDK example. The undeployed YAML voice agent's settings don't configure the SDK-created voice agent.

Keep model calls, instructions, and tools in the conversation engine. Configure audio, voice output, and the greeting on the voice agent. Don't use the older `modelType: hosted_agent` or `targetAgent` settings.

The hosted protocol version `1.0.0` is distinct from the Bridge message handshake, which still uses `protocol_version="1.0"`. Voice Live connects through the conversation engine's `/endpoint/protocols/voice_conversation_engine` endpoint, which Foundry forwards to the container's `/voice_conversation_engine` route. There's no fallback to `/invocations_ws` for a conversation engine that declares CE.

Existing legacy Bridge agents can continue using their `invocations_ws` declaration and Bridge metadata. You don't need to migrate those agents. If the same conversation engine must also serve legacy calls, retain that declaration and metadata alongside CE.

This workflow doesn't replace [custom audio pipelines hosted through `invocations_ws`](../agents/how-to/build-voice-agent). The conversation engine exchanges text and control events with Voice Live rather than processing caller audio itself.

### Review the conversation engine runtime

The sample already uses `VoiceAgentServerHost()` with a CE-capable SDK and the typed `UserBargeIn` event through `@app.on_user_barge_in`. It includes handling for interruption, cancellation, timeout, response correlation, `heard_text`, and cleanup. You don't need to migrate the SDK or rename callbacks.

Keep the sample's committed `pyproject.toml` and `uv.lock`. For local execution, use its frozen uv setup rather than upgrading dependencies:

```powershell
Set-Location src/voice-live-bridge-basic-python
uv sync --frozen --python 3.13
uv run --frozen python main.py
```

Reference: [Run the CE sample locally](https://github.com/microsoft-foundry/foundry-samples/tree/main/samples/python/hosted-agents/bring-your-own/conversation_engine/basic#option-2-run-locally).

This optional local server doesn't require Azure credentials or model settings. Stop it and return to the generated directory containing `azure.yaml` before provisioning or deployment.

To integrate your own streaming logic, replace the sample's `stream_story` asynchronous generator in `on_user_message`. Keep response scheduling asynchronous so control events can interrupt an active response.

### Provision and deploy the conversation engine

From the generated project directory, provision the new Foundry project declared in `azure.yaml`. Skip this command if you initialized against an existing project:

```powershell
azd provision
```

Reference: [azd provision](/en-us/azure/developer/azure-developer-cli/reference#azd-provision).

Deploy only the hosted conversation engine, not the voice agent service:

```powershell
azd deploy voice-live-bridge-basic-python
```

Reference: [azd deploy](/en-us/azure/developer/azure-developer-cli/reference#azd-deploy).

Read the project endpoint and inspect the conversation engine. Wait for its version to become active before creating the voice agent or starting a voice session:

```powershell
azd env get-value FOUNDRY_PROJECT_ENDPOINT
azd ai agent show voice-live-bridge-basic-python --output json
```

Reference: [Deploy a hosted agent](../agents/how-to/deploy-hosted-agent) | [Manage hosted agents](../agents/how-to/manage-hosted-agent).

Continue to Create the voice agent. In your chosen language's example, use the endpoint printed earlier, `voice-live-bridge-basic-python` as the hosted conversation engine's name, and the actual version returned by `show`. No voice agent is deployed yet.

## Create the voice agent

Create the voice agent after deploying the conversation engine with the CLI, or start here if you already have a compatible hosted conversation engine in your project.

Set the voice agent's conversation engine to a `VoiceHostedAgentConversationEngine` that references the hosted conversation engine in your project. Both SDKs serialize its `type` as `hosted_agent`. Don't use `voice_conversation_engine` as the engine's `type`; that name identifies the hosted protocol.

Both examples use the same audio configuration and hosted conversation engine. Choose the SDK language in the following sections.

Replace the project endpoint and the hosted conversation engine's agent name and optional version with your project values. Keep the voice agent's name different from the hosted conversation engine's name. Both examples enable conversation storage, which persists transcripts and audio. Set `store=False` in Python or `Store=false` in C# if you don't need persistence.

# [Python](#tab/python)
Set `allow_preview=True` on `AIProjectClient`. The SDK adds the required `Foundry-Features: VoiceAgents=V1Preview` header. Save this example as `create_voice_agent.py` and run it with `python create_voice_agent.py`:

```python
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import (RealtimeAudioFormatsAudioPcm,VoiceAgentAudioConfig,VoiceAgentAudioInputConfig,VoiceAgentAudioOutputConfig,VoiceAgentDefinition,VoiceAgentInputTranscription,VoiceAgentServerVadTurnDetection,VoiceAgentTemplateGreetingConfig,VoiceHostedAgentConversationEngine,VoiceOutputModality,VoiceType,
)
from azure.identity import DefaultAzureCredential

PROJECT_ENDPOINT = ("https://<resource>.services.ai.azure.com/api/projects/<project>"
)
HOSTED_AGENT_NAME = "<hosted-agent-name>"
HOSTED_AGENT_VERSION = "<hosted-agent-version>"
VOICE_AGENT_NAME = "hosted-conversation-voice-agent"

conversation_engine = VoiceHostedAgentConversationEngine(name=HOSTED_AGENT_NAME,
)

if HOSTED_AGENT_VERSION:conversation_engine.version = HOSTED_AGENT_VERSION

voice_definition = VoiceAgentDefinition(conversation_engine=conversation_engine,greeting=VoiceAgentTemplateGreetingConfig(	text="Hello! How can I help you today?",),store=True,output_modalities=[VoiceOutputModality.AUDIO],audio=VoiceAgentAudioConfig(	input=VoiceAgentAudioInputConfig(		format=RealtimeAudioFormatsAudioPcm(rate=24000),		turn_detection=VoiceAgentServerVadTurnDetection(			threshold=0.5,			prefix_padding_ms=300,			silence_duration_ms=1000,		),		transcription=VoiceAgentInputTranscription(			model="azure-speech",		),	),	output=VoiceAgentAudioOutputConfig(		format=RealtimeAudioFormatsAudioPcm(rate=24000),		voice="en-US-JennyNeural",		voice_type=VoiceType.AZURE_STANDARD,	),),
)

with (DefaultAzureCredential() as credential,AIProjectClient(	endpoint=PROJECT_ENDPOINT,	credential=credential,	allow_preview=True,) as project_client,
):voice_agent = project_client.agents.create_version(	agent_name=VOICE_AGENT_NAME,	description=(		"Voice agent that uses a hosted agent as its conversation engine"	),	definition=voice_definition,)print(	f"Voice agent created: {voice_agent.name}, "	f"version {voice_agent.version}")
```

Reference: [AgentsOperations.create_version](/en-us/python/api/azure-ai-projects/azure.ai.projects.operations.agentsoperations#azure-ai-projects-operations-agentsoperations-create-version) | [VoiceAgentDefinition](/en-us/python/api/azure-ai-projects/azure.ai.projects.models.voiceagentdefinition) | [VoiceHostedAgentConversationEngine](/en-us/python/api/azure-ai-projects/azure.ai.projects.models.voicehostedagentconversationengine).

# [C#](#tab/csharp)
Replace `Program.cs` in `HostedVoiceClient` with the following code and run `dotnet run`. Pass `foundryFeatures: "VoiceAgents=V1Preview"` when creating the version:

```csharp
#pragma warning disable AAIP001, OPENAI002

using System;
using Azure.AI.Projects.Agents;
using Azure.Identity;
using OpenAI.Realtime;

string projectEndpoint =
    "https://<resource>.services.ai.azure.com/api/projects/<project>";
string hostedAgentName = "<hosted-agent-name>";
string hostedAgentVersion = "<hosted-agent-version>";
string voiceAgentName = "hosted-conversation-voice-agent";

VoiceHostedAgentConversationEngine conversationEngine = new(hostedAgentName);
if (!string.IsNullOrEmpty(hostedAgentVersion))
{
    conversationEngine.Version = hostedAgentVersion;
}

VoiceAgentDefinition definition = new()
{
    ConversationEngine = conversationEngine,
    Greeting = new VoiceAgentTemplateGreetingConfig(
        "Hello! How can I help you today?"),
    Store = true,
    Audio = new VoiceAgentAudioConfig
    {
        Input = new VoiceAgentAudioInputConfig
        {
            Format = new RealtimePcmAudioFormat { Rate = 24000 },
            TurnDetection = new VoiceAgentServerVadTurnDetection
            {
                Threshold = 0.5,
                PrefixPaddingMs = 300,
                SilenceDurationMs = 1000,
            },
            Transcription = new VoiceAgentInputTranscription(
                VoiceAgentInputTranscriptionModel.AzureSpeech),
        },
        Output = new VoiceAgentAudioOutputConfig
        {
            Format = new RealtimePcmAudioFormat { Rate = 24000 },
            Voice = "en-US-JennyNeural",
            VoiceType = VoiceType.AzureStandard,
        },
    },
};
definition.OutputModalities.Add(VoiceOutputModality.Audio);

AgentAdministrationClient agentsClient = new(
    new Uri(projectEndpoint), new DefaultAzureCredential());
var result = await agentsClient.CreateAgentVersionAsync(
    voiceAgentName,
    new ProjectsAgentVersionCreationOptions(definition)
    {
        Description =
            "Voice agent that uses a hosted agent as its conversation engine",
    },
    foundryFeatures: "VoiceAgents=V1Preview");
Console.WriteLine(
    $"Voice agent created: {result.Value.Name}, " +
    $"version {result.Value.Version}");
```

Reference: [AgentAdministrationClient](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/ai/Azure.AI.Projects.Agents/src/Generated/AgentAdministrationClient.cs) | [VoiceHostedAgentConversationEngine](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/ai/Azure.AI.Projects.Agents/src/Generated/Models/VoiceHostedAgentConversationEngine.cs).

---

Each script prints the voice agent's name and new immutable version. Keep the endpoint and voice agent name for the connection example.

To use the hosted conversation engine's latest version instead of pinning a version, set `HOSTED_AGENT_VERSION` in Python or `hostedAgentVersion` in C# to an empty string. The example then omits `version` from the conversation engine. When pinning a version, use an actual agent version, not the literal value `deployed` from the CLI configuration.

The following table uses wire-format property names. Python uses `conversation_engine`, `name`, and `version`; C# uses `ConversationEngine`, `Name`, and `Version`:

| Property | Required | Description |
| --- | --- | --- |
| `type` | Yes | Selects the conversation engine. `VoiceHostedAgentConversationEngine` sets this property to `hosted_agent` automatically. |
| `name` | Yes | Specifies the agent name of a hosted conversation engine in the same Foundry project. |
| `version` | No | Pins a hosted conversation engine's agent version. If you omit this property, the service selects the latest version when the conversation engine connection is established. |

For this type of voice agent, don't specify `model_type` or `model`. Exactly one conversation selection form is allowed: a model-backed definition or an engine-backed definition. The presence of `conversation_engine` selects the engine-backed form.

The conversation engine owns the conversation logic. Therefore, don't configure `instructions`, `reasoning_effort`, `tools`, `tool_choice`, `subagent_config`, or `handoff` on the voice agent. You can configure voice-surface properties, including `audio`, `avatar`, `output_modalities`, `greeting`, `structured_inputs`, `store`, and `rai_config`.

The `create_version` operation validates the conversation engine configuration but doesn't verify the referenced hosted conversation engine. When a voice session starts, the service resolves the conversation engine version and checks its `voice_conversation_engine` declaration and supported version. The engine must also accept the Bridge Protocol 1.0 handshake. Creating a voice agent doesn't add a protocol declaration or handler to the conversation engine.

## Use the voice agent

Connect to the SDK-created voice agent, not directly to the hosted conversation engine. Use the same project endpoint and voice agent name as in the creation step.

The following examples wait up to ten seconds for a session readiness event, print a confirmation, and close the connection. They check SDK connectivity only; they don't capture microphone input, play audio, or verify the conversation engine's response.

The voice agent owns audio configuration and turn detection, so the client doesn't send a `session.update` event. A persisted conversation ID isn't required, including when conversation storage is disabled.

# [Python](#tab/python)
Save this example as `check_voice_connection.py` and run `python check_voice_connection.py`:

```python
import asyncio
import uuid

from azure.ai.projects.aio import AIProjectClient
from azure.ai.projects.models import (
    RealtimeServerEventError,
    RealtimeServerEventSessionCreated,
    RealtimeServerEventSessionUpdated,
)
from azure.identity.aio import DefaultAzureCredential

PROJECT_ENDPOINT = "https://<resource>.services.ai.azure.com/api/projects/<project>"
VOICE_AGENT_NAME = "hosted-conversation-voice-agent"

async def check_connection():
    async with (
        DefaultAzureCredential() as credential,
        AIProjectClient(
            endpoint=PROJECT_ENDPOINT, credential=credential, allow_preview=True
        ) as client,
        client.beta.voice_agents.realtime.connect(
            agent_name=VOICE_AGENT_NAME, agent_session_id=uuid.uuid4().hex
        ) as connection,
    ):
        async for event in connection:
            if isinstance(
                event,
                (
                    RealtimeServerEventSessionCreated,
                    RealtimeServerEventSessionUpdated,
                ),
            ):
                print("Voice session connected.")
                return
            if isinstance(event, RealtimeServerEventError):
                raise RuntimeError(event.error.message)
        raise ConnectionError("Connection closed before the session was ready.")

asyncio.run(asyncio.wait_for(check_connection(), timeout=10))
```

Reference: [AsyncBetaRealtime.connect](/en-us/python/api/azure-ai-projects/azure.ai.projects.aio.operations.asyncbetarealtime#azure-ai-projects-aio-operations-asyncbetarealtime-connect).

For microphone capture, playback, and interruption handling, reuse the audio-processing code in the [Python live-audio conversation sample](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/ai/azure-ai-projects/samples/agents/voice/sample_voice_agent_realtime_audio_conversation_async.py). Install that sample's audio dependencies, including PyAudio and PortAudio. Its standalone entry point creates a model-backed agent; adapt its audio loop to connect to the voice agent created in this article instead of running its agent creation and cleanup steps.

# [C#](#tab/csharp)
Replace `Program.cs` in `HostedVoiceClient` with this code and run `dotnet run`:

```csharp
#pragma warning disable AAIP001, AAIP002, OPENAI002

using System;
using System.Threading;
using Azure.AI.Projects;
using Azure.AI.Projects.Agents;
using Azure.Identity;
using OpenAI.Realtime;

string projectEndpoint =
    "https://<resource>.services.ai.azure.com/api/projects/<project>";
string voiceAgentName = "hosted-conversation-voice-agent";

using CancellationTokenSource timeout = new(TimeSpan.FromSeconds(10));
AIProjectClient client = new(
    new Uri(projectEndpoint), new DefaultAzureCredential());
using RealtimeSessionClient session =
    await client.ProjectsRealtimeClient.StartSessionAsync(
        voiceAgentName, intent: null,
        options: new ProjectsRealtimeSessionClientOptions
        {
            Transport = VoiceAgentTransport.Websocket,
            QueryString = $"agent_session_id={Guid.NewGuid():N}",
        },
        cancellationToken: timeout.Token);

await foreach (RealtimeServerUpdate update in
    session.ReceiveUpdatesAsync(timeout.Token))
{
    if (update is RealtimeServerUpdateSessionCreated
        or RealtimeServerUpdateSessionUpdated)
    {
        Console.WriteLine("Voice session connected.");
        return;
    }
    if (update is RealtimeServerUpdateError error)
    {
        throw new InvalidOperationException(error.Error.Message);
    }
}
throw new InvalidOperationException(
    "Connection closed before the session was ready.");
```

Reference: [ProjectsRealtimeClient](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/ai/Azure.AI.Projects/src/Custom/VoiceAgent/ProjectsRealtimeClient.cs).

The [.NET WebSocket audio operations sample](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/ai/Azure.AI.Projects/samples/Sample_VoiceAgent_WebSocketAudio.md) demonstrates sending PCM chunks and receiving audio events. It uses a generated tone, not microphone capture or speaker playback. Reuse its audio operations with the existing voice agent; don't run its model-backed agent creation or cleanup steps against this agent.

---

For a full audio client, stream mono 24-kHz PCM16 input while receiving server events asynchronously. Clear queued playback when the server detects user speech, resume playback for the next response, and close audio devices and background tasks when the session ends.

### Test the voice agent

Use an audio client configured for the existing voice agent, or the Foundry voice playground where available. The connection checks don't perform this audio test:

1. Say a short sentence to trigger the conversation engine. For the basic CE sample, expect the fixed thirty-word story rather than a model-generated answer.
2. Confirm that the client prints your input transcription and the agent's response text, and that you hear the response.
3. Speak while the agent responds, and check that playback stops and the agent handles your new turn.

An active agent or a successful text response alone doesn't establish that the audio path works.

For a model-independent check of the sample's hosted conversation engine, use its [local protocol smoke client](https://github.com/microsoft-foundry/foundry-samples/tree/main/samples/python/hosted-agents/bring-your-own/conversation_engine/basic#local-protocol-smoke-test). It defaults to `/voice_conversation_engine`, sends `Hello, Voice Live!`, and verifies the story and all thirty text deltas. This check verifies the conversation engine's protocol handling, not the public Foundry route or managed voice audio path. A successful check against `/invocations_ws` doesn't verify CE routing.

`azd ai agent invoke` doesn't generate Voice Live conversations. Selecting the voice agent returns [portal guidance](../agents/how-to/invoke-hosted-agent#voice-agent-limitations), not a voice session.

## Troubleshoot

| Symptom | Action |
| --- | --- |
| Initialization reports `not logged in`. | Sign in with `azd auth login`, and run initialization again. |
| Initialization reports `preview feature "agents.voice" is disabled`, or voice options are missing from help. | For extension 1.0.0-beta.23, set `AZD_ALPHA_ENABLE_AGENTS_VOICE=true` in the current shell before running `azd`. Check the voice preview setup and tool versions. |
| Voice agent deployment reports that the target doesn't declare `invocations_ws/1.0.0`. | This condition indicates the CE-only target validation limitation in extension 1.0.0-beta.23. Deploy only `voice-live-bridge-basic-python` and create the voice agent with the SDK. Don't add legacy declarations or metadata to bypass it. |
| The voice session can't resolve its conversation engine. | Check that the SDK definition's `conversation_engine.name` and optional `version` identify an active hosted conversation engine in the same project. |
| Every input produces the same story. | This condition indicates the basic CE sample's expected behavior. Replace `stream_story` with your own asynchronous streaming logic to customize the reply. |
| The conversation engine reports `protocol_mismatch`. | Check that the Bridge handshake uses `protocol_version="1.0"`. The Hosted protocol declaration separately uses `voice_conversation_engine` version `1.0.0`. |
| The CE connection fails after the voice agent is created. | Verify that the selected conversation engine version declares `voice_conversation_engine:1.0.0`, its deployed runtime serves `/voice_conversation_engine`, and the deployment region supports the public route. Adding Bridge metadata isn't a substitute. |
| The SDK can't find the voice agent. | Complete the SDK creation step and connect to `hosted-conversation-voice-agent` (or your chosen name), not the undeployed YAML voice agent. Use the endpoint of the project that contains both agents. |

## Clean up resources

If you created a new project for this walkthrough, run the following command from the generated project directory to remove the project and both agents, including the SDK-created voice agent:

Warning

`azd down` deletes the resource group and all resources created for this environment. Don't use it to clean up individual agents in a shared project.

```powershell
azd down
```

Reference: [azd down](/en-us/azure/developer/azure-developer-cli/reference#azd-down).

If you reused an existing project, don't run `azd down`. Delete only the voice agent you created, using the endpoint and agent name from the creation step:

# [Python](#tab/python)
```python
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

PROJECT_ENDPOINT = "https://<resource>.services.ai.azure.com/api/projects/<project>"
VOICE_AGENT_NAME = "hosted-conversation-voice-agent"

with (
    DefaultAzureCredential() as credential,
    AIProjectClient(
        endpoint=PROJECT_ENDPOINT,
        credential=credential,
        allow_preview=True,
    ) as project_client,
):
    project_client.agents.delete(agent_name=VOICE_AGENT_NAME)
```

Reference: [AgentsOperations.delete](/en-us/python/api/azure-ai-projects/azure.ai.projects.operations.agentsoperations#azure-ai-projects-operations-agentsoperations-delete).

# [C#](#tab/csharp)
Replace `Program.cs` with this cleanup code and run `dotnet run`:

```csharp
using System;
using Azure.AI.Projects.Agents;
using Azure.Identity;

string projectEndpoint =
    "https://<resource>.services.ai.azure.com/api/projects/<project>";
string voiceAgentName = "hosted-conversation-voice-agent";

AgentAdministrationClient agentsClient = new(
    new Uri(projectEndpoint), new DefaultAzureCredential());
await agentsClient.DeleteAgentAsync(voiceAgentName);
```

Reference: [AgentAdministrationClient.DeleteAgentAsync](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/ai/Azure.AI.Projects.Agents/src/Custom/AgentAdministrationClient.cs).

---

If you also created a new, dedicated hosted conversation engine, delete it separately only after confirming that no other voice agent uses it. Keep any pre-existing hosted conversation engine, model deployment, and shared project.
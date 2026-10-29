---
layout: Conceptual
title: Migrate from Voice Live with Foundry Agent Service to Microsoft Foundry voice agents - Microsoft Foundry | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/migrate-from-voice-live
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
author: yulin-li
learn_banner_products:
- azure
manager: mcleans
ms.author: yulili
ms.collection: ce-skilling-ai-copilot
ms.update-cycle: 90-days
ms.service: microsoft-foundry
description: Migrate from Voice Live with Foundry Agent Service to Microsoft Foundry voice agents. Compare architectures, preserve tools, and update WebSocket messages.
ms.date: 2026-10-25T00:00:00.0000000Z
ms.topic: how-to
ms.subservice: foundry-agent-service
ms.custom: preview, doc-kit-assisted
ai-usage: ai-assisted
locale: en-us
document_id: 51bf6fe7-aafa-e4a6-b120-195512ff1367
document_version_independent_id: c2125c00-da15-ce7b-3dea-beec485e9286
original_content_git_url: https://github.com/MicrosoftDocs/azure-ai-docs-pr/blob/live/articles/foundry/agents/how-to/migrate-from-voice-live.md
site_name: Docs
depot_name: Learn.azure-ai
page_type: conceptual
toc_rel: ../../toc.json
asset_id: foundry/agents/how-to/migrate-from-voice-live
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/foundry/agents/how-to/migrate-from-voice-live.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/64b65f6c-101f-411a-9b83-9f577fab52d0
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1a667fd1-8145-4b11-af0f-9f5de205a6e5
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: 209ad685-00a2-7fee-a9b9-c1802a952e7f
---

# Migrate from Voice Live with Foundry Agent Service to Microsoft Foundry voice agents - Microsoft Foundry | Microsoft Learn

Migrate an existing [Voice Live with Foundry Agent Service](../../../ai-services/speech-service/voice-live-agents-quickstart) integration to a voice-based prompt agent in Microsoft Foundry. First, compare the architectures and choose how to preserve your tools and business logic. Then move the configuration, update the WebSocket client, and test responsiveness before switching traffic.

In this article, *Voice Live integration* means Voice Live connected to an existing Foundry text agent. A *Foundry voice agent* is a separate agent with `kind: voice` that still uses Voice Live for the voice runtime. You manage its model, instructions, audio, and tools together in an agent definition.

You can't change an existing text agent's interaction mode to voice, so migration creates a new agent rather than modifying the original. This process is separate from [migrating Agent Service (classic) to the new Agent Service](migrate).

Important

Items marked preview in this article are currently in preview. This preview is provided without a service-level agreement, and Microsoft doesn't recommend it for production workloads. Certain features might not be supported or might have constrained capabilities. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).

## Prerequisites

- Access to a working Voice Live integration with a Foundry text agent, including its configuration and client code.
- A [Foundry project](../../how-to/create-projects) with access to the voice-agent preview and a supported model in the project's region.
- [Foundry User role](../../concepts/rbac-foundry) on the target project, with permission to create and invoke agents.

    Important

    The Foundry RBAC roles were recently renamed. **Foundry User**, **Foundry Owner**, **Foundry Account Owner**, and **Foundry Project Manager** were previously named Azure AI User, Azure AI Owner, Azure AI Account Owner, and Azure AI Project Manager. You might still see the previous names in some places while the rename rolls out. The role IDs and core permissions are unchanged by the rename.
- Access to the tool connections and data resources that the new voice agent needs. Have a resource owner grant any required permissions.
- A microphone and speakers or a headset for testing spoken conversations.
- To run the Python connection example: Python 3.10 or later and the Azure CLI, signed in with `az login`.

## Compare the two approaches

Start with the architecture, not the endpoint URL. Both approaches use Voice Live for real-time audio, configurable voices, turn detection, and interruption handling. What changes is which agent owns the conversation and where you configure it.

### Compare the conversation architecture

In the existing integration, Voice Live provides the speech layer around a separate Foundry text agent. The text agent handles the transcribed request, calls its tools, and returns text for Voice Live to speak.

```text
Caller audio
  -> Voice Live: speech recognition and turn detection
  -> Foundry text agent: text model, instructions, tools, and knowledge
  -> Voice Live: speech synthesis
  -> Spoken response
```

With a Foundry voice agent, one versioned definition owns the conversation, including the model, instructions, audio, greeting, and tools. Voice Live runs that definition without requiring a separate text agent to handle every turn. The agent calls tools through client functions, Model Context Protocol (MCP), or Foundry toolboxes.

```text
Foundry voice agent
  Voice Live runtime, with one of two model paths:
    Speech-to-speech: audio -> realtime model -> audio
    Cascaded: audio -> speech recognition -> text model -> synthesis -> audio
  Tools and knowledge: client functions, MCP servers, Foundry toolboxes
  Optional specialist: an existing prompt or hosted subagent
```

Choose speech-to-speech for a native real-time conversation, or a cascaded text model to retain the model and speech controls your application needs. Tool and knowledge access is available with either architecture, subject to model and tool compatibility. See [How voice-based agents work](../overview#how-voice-based-agents-work).

This comparison covers Voice Live connected to a text agent, not all Voice Live capabilities. [Voice Live used directly](../../../ai-services/speech-service/voice-live) also supports speech-to-speech models.

### Compare capabilities and operations

Use this table to identify which parts of your application change and which capabilities to test.

| Consideration | Voice Live with Foundry Agent Service | Foundry voice agent |
| --- | --- | --- |
| Supported models | Text models supported by the connected Foundry agent. | Both speech-to-speech models, such as `gpt-realtime`, and supported text models. |
| Model hosting and capacity | Uses the model deployment selected for your Foundry text agent. | For either model family, choose a self-deployed or service-managed model. With a service-managed model, you don't maintain a model deployment. |
| Conversational experience | Every spoken turn passes through speech recognition, the text agent, and speech synthesis. | Choose native speech-to-speech interaction or a cascaded text-model pipeline with speech recognition and synthesis. |
| Response latency | Includes speech recognition, processing by the separate text agent, and speech synthesis. | Generally lower end-to-end response latency than Voice Live connected to a Foundry text agent, with a runtime optimized for voice interactions. |
| Existing tools and knowledge | Keep the business logic, tools, and knowledge configured on your text agent. | Supports the same tools and knowledge as Foundry text agents, including Foundry IQ in Foundry Tools, MCP, and tools exposed through a toolbox. Reconnect them, or retain the text agent as a specialist subagent. |
| Configure voice behavior | Tune speech through Voice Live and manage the text agent's instructions and tools separately. | Manage the model, instructions, voice, greeting, and turn-taking together in Foundry. Save and test changes as agent versions. |
| Connect phone callers | Integrate your application with a telephony provider, using provider APIs or a [solution accelerator](../../../ai-services/speech-service/voice-live-telephony). You manage the integration. | Built-in [telephony integration](voice-agent-telephony-channels) supports inbound and outbound calls through Teams Phone extensibility and Twilio. Configure the provider connection and, for inbound calls, bind a phone number in Foundry. |
| Review customer conversations | Review text-agent conversation history and the logs your application captures. Text history might differ from what a caller heard before an interruption. | Opt in to persisted transcripts, conversation events, and audio for review. Recording is off by default. |
| Diagnose delays and failures | View traces of the text-model interaction. Turn detection, audio input, and audio output aren't included in the agent trace. | Trace the voice pipeline, including turn detection, audio input, model and tool calls, and audio output. |
| Plan costs | Account for your Voice Live usage, the text agent's model deployment, and dependent tools and services. | Model hosting, audio usage, tools, and optional recordings or avatars affect cost. Compare service-managed model usage with the cost of your own supported deployment. |

Choose a Foundry voice agent if you need speech-to-speech models, service-managed model hosting, built-in telephony, or integrated voice configuration and call review. You can keep using a supported text model; migration doesn't require switching to `gpt-realtime`.

Model, region, network, and transport restrictions still apply. Actual latency depends on the model, deployment, prompts, tools, and channel. Measure conversation quality, latency, and cost with your workload before switching.

## Choose how to reuse your existing agent

Decide which agent handles the conversation before you move configuration. Reusing a text agent for specialist tasks is different from forwarding every spoken turn to it.

| Migration approach | Use it when | What to change |
| --- | --- | --- |
| Create a model-backed voice agent | You want the voice agent to handle the conversation and call tools directly. | Adapt the instructions, select a supported model, and reconfigure tools for the voice agent. |
| Keep the text agent as a subagent | You want to retain specialist reasoning, retrieval, or business logic in an existing prompt or hosted agent. | Configure `subagent_config` and specify when to delegate. The voice agent handles the conversation and consults the specialist as needed. |
| Use a hosted conversation engine | Your hosted code must own the conversation logic for every turn. | Follow the separate [hosted conversation engine guide](../../how-to/voice-first-with-hosted-agent). The target needs the required `invocations_ws` Bridge Protocol implementation; a text endpoint alone isn't sufficient. |

For the subagent approach, the subagent must be in the same project as the voice agent. Subagents aren't supported in VNet-isolated projects. Follow [Use a subagent in a voice-based agent](use-subagent-voice-first-agent) and test delegation, follow-up questions, and failure behavior.

The rest of this article covers migration to a model-backed voice agent, with optional subagents. For a custom hosted voice application that exposes `invocations_ws`, see [Build a voice agent with hosted agents](build-voice-agent).

## Inventory the source and create a new agent

First, capture the configuration your application actually uses, including client-side overrides. Then create a separate voice agent so that you can test without changing the existing integration.

### Inventory the existing integration

Record these settings before you create the voice agent:

1. Record the source agent name and version, model deployment, instructions, tools, and project connections.
2. Export the Voice Live settings. If you used the integration sample, reassemble `microsoft.voice-live.configuration` and its numbered metadata entries, such as `.1` and `.2`, in order.
3. Record any client-side `session.update` overrides, proactive greeting code, audio formats, interruption handling, and channel configuration.
4. Record authentication and cross-resource dependencies, including any `foundry_resource_override` and managed identity settings. Don't copy credentials into the new agent definition.

### Create the voice agent

Use the inventory to configure a new agent:

1. Follow [Create a voice-based prompt agent](../quickstarts/prompt-voice-agent) to create an agent with a **new name**. In the portal, select **Voice** as the interaction mode. In code, use `VoiceAgentDefinition` instead of `PromptAgentDefinition`.
2. Choose a supported speech-to-speech model, such as `gpt-realtime`, or a supported text model. Both model families support service-managed and self-deployed options.
3. Set `model_type` to `managed` for a service-managed model, or `self_deployed` for your own supported deployment. Use the corresponding model or deployment name.
4. Adapt the instructions for spoken interaction: short answers, one question at a time, and explicit confirmation before consequential actions. Preserve the source agent's business rules and escalation requirements.
5. Save the new agent version and record its name and version for testing. Keep the original text agent and client configuration unchanged until the new path is ready.

Creating a voice agent version doesn't copy the source agent's tools, connections, or conversation history. For an SDK creation example, see [Create from an explicit definition](../quickstarts/prompt-voice-agent?pivots=python#create-from-an-explicit-definition).

## Move voice settings into the definition

Map the existing voice settings to the new definition instead of copying the old session object into metadata. The following table uses JSON field names from the Voice Live integration samples and the voice-agent definition.

| Existing setting | Voice-agent definition field | Migration action |
| --- | --- | --- |
| Text-agent instructions | `instructions` | Adapt the instructions for speech, or keep specialist instructions on the subagent. |
| `session.voice.name` | `audio.output.voice` | Set the voice name as a string, not a nested voice object. |
| `session.voice.type` | `audio.output.voice_type` | Set the provider type, such as `azure-standard`. |
| `session.voice.temperature` | `audio.output.voice_temperature` | Preserve the setting only for a voice type that supports it. |
| `session.input_audio_transcription` | `audio.input.transcription` | Set the transcription model explicitly and carry over supported language and vocabulary settings. |
| `session.turn_detection` | `audio.input.turn_detection` | Review pause detection, automatic response creation, interruption, and truncation settings. |
| `session.input_audio_noise_reduction` | `audio.input.noise_reduction` | Preserve the supported noise-reduction configuration. |
| `session.input_audio_echo_cancellation` | `audio.input.echo_cancellation` | Match the reference source and channel layout to your client. |
| `session.input_audio_format` and `session.output_audio_format` | `audio.input.format` and `audio.output.format` | Use format objects, such as `{"type":"audio/pcm","rate":24000}`, instead of the legacy `pcm16` string. |
| `session.modalities` | `output_modalities` | Select the supported output modalities. Audio output defaults to `["audio"]`; don't copy the old array without reviewing it. |
| `session.interim_response` | `interim_response` | Reconfigure latency or tool-wait responses on the definition. |
| Client-generated opening message | `greeting` | Choose a fixed template or an LLM-generated greeting. Remove the old startup trigger if the new greeting replaces it. |

For configuration details and SDK examples, see [Configure a voice agent](configure-voice-agent). SDK and `azure.yaml` property names can differ from the JSON names in this table.

The service applies the definition when a session starts. Remove client startup code that resends the full legacy session configuration. Keep only supported per-session overrides, such as audio or avatar settings, and verify the effective configuration returned by the service.

## Reconnect tools and knowledge

Voice agents support the same tools and knowledge as Foundry text agents, including Foundry IQ and MCP servers. You don't need to replace your knowledge sources or business APIs merely to add voice. The integration route changes: use a native voice-agent tool, a Foundry toolbox, or a retained specialist subagent.

| Existing capability | Supported voice-agent integration | What to preserve or reconfigure |
| --- | --- | --- |
| Foundry IQ knowledge bases | An `mcp` tool that connects to the knowledge base's MCP endpoint, directly or through a toolbox. | Reuse the knowledge base and configure its project connection. Preserve source permissions and retrieval instructions. See [Connect a Foundry IQ knowledge base](foundry-iq-connect). |
| Remote or custom MCP servers | A native `mcp` tool or MCP tools in a toolbox. | Reconfigure the server, allowed tools, authentication, and any required approvals. |
| Azure AI Search and file search | A `toolbox` reference containing the search tools. | Retain the search index or vector store configuration and the identity that can read it. |
| Web search and code interpreter | A `toolbox` reference containing the corresponding tools. | Reconfigure tool settings, dependent resources, and any required files. |
| OpenAPI business APIs | A `toolbox` reference containing the OpenAPI tool. | Preserve the API schema, connection, permissions, and confirmation requirements for actions. |
| Agent-to-agent (A2A), browser automation, Fabric IQ, and Work IQ | A `toolbox` reference containing the required tool types. | Check each tool's setup, authentication, and region and model requirements. |
| Custom function calling | A native `function` tool executed by your live client. | Register the schema and implement the WebSocket function-call loop. A schema alone doesn't execute the function. |
| Reusable skills | A toolbox containing the skills. | Reference skills in the same project and select the toolbox version that includes them. |
| Existing prompt or hosted agent logic | A specialist configured through `subagent_config`. | Preserve the specialist's tools and instructions, and define when the voice agent delegates to it. |

The toolbox's [feature support](tools/toolbox#feature-support) lists the available tool types. Voice agents reference the toolbox rather than accepting every text-agent tool type directly in their `tools` array. Model, region, network, and individual tool restrictions still apply.

Reconnect and test each dependency:

1. Create or reuse the project connections and toolbox versions required by the new voice agent. Don't copy the text agent's `tools` array unchanged.
2. Confirm which identity accesses each dependency. For permission-aware retrieval, verify that a caller can't retrieve content they're not authorized to read.
3. For Foundry IQ, test a question that requires `knowledge_base_retrieve` and confirm that the spoken answer reflects the retrieved content.
4. Test successful calls, denied permissions, timeouts, unavailable dependencies, and required user confirmations. For subagents, also test delegation and follow-up questions.

See [Attach tools](configure-voice-agent#attach-tools) for configuration examples. For MCP and toolbox tools, review `response_scheduling` so a delayed result speaks at the intended point in the conversation.

## Update the client connection

Use the Foundry **project endpoint**, not the Voice Live resource endpoint. The project endpoint has this form: `https://<account>.services.ai.azure.com/api/projects/<project>`.

The voice-agent API uses `api-version=v1`, but voice agents remain a preview feature. REST requests require the `Foundry-Features: VoiceAgents=V1Preview` opt-in. The Python realtime helper supplies this header automatically.

For a raw WebSocket client, use `wss://` and replace `/voice-live/realtime` with `/api/projects/<project>/agents/<agent-name>/endpoint/protocols/voice?api-version=v1`. Request a Microsoft Entra token for `https://ai.azure.com/.default`, send it in the `Authorization` header, and include the voice-agent preview opt-in.

Resource API keys aren't a substitute for agent authentication. Don't put bearer tokens in the URL or long-lived credentials in browser code.

The new endpoint path identifies both the project and agent. Use this mapping when you replace the handshake:

| Connection detail | Voice Live text-agent integration | Foundry voice agent |
| --- | --- | --- |
| WebSocket route | `/voice-live/realtime` on the Voice Live resource. | `/api/projects/<project>/agents/<agent-name>/endpoint/protocols/voice` on the Foundry resource. |
| API version | A supported dated Voice Live API version. | `api-version=v1` plus the `Foundry-Features: VoiceAgents=V1Preview` header. |
| Agent selection | Agent and project connection parameters; the Python sample uses `agent_name`, `project_name`, and optional `agent_version`. | Project and voice-agent name in the path. Use `x-agent-version-override` to pin the tested voice-agent version. |
| Session configuration | Text-agent configuration plus Voice Live metadata and client `session.update` settings. | Saved voice-agent definition plus supported per-session overrides. |
| Python live client | `azure-ai-voicelive`. | `azure-ai-projects` through `beta.voice_agents.realtime`. |

Review cross-resource connection parameters separately; don't append them to the new URL unchanged. For the earlier connection contract, see [Voice Live agent integration](../../../ai-services/speech-service/how-to-voice-agent-integration?pivots=programming-language-python#agent-integration-concepts).

### Check the connection with Python

In Python, replace the `azure-ai-voicelive` live-session connection with the `beta.voice_agents.realtime` client in `azure-ai-projects`.

Install the Azure AI Projects client library with its voice dependencies:

```bash
python -m pip install "azure-ai-projects[voice]>=2.7.0" azure-identity
```

Reference: [Azure AI Projects client library for Python](https://aka.ms/azsdk/azure-ai-projects-v2/python/code).

Set these environment variables in the shell that runs the example:

| Variable | Value |
| --- | --- |
| `FOUNDRY_PROJECT_ENDPOINT` | The target Foundry project endpoint. |
| `FOUNDRY_VOICE_AGENT_NAME` | The **new voice agent's** name, not the source text agent's name. |
| `FOUNDRY_VOICE_AGENT_VERSION` | The voice-agent version you saved for testing. |

Save the following example as `check_voice_connection.py`, and run it with `python check_voice_connection.py`. It connects to the specified agent version, waits for `session.created`, and then closes the connection. It uses the saved configuration without overrides and doesn't send microphone audio.

```python
import os
import time

from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import (
    RealtimeServerEventError,
    RealtimeServerEventSessionCreated,
)
from azure.identity import DefaultAzureCredential

with (
    DefaultAzureCredential() as credential,
    AIProjectClient(
        endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
        credential=credential,
        allow_preview=True,
    ) as project_client,
):
    with project_client.beta.voice_agents.realtime.connect(
        agent_name=os.environ["FOUNDRY_VOICE_AGENT_NAME"],
        api_version="v1",
        extra_query={
            "x-agent-version-override": os.environ[
                "FOUNDRY_VOICE_AGENT_VERSION"
            ],
        },
    ) as connection:
        deadline = time.monotonic() + 45
        while True:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise TimeoutError("Voice session didn't become ready.")
            event = connection.recv(timeout=remaining)
            if isinstance(event, RealtimeServerEventError):
                raise RuntimeError(event.error.message)
            if isinstance(event, RealtimeServerEventSessionCreated):
                if event.conversation_id:
                    print(f"Conversation ID: {event.conversation_id}")
                print("Voice session ready.")
                break
```

Reference: [Python realtime client and event models](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/ai/azure-ai-projects/azure/ai/projects/_realtime.py).

The example prints `Voice session ready.` when the session is created. If your client sends a `session.update` override, also wait for its `session.updated` acknowledgment before using the changed settings. To test a complete spoken turn, follow [Talk to the agent](../quickstarts/prompt-voice-agent?pivots=python#talk-to-the-agent) or adapt the [live microphone sample](https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/python/voice-agents/voice_agent_realtime_audio_conversation_async.py).

Use the current Projects SDK samples for the public preview. Earlier private-preview samples that use a separate `azure-ai-voiceagents` package or `/voice_agents` management route don't describe this API.

### Update session configuration messages

Keep the model, instructions, tools, and default audio settings in the saved definition. You don't need a startup `session.update` when those defaults match your client. If you need an override in the middle of the session, translate its fields to the voice-agent schema.

For example, an older Voice Live client can set PCM audio formats with this message:

```json
{
  "type": "session.update",
  "session": {
    "input_audio_format": "pcm16",
    "output_audio_format": "pcm16",
    "input_audio_sampling_rate": 24000
  }
}
```

Reference: [Voice Live session.update](../../../ai-services/speech-service/voice-live-api-reference-2026-04-10#sessionupdate).

For a voice-agent session using 24-kHz PCM input and output, the equivalent override uses nested format objects:

```json
{
  "type": "session.update",
  "session": {
    "type": "realtime",
    "audio": {
      "input": {
        "format": {"type": "audio/pcm", "rate": 24000}
      },
      "output": {
        "format": {"type": "audio/pcm", "rate": 24000}
      }
    }
  }
}
```

Reference: [VoiceAgentSessionUpdateConfig and audio models](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/ai/azure-ai-projects/azure/ai/projects/models/_models.py).

Expect `session.updated` with the effective configuration, or an `error` event if the update is rejected. Don't start sending audio in a new format until the update succeeds.

### Adapt audio and event handling

Changing the URL alone isn't enough to migrate an older Voice Live client. Update the event dispatcher, but retain the input and response-control events that keep the same names.

| Purpose | Older Voice Live event | Voice-agent`v1`event |
| --- | --- | --- |
| Append microphone audio | `input_audio_buffer.append` | Unchanged. The JSON `audio` field contains base64-encoded bytes in the configured input format. |
| Commit or clear input | `input_audio_buffer.commit`, `input_audio_buffer.clear` | Unchanged. Use manual commit only when your application controls turn completion. |
| Detect caller speech | `input_audio_buffer.speech_started`, `input_audio_buffer.speech_stopped` | Unchanged. Use speech-start events to stop queued reply playback when the caller interrupts. |
| Stream reply audio | `response.audio.delta`, `response.audio.done` | `response.output_audio.delta`, `response.output_audio.done`. |
| Stream the reply transcript | `response.audio_transcript.delta`, `response.audio_transcript.done` | `response.output_audio_transcript.delta`, `response.output_audio_transcript.done`. |
| Stream text output | `response.text.delta`, `response.text.done` | `response.output_text.delta`, `response.output_text.done`. |
| Read caller transcription | `conversation.item.input_audio_transcription.completed` | Unchanged. Handle it when input transcription is configured. |
| Create or cancel a response | `response.create`, `response.cancel` | Unchanged. Don't create a second response while one is active. |
| Track response state | `response.created`, `response.done` | Unchanged. Inspect the final response status, not just the event name. |
| Receive function arguments | `response.function_call_arguments.delta`, `response.function_call_arguments.done` | Unchanged. Validate the complete arguments before executing a native function. |
| Return a client function result | `conversation.item.create` with a `function_call_output` item | Unchanged message pattern. The client must implement it for native function tools. |

Reference: [Voice Live events](../../../ai-services/speech-service/voice-live-api-reference-2026-04-10) and [voice-agent realtime event mappings](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/ai/azure-ai-projects/azure/ai/projects/_realtime.py).

For a complete spoken turn with automatic turn detection and response creation enabled:

1. Receive `session.created` and capture `conversation_id` when present. If you send a configuration override, wait for `session.updated` before enabling microphone input.
2. Send microphone chunks in `input_audio_buffer.append`. Let the configured turn detector commit the input and start the response; don't also send manual `response.create` events for the same turn.
3. On `response.created`, track the response ID. Decode each `response.output_audio.delta` payload and queue it for playback in the configured output format.
4. Render `response.output_audio_transcript.*` events separately from the audio stream. Don't treat transcript arrival as proof that the audio has played.
5. On `response.done`, check whether the response completed, was cancelled, failed, or is incomplete. Generation completion doesn't mean the local playback buffer is empty.
6. Handle `error` events throughout the session and report failures instead of leaving the caller waiting indefinitely.

The Python SDK maps these events to typed models. `RealtimeServerEventResponseAudioDelta` represents `response.output_audio.delta`, and its `delta` already contains decoded audio bytes. Don't base64-decode it again; raw JSON clients must decode the string themselves.

### Complete client-executed function calls

If you move a function from your text-agent application to a native voice-agent `function` tool, add its execution loop to the live client:

1. Handle `response.function_call_arguments.done`. Read `name` and `call_id`, parse the JSON string in `arguments`, and validate the requested function and arguments.
2. Wait for the corresponding `response.done` and check the response and call state. Don't execute calls from failed, incomplete, or cancelled responses. Preserve authorization and required user confirmations.
3. Execute the function and return its result with `conversation.item.create`. Use the original `call_id` and serialize the result into the string-valued `output` field.
4. If the response includes multiple calls, return their outputs before sending one `response.create` for the follow-up response. Starting it before the previous response finishes can cause a concurrent-response error.

The result message has this shape. Replace both placeholders with the actual call ID and serialized result:

```json
{
  "type": "conversation.item.create",
  "item": {
    "type": "function_call_output",
    "call_id": "<call-id-from-the-function-call>",
    "output": "<serialized-tool-result>"
  }
}
```

Reference: [Client-executed function sample](https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/python/voice-agents/voice_agent_realtime_function_tool.py).

Then send `{"type": "response.create"}` when no response is active. Don't run MCP or toolbox calls through this client loop; the service executes those tools.

### Preserve interruption and greeting behavior

Stopping generation, stopping playback, and updating conversation context are separate actions.

| Action | Client behavior |
| --- | --- |
| Stop queued speech | Clear your local playback buffer on `input_audio_buffer.speech_started`, even if generation has already finished. |
| Stop generation | Preserve the configured automatic interruption behavior. If the client cancels explicitly, send `response.cancel` only for an active response. |
| Align context with what the caller heard | If your client handles assistant-audio truncation, send `conversation.item.truncate` with the assistant `item_id`, `content_index: 0`, and played duration in `audio_end_ms`. Handle `conversation.item.truncated` as the acknowledgment. |

If the definition includes a greeting, handle its response separately from the reply to the first user turn. Remove the old client-side greeting trigger to avoid duplicate greetings.

Validate each required browser or telephony path separately.

## Configure history, recordings, and monitoring

Plan conversation storage and monitoring before switching traffic. Each voice conversation is a new record, not a continuation of the old text-agent conversation.

- Start a new voice conversation at cutover. Retain prior text-agent history according to your existing policy; don't pass its conversation ID expecting an automatic import.
- Decide whether to enable `store`, which defaults to `false`. Setting it to `true` stores the transcript, event timeline, and raw audio together. Review notice, consent, access, and retention requirements before enabling it.
- Capture the voice conversation ID from `session.created` for correlation and, when storage is enabled, read-back through `beta.voice_agents.conversations`. Don't confuse it with a realtime session ID.
- Retrieve merged recordings after the session ends. Recording finalization isn't necessarily immediate; follow the [conversation audio sample](https://github.com/microsoft-foundry/foundry-samples/blob/main/samples/python/voice-agents/voice_agent_read_conversation_audio.py).
- Configure [voice-agent tracing and monitoring](../concepts/voice-agent-observability). Conversation storage and sensitive-content capture in traces are separate controls.

Review [voice-agent pricing](../concepts/voice-agent-pricing) for model hosting, audio usage, tools, and optional features. Measure latency and cost with the new agent rather than assuming they stay the same.

## Validate and switch traffic

Test the new agent alongside the existing integration before changing production routing.

| Check | Acceptance condition |
| --- | --- |
| Business behavior | The agent follows the same business rules and handles required scenarios correctly. |
| Speech | Recognition, language, pronunciation, voice, and audio formats work on each target device. |
| Turn-taking | Pauses, interruptions, queued playback, and opening greetings behave as intended. |
| Tools and subagents | Each required tool succeeds through its new integration route. Foundry IQ retrieval preserves source access controls, failures are visible, and delegation preserves user intent. |
| Identity and network | Intended callers can connect and reach dependencies without broadening access. |
| History and privacy | Storage and trace-content settings match policy, and authorized users can retrieve the expected records. |
| Channels | Browser and phone integrations connect to the tested voice agent and version. |
| Response latency | Median and tail time to first audio meet your targets under representative load. Compare direct answers, retrieval, and action-taking turns against the old integration. Measure time to the substantive answer separately from interim speech. |
| Reliability and cost | Error rates, concurrent-call behavior, and usage meet your application's acceptance criteria. |

For latency comparisons, keep prompts, tools, channel, and load consistent. If you also change models, record that change separately. Use [voice-agent monitoring](../concepts/voice-agent-observability#monitor-a-voice-based-agent) to diagnose stage delays, and measure client-side time until playback starts.

After the checks pass, switch traffic gradually:

1. Pin the tested voice-agent version and any toolbox or subagent versions your release depends on.
2. Configure the required [voice-agent channels](voice-agent-channels-publish). Creating a voice agent doesn't migrate existing text-agent app publishing or phone configuration.
3. Update a test client or a limited traffic route to use the new voice endpoint, and repeat the checks for that route.
4. Increase traffic only after the checks pass. Let existing calls finish on their original integration; don't change the endpoint during a call.
5. Keep the old endpoint, agent, and client configuration available for rollback. If needed, route new sessions back to the original integration.
6. Retire the old path only after confirming that no applications still depend on it and that required historical records are retained.

## Troubleshoot migration issues

Use these symptoms to identify configuration differences between the existing integration and the new voice agent.

| Symptom | What to check |
| --- | --- |
| Creation or connection rejects the agent kind | Use a new agent name with a voice definition, a supported project region, and the preview opt-in. |
| Connection works but no reply audio reaches the client | Check the configured modalities and audio format, and update legacy event handlers to the `response.output_*` names. |
| The first reply is missing or the greeting repeats | Separate the configured greeting's response from the first user response, and remove any duplicate client-side greeting trigger. |
| A migrated tool never completes | Confirm its execution model. Native functions need client implementation; MCP, toolbox, and subagent dependencies need valid configuration and permissions. |
| Stored conversation lookup returns `404` | Check the effective `store` setting, target voice agent, conversation ID, and caller access. An old text-agent conversation ID isn't the new voice conversation ID. |
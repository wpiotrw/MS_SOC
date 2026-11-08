---
layout: Conceptual
title: Use a delegate subagent in a voice-based agent - Microsoft Foundry | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/use-delegate-subagent-voice-agent
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
author: PatrickFarley
learn_banner_products:
- azure
manager: mcleans
ms.author: pafarley
ms.collection: ce-skilling-ai-copilot
ms.update-cycle: 90-days
ms.service: microsoft-foundry
description: Learn how a voice-based agent delegates a focused task to a separate prompt or hosted agent in Microsoft Foundry.
ms.date: 2026-11-05T00:00:00.0000000Z
ms.topic: how-to
ms.subservice: foundry-agent-service
ms.custom: preview, doc-kit-assisted
ai-usage: ai-assisted
locale: en-us
document_id: 03c89ccf-e15c-9ecd-3621-c2eeebf445da
document_version_independent_id: 41ef11ba-63f7-6a90-74fd-ab82c88b605c
original_content_git_url: https://github.com/MicrosoftDocs/azure-ai-docs-pr/blob/live/articles/foundry/agents/how-to/use-delegate-subagent-voice-agent.md
site_name: Docs
depot_name: Learn.azure-ai
page_type: conceptual
toc_rel: ../../toc.json
asset_id: foundry/agents/how-to/use-delegate-subagent-voice-agent
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/foundry/agents/how-to/use-delegate-subagent-voice-agent.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/64b65f6c-101f-411a-9b83-9f577fab52d0
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/de19c5b8-e208-412e-9238-db3f631dea5b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1a667fd1-8145-4b11-af0f-9f5de205a6e5
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ea7bf5d6-7154-4ba9-8ebc-59117ccacd49
platformId: 964dc73d-8d1b-a895-2945-f2efc3fa88d9
---

# Use a delegate subagent in a voice-based agent - Microsoft Foundry | Microsoft Learn

In this article, you configure a voice-based agent in Microsoft Foundry to delegate a focused task to a separate prompt or hosted agent, and then test the resulting voice experience.

A **delegate subagent** is a separate Agent resource. The voice-based agent invokes it, receives its result, and remains the active behavior for the conversation. Use a delegate subagent for bounded work, such as research, analysis, content generation, or a specialist lookup. To compare delegate and inline subagents and choose a type, see [Subagents in voice-based agents](../concepts/voice-agent-subagents).

The delegate subagent can be a Foundry prompt agent or hosted agent. The following sections create a prompt agent that writes poems and reference it from a voice-based agent. You can apply similar steps to a hosted agent.

## Prerequisites

- A [Foundry project](../../how-to/create-projects) with access to voice-based agents.
- [Foundry User role](../../concepts/rbac-foundry) on the project. 
    Important

    The Foundry RBAC roles were recently renamed. **Foundry User**, **Foundry Owner**, **Foundry Account Owner**, and **Foundry Project Manager** were previously named Azure AI User, Azure AI Owner, Azure AI Account Owner, and Azure AI Project Manager. You might still see the previous names in some places while the rename rolls out. The role IDs and core permissions are unchanged by the rename.
- Python 3.10 or later.
- The Azure CLI, signed in with `az login`.
- A voice model and a text model available to your project.
- A microphone and speakers or headphones.

## Install the packages

Install the Microsoft Foundry SDK version 2.7.0 or later with the `voice` extra, Azure Identity client library, and PyAudio in the same Python environment. The `voice` extra supplies `aiohttp` for asynchronous connections. PyAudio handles microphone capture and speaker playback.

```bash
python -m pip install "azure-ai-projects[voice]>=2.7.0" pyaudio
```

For Python SDK setup details, see [Install the packages](../quickstarts/prompt-voice-agent?pivots=python#install-the-packages).

## Set environment variables

Set the project endpoint and model deployment names. In Bash:

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<account>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_SUBAGENT_MODEL="<text-model-deployment-name>"
export FOUNDRY_VOICE_MODEL="gpt-realtime"
```

In PowerShell:

```powershell
$env:FOUNDRY_PROJECT_ENDPOINT = "https://<account>.services.ai.azure.com/api/projects/<project>"
$env:FOUNDRY_SUBAGENT_MODEL = "<text-model-deployment-name>"
$env:FOUNDRY_VOICE_MODEL = "gpt-realtime"
```

Find the project endpoint on the **Overview** page of your project in the Foundry portal.

## Create a delegate subagent

Create a prompt agent with one focused responsibility. The following example creates a separate Agent resource that writes poems based on a user's requested topic and style.

```python
import os

from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition
from azure.identity import DefaultAzureCredential

endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
model = os.environ["FOUNDRY_SUBAGENT_MODEL"]

definition = PromptAgentDefinition(
    model=model,
    instructions=(
        "You are a poetry-writing agent. Write an original poem that "
        "matches the user's requested topic, style, tone, and length. "
        "When the request doesn't specify these details, write a short "
        "poem in free verse. Return only the poem."
    ),
)

with (
    DefaultAzureCredential() as credential,
    AIProjectClient(
        endpoint=endpoint,
        credential=credential,
        allow_preview=True,
    ) as project_client,
):
    poetry_agent = project_client.agents.create_version(
        agent_name="poetry-agent",
        definition=definition,
    )
    print(
        f"Created subagent '{poetry_agent.name}', "
        f"version {poetry_agent.version}"
    )
```

Reference: [Azure AI Projects client library for Python](https://aka.ms/azsdk/azure-ai-projects-v2/python/code).

You can also create a delegate subagent in the Foundry portal or deploy a code-based hosted agent.

## Configure a delegate subagent in the voice-based agent

Create the voice-based agent by using the project endpoint. In `subagent_config`, set `subagent_type` to `delegate`, identify the poetry agent by name, and describe when the voice-based agent delegates a request to it.

```python
import os

from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import (
    RealtimeAudioFormatsAudioPcm,
    VoiceAgentAudioConfig,
    VoiceAgentAudioInputConfig,
    VoiceAgentAudioOutputConfig,
    VoiceAgentDefinition,
    VoiceAgentInputTranscription,
    VoiceAgentServerVadTurnDetection,
    VoiceAgentSubagentConfig,
)
from azure.identity import DefaultAzureCredential

endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
model = os.environ.get("FOUNDRY_VOICE_MODEL", "gpt-realtime")

definition = VoiceAgentDefinition(
    model_type="managed",
    model=model,
    instructions=(
        "Answer ordinary questions yourself. When the user asks for a poem, "
        "always call forward_to_subagent for the configured poetry agent. "
        "After the poetry agent returns, read the poem exactly as written."
    ),
    store=True,
    output_modalities=["audio"],
    audio=VoiceAgentAudioConfig(
        input=VoiceAgentAudioInputConfig(
            format=RealtimeAudioFormatsAudioPcm(rate=24000),
            turn_detection=VoiceAgentServerVadTurnDetection(
                threshold=0.5,
                prefix_padding_ms=300,
                silence_duration_ms=1000,
            ),
            transcription=VoiceAgentInputTranscription(
                model="azure-speech",
            ),
        ),
        output=VoiceAgentAudioOutputConfig(
            format=RealtimeAudioFormatsAudioPcm(rate=24000),
            voice="en-US-JennyNeural",
            voice_type="azure-standard",
        ),
    ),
    subagent_config=VoiceAgentSubagentConfig(
        {
            "subagent_type": "delegate",
            "subagents": [
                {
                    "agent_name": "poetry-agent",
                    "agent_capabilities": (
                        "Writes original poems based on the requested topic, "
                        "style, tone, and length."
                    ),
                    "response_policy": {
                        "immediate_ack": True,
                    },
                }
            ],
        }
    ),
)

with (
    DefaultAzureCredential() as credential,
    AIProjectClient(
        endpoint=endpoint,
        credential=credential,
        allow_preview=True,
    ) as project_client,
):
    voice_agent = project_client.agents.create_version(
        agent_name="poetry-voice-agent",
        definition=definition,
        description="Voice agent that delegates poetry requests",
    )
    print(
        f"Created voice agent '{voice_agent.name}', "
        f"version {voice_agent.version}"
    )
```

Reference: [Azure AI Projects client library for Python](https://aka.ms/azsdk/azure-ai-projects-v2/python/code).

A voice agent version uses either delegate or inline subagents. Don't mix the two modes in one `subagent_config`.

The Python example initializes `VoiceAgentSubagentConfig` from a dictionary to send `subagent_type: delegate` explicitly. This approach also works with SDK versions that don't expose `subagent_type` as a generated model property.

## Talk to the voice-based agent

Connect to the voice-based agent with the Microsoft Foundry SDK. The client streams microphone audio to the agent and plays the spoken response as it arrives. Use headphones to prevent the speaker output from feeding back into the microphone. Run the package installation command with the same Python environment that you use to run the client.

Create a file named `talk_to_voice_agent.py`:

```python
import asyncio
import os

import pyaudio
from azure.ai.projects import models
from azure.ai.projects.aio import AIProjectClient
from azure.ai.projects.aio.operations import AsyncBetaRealtimeConnection
from azure.identity.aio import DefaultAzureCredential

RATE = 24000
CHUNK = 2400

async def wait_until_ready(
    connection: AsyncBetaRealtimeConnection,
) -> None:
    while True:
        event = await connection.recv()
        if isinstance(event, models.RealtimeServerEventSessionCreated):
            return
        if isinstance(event, models.RealtimeServerEventError):
            raise RuntimeError(event.error.message)

async def send_microphone(
    connection: AsyncBetaRealtimeConnection, stream: pyaudio.Stream
) -> None:
    while True:
        audio = await asyncio.to_thread(
            stream.read,
            CHUNK,
            exception_on_overflow=False,
        )
        await connection.input_audio_buffer.append(audio=audio)

async def receive_audio(
    connection: AsyncBetaRealtimeConnection, stream: pyaudio.Stream
) -> None:
    async for event in connection:
        if isinstance(
            event,
            models.RealtimeServerEventResponseAudioDelta,
        ):
            await asyncio.to_thread(stream.write, event.delta)
        elif isinstance(
            event,
            models.RealtimeServerEventResponseAudioTranscriptDone,
        ):
            print(f"Agent: {event.transcript}")
        elif isinstance(event, models.RealtimeServerEventError):
            raise RuntimeError(event.error.message)

async def talk() -> None:
    endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
    audio = pyaudio.PyAudio()
    microphone = audio.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK,
    )
    speaker = audio.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=RATE,
        output=True,
        frames_per_buffer=CHUNK,
    )

    try:
        async with (
            DefaultAzureCredential() as credential,
            AIProjectClient(
                endpoint=endpoint,
                credential=credential,
                allow_preview=True,
            ) as project_client,
            project_client.beta.voice_agents.realtime.connect(
                agent_name="poetry-voice-agent",
            ) as connection,
        ):
            await asyncio.wait_for(wait_until_ready(connection), timeout=30)
            print("Connected. Ask the agent to write a poem.")
            await asyncio.gather(
                send_microphone(connection, microphone),
                receive_audio(connection, speaker),
            )
    finally:
        microphone.close()
        speaker.close()
        audio.terminate()

asyncio.run(talk())
```

Reference: [Azure AI Projects client library for Python](https://aka.ms/azsdk/azure-ai-projects-v2/python/code).

The client waits for `session.created` before streaming microphone audio. It uses the agent's saved configuration, so it doesn't send `session.update` or wait for `session.updated`.

Run the client:

```bash
python talk_to_voice_agent.py
```

After the client connects, ask it to write a short poem about the sea. The voice agent delegates the request to `poetry-agent` and speaks the returned poem. Press `Ctrl+C` to disconnect.

## Use the voice-based agent in the Foundry portal

Open the voice-based agent in the playground to have a spoken conversation:

1. Sign in to the [Foundry portal](https://ai.azure.com).
2. Open the project that contains the voice-based agent and delegate subagent.
3. Select **Build** &gt; **Agents**.
4. Select **poetry-voice-agent**, and then select **Open in playground**.
5. Start a voice session.
6. Ask the agent to write a short poem about the sea.

The voice agent delegates the request to `poetry-agent` and speaks the returned poem.

## Configure delegate subagent behavior

The `subagent_config` object identifies separate text agents that the voice-based agent can consult. Each delegate subagent must belong to the same Foundry project as the voice-based agent. Configure at least one entry in the `subagents` array.

| Property | Required | Description |
| --- | --- | --- |
| `agent_name` | Yes | Specifies the name of the separate prompt or hosted agent. |
| `agent_version` | No | Pins a specific subagent version. If you omit this property, the voice agent uses the active version. |
| `agent_capabilities` | Yes | Describes the subagent's specialization. The voice agent uses this description to decide whether to delegate a request. |
| `invoke_timeout_seconds` | No | Sets the invocation timeout from 5 through 1,200 seconds. If you omit this property, the service timeout applies. |

Use the optional `response_policy` object to control what the voice agent says while it waits for a delegated result:

| Property | Description |
| --- | --- |
| `immediate_ack` | Specifies whether the voice agent immediately acknowledges that it forwarded the request. |
| `ack_instructions` | Provides instructions for generating the immediate acknowledgment. |
| `enable_delta_progress` | Emits progress incrementally instead of waiting for the subagent invocation to finish. The default is `false`. |
| `gap_filling_interval` | Sets the period without subagent content or user input before a gap-filling response. Use a value from 5 through 120 seconds. |
| `gap_filling_instructions` | Provides instructions for speech generated while the voice agent waits for progress. |
| `progress_instructions` | Provides instructions for summarizing streamed subagent progress as speech. |
| `progress_update_interval` | Sets the minimum time between spoken progress updates. Use a value from 5 through 300 seconds. |

In Python, use `datetime.timedelta` for `invoke_timeout_seconds`, `gap_filling_interval`, and `progress_update_interval`. The SDK serializes these values as seconds.

## Apply delegate subagent best practices

- Give each delegate subagent one clearly defined capability.
- Use a delegate subagent for bounded work that returns a result to the active voice-based agent.
- Tune the voice-based agent instructions and `agent_capabilities` together.
- Use an [inline subagent](use-inline-subagent-voice-agent) when a specialist needs to own several subsequent conversation turns.
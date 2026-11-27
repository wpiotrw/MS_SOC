---
layout: Conceptual
title: Register external agents for observability and evaluation - Microsoft Foundry | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/register-external-agent
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
author: sdgilley
learn_banner_products:
- azure
manager: mcleans
ms.author: sgilley
ms.collection: ce-skilling-ai-copilot
ms.update-cycle: 90-days
ms.service: microsoft-foundry
description: Register third-party agents running on any host in Microsoft Foundry for tracing and evaluation, without migrating the runtime or provisioning an AI Gateway.
ms.date: 2026-11-11T00:00:00.0000000Z
ms.subservice: foundry-agent-service
ms.topic: how-to
ms.custom: doc-kit-assisted, dev-focus
ai-usage: ai-assisted
locale: en-us
document_id: bd957f66-7226-296b-4431-8622bc02f067
document_version_independent_id: 03e089ec-1126-8d14-5ab2-3fc69bb60816
original_content_git_url: https://github.com/MicrosoftDocs/azure-ai-docs-pr/blob/live/articles/foundry/agents/how-to/register-external-agent.md
site_name: Docs
depot_name: Learn.azure-ai
page_type: conceptual
toc_rel: ../../toc.json
asset_id: foundry/agents/how-to/register-external-agent
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/foundry/agents/how-to/register-external-agent.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
- https://authoring-docs-microsoft.poolparty.biz/devrel/64b65f6c-101f-411a-9b83-9f577fab52d0
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/de19c5b8-e208-412e-9238-db3f631dea5b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
- https://authoring-docs-microsoft.poolparty.biz/devrel/1a667fd1-8145-4b11-af0f-9f5de205a6e5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ea7bf5d6-7154-4ba9-8ebc-59117ccacd49
platformId: 13fff770-4f43-bf38-aa28-cfdc29c9fc8f
---

# Register external agents for observability and evaluation - Microsoft Foundry | Microsoft Learn

Important

When you use external agents with other Microsoft products and services, you must read all relevant documentation for such products and services and understand related risks and compliance considerations.

If you use external agents with any third-party servers, agents, code, or non-Azure Direct models ("Third-Party Systems"), you do so at your own risk. Third-Party Systems are Non-Microsoft Products under the Microsoft Product Terms and are governed by their own third-party license terms. You're responsible for any usage and associated costs.

We recommend reviewing all data being shared with and received from Third-Party Systems and being cognizant of third-party practices for handling, sharing, retention, and location of data. Similarly, if you connect to or integrate with non-Foundry Microsoft services and features, it is important to review their data practices. It is your responsibility to manage whether your data will flow outside of your organization’s compliance and geographic boundaries and any related implications, and that appropriate permissions, boundaries, and approvals are provisioned.

You're responsible for carefully reviewing and testing applications you build in the context of your specific use cases and making all appropriate decisions and customizations. This includes implementing your own responsible AI mitigations, such as metaprompts, content filters, or other safety systems, and ensuring your applications meet appropriate quality, reliability, security, and trustworthiness standards. See the [Foundry Agent Service transparency note](../../observability/concepts/trace-data).

Microsoft Foundry Agent Service lets you register agents that run outside Foundry, on any cloud, on-premises, or other host, so you can use Foundry's trace view and evaluation experiences. Foundry stores only registration metadata for these agents. It doesn't host, proxy, or invoke the runtime.

External agents are the recommended integration for evaluation and observability use cases in Microsoft Foundry going forward. Use external agent registration for new integrations with agents that run outside Foundry.

Microsoft Foundry Control Plane deprecates [custom agents](../../control-plane/register-custom-agent) on May 7, 2027. That integration routes traffic through an AI Gateway. With external agents, your agent keeps its existing endpoint and shares only OpenTelemetry telemetry. No AI Gateway is required. External agents don't proxy agent traffic or provide gateway-based blocking.

You can no longer add new Control Plane custom agents. If you have an existing custom agent, [migrate to external agents](../../control-plane/migrate-custom-to-external-agent) by preserving its OpenTelemetry agent ID and keeping its existing gateway and invocation route.

In this article, you learn how to:

- Instrument an external agent to emit OpenTelemetry spans to Application Insights.
- Register the agent in Foundry as an `external` agent.
- Verify traces in the Foundry portal.
- Run a trace-based evaluation over the agent's collected telemetry.

The following diagram shows the data flow: your external agent emits OpenTelemetry spans with a `gen_ai.agent.id` attribute to an Application Insights resource connected to your Foundry project. A separate registration call creates the agent record in Foundry. The Foundry portal then matches traces by agent ID and displays them in the agent trace view.

[![Diagram that shows the data flow for external agent observability. The external agent emits OpenTelemetry spans to Application Insights, which connects to the Foundry portal trace view. A separate registration call creates the agent record in the Foundry project.](../media/register-external/architecture.svg)](../media/register-external/architecture.svg#lightbox)

## Prerequisites

- A [Foundry project](../../how-to/create-projects) with an [Application Insights resource connected](../../observability/how-to/trace-agent-setup#connect-application-insights-to-your-foundry-project).
- An agent running outside Foundry that can emit OpenTelemetry spans to that Application Insights resource.
- Python 3.11 or later for the OpenTelemetry instrumentation. To register the agent with an SDK, you also need Python, the [.NET SDK](https://dotnet.microsoft.com/download), or Node.js.
- **Foundry User** role on the project.
- **Reader** role or **Monitoring Reader** role on the connected Application Insights resource to view traces.

    Important

    The Foundry RBAC roles were recently renamed. **Foundry User**, **Foundry Owner**, **Foundry Account Owner**, and **Foundry Project Manager** were previously named Azure AI User, Azure AI Owner, Azure AI Account Owner, and Azure AI Project Manager. You might still see the previous names in some places while the rename rolls out. The role IDs and core permissions are unchanged by the rename.
- `DefaultAzureCredential` configured. Sign in with `az login` or set up a managed identity or service principal.
- *(For evaluation only)* An Azure OpenAI deployment with a GPT model that supports chat completion (for example, `gpt-5-mini`).

## Instrument the external agent with OpenTelemetry

Before you register the agent in Foundry, configure it to export OpenTelemetry spans to the Application Insights resource connected to your Foundry project. The top-level `invoke_agent` span must carry the `gen_ai.agent.id` attribute so Foundry can match the trace to the agent registration and to trace-based evaluations.

### Install the Microsoft OpenTelemetry package

```bash
pip install "microsoft-opentelemetry>=1.6.0"
```

### Configure the exporter

Run this code once during agent startup, before any framework imports that should be instrumented:

```python
import os

os.environ.setdefault("AZURE_EXPERIMENTAL_ENABLE_GENAI_TRACING", "true")
os.environ.setdefault("OTEL_SEMCONV_STABILITY_OPT_IN", "gen_ai_latest_experimental")
os.environ.setdefault("OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT", "SPAN_AND_EVENT")

from microsoft.opentelemetry import use_microsoft_opentelemetry

# Human-readable name for the agent
AGENT_NAME = os.environ.get("AGENT_NAME", "travel-planner-agent")
# Stable ID emitted as gen_ai.agent.id on the invoke_agent span.
# Foundry matches traces to registrations by this value.
OTEL_AGENT_ID = os.environ.get("OTEL_AGENT_ID", AGENT_NAME)

use_microsoft_opentelemetry(
    enable_azure_monitor=True,
    azure_monitor_connection_string=os.environ["APPLICATIONINSIGHTS_CONNECTION_STRING"],
    sampling_ratio=1.0,
    instrumentation_options={
        "fastapi": {"enabled": False},
        "langchain": {
            "enabled": True,
            "agent_id": OTEL_AGENT_ID,
            "agent_name": AGENT_NAME,
        },
    },
)
```

Set the `APPLICATIONINSIGHTS_CONNECTION_STRING` environment variable on the host where the agent runs. Use the connection string from the Application Insights resource linked to your Foundry project. To find the connection string, open the [Foundry portal](https://ai.azure.com), go to your project, and select **Manage** &gt; **Project details** &gt; **Connected resources**. Select the Application Insights resource to view its connection string. Alternatively, open the Application Insights resource directly in the Azure portal and copy the connection string from the **Overview** page.

After configuration, subsequent OpenTelemetry spans from your agent framework automatically flow to Application Insights. The distro sets `gen_ai.agent.id` on the `invoke_agent` span. Its value must match the `otel_agent_id` you use during registration.

If your agent framework doesn't set this attribute automatically, add it manually:

```python
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("invoke_agent travel-planner-agent") as span:
    span.set_attribute("gen_ai.operation.name", "invoke_agent")
    span.set_attribute("gen_ai.agent.id", "travel-planner-agent")
    span.set_attribute("gen_ai.agent.name", "travel-planner-agent")
    # ... your agent logic ...
```

Tip

For framework-specific auto-instrumentation (LangChain, LangGraph), the [Microsoft OpenTelemetry distro for Python](https://github.com/microsoft/opentelemetry-distro-python) can set `gen_ai.agent.id` automatically via `instrumentation_options`. For .NET and JavaScript, see the [.NET distro](https://github.com/microsoft/opentelemetry-distro-dotnet) and [JavaScript distro](https://github.com/microsoft/opentelemetry-distro-javascript). For general guidance, see [Configure tracing for AI agent frameworks](../../observability/how-to/trace-agent-framework).

## Register the external agent in Foundry

After the agent emits spans to Application Insights, register it in Foundry so those spans appear in the Foundry trace view scoped to the agent. Registering creates a named record in Foundry that links incoming traces (matched by `gen_ai.agent.id`) to the Foundry agent experience. Without this registration, traces still flow into Application Insights but don't appear in the Foundry agent trace view.

### Create the registration

# [Foundry portal](#tab/portal)
You can create a registration in the [Foundry portal](https://ai.azure.com) by:

1. Opening your project and selecting **Build** &gt; **Agents** &gt; **New agent**.
2. Selecting **Link external agent**.
3. In the window that appears, entering the agent name, description, and the OpenTelemetry ID.

    [![Screenshot showing the button to link an external agent.](../media/register-external/foundry-button.png)](../media/register-external/foundry-button.png#lightbox)

# [Python SDK](#tab/python)
Install the SDK:

```bash
pip install "azure-ai-projects>=2.11.0"
```

Set the `FOUNDRY_PROJECT_ENDPOINT` environment variable to your project endpoint. You can find this value on the project's **Overview** page in the Foundry portal.

```python
import os
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import ExternalAgentDefinition
from azure.identity import DefaultAzureCredential

endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]

# Create the project client.
project = AIProjectClient(
    endpoint=endpoint,
    credential=DefaultAzureCredential(),
)

# Register the externally hosted agent.
agent = project.agents.create_version(
    agent_name="travel-planner-agent",
    description="Travel planning agent hosted externally.",
    definition=ExternalAgentDefinition(
        # Optional. Defaults to the agent name. Set it when the running
        # agent emits a different gen_ai.agent.id value.
        otel_agent_id="travel-planner-agent",
    ),
)

print(f"Registered external agent: {agent.name}")
print(f"Resolved otel_agent_id: {agent.definition.otel_agent_id}")
```

```output
Registered external agent: travel-planner-agent
Resolved otel_agent_id: travel-planner-agent
```

Note

The `otel_agent_id` parameter is optional and defaults to the agent `name`. Set it explicitly only when the running agent already emits a stable `gen_ai.agent.id` value that differs from the Foundry agent name.

The `create_version()` method atomically creates the agent record and its first registration revision when called with a new name. External agents are versionless from the user's perspective. Edits to `otel_agent_id` create a new internal revision under the same name.

# [C# SDK](#tab/csharp)
Set the `FOUNDRY_PROJECT_ENDPOINT` environment variable to your project endpoint. Install the packages with `dotnet add package Azure.AI.Projects.Agents --prerelease` and `dotnet add package Azure.Identity`.

```csharp
#pragma warning disable AAIP001
using System;
using Azure.AI.Projects.Agents;
using Azure.Identity;

var endpoint = Environment.GetEnvironmentVariable("FOUNDRY_PROJECT_ENDPOINT");

// The .NET SDK still marks ExternalAgentDefinition as experimental (AAIP001).
AgentAdministrationClient agentsClient = new(
    endpoint: new Uri(endpoint),
    tokenProvider: new DefaultAzureCredential());

// Register the externally hosted agent.
ExternalAgentDefinition definition = new()
{
    // Optional. Defaults to the agent name. Set it when the running
    // agent emits a different gen_ai.agent.id value.
    OtelAgentId = "travel-planner-agent",
};
ProjectsAgentVersionCreationOptions options = new(definition)
{
    Description = "Travel planning agent hosted externally.",
};
ProjectsAgentVersion agent = agentsClient.CreateAgentVersion(
    agentName: "travel-planner-agent",
    options: options);

Console.WriteLine($"Registered external agent: {agent.Name}");
```

```output
Registered external agent: travel-planner-agent
```

# [JavaScript/TypeScript SDK](#tab/javascript)
Set the `FOUNDRY_PROJECT_ENDPOINT` environment variable to your project endpoint. Find this value on the project's **Overview** page in the Foundry portal.

Install the required packages:

```bash
npm install @azure/ai-projects @azure/identity
```

```typescript
import { AIProjectClient } from "@azure/ai-projects";
import { DefaultAzureCredential } from "@azure/identity";

const projectEndpoint =
  process.env["FOUNDRY_PROJECT_ENDPOINT"] || "<project endpoint>";

const project = new AIProjectClient(
  projectEndpoint,
  new DefaultAzureCredential(),
);

const agentName = "travel-planner-agent";
// Optional. Defaults to the agent name. Set it when the running
// agent emits a different gen_ai.agent.id value.
const otelAgentId = "travel-planner-agent";

// Register the externally hosted agent.
const agent = await project.agents.createVersion(
  agentName,
  {
    kind: "external",
    otel_agent_id: otelAgentId,
  },
  {
    description: "Travel planning agent hosted externally.",
  },
);

console.log(`Registered external agent: ${agent.name}`);
console.log(`Resolved otel_agent_id: ${otelAgentId}`);
```

```output
Registered external agent: travel-planner-agent
Resolved otel_agent_id: travel-planner-agent
```

Note

The `otel_agent_id` field is optional and defaults to the agent `name`. Set it explicitly only when the running agent already emits a stable `gen_ai.agent.id` value that differs from the Foundry agent name.

The `createVersion()` method atomically creates the agent record and its first registration revision when called with a new name. External agents are versionless from the user's perspective. Edits to `otel_agent_id` create a new internal revision under the same name.

Reference: [AIProjectClient](/en-us/javascript/api/overview/azure/ai-projects-readme)

---

## Verify traces in the Foundry portal

After the agent sends traffic and spans ingest into Application Insights (typically 2–5 minutes), verify that traces appear in the Foundry portal:

1. Open the [Foundry portal](https://ai.azure.com).
2. Go to your project.
3. Select **Build** &gt; **Agents**.
4. Select the external agent name (for example, **travel-planner-agent**).
5. Select the **Traces** tab to view spans attributed to this agent.

Traces are matched by `gen_ai.agent.id = <otel_agent_id>` from the Application Insights resource connected to the project. You can view inputs, outputs, tool calls, and latency for each span.

## Run a trace-based evaluation

After traces flow into Application Insights, you can run evaluations directly over those traces. No separate dataset construction is required. Foundry resolves traces by matching `(project, agent_id)` over a lookback window.

Tip

To evaluate the agent's traces on a recurring schedule, create a scheduled trace evaluation rule and set `agent_id` to the agent's `otel_agent_id` in the trace source. For steps, see [Continuous and scheduled evaluation](../../observability/how-to/continuous-scheduled-evaluation).

### Resolve the agent's otel\_agent\_id

To get the agent's ID for traces, use the following:

# [Foundry portal](#tab/portal)
Open the external agent in the Foundry portal to view its traces. To retrieve the resolved `otel_agent_id` in code, use one of the SDK tabs.

# [Python SDK](#tab/python)
```python
# Retrieve the registered agent and its resolved otel_agent_id.
agent = project.agents.get(agent_name="travel-planner-agent")
otel_agent_id = agent.versions.latest.definition.otel_agent_id
```

# [C# SDK](#tab/csharp)
```csharp
#pragma warning disable AAIP001
// Retrieve the registered agent and its resolved otel_agent_id.
ProjectsAgentRecord agent = agentsClient.GetAgent("travel-planner-agent");
if (agent.GetLatestVersion().Definition is not ExternalAgentDefinition definition)
{
    throw new InvalidOperationException("Expected an external agent definition.");
}

string otelAgentId = definition.OtelAgentId;
```

# [JavaScript/TypeScript SDK](#tab/javascript)
```typescript
// Retrieve the registered agent and its resolved otel_agent_id.
const agent = await project.agents.get("travel-planner-agent");
const definition = agent.versions.latest.definition;
if (definition.kind !== "external") {
  throw new Error(
    `Expected an external agent definition, got "${definition.kind}".`,
  );
}
const otelAgentId = definition.otel_agent_id;
```

---

### Create and run the evaluation

Use the `otel_agent_id` to run a trace evaluation over the agent's collected telemetry. External agents support trace-based evaluation of individual interactions. You can also evaluate multi-turn conversations by conversation ID when the agent emits a stable `gen_ai.conversation.id` and the required message attributes on its `invoke_agent` spans.

For walkthroughs that show how to create an evaluation, configure testing criteria, and interpret results, see:

- [Evaluate individual interactions from deployed models and agents](../../observability/how-to/cloud-evaluation-deployed-interactions#evaluate-traces).
- [Evaluate deployed model and agent conversations](../../observability/how-to/cloud-evaluation-deployed-conversations).

## Manage external agents

Use the same SDK methods to list, retrieve, and delete external agents.

### List external agents

# [Foundry portal](#tab/portal)
In the Foundry portal, select **Build** &gt; **Agents** to view registered external agents.

# [Python SDK](#tab/python)
```python
agents = project.agents.list(kind="external")
for a in agents:
    print(a.name)
```

# [C# SDK](#tab/csharp)
```csharp
#pragma warning disable AAIP001
foreach (ProjectsAgentRecord agent in agentsClient.GetAgents(kind: ProjectsAgentKind.External))
{
    Console.WriteLine(agent.Name);
}
```

# [JavaScript/TypeScript SDK](#tab/javascript)
```typescript
const agents = project.agents.list({ kind: "external" });
for await (const agent of agents) {
  console.log(agent.name);
}
```

---

### Delete an external agent

# [Foundry portal](#tab/portal)
Use one of the SDK tabs to delete an external agent registration. Deleting the registration doesn't affect the externally hosted agent.

# [Python SDK](#tab/python)
```python
# Delete the registration. This does not affect the running agent.
# force=True removes all internal revisions of the agent atomically.
project.agents.delete(agent_name="travel-planner-agent", force=True)
```

# [C# SDK](#tab/csharp)
```csharp
#pragma warning disable AAIP001
// Delete the registration. This action doesn't affect the running agent.
// force: true removes all internal revisions of the agent atomically.
agentsClient.DeleteAgent(agentName: "travel-planner-agent", force: true);
```

# [JavaScript/TypeScript SDK](#tab/javascript)
```typescript
// Delete the registration. This does not affect the running agent.
// force: true removes all internal revisions of the agent atomically.
await project.agents.delete("travel-planner-agent", { force: true });
```

Reference: [AIProjectClient](/en-us/javascript/api/overview/azure/ai-projects-readme)

---

Deleting the registration removes the agent from the Foundry portal and stops traces from appearing in the Foundry agent trace view. The spans remain in Application Insights, and the running agent is not affected.

## Troubleshooting

### Troubleshoot missing traces

If you don't see traces, check the following items:

- The Application Insights resource is connected to the Foundry project where you registered the agent.
- The `otel_agent_id` on the registration matches the `gen_ai.agent.id` attribute on the agent's `invoke_agent` span.
- The agent process has `APPLICATIONINSIGHTS_CONNECTION_STRING` set to the correct Application Insights resource.
- Spans comply with [OpenTelemetry semantic conventions for generative AI](https://opentelemetry.io/docs/specs/semconv/gen-ai/).

For more troubleshooting guidance, see [Troubleshoot evaluation and observability issues](../../observability/how-to/troubleshooting).

### Troubleshoot registration errors

If `create_version()` (Python) or `createVersion()` (JavaScript/TypeScript) fails, check the following items:

- Your identity has the **Foundry User** role (or higher) on the project.
- The agent name value uses only alphanumeric characters, hyphens, and underscores.
- No existing agent with the same name and a different kind already exists. Use `project.agents.get()` to check.

## Current limitations

The following Foundry features aren't currently supported for external agents:

- [Human evaluation](../../observability/how-to/human-evaluation) — Manual review workflows aren't available for externally registered agents.
- [AI red teaming](../../concepts/ai-red-teaming-agent) — Red teaming scans can't target external agents.
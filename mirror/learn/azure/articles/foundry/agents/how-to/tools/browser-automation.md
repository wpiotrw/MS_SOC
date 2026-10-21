---
layout: Conceptual
title: Automate browser tasks with Foundry agents - Microsoft Foundry | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/browser-automation
breadcrumb_path: ../../../../breadcrumb/azure-ai/toc.json
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
author: mattwojo
learn_banner_products:
- azure
manager: mcleans
ms.author: mattwoj
ms.collection: ce-skilling-ai-copilot
ms.update-cycle: 90-days
ms.service: microsoft-foundry
description: Automate web browsing tasks with the Browser Automation tool in Microsoft Foundry agents. Create isolated Playwright sessions for navigation and form filling.
services: cognitive-services
ms.subservice: foundry-agent-service
ms.topic: how-to
ms.date: 2026-10-06T00:00:00.0000000Z
reviewer: lindazqli
ms.reviewer: zhuoqunli
ms.custom: azure-ai-agents, dev-focus, pilot-ai-workflow-jan-2026, doc-kit-assisted
ai-usage: ai-assisted
zone_pivot_groups: selection-browser-tool
locale: en-us
document_id: 109d955c-c481-1456-c22b-bca982183ee8
document_version_independent_id: bd02d1c9-6ec5-2f8b-786e-632b0645a21b
original_content_git_url: https://github.com/MicrosoftDocs/azure-ai-docs-pr/blob/live/articles/foundry/agents/how-to/tools/browser-automation.md
site_name: Docs
depot_name: Learn.azure-ai
page_type: conceptual
toc_rel: ../../../toc.json
asset_id: foundry/agents/how-to/tools/browser-automation
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/foundry/agents/how-to/tools/browser-automation.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/43093068-2dda-408b-b3fe-dfd705c84f78
- https://authoring-docs-microsoft.poolparty.biz/devrel/64b65f6c-101f-411a-9b83-9f577fab52d0
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/7ad90213-4c78-4f1b-974b-eb153f3e6608
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/e453d60d-ba7e-43bc-8028-ec38e6b62512
- https://authoring-docs-microsoft.poolparty.biz/devrel/1a667fd1-8145-4b11-af0f-9f5de205a6e5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/b2f0d354-8384-469a-b9ff-8a0f80d66e6b
platformId: 56e49b87-e066-9ae8-6684-8c2261a9b726
---

# Automate browser tasks with Foundry agents - Microsoft Foundry | Microsoft Learn

The Browser Automation Tool (BAT) is **generally available in Microsoft Foundry**. It enables scalable, reliable browser-based automation within Foundry agents. It's available as an MCP tool powered by Playwright Workspaces as its headless browser infrastructure layer. It integrates seamlessly with modern agentic workflows while providing enterprise-grade security, observability, and extensibility.

By using the Browser Automation Tool, agents can interact with websites to navigate pages, extract and validate information, interact with page elements, complete forms, and perform multistep browser workflows.

Tip

Consider adding this tool using a [toolbox](/en-us/azure/foundry/agents/how-to/tools/toolbox). By using a toolbox, you are able to reuse the tool across agents and runtimes, as well as centralizing credential management, versioning, and policy enforcement through a managed MCP endpoint. See the [toolbox quickstart](/en-us/azure/foundry/agents/quickstarts/quickstart-toolbox-agent).

Browser Automation Tool (BAT) provides a comprehensive platform for browser automation through:

- [Playwright Workspaces](https://aka.ms/pww/docs) (a Generally Available service) as the infrastructure layer
- Real-time debugging with Live View
- Take control for human-in-the-loop scenarios
- Support for private website browsing (Public preview)
- Built-in observability for reliability and optimization
- Flexible orchestration layers

Important

The Browser Automation Tool controls web browsers on your behalf and can take unintended actions. Testing and monitoring are recommended. To learn more, see [Transparency Note for Foundry Agent Service - Microsoft Foundry](/en-us/azure/foundry/responsible-ai/agents/transparency-note).

## Use cases

Use **Browser Automation Tool** for browser-based workflows that require navigation, information extraction, form interaction, or validation across websites and business applications.

For example, a finance operations team can use an agent with **Browser Automation Tool** to retrieve invoice details from a vendor portal, validate the information against its internal system, and enter the required data into a legacy finance application. The agent can use the browser when these systems don't provide APIs or when the workflow spans multiple browser-based applications.

### Common scenarios

- **Form filling and third-party integration:** Complete forms and move information between browser-based applications when an API isn't available.
- **Web research and data extraction:** Navigate websites, filter results, and collect or compare information across sources.
- **Quality assurance and regression testing:** Validate end-to-end user flows, reproduce reported issues, and investigate failures in a real browser session.
- **Customer support and issue replication:** Re-create a customer journey, gather context from a website, and help support teams investigate browser-based issues.
- **Legacy-system automation:** Automate repetitive interactions with internal or vendor portals that don't provide modern APIs.
- **Employee and business operations:** Support supervised workflows such as employee-lifecycle tasks, invoice processing, and other browser-based operational processes.

## How it works

The Browser Automation tool enables a Foundry agent to interact with websites through a managed browser provided by Playwright Workspaces. Playwright Workspaces provides the cloud-hosted browser infrastructure, while the Browser Automation tool exposes browser capabilities that the agent can use to complete a user's task.

When a user gives the agent a browser-based task, the agent determines which browser operations are needed to make progress toward the requested goal. The agent can use the available browser automation tools to create and interact with a browser session, navigate to webpages, inspect page content, find and interact with elements, enter information, and complete multi-step browser workflows.

A typical browser automation flow works as follows:

1. The user provides a natural-language request, such as asking the agent to visit a website, find information, complete a form, or perform a sequence of browser interactions.
2. When browser interaction is required, the agent uses the Browser Automation tool connected to a Playwright Workspace. The workspace provides the managed, remote browser environment in which the task runs.
3. The browser automation service creates a browser session. The session is identified by a browser session ID that is used across subsequent browser operations so the agent can continue working in the same browser context.
4. Browser automation tools allow the agent to navigate pages and inspect the current page state. Based on the user's goal and the information available from the page, the agent determines the next browser operation to perform.
5. The agent can perform browser interactions such as navigating to another page, finding and selecting page elements, entering text, or interacting with controls. The resulting page state becomes available to subsequent browser operations.
6. For multi-step workflows, the agent repeats this observe-and-act process, using the same browser session as it moves through the website. This approach allows the agent to adapt its next action to the current state of the page instead of relying on a predefined sequence of browser steps.
7. After the workflow finishes, the browser session is closed and its associated browser resources are released.

Because the browser runs remotely in Playwright Workspaces, the agent doesn't need a locally installed browser or Playwright runtime to perform these interactions. Playwright Workspaces also provides capabilities for observing and troubleshooting browser sessions, including browser session data and Live View.

This architecture enables agents to perform workflows such as navigating websites, retrieving and validating information, completing forms, interacting with authenticated applications, and carrying out multi-step browser processes.

## List of tools

The Browser Automation Tool provides browser automation tools for managing browser sessions, navigating and inspecting webpages, interacting with elements, handling tabs and files, and capturing browser state.

In Microsoft Foundry, Browser Automation integrates through toolboxes and uses the Playwright Workspaces remote Model Context Protocol (MCP) server for managed browser execution. Enable only the tools required for your scenario.

For the complete list of tools, parameters, and usage guidance, see [Automate browsers with the Playwright Workspaces remote MCP server](/en-us/azure/app-testing/playwright-cloud-browsers/how-to-playwright-workspaces-remote-mcp#tool-reference).

## Regional support

To use the Browser Automation tool with hosted agents, you need a Playwright Workspace in a region that also supports hosted agents. Browser Automation is currently available in the following regions:

| Region | Status |
| --- | --- |
| `australiaeast` | Available |
| `eastasia` | Available |
| `eastus` | Available |
| `japaneast` | Available |
| `switzerlandnorth` | Available |
| `westeurope` | Available |
| `westus3` | Available |

## Choose your setup path

Choose the agent type and development approach before you configure **Browser Automation Tool**. All options use a Playwright workspace and a Browser Automation toolbox. The difference is where your agent logic runs and how much code you manage.

| Choose | Use this option when | Next step |
| --- | --- | --- |
| **Prompt agent** | You want the fastest path to a browser-enabled agent. Define instructions, a model, and tools in Foundry, and let Foundry run the agent. | Follow the Prompt agent sample. |
| **Prompt agent with GitHub Copilot harness** | You want a Prompt Agent with a Foundry-managed harness and isolated execution environment, without deploying or operating the harness code yourself. | See Use Browser Automation with the GitHub Copilot harness. |
| **Hosted agent with Microsoft Agent Framework** | You need custom agent code but want a recommended starting framework and Foundry-managed hosting, scaling, identity, and observability. | Follow the Hosted agent quickstart. Select **Agent Framework** when you create the sample. |
| **Hosted agent with your own framework** | You already use a framework such as LangGraph, OpenAI Agents SDK, Semantic Kernel, or custom code, and need to retain your existing orchestration logic. | Create a Hosted agent, then connect to the Browser Automation toolbox by using your framework's MCP client. |

## Prerequisites

Before you begin, make sure you have:

- An Azure subscription. [Create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- **Foundry User** role on the Foundry project for day-to-day agent development and use.

    Important

    The Foundry RBAC roles were recently renamed. **Foundry User**, **Foundry Owner**, **Foundry Account Owner**, and **Foundry Project Manager** were previously named Azure AI User, Azure AI Owner, Azure AI Account Owner, and Azure AI Project Manager. You might still see the previous names in some places while the rename rolls out. The role IDs and core permissions are unchanged by the rename.
- **Foundry Project Manager** role on the Foundry project if you create the project connection.
- **Contributor** role on the target resource group only while you create the Playwright workspace. This role is required for resource provisioning. Activate it just in time through Microsoft Entra Privileged Identity Management (PIM), and deactivate it after provisioning. Day-to-day agent developers and runtime users don't need this role.
- A Foundry project with a configured endpoint.
- An AI model deployed in your project (for example, `gpt-5.4`). Confirm that both the model and project region support Browser Automation in [Tool support by region and model](../../concepts/limits-quotas-regions#tool-support-by-region-and-model).
- A Playwright workspace resource.
- A project connection set up for your Playwright workspace.

### SDK requirements

For Python examples, install the required packages:

```bash
pip install "azure-ai-projects>=2.8.0" python-dotenv
```

The .NET SDK is currently in preview. For more information, see the [quickstart](../../../quickstarts/get-started-code).

### Configuration

**Get your project endpoint**: Open your project in the [Foundry portal](https://ai.azure.com), and copy the endpoint from the project overview page. The format is `https://{account-name}.services.ai.azure.com/api/projects/{project-name}`.

**Connection ID format**: Use `/subscriptions/{{subscriptionID}}/resourceGroups/{{resourceGroupName}}/providers/Microsoft.CognitiveServices/accounts/{{foundryAccountName}}/projects/{{foundryProjectName}}/connections/{{foundryConnectionName}}`. You can find this value on the tool's details page after you connect the Browser Automation tool.

## Usage support

The following table shows SDK and setup support.

| Microsoft Foundry support | Python SDK | C# SDK | JavaScript SDK | Java SDK | REST API | Basic agent setup | Standard agent setup |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ | ✔️ |

## Choose an authentication type

When you create the Browser Automation connection, select the authentication method that meets your organization's security requirements.

| Authentication type | Use when | Considerations |
| --- | --- | --- |
| **API key** | You are prototyping or your organization permits service access tokens. | The key is stored in the Foundry project connection. Don't place it in source code, prompts, or logs. Rotate and revoke it according to your organization's policy. |
| **Project managed identity** | Multiple agents in the same Foundry project need to access the same Playwright workspace. | Use the Foundry project's Microsoft Entra identity and grant it only the required permissions on the workspace. This identity is the recommended default for enterprise workloads when supported by the connection. |
| **Agent identity** | A deployed Hosted agent needs its own access boundary for browser automation or downstream resources. | A Hosted agent receives a dedicated Microsoft Entra identity when it is deployed. Assign permissions to that identity when the agent requires access that shouldn't be shared with other agents in the project. |

## Set up Browser Automation

### Create a Playwright workspace

1. In the [Azure portal](https://portal.azure.com), create a [Playwright Workspace](https://aka.ms/pww/docs/manage-workspaces) resource.
2. After the workspace is created, go to **Settings** &gt; **Access Management**.

If you selected **API token** as the authentication type:

1. Confirm the **Playwright Service Access Token** authentication method is enabled.
2. Select **Generate Token**, enter a name (for example, `foundry-connection`), and choose an expiry period.
3. **Copy the token immediately**. You can't view it again after closing the page.
4. Store the token only in the Foundry project connection. Don't put it in source code, prompts, or application logs. Rotate it before it expires, and revoke it immediately if it is exposed.

On the workspace **Overview** page, copy the **Browser endpoint** (it starts with `wss://`). Next, grant the Foundry project managed identity access to the Playwright workspace.

### Grant Playwright workspace access

Browser Automation Tool uses the **Foundry project managed identity** to access the Playwright workspace. This identity is different from a hosted agent's dedicated agent identity:

- **Project managed identity:** Project-wide identity used by Foundry platform services and Browser Automation connections.
- **Agent identity:** Per-agent identity created when you deploy a hosted agent. Use it for the agent's runtime access to downstream resources.

Grant the project managed identity the minimum permissions required to use the Playwright workspace:

1. In the Azure portal, open the Playwright workspace.
2. Select **Access control (IAM)**, and then select **Add** &gt; **Add role assignment**.
3. Select a custom role that contains only the Playwright permissions required by the Foundry project identity. If a custom role isn't available, assign **Playwright Workspace Contributor** at the **Playwright workspace resource scope**.
4. On the **Members** tab, select the Foundry project managed identity.
5. Select **Review + assign**.

### Connect the Browser Automation tool in Foundry

1. Go to the [Foundry portal](https://ai.azure.com/nextgen) and select your project.
2. Select **Build** &gt; **Tools**.
3. Select **Create a toolbox**.
4. Fill in the **Name** and **Description** for your toolbox.
5. Under **Tools**, click on **Add**
6. Select **Browser Automation** and click **Add tool**
7. Enter the required fields
    - **Connection name**: Unique name for your connection
    - **Playwright Workspace**: Select the Playwright Workspace resource.
    - **Auth Type**: Select the authentication type for your connection.
8. Select **Connect**.
9. Click on **Publish** to save the toolbox

After the toolbox is created, you can view the **Project connection ID** on the tool's details page. Use this value as the browser automation connection ID in your code.

### Use Browser Automation with the GitHub Copilot harness

 The GitHub Copilot harness is a harness option for Prompt Agents. You create a Prompt Agent and invoke it through the Responses API, while Microsoft Foundry operates the harness and its isolated execution environment. Use this option when you want Foundry to manage the harness infrastructure for your Prompt Agent while giving the agent access to Browser Automation Tool. To use Browser Automation Tool with the GitHub Copilot harness: 

1. Create a Prompt Agent and select the GitHub Copilot harness.
2. Create or use an existing Playwright workspace and configure the Browser Automation connection.
3. Add Browser Automation Tool to the agent through a toolbox.
4. Save the agent configuration and start a new chat session.
5. Give the agent a browser-based task and verify that it uses Browser Automation Tool to complete the task. For example, you can ask the agent to navigate to a website, find specific information, interact with page elements, or complete a multistep browser workflow.

### Add browser automation to a toolbox with the Azure Developer CLI

To add browser automation to a Toolbox, use the Azure Developer CLI to create a Playwrite workspace. *This article assumes you already have a Playwright workspace resource. See the prerequisites section.*

1. Create the Playwright Workspace connection.

```bash
azd ai connection create my-browser-conn \
  --kind PlaywrightWorkspace \
  --target wss://your-browser-endpoint.api.playwright.microsoft.com/playwrightworkspaces/browsers \
  --auth-type api-key \
  --key "<playwright-workspaces-access-token>"
```

`--kind PlaywrightWorkspace` requires exact PascalCase.

1. Define the toolbox (my-toolbox.yaml)

```yaml
description: Browser Automation toolbox
tools:
  - type: browser_automation
    project_connection_id: my-browser-conn
```

1. Create the toolbox

```bash
azd ai toolbox create my-toolbox --from-file my-toolbox.yaml
```

## Browser Automation tool definitions

After you run a sample, verify the tool was called by using tracing in Microsoft Foundry. For guidance on validating tool invocation, see [Best practices for using tools in Microsoft Foundry Agent Service](../../concepts/tool-best-practice).

Note

- The .NET SDK is currently in preview. For more information, see the [quickstart](../../../quickstarts/get-started-code).

```csharp
ProjectsAgentTool tool = new BrowserAutomationTool(
    new BrowserAutomationToolOptions(
        new BrowserAutomationToolConnectionParameters("<BROWSER_AUTOMATION_PROJECT_CONNECTION_ID>")
    )
);
```

```javascript
const tools = [
  {
    type: "browser_automation",
    name: "<OPTIONAL_TOOL_NAME>",
    description: "<Optional description for the model>",
    browser_automation: {
      connection: {
          project_connection_id: "<BROWSER_AUTOMATION_PROJECT_CONNECTION_ID>"
      }
    }
  },
];
```

::: zone pivot="python"

## Use Browser Automation Tool with agents example

The following Python example demonstrates how to create an AI agent with browser automation capabilities. Select **Prompt Agents** to use the Azure AI Projects SDK to create a server-side prompt agent, or **Hosted Agents** to use the Agent Framework [`FoundryChatClient`](../../quickstarts/responses-api) to build an ephemeral, in-process agent.

### Prompt agents

```python
import os
import json
from dotenv import load_dotenv
from util import create_version_with_endpoint
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import (
    PromptAgentDefinition,
    BrowserAutomationTool,
    BrowserAutomationToolParameters,
    BrowserAutomationToolConnectionParameters,
)

load_dotenv()

endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
agent_name = os.environ.get("FOUNDRY_AGENT_NAME") or "MyAgent"

tool = BrowserAutomationTool(
    browser_automation=BrowserAutomationToolParameters(
        connection=BrowserAutomationToolConnectionParameters(
            project_connection_id=os.environ["BROWSER_AUTOMATION_PROJECT_CONNECTION_ID"],
        )
    )
)

with (
    DefaultAzureCredential() as credential,
    AIProjectClient(endpoint=endpoint, credential=credential) as project_client,
    create_version_with_endpoint(
        project_client=project_client,
        agent_name=agent_name,
        definition=PromptAgentDefinition(
            model=os.environ["FOUNDRY_MODEL_NAME"],
            instructions="""You are an Agent helping with browser automation tasks.
        You can answer questions, provide information, and assist with various tasks
        related to web browsing using the Browser Automation tool available to you.""",
            tools=[tool],
        ),
    ),
    project_client.get_openai_client(agent_name=agent_name) as openai_client,
):
    stream_response = openai_client.responses.create(
        stream=True,
        input="""
        Use the Browser Automation tool to visit https://example.com.
        Read the page and report its title and the visible description paragraph.
        Base your answer on the browser results, not on prior knowledge.""",
    )

    for event in stream_response:
        if event.type == "response.created":
            print(f"Response created with ID: {event.response.id}")
        elif event.type == "response.output_item.done":
            item = event.item
            # Each browser action (navigate, click, type, ...) is surfaced as a "remote_function_call" item.
            if item.type == "remote_function_call":
                arguments = json.loads(getattr(item, "arguments", None) or "{}")
                arguments.pop("browserSessionId", None)
                print(f"Browser action: {item.name} (call ID: {item.call_id}), arguments: {arguments}")
        elif event.type == "response.output_text.done":
            # Includes the live view URL message as well as the final answer.
            print(f"\nAgent message: {event.text}")
        elif event.type == "response.completed":
            print("\nResponse completed!")
```

### What this code does

This example creates an agent version with the Browser Automation tool enabled and sends a request that requires the agent to interact with a webpage. The example streams the response and reports browser actions as they occur.

At the start of the run, the agent provides a Live View URL that you can use to observe the browser session. Treat this URL as sensitive and don't share it.

### Required inputs

Set the following environment variables before running the sample:

- `FOUNDRY_PROJECT_ENDPOINT`: Your Microsoft Foundry project endpoint.
- `FOUNDRY_MODEL_NAME`: The deployment name of the AI model in your Foundry project.
- `BROWSER_AUTOMATION_PROJECT_CONNECTION_ID`: The Browser Automation project connection ID.
- `FOUNDRY_AGENT_NAME`: Optional. The name of the agent. If you don't specify a value, the sample uses `MyAgent`.

See Configuration for details.

### Expected output

When you run the sample, you see streaming updates as the agent completes the browser task. The output can include:

- The response ID.
- A Live View URL for observing the browser session.
- Browser actions performed by the agent.
- The agent's final response.
- A message indicating that the response completed.

The exact output varies based on the website content and model behavior.

### Hosted agents

This sample uses [`FoundryChatClient`](../../quickstarts/responses-api) from the Microsoft Agent Framework to create the `browser-automation-toolbox` and connect to its MCP endpoint with `FoundryToolbox`. Install the packages with `pip install agent-framework-foundry azure-ai-projects`, replace `PROJECT_ENDPOINT` and `BROWSER_CONNECTION_ID` with your project values, and sign in with `az login`. For the complete hosted-agent toolbox pattern, see the [full sample](https://aka.ms/foundry-toolbox-maf).

```python
import asyncio

from agent_framework import Agent
from agent_framework.foundry import FoundryChatClient, FoundryToolbox
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import (
  BrowserAutomationToolboxTool,
    BrowserAutomationToolParameters,
    BrowserAutomationToolConnectionParameters,
)
from azure.identity import AzureCliCredential

PROJECT_ENDPOINT = "https://<account>.services.ai.azure.com/api/projects/<project>"
BROWSER_CONNECTION_ID = "your-browser-automation-connection-id"

async def main() -> None:
    credential = AzureCliCredential()

    # 1. Add the Browser Automation tool to a toolbox. Using a toolbox is the recommended way
    #    to give agents tools: you curate tools once and reuse the toolbox across agents.
    #    See /azure/foundry/agents/concepts/toolbox-overview
    project = AIProjectClient(endpoint=PROJECT_ENDPOINT, credential=credential)
    tool = BrowserAutomationToolboxTool(
        browser_automation=BrowserAutomationToolParameters(
            connection=BrowserAutomationToolConnectionParameters(
                project_connection_id=BROWSER_CONNECTION_ID,
            )
        )
    )
    toolbox = project.toolboxes.create_version(
        name="browser-automation-toolbox",
        description="Toolbox with the Browser Automation tool",
        tools=[tool],
    )

    # 2. The toolbox exposes an MCP-compatible endpoint.
    TOOLBOX_MCP_URL = (
        f"{PROJECT_ENDPOINT}/toolboxes/{toolbox.name}"
        f"/versions/{toolbox.version}/mcp?api-version=v1"
    )

    # 3. Attach the toolbox to the hosted agent as an MCP tool.
    toolbox_tool = FoundryToolbox(credential, url=TOOLBOX_MCP_URL)

    agent = Agent(
        client=FoundryChatClient(credential=credential),
        instructions=(
            "You help with browser automation tasks. Use the Browser Automation tool "
            "to navigate and read information from websites."
        ),
        tools=[toolbox_tool],
    )

    result = await agent.run(
        "Go to finance.yahoo.com, search for MSFT, click 'YTD' on the price chart, "
        "and report the year-to-date percent change."
    )
    print(f"Agent: {result.text}")

if __name__ == "__main__":
    asyncio.run(main())
```

### Expected output

The agent navigates the live website through the Browser Automation tool in the toolbox and reports the YTD value it observes. Output varies based on website content:

```console
Agent: The year-to-date change for MSFT is approximately +18.4%.
```

For the complete hosted-agent toolbox pattern, see the [full sample](https://aka.ms/foundry-toolbox-maf).

::: zone-end

::: zone pivot="csharp"

## Use Browser Automation Tool with agents example

Before running this sample, complete the setup steps in Set up Browser Automation.

The following C# example demonstrates how to create an AI agent with Browser Automation capabilities. Select **Prompt Agents** to use the Azure AI Projects SDK to create a server-side prompt agent, or **Hosted Agents** to use the Microsoft Agent Framework to build an ephemeral, in-process agent.

### Prompt agents

This example uses synchronous methods of the Azure AI Projects client library. For an example that uses asynchronous methods, see the [Sample for use of BrowserAutomationTool and Agents](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/ai/Azure.AI.Extensions.OpenAI/samples/Sample23_BrowserAutomationTool.md) sample in the Azure SDK for .NET repository on GitHub.

```csharp
using System;
using System.Threading.Tasks;
using Azure.AI.Projects;
using Azure.AI.Projects.Agents;
using Azure.Identity;
using Microsoft.ClientModel.TestFramework;
using NUnit.Framework;
using OpenAI.Responses;

namespace Azure.AI.Extensions.OpenAI.Tests.Samples;

public class Sample_BrowserAutomotion : ProjectsOpenAITestBase
{
    private AIProjectClient _projectClient;
    private ProjectsAgentVersion _agentVersion;

    #region Snippet:Sample_ParseResponse_BrowserAutomotion
    private static void ParseResponse(StreamingResponseUpdate streamResponse)
    {
        if (streamResponse is StreamingResponseCreatedUpdate createUpdate)
        {
            Console.WriteLine($"Stream response created with ID: {createUpdate.Response.Id}");
        }
        else if (streamResponse is StreamingResponseOutputTextDoneUpdate textDoneUpdate)
        {
            Console.WriteLine($"Response done with full message: {textDoneUpdate.Text}");
        }
        else if (streamResponse is StreamingResponseErrorUpdate errorUpdate)
        {
            throw new InvalidOperationException($"The stream has failed: {errorUpdate.Message}, error code: {errorUpdate.Code}");
        }
        else if (streamResponse is StreamingResponseFailedUpdate failedUpdate)
        {
            throw new InvalidOperationException($"The response has failed: {failedUpdate.Response.Error?.Message}, error code: {failedUpdate.Response.Error?.Code}");
        }
        else if (streamResponse is StreamingResponseIncompleteUpdate incompleteUpdate)
        {
            throw new InvalidOperationException($"The response is incomplete: {incompleteUpdate.Response.Id}");
        }
    }
    #endregion

    [Test]
    [AsyncOnly]
    public async Task BrowserAutomotionAsync()
    {
        IgnoreSampleMayBe();
        #region Snippet:Sample_CreateProjectClient_BrowserAutomotion
#if SNIPPET
        var projectEndpoint = System.Environment.GetEnvironmentVariable("FOUNDRY_PROJECT_ENDPOINT");
        var modelDeploymentName = System.Environment.GetEnvironmentVariable("FOUNDRY_MODEL_NAME");
        var playwrightConnectionId = System.Environment.GetEnvironmentVariable("BROWSER_AUTOMATION_PROJECT_CONNECTION_ID");
#else
        var projectEndpoint = TestEnvironment.FOUNDRY_PROJECT_ENDPOINT;
        var modelDeploymentName = TestEnvironment.FOUNDRY_MODEL_NAME;
        var playwrightConnectionId = TestEnvironment.BROWSER_AUTOMATION_PROJECT_CONNECTION_ID;
#endif
        AIProjectClientOptions options = new()
        {
            NetworkTimeout = TimeSpan.FromMinutes(5)
        };
        AIProjectClient projectClient = new(endpoint: new Uri(projectEndpoint), tokenProvider: new DefaultAzureCredential(), options: options);

        #endregion
        #region Snippet:Sample_CreateAgent_BrowserAutomotion_Async
        BrowserAutomationTool playwrightTool = new(
            new BrowserAutomationToolOptions(
                new BrowserAutomationToolConnectionOptions(playwrightConnectionId)
            ));

        DeclarativeAgentDefinition agentDefinition = new(model: modelDeploymentName)
        {
            Instructions = "You are an Agent helping with browser automation tasks.\n" +
            "You can answer questions, provide information, and assist with various tasks\n" +
            "related to web browsing using the Browser Automation tool available to you.",
            Tools = { playwrightTool }
        };
        ProjectsAgentVersion agentVersion = await projectClient.AgentAdministrationClient.CreateAgentVersionAsync(
            agentName: "myAgent",
            options: new(agentDefinition));
        #endregion
        _projectClient = projectClient;
        _agentVersion = agentVersion;
        #region Snippet:Sample_CreateResponse_BrowserAutomotion_Async
        ProjectResponsesClient responseClient = projectClient.ProjectOpenAIClient.GetProjectResponsesClientForAgent(
            new AgentReference(agentVersion.Name, agentVersion.Version));
        CreateResponseOptions responseOptions = new()
        {
            ToolChoice = ResponseToolChoice.CreateRequiredChoice(),
            StreamingEnabled = true,
            InputItems =
            {
                ResponseItem.CreateUserMessageItem("Use the Browser Automation tool to visit https://finance.yahoo.com/quote/MSFT/performance/. " +
                    "Read the YTD return shown on the page for Microsoft (MSFT) and report the percentage with its label. " +
                    "Use the visible page content, not prior knowledge. Do not use the search bar or interact with charts. " +
                    "If the value is unavailable or access is blocked, say so rather than guessing.")
            }
        };
        await foreach (StreamingResponseUpdate update in responseClient.CreateResponseStreamingAsync(responseOptions))
        {
            ParseResponse(update);
        }
        #endregion
    }

    [Test]
    [SyncOnly]
    public void BrowserAutomotion()
    {
        IgnoreSampleMayBe();
#if SNIPPET
        var projectEndpoint = System.Environment.GetEnvironmentVariable("FOUNDRY_PROJECT_ENDPOINT");
        var modelDeploymentName = System.Environment.GetEnvironmentVariable("FOUNDRY_MODEL_NAME");
        var playwrightConnectionId = System.Environment.GetEnvironmentVariable("BROWSER_AUTOMATION_PROJECT_CONNECTION_ID");
#else
        var projectEndpoint = TestEnvironment.FOUNDRY_PROJECT_ENDPOINT;
        var modelDeploymentName = TestEnvironment.FOUNDRY_MODEL_NAME;
        var playwrightConnectionId = TestEnvironment.BROWSER_AUTOMATION_PROJECT_CONNECTION_ID;
#endif
        AIProjectClientOptions options = new()
        {
            NetworkTimeout = TimeSpan.FromMinutes(5)
        };
        AIProjectClient projectClient = new(endpoint: new Uri(projectEndpoint), tokenProvider: new DefaultAzureCredential(), options: options);
        #region Snippet:Sample_CreateAgent_BrowserAutomotion_Sync
        BrowserAutomationTool playwrightTool = new(
            new BrowserAutomationToolOptions(
                new BrowserAutomationToolConnectionOptions(playwrightConnectionId)
            ));

        DeclarativeAgentDefinition agentDefinition = new(model: modelDeploymentName)
        {
            Instructions = "You are an Agent helping with browser automation tasks.\n" +
            "You can answer questions, provide information, and assist with various tasks\n" +
            "related to web browsing using the Browser Automation tool available to you.",
            Tools = { playwrightTool }
        };
        ProjectsAgentVersion agentVersion = projectClient.AgentAdministrationClient.CreateAgentVersion(
            agentName: "myAgent",
            options: new(agentDefinition));
        #endregion
        _projectClient = projectClient;
        _agentVersion = agentVersion;
        #region Snippet:Sample_CreateResponse_BrowserAutomotion_Sync
        ProjectResponsesClient responseClient = projectClient.ProjectOpenAIClient.GetProjectResponsesClientForAgent(
            new AgentReference(agentVersion.Name, agentVersion.Version));
        CreateResponseOptions responseOptions = new()
        {
            ToolChoice = ResponseToolChoice.CreateRequiredChoice(),
            StreamingEnabled = true,
            InputItems =
            {
                ResponseItem.CreateUserMessageItem("Use the Browser Automation tool to visit https://finance.yahoo.com/quote/MSFT/performance/. " +
                    "Read the YTD return shown on the page for Microsoft (MSFT) and report the percentage with its label. " +
                    "Use the visible page content, not prior knowledge. Do not use the search bar or interact with charts. " +
                    "If the value is unavailable or access is blocked, say so rather than guessing.")
            }
        };
        foreach (StreamingResponseUpdate update in responseClient.CreateResponseStreaming(responseOptions))
        {
            ParseResponse(update);
        }
        #endregion
    }

    [TearDown]
    public override void Cleanup()
    {
        if (_agentVersion is not null)
        {
            _projectClient.AgentAdministrationClient.DeleteAgentVersion(
                agentName: _agentVersion.Name, agentVersion: _agentVersion.Version);
            _agentVersion = null;
        }
        base.Cleanup();
    }

    public Sample_BrowserAutomotion(bool isAsync) : base(isAsync)
    { }
}
```

### What this code does

This example creates a Foundry agent with the Browser Automation tool, sends it a browser-based task, and streams the response. The agent uses the configured Browser Automation project connection to interact with the target website and return the requested information.

### Required inputs

- A Foundry project endpoint and model deployment name. See Configuration for details.
- A Browser Automation project connection ID (`BROWSER_AUTOMATION_PROJECT_CONNECTION_ID`).
- A Playwright connection created in your Foundry project.

### Expected output

You see streaming progress messages, such as text deltas, and a completed response. The output varies based on the website content and model behavior.

### Hosted agents

This sample creates the Browser Automation toolbox with the Azure AI Projects SDK, and then uses the Microsoft Agent Framework `AddFoundryToolboxes` integration to make the tool available to the hosted agent. Install the Agent Framework packages, set the `AZURE_AI_PROJECT_ENDPOINT`, `AZURE_AI_MODEL_DEPLOYMENT_NAME`, and `BROWSER_AUTOMATION_CONNECTION_ID` environment variables, and sign in with `az login`.

```csharp
using System.IO;
using System.Runtime.CompilerServices;
using Azure.AI.AgentServer.Responses;
using Azure.AI.AgentServer.Responses.Models;
using Azure.AI.OpenAI;
using Azure.AI.Projects;
using Azure.AI.Extensions.OpenAI;
using Azure.Identity;
using Microsoft.Agents.AI;
using Microsoft.Agents.AI.Foundry.Hosting;
using Microsoft.Extensions.DependencyInjection;
using OpenAI.Chat;

string projectEndpoint = Environment.GetEnvironmentVariable("AZURE_AI_PROJECT_ENDPOINT")
    ?? "https://<account>.services.ai.azure.com/api/projects/<project>";
string deploymentName = Environment.GetEnvironmentVariable("AZURE_AI_MODEL_DEPLOYMENT_NAME") ?? "gpt-5-mini";
string browserConnectionId = Environment.GetEnvironmentVariable("BROWSER_AUTOMATION_CONNECTION_ID")
    ?? "your-browser-automation-connection-id";

var openAiEndpoint = new Uri(projectEndpoint).GetLeftPart(UriPartial.Authority);
DefaultAzureCredential credential = new();

// 1. Create the Browser Automation tool and add it to a toolbox. Using a toolbox is the
//    recommended way to give agents tools. See /azure/foundry/agents/concepts/toolbox-overview
AIProjectClient projectClient = new(endpoint: new Uri(projectEndpoint), tokenProvider: credential);
ProjectsAgentTool browserTool = new BrowserAutomationTool(
    new BrowserAutomationToolParameters(
        new BrowserAutomationToolConnectionParameters(browserConnectionId)
    ));
ToolboxVersion toolboxVersion = projectClient.AgentAdministrationClient
    .GetAgentToolboxes().CreateToolboxVersion(
        toolboxName: "browser-automation-toolbox",
        tools: [browserTool],
        description: "Toolbox with the Browser Automation tool");

// Create the hosted agent and register the toolbox integration.
AIAgent agent = projectClient.AsAIAgent(
    model: deploymentName,
    instructions: "You are a helpful assistant with access to the toolbox tools.",
    name: "hosted-toolbox-agent");

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddFoundryResponses(agent);
builder.Services.AddFoundryToolboxes(credential, toolboxVersion.Name);

var app = builder.Build();
app.MapFoundryResponses();
app.Run();
```

### Expected output

The hosted agent connects to the Browser Automation tool through the toolbox MCP endpoint and uses the browser to complete the requested web task. Output varies based on website content and model behavior:

```console
Agent: The year-to-date change for MSFT is approximately +18.4%.
```

For the complete hosted-agent toolbox pattern, see the [full sample](https://aka.ms/foundry-toolbox-maf).

::: zone-end

::: zone pivot="rest"

Get an access token:

```bash
AGENT_TOKEN=$(az account get-access-token --scope https://ai.azure.com/.default --query accessToken -o tsv)
```

This access token is short-lived. Keep it only in the current shell or process. Never commit, store, print, or log it. Run the command again after it expires. SDK flows use `DefaultAzureCredential` where supported, but these REST requests require the bearer token.

The recommended way to add Browser Automation is through a toolbox, then attach the toolbox to your agent as an MCP tool. See [What is a toolbox?](../../concepts/toolbox-overview)

1. Create a toolbox that contains the Browser Automation tool:

```bash
curl --request POST \
  --url "$FOUNDRY_PROJECT_ENDPOINT/toolboxes/browser-automation-toolbox/versions?api-version=v1" \
  -H "Authorization: Bearer $AGENT_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{
    "description": "Toolbox with the Browser Automation tool",
    "tools": [
      {
        "type": "browser_automation",
        "browser_automation": {
          "connection": {
            "project_connection_id": "'"$BROWSER_AUTOMATION_PROJECT_CONNECTION_ID"'"
          }
        }
      }
    ]
  }'
```

The toolbox exposes an MCP-compatible endpoint at `$FOUNDRY_PROJECT_ENDPOINT/toolboxes/browser-automation-toolbox/versions/<version>/mcp?api-version=v1`, where `<version>` is the version returned by the previous call.

1. Create a remote-tool project connection that points at the toolbox endpoint, using a user Entra token so the caller's identity is passed through (audience `https://ai.azure.com`).

```bash
azd ai connection create browser-automation-toolbox-conn \
  --kind remote-tool \
  --target "$FOUNDRY_PROJECT_ENDPOINT/toolboxes/browser-automation-toolbox/versions/<version>/mcp?api-version=v1" \
  --auth-type user-entra-token \
  --audience https://ai.azure.com
```

1. Create a response that uses the toolbox by attaching it as an MCP tool.

```bash
curl --request POST \
  --url "${FOUNDRY_PROJECT_ENDPOINT}/openai/v1/responses" \
  --header "Authorization: Bearer ${AGENT_TOKEN}" \
  --header "Content-Type: application/json" \
  --header "User-Agent: insomnia/11.6.1" \
  --data @- <<JSON
{
  "model": "${FOUNDRY_MODEL_DEPLOYMENT_NAME}",
  "input": [
    {
      "role": "user",
      "content": [
        {
          "type": "input_text",
          "text": "Your goal is to report the percent of Microsoft year-to-date stock price change."
        },
        {
          "type": "input_text",
          "text": "Go to finance.yahoo.com, search for MSFT, select YTD on the chart, and report the percent value shown."
        }
      ]
    }
  ],
  "tools": [
    {
      "type": "mcp",
      "server_label": "toolbox",
      "server_url": "${FOUNDRY_PROJECT_ENDPOINT}/toolboxes/browser-automation-toolbox/versions/<version>/mcp?api-version=v1",
      "require_approval": "never",
      "project_connection_id": "browser-automation-toolbox-conn"
    }
  ]
}
JSON
```

::: zone-end

::: zone pivot="typescript"

## Use Browser Automation tool with agents example

The following TypeScript sample demonstrates how to create an agent with the Browser Automation tool, perform web browsing tasks, and process streaming responses with browser automation events. For a JavaScript version of this sample, see the [JavaScript sample for Browser Automation tool](https://github.com/Azure/azure-sdk-for-js/blob/main/sdk/ai/ai-projects/samples/v2/javascript/agents/tools/agentBrowserAutomation.js) in the Azure SDK for JavaScript repository on GitHub.

In `@azure/ai-projects` 2.8.0, `BrowserAutomationTool` and `BrowserAutomationToolboxTool` use the `browser_automation` discriminator and nested property. For implementation details, see the [released Browser Automation agent sample](https://github.com/Azure/azure-sdk-for-js/blob/%40azure%2Fai-projects_2.8.0/sdk/ai/ai-projects/samples-dev/agents/tools/agentBrowserAutomationGA.ts).

```typescript
import { DefaultAzureCredential } from "@azure/identity";
import { AIProjectClient } from "@azure/ai-projects";

// Format: "https://resource_name.ai.azure.com/api/projects/project_name"
const PROJECT_ENDPOINT = "your_project_endpoint";
const BROWSER_CONNECTION_ID = "your-browser-automation-connection-id";

const handleBrowserCall = (item: any) => {
  // TODO: support browser_automation_preview_call schema
  const callId = item.call_id;
  const argumentsStr = item.arguments;

  // Parse the arguments string into a dictionary
  let query = null;
  if (argumentsStr && typeof argumentsStr === "string") {
    try {
      const argumentsObj = JSON.parse(argumentsStr);
      query = argumentsObj.query;
    } catch (e) {
      console.error("Failed to parse arguments:", e);
    }
  }

  console.log(`Call ID: ${callId ?? "None"}`);
  console.log(`Query arguments: ${query ?? "None"}`);
};

export async function main(): Promise<void> {
  // Create clients to call Foundry API
  const project = new AIProjectClient(PROJECT_ENDPOINT, new DefaultAzureCredential());
  const openai = project.getOpenAIClient();

  console.log("Creating a toolbox with the Browser Automation tool...");

  // 1. Add the Browser Automation tool to a toolbox. Using a toolbox is the recommended
  //    way to give agents tools. See /azure/foundry/agents/concepts/toolbox-overview
  const toolbox = await project.toolboxes.createVersion(
    "browser-automation-toolbox",
    [
      {
        type: "browser_automation",
        browser_automation: {
          connection: {
            project_connection_id: BROWSER_CONNECTION_ID,
          },
        },
      },
    ],
    { description: "Toolbox with the Browser Automation tool" },
  );

  // 2. The toolbox exposes an MCP-compatible endpoint.
  const toolboxMcpUrl =
    `${PROJECT_ENDPOINT}/toolboxes/${toolbox.name}` +
    `/versions/${toolbox.version}/mcp?api-version=v1`;

  // 3. Create a remote-tool project connection that points at the toolbox endpoint.
  //    Use a user Entra token so the caller's identity is passed through
  //    (audience https://ai.azure.com). Create the connection once, for example
  //    with the Azure Developer CLI:
  //
  //    azd ai connection create browser-automation-toolbox-conn \
  //      --kind remote-tool \
  //      --target "<toolboxMcpUrl>" \
  //      --auth-type user-entra-token \
  //      --audience https://ai.azure.com
  const toolboxConnectionName = "browser-automation-toolbox-conn";

  // 4. Attach the toolbox to a prompt agent as an MCP tool.
  const agent = await project.agents.createVersion("MyAgent", {
    kind: "prompt",
    model: "gpt-4.1-mini",
    instructions: `You are an Agent helping with browser automation tasks. 
            You can answer questions, provide information, and assist with various tasks 
            related to web browsing using the Browser Automation tool available to you.`,
    tools: [
      {
        type: "mcp",
        server_label: "toolbox",
        server_url: toolboxMcpUrl,
        require_approval: "never",
        project_connection_id: toolboxConnectionName,
      },
    ],
  });
  console.log(`Agent created (id: ${agent.id}, name: ${agent.name}, version: ${agent.version})`);

  console.log("\nSending browser automation request with streaming...");
  const streamResponse = await openai.responses.create(
    {
      input: `Your goal is to report the percent of Microsoft year-to-date stock price change.
            To do that, go to the website finance.yahoo.com.
            At the top of the page, you will find a search bar.
            Enter the value 'MSFT', to get information about the Microsoft stock price.
            At the top of the resulting page you will see a default chart of Microsoft stock price.
            Click on 'YTD' at the top of that chart, and report the percent value that shows up just below it.`,
      stream: true,
    },
    {
      body: {
        agent_reference: { name: agent.name, type: "agent_reference" },
        tool_choice: "required",
      },
    },
  );

  // Process the streaming response
  for await (const event of streamResponse) {
    if (event.type === "response.created") {
      console.log(`Follow-up response created with ID: ${event.response.id}`);
    } else if (event.type === "response.output_text.delta") {
      process.stdout.write(event.delta);
    } else if (event.type === "response.output_text.done") {
      console.log("\n\nFollow-up response done!");
    } else if (
      event.type === "response.output_item.done" ||
      event.type === "response.output_item.added"
    ) {
      const item = event.item as any;
      if (item.type === "browser_automation_preview_call") {
        handleBrowserCall(item);
      }
    } else if (event.type === "response.completed") {
      console.log("\nFollow-up completed!");
    }
  }

  // Clean up resources by deleting the agent version
  // This prevents accumulation of unused resources in your project
  console.log("\nCleaning up resources...");
  await project.agents.deleteVersion(agent.name, agent.version);
  console.log("Agent deleted");

  console.log("\nBrowser Automation sample completed!");
}

main().catch((err) => {
  console.error("The sample encountered an error:", err);
});
```

### What this code does

This example creates an agent version with the Browser Automation tool enabled, sends a prompt that requires tool usage, and processes streaming events, including browser automation call events, as they arrive.

### Required inputs

- A Foundry project endpoint and a browser automation connection ID. See Configuration for details.

### Expected output

You see an "Agent created ..." message, streaming text output, and optionally, browser call details when the tool is invoked. The output varies based on the website content and model behavior.

::: zone-end

::: zone pivot="java"

## Use browser automation in a Java agent

Update these values in your Java agent after you create the toolbox:

- `projectEndpoint` — Your project endpoint.
- `toolboxMcpUrl` — The MCP endpoint for the toolbox version that contains the Browser Automation tool.
- `toolboxConnectionName` — The remote-tool project connection name for the toolbox endpoint.

Add the dependency to your `pom.xml`:

```xml
<dependency>
    <groupId>com.azure</groupId>
    <artifactId>azure-ai-agents</artifactId>
    <version>2.4.0</version>
</dependency>
```

Tip

**Recommended:** For most agents, add the Browser Automation tool through a [toolbox](../../concepts/toolbox-overview) and attach the toolbox to your agent as an MCP tool. The Java SDK doesn't yet expose a toolbox creation API, so create the toolbox by using the [Python](?pivots=python), [REST API](?pivots=rest), [C#](?pivots=csharp), or [TypeScript](?pivots=typescript) example, or the [Foundry portal](toolbox), and then reference its MCP endpoint from your Java agent as an `McpTool`.

::: zone-end

## Monitor browser automation sessions

Browser Automation Tool provides observability features to help you validate, troubleshoot, and review browser-based agent runs.

- **Live View:** Provides a real-time view of an active browser session. Use it during development and testing to verify navigation, page state, and browser interactions as the agent runs.
- **Screenshot recording:** Captures screenshots during an active browser session, helping you verify page state and browser interactions as the agent runs.
- **Take control:** Supports human-in-the-loop workflows. Use it when a person needs to intervene in a browser session before the agent continues.
- For production workflows, review run summaries, traces, and diagnostic logs to investigate outcomes without continuously monitoring active sessions.

## Governance

Browser Automation Tool can interact with real systems, so design browser workflows with appropriate governance controls. Limit agents to the tools and destinations required for the task, use isolated browser sessions, apply least-privilege access with managed identities and Azure RBAC, and use Live View and tracing to review browser activity. Treat web content as untrusted input, keep system policies separate from page content, validate sensitive destinations, and require human approval for consequential or state-changing actions.

Foundry traces can contain sensitive information, including prompts, model responses, system instructions, and tool-call data. For guidance, see [Restrict access to sensitive content in Microsoft Foundry traces](../../../observability/how-to/traces-sensitive-content).

## Troubleshooting

### The agent doesn't use the tool

- Confirm you created the agent with the Browser Automation tool enabled.
- In your request, require tool usage (for example, `tool_choice="required"`).
- Use tracing in Microsoft Foundry to confirm whether a tool call occurred. For guidance, see [Best practices for using tools in Microsoft Foundry Agent Service](../../concepts/tool-best-practice).

### Connection or authorization errors

- Confirm the browser automation connection ID matches the Playwright workspace connection resource ID in your project.
- Confirm the project identity has access to the Playwright workspace resource.
- If you recently rotated the Playwright access token, update the Foundry project connection key.

::: zone pivot="python"

### Python SDK errors

- **Workspace not found**: Verify your project endpoint uses the correct format: `https://{account-name}.services.ai.azure.com/api/projects/{project-name}`. Don't use the legacy Azure ML endpoint format.
- **Unexpected keyword argument errors**: Ensure you're using the latest version of `azure-ai-projects`. Run `pip install "azure-ai-projects>=2.0.0" --upgrade` to update.
- **Import errors**: Install all required packages: `pip install "azure-ai-projects>=2.0.0"`.

::: zone-end

### Requests time out

Browser automation can take longer than typical requests.

- Increase the client timeout (the C# sample sets a 5-minute timeout).
- Reduce the scope of your prompt (for example, fewer pages and fewer interactions).

## Limitations

- **Sign-in and sensitive actions**: Use this tool only with sites you trust. Avoid pages that prompt for credentials, payments, or other sensitive actions.
- **Page volatility**: Web pages can change at any time. Your agent might fail if the page layout, labels, or navigation flows change. Build error handling into your workflows.
- **Complex single-page applications**: JavaScript-heavy SPAs with dynamic content might not render correctly.

## Cost considerations

This tool uses a Playwright workspace resource to run browser sessions. Review the Playwright workspace documentation for pricing and usage details. For guidance on optimizing tool usage, see [Best practices for using tools in Microsoft Foundry Agent Service](../../concepts/tool-best-practice).

## Clean up

- Delete the agent version you created for testing.
- Revoke or rotate the Playwright access token if you no longer need it.
- Remove the project connection if it’s no longer required. For more information, see [Add a connection in Microsoft Foundry](../../../how-to/connections-add).

## Transparency note

Browser Automation Tool carries security risks. Both errors in judgement by the AI and the presence of malicious or confusing instructions on web pages encountered by agents may cause them to execute commands you or others do not intend, which could compromise the security of your or others' browsers, computers, and any accounts to which the browser or AI has access, including personal, financial, or enterprise systems. Testing and monitoring of agents' actions is recommended to reduce risk. [Learn More](../../../responsible-ai/agents/transparency-note)
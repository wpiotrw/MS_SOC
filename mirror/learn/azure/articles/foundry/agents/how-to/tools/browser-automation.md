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
description: Automate web browsing tasks with the Browser automation tool in Microsoft Foundry agents. Create isolated Playwright sessions for navigation and form filling.
services: cognitive-services
ms.subservice: foundry-agent-service
ms.topic: how-to
ms.date: 2026-10-29T00:00:00.0000000Z
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
- https://authoring-docs-microsoft.poolparty.biz/devrel/97159432-14a9-4307-a469-d2f2c75f0e33
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/de19c5b8-e208-412e-9238-db3f631dea5b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/e453d60d-ba7e-43bc-8028-ec38e6b62512
- https://authoring-docs-microsoft.poolparty.biz/devrel/50565c62-5f6b-4687-be38-323113c72c2e
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ea7bf5d6-7154-4ba9-8ebc-59117ccacd49
platformId: 56e49b87-e066-9ae8-6684-8c2261a9b726
---

# Automate browser tasks with Foundry agents - Microsoft Foundry | Microsoft Learn

Browser automation tool is a generally available (GA) service that lets Microsoft Foundry agents navigate websites, read information, and interact with web applications through a managed remote browser. Watch with Live View, intervene with Take control, and review activity through Foundry observability. Use Browser automation tool when the application doesn't have an API or a connector.

Important

The Browser automation tool controls web browsers on your behalf and can take unintended actions. Testing and monitoring are recommended. To learn more, see [Transparency Note for Foundry Agent Service - Microsoft Foundry](/en-us/azure/foundry/responsible-ai/agents/transparency-note).

## Example browser workflow

The following example illustrates a public-site research task:

| Stage | Example |
| --- | --- |
| User request | "Visit this supplier's public catalog. Find three products matching these requirements, compare their specifications, and include source links." |
| Browser activity | The agent navigates the catalog, inspects product pages, and collects specifications. Follow its progress in Live View. |
| Expected result | A comparison of matching products with links to the pages visited. If fewer than three match, the agent reports what it found. |

## Tool primitives for browser actions

The Browser automation tool exposes a Model Context Protocol (MCP) tool set that's optimized for browser actions.

| Primitives | Supported operations |
| --- | --- |
| Navigate and read | Open URLs, follow links, find content, and inspect page elements. |
| Interact | Enter text, complete forms, select options, handle dialogs, and manage tabs. |
| Upload files | Upload through website controls, within tool limits. |
| Observe and intervene | Watch with Live View and intervene with Take control. |
| Inspect activity | Capture screenshots and inspect console messages and network requests. |
| Extend control | Run JavaScript or Playwright code. Enable these tools only for reviewed scenarios. |

For tool names, parameters, and limits, see the [browser tool reference](/en-us/azure/app-testing/playwright-cloud-browsers/how-to-playwright-workspaces-remote-mcp#tool-reference).

## How it works

The Browser automation tool exposes browser operations to a Foundry agent, while Playwright Workspaces provides the managed remote browser. You don't need a local browser or Playwright runtime. You configure access, approvals, and supervision for your application.

1. **Receive a task.** The agent interprets the user's natural-language request and determines whether browser interaction is needed.
2. **Create a session.** The Browser automation tool starts a browser in the connected Playwright workspace. Subsequent operations reuse its browser session ID to maintain the same browser context.
3. **Observe, act, and verify.** The agent inspects page content and controls, then navigates, selects elements, or enters information. It checks the resulting page state and repeats, adapting its actions to the user's goal and page changes.
4. **Finish and close.** The agent reports the outcome, and the session is closed to release browser resources.

Use Live View and browser session data to observe activity and troubleshoot failures.

Use a [Foundry toolbox](../../concepts/toolbox-overview) to reuse the Browser automation tool across agents through a managed MCP endpoint.

## Choose your starting point

| Agent type | Use this option when |
| --- | --- |
| **Prompt agent (recommended to start)** | Define instructions, a model, and tools without implementing a custom runtime. |
| **Prompt agent with GitHub Copilot harness** | Run a prompt agent with a Foundry-managed harness, without deploying or operating the harness code yourself. |
| **Hosted agent** | Run custom agent code in a Foundry-hosted runtime. |

For your first run:

1. **Connect:** Configure a Playwright workspace and Browser Automation connection.
2. **Add:** Add Browser automation tool to your agent.
3. **Run:** Submit a task, watch in Live View, and verify the result.

Follow the [quickstart](browser-automation-prompt-agent-quickstart) for setup and a runnable example.

## Supported scenarios and limitations

Browser automation tool supports browser-based workflows where an agent needs to navigate websites, interact with web applications, complete forms, and perform multistep tasks.

### Supported scenarios

- **Navigate public websites and retrieve information:** Navigate public websites that don't require CAPTCHA, move across multiple pages, retrieve information, and return results with source links.
- **Sign in with user involvement:** If a site requires an email and password, the user can take control of the screen in Live View, sign in, and return control so the agent session can continue.
- **Work with authenticated websites:** Access websites that require authentication using credentials stored in Azure Key Vault or by allowing the user to take control of the browser session.
- **Complete forms with user involvement:** Complete multistep forms while maintaining browser session and form state. The agent can ask for clarification, continue filling the form, and request user approval before final submission. Users can also take control for manual interaction, such as signing in, completing MFA, or entering an OTP.
- **Upload files:** Upload files or forms as part of browser workflows and transactions.
- **Automate private web applications (preview):** Automate browser-based applications that aren't exposed through APIs, such as ERP applications hosted behind a private virtual network, when the required network access and authentication are configured. Learn more about [accessing privately hosted websites](/en-us/azure/app-testing/playwright-workspaces/how-to-access-private-websites).
- **Record sessions for observability:** Agent builders can choose to record sessions. Foundry replay provides session and tool-call trace views. Actual session recordings are available in Playwright Workspaces and stored in customer-owned storage. Learn more about [Playwright Workspaces](/en-us/azure/app-testing/playwright-workspaces/overview-what-is-microsoft-playwright-workspaces).

### Limitations and considerations

Consider these limitations when designing workflows with Browser automation tool:

- **Bot detection and CAPTCHA:** Some websites restrict or block automated browser access. If a website presents a CAPTCHA or blocks automated traffic, BAT might not be able to complete the workflow. Stealth browsers aren't supported. To report CAPTCHA issues or request platform registration, fill out the [CAPTCHA feedback form](https://forms.cloud.microsoft/r/feSSnFeQMq).
- **Credential handling:** When Azure Key Vault credentials are provided to a prompt agent for browser authentication, the model currently has access to the secret value. In coded or hosted agents, the secret can be kept hidden from the model. Consider this when choosing credentials. We plan to improve Azure Key Vault usability for prompt agents.
- **Reusing authenticated sessions:** BAT doesn't currently support starting a workflow from a saved browser profile or cookies copied from the user's browser. Workflows can't reuse an existing authenticated session to bypass sign-in.
- **Geo-restricted websites and proxy access:** BAT doesn't support proxy or static IP configuration to access websites that restrict access based on geographic location or source IP.
- **Complex or long-running workflows:** Tasks involving many browser interactions or slow-loading pages can take longer and might time out.
- **Dynamic webpages:** Page content and controls can change while the agent is working. If an interaction fails, inspect the current page state before retrying the action.

| Supported scenarios | Not supported scenarios |
| --- | --- |
| MCP with an expanded tool set optimized for browser actions | CAPTCHA or bot verification |
| Private VNet injection (preview) | Browser profiles |
| Live View and Take control | Browser proxies |
| Sign-in with SSO or MFA using Azure Key Vault credentials or user takeover in the live browser | Browser extensions |
|  | Enterprise scenarios that require an Intune-enabled device or passkey |

## Security and reliability

Important

Browser automation tool can change real application data. Treat website content as untrusted input and require human approval for consequential actions.

Before production:

- Restrict tools, identities, and destinations to the task's needs.
- Verify application state before retrying: an action might complete despite a timeout.
- Protect Live View URLs, screenshots, traces, and tool-call data.
- Review [regional and model support](../../concepts/limits-quotas-regions#tool-support-by-region-and-model), [browser session and tool limits](/en-us/azure/app-testing/playwright-cloud-browsers/how-to-playwright-workspaces-remote-mcp#limits-and-current-behavior), and [Playwright Workspaces pricing](https://azure.microsoft.com/pricing/details/app-testing/). Review feature-specific status under supported scenarios and limitations.

## Transparency note

Browser automation tool carries security risks. Both errors in judgement by the AI and the presence of malicious or confusing instructions on web pages encountered by agents may cause them to execute commands you or others do not intend, which could compromise the security of your or others' browsers, computers, and any accounts to which the browser or AI has access, including personal, financial, or enterprise systems. Testing and monitoring of agents' actions is recommended to reduce risk. [Learn More](../../../responsible-ai/agents/transparency-note)
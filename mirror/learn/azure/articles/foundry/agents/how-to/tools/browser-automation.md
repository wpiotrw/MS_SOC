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
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://authoring-docs-microsoft.poolparty.biz/devrel/97159432-14a9-4307-a469-d2f2c75f0e33
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/e453d60d-ba7e-43bc-8028-ec38e6b62512
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://authoring-docs-microsoft.poolparty.biz/devrel/50565c62-5f6b-4687-be38-323113c72c2e
platformId: 56e49b87-e066-9ae8-6684-8c2261a9b726
---

# Automate browser tasks with Foundry agents - Microsoft Foundry | Microsoft Learn

Browser automation tool is a generally available (GA) service that lets Microsoft Foundry agents navigate websites, read information, and interact with web applications through a managed remote browser. Powered by Azure Playwright Workspaces, it gives secure, reliable, and isolated browser sessions as part of its managed browser infrastructure. The service is scalable with concurrent browser sessions to meet your agentic needs.

Use the Browser automation tool typically when the application you need has no API or connector, or when its API doesn't cover your task.

Important

The Browser automation tool controls web browsers on your behalf and can take unintended actions. Testing and monitoring are recommended. To learn more, see [Transparency Note for Foundry Agent Service - Microsoft Foundry](/en-us/azure/foundry/responsible-ai/agents/transparency-note).

## Use cases

| Scenario | What the agent can do |
| --- | --- |
| **Form filling and third-party integration** | Complete forms and move information between browser-based applications when an API isn't available. |
| **Web research and data extraction** | Navigate websites, filter results, and collect or compare information with source links. |
| **Quality assurance and regression investigation** | Explore end-to-end user flows, reproduce issues, and investigate failures in a browser session. Use Playwright testing for repeatable regression tests with explicit assertions. |
| **Customer support and issue replication** | Re-create a customer journey and gather page context and evidence to help support teams investigate browser-based issues. |
| **Legacy-system automation** | Automate repetitive interactions with internal or vendor portals that don't provide suitable APIs. |
| **Employee and business operations** | Support supervised employee-lifecycle tasks, invoice processing, and other browser-based operational workflows. |

Review supported scenarios and limitations for authentication and network requirements, and require human approval for consequential actions.

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

## Capabilities

Browser automation tool combines browser actions with capabilities for human oversight, secure access, networking, and observability.

### Browser actions and batching

Browser automation tool provides an expanded set of browser tools for navigating pages, reading content, completing forms, managing tabs, and capturing screenshots. For repetitive multistep workflows, agents can batch actions by running a Playwright script instead of making separate tool calls for each action. Code execution tools are opt-in and should be enabled only for reviewed scenarios.

### Live View and Take control

Use Live View to watch an agent's browser session in real time. By using Take control, a person can intervene to complete a sign-in, provide approval, or recover from an unexpected page state. They can then return control to the agent to continue the workflow. See [monitoring a run](browser-automation-manage-troubleshoot#monitor-a-run).

### Session recording

Opt in to session recording to replay browser activity for debugging, auditing, and compliance reviews. Recordings are stored in your own storage account, where role-based access control determines who can view them. Foundry replay provides a complementary view of sessions and tool-call traces. See [Manage and troubleshoot](browser-automation-manage-troubleshoot).

### Private website access (preview)

Connect a Playwright workspace to your virtual network and a dedicated delegated subnet to let cloud browsers reach privately hosted applications and endpoints. You can apply your subnet's networking policies to control browser egress and define network boundaries. Learn more about [accessing privately hosted websites](/en-us/azure/app-testing/playwright-cloud-browsers/capabilities/private-website-access).

### Browser proxy (preview)

Bring your own proxy to route cloud-browser traffic through your existing infrastructure. Configure proxy pools and domain-based routing rules to select a proxy for each destination, with priorities determining which rule applies when multiple rules match. Proxy credentials are stored in Azure Key Vault and accessed by using a managed identity.

### Profile reuse (preview, coming soon)

Save and reuse browser profiles containing authentication, cookies, and other browser state across sessions. Profile reuse reduces repeated sign-ins and setup for recurring or long-running workflows. The service keeps profiles in encrypted storage, and workspace-level role-based access control governs who can use them.

### Secret management (preview)

Store website credentials in Azure Key Vault and pass them directly to the browser. The Playwright Workspaces remote MCP server retrieves secret values server-side, without exposing them to the model or application code. You can restrict each secret to an allowed list of domains, and rotated Key Vault secrets are picked up automatically.

### CAPTCHA handling with Web Bot Auth (preview)

Web Bot Auth helps identify legitimate browser automation by cryptographically signing HTTP requests. Participating bot management providers can verify the agent's identity and apply the website owner's access policies. You can register your own bot identity or request Microsoft platform registration through supported providers. Web Bot Auth can reduce CAPTCHA challenges, but it doesn't solve CAPTCHAs or bypass website security controls. See Reduce CAPTCHA challenges with Web Bot Auth.

For tool names, parameters, and limits, see the [browser tool reference](/en-us/azure/app-testing/playwright-cloud-browsers/how-to-playwright-workspaces-remote-mcp#tool-reference). For setup and runnable samples, choose a quickstart.

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

- **Navigate public websites and retrieve information:** Navigate public websites, move across multiple pages, retrieve information, and return results with source links. Website access policies and CAPTCHA challenges can still prevent access.
- **Reduce CAPTCHA challenges with Web Bot Auth (preview):** Identify browser requests using cryptographic signatures that participating bot management providers can verify. You can register your own bot identity or request Microsoft platform registration through supported providers. Web Bot Auth can reduce challenges, but it doesn't solve CAPTCHAs or bypass website access policies. See Reduce CAPTCHA challenges with Web Bot Auth.
- **Work with authenticated websites:** Access websites that require authentication using credentials stored in Azure Key Vault or by allowing the user to take control of the browser session.
- **Manage sign-in secrets (preview):** Store website credentials in Azure Key Vault and pass them directly to the browser. The Playwright Workspaces remote MCP server retrieves secrets server-side, so their values aren't exposed to the model or application code. You can restrict each secret to an allowed list of domains and rotate it in Key Vault.
- **Reuse browser profiles (preview, coming soon):** Save and reuse browser profiles containing authentication, cookies, and browser state across sessions, reducing repeated sign-ins and setup. The service stores profiles in encrypted storage and governs them by using workspace-level role-based access control.
- **Complete forms with user involvement:** Complete multistep forms while maintaining browser session and form state. The agent can ask for clarification, continue filling the form, and request user approval before final submission. Users can also take control for manual interaction, such as signing in, completing MFA, or entering an OTP.
- **Upload files:** Upload files or forms as part of browser workflows and transactions.
- **Automate private web applications (preview):** Automate browser-based applications that aren't exposed through APIs, such as ERP applications hosted behind a private virtual network, when the required network access and authentication are configured. Learn more about [accessing privately hosted websites](/en-us/azure/app-testing/playwright-workspaces/how-to-access-private-websites).
- **Route browser traffic through a proxy (preview):** Use your own proxy infrastructure to control how cloud-browser traffic reaches websites. Configure proxy pools and domain-based routing rules to route requests through different proxies. Store proxy credentials in Azure Key Vault and use a managed identity to access them.
- **Record sessions for observability:** Agent builders can choose to record sessions. Foundry replay provides session and tool-call trace views. Actual session recordings are available in Playwright Workspaces and stored in customer-owned storage. Learn more about [Playwright Workspaces](/en-us/azure/app-testing/playwright-workspaces/overview-what-is-microsoft-playwright-workspaces).

### Limitations and considerations

Consider these limitations when designing workflows with Browser automation tool:

- **Bot detection and CAPTCHA:** Some websites restrict or block automated browser access. Web Bot Auth (preview) can reduce CAPTCHA challenges and other anti-bot friction with supported providers when configured for the Playwright workspace. It doesn't solve CAPTCHAs or bypass site policies. Stealth browsers aren't supported. To report CAPTCHA issues or request platform registration, fill out the [CAPTCHA feedback form](https://forms.cloud.microsoft/r/feSSnFeQMq).
- **Credential handling:** When Azure Key Vault credentials are provided to a prompt agent for browser authentication, the model currently has access to the secret value. In coded or hosted agents, the secret can be kept hidden from the model. Consider this when choosing credentials. We plan to improve Azure Key Vault usability for prompt agents.
- **Reusing authenticated sessions:** Browser automation tool doesn't currently support starting a workflow from a saved browser profile or cookies copied from your browser. Workflows can't reuse an existing authenticated session to bypass sign-in.
- **Geo-restricted websites and proxy access:** Browser automation tool doesn't support proxy or static IP configuration to access websites that restrict access based on geographic location or source IP.
- **Complex or long-running workflows:** Tasks involving many browser interactions or slow-loading pages can take longer and might time out.
- **Dynamic webpages:** Page content and controls can change while the agent is working. If an interaction fails, inspect the current page state before retrying the action.

| Supported scenarios | Not supported scenarios |
| --- | --- |
| Expanded tools for efficient browser actions | CAPTCHA solving or bypassing bot verification |
| Private VNet injection (preview) | Browser extensions |
| Browser proxies (preview) | Enterprise scenarios that require an Intune-enabled device or passkey |
| Live View and Take control for sign-in and MFA |  |
| Secret management with Azure Key Vault (preview) |  |
| Web Bot Auth to reduce CAPTCHA challenges (preview) |  |
| Browser profile reuse (preview, coming soon) |  |

### Reduce CAPTCHA challenges with Web Bot Auth (preview)

AI agents that browse the web often run into anti-bot defenses such as CAPTCHA challenges, rate limits, and blocked requests. Sites use these defenses to stop malicious automated traffic, but because they can't reliably tell a legitimate agent from a malicious bot, they often block legitimate agents too. Web Bot Auth addresses this problem by implementing the [IETF](https://datatracker.ietf.org/doc/html/draft-meunier-web-bot-auth-architecture) draft architecture for HTTP Message Signatures for automated traffic.

When you turn on Web Bot Auth for your Playwright workspace, the Browser Automation tool cryptographically signs each browser request with a private key and adds verification headers. Bot management providers verify the signature against a public key directory and apply the access policies that site owners configure. This approach gives legitimate automation a standard, verifiable way to identify itself, while site owners keep control over who gets access. Web Bot Auth doesn't solve CAPTCHAs or bypass site policies. It works with prompt and hosted agents, needs no agent code or connection changes, and has no extra cost.

| Option | How it works | Who registers with providers | Best for |
| --- | --- | --- | --- |
| Microsoft keys (preview) | Requests are signed with a Microsoft-managed platform identity. The platform expects responsible use of bots. | Microsoft, after you complete the [interest form](https://forms.cloud.microsoft/r/feSSnFeQMq) and it is approved. | Getting started without managing provider accounts |
| Customer dedicated keys | A key pair unique to your workspace is created. The private key stays in a Microsoft-managed vault, and the public key directory is hosted at your workspace's directory URL. | You, by submitting your directory URL in each provider's portal. | Organizations that want their own verified bot identity |

Playwright Workspaces and the Browser Automation tool in Foundry support Web Bot Auth with the following bot management providers as part of the Microsoft keys option:

- Cloudflare
- Akamai Technologies
- F5

As we finalize support with additional providers, we will update this article. When you enable Web Bot Auth, your agents can browse websites protected by these services with reduced friction.

For setup instructions, see the [Web Bot Auth documentation for Playwright Workspaces](/en-us/azure/app-testing/playwright-cloud-browsers/capabilities/captcha-handling).

## Security and reliability

Before production:

- Restrict tools, identities, and destinations to the task's needs.
- Verify application state before retrying: an action might complete despite a timeout.
- Protect Live View URLs, screenshots, traces, and tool-call data.
- Review [regional and model support](../../concepts/limits-quotas-regions#tool-support-by-region-and-model), [browser session and tool limits](/en-us/azure/app-testing/playwright-cloud-browsers/how-to-playwright-workspaces-remote-mcp#limits-and-current-behavior), and [Playwright Workspaces pricing](https://azure.microsoft.com/pricing/details/app-testing/). Review feature-specific status under supported scenarios and limitations.

## Transparency note

Browser automation tool carries security risks. Both errors in judgement by the AI and the presence of malicious or confusing instructions on web pages encountered by agents may cause them to execute commands you or others do not intend, which could compromise the security of your or others' browsers, computers, and any accounts to which the browser or AI has access, including personal, financial, or enterprise systems. Testing and monitoring of agents' actions is recommended to reduce risk. [Learn More](../../../responsible-ai/agents/transparency-note)
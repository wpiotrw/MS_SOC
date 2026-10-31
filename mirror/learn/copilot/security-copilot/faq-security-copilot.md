---
layout: Conceptual
title: Microsoft Security Copilot Frequently Asked Questions | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/faq-security-copilot
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn about the Microsoft Security Copilot frequently asked questions.
ms.date: 2026-04-27T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: faq
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom: 
ms.reviewer: lakram
search.audiencetype: Admin
locale: en-us
document_id: eaf71662-efbc-6a72-47bf-1333201c279c
document_version_independent_id: eaf71662-efbc-6a72-47bf-1333201c279c
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/faq-security-copilot.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: faq-security-copilot
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/faq-security-copilot.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: 1574b55f-0336-2cc6-7b00-0d452c08b156
---

# Microsoft Security Copilot Frequently Asked Questions | Microsoft Learn

## General information

### What is Microsoft Security Copilot?

Microsoft Security Copilot is a generative AI-powered assistant for security and IT. It provides tailored insights and recommendations using global threat intelligence, industry best practices, and organizations’ data from Microsoft and partner tools. Teams can also automate workflows with autonomous Security Copilot agents, accelerating responses, prioritizing risks, and reducing manual workloads - all while remaining firmly in control.

### What are the use cases and capabilities that Security Copilot unlocks for customers?

Security Copilot focuses on making the following use cases easy to accomplish.

- Investigating and remediating security threats
- Building KQL queries and analyzing suspicious scripts
- Understanding risks and managing organization’s security posture
- Troubleshooting IT issues faster
- Defining and managing security policies
- Configuring secure lifecycle workflows
- Developing reports for stakeholders
- Automating tasks with autonomous agents

Visit the [Security Copilot adoption hub](https://adoption.microsoft.com/security-copilot/) to delve deeper into how Security Copilot benefits roles like CISOs, threat intelligence analysts, IT admins, data security admins, and more.

### Does Microsoft Security Copilot work with other Microsoft products?

Yes. Security Copilot is integrated with and embedded in other Microsoft Security products. These products include, but aren't limited to:

- Azure Firewall
- Microsoft Defender Attack Surface Management
- Microsoft Defender for Cloud
- Microsoft Defender Threat Intelligence
- Microsoft Defender XDR
- Microsoft Intune
- Microsoft Purview
- Microsoft Sentinel

Security Copilot can access data from these products and provide genAI assistance and agentic automation to increase the effectiveness and efficiency of security professionals using those solutions.

### Who are the intended users of Security Copilot?

SOC analysts, compliance analysts, IT admins, data security admins, identity admins and CISOs are some of the intended users of Security Copilot. Visit the [Security Copilot adoption hub](https://adoption.microsoft.com/security-copilot/) to learn about the key scenarios.

### What languages are supported?

Security Copilot supports multiple languages. The model is available in eight languages\* and the user experience is available in 25 languages.\*\* 

\*Model: English, German, Japanese, Spanish, French, Italian, Portuguese, and Chinese

\*\*UX: Above languages plus Korean, Dutch, Swedish, Polish, Norwegian, Turkish, Danish, Finnish, and more in the user experience.

For more information, see [Supported languages](supported-languages).

### What is the difference between Security Copilot and generic LLM?

A generic LLM lacks key benefits such as:

- Real-time signal processing with structured log data, to detect and analyze threats as they happen rather than after the fact.
- Investigative reasoning to trace the source and impact of incidents. AI needs to pivot across many data points, just as human analysts would, and adjust conclusions as new information emerges.
- Precision with evidence to ensure that the AI is accurate and backed by reliable data.
- Persistent data collection to maintain a continuous, comprehensive view.

Without these capabilities and a deep understanding of your specific security environment, a generic model simply can’t provide the depth of analysis required.

Microsoft is uniquely positioned to tackle the challenges of using AI in security – our solution is built on the most advanced models available, and builds on:

- A hyperscale infrastructure, providing the scalability and infrastructure needed to process massive volumes of data in real-time.
- A security-specific orchestrator that streamlines, contextualizes, and coordinates responses across tools and teams.
- Seamless integration through plugins, connecting your existing systems and extending what our solution can do.
- Evergreen threat intelligence, informed by 84 trillion daily signals, for unmatched visibility across your whole threat landscape.
- Built-in cyber skills training and promptbooks to empower teams with the knowledge and resources they need.

By building on all these components, we provide an AI security solution that understands your security environment, delivers insights in natural language, and handles sensitive data securely.

For Customer Data handling FAQs, see [Data and Compliance](faq-data-compliance).

## Purchasing and billing information

### Are there any prerequisites to purchase?

An Azure subscription and Microsoft Entra ID (formerly known as Azure Active Directory) are prerequisites for using Security Copilot; there are no other product prerequisites. For more information, see [Get started with Security Copilot](get-started-security-copilot).

### Is deployed Microsoft Entra ID (formerly known as Azure Active Directory) a requirement for Security Copilot?

Yes. Security Copilot is a SaaS application and requires Microsoft Entra ID to authenticate the users who have access.

### How is Security Copilot priced?

Security Copilot is priced based on Security Compute Units (SCUs).

- Provisioned SCUs support regular workloads and are billed monthly.
- Overage SCUs offer flexible, on-demand capacity and are billed only when used.

Use the in-product dashboard to monitor SCU usage and adjust capacity as needed.

For more information, see [Microsoft Security Copilot - Pricing](https://azure.microsoft.com/pricing/details/microsoft-security-copilot/)

### Does Security Copilot support tenant or subscription transfers?

No, at this time Security Copilot doesn't support moving Security Copilot resources across Microsoft Entra tenants or subscription transfers.

### Can SCUs be shared between a tenant’s Security Copilot Workspaces?

SCUs, whether Provisioned or Overage, can't be shared between Workspaces. For example, if an organization has Workspace A (1 provisioned, three overage) and Workspace B (2 provisioned, five overage), Workspace A can't use Workspace B’s SCUs to prevent throttling if it exhausts its own total of 4 SCUs. Similarly, Workspace B can't use Workspace A’s SCU capacity if it exhausts its own SCUs.

### How can I estimate SCU provisioning and budget for Security Copilot?

Estimating SCU needs and budgeting depends on how your organization uses generative AI across Microsoft Security products. Use the [SCU capacity calculator](https://securitycopilot.microsoft.com/calculator) to get a starting point based on the number of users and workloads across Microsoft Defender, Microsoft Intune, Microsoft Purview, Microsoft Entra, and the Security Copilot standalone experience. Because every prompt and workflow varies in complexity, SCU consumption isn't fixed. Start small, experiment, and refine based on your actual usage. Track usage in real time with the in-product dashboard, which helps you monitor SCU consumption and adjust capacity as needed.

### How do I interpret the results on the SCU capacity calculator?

The results show the maximum expected number of SCUs per hour, based on the number of monthly users per experience and the inclusion of automation through Logic Apps and Promptbooks. In addition to the maximum SCUs per hour, the calculator also displays all possible combinations of provisioned and overage SCUs, along with the corresponding monthly cost range. The highest monthly cost is calculated based on continuous 24/7 capacity usage.

### What if my needs aren't covered by the SCU capacity calculator (for example, I have more than 50 Intune users).

Feel free to [Contact us](https://info.microsoft.com/ww-landing-security-generic-contact-me.html) or reach out to your Microsoft account manager for more information.

### What are the minimum provisioning requirements for SCUs in Workspaces?

To use Microsoft Security Copilot, each tenant must provision a minimum of one SCU. The one provisioned SCU enables access to at least one Workspace.

- Provisioned SCUs are required to activate capacity and are billed hourly.
- Overage SCUs can be set from 0 to 999 and are billed only when used.

## Technical and product information

### What partner tools are integrated with Security Copilot?

Microsoft Security Copilot supports many plugins, including Microsoft and non-Microsoft plugins. For more information, see [Plugins](/en-us/copilot/security/plugin-other).

Note

Products that integrate with Security Copilot need to be purchased separately.

### Does Security Copilot make recommendations for IoT/OT scenarios?

No, Security Copilot doesn't currently support IoT/OT.

### Does Security Copilot offer dashboarding?

Security Copilot offers an in-product usage dashboard where customers can dive deep into their SCU consumption.

### Can Security Copilot execute workflows - from triaging to using pinned messages, to governing how the customer should label the incident and whether an incident should be closed?

Security Copilot provides [Promptbooks](using-promptbooks) that are ready-to-use workflows that can serve as templates to automate repetitive steps—for instance, regarding incident response or investigations. Additionally, there are [connectors](/en-us/copilot/security/connectors-overview) in Security Copilot that are a wrapper around the API that allows developers and users to call out to the Microsoft Security Copilot platform to perform specialized tasks. For example, the Logic Apps connector allows you to call into Copilot from an Azure Logic Apps workflow. Similarly, the Copilot Studio connector enables you to access Security Copilot to perform actions like ‘submit a Security Copilot prompt’ or ‘fetch a Security Copilot prompt status’.

### What role-based access control or delegation features does Security Copilot have? How are user permissions kept in Security Copilot aligned to user permission configurations in other solutions?

Copilot uses on-behalf-of authentication to access security-related data through active Microsoft plugins. Specific Security Copilot roles must be assigned in order for a group or individual to access the Security Copilot platform. For more information, see [Understand authentication](authentication).

### How is Security Copilot dealing with a "token limit"?

Large language models (LLMs) including GPT have limits on how much information they can process at once. This limit is known as a “token limit”, and roughly correlates to 1.2 words per token. Security Copilot uses the latest GPT models from Azure OpenAI to ensure we can process as much information as possible in a single session. In some cases, large prompts, long sessions, or verbose plugin output may overflow the token space. When this scenario happens, Security Copilot attempts to apply mitigations to ensure an output is always available, even if the content in that output isn’t optimal. Those mitigations aren’t always effective, and it might be necessary to stop processing the request and direct the user to try a different prompt or plugin.

### What are Security Copilot agents?

Microsoft Security Copilot agents enhance security and IT operations with autonomous and adaptive automation. Agents seamlessly integrates with Microsoft Security solutions and third-party partner ecosystem to handle high-volume security tasks. Purpose-built for security, these agents learn from feedback, adapt to organizational workflows with your team fully in-control, and operate securely within Microsoft’s Zero Trust framework—accelerating responses, prioritizing risks, and driving efficiency. By reducing manual workloads, they enhance operational effectiveness and strengthen your organization’s overall security posture.

Visit the [adoption hub](https://adoption.microsoft.com/security-copilot/) to learn more about Security Copilot agents.

For information on how to build custom agents, see [Developer content](/en-us/copilot/security/developer/).

### What compute resources do Security Copilot agents use?

Agents utilize SCUs to operate just like other features in Security Copilot. They integrate seamlessly with Microsoft Security solutions and the broader supported partner ecosystem.

### Where can I find Security Copilot agents?

You can easily discover Microsoft Security Copilot agents from both the standalone and embedded experiences.

For the standalone experience, you can select Go to agents from the banner. You can also navigate to the agent library from the home menu. In the embedded experiences, you'll see agents within the portal and explore their capabilities.

Visit the [adoption hub](https://adoption.microsoft.com/security-copilot/) to learn more.

### What are connectors in Security Copilot?

The connectors in Security Copilot are a wrapper around the API that allows the developers and users to call out to the Microsoft Security Copilot platform to perform specialized tasks. Currently, Logic Apps and Copilot Studio connectors are supported. For more information, see [Connectors](/en-us/copilot/security/connectors-overview).

### How does the Copilot Studio connector work?

Copilot Studio connector enables you to access Security Copilot while creating automation workflows. Using the Security Copilot connector, you can:

- Submit a Security Copilot prompt - Submit a natural language prompt to create a new Security Copilot investigation. After completion, the evaluation result will then be returned to your workflow.
- Fetch a Security Copilot prompt status - Submit a natural language prompt to pull the status of a Security Copilot evaluation. After completion, the evaluation result will then be returned to your workflow.

### How does the Logic Apps connector work?

The Microsoft Security Copilot Logic Apps connector allows you to call into Copilot from an Azure Logic Apps workflow. The connector exposes two connector actions:

- Submit a Security Copilot prompt - Submit a natural language prompt to create a new Security Copilot investigation. After completion, the evaluation result will then be returned to your workflow.
- Submit a Security Copilot promptbook - Given a promptbook, invoke a new Security Copilot promptbook evaluation and return the output to your Azure Logic Apps workflow.

## Partner information

### What are the use cases for Partners?

Partners can provide signals or build complementary solutions around Security Copilot scenarios.

### If a customer works with a managed security service provider (MSSP), can the MSSP use and manage Security Copilot on the customer's behalf?

Yes, MSSPs that provide SOC services for customers are able to access the customer's Security Copilot environment if the customer elects to provide access. Available options include:

- Azure Lighthouse
- B2B Collaboration / Guest Accounts
- Granular Delegated Admin Privileges (GDAP)

There currently isn't a CSP or reseller multitenant model for MSSPs. Each customer is responsible for purchasing their own SCUs and setting up their MSSPs with the necessary access if they're accessing within the customer’s tenant. If Azure Lighthouse delegated access is provided to the customer’s Microsoft Sentinel Workspaces then the partner is able to use their partner capacity plan SCUs to perform prompting against the customer’s Microsoft Sentinel Workspace data.

### If an MSSP prompts across a customer’s tenant, using Azure Lighthouse, will the MSSP use their own SCUs or the customer’s SCUs?

Azure Lighthouse allows partners to gain Security Copilot permissions for customer’s Microsoft Sentinel Workspaces and other supported Azure resources. The capacity plan (SCUs) used is the partner tenant's capacity plan.

### Can MSSPs, use a single instance of Security Copilot to manage multiple tenants?

Azure Lighthouse is supported for invoking Sentinel-based skills from the partner tenant against a single customer's Microsoft Sentinel Workspace at a time that the partner has been provided delegated access to through Azure Lighthouse. The partner tenant will leverage their SCUs to perform Security Copilot invoked Microsoft Sentinel skills against the customer's tenant without the need for the customer tenant to be provisioned for Security Copilot or having SCUs of their own.

### Are there third-party integrations available today?

Microsoft Security Copilot supports many plugins, including Microsoft and non-Microsoft plugins. For more information, see [Non-Microsoft plugins overview](/en-us/copilot/security/plugin-other). Additionally, there are agents from our partners that are available in Security Copilot. For more information, see [Partner agents](/en-us/copilot/security/agents-other).

Note

Products that integrate with Security Copilot need to be purchased separately.

### Is there a marketplace for the plugins or services?

There isn't a plugin marketplace. ISVs can publish their solutions to GitHub. All partners are required to publish their solutions or managed services to the Microsoft Commercial marketplace. For more information on publishing to marketplace, see:

**Publish solution to the Microsoft Commercial Marketplace:**

- [Create a commercial marketplace account in Partner Center - Partner Center](/en-us/partner-center/create-account)
- [How to manage a listing in Partner Center](https://partner.microsoft.com/asset/detail/how-to-manage-a-listing-in-partner-center-mp4)

**MSSP Specific:** Must have a security designation in Microsoft AI Cloud Partner Program.

- [Consulting Service](/en-us/partner-center/marketplace/plan-consulting-service-offer)
- [Managed Services](/en-us/partner-center/marketplace/plan-managed-service-offer)

**SaaS Specific:**

- [Plan a SaaS offer for the Microsoft commercial marketplace - Marketplace publisher](/en-us/partner-center/marketplace/plan-saas-offer)
- [Create a SaaS offer in the commercial marketplace - Marketplace publisher](/en-us/partner-center/marketplace/create-new-saas-offer)
- [ISV Success Program Overview](https://www.microsoft.com/isv/programs-benefits-b?ef_id=_k_3f7804cdfe0e117482f361637f09a6c7_k_&amp;OCID=AIDcmmnzkuyicj_SEM__k_3f7804cdfe0e117482f361637f09a6c7_k_&amp;msclkid=3f7804cdfe0e117482f361637f09a6c7)
- [Build and publish with ISV Success - Partner Center](/en-us/partner-center/isv-success)

### What if MSSPs aren't using Microsoft Defender XDR or Microsoft Sentinel?

Microsoft Security Copilot doesn't have any specific Microsoft security product requirement for provisioning or use since the solution is built on aggregating data sources both from Microsoft and third party services. With that said, there's a significant value in having Microsoft Defender XDR and Microsoft Sentinel enabled as supported plugins for enriching investigations. Security Copilot only uses skills and accesses data from enabled plugins.

### Does an MSSPs SOC Solution need to be hosted on Azure?

It's recommended that the solution is hosted on Azure but not required. 

### Is there a product roadmap that can be shared with Partners?

Not at this time.
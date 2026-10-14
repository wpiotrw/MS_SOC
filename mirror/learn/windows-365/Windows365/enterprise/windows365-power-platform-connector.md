---
layout: Conceptual
title: Windows 365 Power Platform connector (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/windows365-power-platform-connector
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn more about the Windows 365 Power Platform connector.
author: IvayloIvanov-W365
ms.author: ivivano
ms.service: windows-365
ms.topic: article
ms.date: 2026-04-01T00:00:00.0000000Z
locale: en-us
document_id: f14a3fad-51c7-ca2c-8988-1e4c1efd909b
document_version_independent_id: f14a3fad-51c7-ca2c-8988-1e4c1efd909b
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/windows365-power-platform-connector.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/windows365-power-platform-connector
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/windows365-power-platform-connector.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
- https://authoring-docs-microsoft.poolparty.biz/devrel/1ae5c491-970a-4062-8301-6336e69f9026
- https://authoring-docs-microsoft.poolparty.biz/devrel/e6f942e8-55a7-4c86-b8e3-7456508ea850
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
- https://authoring-docs-microsoft.poolparty.biz/devrel/f2c3e52e-3667-4e8a-bf11-20b9eaccdc8c
- https://authoring-docs-microsoft.poolparty.biz/devrel/f1834696-48d6-470d-966b-6ee418881596
platformId: 97e5b13b-503c-d8fc-3cec-52bc766441f4
---

# Windows 365 Power Platform connector (preview) | Microsoft Learn

Note

The Windows 365 Power Platform connector is currently in Public Preview. Visit [this page](/en-us/windows-365/public-preview) to learn more about previews in Windows 365.

 With prebuilt actions and triggers for Windows 365 built on top of Graph, IT and operations teams can use the connector to: 

- Build Cloud PC workflows using Power Automate and Azure Logic Apps, such as sending emails to users when Cloud PCs are provisioned
- Build Copilot Studio agents to provide guided responses to common questions based on configured knowledge sources

## Build repeatable Cloud PC workflows with Power Automate or Azure Logic Apps

Power Automate and Azure Logic Apps are a great fit when you want to turn an event or request into a repeatable sequence of steps. With the Windows 365 connector, you can build flows for both users and admins. 

**Example: Send an email to a user once a Cloud PC has been provisioned**

![Diagram that shows an example of how to build a workflow to send users an email once a Cloud PC has been provisioned.](media/windows365-power-platform-connector/w365-power-platform-workflow.png)

**Permissions needed:**

The user that wants to set up the flow must have one of the following roles: 

- Global Administrator
- Intune Service Administrator
- Windows 365 Administrator (for Cloud PC-specific operations)
- Custom role with Windows 365 permissions (requires Webhook.Create and Webhook.Delete for trigger operations)

**How to build this capability in Power Automate:**

1. Log in to Power Automate and click New and choose Automated cloud flow. Name your flow.
2. Select the When a Cloud PC is created or updated trigger. The trigger will then be added to your new workflow.
3. Select When a Cloud PC is created in the dropdown menu of the trigger.
4. Select the Get Cloud PC action and add the dynamic Cloud PC ID returned from the trigger.
5. Click the + symbol and add the Get user profile (V2) action, then add the User principal name dynamic field from the Get a Cloud PC action above it.
6. Click the + symbol and add the Send an email (V2) action.
7. Add the User principal name from the Get a Cloud PC action to the To line.
8. Add the appropriate subject to the email. Here, you can also include the Display name from the Get user profile (V2) action.
9. Add the appropriate body content for your organization, including how your organization’s users can access their Cloud PCs and where to get support.
10. Click Save in the top right to save your flow.

Note

We recommend testing this capability by limiting who it applies to at first. For example, it's possible to set the To line in the email action to an IT admin to first test your flow before opening it to more users. 

Ideas for how to extend this capability: 

Send notifications via Teams instead with the Teams connector 

Use [Adaptive Cards](https://adaptivecards.microsoft.com/?topic=design-best-practices) and the [Adaptive Card Designer](https://adaptivecards.microsoft.com/designer.html) to design a notification that has the right information for your users. 

- Use [device preparation policies](/en-us/windows-365/enterprise/autopilot-device-preparation) to ensure that the Cloud PC has the right apps and scripts before user login.

## What is Microsoft Power Platform?

Microsoft Power Platform is a low-code platform that enables organizations to analyze data, build custom apps, automate processes, and create agents, while integrating deeply with Microsoft 365, Dynamics 365, Azure, Entra, and many third-party connectors. 

- **Power Automate and Azure Logic Apps** for workflow automation across apps and services

**Copilot Studio** to build and custom AI agents and conversational experiences 

**Power Apps** to build business apps with rich forms and logic 

**Power Pages** to build websites 

- **Power BI** to analyze data and share insights

With [1400+ connectors from Microsoft and other companies](/en-us/connectors/connector-reference/), plus the ability to [create custom connectors](/en-us/connectors/custom-connectors/), organizations can bring in their own data from systems with a REST API. 

## Learn more about Power Platform and the connector

[Windows 365 - Connectors](/en-us/connectors/windows365/)

[Introduction to Microsoft Power Platform](/en-us/power-platform/developer/get-started)

[Licensing overview for Microsoft Power Platform](/en-us/power-platform/admin/pricing-billing-skus)

[Overview - Azure Logic Apps](/en-us/azure/logic-apps/logic-apps-overview)

## Feedback for the Public Preview

As you try it out, share what’s working, what’s missing, and which scenarios matter most to you and your organization, especially around the triggers and actions we made available so far.

To provide general feedback, feature requests, and report issues, visit this [form](https://forms.office.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbRwEeQeDAcnZPsQGKusPYIeNUODIzQjBaTUpCTTZGUVpXRVdNTFFTMTU3Mi4u&amp;fswReload=1&amp;fswNavStart=1774634225052).
---
layout: Conceptual
title: Audit logs for Copilot and AI applications | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/audit-copilot
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn about how audit logs are generated for user interactions and admin activities related to Microsoft Copilot and AI applications.
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-08-26T00:00:00.0000000Z
ms.update-cycle: 180-days
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-audit
ms.collection:
- purview-compliance
- audit
- msec-ai-copilot
f1.keywords:
- NOCSH
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1017
locale: en-us
document_id: 71f05e16-fa71-1ca4-cac3-84e8d06e7b22
document_version_independent_id: 71f05e16-fa71-1ca4-cac3-84e8d06e7b22
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/audit-copilot.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: audit-copilot
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/audit-copilot.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: d3a7e87a-04af-aa61-fa33-f334e0331a40
---

# Audit logs for Copilot and AI applications | Microsoft Learn

This article provides an overview of audit logs generated for user interactions and admin activities related to [Microsoft Copilot](/en-us/copilot/) and AI applications. The system automatically logs these activities as part of [Audit (Standard)](audit-solutions-overview#audit-standard). If your organization enables auditing, you don't need to take extra steps to configure auditing support for Copilot and AI applications.

## Billing for auditing non-Microsoft AI applications

Audit logs for non-Microsoft AI applications use pay-as-you-go billing. This billing model provides user and admin interaction audit logs that the system retains for 180 days. These audit logs cover interactions with non-Microsoft AI applications.

Your enterprise subscription doesn't include audit logs for this type of user interaction. Instead, it falls under [pay-as-you-go billing](purview-billing-models). The system logs these interactions under the *AIAppInteraction* recordType or *AIApp* workload. Some scenarios logged under the *ConnectedAiAppInteraction* recordType are also part of this pay-as-you-go billing model. You need to enable pay-as-you-go features to turn on these logs. When you enable them, the system retains these audit logs for 180 days. Consumption is charged based on the number of audit records ingested for user interactions with these non-Microsoft AI applications.

Pay-as-you-go billing doesn't apply to Microsoft applications. All Microsoft applications, including Microsoft Copilots like [Microsoft Security Copilot](/en-us/copilot/security/microsoft-security-copilot), [Copilot in Microsoft Fabric](/en-us/fabric/fundamentals/copilot-fabric-overview), and custom applications built using [Microsoft Copilot Studio](/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio) and Microsoft Foundry are included in Audit Standard.

## Admin activities with Copilot and AI applications

The system generates audit logs when an administrator performs activities related to Copilot settings, plugins, promptbooks, or workspaces. For more information, see [Microsoft 365 Copilot activities](audit-log-activities#microsoft-365-copilot-admin-activities).

## User activities with Copilot, Cowork, and AI applications

The system automatically generates audit logs when a user interacts with Copilot, Cowork, or an AI application. These audit records contain details about which user interacted with Copilot, when the interaction took place, and where it occurred. Audit records also include references to files, sites, or other resources Copilot, Cowork, and AI applications accessed to generate responses to user prompts.

### Common properties in Copilot audit logs

The following table outlines some of the common properties included in audit logs.

| Attribute | Definition | Examples |
| --- | --- | --- |
| AccessedResources | References to all resources (files, documents, emails, etc.) which Copilot accessed in response to the user's request.  - *ID* is the unique identifier for the resource. This could be a fileId on OneDrive, or a messageId in Teams, or email ID in Outlook, etc.  - *SiteUrl* is the URL of the resource that was accessed. This could be the URL of a SharePoint site, full file path of a file, etc.  - *ListItemUniqueId* is a unique identifier for an item in SharePoint.  - *Type* refers to the type of resource that was accessed. It can contain values like the filetype extension (pptx, docx, etc.) or describe the type of resource (for non-SharePoint resources).  - *Name* is the user-friendly readable name of the resource (for example, fileName).  - *SensitivityLabelId* is the ID of the sensitivity label assigned to the resource. This is helpful in identifying whether Copilot accessed any sensitive information while generating its response.  - *Action* refers to the nature of access which Copilot performed on the resource. Common values include *read*, *create*, *modify*.  - *PolicyDetails* is used in scenarios where Copilot's access to a particular resource was blocked or restricted based on some policy. This property can include details like *PolicyId*, *PolicyName*, list of rules, etc.  - *Status* is used to specify whether Copilot's action on a specific resource was a *success* or *failure*.  - *XPIADetected* is a boolean that denotes whether there was an XPIA (Cross Prompt Injection Attack) detected from a particular resource which Copilot accessed. | For example: "AccessedResources":[{"Action":"Read","ID":"AAAAAEYE2GAACp1FlnN\_CHXStUkHAGWJYgtgcv1eOxe2v4H4jOsAAAQsLLeAAGWJYgtgcv1EoXe2v4H4josAABwvq8gAAA2","Name":"Document1.docx","SensitivityLabelId":"f41ab342-8706-4188-bd11-ebb85995028c","SiteUrl":"`https://microsoft.sharepoint.com/teams/OfficeSerbia/Shared%20Documents/SPOPPE/Document%20transformation%20services/Crawled%20Word%20documents/IW/Document1.docx?web=1`","Type":"docx","listItemUniqueId":"AAAAAEYE2GAACp1FlnN\_CHXStUkHAGWJYgtgcv1eOxe2v4H4jOsAAAQsLLeAAGWJYgtgcv1EoXe2v4H4josAABwvq8gAAA2"}], |
| AgentId | Unique identifier for an agent. The string can also include details about the category of agent involved in the interaction. | For example, when a user interacts with a Declarative Agent or a Custom-engine Agent created through Microsoft Copilot Studio, then Agent ID contains values like *CopilotStudio.Declarative.8ad83f3e-b424-4d54-8ddb-15dc19247088* or *CopilotStudio.CustomEngine.11fd28b5-4452-4615-be3d-7046a6f31131*. |
| AgentName | A friendly readable name of the agent. | *JiraStatusAgent*, *SalesAgent*, *ReminderBot*, and others. |
| AgentVersion | The version number or version ID of the agent involved. | Values like *25.001*, *8076fbed-be52-4004-ac89-81181ecd7b33*, and others. |
| AISystemPlugin | Details of plugins or extensions enabled for the Copilot interaction.  - *Name* is the name of the plugin that Copilot uses in generating the response.  - *ID* is the unique identifier for the plugin.  - *Version* refers to the version of plugin used. |  |
| AppHost | The same Copilot application can be deployed within multiple host applications. This property helps identify the application that hosted the interaction between a user and Copilot. | Some of the common AppHost scenarios are:  - *BizChat*: The Copilot interaction was performed in the Microsoft 365 Copilot Chat client (either via Teams, or the app), or via the website microsoft365.com/copilot or microsoft365.com/chat  - *Bing*: The Copilot interaction was performed through the Microsoft Edge browser, Office mobile apps, or copilot.cloud.microsoft.com  - *Office*: The Copilot interaction was performed through office.com or microsoft365.com  - Other application-specific values: Values like *Word*, *Excel*, *PowerPoint*, *OneNote*, *Stream*, and others indicate that the interaction was performed within these applications |
| AppIdentity | A detailed string that you use to uniquely identify the specific Copilot or AI Application that the user interacted with. It typically follows the structure *workloadName.appGroup.appName*. | For example, interactions with first-party Copilot apps developed by Microsoft use values like *Copilot.MicrosoftCopilot.Microsoft365Copilot*, *Copilot.Fabric.CopilotforPowerBI*, *Copilot.Security.SecurityCopilot*, and others. Interactions with custom-built Copilots created through Copilot Studio use values like *Copilot.Studio.AppId*. Interactions with third-party AI apps deployed within your organization (which use *ConnectedAIApp* as the workload) use values like *ConnectedAIApp.Entra.AppId* or *ConnectedAIApp.AzureAI.AzureResourceName*. Interactions with third-party AI apps that are audited through network/browser Data Loss Prevention (DLP) (which use *AIApp* as the workload) use values like *AIApp.SaaS.AppName*. |
| CapacityId | Unique identifier for the Microsoft Fabric Capacity in a tenant. | You can find the *CapacityID* in the URL of the capacity management page. In Microsoft Fabric, go to **Settings** &gt; **Governance and insights** &gt; **Admin portal** &gt; **Capacity settings** and select a capacity. The *CapacityID* is shown in the URL after */capacities/*. For example, `00001111-aaaa-2222-bbbb-3333cccc4444` is the *CapacityID* in the following URL: `https://app.powerbi.com/admin-portal/capacities/00001111-aaaa-2222-bbbb-3333cccc4444`. |
| ClientRegion | The user's region when they performed the operation. |  |
| Contexts | Contains a collection of attributes to help describe where the user was during the Copilot interaction.  - *ID* is the identifier of the resource that was being used during the Copilot interaction.  - *Type* is the filetype/name of the app or service where the interaction occurred. | - *ID* contains values like *FileId* or *FilePath* (for SharePoint scenarios), or Teams Chat ID or Meeting ID (for Teams scenarios), and others.  - *Type* contains values like docx, pptx, xlsx, TeamsMeeting, TeamsChannel, TeamsChat, and others. |
| DLPEvaluationDeferred | An integer bitmask that indicates DLP evaluation of one or more content processing stages couldn't be completed, so it's deferred for later reevaluation. | The value is a bitmask where each bit represents a specific evaluation scenario that was deferred. Multiple deferred scenarios can be represented by combining bit values using a bitwise OR operation.  - *1 – Prompt*: DLP evaluation of the user prompt was deferred.  - *2 – Response*: DLP evaluation of the generated response was deferred.  - *4 – Grounding*: DLP evaluation of grounding content was deferred.  - *8 – WebGrounding*: DLP evaluation of web-grounding content was deferred. |
| DLPEvaluationDeferredReason | Provides the reason why one or more DLP evaluation stages identified by *DLPEvaluationDeferred* could not be completed during the original request processing and were deferred for later reevaluation. | This field is populated only when *DLPEvaluationDeferred* contains a non-zero value. For example, Timeout, Authentication Error, Service Unavailable. |
| Messages | Contains details about the prompt and response messages within the Copilot interaction. A single audit record typically contains a prompt-response pair but can also include a prompt with multiple response messages (that is, all Copilot responses associated with that prompt).  - *ID* is the messageId of the prompt/response message in the Copilot interaction.  - *IsPrompt* is a boolean flag to denote whether this message is a user prompt or Copilot response.  - *JailbreakDetected* is a boolean flag to denote whether a jailbreak attempt was made using this prompt message.  - *Size* is currently not used. | "Messages": [ {"ID":"1715186983849", "isPrompt":true}, {"ID":"1715186984291", "isPrompt":false} ] |
| ModelTransparencyDetails | Details of the AI model used in the interaction.  - *ModelProviderName* is the publisher of the model used. All Microsoft 365 Copilot scenarios include a ModelProviderName.  - *ModelName* is the name of the model used. Not available in Microsoft 365 Copilot scenarios.  - *ModelVersion* is the version of the model used. Not available in Microsoft 365 Copilot scenarios. |  |
| Operation | Specifies the name of the activity that was audited. | For user interactions with Copilot or Cowork, this property contains *CopilotInteraction*. For user interactions with other AI applications, values like *ConnectedAIAppInteraction* and *AIAppInteraction* are used, as described in the RecordType row.  Also includes Copilot admin operations like *UpdateTenantSettings*, *CreatePlugin*, *DeletePlugin*, *EnablePromptBook*, and others. |
| RecordType | Identifies the category of Copilot or AI application that the user interacted with. | *CopilotInteraction* refers to scenarios where a user interacted with a Microsoft-developed Copilot application such as Microsoft 365 Copilot, Cowork, Security Copilot, and others. *ConnectedAIAppInteraction* refers to scenarios where a user interacted with a custom-built Copilot or third-party AI application deployed and registered within your organization. *AIAppInteraction* refers to interactions with third-party AI applications that aren't deployed within your organization. |
| Workload | Identifies the app category, similar to RecordType. | *Copilot*, *ConnectedAIApp*, *AIApp* |

### Common AppHost scenarios in Copilot

The following table lists some of the commonly used values for AppHost and describes the scenarios in which they're used.

| AppHost | Copilot Scenario | Copilot product |
| --- | --- | --- |
| Bing | **Business Chat via Bing/Windows interface.** Refers to Microsoft 365 Copilot's cross-app **Business Chat** access through the Bing Chat experience (for instance, in the Microsoft Edge browser sidebar, Windows Copilot, or the copilot.cloud.microsoft.com web portal). This scenario occurs when a user engages the Copilot in a general-purpose chat outside any specific Office app. | [Microsoft 365 Copilot Chat](/en-us/copilot/overview) |
| Bookings | Copilot in Microsoft Bookings. | Microsoft 365 Copilot |
| Copilot in Azure | **Copilot in Microsoft Azure (Cloud Management).** This refers to Copilot usage in the context of **Microsoft Azure**. Though labeled under Microsoft 365 Copilot, the scenario is a cloud admin or developer using Copilot to manage Azure resources. For example, in the Azure portal, ad admin might ask, "How do I set up an alert for CPU usage on my VMs?" and Copilot would generate an ARM template or Azure CLI steps. Or "list untagged resources and suggest a tagging scheme". Essentially, Copilot in Azure is an AI cloud assistant to query and control Azure services via natural language. | Microsoft 365 Copilot |
| Copilot in Defender | **Security Copilot in Microsoft Defender.** The user is using Copilot within the **Microsoft Defender** security portal. This assists security operations (SecOps) tasks. For example, an analyst could ask, "Investigate alert ID 23455 and summarize what happened," and Copilot analyzes Defender alerts and incidents to produce an explanation or even recommend next steps. It can also cross-reference threat intelligence. This scenario specifically focuses on **Defender for Endpoint/Office/Cloud, etc.** data via the Security Copilot interface. | Security Copilot |
| Copilot in Intune | **Security Copilot in Microsoft Intune (Endpoint Management).** Copilot is used in the **Microsoft Intune** admin center. It helps IT admins with device management and security posture. For instance, an admin might ask, "How many devices are noncompliant this week and why?". Copilot retrieves Intune data on device compliance and summarize reasons. It can also assist with troubleshooting by comparing device configuration or retrieving app deployment status. This is essentially Security Copilot tapping into Intune's information to answer questions and provide insights for IT and security teams. | Security Copilot |
| Designer | Copilot in Microsoft Designer. | Microsoft 365 Copilot |
| Edge | **Business Chat in Edge sidebar.** Represents Microsoft 365 Copilot chat accessed through the **Edge browser's Copilot (Bing Chat Enterprise) sidebar**. In this scenario, the user is likely using the Microsoft Edge sidebar Copilot to query organizational data (a BizChat experience within Microsoft Edge). | Microsoft 365 Copilot Chat |
| Excel | **Copilot in Microsoft Excel.** The user is using Copilot inside an Excel spreadsheet. For example, Copilot might be asked to analyze data, create formulas, or generate a summary of a table. It's the Excel-integrated Copilot helping with computations or insights in workbooks. | Microsoft 365 Copilot |
| Forms | **Copilot in Microsoft Forms.** Represents Copilot being used in the context of Forms. For example, Copilot could help create survey questions, quizzes, or analyze form responses. This would be the AI assistant helping content creation or summarization in Forms. | Microsoft 365 Copilot |
| Logic App | Copilot in Azure Logic Apps. | Microsoft 365 Copilot |
| Loop | **Copilot in Microsoft Loop.** This refers to Copilot assisting within the Microsoft Loop application or Loop components. The user might have Copilot generate or summarize content in a Loop workspace. For example, Copilot could help brainstorm in a Loop page, given Loop's collaborative canvas. This integration brings Copilot to the Loop app context. | Microsoft 365 Copilot |
| M365AdminCenter | **Copilot in Microsoft 365 Admin Center.** This refers to an AI assistant for IT administrators. In this scenario, Copilot could help an admin with tasks in the Microsoft 365 admin center. For example, answering questions about settings, generating PowerShell scripts, or summarizing user reports. | Microsoft 365 Copilot |
| M365App | **Business Chat via Microsoft 365 app (desktop or mobile).** Similar to the Office apphost, this denotes Business Chat launched from the **Microsoft 365 unified app** on Windows or mobile. It covers the scenario where a user uses the Office/Microsoft 365 app itself (outside a specific product like Word) to chat with Copilot across their data. | Microsoft 365 Copilot Chat |
| Microsoft Purview | **Security Copilot in Purview (Compliance).** The user is interacting with Copilot in the **Microsoft Purview** compliance portal. Copilot helps compliance officers and security teams triage and summarize issues related to data protection and governance. For example, Copilot can summarize a batch of Data Loss Prevention (DLP) alerts, highlight inside risk activities, or answer questions like "Have we had any policy violations in email this week?". It can work in both an embedded way (inside Microsoft Purview UI, summarizing whatever section you're on) and in a standalone Q&A way for Microsoft Purview data. This scenario brings AI to compliance workflows, making it faster to grasp risks and decide on actions. | Security Copilot |
| Office | **Business Chat via Office.com or Microsoft 365 app.** Indicates the Copilot Business Chat accessed through the Office.com or Microsoft 365 home app (web, desktop, or mobile). For example, when a user opens the "Copilot" chat on Office.com (microsoft365.com) or the Microsoft 365 mobile app to ask cross-domain questions. | Microsoft 365 Copilot Chat |
| OfficeCopilotNotebook | **Copilot Notebook (Microsoft 365).** Refers to the **Copilot Notebooks** feature in Microsoft 365 Copilot (a central AI-powered notebook). This scenario is when Copilot compiles or interacts with a **cross-application notebook** of content. Copilot Notebooks allow users to gather and generate information across multiple sources in a notebook interface. This AppHost appears when that notebook is used on the Office.com/Microsoft 365 side (outside of OneNote). | Microsoft 365 Copilot Chat |
| OfficeCopilotSearchAnswer | **Copilot answer in Microsoft 365 Search.** This value refers to Copilot generating an **AI-powered answer in the Office/Microsoft 365 search experience**. For instance, when a user searches on Office.com or SharePoint and Copilot provides a natural language answer (drawing from workplace data) instead of just search results. This is a Business Chat-like Q&A feature within the search context. | Microsoft 365 Copilot Chat |
| OneDrive | Also refers to the **Copilot in SharePoint** scenario, as described previously. | Microsoft 365 Copilot |
| OneNote | **Copilot in Microsoft OneNote.** The user is using Copilot inside OneNote notebooks. This in-app OneNote Copilot can summarize notes, generate plans or lists, or answer questions based on NoteNote content. Copilot "*supercharges your note-taking*" in OneNote, helping to create, recall, and organize information. | Microsoft 365 Copilot |
| OneNoteCopilotNotebook | **Copilot Notebook in OneNote.** Similar to the OfficeCopilotNotebook scenario, but specifically when the Copilot Notebook is accessed within OneNote. Microsoft introduced Copilot Notebooks integrated into OneNote, so this AppHost logs when a user uses the **AI-powered notebook inside OneNote** (bringing cross-data Copilot functionality into OneNote). | Microsoft 365 Copilot Chat |
| Outlook | **Copilot in Microsoft Outlook.** The user in engaging Copilot while using Outlook (desktop, web, or mobile). This typically means the Copilot is helping with email tasks. For example, drafting an email reply, summarizing a long email thread, or organizing an inbox. | Microsoft 365 Copilot Chat |
| OutlookOnCanvas | **Copilot inline in Outlook compose.** This refers to Copilot's assistance directly in the email canvas. For example, when composing an email, Copilot might autogenerate text right in the draft. It's the on-canvas helper in Outlook's compose window (as opposed to using a separate Copilot pane). | Microsoft 365 Copilot |
| OutlookSidepane | **Copilot in Outlook side pane.** Denotes the classic Outlook Copilot experience via the Copilot pane in Outlook. For example, a user opens the Copilot sidebar in Outlook to draft or summarize messages. This value explicitly captures that side pane interaction. | Microsoft 365 Copilot |
| Planner | **Copilot in Microsoft Planner.** Indicates a Copilot scenario in Planner, likely assisting with project plans or tasks. A user might ask Copilot to draft a plan, generate task checklists, or update task descriptions. | Microsoft 365 Copilot |
| Power BI | Copilot in Microsoft Power BI. | Microsoft 365 Copilot |
| PowerPoint | **Copilot in Microsoft PowerPoint.** Copilot is being used within a PowerPoint presentation. In this scenario, a user could ask Copilot to create slides, generate speaker notes, or redesign content in PowerPoint. | Microsoft 365 Copilot |
| PowerPointOnCanvas | **Copilot on PowerPoint slides.** Indicates an on-canvas Copilot experience in PowerPoint, where Copilot inserts or modifies content directly on slides. This could be the scenario of Copilot generating layouts or bulleted points straight into the presentation (without solely relying on the chat pane). It's a more embedded form of the PowerPoint Copilot. | Microsoft 365 Copilot |
| Security Copilot Standalone | **Security Copilot standalone experience.** The user is interacting with Security Copilot through the standalone experience, as opposed to interacting with Copilot through an embedded experience within Defender, Purview, etc. | Security Copilot |
| SharePoint | **Copilot in SharePoint.** Copilot is used within SharePoint (likely on a SharePoint site or page). For instance, a user might ask Copilot to summarize a SharePoint news post or draft content for a SharePoint page. This scenario corresponds to a SharePoint-integrated Copilot helping with intranet content. | Microsoft 365 Copilot |
| Stream | Copilot in Microsoft Stream. | Microsoft 365 Copilot |
| Teams | **Copilot in Microsoft Teams.** Represents Copilot usage inside the Microsoft Teams app (Web/Desktop/Mobile). This covers interactions with Copilot in Teams chats or channels. For example, asking Copilot to summarize a Teams chat, answer a question in a channel, or assist in a meeting context. This is essentially the Copilot experience within Teams' interface. For example, the "Chat Copilot" in a Teams chat thread. | Microsoft 365 Copilot |
| TeamsAdminPortal | **Copilot in Microsoft Teams Admin Center.** Similar to the M365AdminCenter scenario, this indicated a Copilot scenario in the Teams Admin Portal. An admin might use Copilot to configure Teams settings or generate reports. | Microsoft 365 Copilot |
| VivaEngage | **Copilot in Viva Engage (Viva Engage).** The user is interaction with Copilot within Viva Engage. For example, drafting a post or summarizing conversation threads in a Viva Engage community. This scenario covers any AI assistance inside Viva Engage, such as helping craft announcements or answers. | Microsoft 365 Copilot |
| VivaGoals | **Copilot in Viva Goals.** Viva Goals manages OKRs (objectives and key results). A Copilot here could draft OKRs, update progress, or analyze goal attainment. | Microsoft 365 Copilot |
| VivaPulse | **Copilot in Viva Pulse.** Viva Pulse is a feedback survey tool; Copilot here might draft survey questions or summarize sentiment from responses. | Microsoft 365 Copilot |
| Whiteboard | **Copilot in Microsoft Whiteboard.** The user is using Copilot on a digital whiteboard. Copilot in Whiteboard helps brainstorm and organize ideas on the whiteboard canvas. For example, suggesting ideas, clustering sticky notes, or summarizing the board's content. This scenario covers using Copilot during a Whiteboard session (in Teams or the Whiteboard app) to enhance creativity and structure. | Microsoft 365 Copilot |
| Word | **Copilot in Microsoft Word.** The user is interacting with Copilot within Word. For example, asking it to draft or edit portions of a Word document. This is the in-app **Word Copilot** (side-pane chat and commands in Word). Copilot can generate content, summarize text, or adjust formatting the document context. | Microsoft 365 Copilot |
| WordOnCanvas | **Copilot inline in Word's document.** This refers to Copilot assistance directly *on the canvas* in Word. Instead of the side pane, Copilot acts within the document editing area. For example, the feature where Copilot writes directly into the document or provides inline suggestions. It's essentially Word Copilot's capabilities applies within the document body, rather than via the chat pane. | Microsoft 365 Copilot |

### Example Copilot scenarios for user activities

The following tables list some example scenarios and how they appear in the audit log. These example audit logs come from Copilot activities.

#### Microsoft Copilot

A user interacts with Microsoft Copilot through the Microsoft 365 Copilot Chat client.

| Operation | RecordType | AppIdentity | AppHost |
| --- | --- | --- | --- |
| CopilotInteraction | CopilotInteraction | Copilot.MicrosoftCopilot.BizChat | BizChat |

#### Security Copilot

A user interacts with Security Copilot within Microsoft Defender.

| Operation | RecordType | AppIdentity | AppHost |
| --- | --- | --- | --- |
| CopilotInteraction | CopilotInteraction | Copilot.Security.SecurityCopilot | Defender |

#### Copilot Studio applications

A user interacts with a custom-built Copilot Studio application (whose appId is the GUID contained in appIdentity). The interaction takes place within Microsoft Teams, where this custom-built application is deployed.

| Operation | RecordType | AppIdentity | AppHost |
| --- | --- | --- | --- |
| CopilotInteraction | CopilotInteraction | Copilot.Studio.f4d97b45-1deb-40ce-9004-b473b79eab85 | Teams |

#### Microsoft Facilitator

Microsoft Facilitator updates AI Notes, Live Notes, or Meeting Moderation in Microsoft Teams.

| Operation | RecordType | AppIdentity | AppHost |
| --- | --- | --- | --- |
| AINotesUpdate | TeamCopilotInteraction | Copilot.TeamCopilot.AINotes | Teams |
| LiveNotesUpdate | TeamCopilotInteraction | Copilot.TeamCopilot.LiveNotes | Teams |
| LiveNotesUpdate | TeamCopilotInteraction | Copilot.TeamCopilot.MeetingModerator | Teams |
| TeamCopilotMsgInteraction | TeamCopilotInteraction | Copilot.TeamCopilot.Message | Teams |

### Identifying if Copilot accessed the web

When you enable web search, Microsoft 365 Copilot and Microsoft 365 Copilot Chat parse user prompts and determine whether web search would improve the quality of the response. To identify if Copilot referenced the public web in a user interaction, review the *AISystemPlugin.Id* property in the *CopilotInteraction* audit record. *AISystemPlugin.Id* contains the value *BingWebSearch* when user Copilot requests use the public web via Microsoft Bing for additional data.

## Accessing Copilot audit logs

Access Copilot audit logs by using the Microsoft Purview portal and selecting **Audit**.

To search for specific Copilot or AI application scenarios, use the **Activities – operation names** field in the Microsoft Purview portal to filter audit logs by properties like *Operation*, *RecordType*, and *Workload*.

If you need to search for audit logs containing a specific *AppIdentity* value or set of values, first search and export all relevant Copilot audit logs by filtering by operation name. From the exported search results, apply a filter on the *AppIdentity* property offline.

Audit logs for Microsoft Copilot and Microsoft Copilot Chat include the model provider and model name when a request is processed. This information can help support auditing, compliance, and governance requirements in organizations that enable multiple model providers.

For example, if a user selects a specific model instead of **Auto**, audit records might include entries similar to:

- `ModelProvider: OpenAI, ModelName: gpt-55-high`
- `ModelProvider: Anthropic, ModelName: claude-sonnet-4-6` And, if a user selects **Auto**, the model provider and model name might not be available for every request, such as when an internal model is used.

Currently, Cowork doesn't show provider details.
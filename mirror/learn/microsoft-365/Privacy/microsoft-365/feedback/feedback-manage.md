---
layout: Conceptual
title: Manage Microsoft feedback for your organization - Microsoft 365 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/privacy/microsoft-365/feedback/feedback-manage
breadcrumb_path: /privacy/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: danbrown
author: DHB-MSFT
manager: dansimp
ms.date: 2026-10-13T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: microsoft-365-business
ms.subservice: m365-privacy
ms.collection:
- M365-subscription-management
- Adm_O365
- Adm_TOC
- feedback-content
ms.custom: admindeeplinkMAC
description: Manage feedback your users can send to Microsoft about Microsoft products.
locale: en-us
document_id: 76640002-8d45-24e3-ccf8-b64e1b496161
document_version_independent_id: 76640002-8d45-24e3-ccf8-b64e1b496161
original_content_git_url: https://github.com/MicrosoftDocs/OfficeDocs-Privacy-pr/blob/live/Privacy/microsoft-365/feedback/feedback-manage.md
site_name: Docs
depot_name: office.OfficeDocs-Privacy
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: microsoft-365/feedback/feedback-manage
moniker_range_name: 
monikers: []
item_type: Content
source_path: Privacy/microsoft-365/feedback/feedback-manage.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: f30d50b9-25ac-3edc-cc6d-804a3e05d5cc
---

# Manage Microsoft feedback for your organization - Microsoft 365 | Microsoft Learn

As the admin of a Microsoft 365 organization, there are several policies to help you manage the feedback collection and the customer engagement experience of your users when using Microsoft 365 applications and Microsoft Copilot. All policies described in this article govern feedback for both Microsoft 365 applications and Microsoft Copilot. You can create and use existing Microsoft Entra groups in your organization for each of these policies. With these policies, you can control how different departments in your organization can send feedback to Microsoft.

Microsoft reviews all feedback submitted by customers. Microsoft uses this feedback to improve the product experiences for users, including by improving the quality of AI-generated responses and troubleshooting product issues. Keeping the feedback experiences enabled allows you to see what your users are saying about the Microsoft products they're using. The feedback we collect from your users is available in the [Microsoft 365 admin center](https://admin.microsoft.com).

Note

Microsoft acts as a data processor for your tenant's feedback. As the tenant administrator, you can manage your tenant's feedback in the Microsoft 365 admin center. For more information, see [How can I see my user's feedback?](feedback-overview#how-can-i-see-my-users-feedback)

To learn more about the types of feedback and how Microsoft uses user feedback, see [Learn about Microsoft feedback for your organization](feedback-overview).

The following table represents which apps and services are currently connected to the feedback policies shown in the Feedback policies table. For examples of in-product feedback and surveys, see [Feedback types](feedback-overview#feedback-types).

| **Apps & Services** | **In-product feedback** | **In-product surveys** | **Metadata collection** | **Customer engagement** |
| --- | --- | --- | --- | --- |
| Access | Yes | Yes | Yes | Yes |
| Clipchamp | Yes | Yes | Yes | No |
| Excel | Yes | Yes | Yes | Yes |
| Forms | Yes | Yes | Yes | Yes |
| Intune Company Portal (Android) | Yes | Yes | Yes | Yes |
| Microsoft Copilot | Yes | Yes | Yes | Yes |
| Microsoft Whiteboard | Yes | Yes | Yes | Yes |
| Microsoft365.com | Yes | Yes | Yes | Yes |
| OneNote | Yes | Yes | Yes | Yes |
| OneDrive | Some settings are managed by other controls. For more information, see [Prevent users from contacting Microsoft directly](/en-us/sharepoint/disable-contact-support-send-feedback). |  |  |  |
| Outlook | Yes | Yes | Yes | Yes |
| PowerPoint | Yes | Yes | Yes | Yes |
| Project | Yes | Yes | Yes | Yes |
| Publisher ^[\*]^ | Yes | Yes | Yes | Yes |
| SharePoint | Yes | Yes | Yes | Yes |
| Teams | Yes | Yes | Yes | Yes |
| Teams Rooms | Yes | Yes | Yes | No |
| To Do | Yes | Yes | Yes | Yes |
| Word | Yes | Yes | Yes | Yes |
| Visio | Yes | Yes | Yes | Yes |
| Viva Connections | Yes | No | Yes | Yes |
| Viva Engage | Yes | Yes | Yes | Yes |
| Viva Glint | Yes | Yes | Yes | Yes |
| Viva Insights | Yes | Yes | Yes | Yes |
| Viva Pulse | Yes | Yes | Yes | Yes |

Note

^[\*]^ Support for Microsoft Publisher ended on October 13, 2026. For more information, see [Microsoft Publisher will no longer be supported after October 2026](https://support.microsoft.com/publisher/microsoft-publisher-will-no-longer-be-supported-after-october-2026).

## Feedback policies

Important

If you're an admin in a United States government environment, see the Feedback policies in United States government environments section later in this article.

When the following policies are set to **Not Configured**, it has the same effect as if you set the policies to **Enabled**.

| **Policy name** | **Control summary** |
| --- | --- |
| Allow users to access feedback portal | Manage user access to the feedback portal where users can follow up on their feedback and participate in community feedback. Note: This policy is only available in [Cloud Policy service for Microsoft 365](/en-us/microsoft-365-apps/admin-center/overview-cloud-policy). This policy isn't available in Group Policy and doesn't have a corresponding registry key available to set the policy. |
| Allow users to submit feedback to Microsoft | Controls feedback entry points across applications. |
| Allow users to receive and respond to in-product surveys from Microsoft | Controls whether surveys appear within product. |
| Allow users to include screenshots and attachments when they submit feedback to Microsoft | Allows users to choose relevant files, screen recordings, and screenshots to help Microsoft better understand and troubleshoot their feedback. |
| Allow Microsoft to follow up on feedback submitted by users | Determines if user can share contact info with feedback/survey for follow-up by Microsoft. Also allows users to get notified of feedback status changes. Users can manage communications settings in the feedback portal. |
| Allow users to include log files and relevant content samples when feedback is submitted to Microsoft | Allows users to include Microsoft generated files such as additional log files and content samples when relevant to feedback they're submitting. Examples may include Microsoft Copilot prompt and response interactions. |

Note

To help [optimize your organization’s Microsoft Copilot experience](/en-us/microsoft-365/copilot/optimize-microsoft-365-configuration-settings), we recommend that you set the following two policies to **Enabled**:

- Allow users to submit feedback to Microsoft
- Allow users to include log files and relevant content samples when feedback is submitted to Microsoft

## Configure policies

To configure these policy settings, you can use Cloud Policy service for Microsoft 365. For more information, see [Overview of Cloud Policy service for Microsoft 365](/en-us/microsoft-365-apps/admin-center/overview-cloud-policy). You can search for "feedback" or "survey" within Cloud Policy UI to find the policy settings to configure them.

These policy settings are also available if you use Group Policy. To use these policy settings, download the most current version of the [Administrative Template files (ADMX/ADML)](https://www.microsoft.com/download/details.aspx?id=49030). You can find these policy settings under User Configuration\Policies\Administrative Templates\Microsoft Office 2016\Privacy\Trust Center.

Note

After you apply policies, it can take a few hours for the client applications to update.

## Feedback policies in United States government environments

The following information only applies to United States government customers using Microsoft 365 (or Office 365) Government Community Cloud (GCC), GCC High, or DoD offerings.

- Not all products currently support feedback collection in this environment, but we're working to implement that support. To prepare for feedback collection, we recommend you review and configure the policy settings in the way that's appropriate for your organization.
- The behavior of the **Allow users to submit feedback to Microsoft** policy differs from commercial tenants. When the policy is **Not configured** (the default), users can submit restricted feedback only. Setting the policy to **Enabled** allows users to submit verbatim feedback, while setting it to **Disabled**prevents users from submitting feedback entirely.
    - Restricted feedback: Users can't provide written comments but can only provide predefined feedback such as giving a thumbs up/down rating or selecting an issue type from a list of likely issues.
    - Verbatim feedback: Users can submit more detailed feedback that includes optional written comments.
- No diagnostic logs, prompts, responses, screenshots, attachments, or user files are collected in any configuration in United States government environments.
- The Feedback portal and in-product surveys aren't available in this environment, so setting these policies don't have any effect at this time.
- While the following policies are available to change, changes will have no effect and those policies will always be treated as **Disabled**:
    - Allow users to include screenshots and attachments when they submit feedback to Microsoft.
    - Allow Microsoft to follow up on feedback submitted by users.
    - Allow users to include log files and relevant content samples when feedback is submitted to Microsoft.
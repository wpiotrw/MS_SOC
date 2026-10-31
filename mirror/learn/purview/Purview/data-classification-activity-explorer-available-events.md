---
layout: Conceptual
title: Labeling actions reported in Activity explorer | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-classification-activity-explorer-available-events
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2024-12-16T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.collection:
- purview-compliance
- m365solution-mip
- m365initiative-compliance
- highpri
search.appverid:
- MOE150
- MET150
description: A list of labeling activities that are available in Activity explorer.
locale: en-us
document_id: 5321fc16-5e3b-bcb1-d936-7cd0de252efa
document_version_independent_id: 5321fc16-5e3b-bcb1-d936-7cd0de252efa
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-classification-activity-explorer-available-events.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-classification-activity-explorer-available-events
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-classification-activity-explorer-available-events.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/3e34b70d-bca0-4369-a01b-71d1edfd427b
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/8ca32b3f-fa14-46df-b09a-9c4a591d6396
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
platformId: 7642c3c5-ddb4-a7e7-68c2-5dc86e0e3048
---

# Labeling actions reported in Activity explorer | Microsoft Learn

## Sensitivity label applied

This event is generated each time you label an unlabeled document or send an email with a sensitivity label.

- Activity explorer captures this event when you save a labeled document in native Microsoft Office applications and web applications.
- It captures this event when you apply a label for the Microsoft Purview Information Protection client.
- You can also monitor upgrade and downgrade label actions through the *Label event type* field and filter.

| Source | Reported in Activity explorer | Note |
| --- | --- | --- |
| Word, Excel, PowerPoint | Yes |  |
| Outlook | Yes | If you apply a sensitivity label to any email in an email thread, the same label is automatically applied to subsequent replies on the thread. These labeling events appear in activity explorer as automatic labeling events, even when automatic labeling isn't configured. |
| SharePoint, OneDrive | Yes |  |
| Exchange | Yes |  |
| Microsoft Purview Information Protection client and scanner | Yes | The *new label* action maps to *label applied* in activity explorer |
| Microsoft Information Protection (MIP) SDK | Yes | The *new label* action maps to *label applied* in activity explorer |
| Rights Management Service (RMS) | Not applicable |  |
| Power BI desktop and web | No | Accessible in the Microsoft 365 audit logs |
| Microsoft Defender for Cloud Apps | No |  |

## Sensitivity label changed

This event is generated each time a sensitivity label is updated on the document or email.

- For the Microsoft Purview Information Protection client and scanner, and MIP SDK sources, the *upgrade label* and *downgrade label* action maps to Activity explorer *label changed*.
- The event is captured when the action is saved in native Microsoft Office applications and web applications.
- The event is captured when the action occurs for the Microsoft Purview Information Protection client and scanner enforcements.
- You can also monitor upgrade and downgrade labels actions via the *Label event type* field and filter. The *justification* text is also captured, except for SharePoint and OneDrive.
- Sensitivity labeling in Microsoft Office apps: Outlook collects the last action that was generated before *file save*/*email send* actions. For example, if the user changes label on an email multiple times before sending, the last label found on the email when it is sent is captured in the audit log and then reported in activity explorer.

| Source | Reported in Activity explorer | Note |
| --- | --- | --- |
| Word, Excel, PowerPoint | Yes |  |
| Outlook | Yes |  |
| SharePoint, OneDrive | Yes |  |
| Exchange | Yes |  |
| Microsoft Purview Information Protection client | Yes |  |
| Microsoft Purview Information Protection scanner | Yes |  |
| MIP SDK | Yes |  |
| RMS service | Not applicable |  |
| Power BI desktop and Web | No | Accessible in the Microsoft 365 audit logs |
| Microsoft Defender for Cloud Apps | No |  |

## Sensitivity label removed

This event is generated each time you remove a sensitivity label from a file or document.

- Microsoft Office applications and web applications capture this event when you save the document.
- Microsoft Purview Information Protection client captures this event when you remove the label.
- Sensitivity labeling in Microsoft Office: Outlook collects the last labeling event that was generated before *file save*/*email send* actions.

| Source | Reported in Activity explorer | Note |
| --- | --- | --- |
| Word, Excel, PowerPoint | Yes |  |
| Outlook | Yes |  |
| SharePoint, OneDrive | Yes |  |
| Exchange | Yes |  |
| Microsoft Purview Information Protection client | Yes | The *remove label* action is mapped to the *label removed* action in activity explorer |
| Microsoft Purview Information Protection scanner | Yes | The *remove label* action is mapped to the *label removed* action in activity explorer |
| MIP SDK | Yes | The *remove label* action is mapped to the *label removed* action in activity explorer |
| RMS service | Not applicable |  |
| Power BI desktop and Web | No | Accessible in the Microsoft 365 audit logs |
| Microsoft Defender for Cloud Apps | No |  |

## Sensitivity label file read

This event is generated each time a sensitivity labeled or protected document is opened.

| Source | Reported in Activity explorer | Note |
| --- | --- | --- |
| Word, Excel, PowerPoint | Yes |  |
| Outlook | No |  |
| SharePoint, OneDrive | No |  |
| Exchange | No |  |
| Microsoft Purview Information Protection client | Yes | The *access* action maps to the *file read* action in activity explorer |
| Microsoft Purview Information Protection scanner | Yes | The *access* action maps to the *file read* action in activity explorer |
| MIP SDK | Yes | The *access* action maps to the *file read* action in activity explorer |
| RMS service | Yes | The *access* action maps to the *file read* action in activity explorer |
| Power BI desktop and Web | No | Accessible in the Microsoft 365 audit logs |
| Microsoft Defender for Cloud Apps | No |  |

## Files discovered

The Microsoft Purview Information Protection scanner generates this event each time it discovers files while scanning sensitive data in various locations.

| Source | Reported in Activity explorer | Note |
| --- | --- | --- |
| Word, Excel, PowerPoint | Not applicable |  |
| Outlook | Not applicable |  |
| SharePoint, OneDrive | Not applicable |  |
| Exchange | Not applicable |  |
| Microsoft Purview Information Protection client | Not applicable |  |
| Microsoft Purview Information Protection scanner | Yes | The *discover* action maps to the *files discovered* action in activity explorer |
| MIP SDK | Yes | The *discover* action maps to the *file discovered* action in Activity explorer |
| RMS service | Not applicable |  |
| Power BI desktop and Web | Not applicable |  |
| Microsoft Defender for Cloud Apps | Not applicable |  |

## Sensitivity label file renamed

This event is generated each time you rename a document with a sensitivity label.

| Source | Reported in Activity explorer | Note |
| --- | --- | --- |
| Word, Excel, PowerPoint | Yes |  |
| Outlook | Not applicable |  |
| SharePoint, OneDrive | No |  |
| Exchange | Not applicable |  |
| Microsoft Purview Information Protection client | No |  |
| Microsoft Purview Information Protection scanner | No |  |
| MIP SDK | No |  |
| RMS service | No |  |
| Power BI desktop and Web | No |  |
| Microsoft Defender for Cloud Apps | No |  |

## File removed

The Microsoft Purview Information Protection scanner generates this event each time it detects that a previously scanned file is removed.

| Source | Reported in Activity explorer | Note |
| --- | --- | --- |
| Word, Excel, PowerPoint | Not applicable |  |
| Outlook | Not applicable |  |
| SharePoint, OneDrive | Not applicable |  |
| Exchange | Not applicable |  |
| Microsoft Purview Information Protection client | Not applicable |  |
| Microsoft Purview Information Protection scanner | Yes |  |
| MIP SDK | Not applicable |  |
| RMS service | Not applicable |  |
| Power BI desktop and Web | Not applicable |  |
| Microsoft Defender for Cloud Apps | Not applicable |  |

### Protection applied

This event is generated the first time you manually add protection to an item that doesn't have a label.

| Source | Reported in Activity explorer | Note |
| --- | --- | --- |
| Word, Excel, PowerPoint | No |  |
| Outlook | No |  |
| SharePoint, OneDrive | Not applicable |  |
| Exchange | No |  |
| Microsoft Purview Information Protection client | Yes |  |
| Microsoft Purview Information Protection scanner | Not applicable |  |
| MIP SDK | Yes |  |
| RMS service | Not applicable |  |
| Power BI desktop and Web | Not applicable |  |
| Microsoft Defender for Cloud Apps | Not applicable |  |

## Protection changed

This event is generated each time you manually change the protection on an unlabeled document.

| Source | Reported in Activity explorer |
| --- | --- |
| Word, Excel, PowerPoint | No |
| Outlook | No |
| SharePoint, OneDrive | Not applicable |
| Exchange | No |
| Microsoft Purview Information Protection client | Yes |
| Microsoft Purview Information Protection scanner | Not applicable |
| MIP SDK | Yes |
| RMS service | Not applicable |
| Power BI desktop and Web | Not applicable |
| Microsoft Defender for Cloud Apps | Not applicable |

## Protection removed

This event is generated each time you manually change the protection on an unlabeled document.

| Source | Reported in Activity explorer |
| --- | --- |
| Word, Excel, PowerPoint | No |
| Outlook | No |
| SharePoint, OneDrive | Not applicable |
| Exchange | No |
| Microsoft Purview Information Protection client | Yes |
| Microsoft Purview Information Protection scanner | Not applicable |
| MIP SDK | Yes |
| RMS service | Not applicable |
| Power BI desktop and Web | Not applicable |
| Microsoft Defender for Cloud Apps | Not applicable |

## Data loss prevention (DLP) policy matched

This event is generated each time a DLP policy matches a document or an email.

| Source | Reported in Activity explorer |
| --- | --- |
| Exchange | Yes |
| SharePoint | Yes |
| OneDrive | Yes |
| Teams | Yes |
| Windows 10, Windows 11, and macOS devices | Yes |
| MAC | No |
| On-premises | No |
| Microsoft Defender for Cloud Apps | No |

The Endpoint DLP events for devices running Windows 10, Windows 11, and any of the three most recently released major versions of macOS are:

- File deleted
- File created
- File copied to clipboard
- File modified
- File read
- File printed
- File renamed
- File copied to network share
- File accessed by unallowed app

## Retention label applied

This event is generated each time you label an unlabeled document or send an email with a retention label.

- The event is captured when you save a document or send an email.

| Source | Reported in Activity explorer |
| --- | --- |
| Exchange | No |
| SharePoint | Yes |
| OneDrive | Yes |

## Retention label changed

This event is generated each time you update a label on a document or email.

- The event is captured when you save a document or send an email.

| Source | Reported in Activity explorer |
| --- | --- |
| Exchange | No |
| SharePoint | Yes |
| OneDrive | Yes |

## Retention label removed

This event is generated each time you remove a label from a file or document.

- The event is captured when you save a document or send an email.

| Source | Reported in Activity explorer |
| --- | --- |
| Exchange | No |
| SharePoint | Yes |
| OneDrive | Yes |

## Considerations

- When the recommended label tool tip appears to an end user, the event isn't captured. However, if the user chooses to apply the recommended label, the label appears under the *How applied* field as *Recommended*.
- Sensitive information types aren't currently available for auto-labeling activities from Word, Excel, PowerPoint, and Outlook, SharePoint, and OneDrive.
- When you label items with a sensitivity label and then delete that label, any events involving those items still appear in activity explorer. Instead of showing the name of the deleted sensitivity label, the GUID of the deleted sensitivity label appears.
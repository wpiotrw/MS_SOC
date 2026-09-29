---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Engagements in the Microsoft 365 Admin Center Enhanced engagements section - Microsoft 365 Enterprise | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-admin-engagements?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: true
uhfHeaderId: MSDocsHeader-M365-IT
f1.keywords:
- NOCSH
ms.author: vpattnaik
author: vpattnai
manager: dansimp
ms.date: 2026-08-27T00:00:00.0000000Z
audience: Admin
ms.reviewer: dansimp
ms.topic: article
ms.service: microsoft-365-enterprise
ms.localizationpriority: medium
ms.collection:
- m365admin
description: The Engagements section in Enhanced engagements offers a centralized overview of all customer-specific engagements with Microsoft.
ai-usage: ai-assisted
locale: en-us
document_id: a8e5e9ce-a5ba-15d3-e3d2-a61fe13d1460
document_version_independent_id: a8e5e9ce-a5ba-15d3-e3d2-a61fe13d1460
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/enterprise/microsoft-365-admin-engagements.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../admin/toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/microsoft-365-admin-engagements
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/enterprise/microsoft-365-admin-engagements.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
platformId: f016f200-ef1e-082f-6d2b-e4f432ca9c6b
---

# Engagements in the Microsoft 365 Admin Center Enhanced engagements section - Microsoft 365 Enterprise | Microsoft Learn

The Engagements pivot in Enhanced engagements offers a centralized overview of all customer-specific engagements with Microsoft. This section allows users to request and track engineering-led escalations, post-incident analyses, and Customer Advisory Board (CAB) discussions. Each engagement type provides detailed insights, status updates, and filtering options to help manage support efficiently.

[![Screenshot of engagements landing page in enhanced engagements portal.](media/enhanced-engagements/enhanced-engagements-mcs.png)](media/enhanced-engagements/enhanced-engagements-mcs.png#lightbox)

## Service Requests

The Service Requests view under Engagements provides visibility into all service requests raised for your tenant. This view helps monitor escalation activity, review trends, and gain insights into how issues are distributed across products, severity levels, and sources. You can also use the Nudge feature to gain additional traction from Microsoft.

**Nudge**: This option allows you to request additional support for an active service request when urgency, clarity, or escalation is needed. Use it when the issue affects business operations, impacting key users, requires more attention, or the current progress isn't meeting expectations.

To submit a request, follow these steps:

1. Select a reason using one of the available radio button options.
2. Provide additional context in the description text box to help us understand the urgency, impact, or scenario.
3. Attach any supporting files (optional) to help clarify the request (screenshots, logs, documentation).
4. Choose a primary point of contact who Microsoft can follow up with for additional details or alignment.
5. Once complete, select **Submit** to send the request to our support team for review.
6. Once submitted, the request will be reviewed, and our team will contact you using the email you provide assistance with the issue.

[![Screenshot of nudge feedback form in enhanced engagements portal.](media/enhanced-engagements/nudge-enhanced-engagements.png)](media/enhanced-engagements/nudge-enhanced-engagements.png#lightbox)

### Nudge Status

After submitting a nudge in Enhanced engagements, you can monitor its progress through three stages. The status provides end-to-end tracking for each Nudge directly within the MCS Portal.

1. **Nudge Initiated -** The request has been submitted and is in progress.
2. **Nudge Acknowledged -** The request has been reviewed by the appropriate engineering or support team.
3. **Nudge Actioned -** The request has been addressed and actions have been completed.

[![Screenshot of nudge status update in enhanced engagements portal.](media/enhanced-engagements/nudge-status.png)](media/enhanced-engagements/nudge-status.png#lightbox)

It also shows who most recently nudged the request and when, making the process more transparent and accountable.

[![Screenshot of nudge status change in enhanced engagements portal.](media/enhanced-engagements/nudge-user-update.png)](media/enhanced-engagements/nudge-user-update.png#lightbox)

### View nudge history and follow-up nudges

For an open service request, select the request title to open the details pane. Closed service requests appear as plain text and don't open a details pane.

[![Screenshot of Service Requests report for an M365 tenant.](media/enhanced-engagements/escalation-list-nudge-status.png)](media/enhanced-engagements/escalation-list-nudge-status.png#lightbox)

In **Overview**, you can review:

| Field | Description |
| --- | --- |
| **Nudge status** | The current aggregate state of the nudge: Initiated, Acknowledged, or Actioned. |
| **Number of nudges** | The total count of nudges submitted for the service request, including follow-up nudges. |
| **Last nudged by** | The user who submitted the most recent nudge. |
| **Last nudged time** | The date and time of the most recent nudge, shown in your local time zone. |

Expand **Nudge timeline** to view nudge activity from oldest to newest. The timeline can include the following entries:

| Timeline entry | Meaning |
| --- | --- |
| **Nudge initiated by &lt;user&gt;** | The first nudge in the current nudge cycle was submitted. |
| **Re-nudged by &lt;user&gt;** | Another nudge was submitted before the current nudge cycle was resolved. |
| **Nudge acknowledged** | The appropriate Microsoft support or engineering team acknowledged the nudge. |
| **Nudge resolved** | The nudge was addressed. When this entry appears in gray, it's the expected next event. |

A check mark identifies a completed event, a filled marker identifies the current event, and a gray marker identifies the expected next event.

[![Screenshot of nudge timeline showing an initial nudge, three follow-up nudges, acknowledgement, and Nudge resolved.](media/enhanced-engagements/enhanced-engagements-nudge-timeline.png)](media/enhanced-engagements/enhanced-engagements-nudge-timeline.png#lightbox)

To request additional attention before the current nudge is resolved, select **Nudge** again. The follow-up action appears in the timeline as **Re-nudged by &lt;user&gt;** with its own timestamp.

Note

Sending another nudge doesn't create a new status. If you nudge again while the status is **Nudge Acknowledged**, the status remains **Nudge Acknowledged** while the nudge count and latest-nudge details are updated. A **Nudge resolved** event ends the current cycle - if the service request is nudged again afterward, that nudge starts a new cycle and appears as **Nudge initiated by &lt;user&gt;**.

### Benefits of Nudge status updates

This enhancement helps to:

- Increase transparency into Nudge request handling.
- Reduce uncertainty around request status.
- Help administrators determine whether additional follow-up is needed by providing visibility into previous nudge activity.

### Overview of Service Requests

At the top of the page, several visual summaries provide quick insights into your tenant's escalation activity:

- **Total escalations** - The total number of escalations associated with your tenant.
- **Open escalations** - The number of currently active or unresolved escalations.
- **Escalations by product** - A workload-based view that shows how many escalations relate to services such as Microsoft Exchange, SharePoint, or Teams.
- **Customer raised escalations** - Displays the number of escalations initiated directly by your organization.
- **Distribution by escalation source** - A chart showing whether escalations were raised by your organization or Microsoft Support.
- **Distribution by severity** - Summarizes escalations by severity level (Severity 1, A, B, or C).
- **Escalations per week by status** - A trend chart showing how many escalations were created and closed each week.

Note

These insights update automatically as new escalations are raised or resolved.

### Service Request report

Below the overview section, the service request report provides a detailed, filterable table of all active and historical escalations for your tenant. You can use this table to review case progress, assigned severity, and escalation sources.

You can:

- **Search** by title, ticket number, or keywords.
- **Filter** by status, product, severity, or escalation source.
- **Refresh** the data to view the most recent updates.
- **Export** the results for reporting or analysis.

| Column | Description |
| --- | --- |
| **Title** | The name or brief summary of the service request. |
| **Created by** | The user who initiated the service request. |
| **Ticket** | The unique service request identifier. |
| **Severity** | Indicates the service request's priority (for example, *A*, *B*, *C*, or *1*). |
| **Escalation date** | When the service request was created. |
| **Status** | The current state of the service request (*Open*, *Closed*, *In Progress*). |
| **Escalation source** | Identifies whether the service request originated from your organization or from Microsoft Support. |

Tip

Combine filters and charts to spot recurring service request trends or identify products that require the most attention.

### Benefits of Service Requests

The Service Requests view helps your organization:

- Maintain visibility into engineering-level service requests.
- Understand patterns across products and severity levels.
- Identify and manage high-impact issues efficiently.
- Improve collaboration with Microsoft support and engineering teams.

## Critical Project Assistance (CPAs)

The Critical Project Assistance (CPA) feature in the Enhanced Engineering portal enables organizations to notify Microsoft about upcoming business activities or infrastructure changes that might impact their Microsoft 365 services. During these periods, Microsoft's Service Engineering team provides elevated monitoring and proactive engagement to help identify and mitigate potential risks.

[![Screenshot of critical project assistance in enhanced engagements portal.](media/enhanced-engagements/critical-project-assistance.png)](media/enhanced-engagements/critical-project-assistance.png#lightbox)

Examples of qualifying projects include:

- Major datacenter or network changes
- Mergers, acquisitions, or divestitures
- Large-scale product launches or migrations
- Tenant rebranding or restructuring

### Submit a new CPA request

If you're planning a significant business event, you can submit a CPA request to inform Microsoft's Service Engineering team in advance. For a meaningful engagement, kindly notify us about your critical project at least 10 business days before the event.

[![Screenshot of critical project assistance intake form.](media/enhanced-engagements/cpa-intake-form.png)](media/enhanced-engagements/cpa-intake-form.png#lightbox)

1. In the **Enhanced engagements** section, go to **Engagements** &gt; **CPAs**.
2. Select **Submit new CPA**.
3. Enter the required details about your planned activity, including:

    - Project title and Project details
    - Start and end dates
    - Products (for example, Exchange, SharePoint, Teams)
    - Primary contact information
4. Review your information and select **Submit**.

Once submitted, your request will appear in the CPA overview table with its current status.

### CPA overview

The CPA overview section provides a summary of all CPA requests submitted for your tenant.

It includes:

- **Total CPAs** and **Active CPAs**
- **Active CPAs by workload** (Exchange, SharePoint, Teams)
- A searchable and filterable list of CPA requests

You can:

- **Filter** CPAs by status or workload
- **Export** CPA data for reporting or tracking
- **Refresh** the view to see the latest submissions

Each CPA entry includes key details:

| Column | Description |
| --- | --- |
| **Project title** | Name of the submitted business activity |
| **Ticket ID** | Unique identifier for the CPA request |
| **Start/ End date** | Duration of the planned event |
| **Product** | Microsoft 365 workload impacted |
| **Created by** | Person who submitted the CPA |
| **Contact** | Primary contact for follow-up |
| **Status** | Current state of the request (for example, *Submitted*, *In review*, *Closed*) |

By clicking the project title, a flyout would be shown form right side of the portal, which would allow you to view CPA request details (for example, project details).

[![Screenshot of critical project assistance title page.](media/enhanced-engagements/cpa-request-title.png)](media/enhanced-engagements/cpa-request-title.png#lightbox)

### Active CPAs by workload

The **Active CPAs by Workload** chart provides a quick visual summary of ongoing CPA engagements by product area. This helps you identify which workloads currently have active awareness requests and plan accordingly.

## Customer Advisory Board (CAB)

The Customer Advisory Board offers you a prioritized voice into the evolution of Microsoft 365 through various virtual and in-person engagements with engineering, designed to facilitate roadmap discussions and feedback loops into all in-scope product teams.

[![Screenshot of customer advisory board in enhanced engagements portal.](media/enhanced-engagements/customer-advisory-board.png)](media/enhanced-engagements/customer-advisory-board.png#lightbox)

### CAB overview

The CAB overview section provides quick access to recent and upcoming engagement details.

- **Last completed event** - Displays the most recent in-person CAB event and links to its feedback form.
- **Upcoming CAB event** - Shows the next scheduled in-person CAB session.
- **Last completed community call** - Displays the most recent virtual community call and provides a feedback link.
- **Upcoming community call** - Highlights the next scheduled community call.

If a CAB event or call hasn't been scheduled yet, the corresponding date and details won't be displayed. These fields automatically update once new schedule information becomes available. If a CAB event or call hasn't been scheduled yet, the corresponding date and details won't be displayed. These fields automatically update once new schedule information becomes available.

Note

CAB event and call details are refreshed periodically. When no upcoming events are listed, it means the schedule is still being finalized and will appear once available.

### Upcoming CAB schedule

The **Upcoming CAB schedule** lists all planned engagements with Microsoft 365 engineering teams. Each entry provides event details, topics, audience, and registration information.

You can:

- **View** upcoming and past CAB sessions.
- **Export** the schedule for tracking and internal coordination.
- **Register** for upcoming sessions directly from the portal.

Each schedule entry includes:

| Column | Description |
| --- | --- |
| **Column** | Start and end dates for the CAB engagement |
| **Dates** | Title of the CAB session or community call |
| **Event** | Microsoft 365 workload impacted |
| **Topic** | Key discussion areas (for example, product roadmap updates, feature deep dives) |
| **Audience** | Recommended participants (for example, CIOs, CTOs, IT Admins) |
| **Registration Info** | Direct registration links or invitation details |

Tip

If registration details aren't available for an upcoming event, check back later. The information will appear automatically once registration links are available.

### Benefits of CAB

The Customer Advisory Board program allows you to:

- Engage directly with Microsoft engineering teams.
- Preview and provide feedback on [Microsoft AI at Work Roadmap](https://www.microsoft.com/microsoft-365/roadmap), formerly known as the Microsoft 365 Roadmap, plans.
- Network with peers across industries facing similar challenges.
- Influence future product and service enhancements.

## Incident Analysis

The Incident Analysis page in Enhanced engagements allows you to request incident analysis for closed incidents. You can submit a request for incidents that have been critical in nature and resolved in the last 7 days. In addition, you can view insights into your current incident analysis requests, including their status, and see a report of all past requests.

[![Screenshot that shows a dashboard with sections for engaging in incident analysis, requesting analysis for closed critical incidents, and submitting a new incident request.](../media/enhanced-engagements/incident-analysis-engagements.png)](../media/enhanced-engagements/incident-analysis-engagements.png#lightbox)

### Create an Incident Analysis request

To submit an incident analysis request:

1. Go to the **Incident Analysis** page and navigate to the Incident Analysis section under **Engagements**.
2. Select **Create a new request**. A flyout menu will open, showing a list of eligible incidents that can be selected for incident analysis.
3. Select a case. In the flyout menu, choose an incident by selecting the ticket number from the available list.
4. Review case details after selecting an incident where you'll also see additional details related to the ticket. Follow the prompts to complete your analysis request.
5. If it's a Copilot issue, check the box.
6. Submit your request. Once you've reviewed the information, submit your incident analysis request.

    [![Screenshot that shows a selection interface for submitting an incident analysis, with a list of technical issue categories such as Exchange, SharePoint, and Copilot for Microsoft 365.](../media/enhanced-engagements/submit-incident-analysis.png)](../media/enhanced-engagements/submit-incident-analysis.png#lightbox)

Alternatively, you can do the following:

1. If you do not see your incident listed, select **Don't see your incident**.
2. A flyout menu will open. Provide your case number and contact details, explain why this case should qualify for Incident Analysis, and outline the specific information you seek if eligible.
3. Submit your request. All requests will be reviewed by a Technical Customer Lead (TCL).

    [![Screenshot that shows a form for submitting an Incident Analysis request, including fields for case number, contact information, description, and a submit button.](../media/enhanced-engagements/manually-submit-request-incident-analysis.png)](../media/enhanced-engagements/manually-submit-request-incident-analysis.png#lightbox)

### Incident Analysis Overview

The Incident Analysis (IA) overview section provides a snapshot of the current state of your incident analysis requests:

- **Total IAs**: Displays the total number of open incident analysis requests.
- **Active IAs**: Shows the number of active requests that are being worked on.

### Active IAs by workload

This section breaks down your active incident analysis requests by workload type:

- **Exchange**: The number of active analysis requests related to Exchange incidents.
- **SharePoint**: The number of active analysis requests related to SharePoint incidents.
- **Teams**: The number of active analysis requests related to Teams incidents.
- **Copilot for M365**: The number of active analysis requests related to Copilot incidents

### Incident analysis filters

You can refine your view of the incident analysis requests by using the following filters:

- **Status**: Filter by the status of the request (for example, *Submitted*, *Completed*).
- **Created By**: Filter by the user who created the request.
- **Product**: Filter by the product associated with the incident (for example, *Exchange*, *SharePoint*, *Teams*, *Copilot for M365*).

### Request Report

The **Request Report** section displays a table with all the incident analysis requests that have been submitted. For each request, you can see the following details:

- **Ticket #**: The unique identifier for the incident.
- **Case Title**: The title of the incident request.
- **Status**: The current status of the request (for example, *Submitted*, *Completed*).
- **Created By**: The user who created the request.
- **Date Created**: The date when the request was created.
- **Product**: The product associated with the incident (for example, *Exchange*, *SharePoint*, *Teams, Copilot for M365*).

## Navigation and Pagination

The request report is displayed in a paginated table format. You can navigate through the pages of requests by using the pagination controls at the bottom of the table:

- **Next** and **Previous** arrows allow you to move between pages.
- The **Items per page** selector lets you adjust how many requests are displayed on each page.
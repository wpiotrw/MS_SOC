---
layout: Conceptual
title: Automatically apply a retention label to Microsoft 365 items | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/apply-retention-labels-automatically
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
manager: laurawi
ms.date: 2026-02-26T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-records-management
ms.collection:
- purview-compliance
- SPO_Content
- m365copilot
search.appverid:
- MOE150
- MET150
description: Create auto-labeling retention policies so you can automatically apply labels to retain what you need and delete what you don't
locale: en-us
document_id: b0f44eb6-740f-9145-dbe4-548a6426e024
document_version_independent_id: b0f44eb6-740f-9145-dbe4-548a6426e024
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/apply-retention-labels-automatically.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: apply-retention-labels-automatically
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/apply-retention-labels-automatically.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/7428317a-e6c2-4461-ad3e-8a8ad3608734
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://authoring-docs-microsoft.poolparty.biz/devrel/e4f59707-f107-48f2-8d75-0afd91868cd7
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
platformId: b1ce1dce-ecf4-5d69-4716-7b82382aa321
---

# Automatically apply a retention label to Microsoft 365 items | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

Note

This scenario isn't supported for [regulatory records](records-management#records) or default labels for an organizing structure such as a document set or library in SharePoint, or a folder in Exchange. These scenarios require a [published retention label policy](create-apply-retention-labels).

One of the most powerful features of [retention labels](retention) is the ability to apply them automatically to content that matches specified conditions. In this case, people in your organization don't need to apply the retention labels. Microsoft 365 does the work for them.

Auto-applying retention labels are powerful because:

- You don't need to train your users on all of your classifications.
- You don't need to rely on users to classify all content correctly.
- Users no longer need to know about data governance policies - they can focus on their work.

You can apply retention labels to content automatically when that content doesn't already have a retention label applied and contains sensitive information, keywords or searchable properties, or a match for [trainable classifiers](trainable-classifiers-get-started-with). You can also automatically apply a retention label to cloud attachments that are stored in SharePoint or OneDrive.

Tip

Use searchable properties to identify Teams meeting transcripts or recordings with accompanying transcripts and items that have a sensitivity label applied.

The processes to automatically apply a retention label based on these conditions:

![Diagram of roles and tasks for auto-apply labels.](media/32f2f2fd-18a8-43fd-839d-72ad7a43e069.png)

Use the following instructions for the two admin steps.

Note

Auto-policies use service-side labeling with conditions to automatically apply retention labels to items. You can also automatically apply a retention label with a label policy when you do the following:

- Apply a retention label to a Microsoft Syntex model
- Apply a default retention label for SharePoint and Outlook
- Apply a retention label to email by using Outlook rules

For these scenarios, see [Publish retention labels and apply them in apps](create-apply-retention-labels).

## Learn about simulation mode

You can run an auto-labeling policy in simulation mode when it's configured for either of the following conditions:

- Specific types of sensitive information
- Specific keywords or searchable properties that match a query you create

Very similar to [simulation mode for auto-labeling policies for sensitivity labels](apply-sensitivity-label-automatically#learn-about-simulation-mode), this addition lets you run the auto-labeling deployment like the WhatIf parameter for PowerShell. You see results reported as if the auto-labeling policy applied your selected label, using the conditions that you defined. You can then refine your conditions for accuracy if needed, and rerun the simulation.

Simulation mode also lets you gradually increase the scope of your auto-labeling policy before deployment. For example, you might start with a single location, such as a SharePoint site, with a single document library. Then, with iterative changes, increase the scope to multiple sites, and then to another location, such as OneDrive.

Typical workflow for an auto-labeling policy:

1. Create and configure an auto-labeling retention policy.
2. Run the policy in simulation mode, and wait for it to complete.
3. Review the results, and if necessary, refine your policy and rerun simulation. Wait for it to complete again.
4. Repeat step 3 as needed.
5. Deploy in production by turning on the policy.

Unlike simulation mode for automatically applying sensitivity labels:

- Simulation mode is optional, and not required to complete before you turn on the policy. You can even turn on the policy while simulation is still running.
- When simulation completes, the results automatically expire within seven days. Then, to view samples for your policy, you must restart the simulation.

Other considerations for simulation mode for auto-apply retention label policies:

- A maximum of 30 simulation jobs can be active in a 12-hour time period.
- A maximum of 100 item samples can be collected per mailbox.
- If you use [adaptive scopes](retention#adaptive-or-static-policy-scopes-for-retention)for your policy:
    - A maximum of 20,000 locations (any combination of sites and mailboxes) is supported.
    - Because these scopes use dynamic queries that run daily and can take a few days to fully populate, wait and [confirm their membership](purview-adaptive-scopes#view-adaptive-scope-membership-details) before you start simulation.
    - For the **Microsoft 365 Group mailboxes & sites** location, items stored in [AuxPrimary mailboxes](/en-us/powershell/module/exchange/get-mailboxlocation#-mailboxlocationtype) aren't supported.
- You might need to be assigned additional permissions to see the simulation results. For information about the required roles, see the next section, Before you begin.
- Simulation counts all items matching the policy criteria at time of simulation. However, when the policy is turned on, only content that isn't already labeled is eligible for auto-applying retention labels.
- Although auto-labeling for sensitive information types applies to emails sent and received rather than emails stored in mailboxes, simulation for Exchange locations runs against emails stored in mailboxes. Using historical data lets you more quickly assess the effectiveness of your chosen sensitive information types and configuration.
- For the **Microsoft 365 Group mailboxes & sites** and **OneDrive accounts** locations: Items that are stored in [arbitration mailboxes](/en-us/powershell/module/exchange/new-mailbox#-arbitration) aren't supported for simulation.
- Because simulation results are based on items available in the specified locations at the time the simulation job runs, remember to take the following considerations into account when you turn on the policy:
    - Items that are no longer within the specified location won't be labeled.
    - Items that no longer match the policy criteria won't be labeled.

On the **Label policies** page, the **Status** column displays **In simulation** for auto-labeling policies that are running in simulation, or configured for simulation and complete.

Simulation typically completes within one or two days, depending on the amount of data to analyze. The completed simulation triggers an email notification that's sent to the user configured to receive [activity alerts](/en-us/defender-xdr/alert-policies).

To view the simulation results, select the policy from the **Label policies** page, and from the flyout pane, select **View simulation**. You can then view any samples, review the number of matching items and the locations, edit the policy, turn on the policy, or restart the simulation.

## Before you begin

To make sure you have permissions to create and edit retention labels and their policies, see the permissions information for [records management](get-started-with-records-management#permissions) or [data lifecycle management](get-started-with-data-lifecycle-management#permissions-for-retention-policies-and-retention-labels), depending on the solution you're using.

To run the policy in simulation mode:

- Auditing for Microsoft 365 must be turned on. If you need to turn on auditing or you're not sure whether auditing is already on, see [Turn audit log search on or off](audit-log-enable-disable).
- To view the list of samples, you must have the **Data Classification List Viewer** role, and to view file or email contents in the source view, you must have the **Data Classification Content Viewer** role.

Make sure you have [created the retention labels](file-plan-manager#create-retention-labels) you want to apply to items.

Note

You can extend your auto-labeling of retention labels to images. For more information, see [Learn about optical character recognition in Microsoft Purview](ocr-learn-about).

## How to create an auto-apply retention label policy

Decide before you create your retention label policy whether to make it **adaptive** or **static**. For more information, see [Adaptive or static policy scopes for retention](retention#adaptive-or-static-policy-scopes-for-retention). If you decide to use an adaptive policy, you must create one or more adaptive scopes before you create your retention label policy, and then select them during the create retention label policy process. For instructions, see [Configuration information for adaptive scopes](purview-adaptive-scopes#configure-adaptive-scopes).

When you create an auto-apply policy, you select a retention label to automatically apply to content, based on the conditions that you specify:

1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) and then:

    If you're using records management: **Solutions** &gt; **Records Management** &gt; **Policies** &gt; **Label policies** &gt; **Auto-apply a label**

    If you're using data lifecycle management: **Solutions** &gt; **Data Lifecycle Management** &gt; **Policies** &gt; **Label policies** &gt; **Auto-apply a label**
2. Enter a name and description for this auto-labeling policy, and then select **Next**.
3. For **Choose the type of content you want to apply this label to**, select one of the available conditions. For more information about the choices, see the Configuring conditions for auto-apply retention labels section on this page.
4. For the **Assign admin units** page, keep the default of **Full directory**. Currently, admin units aren't supported for this policy.

1. For the **Choose the type of retention policy to create** page, select **Adaptive** or **Static**, depending on the choice you made from the Before you begin instructions. If you haven't already created adaptive scopes, you can select **Adaptive** but because there won't be any adaptive scopes to select, you won't be able to finish the policy configuration with this option.
2. Depending on your selected scope:

    - If you chose **Adaptive**: On the **Choose adaptive policy scopes and locations** page, select **Add scopes** and select one or more adaptive scopes that have been created. Then, select one or more locations. The locations that you can select depend on the [scope types](purview-adaptive-scopes#configure-adaptive-scopes) added. For example, if you only added a scope type of **User**, you'll be able to select **Exchange mailboxes** but not **SharePoint sites**.
    - If you chose **Static**: On the **Choose locations** page, toggle on or off any of the locations. For each location, you can leave it at the default to [apply the policy to the entire location](retention-settings#a-policy-that-applies-to-entire-locations), or [specify includes and excludes](retention-settings#a-policy-with-specific-inclusions-or-exclusions)

    For information about the location choices, see [Locations](retention-settings#locations).
3. Follow the prompts to select a retention label, whether to run the policy in simulation mode or turn it on (if applicable for your chosen condition), and then review and submit your configuration choices.

To edit an existing retention label policy (the policy type is **Auto-apply**), select it, and then select the **Edit** option to start the **Edit retention policy** configuration.

After content is labeled by using an auto-apply label policy, the applied label can't be automatically removed or changed by changing the content or the policy, or by a new auto-apply label policy. For more information, see [Only one retention label at a time](retention#only-one-retention-label-at-a-time).

Note

An auto-apply retention label policy will never replace an existing retention label that's applied to content. If you want to relabel content by using the conditions you configure, you'll need to manually remove the current retention label from existing content.

### Configuring conditions for auto-apply retention labels

You can apply retention labels to content automatically when that content contains:

- Specific types of sensitive information
- Specific keywords or searchable properties that match a query you create
- A match for trainable classifiers

Or, you can automatically apply retention labels to newly shared cloud attachments.

When you configure retention labels to auto-apply based on sensitive information, keywords or searchable properties, or trainable classifiers, use the following table to identify when retention labels can be automatically applied.

SharePoint items that are in draft or that have never been published aren't supported for this scenario.

Exchange:

| Condition | Items in transit (sent or received) | Existing items (data at rest) |
| --- | --- | --- |
| Sensitive info types | Yes | No |
| Specific keywords or searchable properties | Yes | Yes |
| Trainable classifiers | Yes | Yes (last six months only) |

SharePoint and OneDrive:

| Condition | New or modified items | Existing items |
| --- | --- | --- |
| Sensitive info types | Yes | Yes ^\*^ |
| Specific keywords or searchable properties | Yes | Yes |
| Trainable classifiers | Yes | Yes (last six months only) |

**Footnote:**

^\*^ Applies only to content that's already classified, which you can determine by using [content explorer](data-classification-content-explorer).

#### Auto-apply labels to content with specific types of sensitive information

When you create auto-apply retention label policies for sensitive information, you see the same list of policy templates as when you create a Microsoft Purview Data Loss Prevention (DLP) policy. Each template is preconfigured to look for specific types of sensitive information. In the following example, the sensitive info types are from the **Privacy** category, and **U.S Personally Identifiable Information (PII) Data** template:

![Policy templates with sensitive information types.](media/sensitive-info-configuration.png)

To learn more about the sensitive information types, see [Learn about sensitive information types](sit-sensitive-information-type-learn-about#learn-about-sensitive-information-types). Currently, [exact data match based sensitive information types](sit-learn-about-exact-data-match-based-sits#learn-about-exact-data-match-based-sensitive-information-types) and [document fingerprinting](sit-document-fingerprinting) aren't supported for this scenario.

After you select a policy template, you can add or remove any types of sensitive information, and you can change the confidence level and instance count. In the previous example screenshot, these options have been changed so that a retention label will be auto-applied only when:

- The type of sensitive information that's detected has a match accuracy (or [confidence level](sit-sensitive-information-type-learn-about#more-on-confidence-levels)) of at least **Medium confidence** for two of the sensitive info types, and **High confidence** for one. Many sensitive information types are defined with multiple patterns, where a pattern with a higher match accuracy requires more evidence to be found (such as keywords, dates, or addresses), while a pattern with a lower match accuracy requires less evidence. The lower the confidence level, the easier it is for content to match the condition but with the potential for more false positives.
- The content contains between 1 and 9 instances of any of these three sensitive info types. The default for the **to** value is **Any**.

For more information about these options, see the following guidance from the DLP documentation [Test your Data Loss Prevention policies](dlp-test-dlp-policies).

Important

Sensitive information types have two different ways of defining the max unique instance count parameters. To learn more, see [Instance count supported values for SIT](sit-limits#instance-count-supported-values-for-sit).

To consider when using sensitive information types to auto-apply retention labels:

- If you use custom sensitive information types, these can't auto-label existing items in SharePoint and OneDrive.

#### Auto-apply labels to content with keywords or searchable properties

You can auto-apply labels to content by using a query that contains specific words, phrases, or values of searchable properties. You can refine your query by using search operators such as AND, OR, and NOT.

![Query editor.](media/new-retention-query-editor.png)

For more information about the query syntax that uses Keyword Query Language (KeyQL), see [Keyword Query Language (KeyQL) syntax reference](/en-us/sharepoint/dev/general-development/keyword-query-language-kql-syntax-reference).

Query-based auto-apply policies use the same search index as eDiscovery content search to identify content. For more information about the searchable properties that you can use, see [Keyword queries and search conditions for Content Search](ediscovery-keyword-queries-and-search-conditions).

Some things to consider when using keywords or searchable properties to auto-apply retention labels:

- For SharePoint, crawled properties and custom properties aren't supported for these KeyQL queries and you must use only predefined managed properties for documents. However, you can use mappings at the tenant level with the predefined managed properties that are enabled as refiners by default (RefinableDate00-19, RefinableString00-99, RefinableInt00-49, RefinableDecimals00-09, and RefinableDouble00-09). For more information, see [Overview of crawled and managed properties in SharePoint Server](/en-us/SharePoint/technical-reference/crawled-and-managed-properties-overview), and for instructions, see [Create a new managed property](/en-us/sharepoint/manage-search-schema#create-a-new-managed-property).
- If you map a custom property to one of the refiner properties, wait 24 hours before you use it in your KeyQL query for a retention label.
- Although SharePoint managed properties can be renamed by using aliases, don't use these for KeyQL queries in your labels. Always specify the actual name of the managed property, for example, "RefinableString01".
- To search for values that contain spaces or special characters, use double quotation marks (`" "`) to contain the phrase; for example, `subject:"Financial Statements"`.
- Suffix wildcard searches (such as `*cat`) or substring wildcard searches (such as `*cat*`) aren't supported. However, prefix wildcard searches (such as `cat*`) are supported.
- Use the *DocumentLink* property instead of *Path* to match an item based on its URL. To include or exclude content inside a specific document library, use the *ParentLink* property.
- Be aware that partially indexed items can be responsible for not labeling items that you're expecting, or labeling items that you're expecting to be excluded from labeling when you use the NOT operator. For more information, see [Partially indexed items in Content Search](ediscovery-partially-indexed-items-in-content-search).
- We recommend that you don't use spaces between words in RefinableStrings values on documents. RefinableString isn't a word-break property.

Examples queries:

| Workload | Example | Description |
| --- | --- | --- |
| Exchange | `subject:"Financial Statements"` | Finds emails with the exact phrase "Financial Statements" in the subject line, ignoring case. |
| Exchange | `recipients:garthf@contoso.com` | Finds emails sent to `garthf@contoso.com` , whether directly or copied. |
| SharePoint | `contenttype:document` | Finds all items classified as documents in SharePoint. |
| SharePoint | `site:https://contoso.sharepoint.com/sites/teams/procurement AND contenttype:document` | Finds all documents in the Procurement team site on SharePoint. |
| SharePoint | `ParentLink:SiteAssets` | Finds items stored in the Site Assets library of SharePoint sites. |
| SharePoint | `ParentLink:"https://contoso.sharepoint.com/sites/Legal/Shared Documents"` | Finds only items stored in the Shared Documents library of the Legal site. |
| SharePoint | `NOT ParentLink:"https://contoso.sharepoint.com/sites/Legal/Shared Documents"` | Finds all content except items stored in that document library. |
| OneDrive | `ParentLink:"https://contoso-my.sharepoint.com/personal/john_doe_contoso_com/Documents"` | Includes only content stored in John Doe’s OneDrive Documents library. |
| OneDrive | `NOT ParentLink:"https://contoso-my.sharepoint.com/personal/john_doe_contoso_com/Documents"` | Excludes all content from that specific OneDrive library. |
| Exchange or SharePoint | `"customer information" OR "private"` | Finds content that includes either "customer information" or "private", in emails (Exchange) or documents (SharePoint). |

More complex examples:

The following query for SharePoint identifies Word documents or Excel spreadsheets when those files contain the keywords **password**, **passwords**, or **pw**:

```KeyQL
(password OR passwords OR pw) AND (filetype:doc* OR filetype:xls*)
```

The following query for Exchange identifies any Word document or PDF that contains the word **nda** or the phrase **non disclosure agreement** when those documents are attached to an email:

```KeyQL
(nda OR "non disclosure agreement") AND (attachmentnames:.doc* OR attachmentnames:.pdf)
```

The following query for SharePoint identifies documents that contain a credit card number:

```KeyQL
sensitivetype:"credit card number"
```

The following query contains some typical keywords to help identify documents or emails that contain legal content:

```KeyQL
ACP OR (Attorney Client Privilege*) OR (AC Privilege)
```

The following query contains typical keywords to help identify documents or emails for human resources:

```KeyQL
(resume AND staff AND employee AND salary AND recruitment AND candidate)
```

Note that this final example uses the best practice of always including operators between keywords. A space between keywords (or two `property:value` expressions) is the same as using AND. By always adding operators, it's easier to see that this example query identifies only content that contains all these keywords, instead of content that contains any of the keywords. If your intention is to identify content that contains any of the keywords, specify OR instead of AND. As this example shows, when you always specify the operators, it's easier to correctly interpret the query.

##### Microsoft Teams meeting recordings and transcripts

To identify Microsoft meeting recordings and transcripts that are stored in users' OneDrive accounts or in SharePoint, specify the following for the **Keyword query editor**:

```KeyQL
ProgID:Media AND ProgID:Meeting
```

Most of the time, meeting recordings and transcripts are saved to OneDrive. But for channel meetings, they're saved in SharePoint. For more information, see [Use OneDrive and SharePoint to store meeting recordings](/en-us/MicrosoftTeams/tmr-meeting-recording-change).

The query will identify:

- A Teams meeting transcript, when there isn't an accompanying recording
- A Teams meeting recording and accompanying transcript

Because video transcripts are [stored with the video in OneDrive or SharePoint](https://support.microsoft.com/office/view-edit-and-manage-video-transcripts-and-captions-3cb9acb6-05b2-4f59-a50d-7df61123aa20#bkmk_how-captions-and-transcripts-are-stored), they can't be targeted for retention separately when there's a Teams meeting recordings video file.

##### Identify files and emails that have a sensitivity label

To identify files in SharePoint or OneDrive and Exchange emails that have a specific [sensitivity label](sensitivity-labels) applied, specify the following for the **Keyword query editor**:

```KeyQL
InformationProtectionLabelId:<GUID>
```

To find the GUID, use the [Get-Label](/en-us/powershell/module/exchange/get-label) cmdlet from [Security & Compliance PowerShell](/en-us/powershell/exchange/scc-powershell):

```powershell
Get-Label | Format-Table -Property DisplayName, Name, Guid
```

#### Auto-apply labels to content by using trainable classifiers

Important

Currently, trainable classifiers for auto-labeling can't be used with [adaptive scopes](retention#adaptive-or-static-policy-scopes-for-retention). Use a static scope instead.

When you choose the option for a trainable classifier, you can select one or more of the pre-trained or custom trainable classifiers:

![Choose trainable classifier.](media/retention-label-classifers.png)

The available pre-trained classifiers are often updated, so there might be more entries to select than the ones displayed in this screenshot.

For more information about trainable classifiers, see [Learn about trainable classifiers](trainable-classifiers-learn-about).

To automatically apply a label by using this option, SharePoint sites, as well as mailboxes, must have at least 10 MB of data.

To consider when using trainable classifiers to auto-apply retention labels:

- You can't auto-label SharePoint and OneDrive items that are older than six months.

#### Auto-apply labels to cloud attachments

Note

Support for cloud attachments that are shared in Viva Engage is in preview.

You might need to use this option if you're required to capture and retain all copies of files in your tenant that are sent over communications by users, or files that are referenced in Microsoft 365 Copilot or Microsoft 365 Copilot Chat. You use this option in conjunction with retention policies for the communication services themselves; Exchange, Teams, Viva Engage, and Copilot.

Important

When you select a label to use for auto-applying retention labels for cloud attachments, ensure that the label retention setting **Start the retention period based on** is **When items were labeled**.

Cloud attachments, sometimes also known as modern attachments, are a sharing mechanism that uses embedded links to files that are stored in the cloud. They support centralized storage for shared content with collaborative benefits, such as version control. Cloud attachments are not attached copies of a file or a URL text link to a file. However, support for URL text links is also supported. You might find it helpful to refer to the visual checklists for supported cloud attachments in [Outlook](/en-us/microsoft-365/troubleshoot/retention/cannot-retain-cloud-attachments#cloud-attachments-in-outlook), [Teams](/en-us/microsoft-365/troubleshoot/retention/cannot-retain-cloud-attachments#cloud-attachments-in-teams), and [Viva Engage](/en-us/microsoft-365/troubleshoot/retention/cannot-retain-cloud-attachments#cloud-attachments-in-viva-engage).

When you choose the option to apply a retention label to cloud attachments, for compliance purposes, a copy of that file is created at the time of sharing. Your selected retention label is then applied to the copy that can then be [identified using eDiscovery](ediscovery-cloud-attachments). Users aren't aware of the copy that is stored in the Preservation Hold library. The retention label isn't applied to the message itself, or to the original file.

If the file is modified and shared again, a new copy of the file as a new version is saved in the Preservation Hold library. For more information, including why you should use the **When items were labeled** label setting, see [How retention works with cloud attachments](retention-policies-sharepoint#how-retention-works-with-cloud-attachments).

The cloud attachments supported for this option are files such as documents, videos, and images that are stored in SharePoint and OneDrive. For Teams, cloud attachments shared in chat messages, and standard and private channels are supported. For Viva Engage, cloud attachments shared with users in storylines, community posts, and Inbox messages are supported. For Copilot, files referenced to users in the chat conversation and referenced by users are supported.

Cloud attachments shared over meeting invites and apps other than Teams, Outlook, Viva Engage, and Copilot aren't supported. The cloud attachments must be shared by users or Copilot; cloud attachments sent via bots aren't supported.

Although not required for this option, we recommend that you ensure versioning is enabled for your SharePoint sites and OneDrive accounts so that the version shared can be accurately captured. If versioning isn't enabled, the last available version is retained. Documents in draft or that have never been published aren't supported.

When you select a label to use for auto-applying retention labels for cloud attachments, make sure the label retention setting **Start the retention period based on** is **When items were labeled**.

When you configure the locations for this option, you can select:

- **SharePoint classic and communication sites** for shared files stored in SharePoint communication sites, team sites that aren't connected by Microsoft 365 groups, and classic sites.
- **Microsoft 365 Groups** for shared files that are stored in team sites connected by Microsoft 365 groups.
- **OneDrive accounts** for shared files stored in users' OneDrive.

You'll need to create separate retention policies if you want to retain or delete the original files, email messages, or messages from Teams and Copilot, and Viva Engage.

Note

If you want retained cloud attachments to expire at the same time as the messages that contained them, configure the retention label to have the same retain and then delete actions and timings as your retention policies for Exchange, Teams and Copilot, and Viva Engage.

To consider when auto-applying retention labels to cloud attachments:

- If cloud attachments and links in a Teams or Viva Engage message are changed after the message is sent by editing the message, those changed cloud attachments and links aren't supported for retention.
- When a user is added to a Teams conversation and given access to the full history of the conversation, that history can include cloud attachments and URL text links. If these attachments were shared within 48 hours of the user added to the conversation, current copies of the attachments are auto-labeled for retention. Attachments shared before this time period aren't supported for newly added users.
- Attachments and links shared outside Teams, Outlook, Viva Engage, and Copilot aren't supported, and the attachments and links must be content stored in SharePoint or OneDrive.
- Cloud attachments and links in encrypted emails or encrypted messages aren't supported.
- Sharing an existing Viva Engage message with an attachment isn't supported.
- Specific to shared documents from URL text links:

    - Supported in the message body but not in the email subject or Teams channel subject, announcement, or subheadings.
    - Not supported for previous responses in the same thread, only the current message
    - Total limit of 25 attachments in a single message, where this maximum can be any combination of cloud attachments and shared documents from URL text links
    - Not supported beyond 5,000 characters in the initial email body or in Teams, Copilot, and Viva Engage messages
- The following items aren't supported as attachments that can be retained:

    - SharePoint sites, pages, lists, forms, folders, document sets, and OneNote pages.
    - Files shared by users who don't have access to those files at the time of sharing.
    - Files that are deleted or moved before the cloud attachment is sent. For example, a user copies and pastes a previously shared attachment from another message, without first confirming that the file is still available. Or, somebody forwards an old message when the file is now deleted.
    - Files that are shared by guests or users outside your organization.
    - Files in draft emails and messages that aren't sent.
    - Empty files.

## How long it takes for retention labels to take effect

When you auto-apply retention labels based on sensitive information, keywords or searchable properties, or trainable classifiers, it can take up to seven days for the retention labels to be applied:

![Diagram of when auto-apply labels take effect.](media/retention-labels-autoapply-timings.png)

If the expected labels don't appear after seven days, check the **Status** of the auto-apply policy by selecting it from the **Label policies** page in the Microsoft Purview portal. If you see the status of **Off (Error)** and in the details for the locations see a message that it's taking longer than expected to deploy the policy (for SharePoint) or to try redeploying the policy (for OneDrive), try running the [Set-RetentionCompliancePolicy](/en-us/powershell/module/exchange/set-retentioncompliancepolicy) PowerShell command to retry the policy distribution:

1. [Connect to Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell).
2. Run the following command:

    ```PowerShell
    Set-RetentionCompliancePolicy -Identity <policy name> -RetryDistribution
    ```

## Updating retention labels and their policies

For auto-apply retention label policies that are configured for sensitive information, keywords or searchable properties, or a match for trainable classifiers: When a retention label from the policy is already applied to content, a change in configuration to the selected label and policy will be automatically applied to this content in addition to content that's newly identified.

For auto-apply retention label policies that are configured for cloud attachments: Because this policy applies to newly shared files rather than existing files, a change in configuration to the selected label and policy will be automatically applied to newly shared content only.

Some settings can't be changed after the label or policy is created and saved, which include:

- Names for retention labels and their policies, the scope type (adaptive or static), and the retention settings except the retention period.
- The option to mark items as a record.

### Deleting retention labels

To delete a retention label, all three conditions must apply:

- The label isn't included in any retention label policy
- The label isn't configured for event-based retention
- The label isn't configured to mark items as regulatory records

When all these conditions are met:

- You can always delete a retention label that doesn't mark items as records (sometimes referred to as a "standard retention label"). The deletion succeeds even if the label is applied to items, and the retention label is then removed from these items.
- You can delete a retention label that marks items as records only if the label isn't applied to items. If the label has been applied to items, the deletion fails and you see a link to content explorer to identify the labeled items. It can take up to two days for content explorer to show the items that are labeled. In this scenario, the retention label might be deleted without showing you the link to content explorer.

## Locking the policy to prevent changes

If you need to ensure that no one can turn off the policy, delete the policy, or make it less restrictive, see [Use Preservation Lock to restrict changes to retention policies and retention label policies](retention-preservation-lock).

## Troubleshooting retention label policies

If your auto-apply retention label policies aren't working as expected or you see errors related to these policies, use the following troubleshooting resources:

- [Identify errors in Microsoft 365 retention and retention label policies](/en-us/microsoft-365/troubleshoot/retention/identify-errors-in-retention-and-retention-label-policies)
- [Resolve errors in Microsoft 365 retention and retention label policies](/en-us/microsoft-365/troubleshoot/retention/resolve-errors-in-retention-and-retention-label-policies)

Additionally, if you're also using the older feature, [MRM retention tags and retention policies](/en-us/exchange/security-and-compliance/messaging-records-management/retention-tags-and-policies), see [Auto-apply retention label doesn't apply to items in a mailbox](/en-us/microsoft-365/troubleshoot/retention/auto-apply-retention-label-not-apply-messages).
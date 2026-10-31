---
layout: Conceptual
title: Help prevent sharing credit card numbers through email | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/dlp-create-policy-cc-email
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- CSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-26T00:00:00.0000000Z
audience: ITPro
ms.topic: how-to
ms.service: purview
ms.subservice: purview-data-loss-prevention
ms.collection:
- highpri
- tier1
- M365-security-compliance
- m365solution-mip
- m365initiative-compliance
ms.custom: admindeeplinkCOMPLIANCE, msecd-doc-authoring-1014
search.appverid:
- MET150
description: Create a Microsoft Purview DLP policy to detect and block credit card numbers sent through email. Includes a step-by-step policy creation scenario for testing and deployment planning.
ai-usage: ai-assisted
locale: en-us
document_id: c526b71a-ebc0-6ce7-e034-1eb854d35ea8
document_version_independent_id: c526b71a-ebc0-6ce7-e034-1eb854d35ea8
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/dlp-create-policy-cc-email.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: dlp-create-policy-cc-email
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/dlp-create-policy-cc-email.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
platformId: 07802521-217f-e178-4ad5-78822ebce319
---

# Help prevent sharing credit card numbers through email | Microsoft Learn

This section shows how to create a Microsoft Purview Data Loss Prevention (DLP) policy that blocks emails containing credit card numbers. It follows the process described in [Design a data loss prevention policy](dlp-policy-design#design-a-data-loss-prevention-policy). Work through this scenario in your test environment to familiarize yourself with the policy creation UI.

Important

This article presents a hypothetical scenario with hypothetical values. It's only for illustrative purposes. Substitute your own sensitive information types, sensitivity labels, distribution groups, and users.

How you deploy a policy is as important as policy design. [This article](dlp-create-deploy-policy#deploy-and-manage-dlp-policies) shows you how to use the deployment options so that the policy achieves your intent while avoiding costly business disruptions.

## Prerequisites and assumptions

This scenario uses the *Highly confidential* sensitivity label, so it requires that you create and publish sensitivity labels. To learn more, see:

- [Learn about sensitivity labels](sensitivity-labels)
- [Get started with sensitivity labels](get-started-with-sensitivity-labels)
- [Create and configure sensitivity labels and their policies](create-sensitivity-labels)

This procedure uses a hypothetical distribution group *Finance team* at Contoso.com and a hypothetical SMTP recipient *adele.vance@fabrikam.com*.

This procedure uses alerts, see: [Get started with the data loss prevention alerts](dlp-alerts-get-started)

## Policy intent statement and mapping

*We need to block emails to all recipients that contain credit card numbers or that have the ‘highly confidential’ sensitivity label applied except if the email is sent from someone on the finance team to adele.vance@fabrikam.com. We want to notify the compliance admin every time an email is blocked and notify the user who sent the item and no one can be allowed to override the block. Track all occurrences of this high risk event in the log and we want the details of any events captured and made available for investigation*

| Statement | Configuration question answered and configuration mapping |
| --- | --- |
| "We need to block emails to all recipients..." | - Where to monitor: **Enterprise applications & devices** and **Exchange**- Administrative scope: **Full directory**- Action: **Restrict access or encrypt the content in Microsoft 365 locations** &gt; **Block users from receiving email or accessing shared SharePoint, OneDrive, and Teams files** &gt; **Block everyone** |
| "...that contain credit card numbers or have the 'highly confidential' sensitivity label applied..." | - What to monitor: use the **Custom template** - Conditions for match: edit it to add the *highly confidential* sensitivity label |
| "...except if..." | - Condition group configuration: Create a nested boolean NOT condition group joined to the first conditions using a boolean AND |
| "...the email is sent from someone on the finance team..." | - Condition for match: **Sender is a member of** |
| "...and..." | - Condition for match: add a second condition to the NOT group |
| "...to adele.vance@fabrikam.com..." | - Condition for match: **Recipient is** |
| "...Notify..." | - User notifications: **enabled**- Policy tips: **enabled** |
| "...the compliance admin every time an email is blocked and notify the user who sent the item..." | - Policy tips: **enabled** - Notify these people: **selected**- The person who sent, shared, or modified the content: **selected**- Send the email to these additional people: add the email address of the compliance administrator |
| "...and no one can be allowed to override the block... | - **Allow overrides from M365 Services**: not selected |
| "...Track all occurrences of this high risk event in the log and we want the details of any events captured and made available for investigation." | - Use this severity level in admin alerts and reports: **high**- Send an alert to admins when a rule match occurs: **selected**- Send alert every time an activity matches the rule: **selected** |

## Steps to create the policy

Important

For this policy creation procedure, accept the default include and exclude values and leave the policy turned off. Change these values when you deploy the policy.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Open the **Data loss prevention** solution and go to **Policies** &gt; **+ Create policy**.
3. Select **Enterprise applications & devices**.
4. Select **Custom** from the **Categories** list.
5. Select **Custom** from the **Regulations** list.
6. Select **Next**.
7. Enter a **Name** and a **Description** for the policy. You can use the policy intent statement here.

    Important

    You can't rename policies.
8. Select **Next**.
9. **Assign admin units**. To apply the policy to all users, accept the default setting.
10. Select **Next**.
11. Choose where to apply the policy. Select only the **Exchange email** location. Deselect all the other locations.
12. Select **Next**.
13. On the **Define policy settings** page, the **Create or customize advanced DLP rules** option should already be selected.
14. Select **Next**.
15. Select **Create rule**. Name the rule and provide a description.
16. Under **Conditions**, select **Add condition** &gt; **Content contains**.
17. (Optional) Enter a **Group name**.
18. (Optional) Select a **Group operator**.
19. Select **Add** &gt; **Sensitive info types** &gt; **Credit Card Number**.
20. Select **Add**.
21. Still within the **Content contains** section, select **Add** &gt; **Sensitivity labels** &gt; **Highly confidential** and then select **Add**.
22. Next, beneath the **Content contains** section, select **Add group**.
23. Leave the Boolean operator set to **AND**, then set the toggle to **NOT**.
24. Select **Add condition**.
25. Select **Sender is a member of**.
26. Select **Add or remove distribution groups**.
27. Select **Finance Team** and then select **Add**.
28. Select **Add condition** &gt; **Recipient is**.
29. In the email field, enter *adele.vance@fabrikam.com* and select **Add** .
30. Under **Actions**, select **Add an action** &gt; **Restrict access or encrypt the content in Microsoft 365 locations**.
31. Select **Block users from receiving email or accessing shared SharePoint, OneDrive, and Teams files**, then select **Block everyone**.
32. Set the **User notifications** toggle to **On**.
33. Select **Email notifications** &gt; **Notify the person who sent, shared, or last modified the content**.
34. Choose whether or not to **Attach matching email message to the notification**.
35. Choose whether or not to add **Policy tips**.
36. Under **User ovverides**, make sure that **Allow overrides from Microsoft 365 apps and services ...** is *NOT* selected.
37. Under **Incident reports**, set **Use this severity level in admin alerts and reports** to **High**.
38. Set **Send alert every time an activity matches the rule** toggle to **On**.
39. Select **Save**.
40. Select **Next**, then select **Run the policy in simulation mode**.
41. Select **Next** and then select **Submit**.
42. Select **Done**.
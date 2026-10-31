---
layout: Conceptual
title: Help prevent Power BI reports with credit card numbers | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/dlp-create-policy-powerbi-cc-numbers
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
description: Create a DLP Policy that helps protect against unintentional sharing of Power BI reports that contain credit card numbers.
ai-usage: ai-assisted
locale: en-us
document_id: c45ec9a0-00b9-2eb3-7094-5f3f4d2f4935
document_version_independent_id: c45ec9a0-00b9-2eb3-7094-5f3f4d2f4935
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/dlp-create-policy-powerbi-cc-numbers.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: dlp-create-policy-powerbi-cc-numbers
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/dlp-create-policy-powerbi-cc-numbers.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/d3197845-b4ce-44c6-a237-cd4be160e76c
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/aea905fb-0a9d-4d46-b30f-e9cbaf772d1b
platformId: 4e86cd30-c574-7f7d-bd79-f2ca343c0634
---

# Help prevent Power BI reports with credit card numbers | Microsoft Learn

## Overview

Note

The features used in this scenario are in preview.

This article uses the process you learned in [Design a data loss prevention policy](dlp-policy-design#design-a-data-loss-prevention-policy) to show you how to create a Microsoft Purview data loss prevention (DLP) policy that helps protect against unintentional sharing of Power BI reports that contain credit card numbers. Work through this scenario in your test environment to familiarize yourself with the policy creation UI.

Important

This article presents a hypothetical scenario with hypothetical values. It's only for illustrative purposes. Substitute your own sensitive information types, sensitivity labels, distribution groups, and users.

How you deploy a policy is as important as policy design. [This article](dlp-create-deploy-policy#deploy-and-manage-dlp-policies) shows you how to use the deployment options so that the policy achieves your intent while avoiding costly business disruptions.

## Prerequisites and assumptions

This scenario uses the *Highly Confidential - Internal* sensitivity label, so it requires that you create and publish sensitivity labels. To learn more, see:

- [Learn about sensitivity labels](sensitivity-labels)
- [Get started with sensitivity labels](get-started-with-sensitivity-labels)
- [Create and configure sensitivity labels and their policies](create-sensitivity-labels)

The following policy creation procedure uses alerts. For setup information, see [Get started with the data loss prevention alerts](dlp-alerts-get-started).

## Policy intent statement and mapping

*We need to block external users from reports containing credit card numbers, unless the data is labeled with the 'Highly Confidential - Internal' sensitivity lable, in which case a protection policy restricts access to select security groups. We want to notify the compliance admin to know whenever a semantic model is blocked and the data owner to be aware the restriction took place. We also want internal users to be aware that the data is highly confidential and that they shouldn't share it outside the organization.*

| Statement | Configuration question answered and configuration mapping |
| --- | --- |
| "We need to block external users..." | - Where to monitor: **Fabric and Power BI**- Administrative scope: **Full directory**- Action: **Restrict access or encrypt the content in Microsoft 365 locations** &gt; **Block users from receiving email or accessing shared SharePoint, OneDrive, and Teams files, and Power BI items** &gt; **Block only people outside your organization** |
| "...from reports containing credit card numbers..." | - What to monitor: use the **Custom template** - Conditions for match: edit it to add the *Credit Card Number* sensitive info type. |
| "...except if the data is labeled with the *Highly Confidential - Internal* sensitivity label..." | - Condition group configuration: Create a nested boolean NOT condition group joined to the first condition using a boolean AND- Condition for match: edit it to add the *Highly Confidential - Internal* sensitivity label. |
| "We want to notify the compliance admin to know whenever a semantic model is blocked..." | -Incident reports: **Send an alert to admins when a rule match occurs**: **On**- Send an alert every time an activity matches the rule: **selected** |
| "...the data owner to be aware the restriction took place. We also want internal users to be aware that the data is highly confidential and that they shouldn't share it outside the organization." | - User notifications: **On**- Microsoft 365 files and Microsoft Fabric items: Notify users in Office 365 service with a policy tip or email notifications: **selected**- Policy tips: Customize the policy tip text: **selected**. Add text in the text box explaining the rules governing sharing highly confidential data. |

## Steps to create the policy

Important

For this policy creation procedure, accept the default include and exclude values and leave the policy turned off. Change these values when you deploy the policy.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com).
2. Open the **Data loss prevention** solution and go to **Policies**.
3. Select **Create policy**.
4. Select **Enterprise applications & devices**.
5. Select **Custom** from the **Categories** list.
6. Select **Custom policy** from the **Regulations** list.
7. Select **Next**.
8. Enter a name and description for the policy. You can use the policy intent statement here. 
    Important

    Policies can't be renamed
9. Select **Next**.
10. Accept the **Full directory** default under **Admin units**.
11. Select **Next**.
12. Choose where to apply the policy. Select only the **Fabric and Power BI workspaces** location.
13. Select **Next**.
14. On the **Define policy settings** page, make sure the **Create or customize advanced DLP rules** option is selected.
15. Select **Next**.
16. Select **+ Create rule**. Name the rule and provide a description.
17. Under **Conditions**, select **Add condition** &gt; **Content contains** &gt; **Add** &gt; **Sensitive info types**.
18. Select the info types that apply to credit card numbers.
19. Select **Add**.
20. Next, under the **Content contains** section, select **Add group**.
21. Leave the Boolean operator set to **AND**, then set the toggle to **NOT**.
22. In the line below the toggle, select **Add condition** &gt; **Content contains** &gt; **Add** &gt; **Sensitivity labels**.
23. Select the sensitivity label **Highly Confidential - Internal**.
24. Select **Add**.
25. Under **Actions**, select **Add an action** &gt; **Restrict access or encrypt the content in Microsoft 365 locations** &gt; **Block users from receiving email or accessing shared SharePoint, OneDrive, and Teams files, and Power BI items** &gt; **Block only people outside your organization**.
26. Under **User notifications**, set the toggle to **On**.
27. Select **Notify users in Office 365 service with a policy tip or email notifications**, and then select **Customize the policy tip text**.
28. Provide a policy tip that explains that the data in the report is highly confidential is not to be shared outside the organization.
29. Under **Incident reports**, set **Use this severity level in admin alerts and reports** to **High**.
30. Make sure the **Send an alert to admins when a rule match occurs** toggle is set to **On**.
31. Make sure the **Send alert every time an activity matches the rule** radio button is selected.
32. Select **Save**.
33. Review the rule, then select **Next**.
34. Make sure the **Run the policy in simulation mode** radio button and the **Show policy tips while in simulation mode** checkbox are selected.
35. Select **Next**.
36. Review the policy, then select **Submit**.
37. Select **Done**.
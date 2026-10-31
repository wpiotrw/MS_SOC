---
layout: Conceptual
title: Set up global exclusions for Insider Risk Management policies | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/insider-risk-management-settings-global-exclusions
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Learn how to exclude domains, email signature attachments, file types, file paths, sensitive info types, trainable classifiers, SharePoint sites, and keywords from being scored by Insider Risk Management policies
keywords: Microsoft 365, Microsoft Purview, insider risk, risk management, compliance
ms.service: purview
ms.subservice: purview-insider-risk-management
ms.topic: install-set-up-deploy
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-02-27T00:00:00.0000000Z
audience: itpro
ms.collection:
- highpri
- purview-compliance
- m365solution-insiderrisk
- m365initiative-compliance
- highpri
ms.custom: admindeeplinkCOMPLIANCE
locale: en-us
document_id: d365acda-ec8a-87de-109d-312d4b2be62e
document_version_independent_id: d365acda-ec8a-87de-109d-312d4b2be62e
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/insider-risk-management-settings-global-exclusions.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: insider-risk-management-settings-global-exclusions
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/insider-risk-management-settings-global-exclusions.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
platformId: 67054091-299b-9e73-9457-e553789dddcf
---

# Set up global exclusions for Insider Risk Management policies | Microsoft Learn

Important

[Microsoft Purview Insider Risk Management](insider-risk-management) correlates various signals to identify potential malicious or inadvertent insider risks, such as IP theft, data leakage, and security violations. Insider Risk Management enables customers to create policies to manage security and compliance. Built with privacy by design, users are pseudonymized by default, and role-based access controls and audit logs are in place to help ensure user-level privacy.

Use the **Global exclusions** setting in Microsoft Purview Insider Risk Management to exclude items from being scored by Insider Risk Management policies. For example, to reduce "noise" in your policies, you might want to exclude certain file types or domains from being scored for risk if those file types or domains don't present risk to your organization.

When you set up global exclusions, consider using [detection groups](insider-risk-management-settings-detection-groups) to tailor detections for different sets of users. Detection groups can help you reduce false positives for your policies.

## Configure a domain exclusion

You can exclude specific domains related to user activities from being scored by your Insider Risk Management polices. These activities include:

- Email sent to external domains.
- Files, folders, and sites shared with external domains.
- Files uploaded to external domains (using the Microsoft Edge browser).

Allowed domains are ignored by your policies and don't generate alerts.

### Set up a domain exclusion

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Select **Settings** in the upper-right corner of the page, then select **Insider Risk Management** to go to the Insider Risk Management settings.
3. Under **Insider risk settings**, select **Global exclusions**.
4. In the **Type** panel to the right, select **Domains**.
5. In the **Domains** panel to the right, select one of the following tabs:

    - **Individual domains**. To add domains one at a time:

        1. Select **Add domains**, then enter an exact domain in the **Domain** field or use a wildcard asterisk (\*) to detect a subdomain (for example, \*.contoso.com). Preceding the domain name with a wildcard detects a maximum of one subdomain (for example, support.contoso.com).
        2. To include all subdomains within the domain, select the **Include multi-level subdomains** checkbox.

            Note

            You can use wildcards to help match variations of root domains or subdomains. For example, to specify sales.wingtiptoys.com and support.wingtiptoys.com, use the wildcard entry "\*.wingtiptoys.com" to match these subdomains (and any other subdomain at the same level). To specify multi-level subdomains for a root domain, you must select the **Include multi-level subdomains** checkbox.
        3. Press Enter.
        4. Repeat this process for each domain that you want to add.

            Each domain that you enter is added to the **Domain** column and **Yes** or **No** is added to the **Multi-level subdomains included** list.

            Tip

            If you don't want to add domains one at a time, you can import a list of domains from a CSV file by selecting **Import domains from CSV file** on the previous page.
        5. Select **Add domains**.
    - **Domain groups**. To select a [domain detection group that you already created](insider-risk-management-settings-detection-groups#create-a-domains-detection-group):

        1. Select **Add domain group**.
        2. Select the appropriate domain groups from the list. The number of domains included in each domain group is listed in the **Included domains** column.
        3. Select **Save**.

## Configure an email signature attachments exclusion

One of the main sources of noise in Insider Risk Management policies is images in email signatures. The system often detects these images as attachments in emails. If you select the *Sending email with attachments to recipients outside the organization* indicator, the system scores the attachment like any other email attachment sent outside the organization, even if the only thing in the attachment is the email signature. You can use the **Ignore email signature attachments (preview)** setting to exclude these attachments from scoring.

Turning on this setting significantly reduces noise from email signature attachments, but it doesn't completely eliminate all noise. This limitation exists because the system excludes from scoring only the email signature attachment of the email sender (the person who initiates the email or replies to the email). The system still scores a signature attachment for anyone on the To, CC, or BCC line. Also, if someone changes their email signature, the system needs to profile the new signature, which can cause alert noise for a short period of time.

### Configure an email signature attachments exclusion

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Select **Settings** in the upper-right corner of the page, then select **Insider Risk Management** to go to the Insider Risk Management settings.
3. Under **Insider risk settings**, select **Global exclusions**.
4. In the **Type** panel to the right, select **Email signature attachments**.
5. In the **Ignore email signature attachments (preview)** panel to the right, turn the setting **On**.
6. Select **Save**.

## Configure a file path exclusion

When you exclude file paths, user activities that map to specific indicators and that occur in those file path locations don't generate policy alerts. Examples include copying or moving files to a system folder or network share path. You can enter up to 500 file paths for exclusion.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Select **Settings** in the upper-right corner of the page, then select **Insider Risk Management** to go to the Insider Risk Management settings.
3. Under **Insider risk settings**, select **Global exclusions**.
4. In the **Type** panel to the right, select **File paths**.
5. In the **File paths** panel to the right, select one of the following tabs:

    - **Individual file paths**. To add an individual file path, select **Add file paths to exclude**, enter an exact network share or device file path, then select **Add file paths to exclude**. Repeat this process for each file path that you want to exclude. Examples:

        | Example | Description |
        | --- | --- |
        | **\ms.temp\LocalFolder\ or C:\temp** | Excludes files directly under the folder and all subfolders for every file path starting with the entered prefix. |
        | **\public\local\** | Excludes files from every file path containing the entered value.<br>Matches with 'C:\Users\Public\local\', 'C:\Users\User1\Public\local', and '\ms.temp\Public\local'. |
        | **C:\Users\*\Desktop** | Matches with 'C:\Users\user1\Desktop' and 'C:\Users\user2\Desktop'. |
        | **C:\Users\*(2)\Desktop** | Wilcards with numbers are supported. Matches with 'C:\Users\user1\Desktop' and 'C:\Users\user2\Shared\Desktop'. |

        Each file path that you enter is added to the **File path column** on the page.

        Note

        See Default file paths for file paths that are automatically excluded from generating policy alerts.
    - **File path groups**. To select a [file path detection group that you have already created](insider-risk-management-settings-detection-groups#create-a-file-paths-detection-group), select **Add file path group**, then select the appropriate file path groups. The number of file paths included in each group is listed in the **Included file paths** column.
6. Select **Save**.

### Default file paths

By default, the system automatically excludes several file paths from generating policy alerts. Activities in these file paths are typically benign and could potentially increase the volume of non-actionable alerts. If needed, you can cancel the selection for these default file path exclusions to enable risk scoring for activities in these locations.

The default file path exclusions are:

- \Users\*\AppData
- \Users\*\AppData\Local
- \Users\*\AppData\Roaming
- \Users\*\AppData\Local\Temp

The wildcards in these paths denote that all folder levels between the \Users and \AppData are included in the exclusion. For example, activities in *C:\Users\Test1\AppData\Local* and *C:\Users\Test2\AppData\Local*, *C:\Users\Test3\AppData\Local* (and so on) are all included and not scored for risk as part of the *\Users\*\AppData\Local* exclusion selection.

## Configure a file type exclusion

You can exclude specific file types from all Insider Risk Management policy matching. For example, you might want to exclude all .wav files. Files with that extension are ignored for risk scoring by all Insider Risk Management policies.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Select **Settings** in the upper-right corner of the page, then select **Insider Risk Management** to go to the Insider Risk Management settings.
3. Under **Insider risk settings**, select **Global exclusions**.
4. In the **Type** panel to the right, select **File types**.
5. In the **File types** panel to the right, select one of the following tabs:

    - **Individual file types**. To add file types one at a time, select **Add file type**, enter a file type, and then press Enter. Repeat this process for each file type that you want to add. Each file type that you enter is added to the page.
    - **File type groups**. To select a [file type detection group that you have already created](insider-risk-management-settings-detection-groups#create-a-file-types-detection-group), select **Add File type group**, then select the appropriate file type groups from the list.
6. Select **Save**.

## Configure a keyword exclusion

You can configure exclusions for keywords that appear in file names, file paths, or email message subject lines. This configuration provides flexibility for organizations that need to reduce potential alert frequency due to flagging of benign terms. Your Insider Risk Management policies ignore activities related to files or email subjects containing the keyword and don't generate alerts. You can exclude up to 500 keywords.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Select **Settings** in the upper-right corner of the page, then select **Insider Risk Management** to go to the Insider Risk Management settings.
3. Under **Insider risk settings**, select **Global exclusions**.
4. In the **Type** panel to the right, select **Keywords**.
5. In the **Keywords** panel to the right, select one of the following tabs:

    - **Individual keywords**. To add keywords one at a time, enter a keyword in the **Exclude these keywords** field, then press Enter. Repeat this process for each keyword that you want to add. To delete a keyword that you added to the list, select the *X* next to the keyword.

        Tip

        If you want to exclude a keyword from scoring, but you want to score that keyword when it's used in combination with other keywords or a phrase, enter the keyword you want to exclude in the **Exclude these keywords** field, then enter the word or words that are part of the phrase that you do want to score in the **Exclude the above keywords only if these terms aren't also present** field. For example, if you add the keyword "compliance" to the **Exclude these keywords** field, but enter the keyword "training" in the **Exclude the above keywords only if these terms aren't also present** field, the word "compliance" by itself is excluded from scoring, but the phrase "compliance training" is scored.
    - **Keyword groups**. To select a [keyword detection group that you already created](insider-risk-management-settings-detection-groups#create-a-keywords-detection-group), select **Add keyword group**, then select the appropriate keyword groups from the list. The number of keywords included in each group displays under the **Included keywords** heading.
6. Select **Save**.

## Configure a sensitive info type (preview) exclusion

Excluded [sensitive info types](sensitive-information-type-learn-about) map to indicators and triggers involving file-related activities for Endpoint, SharePoint, Teams, OneDrive, and Exchange. The system treats these excluded types as non-sensitive info types. If a file contains any sensitive info type you identify in this section, the system risk scores the file but doesn't show activities involving content related to sensitive info types. For a complete list of sensitive info types, see [Sensitive information type entity definitions](sensitive-information-type-entity-definitions).

You can select sensitive info types to exclude from the list of all available (out-of-box and custom) types available in your organization. You can choose up to 500 sensitive info types.

Note

The exclusion list of sensitive info types takes precedence over the [priority content](insider-risk-management-policies#prioritize-content-in-policies) list.

### Configure a sensitive info type exclusion

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Select **Settings** in the upper-right corner of the page, then select **Insider Risk Management** to go to the Insider Risk Management settings.
3. Under **Insider risk settings**, select **Global exclusions**.
4. In the **Type** panel to the right, select **Sensitive info types**.
5. In the **Sensitive info types** panel to the right, select one of the following tabs:

    - **Individual sensitive info types**. To add sensitive info types one at a time, select **Add or edit sensitive info types to exclude**, select the sensitive info types you want to exclude, and then select **Add**. You can also use the search box to search for a sensitive info type.
    - **SIT groups**. To select a [sensitive info type detection group that you already created](insider-risk-management-settings-detection-groups#create-a-sensitive-info-types-detection-group), select **Add sensitive info type group**, then select the appropriate groups from the list. The number of sensitive info types included in a sensitive info type group displays under the **Included sensitive info types** heading. Select **Save** when you're done.

## Configure a Sharepoint site exclusion

You can configure SharePoint site exclusions to prevent activities that occur in SharePoint (and SharePoint sites associated with Teams channel sites) from generating policy alerts. For example, you might want to exclude sites or channels that contain non-sensitive files and data that you can share with stakeholders or the public. You can enter up to 500 SharePoint site URL paths.

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Select **Settings** in the upper-right corner of the page, then select **Insider Risk Management** to go to the Insider Risk Management settings.
3. Under **Insider risk settings**, select **Global exclusions**.
4. In the **Type** panel to the right, select **SharePoint sites**.
5. In the **SharePoint sites** panel to the right, select one of the following tabs:

    - **Individual sites**. To add SharePoint sites one at a time, select **Add or edit sites to exclude**, select the sites you want to exclude, then select **Edit**. You can also use the search box to search for a site.
    - **Site groups**. To select a [SharePoint site detection group that you already created](insider-risk-management-settings-detection-groups#create-a-sharepoint-sites-detection-group), select **Add SharePoint site group**, then select the appropriate groups from the list. The number of sites included in a site group displays under the **Included sites** heading. Select **Save** when you're done.

## Set up a trainable classifier (preview) exclusion

Excluded [trainable classifiers](classifier-get-started-with) map to indicators and triggers that involve file-related activities for SharePoint, Teams, OneDrive, and Exchange. If any file contains a trainable classifier identified as an exclusion, the file is risk scored but not shown as activity involving content related to trainable classifiers. For a complete list of pre-trained classifiers, see [Trainable classifiers definitions](classifier-tc-definitions#trainable-classifiers-definitions).

You can select trainable classifiers to exclude from the list of all available (out-of-box and custom) types in your organization. Insider Risk Management excludes some trainable classifiers by default, including Threat, Profanity, Targeted harassment, Offensive language, and Discrimination. You can choose up to 500 trainable classifiers.

Note

Optionally, you can choose trainable classifiers to include in the [priority content](insider-risk-management-policies#prioritize-content-in-policies) list.

### Configure a trainable classifier exclusion

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Select **Settings** in the upper-right corner of the page, then select **Insider Risk Management** to go to the Insider Risk Management settings.
3. Under **Insider risk settings**, select **Global exclusions**.
4. In the **Type** panel to the right, select **Trainable classifiers**.
5. In the **Trainable classifiers** panel to the right, select one of the following tabs:

    - **Individual trainable classifier**. To select trainable classifiers one at a time, select **Add or edit trainable classifiers to exclude**, select the appropriate trainable classifiers from the list, and then select **Add**. You can use the search box to search for a trainable classifier.
    - **Trainable classifier groups**. To select a [trainable classifier detection group that you already created](insider-risk-management-settings-detection-groups#create-a-sharepoint-sites-detection-group), select **Add trainable classifier group**, then select the appropriate groups from the list. The number of trainable classifiers included in a trainable classifier group displays under the **Included trainable classifiers** heading. Select **Save** when you're done.
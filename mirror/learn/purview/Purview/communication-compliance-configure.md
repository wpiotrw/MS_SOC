---
layout: Conceptual
title: Get started with Communication Compliance | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/communication-compliance-configure
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Set up Communication Compliance policies to configure user communications for review.
keywords: Microsoft 365, Microsoft Purview, compliance, Communication Compliance
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2025-08-14T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.subservice: purview-communication-compliance
ms.collection:
- highpri
- purview-compliance
- m365solution-insiderrisk
- m365initiative-compliance
- highpri
ms.custom: admindeeplinkCOMPLIANCE
search.appverid:
- MET150
- MOE150
locale: en-us
document_id: 1459622d-0480-363d-5d4b-10ffce67558a
document_version_independent_id: 1459622d-0480-363d-5d4b-10ffce67558a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/communication-compliance-configure.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: communication-compliance-configure
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/communication-compliance-configure.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 2847aca0-8f9b-9820-4656-14b41be1116e
---

# Get started with Communication Compliance | Microsoft Learn

Important

[Microsoft Purview Communication Compliance](communication-compliance) provides the tools to help organizations detect regulatory compliance (for example, SEC or FINRA) and business conduct violations such as sensitive or confidential information, harassing or threatening language, and sharing of adult content. Communication Compliance is built with privacy by design. Usernames are pseudonymized by default, role-based access controls are built in, investigators are opted in by an admin, and audit logs are in place to help ensure user-level privacy.

Use Communication Compliance policies to identify user communications for analysis by internal or external reviewers. For more information about how Communication Compliance policies can help you detect communications in your organization, see [Communication Compliance policies](communication-compliance-policies). To see how Contoso quickly configured a Communication Compliance policy to detect potentially inappropriate content in Microsoft Teams, Exchange Online, and Viva Engage communications, check out this [case study](communication-compliance-case-study).

## Subscriptions and billing

Before getting started with Communication Compliance, confirm your [Microsoft 365 subscription](https://www.microsoft.com/microsoft-365/compare-all-microsoft-365-plans) and any add-ons. To access and use Communication Compliance, administrators need to verify that their organization has a supported subscription and that users have the appropriate licenses assigned. For more information about subscriptions and licensing, see the [subscription requirements](https://aka.ms/M365EnterprisePlans) for Communication Compliance.

Additionally, to detect inappropriate or risky interactions for non-Microsoft 365 AI data, you need to enable [pay-as-you-go billing](/en-us/purview/purview-billing-models) in your organization. Non-Microsoft 365 AI data includes information from other generative AI applications from Microsoft and connected external AI applications. This data type includes [Copilot in Microsoft Fabric](/en-us/fabric/fundamentals/copilot-fabric-overview), [Microsoft Security Copilot](/en-us/copilot/security/microsoft-security-copilot), [Microsoft Copilot Studio](/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio), and any connected or cloud AI application. There aren't any pay-as-you-go billing requirements or charges for Microsoft 365 detecting inappropriate or risky interaction for Microsoft 365 Copilot data.

Important

Communication Compliance is currently available for tenants hosted in geographical regions and countries supported by Azure service dependencies. To verify that Communication Compliance is supported for your organization, see [Azure dependency availability by country/region](/en-us/troubleshoot/azure/general/dependency-availability-by-country).

This feature uses pay-as-you-go billing or per-user licensing for Microsoft Purview capabilities or both. To help you understand and manage your usage, Microsoft Purview provides a **Usage center** in the Microsoft Purview portal. For more information, see [Manage pay-as-you-go and per-user licensing usage](purview-billing-usage). To learn more about Purview billing, see [Purview billing models.](purview-billing-models).

## Recommended actions

Recommended actions can help your organization quickly get started with Communication Compliance. Included on the **Overview** page, recommended actions help guide you through the steps to configure and deploy policies.

The following recommendations help you get started and maximize your Communication Compliance configuration:

- **Get to know Communication Compliance**: Before completing set up, review our official documentation to learn about, plan for, and deploy Communication Compliance in your organization.
- **Assign permissions to ensure your team can get their jobs done**: Ensure that only the appropriate stakeholders can access the solution by assigning team members responsible for managing Communication Compliance features and investigating and reviewing alerts.
- **Create distribution groups for users' whose communications you want to detect**: Create distribution groups containing users who are included in Communication Compliance policies.
- **Create your first policy to start detecting communications**: Detect and investigate potential regulatory compliance violations by first setting up a policy that identifies potential violations across your organization's internal and/or external communications.
- **Review alerts to investigate detected messages and take action**: Identify and analyze messages that match a policy's conditions to trigger alerts that provide context around a policy violation, so you can investigate and take action if needed.
- **Review reports for quick insights into how policies are performing**: Get quick insights into how your policies are performing, view detailed reports to drill down further, and export results for further analyses.

Each action in Communication Compliance has three attributes:

- **Action**: The name and description of the recommended action.
- **Recommended, required, or optional**: Whether the recommended action is highly recommended, required, or optional for Communication Compliance features to function as expected.
- **Estimated time to complete**: Estimated time to complete the recommended action in minutes.

Select recommendations from the list to get started with configuring Communication Compliance. Each recommended action guides you through the required activities for the recommendation, including any requirements, what to expect, and the impact of configuring the feature in your organization. Some recommended actions are automatically marked as complete when configured. If not, manually select the action as complete when configured.

Recommended actions insights on the **Policies** page help summarize current sensitive information types and potential regulatory compliance violations in communications in your organization. [Data classification](data-classification-overview) and the application of sensitivity labels, retention labels, and sensitive information type classification support these insights. These insights are aggregated and don't include any personal data for users in your organization.

![Communication Compliance recommended actions.](media/communication-compliance-recommended-actions.png)

Activity in messages aggregates by [trainable classifier type](communication-compliance-policies#microsoft-provided-trainable-classifiers) from existing policies that use the *Detect inappropriate text* policy template or custom policies that use classifiers. Investigate alerts for these messages on the **Alert dashboard** for your policies.

Activity involving [sensitive information types](communication-compliance-policies#sensitive-information-types) detects in messages covered in existing policies and for messages that aren't covered by existing policies. Insight messages that aren't covered by existing policies can't be investigated and remediated, a new policy must be created to detect and remediate similar activity in future messages. Insights aggregate for all sensitive information types, including ones that your organization didn't previously define in an existing Communication Compliance policy. Use these insights to create a new Communication Compliance policy or to update existing policies. After creating a new policy, message alerts for this policy might or might not match an equal number of messages identified in a similar insight. Your policy might have different conditions, a different number of included users, and only detects message activity that occurs after the policy is active.

Tip

To disable the display of recommended action insights, open a request with Microsoft Support.

## Step 1 (required): Assign permissions for Communication Compliance

To use any of the Communication Compliance-related tools in the Microsoft Purview portal, users need the appropriate permissions. The easiest way to assign roles is to add the user to the appropriate role group on the **Role groups** page in the [Microsoft Purview portal](purview-portal).

For step-by-step guidance, see [Assign permissions in Communication Compliance](communication-compliance-permissions).

## Step 2 (required): Enable the audit log

Communication Compliance requires audit logs to show alerts and log remediation actions that reviewers take. The audit logs summarize all activities associated with a defined organizational policy or any time a Communication Compliance policy changes.

Auditing is enabled for Microsoft 365 organizations by default. Some organizations might disable auditing for specific reasons. If auditing is disabled for your organization, another administrator might have turned it off. We recommend confirming that it's OK to turn auditing back on when you complete this step.

For step-by-step instructions to turn on auditing, see [Turn audit log search on or off](audit-search). After you turn on auditing, a message is displayed that says the audit log is being prepared and that you can run a search in a couple of hours after the preparation is complete. You only need to perform this action once. For more information about using the audit log, see [Search the audit log](audit-search).

## Step 3 (optional): Set up groups for Communication Compliance

When you create a Communication Compliance policy, you define who has their communications reviewed and who performs reviews. In the policy, use email addresses to identify individuals or groups of people. To simplify your setup, you can create groups for people who have their communication reviewed and groups for people who review those communications. If you use groups, you might need several. For example, you might need multiple groups if you want to detect communications between two distinct groups of people or if you want to specify a group that isn't going to be scoped.

Use the following chart to help you configure groups in your organization for Communication Compliance policies:

| Policy Member | Supported Groups | Unsupported Groups |
| --- | --- | --- |
| Scoped users  Excluded users | Distribution groups  Microsoft 365 GroupsMail-enabled security groups | Dynamic distribution groups  Shared mailbox  Nested distribution groups  Microsoft 365 Groups with dynamic membership |
| Reviewers | None | Distribution groups  Dynamic distribution groups  Nested distribution groups Mail-enabled security groups |

When you assign a *distribution group* in the policy, the policy detects all emails and Teams chats from each user in the *distribution group*. When you assign a *Microsoft 365 group* in the policy, the policy detects all emails and Teams chats sent to the *Microsoft 365 group*,\* not the individual emails and chats received by each group member\*. We recommend using distribution groups in Communication Compliance policies so that individual emails and Teams chats from each user are automatically detected.

Tip

For a more flexible configuration and to reduce administrative overhead, consider using an [adaptive scope](purview-adaptive-scopes) instead of a distribution group.

If you're an organization with an Exchange on-premises deployment or an external email provider and you want to detect Microsoft Teams chats for your users, you must create a distribution group for the users with on-premises or external mailboxes. Later in these steps, you assign this distribution group by using the **Choose users and groups** selection in the policy workflow. For more information about the requirements and limitations for enabling cloud-based storage and Teams support for on-premises users, see [Search for and export Teams chat data for on-premises users](ediscovery-search-cloud-based-mailboxes-for-on-premises-users).

To manage scoped users in large enterprise organizations, you might need to detect messages for all users across large groups. You can use PowerShell to configure a distribution group for a global Communication Compliance policy for the assigned group. This configuration enables you to detect messages for thousands of users with a single policy and keep the Communication Compliance policy updated as new employees join your organization.

1. Create a dedicated [distribution group](/en-us/powershell/module/exchange/new-distributiongroup) for your global Communication Compliance policy with the following properties: Make sure that you don't use this distribution group for other purposes or other Office 365 services.

    - **MemberDepartRestriction = Closed**. Ensures that users can't remove themselves from the distribution group.
    - **MemberJoinRestriction = Closed**. Ensures that users can't add themselves to the distribution group.
    - **ModerationEnabled = True**. Ensures that all messages sent to this group are subject to approval and that the group isn't being used to communicate outside of the Communication Compliance policy configuration.

    ```PowerShell
    New-DistributionGroup -Name <your group name> -Alias <your group alias> -MemberDepartRestriction 'Closed' -MemberJoinRestriction 'Closed' -ModerationEnabled $true
    ```
2. Select an unused [Exchange custom attribute](/en-us/Exchange/recipients/mailbox-custom-attributes) to log users added to the Communication Compliance policy in your organization.
3. Run the following PowerShell script on a recurring schedule to add users to the Communication Compliance policy:

    ```PowerShell
    $Mbx = (Get-Mailbox -RecipientTypeDetails UserMailbox -ResultSize Unlimited -Filter {CustomAttribute9 -eq $Null})
    $i = 0
    ForEach ($M in $Mbx)
    {
      Write-Host "Adding" $M.DisplayName
      Add-DistributionGroupMember -Identity <your group name> -Member $M.DistinguishedName -ErrorAction SilentlyContinue
      Set-Mailbox -Identity $M.Alias -<your custom attribute name> SRAdded
      $i++
    }
    Write-Host $i "Mailboxes added to supervisory review distribution group."
    ```

For more information about setting up groups, see:

- [Create and manage distribution groups](/en-us/Exchange/recipients-in-exchange-online/manage-distribution-groups/manage-distribution-groups)
- [Overview of Microsoft 365 Groups](/en-us/office365/admin/create-groups/office-365-groups)

## Step 4 (optional): Verify your Viva Engage tenant is in Native Mode

In Native Mode, all Viva Engage users are in Microsoft Entra ID, all groups are Microsoft 365 Groups, and all files are stored in SharePoint Online. Your Viva Engage tenant must be in Native Mode for Communication Compliance policies to check and identify risky conversations in private messages and community conversations in Viva Engage.

For more information about configuring Viva Engage in Native Mode, see:

- [Overview of Viva Engage Native Mode in Microsoft 365](/en-us/viva/engage/overview-native-mode)
- [Configure your Viva Engage network for Native Mode for Microsoft 365](/en-us/viva/engage/configure-your-viva-engage-network/native-mode)

## Step 5 (required): Create a Communication Compliance policy

You can quickly create a Communication Compliance policy by choosing from several [policy templates](communication-compliance-policies#policy-templates), or you can create a custom policy.

Important

If your role [is scoped by one or more admin units](purview-admin-units), you can't create a policy based on a template. You can create a custom policy, however.

When you create a policy from a template, many settings are automatically chosen for you based on the template you choose. As the final step, you can customize the policy if you want to change any of the settings.

When you create a custom policy, you select all of the settings yourself.

### Create a policy from a template

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Communication Compliance** solution.
3. Select **Policies** in the left navigation.
4. Select **Create policy**, then select one of the policy templates. For example, select **Detect inappropriate text**.
5. In the pane on the right side of the screen:

    1. In the **Policy name** field, confirm or update the policy name. You can't change policy names after you create the policy.
    2. In the **Users or groups in scope** field, choose the users or groups to apply the policy to. If you select the *Detect conflict of interest* template, select two scoped groups or two scoped users to detect internal communications.
    3. In the **Reviewers** field, choose the reviewers for the policy. Reviewers that you add in this field are the reviewers that you can choose from when escalating an alert in the investigation and remediation workflow. When you add reviewers to a policy, they automatically receive an email message that notifies them of the assignment to the policy and links to information about the review process. **Reviewers are individual users and all reviewers must have mailboxes hosted on Exchange Online.**
    4. Review the list of settings that are automatically chosen based on the template you choose. To customize any settings, select **Customize policy**, then make the changes you want. If everything looks OK, select **Create policy**.

    Note

    To enable [optical character recognition (OCR)](/en-us/microsoft-365/compliance/communication-compliance-policies#optical-character-recognition-ocr) to identify embedded or attached images in messages for printed or handwritten text that match policy conditions, select **Customize policy**, then on the **Choose conditions and percentage** page, select the **Use OCR to extract text from images** checkbox.

### Create a custom policy

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Communication Compliance** solution.
3. Select **Policies** in the left navigation.
4. Select **Create policy**, then select **Custom policy**.
5. On the **Name and describe your policy** page, enter a name (required) and description (optional) for the policy. You can't change the policy name after you create it. Select **Next** when you're done.
6. If [one or more admin units exist for your organization](purview-admin-units), you see the **Admin units (preview)** page. Otherwise, you see the **Choose users and reviewers** page (next step) and a banner with a link to learn more about admin units.

    To scope the policy to one or more admin units, select **Add admin units**, select the admin units to apply to the policy, then select **Save**.

    Note

    You can only see the admin units that are scoped to your role. If you're an unrestricted administrator, you can see all admin units for the organization. To view a summary of the role groups and admin units that you're assigned to, select **View my permissions**.

    Select **Next** when you're done with the **Admin units (preview)** page.
7. On the **Choose users and reviewers** page:

    1. In the **Choose users and groups** section, select one of the following options:

    - **All users**: This option is the most inclusive and recommended for the broadest protection.

        Note

        If the policy is [scoped by one or more admin units](purview-admin-units), selecting this option selects all users in the admin units.
    - **Select users**: Start typing to find specific users or groups. The **Show insights and recommendations for users who match this policy's conditions but weren't included in the policy** checkbox appears when you select this option. Leave this checkbox selected if you want to [reduce blind spots by receiving recommendations when users outside of the selected users match the policy conditions](communication-compliance-policies#reduce-user-scoping-blind-spots). This setting isn't available if you choose the **All users** option or the **Select adaptive scopes** option.

        Note

        If the policy is [scoped by one or more admin units](purview-admin-units), you can only select users that are part of those admin units.
    - **Select adaptive scopes**: An adaptive scope uses a query that you specify to define the membership of users or groups. To use an adaptive policy, [create the adaptive scope before you create your policy](purview-adaptive-scopes#configure-adaptive-scopes), then select the scope when you choose this option. Site scopes aren't applicable to Communication Compliance so you won't see them when you add a scope. [Learn more about the advantages of using an adaptive scope](purview-adaptive-scopes).

        Note

        If the policy is [scoped by one or more admin units](purview-admin-units) the **Select adaptive scopes** option doesn't appear. At this time, you can't use adaptive scopes together with admin units.

    1. In the **Excluded users and groups** section, add any users or groups to exclude from the policy.

        Note

        If the policy is [scoped by one or more admin units](purview-admin-units), you can only exclude users and groups that are part of those admin units.
    2. In the **Reviewers** section, choose the reviewers for the policy. Reviewers you add in this section are the reviewers you can choose when escalating an alert in the investigation and remediation workflow. When you add reviewers to a policy, they automatically receive an email message that notifies them of the assignment to the policy and links to information about the review process. **Reviewers are individual users and all reviewers must have mailboxes hosted on Exchange Online.**
    3. Select **Next** when you're done.
8. On the **Choose locations to detect communications** page, choose the communication channels to check, including **Exchange**, **Teams**, **Viva Engage**, or a specific generative AI channel. Supported generative AI channels include **Microsoft Copilot experiences**, **Enterprise AI apps**, and **Other AI apps**. You can also choose to check third-party sources if you configured a connector in Microsoft 365. Select **Next** to move to the next page.
9. On the **Choose conditions and review percentage** page:

    1. In the **Communication direction** section, choose the communication direction to detect, including inbound, outbound, or internal communications.
    2. In the **Conditions** section, add the [conditions](/en-us/microsoft-365/compliance/communication-compliance-policies#conditional-settings) you want to detect. You can choose from many different conditions for messages and message attachments, including conditions that detect for:

    - Default or custom [sensitive information types](communication-compliance-policies#sensitive-information-types). You can create sensitive info types before running the workflow or create them from the workflow.
    - Default or custom [keyword dictionaries](communication-compliance-policies#custom-keyword-dictionaries).
    - [Microsoft provided trainable classifiers](communication-compliance-policies#microsoft-provided-trainable-classifiers). Microsoft provided trainable classifiers can detect potentially inappropriate language and images sent or received in the body of email messages or other types of text. You can choose from the following built-in Microsoft provided trainable classifiers: *Targeted threat*, *Profanity*, *Targeted harassment*, *Adult images*, *Racy images*, and *Gory images*. Communication Compliance also includes content safety classifiers (preview) for Microsoft Teams that are based on large language models (LLMs). These classifiers include *Hate*, *Sexual*, *Violence*, and *Self-harm*. [Learn more about content safety classifiers based on large language models](communication-compliance-policies#content-safety-classifiers-based-on-large-language-models).

    1. In the **Optical character recognition (OCR)** section, to enable [optical character recognition (OCR)](/en-us/microsoft-365/compliance/communication-compliance-policies#optical-character-recognition-ocr) to identify embedded or attached images in messages for printed or handwritten text that match policy conditions, select the **Use OCR to extract text from images** checkbox. One or more conditional settings associated with text, keywords, Microsoft provided trainable classifiers, or sensitive info types must be configured in the policy to enable the selection of the checkbox.
    2. In the **Review percentage** section, move the slider to change the amount of content to review.
    3. In the **Filter email blasts** section, the **Filter out messages from email blasting services** check box is selected by default. This setting causes messages sent from email blast services to be excluded. Messages that match specific conditions won't generate alerts. This exclusion includes bulk email (such as newsletters), spam, phishing, and malware. You can view a [report](communication-compliance-reports-audits#detailed-reports) containing the bulk email senders that are filtered out. The list of senders is filtered before the content is analyzed so there might be senders that don't match the content conditions (extra senders included in the report).
    4. Select **Next** to move to the next page.
10. On the **Review and finish** page, review your policy selections, then select **Create policy**.

### Notes and tips on creating Communication Compliance policies

- After configuring a policy, [learn about best practices for managing the volume of alerts](communication-compliance-alerts-best-practices).
- You can't use PowerShell to create and manage Communication Compliance policies. You must use the [Communication Compliance solution](https://purview.microsoft.com/supervisoryreview).
- For an in-depth walkthrough of setting up a new Communication Compliance policy and remediating an alert, see this 15-minute video:

### Test conditions (preview) when you create or edit a policy

If you create or edit a policy without testing conditions first, you might wait a long time before you can verify that the policy works as intended. Typically, you need to create a pilot policy and test it for several days before rolling the policy out to the wider organization. If you're a member of the Communication Compliance Admins role group or the Communication Compliance role group, you can save time by testing your conditions when you create or edit a policy. You can fine-tune the conditions to make sure the policy works as intended before rolling it out to the wider organization.

Note

Currently, you can only test the following conditions:

- *Content matches any of these classifiers*
- *Content contains any of these sensitive info types*

1. Make sure you're a member of the Communication Compliance Admins role group or the Communication Compliance role group. You must be a member of one of these role groups to use this feature.
2. Create a policy or edit an existing policy.
3. On the **Conditions and percentage** page, after entering your conditions, select **Test your conditions**.

    ![Communication Compliance test conditions.](media/communication-compliance-test-conditions.png)

    Tip

    You can also access the **Test your conditions** command from the list of policies on the **Policies** page or in the policy details panel if you choose to edit the policy.
4. In the **Test policy conditions** pane that appears on the right side of the page, do one of the following actions:

    - Select the **Enter messages to test** option, then enter some messages that you expect the policy to detect. Separate messages with a comma.
    - If you have a .txt file that includes a list of messages to detect, select the **Upload a file to test whether the trainable classifiers detects the matching elements you specified** option, then select **Upload file** to upload your text file.
5. Select **Test** to see a list of test results.

    Tip

    If you don't see the results you're looking for:

    - Check the definition of the [sensitive info type](sit-sensitive-information-type-learn-about#learn-about-sensitive-information-types) or the [trainable classifier](trainable-classifiers-definitions) to make sure it's designed to detect the type of info you expect.
    - Make sure that the message [meets minimum word count requirements](trainable-classifiers-definitions#word-count-requirements).

## Step 6 (optional): Update compliance boundaries for Communication Compliance policies

[Compliance boundaries](ediscovery-set-up-compliance-boundaries) create logical boundaries within an organization that control the user content locations (such as mailboxes, OneDrive accounts, and SharePoint sites) that eDiscovery managers can search.

If you configure compliance boundaries in your organization, update the compliance boundaries to allow certain users access to mailboxes that support Communication Compliance policies. You need to allow access to Communication Compliance administrators and Communication Compliance reviewers for your policy management and investigation and remediation actions to work properly.

To allow access for Communication Compliance admins and reviewers, run the following PowerShell commands. You only need to run these commands once, even if you add new Communication Compliance policies in the future:

```powershell
Import-Module ExchangeOnlineManagement
$UserCredential = Get-Credential
Connect-IPPSSession -Credential $UserCredential
New-ComplianceSecurityFilter -FilterName "CC_mailbox" -Users <list your Communication Compliance admins and reviewers user alias or email address> -Filters "Mailbox_Name -like 'SupervisoryReview{*'" -Action All
```

For more information about cmdlet syntax, see [New-ComplianceSecurityFilter](/en-us/powershell/module/exchange/new-compliancesecurityfilter).

## Step 7 (optional): Create notice templates and configure user anonymization

If you want to respond to a policy alert by sending a reminder notice to the associated user, create at least one notice template in your organization. The notice template fields are editable before they're sent as part of the alert remediation process. We recommend creating a customized notice template for each Communication Compliance policy.

You can also choose to enable anonymization for displayed usernames when investigating policy matches and taking action on messages.

### Create templates and configure user anonymization

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com) with credentials for an admin account in your Microsoft 365 organization.
2. Go to the **Communication Compliance** solution.
3. Select **Settings** in the upper-right corner of the page, select **Communication Compliance**, select the **Privacy** tab, select **Show anonymized versions of usernames**, and then select **Save**.
4. Select the **Notice templates** tab, then select **Create notice template**.
5. In the right pane, complete the following fields:

    - Template name (required)
    - Send from (required)
    - Cc and Bcc (optional)
    - Subject (required)
    - Message body (required)
6. Select **Save** to create and save the notice template.

## Step 8 (optional): Test your Communication Compliance policy

After you create a Communication Compliance policy, test it to make sure that the policy properly enforces the conditions you defined. If your Communication Compliance policies include sensitive information types, you might also want to [test your Microsoft Purview Data Loss Prevention (DLP) policies](dlp-test-dlp-policies). Make sure you give your policies time to activate so that the communications you want to test are captured.

Tip

To save time, you can test the following conditions before creating your policy:

- *Content matches any of these classifiers*
- *Content contains any of these sensitive information types*Learn more about testing conditions before creating a policy.

Follow these steps to test your Communication Compliance policy:

1. Open an email client, Microsoft Teams, or Viva Engage while signed in as a scoped user defined in the policy you want to test.
2. Send an email, Microsoft Teams chat, or Viva Engage message that meets the criteria you defined in the Communication Compliance policy. This test can be a keyword, attachment size, domain, and more. Make sure you determine if your configured conditional settings in the policy are too restrictive or too lenient.

    Note

    Email messages can take approximately 24 hours to fully process in a policy. Communications in Microsoft Teams, Viva Engage, and third-party platforms can take approximately 48 hours to fully process in a policy.
3. Sign in to Microsoft 365 as a reviewer designated in the Communication Compliance policy. Go to **Communication Compliance** &gt; **Alerts** to view the alerts for your policies.
4. Remediate the alert by using the remediation controls and verify that the alert is properly resolved.
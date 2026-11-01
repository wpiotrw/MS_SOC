---
layout: Conceptual
title: Adaptive scopes | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/purview-adaptive-scopes
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: TracyP
author: MSFTTracyP
ms.reviewer: samsonchan
manager: laurawi
ms.date: 2026-09-11T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-adaptive-scopes
ms.collection:
- purview-compliance
- m365copilot
- highpri
- SPO_Content
- essentials-manage
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1028
search.appverid:
- MOE150
- MET150
description: Learn about Microsoft Purview adaptive scopes for policies.
locale: en-us
document_id: 92875fe5-0181-9dd4-4677-5636477682ce
document_version_independent_id: 92875fe5-0181-9dd4-4677-5636477682ce
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/purview-adaptive-scopes.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: purview-adaptive-scopes
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/purview-adaptive-scopes.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: d715d615-5ce3-ee8d-7a18-29c1259ceba5
---

# Adaptive scopes | Microsoft Learn

> 
> *[Microsoft Purview service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description)*

When you create a [communication compliance policy](communication-compliance-policies), a [policy for retention](retention#retention-policies-and-retention-labels), or an [auto-labeling policy](apply-sensitivity-label-automatically), you can add an adaptive scope for your policy. A single policy can have one or many adaptive scopes.

- An adaptive scope uses a query that you specify, so you can define the membership of users or groups included in that query. These dynamic queries run daily against the attributes or properties that you specify for the selected scope. You can use one or more adaptive scopes with a single policy.
- For example, you can assign different policy settings to users according to their department by using existing Microsoft Entra attributes without the administrative overhead of creating and maintaining groups for this purpose.

## Advantages of using adaptive scopes

The advantages of using adaptive scopes include:

- No limits on the number of items per policy. Although adaptive policies are still subject to the maximum number of policies per tenant limitations, the more flexible configuration likely results in far fewer policies.
- More powerful targeting for your policies. For example, you can assign different settings to users according to their geographical location without the administrative overhead of creating and maintaining groups.
- Query-based scopes provide resilience against business changes that might not be reliably reflected in group membership or external processes that rely on cross-department communication.
- A single policy can include locations for both Microsoft Teams and Viva Engage, whereas when you don’t use an adaptive scope, each location requires its own policy.
- Support for [Microsoft Entra administrative units](/en-us/azure/active-directory/roles/administrative-units).

For additional advantages of using adaptive scopes specific to policies for retention, see [Adaptive or static policy scopes for retention](retention#adaptive-or-static-policy-scopes-for-retention).

For configuration information, see Configuring adaptive scopes.

### How adaptive scopes work with Microsoft Entra administrative units

Whereas adaptive scopes are created and configured in Microsoft Purview to support the dynamic targeting of policies for compliance, administrative units are created and configured in Microsoft Entra ID. They provide the ability to assign admins to one or more administrative units, with the result that these now restricted admins can manage only the users in their assigned administrative units. This configuration supports the security best practice of least privilege. Typically, administrative units are designed around specific geography, department, or business divisions.

This boundary of management flows into Microsoft Purview for supported solutions to ensure that restricted admins can manage only the users they have been assigned to manage.

As an example to show how administrative units integrate with adaptive scopes, consider a restricted compliance admin who wants to create an adaptive user scope just for users in France:

1. A compliance admin is assigned two administrative units, **All users in Europe** and **All users in North America**. When they create an adaptive scope, they can select and assign only these administrative units. They can't create an adaptive scope to manage users from other administrative units.
2. They create a new adaptive scope for users and select the administrative unit **All users in Europe**. Then, because they want the adaptive scope to be only for users in France, they use the Microsoft Entra ID **Country or region** attribute to specify France (CountryOrRegion = France). If they misconfigure this attribute and specify a valid value in Microsoft Entra ID, such as India, but the users with that value aren't included in the **All users in Europe** administrative unit, the scope won't contain any users.
3. When just this adaptive scope is selected for a policy that's targeted to all users, the policy is applied just to users in France.
4. As a reusable configuration element, the same adaptive scope can be used for other compliance policies.

If the compliance admin adds both of the administrative units to this adaptive scope, the end result is still the same because users in the North America administrative scope don't have France specified as their country or region attribute. However, the compliance admin knows that they need to target just users in France, so it's more efficient to run the query against just the Europe administrative unit. If requirements change, you can always add or remove administrative units from an existing adaptive scope.

### Maximums for adaptive policy scopes

There's no limit to the number of adaptive policy scopes that you can add to a policy, but there are some maximum limits for the query that defines each adaptive scope:

- String length for attribute or property values: 200
- Number of attributes or properties without a group, or within a group: 10
- Number of groups: 10
- Number of characters in an advanced query: 10,000
- Grouping attributes or properties within a group isn't supported. This limitation means that the maximum number of properties or attributes supported within a single adaptive scope is 100.
- For auto-labeling policies, a SharePoint adaptive scope supports up to 50,000 sites per policy.

## Configure adaptive scopes

When you choose to use adaptive scopes, you're prompted to select the type of adaptive scope you want. There are three different types of adaptive scopes, and each one supports different attributes or properties:

| Adaptive scope type | Attributes or properties supported |
| --- | --- |
| **Users** - applies to:  - Exchange mailboxes  - OneDrive accounts  - Teams chats and Copilot interactions  - Teams private channel messages (applicable [pre-migration](retention-policies-teams#migration-of-private-channel-messages-in-2025) only)  - Viva Engage user messages  - Team chats  - Teams call logs  - Microsoft Copilot experiences  - Enterprise AI apps  - Other AI apps | First Name  Last name Display name  Job title  Department  Office Street address  City State or province Postal code  Country or region  Email addresses  Alias  Exchange custom attributes: CustomAttribute1 - CustomAttribute15  Exchange Extension custom attributes: ExtensionCustomAttribute1 - ExtensionCustomAttribute5 |
| **SharePoint sites**^\*^ - applies to:  - SharePoint sites and OneDrive accounts for retention policies  - SharePoint sites for auto-labeling policies | Site URL Site name  Site template  Custom properties (SharePoint only): RefinableString00 - RefinableString99 |
| **Microsoft 365 Groups** - applies to:  - Microsoft 365 Group mailboxes & sites  - Teams channel messages (standard, shared, and private [post-migration](retention-policies-teams#migration-of-private-channel-messages-in-2025))  - Viva Engage community messages | Name  Display name  Description  Email addresses  Alias  Exchange custom attributes: CustomAttribute1 - CustomAttribute15  Exchange Extension custom attributes: ExtensionCustomAttribute1 - ExtensionCustomAttribute5 |

^\*^[Records Center sites](https://support.microsoft.com/office/introduction-to-the-records-center-bae6ca5a-7b19-40e0-b433-e3613a747c2c) (legacy feature) in SharePoint aren't supported.

Note

For communication compliance policies:

- SharePoint sites and OneDrive accounts aren't supported.
- Excluded users and Microsoft 365 groups are supported.

The property names for sites are based on SharePoint site managed properties. For information about the custom attributes, see [Using Custom SharePoint Site Properties to Apply Microsoft 365 Retention with Adaptive Policy Scopes](https://techcommunity.microsoft.com/t5/security-compliance-and-identity/using-custom-sharepoint-site-properties-to-apply-microsoft-365/ba-p/3133970).

The attribute names for users and groups are based on [filterable recipient properties](/en-us/powershell/exchange/recipientfilter-properties#filterable-recipient-properties) that map to Microsoft Entra attributes. For example:

- **Alias** maps to the LDAP name **mailNickname** that displays as **Email** in the Microsoft Entra admin center.
- **Email addresses** maps to the LDAP name **proxyAddresses** that displays as **Proxy address** in the Microsoft Entra admin center.

You can easily specify the attributes and properties listed in the table when you configure an adaptive scope by using the simple query builder. The advanced query builder supports additional attributes and properties, as described in the following section.

### How to configure an adaptive scope

Before you configure your adaptive scope, use the previous section to identify what type of scope to create and what attributes and values to use. You might need to work with other administrators to confirm this information.

You need to assign the correct role groups to admins to create an adaptive scope. Any role group with the *Scope Manager* role can create an adaptive scope. The *Scope Manger* role is included in the following [built-in role groups](/en-us/microsoft-365/security/office-365-security/scc-permissions):

- Compliance Administrator
- Compliance Data Administrator
- Organization Management
- Records Management
- Communication Compliance
- Communication Compliance Admins

For SharePoint sites, there might be additional SharePoint configuration needed if you plan to use [custom site properties](https://techcommunity.microsoft.com/t5/security-compliance-and-identity/using-custom-sharepoint-site-properties-to-apply-microsoft-365/ba-p/3133970).

To create and configure adaptive scopes, use the following instructions.

1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Settings** &gt; **Roles and scopes** &gt; **Adaptive scopes**.
2. On the **Adaptive scopes** page, select **+ Create scope**.
3. Follow the prompts in the configuration where you're first asked to assign an administrative unit. If your account is [assigned administrative units](purview-admin-units#permissions-for-administrative-units), you must select one administrative unit that restricts the scope membership.

    Note

    Because administrative units don't yet support SharePoint sites, you can't create an adaptive scope for SharePoint sites if you select administrative units.

    If you don't want to restrict the adaptive scope by using administrative units, or your organization hasn't configured administrative units, keep the default of **Full directory**.
4. Select the type of scope, and then select the attributes or properties you want to use to build the dynamic membership. Type in the attribute or property values.

    For example, to configure an adaptive scope that identifies users in Europe, first select **Users** as the scope type. Then select the **Country or region** attribute, and type in **Europe**:

    ![Example adaptive scope configuration.](media/example-adaptive-scope.png)

    Once daily, this query runs against Entra ID and identifies all users who have the value **Europe** specified for in their account for the **Country or region** attribute.

    Important

    Because the query doesn't run immediately, there's no validation that you typed in the value correctly.

    Select **Add attribute** (for users and groups) or **Add property** (for sites) to use any combination of attributes or properties that are supported for their scope type. Use logical operators to build queries. The operators supported are **is equal to**, **is not equal to**, **starts with**, and **not starts with**. You can group selected attributes or properties. For example:

    ![Example adaptive scope configuration with groupings of attributes.](media/example-adaptive-scope-grouping.png)

    Alternatively, you can select **Advanced query builder** to specify your own queries:

    - For **User** and **Microsoft 365 Group** scopes: Use [OPATH filtering syntax](/en-us/powershell/exchange/recipient-filters). For example, to create a user scope that defines its membership by department, country/region, and state:

        ![Example adaptive scope with advanced query.](media/example-adaptive-scope-advanced-query.png)

        One of the advantages of using the advanced query builder for these scopes is a wider choice of query operators:

        - **and**
        - **or**
        - **not**
        - **eq** (equals)
        - **ne** (not equals)
        - **lt** (less than)
        - **gt** (greater than)
        - **like** (string comparison)
        - **notlike** (string comparison)
    - For **SharePoint sites** scopes: Use Keyword Query Language (KeyQL). You might already be familiar with using KeyQL to search SharePoint by using indexed site properties. To help you specify these KeyQL queries, see [Keyword Query Language (KeyQL) syntax reference](/en-us/sharepoint/dev/general-development/keyword-query-language-kql-syntax-reference).

        For example, because SharePoint site scopes automatically include all SharePoint site types, which include Microsoft 365 group-connected and OneDrive sites, you can use the indexed site property **SiteTemplate** to include or exclude specific site types. The templates you can specify:

        - `SITEPAGEPUBLISHING` for modern communication sites
        - `GROUP` for Microsoft 365 group-connected sites
        - `TEAMCHANNEL` for Microsoft Teams private channel sites
        - `STS` for a classic SharePoint team site
        - `SPSPERS` for OneDrive sites

        So to create an adaptive scope that includes only modern communication sites and excludes Microsoft 365 group-connected and OneDrive sites, specify the following KeyQL query:

        ```console
        SiteTemplate=SITEPAGEPUBLISHING
        ```

        You can validate these advanced queries independently from the scope configuration.

        Note

        You must use the advanced query builder if you want to exclude inactive mailboxes. Or conversely, target just inactive mailboxes. For this configuration, use the OPATH property *IsInactiveMailbox*:

        - To exclude inactive mailboxes, make sure the query includes: `(IsInactiveMailbox -eq "False")`
        - To target just inactive mailboxes, specify: `(IsInactiveMailbox -eq "True")`
5. Create as many adaptive scopes as you need. You can select one or more adaptive scopes when you create your policy.

It can take up to five days for the queries to fully populate and changes aren't immediate. Factor in this delay by waiting a few days before you add a newly created scope to a policy.

Tip

For the data lifecycle management and records management solutions, use the [policy lookup option](retention#policy-lookup) to help you identify policies that are currently assigned to specific users, sites, and Microsoft 365 groups.

### Validate advanced queries

You can manually validate advanced queries by using PowerShell and SharePoint search:

- Use PowerShell for the scope types **Users** and **Microsoft 365 Groups**
- Use SharePoint search for the scope type **SharePoint sites**

#### To run a query by using PowerShell

1. [Connect to Exchange Online PowerShell](/en-us/powershell/exchange/connect-to-exchange-online-powershell) by using an account with [appropriate Exchange Online Administrator permissions](/en-us/powershell/exchange/find-exchange-cmdlet-permissions#use-powershell-to-find-the-permissions-required-to-run-a-cmdlet).
2. Use either [Get-Recipient](/en-us/powershell/module/exchange/get-recipient), [Get-Mailbox](/en-us/powershell/module/exchange/get-mailbox), or [Get-User](/en-us/powershell/module/exchange/get-user) with the *-Filter* parameter and your [OPATH query](/en-us/powershell/exchange/filter-properties) for the adaptive scope enclosed in curly brackets (`{`,`}`). If your attribute values are strings, enclose these values in double or single quotes.

    You can determine whether to use Get-Mailbox, Get-Recipient, or Get-User for validation by identifying which cmdlet is supported by the [OPATH property](/en-us/powershell/exchange/filter-properties) that you choose for your query.

    Important

    Get-Mailbox doesn't support the *MailUser* recipient type, so you must use Get-Recipient or Get-User to validate queries that include on-premises mailboxes in a hybrid environment.

    To validate a **User** scope, use the appropriate command:

    - `Get-Mailbox` with *-RecipientTypeDetails UserMailbox,SharedMailbox,RoomMailbox,EquipmentMailbox*
    - `Get-Recipient` with *-RecipientTypeDetails UserMailbox,MailUser,SharedMailbox,RoomMailbox,EquipmentMailbox*

    To validate a **Microsoft 365 Group** scope, use:

    - `Get-Mailbox` with *-GroupMailbox* or `Get-Recipient` with *-RecipientTypeDetails GroupMailbox*

    For example, to validate a **User** scope related to the **Department** attribute set to the value **Marketing**, you could use:

    ```PowerShell
    Get-Recipient -RecipientTypeDetails UserMailbox,MailUser -Filter {Department -eq "Marketing"} -ResultSize Unlimited
    ```

    To validate a **User** scope related to the **EmailAddresses** attribute generally requires the value to include the **smtp:** prefix. For example to **exclude** a user where EmailAddresses includes **admin@contoso.com**:

    ```PowerShell
    Get-Mailbox -RecipientTypeDetails UserMailbox -Filter {EmailAddresses -notlike "smtp:admin@contoso.com"} -ResultSize Unlimited
    ```

    To validate a **Microsoft 365 Group** scope related to the group's **CustomAttribute15** attribute set to **Marketing** as the value, you could use:

    ```PowerShell
    Get-Mailbox -RecipientTypeDetails GroupMailbox -Filter {CustomAttribute15 -eq "Marketing"} -ResultSize Unlimited
    ```

    Tip

    When you use these commands to validate a user scope, if the number of recipients returned is higher than expected, it might be because it includes users who don't have a valid license for adaptive scopes. These users don't have the policy settings applied to them.

    For example, in a hybrid environment, you might have unlicensed synchronized user accounts without an Exchange mailbox on-premises or in Exchange Online. You can identify these users by running the following command: `Get-User -RecipientTypeDetails User`
3. Verify that the output matches the expected users or groups for your adaptive scope. If it doesn't, check your query and the values with the relevant administrator for Microsoft Entra ID or Exchange.

    Note

    The output from these commands might not match the member list for the same filter within the scope details on the Adaptive Scopes page. The member list in scope details shows arbitration mailboxes in scope whereas the command output doesn't. Moreover, adaptive scope query changes can take up to five days to become effective and reflected in the scope details view of the Adaptive Scopes page.

#### To run a query by using SharePoint search

1. Using an account that has the SharePoint admin role, go to `https://<your_tenant>.sharepoint.com/search`.
2. Use the search bar to specify your KeyQL query.
3. Verify that the search results match the expected site URLs for your adaptive scope. If they don't, check your query and the URLs with the relevant administrator for SharePoint.

### View adaptive scope membership details

After creating a query for an adaptive scope in Microsoft Purview, you can view the member details of the scope.

Complete the following steps to access the member details page of an adaptive scope in Microsoft Purview:

1. [Sign in to the Microsoft Purview portal](https://purview.microsoft.com), if you're not already signed in.
2. Select **Settings** &gt; **Roles and scopes** &gt; **Adaptive scopes**.
3. Select an existing adaptive scope from the list.
4. From the **Details** flyout pane, select **Scope details**.
5. A list of scope members is shown. Review the **State** column in the list that shows **Added** for members within the adaptive scope or **Removed** if the member was previously in the adaptive scope but removed now they no longer match the scope query.
6. Optionally, use the **Export** option to download a list of the displayed scope members to a CSV file.

    If the scope membership is large (1,000 or more), or you want to customize the export, use the PowerShell cmdlet [Get-AdaptiveScopeMembers](/en-us/powershell/module/exchangepowershell/get-adaptivescopemembers).

Note

It might take up to five days for the member details list to update added or removed members. The adaptive scope can apply to more than 1 million members. However, the member details can only show up to 1 million members across both added and removed members.
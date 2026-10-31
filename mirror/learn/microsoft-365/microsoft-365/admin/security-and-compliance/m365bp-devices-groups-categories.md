---
layout: Conceptual
monikers:
- o365-21vianet
- o365-worldwide
defaultMoniker: o365-worldwide
versioningType: Ranged
title: Device groups and Intune categories in Microsoft 365 Business Premium - Microsoft 365 admin | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/m365bp-devices-groups-categories?view=o365-worldwide
config_moniker_range: =o365-worldwide || =o365-21vianet
feedback_system: Standard
feedback_product_url: https://admin.microsoft.com/adminportal/home?showfeedback=DocsMacCampaign
breadcrumb_path: /microsoft-365/breadcrumb/toc.json
recommendations: false
uhfHeaderId: MSDocsHeader-M365-IT
description: In Microsoft 365 Business Premium, learn about device groups in Defender for Business and categories in Microsoft Intune.
search.appverid: MET150
ms.author: vpattnaik
author: vpattnai
manager: dansimp
audience: Admin
ms.topic: how-to
ms.service: m365-core
ms.subservice: security
ms.date: 2025-08-14T00:00:00.0000000Z
ms.localizationpriority: medium
ms.reviewer: nehabha
f1.keywords: NOCSH
ms.collection:
- SMB
- m365-security
- tier2
- trust-pod
ms.custom: security
locale: en-us
document_id: 9391d9dd-f14b-9d67-79cb-729ec5a9374e
document_version_independent_id: 9391d9dd-f14b-9d67-79cb-729ec5a9374e
original_content_git_url: https://github.com/MicrosoftDocs/microsoft-365-docs-pr/blob/live/microsoft-365/admin/security-and-compliance/m365bp-devices-groups-categories.md
default_moniker: o365-worldwide
site_name: Docs
depot_name: office.Microsoft-365-docs
page_type: conceptual
toc_rel: ../toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/office.Microsoft-365-docs/{branchName}{pdfName}
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: admin/security-and-compliance/m365bp-devices-groups-categories
moniker_range_name: 626dcefb463b053bbc5c86fb8d873ef6
monikers:
- o365-21vianet
- o365-worldwide
item_type: Content
source_path: microsoft-365/admin/security-and-compliance/m365bp-devices-groups-categories.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/68cb9039-df60-49b0-8ef8-89ad96497f63
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c671beaa-a830-4c9f-aceb-97379ee031ca
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/725b6df3-93e8-472d-834e-e7e0d2953d35
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/8921374c-4dbe-4ed0-b011-a39e18bfbd98
platformId: ea7fb397-e1dd-18ef-c9ef-402eebeb8d7e
---

# Device groups and Intune categories in Microsoft 365 Business Premium - Microsoft 365 admin | Microsoft Learn

Microsoft 365 Business Premium includes device endpoint protection through Microsoft Defender for Business and Microsoft Intune Plan 1. Device protection policies are applied to devices through different types of device collections:

- **Device groups in Defender for Business**: There are two types of device groups:

    - **Dynamic device groups**: You create dynamic device groups with one or more rules that use available device properties to identify the members of the group (devices, not users). During device enrollment or if the properties of the device change, the device is automatically added to or removed from the group. For more information, see the Dynamic device groups section later in this article.
    - **Assigned device groups**: You create and manually add or remove onboarded devices to and from the device group.
- **Device categories in Intune**: Require corresponding dynamic device groups in Microsoft Entra. The rule condition uses the device category name, so all devices that have the category assigned are automatically members of the dynamic device group.

The rest of this article explains device groups in Defender for Business, device categories in Intune, and how to manage them.

## Device groups in Defender for Business

Defender for Business in Business Premium contains the built-in device group named **All Devices** assigned to the built-in [device protection policies](m365bp-devices-protection) named **NGP Windows default policy** and **Firewall Windows default policy**. This device group includes all devices that are onboarded in Defender for Business.

You can also create custom device groups to use in the built-in device protection policies or in custom protection policies. You can create device groups in the following locations:

- In the Defender portal when you create or edit device protection policies at https://security.microsoft.com/policy-management. You don't need to complete creating or modifying the device protection policy to create new device groups.
- In the Microsoft Entra admin center at https://entra.microsoft.com/#view/Microsoft_AAD_IAM/GroupsManagementMenuBlade.

Tip

- Device groups created in the Defender portal are available to view, modify, and delete in the Microsoft Entra admin center.
- Device groups created in the Microsoft Entra admin center aren't available in the Defender portal unless you modify the **Mail Nickname** property using Microsoft Graph PowerShell. For more information, see the Create device groups in the Microsoft Entra admin center section later in this article.
- The built-in device group named **All Devices** isn't available in the Microsoft Entra admin center, and isn't available to use in custom device protection policies. **All Devices** is available to use only in the built-in device protection policies named **NGP Windows default policy** and **Firewall Windows default policy**.

### Dynamic device groups

Dynamic device groups use one or more rules based on device properties (not user properties) to identify the devices that belong to the group. A rule in a dynamic device group uses the following syntax: `'<Property>' '<Operator>' '<Value>'`:

- **Property** is the device characteristic that you want to use as an identifier.
- **Operator** is a comparison operator.
- **Value** is the text or numeric value of the property.

For example, **'Device OS Type' 'equals' 'Windows'**.

In the Defender portal, multiple rules in a dynamic device group use AND logic. A device must match **all** of the specified rules to be included in the dynamic device group. In the Microsoft Entra admin center, you can use a combination of AND and OR logic for multiple rules.

Creating dynamic device groups in the Defender portal is simplified but limited as compared to creating dynamic device groups in the Microsoft Entra admin center. The differences are summarized in the following table:

| - | Defender portal | Microsoft Entra admin center |
| --- | --- | --- |
| Properties | A subset of available Microsoft Entra ID device properties. | All available Microsoft Entra ID device properties. |
| Operators | A subset of available Microsoft Entra ID operators, and limited operators for each property. For example, the **Device OS Type** property is limited to the operator value **In**. | All available Microsoft Entra ID operators. |
| Values | Mostly free text. The **Device OS Type** property is limited to the values **Windows** or **Windows Server**^\*^. | Free text for all values. |
| Logical operator for multiple rules | AND (not selectable) | AND or OR (selectable for each rule) |

Details about dynamic device groups in the Defender portal vs. the Microsoft Entra admin center are explained in the following subsections.

#### Dynamic device groups in the Defender portal

As you create or edit [device protection policies](m365bp-devices-protection) in the Defender portal, the following dynamic device group elements are available:

- **Property**:

    - **Device OS Type**: One or both of the following values:
        - **Windows**
        - **Windows Server**^\*^
    - **Device Display name**: Text.
    - **Device Model**: Text.
    - **Device OS Version**: Text.
    - **Device Id**: A valid Microsoft Entra device ID. For example, `d4fe7726-5966-431c-b3b8-cddc8fdb717d`.
- **Operator**:

    - **Equals**: The property value must match the specified value exactly.
    - **Not Equals**: The property value doesn't match the specified value.
    - **Starts With**: The beginning of the property value contains the specified value.
    - **Not Starts With**: The beginning of the property value doesn't contain the specified value.
    - **In**: The property value is included in any of the specified values (multiple values).
    - **Not In**: The property value isn't included in any of the specified values.

    The available operators in dynamic device groups in the Defender portal depend on the property as described in the following table:

    | Property | Equals | Not Equals | Starts With | Not Starts With | In | Not In |
    | --- | --- | --- | --- | --- | --- | --- |
    | **Device OS type** |  |  |  |  | ✔ |  |
    | **Device Display name** | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
    | **Device Model** | ✔ | ✔ | ✔ | ✔ |  |  |
    | **Device OS Version** | ✔ | ✔ | ✔ | ✔ |  |  |
    | **Device Id** | ✔ | ✔ | ✔ | ✔ |  |  |
- **Value**: The text or numeric value of the property you selected, or the default value **Any** for most properties. The **Device OS Type** property is limited to the values **Windows** and **Windows Server**^\*^.

To create dynamic device groups in the Defender portal, see the Create device groups in the Microsoft Defender portal section.

^\*^ Protecting Windows Server operating systems require an extra license not included in Defender for Business or Business Premium (for example, [Microsoft Defender for Business servers](/en-us/defender-business/get-defender-business#how-to-get-microsoft-defender-for-business-servers)).

### Device groups in the Microsoft Entra admin center

In the Microsoft Entra admin center, you can modify and remove dynamic or assigned device groups while you create or modify device protection policies. For instructions, see the following articles:

- **Remove device groups**: [Delete a group](/en-us/entra/fundamentals/how-to-manage-groups#delete-a-group)
- **Modify device groups**:
    - [Edit group settings](/en-us/entra/fundamentals/how-to-manage-groups#edit-group-settings)
    - **Dynamic device groups**: You can modify the rules with more available device properties, operators, and an available mixture of AND and OR logic for multiple rules. For more information, see the following articles:
        - [Update rules in existing dynamic membership groups](/en-us/entra/identity/users/groups-create-rule#to-update-an-existing-rule).
        - [Properties for device rules](/en-us/entra/identity/users/groups-dynamic-membership#rules-for-devices)
        - [Supported expression operators](/en-us/entra/identity/users/groups-dynamic-membership#supported-expression-operators)
        - [Validate rules for dynamic membership groups in Microsoft Entra ID](/en-us/entra/identity/users/groups-dynamic-rule-validation).
    - **Assigned device groups**: [Add members](/en-us/entra/fundamentals/how-to-manage-groups#add-members-or-owners-of-a-group).

To create device groups in the Microsoft Entra admin center, see the Create device groups in the Microsoft Entra admin center section later in this article.

### Create device groups in the Microsoft Defender portal

There's no direct location to create device groups in the Defender portal. Instead, you can create device groups while you create or edit device protection policies on the **Windows** tab of the **Device configuration** page. For more information about creating or editing device protection policies, see [Device protection policies in Microsoft 365 Business Premium](m365bp-devices-protection).

1. In the Microsoft Defender portal at https://security.microsoft.com, go to **Endpoints** &gt; **Configuration management** &gt; **Device configuration**. Or, to go directly to the **Device configuration** page, use https://security.microsoft.com/policy-management.
2. On the **Windows** tab of the **Device configuration** page, do one of the following steps in the **Next-generation protection** or **Firewall** sections:

    - **Create a new policy**: Select ![](../../media/m365-cc-sc-create-icon.png)**Add**.
    - **Edit an existing policy**: Do one of the following steps:
        - Select a policy from the list by clicking on the check box next to the policy name, and then select the ![](../../media/m365-cc-sc-edit-icon.png)**Edit** action that appears.
        - Select a policy from the list by clicking anywhere in the row other than the check box next to the policy name. In the details flyout that opens, select ![](../../media/m365-cc-sc-edit-icon.png)**Edit** at the top of the flyout.
3. On the **General information** page, review or modify the **Policy name**, **Description**, or **Policy order** settings, and then select **Next**.
4. On the **Device groups** page, do the following steps:

    1. Select ![](../../media/m365-cc-sc-create-icon.png)**Create new group**.
    2. On the **Create new group**page that opens, configure the following settings:
        - **Group name**: The unmodifiable prefix is **MDE Windows**. Enter a unique, descriptive suffix for the device group name.
        - **Description**: Enter an optional description for the device group.
        - **Membership type**: Select one of the following values:
            - **Dynamic group**: Devices are automatically added and removed based on rules.
            - **Assigned group**: You manually add and remove existing devices.

    When you're finished on the **Create new group** page, select **Next**.
5. On the **Targeted devices** page, the available options depend on the **Membership type** value you selected on the previous page:

    - **Dynamic group**: Configure one or more rules as described in the Dynamic device groups in the Defender portal section earlier in this article:

        - Select **Select Property**. In the drop-down list that appears, select an available property.
        - Select **Select an operator**. In the drop-down list that appears, select an available operator.
        - The value control appears with the default value **Any**. Leave the value **Any** selected, or click on **Any**, and in the dialog that appears, select or enter the value, and then select **Apply**.

            To add another rule, select ![](../../media/m365-cc-sc-create-icon.png)**Add filter** and then repeat the previous steps. Multiple rules use the AND logical operator (a device must match **all** of the specified rules to be included in the dynamic device group).

            Tip

            Typically, you don't want to use the same property more than once in one dynamic device group that you create in the Defender portal. It's too easy to create conflicting rules that devices can never meet.

            To remove an existing complete rule, select ![](../../media/m365-cc-sc-remove-selection-icon.png) next to the rule.

            To remove a partial rule, select ![](../../media/m365-cc-sc-delete-icon.png)**Delete** next to the rule.

            To clear all existing rules, select ![](../../media/m365-cc-sc-remove-icon.png)**Clear all**, and then select a property from the **Properties** drop down list in the **Select a filter** dialog that appears.
    - **Assigned group**: Select one or more enrolled devices from the list. You can sort the list of enrolled devices by clicking on an available column header:

        - **Device name**
        - **Domain**
        - **Primary user**
        - **IP address**

        Tip

        You can't create assigned device groups unless there are enrolled devices to select as members.

    When you're finished on the **Targeted devices** page, select **Create group**.
6. If there are no errors, you return to the **Device groups** page where the device group you created is listed on the page and is now selected in ![](../../media/m365-cc-sc-add-internal-icon.png)**Use existing group**.

    You can take the following actions on the device groups listed on the **Device groups** page:

    - Select **⋮** &gt; **Edit** to edit the device group.
    - Select **⋮** &gt; **Group details** to open a flyout that shows the devices that are included in the device group.
    - Select **Remove** to remove the device group from the list. If you do this action, you need to do one of the following steps before you can select **Next**to go to the next page in the wizard:
        - Select ![](../../media/m365-cc-sc-create-icon.png)**Create new group** to create another device group.
        - Select ![](../../media/m365-cc-sc-add-internal-icon.png)**Use existing group** to select one or more device groups to use in this protection policy.
7. At this step in creating the device protection policy, you have the following options on the **Device groups** page:

    - Select **Next** to continue creating or modifying the device protection policy as described in [Device protection in Microsoft 365 Business Premium](m365bp-devices-protection) (starting at Step 4).
    - Select **Cancel** to stop creating or modifying the device protection policy. The new device group is available to select in new or existing device protection policies in the Defender portal, and is available in the Microsoft Entra admin center.

### Create device groups in the Microsoft Entra admin center

Although you can create dynamic and assigned device groups in the Microsoft Entra admin center, these groups aren't initially available to select when you create or edit device protection policies in the Defender portal.

Dynamic and assigned device groups in the Microsoft Entra admin center share the following settings:

- **Group type**: **Security** (default).
- **Microsoft Entra roles can be assigned to the group**: **No** (default).

Specific settings for each device group type are described in the following list:

- **Dynamic device groups**: [Create a rule for a dynamic membership group](/en-us/entra/identity/users/groups-create-rule#to-create-a-rule-for-a-dynamic-membership-group):

    - **Membership type**: **Dynamic Device** (Step 4).
- **Assigned device groups**: [Create a basic group and add members](/en-us/entra/fundamentals/how-to-manage-groups#create-a-basic-group-and-add-members):

    - **Membership type**: **Assigned** (default; Step 9).
    - **Members**: (Step 10): Select **No members selected**. On the **Add members** page that opens, select the **Devices** tab to select the devices to add to the group.

After you create the device group, you need to set the **Mail nickname** property to the value `MdeDeviceConfiguration` so the group is available to select when you create or edit device protection policies in the Defender portal. You take this action in Microsoft Graph PowerShell (you get an error if you try in the Microsoft Entra admin center). General instructions for modifying groups in PowerShell are in [Microsoft Entra version 2 cmdlets for group management](/en-us/entra/identity/users/groups-settings-v2-cmdlets):

1. If you haven't already, install the Microsoft.Graph.Groups PowerShell module by running the following command in Windows PowerShell:

    ```powershell
    Install-Module Microsoft.Graph
    ```
2. Connect to Microsoft.Graph.Groups PowerShell by running the following command:

    ```powershell
    Connect-MgGraph -Scopes "Group.ReadWrite.All"
    ```

    For detailed syntax and parameter information, see [Connect-MgGraph](/en-us/powershell/module/microsoft.graph.authentication/connect-mggraph).
3. Replace `<DisplayName>` with the display name of the group, and then run the following command to store the **Id** property value of the device group to the variable named `$ID`:

    ```powershell
    $ID = (Get-MgGroup -Filter "DisplayName eq '<DisplayName>'").Id
    ```

    For example:

    ```powershell
    $ID = (Get-MgGroup -Filter "DisplayName eq 'Engineering Dynamic Device Group'").Id
    ```

    You use the `$ID` value in the next step.

    For detailed syntax and parameter information, see [Get-MgGroup](/en-us/powershell/module/microsoft.graph.groups/get-mggroup).
4. Run the following command to change the **MailNickname** property value of the device group to `MdeDeviceConfiguration`:

    ```powershell
    Update-MgGroup -GroupId $ID -MailNickname MdeDeviceConfiguration
    ```

    For detailed syntax and parameter information, see [Update-MgGroup](/en-us/powershell/module/microsoft.graph.groups/update-mggroup).

## Device categories in Intune

Device categories in Intune require an associated dynamic device group in Microsoft Entra. After you create the device category in Intune, create a dynamic device group in the Microsoft Entra admin center that uses the following rule: **'deviceCategory' equals '&lt;DeviceCategoryName&gt;'**. For more information, see [Categorize devices into groups](/en-us/intune/intune-service/enrollment/device-group-mapping).

The steps are described in the following subsections.

### Step 1: Create the device category in Intune

1. In the Microsoft Intune admin center at https://intune.microsoft.com, go to **Devices** &gt; **Manage devices** &gt; **Device categories**. Or, to go directly to the **Device categories** page, use [https://intune.microsoft.com/#view/Microsoft_Intune_DeviceSettings/DevicesMenu/~/deviceCategories](https://intune.microsoft.com/#view/Microsoft_Intune_DeviceSettings/DevicesMenu/%7E/deviceCategories).
2. On the **Device categories** page, select ![](../../media/m365-cc-sc-create-icon.png)**Create device category** to start the new category wizard.
3. On the **Basics** tab, enter the following information:

    - **Name**: Enter a unique, descriptive name for the category.
    - **Description**: Enter an optional description for the category.

    When you're finished on the **Basics** tab, select **Next**.
4. On the **Scope tags** tab, optionally select a scope tag to limit management of the category to specific IT groups. For more information, see [Use RBAC and scope tags for distributed IT](/en-us/intune/intune-service/fundamentals/scope-tags).

    When you're finished on the **Scope tags** tab, select **Next**.
5. On the **Review + create** tab, review the settings. You can select **Previous** to go back and modify the settings.

    When you're finished **Review + create** tab, select **Create**.

Back on the **Device categories** page, the new device category appears in the list.

Tip

- To delete an existing device category, select ![](../../media/m365-cc-sc-more-actions-icon.png)**Context menu** &gt; ![](../../media/m365-cc-sc-delete-icon.png)**Delete**.

    After you delete the device category, devices that had the category assigned have the category value **Unassigned**.
- To modify an existing device category, select the category from the list by clicking anywhere in the row. On the **Properties** page that opens, select **Edit** in the **Basics** or **Scope tags** sections.

    If you change the name of the device category, be sure to update the dynamic device group that refers to the category (the **deviceCategory** value that's used in the rule).

### Step 2: Create a dynamic device group in Microsoft Entra that uses the Intune device category

1. In the Microsoft Entra admin center at https://entra.microsoft.com, go to **Groups** &gt; **All groups**. Or, to go directly to the **All groups** page, use [https://entra.microsoft.com/#view/Microsoft_AAD_IAM/GroupsManagementMenuBlade/~/AllGroups/menuId/AllGroups](https://entra.microsoft.com/#view/Microsoft_AAD_IAM/GroupsManagementMenuBlade/%7E/AllGroups/menuId/AllGroups).
2. On the **All groups** page, select ![](../../media/entra-new-group-icon.png)**New group**.
3. On the **New group** page, configure or verify the following options:

    - **Group type**: Verify **Security** is selected.
    - **Group name**" Enter a unique, descriptive name for the group.
    - **Group description**: Enter an optional description for the group.
    - **Microsoft Entra roles can be assigned to the group**: Verify **No** is selected.
    - **Membership type**: Select **Dynamic device**.
    - **Owners**: Optionally, select **No owners selected** to add one or more group owners.
    - **Dynamic device members**: Select **Add dynamic query**. On the **Configure rules** tab of the **Dynamic membership rules** page that opens, configure the following settings:

        - **Property**: **deviceCategory**
        - **Operator**: **Equals**
        - **Value**: The category name you created in Step 1:.

        Select ![](../../media/m365-cc-sc-save-icon.png)**Save**.

    Back on the **New group** page, select **Create**.

Back on the **All groups** page, the new dynamic device group appears in the list.

### How users select categories on devices

Tip

Admins can customize the Intune user experience to hide the category selection prompt in the Company Portal apps or website. For more information, see [Customizing the user experience: Device categories](/en-us/intune/intune-service/apps/company-portal-app#device-categories).

After an admin creates categories, users have the following options to select a category on their devices:

- **Company portal website on Windows, macOS, iOS, iPadOS, and Android devices**:

    1. Go to the **Devices** page of the Company Portal at https://portal.manage.microsoft.com/devices, and then do the following steps:
        1. If you haven't already, select the **Tap here to tell us which device you're using or add a new device** banner. In the **Which device are you using?** dialog that opens, select your device from the **Your managed devices** section, and then select **Select**.
        2. Back on the **Devices** page, select **This device**.
    2. On the device properties page that opens, select the **Category is unknown. Tap to select now** banner.
    3. In the **Choose the best category for this device** dialog that opens, select an available category, and then select **Select**.
- **Company Portal app on Windows devices**:

    1. If necessary, download and install the Company Portal app from the Microsoft Store at https://apps.microsoft.com/detail/9wzdncrfj3pz.
    2. Open the Company Portal app on the Windows device.
    3. On the **Choose the best category for this device** page that opens, select a category from the list, and then select **Done**.

After you choose a category, the device is automatically added to the corresponding dynamic device group.

Tip

Users can't change the category on their device. Only an admin can switch the device to a different category as described in the next section.

### How admins manage categories on devices

In the Microsoft Intune admin center at https://intune.microsoft.com, go to **Devices** &gt; **All devices**. Or, to go directly to the **All devices** page, use [https://intune.microsoft.com/#view/Microsoft_Intune_DeviceSettings/DevicesMenu/~/allDevices](https://intune.microsoft.com/#view/Microsoft_Intune_DeviceSettings/DevicesMenu/%7E/allDevices).

On the **All devices** page, admins can do the following category-related tasks:

- **View categories assigned to devices**: if the **Category** column isn't shown, select ![](../../media/entra-columns-icon.png)**Columns** &gt; **Categories**.

    You can also filter the results by selecting **Add filters** &gt; **Category**, selecting one or more categories, and then selecting **Apply**.
- **Change categories assigned to devices**: Select a device entry from the list by clicking on the **Device name** value. In the device details page that opens, select **Manage** &gt; **Properties**.

    On the **Properties** page that opens, find the **Device category** property. Select a device category or the value **Unassigned** from the drop-down list, and then select ![](../../media/m365-cc-sc-save-icon.png)**Save**.
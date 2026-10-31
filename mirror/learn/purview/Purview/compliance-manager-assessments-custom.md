---
layout: Conceptual
title: Build custom assessments (preview) in Microsoft Purview Compliance Manager | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/compliance-manager-assessments-custom
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-11-27T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-compliance-manager
ms.collection:
- purview-compliance
- m365solution-compliancemanager
- m365initiative-compliance
search.appverid:
- MOE150
- MET150
description: Build custom assessments (preview) by adding or modifying controls and improvement actions with Microsoft Purview Compliance Manager.
locale: en-us
document_id: 3469b96e-ede1-6a87-ccd0-1c8cf93bc56c
document_version_independent_id: 3469b96e-ede1-6a87-ccd0-1c8cf93bc56c
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/compliance-manager-assessments-custom.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: compliance-manager-assessments-custom
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/compliance-manager-assessments-custom.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/eab1aabc-e18c-405b-ac29-e35eb0b15e3b
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/574d2eb1-e22a-49c0-b4eb-64e86dbeee6b
platformId: e4ca9ebc-d326-ce62-cc03-69b12e5d92db
---

# Build custom assessments (preview) in Microsoft Purview Compliance Manager | Microsoft Learn

Compliance Manager provides the option to modify a regulatory template by adding controls and improvement actions to suit your needs for building a custom assessment. First you copy a regulation, then add controls and improvement actions and services, then publish it so that you can start using it for assessments. This article explains how to copy and modify a regulation in order to create a customized assessment.

## Customize a regulation

You can make changes to an existing [Microsoft regulatory template](compliance-manager-templates) in order to customize it for your needs. When you customize a regulation:

- It inherits all the controls and actions of the parent regulation.
- It inherits automatic updates to the Microsoft managed controls and automatically tested actions, except for any actions you modify.
- You can add more actions into a control that already exist in other controls.
- You can create your own actions and controls.
- You can add services.

Note

Copying a premium regulation activates the regulation for your organization and consumes a license for it. The license allows you to create multiple copies of a regulation, and build multiple assessments from a copied regulation. Learn more about [regulation licensing](compliance-manager-regulations#regulation-availability-and-licensing).

#### Updates and versioning

When you customize a regulation, it inherits all of the details, controls, and actions from the parent regulation. The customized regulation [receives updates](compliance-manager-assessments#accept-updates-to-assessments) from Microsoft when there are changes to the related regulation or product. However, if you modify an action that is [automatically tested](compliance-manager-improvement-actions#testing-type), your organization takes over testing and implementation, and the action doesn't receive updates by Microsoft.

Tip

We recommend not making changes to a copied and published regulation for now, as any udpates will not be reflected in versioning history. A versioning exprience that reflects all updates for customized regulations is in our product roadmap for the near future.

### Steps for customizing a regulation

1. In Compliance Manager, go to the **Regulations** page.
2. Select the checkbox next to the name of the regulation you want to customize.
3. Select **Customize regulation** above the list of regulations.
4. In the **Create a copy of...** dialog, select **Copy**.

The copy of the assessment is created and the assessment's details page opens.

The name of the regulation is automatically created, starting with "Extension," followed by the name of the regulation, followed by "Copy 1." For example, if you copy the ISO 27005:2018 regulation, the name of the copied regulation will be "Extension ISO 27005:2018 Copy 1."

Tip

After you publish the regulation, you can edit the copied regulation to change the title or modify the description.

The **Controls** tab lists all of the controls inherited from the original, or parent, regulation. The **Service** lists the services to which the assessment applies, and is where you can add more services to the assessment.

The copied regulation has a status of **Draft** and can't be used to build an assessment until you publish it. To search for your newly copied regulation on the **Regulations** page, set the **Status** filter to **Draft** to see it and any other copied yet unpublished regulations.

A copied regulation can't be deleted.

## Add controls

The **Controls** tab of the copied regulation's details page lists all the controls of the underlying regulation. You can add your own controls by following the steps below:

1. On the regulation's **Controls** tab, select **Create control**. The **Create control** flyout pane appears.
2. Enter a **Title** for the control.
3. Enter a **Control ID**. This must be a unique number, up to 150 characters. The ID can't belong to any existing control in this assessment or in any other regulation.
4. Select a control family from the dropdown menu. If the control family name you want isn't listed as an option, you can create a new family name as follows:

    - Select **Create new** from the **Control family** dropdown menu.
    - Enter a name for the new family in the **Control family name** field. This control family name will be added as a dropdown option after you create the control.
5. Enter an optional **Description** for the control.
6. Select **Create**.

After creating the control, you arrive at the details page for the control you created. The next step is to link improvement actions to the control.

## Add improvement actions to controls

On the **Your improvement actions** tab of the control details page, you can import actions from the parent regulation, or you can create your own actions.

### Import actions

You can import any of the other improvement actions that exist in other controls within the parent regulation into a control. Select **Import actions**. On the **Select actions to import** flyout pane, you can select all the actions by checking the box next to the **Improvement actions** column header. You can also check individual actions by selecting the checkbox next to the names.

After selecting your desired actions, select **Import**.

### Create actions

You can create your own improvement actions to add to your copied regulation by following the steps below.

1. Enter a **Title** for the improvement action.
2. Select a **Score** value from the dropdown menu. Score values represent the maximum number of points awarded for action completion. Values are assigned based on whether the action is preventative, detective, or corrective actions, and whether they're mandatory or discretionary. Refer to this [explanation of score values](compliance-manager-scoring#how-score-values-are-determined) to see which number is assigned to which type of action.
3. At **Services**, select a service from the dropdown menu that the action applies to.
4. If the action applies to the Microsoft 365 service, then at **Solution**, select the appropriate solution from the dropdown menu.
5. Enter an optional **Description** for the action.
6. Select **Create**.

After the action is created, you arrive back at the control details page, and the improvement action you just created is listed on the **Your improvement actions** tab.

## Add services

The **Services** tab lists the services that apply to the parent regulation. You can add a service that is available for that regulation by selecting **Add available services** and selecting one or more services. If there aren't any services listed, you can create a service and add it to the regulation.

To create your own service, select **Create service**. On the flyout pane, enter a name and description for the service, then select **Save**. After you publish regulation, the added service will be an available option if you make more copies of the same regulation.

## Finalize changes by publishing

After adding controls and connecting improvement actions to the regulation you copied, you need to publish the changes in order to begin using the extended regulation for assessments.

1. Go to the details page of the extended regulation.
2. Select **Publish template** in the upper right corner.

After you publish the template, it will be listed on the **Regulations** page and it will be ready for assessment creation. The status of the regulation, which is a filter option, is now **Ready to use** instead of **Draft**.

Simple ways to search for a copied regulation on your **Regulations** page include:

- Set the **Created by** filter to your name.
- Select the **Includes custom content** column to sort by the **True** value. True indicates that the regulation has been customized.

Note

You can't create an assessment from a copied regulation until you publish it by selecting **Publish template**.

## Edit a copied regulation

After you publish a copied regulation, you can change its name, modify its description, and continue to add and edit controls and actions. To edit a regulation, select it from the list on the **Regulations** page. On the regulation details page, select the ellipsis (...) in the top right corner and select **Edit regulation**.

At this point, a working copy of the regulation is made so that you can make edits and save your work in progress without overriding the published copy. When you're done making edits, you need to again publish it by selecting **Publish template** in the upper right corner. When you select **Publish template**, a **Review and publish** flyout pane appears, where you can review your changes and add publishing notes. Select **Publish template** on the flyout pane to save the changes and republish your regulation.

## Creating multiple copies of the same regulation

You can create multiple copies of a regulation so that you can customize it in different ways. You might want to have multiple versions of a regulation if you want to create different control configurations or include only certain services for the same regulation, and then create assessments based off of those extensions.

Multiple copies are automatically named with numbers appended to the name. For example, if you create two copies of the ISO 27005:2018 regulation, they're named as follows: "Extension ISO 27005:2018 Copy 1" and "Extension ISO 27005:2018 Copy 2."

We recommend editing the descriptions of extended regulations so that you can clearly identify how they differ or what they're intended to assess. To edit the description:

1. Go to the regulation's details page.
2. In the **Overview** section, under **Details**, select **Edit details**. The **Edit template details** flyout pane appears.
3. In the **Description** field, enter a detailed description.
4. Select **Save**.
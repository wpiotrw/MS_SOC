---
layout: Conceptual
title: Learn about regulations in Microsoft Purview Compliance Manager | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/compliance-manager-regulations
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2024-11-04T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.custom:
- admindeeplinkMAC
- sfi-ga-flagged
ms.service: purview
ms.subservice: purview-compliance-manager
ms.collection:
- purview-compliance
- m365solution-compliancemanager
- m365initiative-compliance
search.appverid:
- MOE150
- MET150
description: Understand how to use and manage regulatory templates for building assessments in Microsoft Purview Compliance Manager.
locale: en-us
document_id: 4476387b-9baa-23a2-e6f2-c52131b0f443
document_version_independent_id: 4476387b-9baa-23a2-e6f2-c52131b0f443
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/compliance-manager-regulations.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: compliance-manager-regulations
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/compliance-manager-regulations.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/eab1aabc-e18c-405b-ac29-e35eb0b15e3b
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/574d2eb1-e22a-49c0-b4eb-64e86dbeee6b
platformId: 3a5b1478-6c7a-e49b-2f70-e6b0db7724a2
---

# Learn about regulations in Microsoft Purview Compliance Manager | Microsoft Learn

Important

The regulations that are available for your organization's use by default depend on your licensing agreement. [Review licensing details](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description#microsoft-purview-compliance-manager).

## Regulations overview

The **Regulations** page in Compliance Manager displays the list of regulations and certifications for which Compliance Manager provides control-mapping templates. When you build an assessment, you choose the underlying regulation by selecting from among our [set of regulatory templates](compliance-manager-regulations-list), then select the services you want to assess for that regulation. Setting up Compliance Manager for multicloud support provides you with greater automation in testing and monitoring of controls.

Each regulatory template also comes in a universal version, which provides general control mapping that can broadly apply to services. Universal templates provide the most general type of implementation guidance and require manual implementation and testing by the organization. Note that US Government Community (GCC) Moderate, GCC High, and Department of Defense (DoD) customers can't currently use universal templates.

## List of regulations

Visit [Compliance Manager regulations list](compliance-manager-regulations-list) to see the list of all regulatory templates available for building assessments.

For organizations with unique compliance needs, you can also create custom regulation templates. Learn more about [creating regulation templates](compliance-manager-create-template).

## Regulation availability and licensing

The Microsoft **Data Protection Baseline** regulatory template is available for organizations at all subscription levels to use. The regulations designated as **premium** require purchase of a license to use them.

On the **Regulations** page in Compliance Manager, the regulations are grouped under four headings:

- **Sub-service compliance readiness**: Use these to help assess your [predeployment compliance posture (preview)](compliance-manager-predeployment-compliance) (does not involve use of a license).
- **Included templates**: The [Microsoft data protection baseline](compliance-manager-assessments#data-protection-baseline-default-assessment).
- **Premium AI templates**: To use for [assessments for AI regulations](compliance-manager-assessments#assessments-for-ai-regulations).
- **Premium templates**: All other [global, regional, and industry regulations](compliance-manager-regulations-list#list-of-regulations-and-where-to-find-them).

When you purchase a license for a regulatory template, you can create as many assessments for that regulation as you wish. Depending on your licensing agreement, your organization might be able to use up to three more **premium** regulatory templates for free. When you begin creating assessments, Compliance Manager tracks how many templates are active so you can monitor your usage.

##### Resources

- Learn more about [included regulations by subscription level](compliance-manager-regulations-list#included-regulations).
- Go to the [Compliance Manager service description](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description#microsoft-purview-compliance-manager).
- Understand your regulation usage through active and inactive regulation status.

### Purchasing premium regulations

Licenses for premium regulatory templates can be obtained in various ways, depending on your Compliance Manager licensing agreement. Once your purchase has been finalized, the templates should become available in your tenant within 48 hours. Licenses for activated regulations are good for one year.

- **Commercial and GCC Moderate**: Purchase licenses in the admin center ([learn more about subscriptions, licenses, and billing](/en-us/microsoft-365/commerce/)). Select the quantity of licenses you wish to purchase and your payment plan.
    - [Commercial](https://admin.microsoft.com/Adminportal/Home#/catalog/offer-details/compliance-manager-premium-assessment-add-on/46E9BF2A-3C8D-4A69-A7E7-3DA04687636D)
    - [GCC Moderate](https://admin.microsoft.com/Adminportal/Home?#/catalog/offer-details/compliance-manager-premium-assessment-add-on/3129986d-5f4b-413b-a34b-b706db5a7669)
    - You can also acquire licenses through your participation in the [Cloud Solution Provider program](https://partner.microsoft.com/membership/cloud-solution-provider) or [volume licensing](https://www.microsoft.com/licensing/licensing-programs/licensing-programs).
- **GCC High and DOD accounts**: Purchase through [volume licensing](https://www.microsoft.com/licensing/licensing-programs/licensing-programs).

##### Staring a premium trial

You can try out premium regulation templates by acquiring trial versions of the licenses. Trial licenses are good for up to 25 templates for 90 days. Once you obtain your trial license, the templates should become available in your tenant within 48 hours. If your organization has a commercial license for Compliance Manager, you can learn how to start your trial at [About the free trial for Microsoft Purview Compliance Manager premium assessments](compliance-easy-trials-compliance-manager-assessments). If your organization is under a GCC or DOD license, choose the appropriate trial link for your organization:

- [GCC Moderate](https://admin.microsoft.com/Adminportal/Home?#/catalog/offer-details/compliance-manager-premium-assessment-add-on/87ed2908-0a8d-430a-9635-558ed42b581f)
- [GCC High](https://portal.office365.us/SubscriptionDetails?OfferId=e14362d7-2c11-4a43-9c92-59f1b499b96a)
- [DOD](https://portal.apps.mil/Commerce/Trial.aspx?OfferId=17e28290-7de6-41a9-af30-f6497396ab2e)

## Active and inactive regulations

Regulations display a status as either active or inactive:

- **Active** indicates use in at least one assessment.
- **Inactive** indicates it's not being used for an assessment.

When you use a premium regulation to create an assessment, that regulation's availability status changes to **Active** and the purchased license is active for one year. Your purchase renews automatically unless you cancel.

## Regulation licenses counter

The **Regulation licenses used** counter near the top of the **Regulations** page represents the number of regulatory templates in use out of the number you're eligible to use according to your licensing agreement and any purchased licenses. For example, if your counter shows 2/5, it means your organization has activated two regulations out of the five that are available to use. If your counter shows 5/2, it indicates that your organization exceeds its limits and needs to purchase three of the premium regulations in use.

Select **View details** the counter to view a detailed list of all regulations in use and their corresponding assessments.

## Regulations details page

Select a regulation from the list on the **Regulations** page to open a regulation's details page. Regulatory templates that belong to the same regulation family are counted as one template. The regulation family is shown in the **Overarching regulation** column on the **Assessment templates** page. When you purchase a template license for a regulation and activate the template, it counts as one activated template even if you create assessments for different levels or versions of that regulation. For example, if you use a template for CMMC Level 1 and a template for CMMC Level 2, your activated templates counter increases by only one.

For more information, see [Compliance Manager licensing guidance](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description#microsoft-purview-compliance-manager).

## Grant user access to regulations

When you assign users a Compliance Manager role in the Microsoft Purview portal, their role extends by default to all regulations (review the [Compliance Manager role types](compliance-manager-setup#role-types)). This access means that, depending on the user's role type, they can view or interact with any existing or future assessments created with that regulation.

You can give users a specific role that applies to certain regulations by managing user roles from a regulation's details page. When you set a user's role for a regulation, the user will be able to interact at that role level for all assessments (existing and future) created with that regulation. (You can also restrict access to individual assessments following [these instructions](compliance-manager-assessments#grant-user-access-to-individual-assessments).)

External users who need access for auditing or other purposes can also be assigned an access role for regulations. You provide access to external individual by assigning them a Microsoft Entra role. Learn more about [assigning roles](compliance-manager-setup#set-user-permissions-and-assign-roles).

#### Steps for granting access

Follow the steps to grant user access to a regulation.

1. From the **Regulations** page, find the regulation you want to grant access to. Select it to open its details page.
2. In the upper-right corner, select **Manage user access**.
3. A **Manage user access** flyout pane appears. It has three tabs, one for each role of Reader, Assessor, and Contributor. Navigate to the tab for the role you want your user to hold for this regulation.
4. Select the **+ Add** command for the role tab you're on: **Add readers**, or **Add assessors** or **Add contributors**.
5. Another flyout pane appears which lists all the users in your organization. You can select the checkbox next to the username you want to add, or you can enter their name in the search bar and select the user from there. You can select multiple users at once.
6. After making all your selections, select **Add**.

    Note

    If you assign a role to someone who already has an existing role, the new role assignment you choose will override their existing role. In this case, you'll see a confirmation box asking you to confirm the change in role.
7. The flyout pane closes and you arrive back at the regulation details page. Select **Save**. A confirmation message at the top confirms the new role assignment for that regulation.

#### Steps for removing access

You can remove a user's access to individual regulations by following these steps:

1. On the regulation's details page, select **Manage user access**.
2. On the **Manage user access** flyout pane, go the tab corresponding to the user's role you want to remove.
3. Find the user whose role you want to remove. Check the circle to the left of their name, then select the **Remove** command just below the role tab. To remove all users at once, select the **Remove all** command without checking the circle next to every user's name.
4. A **Remove access?** dialog appears, asking you to confirm the removal. Select **Remove access** to confirm the role removal.
5. Select **Save** on the flyout pane. The users' roles will now be removed from the assessment.

##### Note about multiple roles

- A user can have one role that applies to a regulation, while also holding another role that applies broadly to overall Compliance Manager access.

    - For example, if you've assigned a user a **Compliance Manager Reader** role, you can also assign that user a **Compliance Manager Assessor** role for a specific regulation. In effect, the user holds the two roles at the same time, but their ability to edit data will be limited to the assessment to which they've been assigned the **Assessor** role.
    - Removing a regulation-based role won't remove the user's overall Compliance Manager role if they have one. If you want to change a user's overall role, you have to change it in the Microsoft Purview portal. Learn more about [assigning roles and permissions](purview-permissions).
- For an individual regulation, one user can only hold one assessment-based role at a time.

    - For example, if a user holds a reader role for the GDPR regulation and you want to change them to a contributor role, you'll first need to remove their reader role, and then reassign them the reader role.

Note

Admins whose permissions for Compliance Manager were set in Microsoft Entra ID won't appear on the **Manage user access** flyout pane. This means that if a user has access to one or more regulations, and their role is Global Administrator, Compliance Administrator, Compliance Data Administrator, or Security Administrator, they won't appear on this pane. Learn more about [setting Compliance Manager permissions and roles](compliance-manager-setup#set-user-permissions-and-assign-roles).
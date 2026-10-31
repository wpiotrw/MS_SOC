---
layout: Conceptual
title: Authoring and publishing protection policies for Azure sources (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-gov-protection-policy-azure-sources
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: blessonj
ms.date: 2026-07-01T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Get guidance on authoring and publishing protection policies for Azure sources using sensitivity labels in Microsoft Purview.
ai-usage: ai-assisted
locale: en-us
document_id: 199b1f3e-9b4b-b806-1211-a2c18fafd513
document_version_independent_id: 199b1f3e-9b4b-b806-1211-a2c18fafd513
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-gov-protection-policy-azure-sources.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-gov-protection-policy-azure-sources
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-gov-protection-policy-azure-sources.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 1578f86d-7be4-abbd-8cce-69171af6affe
---

# Authoring and publishing protection policies for Azure sources (preview) | Microsoft Learn

Protection access control policies (protection policies) enable organizations to automatically protect sensitive data across data sources. Microsoft Purview already scans data assets and identifies sensitive data elements. This new feature allows you to automatically restrict access to that data by using sensitivity labels from Microsoft Purview Information Protection.

Protection policies ensure that Enterprise Admins must authorize data access for a sensitivity type. After you enable these policies, access control is automatically imposed whenever Information Protection detects sensitive information.

## Actions supported

- Restrict access on labeled data assets so that only users and groups you select can access them.
- Configure action on Sensitivity Labels in the Information Protection solution.

## Sources supported

- Azure Blob Storage
- Azure Data Lake Storage Gen2

## Prerequisites

- Microsoft 365 E5 license and setup of the pay-as-you-go billing model. To understand pay-as-you-go billing by assets protected, see the [pay-as-you-go billing model](purview-billing-models#pay-as-you-go-billing-model). For information about the specific licenses required, see [sensitivity label licensing information](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description#microsoft-purview-information-protection-sensitivity-labeling). To get a Microsoft 365 E5 trial license for your tenant, [sign up from your environment](https://signup.microsoft.com/signup?ShowInternalOffers=true&amp;OfferId=f6f20264-e785-4749-bd8e-884bab076de4).

- Existing Purview accounts [upgraded to Microsoft Purview single tenant model and new Portal experience](account-upgrades), using the [enterprise version of Microsoft Purview](data-governance-free-version-upgrade-to-enterprise).

- [Configure users and permissions](data-gov-protection-policy-azure-sources#users-and-permissions).
- [Create or extend sensitivity labels from Microsoft Purview Information Protection to Data Map assets](data-map-sensitivity-labels-apply#step-2-create-or-modify-existing-label-to-be-scoped-to-files--other-data-assets-so-theyre-available-for-data-map).
- Register sources - register any of these sources you like:

    - [Azure Blob Storage](register-scan-azure-blob-storage-source#register)
    - [Azure Data Lake Storage Gen2](register-scan-adls-gen2#register)

    Note

    To continue, you need to be a [data source administrator](data-gov-classic-permissions#roles) in the collection where your Azure storage source is registered.
- Enable data policy enforcement:

    - Go to the new [Microsoft Purview portal](https://purview.microsoft.com/).
    - Select the **Data Map** tab in the left menu.
    - Select the **Data sources** tab in the left menu.
    - Select the source where you want to enable *data policy enforcement*.
    - Set the **Data policy enforcement** toggle to **On**.
- Scan sources - register any of the sources you've registered:

    - [Azure Blob Storage](register-scan-azure-blob-storage-source#scan)
    - [Azure Data Lake Storage Gen2](register-scan-adls-gen2#scan)

    Note

    Wait at least 24 hours after scanning.

### Users and permissions

There are several types of users you need, and you need to set up the corresponding roles and permissions for these users:

1. Microsoft Purview Information Protection Admin - Broad rights to manage Information Protection solution: reviewing / creating / updating / deleting protection policies, sensitivity labels and label/auto-labeling policies, all classifier types. They should also have full access to data explorer, activity explorer, Microsoft Purview Information Protection insights, and reports.
    - User needs the roles from within the built-in role group “Information Protection”, along with new roles for data map reader, insights reader, scan reader, source reader. Full permissions would be:
        - Information Protection reader
        - Data Map Reader
        - Insights Reader
        - Source Reader
        - Scan Reader
        - Information Protection admin
        - Information Protection analyst
        - Information protection investigator
        - Data classification list viewer
        - Data classification content viewer
        - Microsoft Purview evaluation administrator
    - **Option 1**- Recommended:
        1. Within the Microsoft Purview role groups panel, search for **Information Protection**.
        2. Select the Information Protection role group, select **Copy**.
        3. Name it: "Preview - Information Protection", and select **Create copy**.
        4. Select **Preview - Information Protection** and select **Edit**.
        5. On the **Roles** page, **+ Choose roles** and search for “reader”.
        6. Select these four roles: Data map reader, insights reader, scan reader, source reader.
        7. Add the Microsoft Purview Information Protection admin test user account to this new copied group and complete the wizard.
    - **Option 2**- uses built-in groups (will provide more permissions than needed)
        1. Place a new Microsoft Purview Information Protection admin test user account within the built-in groups for Information Protection, Data Estate Insights Readers, Data Source Administrators.
2. [Data Owner/Admin](data-gov-classic-permissions#roles) - This user will enable your source for data policy enforcement in Microsoft Purview for Azure and Amazon S3 sources.

## Create protection policy

After you check the prerequisites and prepare your Microsoft Purview instance and source for protection policies and wait at least 24 hours after your most recent scan, complete the following steps to create your protection policies:

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com/) and select the **Information Protection** card. If the **Information Protection** solution card isn't displayed, select **View all solutions** and then select **Information Protection** from the **Data Security** section.
2. On the left navigation, select select **Policies**, then select **Protection policies**.
3. Select **New protection policy**.
4. Provide a name and description and select **Next**.
5. Select **+ Add sensitivity label** to add sensitivity label(s) to detect for the policy, and select all the labels you want the policy to apply to.
6. Select **Add** then select **Next**.
7. Select the sources you want to apply the policy to. You can select multiple sources. Select **Edit** to manage the scope for each you select.
8. Depending on your source, select the **+ Include** button at the top to add up to 10 resources your scope list. The policy will be applied to all the resources you select.

    Note

    Currently a maximum of 10 resources is supported, and they must be selected under **Edit** for them to be enabled.
9. Select **Add** and then select **Done** when your list of sources is complete.
10. Depending on your source, select the type of protection policy you want to create.
11. Select the users who will **NOT** be denied access based on the label. Everyone in your org will be denied access to labeled items except for the users and groups you add here.

    Important

    Ensure that any service principal accounts running data governance scans for the scoped sources are included in a Security Group. Add this Security Group to the allowed list of your protection policies. This will prevent future scans from being blocked by access restrictions on labeled files.
12. Select **Next**.
13. Choose whether turn on the policy right away or not, and select **Next**.
14. Select **Submit**.
15. Select **Done**.

You should now see your new policy in the list of protection policies. Select it to confirm that all the details are correct.

## Manage protection policy

To edit or delete an existing protection policy, follow these steps:

1. Open the [Microsoft Purview portal](https://purview.microsoft.com).
2. Open the **Information Protection** solution.
3. Select **Policies**, then select **Protection policies**.
4. Select the policy you want to manage.
5. To change any of the details, select the **Edit policy** button.
6. To delete the policy, select **Delete policy**.
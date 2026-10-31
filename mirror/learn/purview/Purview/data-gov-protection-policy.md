---
layout: Conceptual
title: Get Started with Protection Policies (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-gov-protection-policy
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
description: Step-by-step guide on authoring and publishing protection policies for sensitivity labels in Microsoft Purview so only certain users can access sensitive information.
ai-usage: ai-assisted
locale: en-us
document_id: 9be2e6cc-f696-f51f-45de-0b7b489a2ec9
document_version_independent_id: 9be2e6cc-f696-f51f-45de-0b7b489a2ec9
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-gov-protection-policy.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-gov-protection-policy
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-gov-protection-policy.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/68ec7f3a-2bc6-459f-b959-19beb729907d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/90370425-aca4-4a39-9533-d52e5e002a5d
platformId: 125cfe5e-469a-f4a2-9f80-5f587e619c82
---

# Get Started with Protection Policies (preview) | Microsoft Learn

Protection policies help organizations automatically protect sensitive data across data sources. Microsoft Purview already scans data assets and identifies sensitive data elements. Protection policies help you automatically restrict access to that data by using sensitivity labels from Microsoft Purview Information Protection.

Protection policies ensure that enterprise admins must authorize data access for a sensitivity label. After you enable these policies, access control is automatically imposed whenever Information Protection detects sensitive information.

## Actions supported

- Restrict access on labeled data assets so that only users and groups you select can access them.
- Configure action on sensitivity labels in the Information Protection solution.

## Data sources supported

- [Azure Sources](data-gov-protection-policy-azure-sources):
    - Azure Blob storage
    - Azure Data Lake Storage Gen2
- [Microsoft Fabric](/en-us/fabric/governance/protection-policies-create)

Tip

This article covers general steps for all protection policies. The available data source articles cover specifics like available regions, limitations, and specific features for those data sources.

## Prerequisites

- Microsoft 365 E5 license and setup of the pay-as-you-go billing model. To understand pay-as-you-go billing by assets protected, see the [pay-as-you-go billing model](purview-billing-models#pay-as-you-go-billing-model). For information about the specific licenses required, see [sensitivity label licensing information](/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-purview-service-description#microsoft-purview-information-protection-sensitivity-labeling). To get a Microsoft 365 E5 trial license for your tenant, [sign up from your environment](https://signup.microsoft.com/signup?ShowInternalOffers=true&amp;OfferId=f6f20264-e785-4749-bd8e-884bab076de4).

# [Azure sources](#tab/azure-sources)
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

# [Microsoft Fabric](#tab/microsoft-fabric)
See the [protection policies for Fabric overview](/en-us/fabric/governance/protection-policies-overview).

---

### Users and permissions for Azure sources

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

1. Sign in to the [Microsoft Purview portal](https://purview.microsoft.com/) &gt; **Information Protection** card &gt; **Policies**. If the **Information Protection** solution card isn't displayed, select **View all solutions** and then select **Information Protection** from the **Data Security** section.
2. Select **Protection policies**.
3. Select **+ New protection policy**.
4. Enter a name and description, and select **Next**.
5. Select **+ Add sensitivity label** to add sensitivity labels to detect for the policy, and select all the labels you want the policy to apply to.
6. Select **Add** and then select **Next**.
7. Select the sources you want to apply the policy to.

    1. For Microsoft Fabric sources, select only Fabric and select **Next**. ([For more information, see the Fabric documentation.](/en-us/fabric/governance/protection-policies-create))
    2. For Azure sources, you can select multiple sources. Select the **Edit** button to manage the scope for each source you select.
8. Depending on your source, select the **+ Include** button at the top to add up to 10 resources to your scope list. The policy applies to all the resources you select.

    Note

    Currently, a maximum of 10 resources are supported, and you must select them under **Edit** for them to be enabled. If the Azure storage account enables a customer-managed key, the storage account doesn't work for protection policies.
9. Select **Add** and then select **Done** when your list of sources is complete.
10. Depending on your source, select the type of protection policy you want to create.

    1. For Fabric sources, follow the [protection policies for Fabric documentation](/en-us/fabric/governance/protection-policies-create).
    2. For other sources, select the users who are **NOT** denied access based on the label. Everyone in your org is denied access to labeled items except for the users and groups you add here.

Important

Ensure that you include any service principal accounts running Microsoft Purview Data Governance Scans for the scoped sources in a security group. Add this security group to the allowed list of your protection policies. This action prevents future scans from being blocked by access restrictions on labeled files.

1. Select **Next**.
2. Select whether to turn on the policy right away or not, and select **Next**.
3. Select **Submit**.
4. Select **Done**.
5. You should now see your new policy in the list of protection policies. Select it to confirm that all the details are correct.

## Manage protection policy

To edit or delete an existing protection policy, follow these steps:

1. Open the [Microsoft Purview portal](https://purview.microsoft.com).
2. Open the **Information Protection** solution.
3. Select **Policies**, then select **Protection policies**.
4. Select the policy you want to manage.
5. To change any of the details, select the **Edit policy** button.
6. To delete the policy, select **Delete policy**.
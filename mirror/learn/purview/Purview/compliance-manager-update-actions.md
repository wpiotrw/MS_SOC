---
layout: Conceptual
title: Update improvement actions and bring compliance data into Microsoft Purview Compliance Manager | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/compliance-manager-update-actions
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.date: 2026-07-01T00:00:00.0000000Z
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
description: Migrate your existing compliance data into Microsoft Purview Compliance Manager using an Excel based upload process.
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: 02758485-1f5d-79f1-20ba-e9cd26aba373
document_version_independent_id: 02758485-1f5d-79f1-20ba-e9cd26aba373
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/compliance-manager-update-actions.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: compliance-manager-update-actions
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/compliance-manager-update-actions.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/eab1aabc-e18c-405b-ac29-e35eb0b15e3b
- https://authoring-docs-microsoft.poolparty.biz/devrel/60932d05-feee-4685-a73b-595e25dd9318
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/574d2eb1-e22a-49c0-b4eb-64e86dbeee6b
- https://authoring-docs-microsoft.poolparty.biz/devrel/c43bb58b-1190-419b-8d18-e6052371b599
platformId: a0a8b3c7-3f59-619a-6a5a-4813f0ce90c0
---

# Update improvement actions and bring compliance data into Microsoft Purview Compliance Manager | Microsoft Learn

## Overview

Compliance Manager enables organizations to bring their existing compliance activity data and evidence into the Compliance Manager solution. Uploading a specially formatted Excel file allows organizations who are new to Compliance Manager to migrate compliance activities completed in other systems into Compliance Manager and quickly start increasing their overall compliance score.

This upload process also gives new and existing Compliance Manager users greater flexibility and ability to update improvement actions on a larger scale. For example, you can:

- [Add test results and evidence](compliance-manager-improvement-actions#storing-evidence) to multiple improvement actions that were tested in a system other than Compliance Manager.
- [Assign improvement actions](compliance-manager-improvement-actions#assign-an-owner) to various users based on the actions' score potential.
- Update the implementation status or testing status of multiple improvement actions all at one time.
- Change improvement actions' [testing type](compliance-manager-improvement-actions#testing-type) from automatic to manual.

## Get started with updating improvement actions

To migrate existing data into Compliance Manager or to perform a bulk update of improvement actions, you can start from one of two places in Compliance Manager:

- From **Assessments** page: Helps you update specific assessments with information from elsewhere, such as test results or evidence for actions that were tested by a separate system.
- From **Improvement actions** page: Facilitates updating multiple actions at once, such as assigning them to users, changing implementation or test status, and adding notes and evidence.

To begin the process of migrating data or updating actions, follow the steps in Steps for updating actions.

Important

- Only the improvement actions managed by your organization, not Microsoft managed actions, can be updated by this process. (Learn more about [types of improvement actions](compliance-manager-scoring#action-types-and-scoring).)
- Improvement actions must already be associated to an assessment before you can update them through this process. (Learn more about [building and managing assessments](compliance-manager-assessments).)

## Migrating your existing work into Compliance Manager

If you're new to Compliance Manager, the steps below illustrate the basic workflow for bringing your existing compliance activities into Compliance Manager:

1. **Create an assessment**: Compliance Manager can recommend assessments that may be most relevant to your organization, or you can create one through a guided process. Visit [Create assessments](compliance-manager-assessments#create-assessments) for instructions.
2. **Export improvement actions**: You'll export an Excel file containing the action data that you want to update. It may make more sense to start the export from your **Assessments** page, but you can also export from the **Improvement actions** page. See Steps for updating actions.
3. **Update the improvement action Excel file**: Use the instructions on the **How to update actions** tab of the Excel file to add your information.
4. **Upload the Excel file**: Upload your edited Excel file by selecting the **Upload actions** command on the **Assessments** or **Improvement actions** page.

## Updating multiple improvement actions at once

To update the status, evidence, notes, or other data in multiple improvement actions at one time, you'll follow the basic flow outlined below:

1. **Export improvement actions.** Export the improvement actions you want to update, staring either from your **Improvement actions** page or your **Assessments** page. The export is a downloaded Excel file containing improvement action data. See Steps for updating actions.
2. **Update the improvement action Excel file.** Use the instructions on the **How to update actions** tab of the Excel file to add or update the information in the specially formatted Excel file.
3. **Upload the Excel file.** Upload your edited Excel file by selecting the **Upload actions** command on the **Assessments** or **Improvement actions** page.

Note

If you export the improvement actions from an assessment, the exported Excel file will include control-mapping data for that assessment. However, you won't be able to change the control-mapping data when you edit your Excel file.

## Steps for updating actions

The following steps outline the process for bringing compliance activity data into your assessments and updating improvement actions.

1. In Compliance Manager, begin from either from the **Assessments** page or the **Improvement actions** page.
2. Export the improvement actions that you want to update:

    a. From the **Improvement actions** page: Find the improvement actions you want to update, and select the checkbox to the left of their names. Then select the **Export actions** command above the list of actions.

    b. From the **Assessments** page: Find the assessment or assessments you want to update, and select the checkbox to the left of their names. Then select the **Export actions** command above the list of assessments.
3. An Excel file will download, which contains all the data related to the actions. Open the file and refer to the formatting instructions on the tab labeled **How to update actions.**
4. Edit the information on the **Action Update** tab of the spreadsheet according to the formatting instructions. Then save your updated version of the Excel file to your computer.
5. On your **Assessments** page or **Improvement actions** page, select the **Update actions** command, which will open the improvement actions update wizard.
6. The first page in the wizard lists the main prerequisites: that all improvement actions must be associated to at least one assessment, and that your data needs to be formatted in an Excel file for upload. Check the boxes next to the reminders, then continue the process by selecting **Next**.
7. On the **Import updated improvement actions** page, select **Browse** to locate your updated Excel file from its saved location, then select **Next**. If there are any problems with the format of your file, an error message will give instructions for fixing the problem. Upload your corrected file again, then select **Next**.
8. On the **Review and finish** page, review the summary showing the number of actions that will be updated, their associated assessments, and how they affect your compliance score. From here you can upload a different file, or continue with the upload by selecting **Update actions**.
9. When your file has been successfully uploaded, you'll see a confirmation screen. Select **Finish** to exit the wizard and arrive back at the page where you began the update actions process.

Most of the updates will take effect right away, but it may take up to a day for all the updated information to be fully reflected in Compliance Manager.

Note

Control mapping won't be included in the Excel file that's downloaded when you generate a report by selecting *Export actions*.
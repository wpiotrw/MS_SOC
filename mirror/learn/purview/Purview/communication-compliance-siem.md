---
layout: Conceptual
title: Use Communication Compliance with SIEM solutions | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/communication-compliance-siem
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: Integrate Microsoft Purview Communication Compliance with SIEM solutions such as Microsoft Sentinel or Splunk to surface alerts, correlate audit events, and investigate incidents in the Communication Compliance workflow.
keywords: Microsoft 365, Microsoft Purview, compliance, Communication Compliance
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-26T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-communication-compliance
ms.collection:
- purview-compliance
search.appverid:
- MET150
- MOE150
ai-usage: ai-assisted
ms.custom: msecd-doc-authoring-1014
locale: en-us
document_id: ac820802-b98a-c4ef-7415-20fb9daa4ea6
document_version_independent_id: ac820802-b98a-c4ef-7415-20fb9daa4ea6
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/communication-compliance-siem.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: communication-compliance-siem
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/communication-compliance-siem.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8a94907f-2511-4271-b5ca-ec7f2e75067c
- https://authoring-docs-microsoft.poolparty.biz/devrel/1dd701e0-441f-4b0a-9806-aa47decc4e35
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bffa8e88-f633-409d-a24d-083bdbc68872
- https://authoring-docs-microsoft.poolparty.biz/devrel/0a2fc935-5977-4aa6-9f55-0be03bd2acb8
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 987d9e4e-73a9-1ac8-2f09-e355db386bb0
---

# Use Communication Compliance with SIEM solutions | Microsoft Learn

Important

[Microsoft Purview Communication Compliance](communication-compliance) provides the tools to help organizations detect regulatory compliance (for example, SEC or FINRA) and business conduct violations such as sensitive or confidential information, harassing or threatening language, and sharing of adult content. Communication Compliance is built with privacy by design. Usernames are pseudonymized by default, role-based access controls are built in, investigators are opted in by an admin, and audit logs are in place to help ensure user-level privacy.

[Microsoft Purview Communication Compliance](communication-compliance) is an insider risk solution that helps you minimize communication risks by helping you detect, capture, and act on potentially inappropriate messages in your organization. Security information and event management (SIEM) solutions such as [Microsoft Sentinel](https://azure.microsoft.com/services/azure-sentinel) or [Splunk](https://www.splunk.com/) are commonly used to aggregate and track threats within an organization.

A common need for organizations is to integrate Communication Compliance alerts and their SIEM solutions. With this integration, organizations can view Communication Compliance alerts in their SIEM solution and then remediate alerts within the Communication Compliance workflow and user experience.

For example, an employee sends an offensive message to another employee and the offensive message is detected by a Communication Compliance policy for potentially inappropriate content. Communication Compliance solution logs events such as policy matches for inappropriate content in Microsoft 365 Audit (also known as "unified audit log") and imports them into the SIEM solution. You can associate SIEM alerts that were created from Microsoft 365 Audit events with the corresponding Communication Compliance alerts. Investigators receive notifications of these alerts in their SIEM solution, and they can investigate and remediate the corresponding alerts in the Communication Compliance dashboard.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](copilot-in-purview-overview).

## Communication Compliance alerts in Microsoft 365 Audit

Microsoft 365 Audit captures all Communication Compliance policy matches. The following examples show the details available for selected Communication Compliance policy match activities:

**Example of audit log entry for an Inappropriate Content policy template match:**

```xml
RunspaceId: 5c7bc9b0-7672-4091-a112-0635bd5f7732
RecordType: ComplianceSupervisionExchange
CreationDate: 7/7/2022 5:30:11 AM
UserIds: user1@contoso.onmicrosoft.com
Operations: SupervisionRuleMatch
AuditData: {"CreationTime":"2022-07-07T05:30:11","Id":"44e98a7e-57fd-4f89-79b8-08d941084a35","Operation":"SupervisionRuleMatch","OrganizationId":"338397e6\-697e-4dbe-a66b-2ea3497ef15c","RecordType":68,"ResultStatus":"{\\"ItemClass\\":\\"IPM.Note\\",\\"CcsiResults\\":\\"\\"}","UserKey":"SupervisionStoreDeliveryAgent","UserType":0,"Version":1,"Workload":"Exchange","ObjectId":"\<HE1P190MB04600526C0524C75E5750C5AC61A9@HE1P190MB0460.EURP190.PROD.OUTLOOK.COM\>","UserId":"user1@contoso.onmicrosoft.com","IsPolicyHit":true,"SRPolicyMatchDetails":{"SRPolicyId":"00aa00aa-bb11-cc22-dd33-44ee44ee44ee","SRPolicyName":"Adult images","SRRuleMatchDetails":\[\]}}
ResultIndex: 24
ResultCount: 48
Identity: 44e98a7e-57fd-4f89-79b8-08d941084a35
IsValid: True
ObjectState: Unchanged
```

**Example of a Microsoft 365 audit log entry for a policy with custom keyword match (custom sensitive information type):**

```xml
RunspaceId: 5c7bc9b0-7672-4091-a112-0635bd5f7732
RecordType: ComplianceSupervisionExchange
CreationDate: 7/6/2022 9:50:12 PM
UserIds: user2@contoso.onmicrosoft.com
Operations: SupervisionRuleMatch
AuditData: {"CreationTime":"2022-07-06T21:50:12","Id":"5c61aae5-26fc-4c8e-0791-08d940c8086f","Operation":"SupervisionRuleMatch","OrganizationId":"338397e6\-697e-4dbe-a66b-2ea3497ef15c","RecordType":68,"ResultStatus":"{\\"ItemClass\\":\\"IPM.Note\\",\\"CcsiResults\\":\\"public\\"}","UserKey":"SupervisionStoreDeliveryAgent","UserType":0,"Version":1,"Workload":"Exchange","ObjectId":"\<20210706174831.24375086.807067@sailthru.com\>","UserId":"user2@contoso.onmicrosoft.com","IsPolicyHit":true,"SRPolicyMatchDetails":{"SRPolicyId":"11bb11bb-cc22-dd33-ee44-55ff55ff55ff","SRPolicyName":"Insiders","SRRuleMatchDetails":\[{"SRCategoryName":"New insiders lexicon"}\]}}
ResultIndex: 46
ResultCount: 48
Identity: 5c61aae5-26fc-4c8e-0791-08d940c8086f
IsValid: True
ObjectState: Unchanged
```

Note

Currently, there might be up to a 24-hour delay between the time Microsoft 365 Audit records a policy match and the time you can investigate policy matches in Communication Compliance.

## Configure Communication Compliance and Microsoft Sentinel integration

When you use Microsoft Sentinel to aggregate Communication Compliance policy matches, Microsoft Sentinel uses Microsoft 365 Audit as the data source. To integrate Communication Compliance alerts with Microsoft Sentinel, complete the following steps:

1. [Onboard to Microsoft Sentinel](/en-us/azure/sentinel/quickstart-onboard). As part of the onboarding process, you configure your data sources.
2. Configure the Microsoft Sentinel [Microsoft Office 365 data connector](/en-us/azure/sentinel/data-connectors-reference#microsoft-office-365) and under connector configuration, select *Exchange*.
3. Configure search query to retrieve Communication Compliance alerts. For example:

    *| OfficeActivity | where OfficeWorkload == "Exchange" and Operation == "SupervisionRuleMatch" | sort by TimeGenerated*

    To filter for a specific user, use the following query format:

    *| OfficeActivity | where OfficeWorkload == "Exchange" and Operation == "SupervisionRuleMatch" and UserId == "User1@Contoso.com" | sort by TimeGenerated*

For more information about the Microsoft 365 Audit logs for Office 365 that Microsoft Sentinel collects, see [Azure Monitor Logs reference](/en-us/azure/azure-monitor/reference/tables/OfficeActivity).

## Configure Communication Compliance and Splunk integration

To integrate Communication Compliance alerts with Splunk, complete the following steps:

1. Install the [Splunk Add-on for Microsoft Office 365](https://docs.splunk.com/Documentation/AddOns/released/MSO365/ConfigureinputsmanagementAPI)
2. Configure an integration application in Microsoft Entra ID for the Splunk Add-on for Microsoft Office 365
3. Configure search queries in your Splunk solution. Use the following search example to identify all Communication Compliance alerts:

    *index=\* sourcetype="o365:management:activity" Workload=Exchange Operation=SupervisionRuleMatch*

To filter results for a specific Communication Compliance policy, use the *SRPolicyMatchDetails.SRPolicyName* parameter.

For example, the following search example returns alerts for matches to a Communication Compliance policy named *Inappropriate content*:

*index=\* sourcetype='o365:management:activity' Workload=Exchange Operation=SupervisionRuleMatch SRPolicyMatchDetails.SRPolicyName=&lt;Inappropriate content&gt;*

The following table shows sample search results for different policy types:

| Policy types | Example search results |
| --- | --- |
| Policy detecting a custom sensitive information type keyword list | {  CreationTime: 2022-09-17T16:29:57  ID: 4b9ce23d-ee60-4f66-f38d-08d979f8631f  IsPolicyHit: true  ObjectId: CY1PR05MB27158B96AF7F3AFE62E1F762CFDD9@CY1PR05MB2715.namprd05.prod.outlook.com Operation: SupervisionRuleMatch  OrganizationId: 22cc22cc-dd33-ee44-ff55-66aa66aa66aa  RecordType: 68  ResultStatus: {"ItemClass":"IPM.Note","CcsiResults":"leak"}  SRPolicyMatchDetails: { [+] }  UserId: user1@contoso.OnMicrosoft.com  UserKey: SupervisionStoreDeliveryAgent  UserType: 0  Version: 1  Workload: Exchange  } |
| Policy detecting potentially inappropriate language | {  CreationTime: 2022-09-17T23:44:35  ID: e0ef6f54-9a52-4e4c-9584-08d97a351ad0  IsPolicyHit: true  ObjectId: BN6PR05MB3571AD9FBB85C4E12C1F66B4CCDD9@BN6PR05MB3571.namprd05.prod.outlook.com Operation: SupervisionRuleMatch  OrganizationId: 22cc22cc-dd33-ee44-ff55-66aa66aa66aa  RecordType: 68  ResultStatus: {"ItemClass":"IPM.Yammer.Message","CcsiResults":""}  SRPolicyMatchDetails: { [+] }  UserId: user1@contoso.com  UserKey: SupervisionStoreDeliveryAgent  UserType: 0  Version: 1  } |

## Configure Communication Compliance with other SIEM solutions

To retrieve Communication Compliance policy matches from Microsoft 365 Audit, use PowerShell or the [Office 365 Management API](/en-us/office/office-365-management-api/office-365-management-activity-api-reference).

When you use PowerShell, you can use either of these parameters with the **Search-UnifiedAuditLog** cmdlet to filter audit log events for Communication Compliance activities.

| Audit log parameter | Communication Compliance parameter value |
| --- | --- |
| Operations | SupervisionRuleMatch |
| RecordType | ComplianceSupervisionExchange |

The following examples show how to search for Communication Compliance matches.

```powershell
Search-UnifiedAuditLog -StartDate $startDate -EndDate $endDate -Operations SupervisionRuleMatch | ft CreationDate,UserIds,AuditData
```

The following is a sample search using the **RecordsType** parameter and the *ComplianceSupervisionExchange* value:

```powershell
Search-UnifiedAuditLog -StartDate $startDate -EndDate $endDate -RecordType ComplianceSuperVisionExchange | ft CreationDate,UserIds,AuditData
```

## Additional SIEM integration resources

- [Communication Compliance auditing](communication-compliance-reports-audits#audit)
- [Microsoft Purview Audit (Premium)](audit-solutions-overview#audit-premium)
- [Office 365 Management Activity API reference](/en-us/office/office-365-management-api/office-365-management-activity-api-reference)
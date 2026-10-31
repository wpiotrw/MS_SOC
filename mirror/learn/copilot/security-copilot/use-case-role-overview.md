---
layout: Conceptual
title: Security Copilot use cases for security and IT roles | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/use-case-role-overview
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn about the different security and IT tasks and goals Security Copilot can help accomplish.
ms.date: 2025-10-24T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: article
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom:
- cx-ti
- cx-cop
ms.reviewer: 
search.audiencetype: Admin
locale: en-us
document_id: e6b2a94d-8704-abe6-28ad-5b1701a06dfe
document_version_independent_id: e6b2a94d-8704-abe6-28ad-5b1701a06dfe
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/use-case-role-overview.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: use-case-role-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/use-case-role-overview.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c6f99e62-1cf6-4b71-af9b-649b05f80cce
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3f56b378-07a9-4fa1-afe8-9889fdc77628
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
platformId: 490fa27d-8b44-7fcc-18bc-991b8f6cdb9a
---

# Security Copilot use cases for security and IT roles | Microsoft Learn

Security Copilot empowers users to accomplish the following key use cases as they apply to the different personas or roles in a security operations center or IT team.

## Investigate and remediate security threats

Gain context for incidents to quickly triage complex security alerts into actionable summaries and remediate quicker with step-by-step response guidance.

- **SOC** - Receive actionable step-by-step guidance for incident response, including directions for triage, investigation, containment, and remediation.
- **Identity admins** - Streamline incident resolution by quickly summarizing critical information like user roles, sign-logs, and risk factors to help analysts understand the scope and specifics of potential compromises.
- **CISO** - Get up-to-date, summarized threat intelligence from Microsoft and open source, providing contextual insights on relevant exposures and threat actors, tooling, and techniques.

Read the following related resources:

- [Use case: Incident response and remediation](use-case-incident-response-remediation)
- [Use case: Triage incidents based on enrichment from threat intelligence](triage-alert-with-enriched-threat-intel)
- [Incident investigation](using-promptbooks#incident-investigation) promptbook
- [Triage and investigate incidents with guided responses from Microsoft Copilot in Microsoft Defender](/en-us/defender-xdr/security-copilot-m365d-guided-response)

## Build KQL queries or analyze suspicious scripts

Eliminate the need to manually write query-language scripts or reverse-engineer malware scripts with natural language translation to allow every team member to perform technical tasks.

- **TI analysts** - Build Kusto Query Language (KQL) queries to hunt threats across your organization more quickly and easily.
- **Data security admins** - Simplify eDiscovery investigation by translating inquiries from natural to keyword query language (KeyQL). Prompt in natural language to make your search iterations faster and more accurate. Strengthen team expertise and enable more assertive evidence search.
- **IT admins** - Construct and run KQL queries to get device details from single and multiple devices.
- **Cloud security admins** - Fix issues in Infrastructure-as-Code (IaC) by submitting pull requests to developers with step-by-step remediation guidance and necessary code from Copilot.

Read the following related resources:

- [Suspicious script analysis](using-promptbooks#suspicious-script-analysis) promptbook
- [Use case: Investigate an incident and associated suspicious entities](investigate-incident-malicious-script)
- [Generate KQL queries with Security Copilot in Microsoft Defender](/en-us/defender-xdr/advanced-hunting-security-copilot)

## Understand risks and manage security posture of the organization

Get a broad picture of your environment with prioritized risks to uncover opportunities to improve posture more easily.

- **Cloud security admins** - Understand your comprehensive multicloud risks and receive actionable step-by-step guidance for risk remediation, including AI-generated scripts. Facilitate risk remediation across teams with delegation and pull request creation capabilities.
- **IT admins** - Get a comprehensive view of your environment with prioritized risks and AI-generated summaries to identify overlapping settings, prevent policy conflicts, and minimize vulnerabilities during policy creation or updates.
- **Data security admins** - Assess and manage organization’s data security posture by reviewing and tackling prioritized data security risks with a centralized data security dashboard to reduce investigation time.
- **TI analysts** - Get summarized threat intelligence relevant to an artifact to quickly contextualize an incident and extract MITRE techniques, tactics, and procedures (TTPs) to understand associated threat activity.

Read the following related resources:

- [Check impact of an external threat article](using-promptbooks#check-impact-of-an-external-threat-article) promptbook
- [Threat Intelligence 360 report based on an MDTI article](using-promptbooks#threat-intelligence-360-report-based-on-mdti-article) promptbook

## Troubleshoot IT issues faster

Synthesize relevant information rapidly and receive actionable insights to identify and resolve IT issues quickly.

- **IT admins** - Reduce mean time from discovery to response of IT incidents by analyzing error codes and summarizing device context.
- **Identity admins** - Simplify sign-in log troubleshooting by automating data gathering and correlation into summaries of relevant information (for example, failed MFA attempts and policy changes). Get recommendations to resolve access issues efficiently, such as re-registering devices or adjusting policies.

## Define and manage security policies

Define a new policy, cross-reference it with others for conflicts, and summarize existing policies to manage complex organizational context quickly and easily.

- **IT admins** - Reduce the risk of operational disruptions and vulnerabilities by analyzing conflicting or misconfigured policies and get guidance for recommended policy settings.
- **Data security admins** - Streamline DLP policy tuning and policy planning of data landscape to improve coverage and controls.

## Configure secure lifecycle workflows

Build groups and set access parameters with step-by-step guidance to ensure a seamless configuration to prevent security vulnerabilities.

- **Identity admins** - Quickly configure workflows based on user roles, groups, and access package parameters, providing step-by-step guidance to ensure comprehensive and accurate setup.

## Develop reports for stakeholders

Get a clear and concise report that summarizes the context and environment, open issues, and protective measures prepared for the tone and language of the report’s audience.

- **SOC** - Summarize investigations in Copilot into exportable, natural language reports to simplify communication to security stakeholders.
- **CISO** - Get a clear and concise report that covers threats, threat actors, analysts’ work, and protective measures, tailored for the board of directors in their native languages.

Read the following related resources:

- [Check impact of an external threat article](using-promptbooks#check-impact-of-an-external-threat-article) promptbook
- [Incident investigation](using-promptbooks#incident-investigation) promptbook
- [Threat Intelligence 360 report based on an MDTI article](using-promptbooks#threat-intelligence-360-report-based-on-mdti-article) promptbook
- [Summarize an incident with Microsoft Copilot in Microsoft Defender](/en-us/defender-xdr/security-copilot-m365d-incident-summary)
---
layout: Conceptual
title: 1Password and Microsoft Security Copilot | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/plugin-1password
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn about the instructions for implementing, configuring, and using the 1Password plugin with Microsoft Security Copilot.
ms.date: 2026-03-18T00:00:00.0000000Z
ms.update-cycle: 180-days
ms.topic: concept-article
ms.service: security-copilot
ms.localizationpriority: high
ms.collection:
- security-copilot
- msec-ai-copilot
- tier1
ms.custom: 
search.audiencetype: Admin
search.appverid: MET150
f1.keywords: NOCSH
audience: ITPro
locale: en-us
document_id: 3a3f0f1d-f233-ba70-36e9-58e242c0c9fe
document_version_independent_id: 3a3f0f1d-f233-ba70-36e9-58e242c0c9fe
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/plugin-1password.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: plugin-1password
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/plugin-1password.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/8a94907f-2511-4271-b5ca-ec7f2e75067c
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/03921bea-3752-4ddc-98c2-5aa70db91565
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bffa8e88-f633-409d-a24d-083bdbc68872
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/09911d3e-3eb9-4c8d-ab86-ce80d8d36bbd
platformId: 3434d316-7005-ecce-fffa-bc497f926fbb
---

# 1Password and Microsoft Security Copilot | Microsoft Learn

Important

Some information in this article relates to a prerelease product that may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

Note

This article contains information about third-party plugins. This guidance is provided to help complete integration scenarios. However, Microsoft does not provide troubleshooting support for third-party plugins. Contact the third-party vendor for support.

The 1Password plugin for Microsoft Copilot for Security leverages audit data collected by Microsoft Sentinel to provide security teams with insights into 1Password usage, potential security events, and anomalous behaviors. This plugin does not retrieve secrets or credentials from 1Password, but rather analyzes the audit logs and events to enhance security monitoring and incident response capabilities.

## Prerequisites

- 1Password Business or Enterprise subscription with audit logging capability.
- Microsoft Sentinel deployed and configured in your Azure environment.
- 1Password Events Reporting integration set up to send audit logs to Microsoft Sentinel.
- Microsoft Sentinel 1Password data connector configured and actively ingesting 1Password audit data.
- Administrative access to Microsoft Security Copilot.
- Linked Microsoft Sentinel workspace in Security Copilot.
- Familiarity with Kusto Query Language (KQL) for custom queries.

## Know before you begin

Integration with Microsoft Security Copilot works by connecting to your Microsoft Sentinel workspace where 1Password events are stored.

You'll need to take the following steps before using the plugin.

### Step 1: Configure 1Password Audit Logging

To enable audit logging in 1Password, follow the [Events Reporting documentation](https://support.1password.com/events-reporting/) or complete these steps:

1. Sign in to 1Password.com as an owner or administrator.
2. Click **Integrations** in the sidebar.
3. Click **Directory** at the top of the page.
4. Find the **Microsoft Sentinel** integration and select **Set Up**.
5. Enter a name for your integration (for example, "Microsoft Sentinel Connector").
6. Choose between:
    - **Send events from all vaults** to report events for your entire account.
    - **Choose vaults** to select specific vaults for event reporting.
7. Select **Add Integration**.
8. Save the bearer token that's displayed - you'll need this to configure the Microsoft Sentinel connector.
9. Follow the [1Password Sentinel integration guide](https://support.1password.com/1password-sentinel-integration/#step-2-activate-the-1password-serverless-connector) to activate the serverless connector.
10. Configure the appropriate log retention policies.
11. Verify that user activities, authentication events, and admin actions are being logged.

For detailed configuration options and troubleshooting, refer to the [Events Reporting setup guide](https://support.1password.com/events-reporting/#step-1-set-up-an-events-reporting-integration).

### Step 2: Set up Microsoft Sentinel Connector for 1Password

1. Access your Microsoft Sentinel workspace.
2. Navigate to the Data Connectors section.
3. Locate and select the 1Password data connector.
4. Follow the configuration wizard to connect to your 1Password environment.
5. Validate that audit logs are being successfully ingested into Microsoft Sentinel.

### Step 3: Install and configure the plugin

1. Sign in to [Microsoft Security Copilot](https://securitycopilot.microsoft.com/).
2. Access **Manage Plugins** by selecting the **Sources** button from the prompt bar.
3. Next to **1Password**, select **Set up**.
4. Upload the 1Password plugin package or specify its repository location.
5. Configure the plugin to connect to your Microsoft Sentinel workspace.

## Configuration guide

### Required parameters

Configure the following parameters for the plugin to function correctly:

1. **Microsoft Entra Tenant ID**

    - The unique identifier of your Microsoft Entra environment
    - Format: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`
2. **Subscription ID**

    - The unique identifier of the Azure Subscription of Microsoft Sentinel
    - Format: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`
3. **ResourceGroup Name**

    - This is the resource group name that security copilot will use for sentinel.
4. **Workspace Name**

    - This is the workspace name that security copilot will use for sentinel.

### Configuration methods

1. **Plugin Configuration Portal**
    - Configure settings directly in the Microsoft Copilot for Security plugin interface
    - Specify workspace connection parameters
    - Test connectivity before saving

## Sample 1Password prompts

The following section provides example prompts to try.

### 1. Natural Language Queries

Use conversational language to analyze 1Password audit data:

- "Show me all failed login attempts in 1Password over the past week"
- "Who accessed sensitive vaults in 1Password outside of business hours?"
- "Has anyone created new shared vaults in the last month?"

### 2. Structured Commands

For more precise control, use structured command syntax:

- `analyze-events -type:"item.view" -timeframe:"last 7 days" -user:"admin"`
- `detect-anomalies -dataset:"authentication" -baseline:"30 days"`
- `report-activity -vault:"Finance" -action:"create,delete,modify"`

### 3. Workflow Integration

Include 1Password audit analysis as part of larger security workflows:

- "Investigate this user account and check for unusual 1Password activity"
- "Analyze login patterns across our SSO providers including 1Password"
- "Generate a compliance report showing all access to regulated data in 1Password"

### Response Formatting

The plugin formats responses to provide clear security insights:

- **Event Timelines**: Chronological view of related security events
- **User Activity Profiles**: Aggregated view of user behaviors
- **Anomaly Highlighting**: Clear identification of outlier events
- **Visual Analytics**: Charts and graphs for pattern recognition

### Advanced usage

#### Security Incident Investigation

The plugin enables advanced investigation of security incidents involving 1Password usage:

**Example Investigation Workflow**

1. Receive alert about suspicious access to sensitive vault
2. Query 1Password audit logs for all actions by the flagged user
3. Analyze access patterns and compare to historical baseline
4. Correlate with other security telemetry (network logs, endpoint data)
5. Generate comprehensive incident timeline and recommended actions

## Troubleshoot the 1Password plugin

### Errors occur

If you encounter errors, such as *Couldn't complete your request*, or *An unknown error occurred*. Make sure the plugin is turned on. This error may occur if the lookback period is too long, causing the query to attempt to retrieve an excessive amount of data. If the issue persists, sign out of Copilot for Security, and then sign back in.

#### Data Ingestion Issues

| Issue | Possible Causes | Resolution Steps |
| --- | --- | --- |
| Missing Audit Data | Connector misconfiguration, Ingestion pipeline issues | 1. Verify Microsoft Sentinel connector status2. Check 1Password audit logging settings3. Review data connector logs4. Validate Log Analytics agent functionality |
| Data Delay | Ingestion latency, High data volume, Processing bottlenecks | 1. Check ingestion pipeline status2. Review Microsoft Sentinel health metrics3. Optimize data collection rules4. Consider dedicated capacity for critical data |

#### Query Issues

| Issue | Possible Causes | Resolution Steps |
| --- | --- | --- |
| Query Timeout | Complex queries, Large data volume, Resource constraints | 1. Optimize query complexity2. Add appropriate filters3. Use time-based partitioning4. Consider materialized views |
| Schema Mismatch | Custom field mappings, Schema evolution, Parser errors | 1. Review schema definitions2. Update field mappings3. Check for data format changes4. Update custom parsers if needed |

#### Plugin Access Issues

| Feature | Common Problems | Troubleshooting Steps |
| --- | --- | --- |
| Workspace Access | Permission issues, Misconfigured workspace ID | 1. Verify workspace access permissions2. Check workspace connection string3. Review Microsoft Copilot for Security configuration4. Validate Microsoft Entra ID permissions |
| KQL Functions | Function registration failure, Syntax errors, Execution timeout | 1. Check function registration status2. Validate KQL syntax3. Review function permissions4. Optimize function logic |

### Performance Optimization

- Use efficient KQL patterns and avoid cross-joins on large datasets
- Implement appropriate time filters to limit data processing
- Consider materialized views for frequently run analytical queries
- Monitor query performance and optimize resource-intensive operations

### Prompts aren't invoking the correct capabilities

If prompts aren't invoking the correct capabilities, or prompts are invoking some other capability set, you might have custom plugins or other plugins that have similar functionality as the capability set you want to use.

## Provide feedback

To provide feedback, contact https://support.1password.com/.
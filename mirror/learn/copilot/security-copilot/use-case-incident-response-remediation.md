---
layout: Conceptual
title: Incident response and remediation | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/copilot/security/use-case-incident-response-remediation
author: mjcaparas
ms.author: macapara
manager: orspodek
breadcrumb_path: /security-copilot/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Security
permissioned-type: public
description: Learn about the incident response and remediation use case for Security Copilot.
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
- sfi-image-nochange
ms.reviewer: 
search.audiencetype: Admin
locale: en-us
document_id: e80849ed-968a-3603-85cd-4b7c9093b024
document_version_independent_id: e80849ed-968a-3603-85cd-4b7c9093b024
original_content_git_url: https://github.com/MicrosoftDocs/security-copilot-pr/blob/live/security-copilot/use-case-incident-response-remediation.md
site_name: Docs
depot_name: MSDN.Security-Copilot-docs
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: use-case-incident-response-remediation
moniker_range_name: 
monikers: []
item_type: Content
source_path: security-copilot/use-case-incident-response-remediation.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/46e3c7c4-fe77-4a6e-b40a-44c569819fa5
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d0c6fab8-2d7d-4bb0-bf40-589e08d7c132
platformId: ce7c6e80-bcb5-8a1a-d58c-9829e86a4bd7
---

# Incident response and remediation | Microsoft Learn

**Role mentioned**: Tier 1 SOC analysts investigating security incidents and resolving noncritical alerts

## Scenario

Security Copilot can support Tier 1, entry-level, or junior analysts in assessing and managing incidents with greater efficiency and effectiveness.

This use case presents an abbreviated version of the incident analysis in [Case Study: Harnessing Security Copilot in Defending Against Cyberthreats](https://techcommunity.microsoft.com/blog/securitycopilotblog/case-study-harnessing-copilot-for-security-in-defending-against-cyberthreats/4251623) and extended here to include remediation steps.

You're a tier 1 analyst. An incident has been assigned to you by your team lead and your job is to determine whether the incident is indeed malicious and if it is, to resolve it as soon as possible.

## Steps

1. In the Microsoft Defender XDR incident queue, you can see that the high-severity incident titled *Multistage incident involving Initial access & Lateral movement on multiple endpoints reported by multiple sources* correlates 25 alerts from various Microsoft security solutions. It involves three devices, four users, and one email account. [![Screenshot of the incident queue.](media/use-case-incident-response-remediation-1-tb.png)](media/use-case-incident-response-remediation-1.png#lightbox)
2. Open the incident page to see the attack story. You check the Security Copilot pane on the right side of the attack story and see that it automatically creates a summary of the incident, along with some steps under guided response. [![Screenshot of the attack story.](media/use-case-incident-response-remediation-2-tb.png)](media/use-case-incident-response-remediation-2.png#lightbox)
3. To get an overview of what transpired, you read the summary provided by Security Copilot. You copy the incident summary by selecting **Copy to clipboard** in the options menu and paste it in another document. [![Screenshot of the Copilot pane with Copy function highlighted.](media/use-case-incident-response-remediation-3-tb.png)](media/use-case-incident-response-remediation-3.png#lightbox)This is useful for the required report as it is already organized by attack phase and highlights the important aspects of the attack. Without Security Copilot, you would need to develop the report from scratch.
4. You then easily determine that the complex incident involved multiple attacks. You go through each of the attack phase as laid out in [Initial access, discovery, and defense evasion](https://techcommunity.microsoft.com/blog/securitycopilotblog/case-study-harnessing-copilot-for-security-in-defending-against-cyberthreats/4251623). For this use case, you're interested in the suspected DCSync attack under the credential access activity.
5. You select **Open in Security Copilot** from the Copilot pane to ask about DCSync attacks. **Prompt**: *What's a DCSync attack? Can you provide its TTPs?*[![Screenshot of the DCSync attack prompt in Copilot.](media/use-case-incident-response-remediation-5-tb.png)](media/use-case-incident-response-remediation-5.png#lightbox) Security Copilot tells you that in DCSync attacks, an attacker mimics the behavior of a domain controller to replicate hashed credentials from Active Directory, usually through Mimikatz or Empire.
6. Knowing this, you return to Defender XDR and look at the *Suspected DCSync attack* more closely. You see that the user sent a replication request to a domain controller. You ask the standalone Security Copilot whether this is considered typical behavior.**Prompt**: *Is it common for a regular user on a Windows 10 device to send a replication request to a DC?*[![Screenshot of the DCSync attack response in Copilot.](media/use-case-incident-response-remediation-6-tb.png)](media/use-case-incident-response-remediation-6.png#lightbox)With Security Copilot's response you can confirm that this is a true security incident that needs further investigation by the Tier 2 team.
7. The next security alert in the incident summary is a suspicious service creation event that is classified under Persistence. You see that the same alert title was generated by Defender for Identity and Defender for Endpoint. However, when you check the alert, you see that the service path listed is encoded. [![Screenshot of the alert story with encoded path.](media/use-case-incident-response-remediation-7-tb.png)](media/use-case-incident-response-remediation-7.png#lightbox)
8. To investigate the script, you consult Security Copilot.**Prompt**: *Can you decode then tell me more about this service path: %COMSPEC% /C “powershell.exe -EncodedCommand QwA6AFwAUwBjAHIAaQBwAHQAcwBcAFIAZQBuAGEAbQBlAFAAbwB3AGUAcgBzAGgAZQBsAGwALgBwAHMAMQA=”*[![Screenshot of Copilot prompt asking about the suspicious alert.](media/use-case-incident-response-remediation-8-tb.png)](media/use-case-incident-response-remediation-8.png#lightbox) Copilot identifies the encoded command as Base64 encoding and decodes it for you. It appears that the service path is used to run a PowerShell script located in a certain directory. The use of encoding to obfuscate the command could be a sign of malicious activity.
9. As you gain more confidence that this is a true security incident, you can go back to review the **Guided response** in the Security Copilot pane in the incident page to determine which actions you can take to contain or mitigate the attack. [![Screenshot of the guided response pane.](media/use-case-incident-response-remediation-9-tb.png)](media/use-case-incident-response-remediation-9.png#lightbox)

## Conclusion

Using Security Copilot can provide several efficiency benefits to analysts tasked to investigate and remediate large incidents involving multiple alerts and entities. It helps in understanding the attack overview, in providing analysis for malicious scripts, in providing context for named attacks, and in performing the necessary steps to remediate the threat.
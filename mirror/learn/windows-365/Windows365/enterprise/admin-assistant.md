---
layout: Conceptual
title: Windows 365 admin assistant (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows-365/enterprise/admin-assistant
breadcrumb_path: /windows-365/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://feedbackportal.microsoft.com/feedback/forum/6ab53114-95ab-ec11-9840-000d3a1c7d74
uhfHeaderId: MSDocsHeader-Windows365
description: Learn how to use Windows 365 admin assistant in the Microsoft Intune admin center to investigate Cloud PC connectivity issues, including prerequisites, example prompts, permissions, and known limitations.
author: khyatishah1121
ms.author: khyatishah
ms.service: windows-365
ms.topic: overview
ms.date: 2026-11-16T00:00:00.0000000Z
ai-usage: ai-assisted
locale: en-us
document_id: 632e762a-1b30-d4f3-f254-97dbc35e8283
document_version_independent_id: 632e762a-1b30-d4f3-f254-97dbc35e8283
original_content_git_url: https://github.com/MicrosoftDocs/windows-cloud-pr/blob/live/Windows365/enterprise/admin-assistant.md
site_name: Docs
depot_name: Learn.Windows365
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: enterprise/admin-assistant
moniker_range_name: 
monikers: []
item_type: Content
source_path: Windows365/enterprise/admin-assistant.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/72cb4d1c-66f7-4281-99d5-e04a64d084fc
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/d9ebaec0-4879-449e-9781-0afdce99fe0a
platformId: 780814ac-2a86-94e7-6518-f1820e070e6a
---

# Windows 365 admin assistant (preview) | Microsoft Learn

Windows 365 Admin Assistant is an agentic experience in the Microsoft Intune admin center that works alongside IT administrators to manage Windows 365. It extends your expertise so you can move from complex issues to clear answers faster, in the same place you already manage Cloud PCs alongside your other devices.

Note

Windows 365 Admin Assistant is different from these Microsoft products:

- Windows 365 for Agents provides Cloud PCs that AI agents use to run tasks. Admin assistant is for the IT administrators who manage Cloud PCs.
- Microsoft Copilot in Intune is powered by Microsoft Security Copilot and requires Security Copilot capacity. Admin assistant is a separate Windows 365 experience. It's included with Windows 365 and doesn't require Security Copilot.

In this preview, admin assistant focuses on Cloud PC connectivity troubleshooting. Describe the issue in natural language, and admin assistant:

- Investigates Cloud PC health and connection history for the affected users and Cloud PCs.
- Identifies the likely root cause and whether other Cloud PCs share the same problem.
- Recommends actions for you to take.

Connectivity is the first of several scenarios planned for admin assistant. More will be added over time.

Admin Assistant is designed for Windows 365 IT operations administrators, second- and third-line support teams, and IT leaders.

## Prerequisites and availability

Admin Assistant is available to eligible Windows 365 customers, and no separate setup is required. Before you start, check the following requirements.

### Licensing

Admin Assistant is included with your Windows 365 license, subject to usage limits that can change to maintain service eligibility.

### Administrator roles

Admin Assistant is turned on by default for administrators who have Cloud PC permissions in Intune. What it can show you depends on your own role assignments. For more information about permissions and administrative controls, see Permissions and administrative controls.

### Availability

Admin Assistant is in public preview. For the general service requirements, see [Windows 365 requirements](requirements).

## Open and use Windows 365 admin assistant

### Start a conversation

1. Sign in to the [Microsoft Intune admin center](https://intune.microsoft.com).
2. Go to **Windows 365**, and then select **Windows 365 Admin Assistant**. A full-screen chat experience opens.
3. To open the chat as a side panel instead, select the **Windows 365 Admin Assistant** icon in the lower-right corner of the screen. The icon is available on Windows 365 pages. You can switch between the full-screen and side-panel views as needed.
4. Enter your question in the chat box, or select a previous conversation from the chat history to pick up where you left off.

You can also open Admin Assistant as a side chat next to other Windows 365 pages, and from Windows 365 monitoring reports. When you start a chat from the insight cards in the Cloud PC overview or the **Monitor Cloud PCs** pages, Admin Assistant uses the filters already set on the page as context for the investigation.

### Describe the issue

The more specific your request, the more focused the investigation. A good request includes:

- Who or what is affected, such as specific users, Cloud PCs, or a group like a provisioning policy, region, or office.
- The symptom, such as a connection error, a failed sign-in, dropped sessions, or slow performance.
- The time window, such as when the problem started or when users reported it.
- Relevant context, such as maintenance windows, known high-latency or VPN connections, and recent changes you're aware of.

You can attach images (for example, a screenshot of a support ticket), CSV files, or text files. Share only what's needed for the investigation, and don't include passwords, secrets, or unrelated personal information.

### Review the evidence and refine the investigation

Admin Assistant responds with an explanation, a summary of the evidence it used, a likely-cause hypothesis, and recommended next steps. Before you act on a response:

- Check that it covers the users, devices, and time period you asked about.
- Look at which signals support each conclusion, and treat a likely cause as something to verify rather than proof.
- Check whether the pattern also holds for other relevant groups, such as Cloud PCs in the same region or provisioning policy.

Ask follow-up questions to narrow or extend the investigation, for example, "What changed on these Cloud PCs before the failures began?" or "Do other users in the same provisioning policy show the same failure?" You can add context at any point, such as a maintenance window you forgot to mention, and Admin Assistant revises its reasoning. For harder questions, turn on deeper reasoning to get a more thorough analysis of the available evidence.

Conversations are saved to your chat history, so you can resume an investigation later. The history keeps the context of that investigation. It isn't memory that carries over into unrelated conversations.

### Report an incorrect or incomplete response

Use the feedback option on a response to report a problem. Describe what you expected, what the response missed, and which evidence contradicted it. Your feedback is linked to the conversation so the issue can be investigated. If an incident is urgent or stays unresolved, continue with your normal support and incident-management process rather than waiting on repeated answers.

## Capabilities and example prompts

Admin Assistant can help you:

- **Investigate connection failures**: Find out whether failures point to authentication, the network path, or the Cloud PC itself, and which other Cloud PCs share the same failure.
- **Analyze connection signals across devices**: Review connection checkpoints, errors, protocols, and health signals across many Cloud PCs at once.
- **Find configuration-related causes**: Identify whether Intune or Azure configurations are contributing to connection failures.
- **Identify network paths behind poor performance**: Interpret network provider (ASN) ownership to pinpoint the specific paths contributing to high latency or dropped connections.
- **Compare affected and healthy groups**: Compare affected Cloud PCs or users with healthy ones, or with your tenant baseline, to tell a shared pattern apart from an isolated issue.
- **Analyze trends and investigate spikes**: Track how connection quality and sign-in times change over time, and investigate sudden spikes in failures or degraded performance.

### Example prompts

- "Review my tenant's connectivity health over the last seven days. Identify the three most important issues, their affected scope, and what warrants investigation first."
- "Investigate Korea Central's connection failure rate over the last seven days relative to the tenant baseline. Identify which cohorts account for the excess and what remains unexplained."
- "Have remote sign-in times increased this week? Compare provisioning policies, identify the largest measured regression, and explain what the evidence can establish."
- "Investigate why [Cloud PC name] had connection problems yesterday. Distinguish attempts that never reached the desktop from sessions that connected and later dropped."

### Tips for better results

Admin Assistant works best when your request is specific. Name the affected users, Cloud PCs, region, or provisioning policy, and give a time window, such as "yesterday" or "the last seven days." Include context it can't see, such as maintenance windows, VPN use, or recent changes you know about, so expected behavior isn't flagged as a problem. Start broad, then narrow down with follow-up questions, and check which evidence supports each conclusion before you act on it.

## Permissions and administrative controls

Two separate controls apply to Admin Assistant: whether you can open it, and what data it can read on your behalf. Being able to open admin assistant doesn't give you access to any additional data.

### Data accessed

Admin Assistant reads data from Windows 365, Microsoft Entra, Azure, and Intune. Its access is read-only. Depending on the investigation, it can read:

- Basic user information, assigned licenses, and group membership, used to identify affected users.
- Cloud PC details, such as assigned users, device status, region, configuration, and usage.
- Connection information, such as connection history, performance, failures, and error details.
- Device policies and settings that might affect Cloud PC access or performance.
- Current and recent Windows 365 service incidents and advisories.
- Sign-in activity and access policies, used to investigate authentication failures.

Admin Assistant also uses what you provide in the conversation, such as your prompts, added context, and attachments.

### Permissions

Admin Assistant uses delegated access. It can only read information that you, the signed-in administrator, are authorized to view under your role-based access control (RBAC) assignments, and it never has broader access than you do.

As a result, answers depend on who's asking. Two administrators with different roles can get different results for the same question. If a response looks incomplete, it might mean you don't have permission to some of the relevant data, not that there's no issue. Check your role assignments, or ask an administrator with the right access to run the investigation.

### Manage availability

Admin Assistant is on by default for administrators who have Cloud PC permissions. A tenant administrator can turn it off for the whole tenant from the Windows 365 tenant administration settings in the Microsoft Intune admin center.

## Known limitations

### Scenario boundaries

Admin Assistant focuses on Cloud PC connectivity troubleshooting, including the deployment awareness needed to support connectivity investigations. Investigations into other areas might be limited. In this preview, admin assistant doesn't:

- Run autonomous or admin-led actions or make any changes to your environment.
- Handle issues that require changes to domain controller settings.
- Perform expert-level investigations, such as deep analysis of on-device logs to identify novel service issues.

For novel, highly complex, or uncommon issues, use your existing tools and escalate to the appropriate support or engineering team rather than treating a plausible answer as an expert diagnosis.

### Investigation scale

Some requests cover more data than admin assistant can reason through at once. Large or open-ended requests, such as every Cloud PC in the tenant over a long period, can return incomplete or generic answers. Narrow the request by user group, provisioning policy, region, or time window, or start from a filtered report.

### Evidence and interpretation

The answers from admin assistant are only as good as the signals and context available to it. Keep these points in mind:

- A failed or missing query is a gap in evidence, not evidence that there's no problem. Restore access to the data, or check the underlying administration tools, before you rely on the result.
- A likely cause isn't an established cause. A recent script or policy change that lines up with the failures supports a hypothesis, and you confirm whether it actually explains the issue.
- Without relevant context, such as maintenance windows or known high-latency connections, admin assistant can flag expected behavior as a problem.
- Confidence scores are model-generated and aren't a calibrated measure of correctness. A fluent, confident answer still needs your review.

When the evidence stays inconclusive, or the issue is urgent, move to your existing administration tools and support process instead of repeating the question.

## Data, privacy, and responsible AI

When you enter prompts using Windows 365 Admin Assistant, the information in your prompts, the data they retrieve, and the generated responses are processed and stored in alignment with contractual commitments with your organization's other content in Windows 365. Using admin assistant doesn't transfer Windows 365 data to Intune. Windows 365 data remains within the Windows 365 service. For more information, see [Privacy and data in Windows 365](privacy-personal-data).

Note

Microsoft uses a third-party AI model from OpenAI to power Windows 365 Admin Assistant experiences. As an admin, you can decide whether to use these models to power your experiences, and additional terms might apply. To learn more, see [OpenAI as a subprocessor in Microsoft Online Services](/en-us/microsoft-365/copilot/openai-subprocessor). Data from your environment isn't used to train foundation models, and neither is data accessed through Microsoft Graph.

- Sessions operate within your organization's tenant boundary, and session data isn't shared across tenants.
- Access is delegated and read-only, limited to what the signed-in administrator is authorized to view.
- Sessions are kept as records of agent activity, inputs, and outputs to support security audits and compliance reviews.
- If your tenant's Customer Data storage location is in the EU, prompts are processed in the EU. Otherwise, prompts are processed depending on locality and GPU availability.

Admin Assistant is evaluated for response quality and safety, including resistance to jailbreak and prompt-injection attempts such as instructions hidden in attachments. AI can still make mistakes, so review responses before you act on them and keep remediation within your change-management process. Don't use admin assistant to make consequential decisions about people, such as employment, financial, or eligibility decisions.

For details on capabilities, intended uses, evaluations, and limitations, see the [Application card for Windows 365 admin assistant](app-card-w365-admin-assistant). For how Windows 365 handles your data, see [Privacy and data in Windows 365](privacy-personal-data).
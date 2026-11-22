---
layout: Conceptual
title: Use the Web App Pen Test Agent in Microsoft Perception (preview) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/security/agentic-security/web-app-pen-test-agent
feedback_system: Standard
breadcrumb_path: breadcrumb/agentic-security/toc.json
permissioned-type: public
uhfHeaderId: MSDocsHeader-Security
description: Learn how to test web applications, validate code-scanning findings, and plan remediation with Perception playbooks.
ms.service: project-perception
ms.author: inbarc
author: InbarckMS
ms.localizationpriority: medium
ms.collection:
- m365-security
- tier1
- security-copilot
- magic-ai-copilot
ms.topic: how-to
ms.date: 2026-11-13T00:00:00.0000000Z
ms.update-cycle: 180-days
ai-usage: ai-generated
locale: en-us
document_id: 9cda08b7-ae8a-352b-4cd0-4fa9b5a11ab0
document_version_independent_id: 9cda08b7-ae8a-352b-4cd0-4fa9b5a11ab0
original_content_git_url: https://github.com/MicrosoftDocs/security-docs-pr/blob/live/docs/agentic-security/web-app-pen-test-agent.md
site_name: Docs
depot_name: Learn.agentic-security
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: web-app-pen-test-agent
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/agentic-security/web-app-pen-test-agent.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/7ebba99b-05c3-4387-8883-f7bbf6632cb8
- https://authoring-docs-microsoft.poolparty.biz/devrel/e8fdebed-2921-4997-a75a-fa863723a535
- https://authoring-docs-microsoft.poolparty.biz/devrel/07bb3e10-d135-43ff-bc8b-360497cb39fa
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/006ab567-b18c-4cf1-9a25-c24daa46ede1
- https://authoring-docs-microsoft.poolparty.biz/devrel/cf1e63a8-325f-42be-b60c-d84a95a42b1f
- https://authoring-docs-microsoft.poolparty.biz/devrel/12e559b9-eaf6-4aee-9af7-62334e15f863
platformId: 14e5f3b3-80fd-d7b0-108d-5197ddda899e
---

# Use the Web App Pen Test Agent in Microsoft Perception (preview) | Microsoft Learn

Important

Some information in this article relates to a prereleased product which may be substantially modified before it's commercially released. Microsoft makes no warranties, expressed or implied, with respect to the information provided here. Perception is currently in limited public preview. The limited public preview program means Perception is available to a small, invitation-only set of customers for a defined preview window before broader public availability.

Use the Web App Pen Test Agent to assess an authorized, internet-reachable web application from an attacker's perspective. The **Run web pen test** playbook explores the application, proposes a testing plan, and tests for exploitable weaknesses within the approved target boundary. Testing can examine areas such as authentication, authorization, injection, application programming interfaces (APIs), and business logic. Use the assessment to discover weaknesses, validate findings from code scanning, or mitigate exposure.

This article covers testing scenarios and day-to-day operation. For prerequisites, permissions, approved targets, and DNS ownership verification, see [Set up the Web App Pen Test Agent](web-app-pen-test-agent-setup).

Warning

Active penetration testing can affect application availability, data, and user workflows. Test only applications you own or are explicitly authorized to assess. Use an approved testing window, test accounts, application monitoring, and an agreed stop procedure. Safeguards don't make testing risk-free.

## Choose a testing scenario

Choose the workflow that matches your objective:

| Goal | Playbook | How to use it |
| --- | --- | --- |
| Pen test your application | **Run web pen test** | Assess a verified application, with or without authorized test credentials, and review the findings and supporting evidence. |
| Validate code-scanning findings | **Run web pen test** | Supply code-scanning findings from codename MDASH as input to test whether suspected code weaknesses are exploitable in the deployed application. |
| Mitigate weaknesses with configuration changes | **Protect web app** | Run a pen test, then plan containment, permanent fixes, and eligible Azure Web Application Firewall (WAF) policy changes for Azure Front Door. |

## Before each assessment

Confirm the following with the administrator and application owner:

- The agent is active and the target domain is approved and verified.
- You have access to run the agent and review its results.
- The authorized hosts, testing window, test accounts, and application areas that must not be accessed are clear.
- The application is reachable, and any approved Web Application Firewall (WAF) configuration is ready.
- Someone will monitor application health and can carry out the agreed stop procedure.

Start with a controlled nonproduction application when evaluating the agent or a new configuration.

Important

Don't assume a redirect or discovered link expands the approved target. Don't rely on free-text exclusions or sign-in instructions as enforced URL-level restrictions. If the required boundary can't be maintained, resolve the configuration with the application owner before starting.

## Pen test your application

Use **Run web pen test** to discover and validate weaknesses in a verified application. Choose unauthenticated testing to assess publicly reachable areas, or provide least-privileged test credentials for a supported sign-in flow to assess areas available to a test user.

### Start a Run web pen test session

1. In the [Microsoft Defender portal](https://security.microsoft.com), go to **Perception** &gt; **Sessions**.
2. Select **New session**.
3. Select **Run web pen test**.

    [![Screenshot of Run web pen test inputs showing Target domain, Advanced settings, and Start session, with the OWASP Juice Shop sample selected.](media/web-app-pen-test-agent-run-session.png)](media/web-app-pen-test-agent-run-session.png#lightbox)

    The screenshot shows the OWASP Juice Shop sample target. For your own application, select an approved, verified domain. Expand **Advanced settings** to review additional inputs.
4. Review and complete the session inputs:

    | Input | What to provide |
    | --- | --- |
    | **Target domain** | Select the approved, verified domain for the assessment. |
    | **Exclusions** | Specify application areas that should not be tested. Confirm that the environment also enforces any boundary you must not cross. |
    | **Security tests** | Select the testing categories that match your assessment objective and authorization. |
    | Approval setting | Review the available approval options before starting. Keep human review enabled for actions that require approval under your rules of engagement. |
    | **Username and Password** (optional) | Provide an authorized test account if you need authenticated testing. Include any necessary sign-in instructions. |
    | **Header** (optional) | Enter the header name and value agreed with the WAF or firewall administrator. |
    | Code-scanning findings (optional) | Include selected findings when you want source-informed exploit validation. See Validate code-scanning findings. |
5. Check that the selected target, test categories, test account, and any WAF exception match the authorization.
6. Select **Start session**.

Starting the session begins discovery and planning. Discovery can contact the application, so the approved testing window and monitoring must already be in place.

### Authenticated testing

The preview supports username-and-password input for authenticated testing. Use a least-privileged test account and a supported sign-in flow. Check the session activity to confirm that sign-in succeeded before interpreting findings about authenticated application areas.

Important

Don't put credentials in general chat, exclusions, or report notes. Use the designated credential inputs. 

## Validate code-scanning findings

Use the same **Run web pen test** playbook with code-scanning findings as input to focus testing on suspected code weaknesses. You don't need a separate validation playbook.

Before using this input, confirm that you have permission to read the findings and associated exposure information, and that they correspond to the application you're authorized to test.

1. Start a Run web pen test session and enable the optional code-scanning input.
2. Select the relevant repository and findings where prompted.
3. Review the selection and narrow it to the issues relevant to the assessment. Use the **Severity** and **Confidence** filters to refine the findings.

    [![Screenshot of code-scanning inputs showing repository selection and Severity and Confidence filters, with the repository name redacted.](media/web-app-pen-test-agent-code-scanning-inputs.png)](media/web-app-pen-test-agent-code-scanning-inputs.png#lightbox)
4. Check that the selected findings and target refer to the same application before starting.

Review the resulting exploit-validation evidence alongside the original code findings. A finding that wasn't reproduced in this session isn't proof that the source-code issue is fixed or harmless.

For both testing scenarios, follow the plan-review, monitoring, and results-review guidance below.

## Review the plan before active testing

The agent performs discovery and prepares a penetration-testing plan. Review the proposed plan before authorizing active vulnerability testing.

1. Open the session and review the discovery activity and proposed plan.

    [![Screenshot of a plan marked Needs review, showing scope, authentication, proposed testing limits, and response options. The target URL and custom header value are redacted.](media/web-app-pen-test-agent-review-plan.png)](media/web-app-pen-test-agent-review-plan.png#lightbox)

    This example shows a plan awaiting review. Its stated testing limits describe that plan, not product-wide guarantees.
2. Check that the target, application areas, test categories, and account match the approved assessment.
3. Check any access failures or assumptions. Resolve issues that would make the plan incomplete or outside your authorization.
4. Respond to the plan approval request only when you're satisfied that the proposed testing is authorized.
5. Review any later requests for input or action approval before allowing the work to proceed.

For the shared approval workflow, see [Approve, reject, or stop agentic work](agentic-security-supervise-work).

## Monitor the assessment

Open the session from **Perception** &gt; **Sessions**. Review the activity, task status, inputs, and outputs as the assessment progresses. For the page layout, see [Work with a session](agentic-security-session-details).

During the assessment:

- Monitor application health independently of the session status.
- Check for sign-in failures, unreachable application areas, blocked requests, and requests for input.
- Compare activity with the authorized target and testing window.
- Use the agreed stop procedure if testing affects the application or no longer matches the authorization.

The session page provides a stop workflow. See [Stop a session](agentic-security-supervise-work#stop-a-session). Stopping doesn't undo requests already sent or application changes already made; coordinate any recovery with the application owner.

## Review the results

Open the session and select a report under **Outputs**. You can view the file in the session or use **Download** to save an output. Handle reports as sensitive security-assessment material.

The primary output is the **Web Vulnerability Report**. Source-informed testing can also produce an **Exploit Validation Report** that relates testing evidence to the selected code-scanning findings.

[![Screenshot of the Web Vulnerability Report PDF open in a session, showing an overview and findings by severity alongside the session outputs. The target domain and URL are redacted.](media/web-app-pen-test-agent-vulnerability-report.png)](media/web-app-pen-test-agent-vulnerability-report.png#lightbox)

[![Screenshot of the Exploit Validation Report showing selected leads, confirmed findings, filters, and per-finding validation status. File paths and repository names are redacted.](media/web-app-pen-test-agent-exploit-validation-report.png)](media/web-app-pen-test-agent-exploit-validation-report.png#lightbox)

These examples show results from one assessment, not guaranteed findings or coverage.

Reports can include affected assets, severity and validation status, proof-of-concept evidence, reproduction steps, verification commands, and remediation recommendations. The available evidence depends on what the session completed.

Review each report in this order:

1. **Check scope and completion.** Confirm which target, account, and tests were used. Identify failed tasks, access limitations, and application areas that weren't assessed.
2. **Inspect the evidence.** Review the affected endpoint, observed behavior, and reproduction details. Don't treat a severity or validation label alone as proof.
3. **Evaluate impact in context.** Work with the application owner to assess the affected data, users, permissions, and business workflows.
4. **Review suggested remediation.** Check recommendations for accuracy and applicability before changing the application.
5. **Record follow-up.** Link the report and relevant evidence to your existing remediation process, with access limited to authorized reviewers.

Important

Outputs are AI-generated and can be incorrect or incomplete. A completed session or a report with no findings doesn't establish that the application is secure. Interpret results within the access, tests, and evidence available to that session.

Only run reproduction or verification commands with separate authorization for the target and action. Reproducing a finding can itself affect the application.

## Mitigate weaknesses with configuration changes

Use **Protect web app** to assess an application and plan remediation for validated findings. The playbook runs the Web App Pen Test Agent first, followed by the Web App Risk Reduction Agent. The second agent uses the findings and their supporting HTTP requests, responses, observations, and context to recommend containment and permanent fixes.

The playbook provides remediation guidance and supports approval-based execution of eligible Azure Front Door WAF policy changes. Recommendations for application code, configuration, deployment pipelines, and dependencies require separate review and implementation.

Before starting, ask the administrator to complete [Protect web app setup and Azure access](web-app-pen-test-agent-setup#step-6-set-up-protect-web-app-optional). Permission to run a session isn't permission to change Azure resources.

### Start a Protect web app session

1. In the [Microsoft Defender portal](https://security.microsoft.com), go to **Perception** &gt; **Sessions**.
2. Select **New session**.
3. Select **Protect web app** and review the playbook description.
4. Select the approved, verified web application target for the penetration test.
5. Check that the target and assessment scope match the authorization and that the approved testing window and monitoring are in place.
6. Select **Start session**.

The Web App Pen Test Agent performs discovery and testing before remediation planning begins. A penetration test can take more than an hour, depending on the application.

### Review the testing and remediation plans

Follow Review the plan before active testing for the penetration-testing phase.

The Web App Risk Reduction Agent then processes the validated findings. It might ask you to clarify application context or choose a preferred remediation type, such as WAF-only mitigation. Review the proposed approach and answer only within your authorization.

Important

Answering a planning question doesn't approve a resource change. Review each proposed Azure Front Door WAF policy change and its required permissions before responding to an execution approval request.

### Monitor remediation planning

Open the session from **Perception** &gt; **Sessions** and review its activity, status, and requests for input. Continue to monitor the application during testing.

Remediation planning processes findings in batches and can take several minutes. Review requests for clarification or approval before allowing the work to proceed. Use the shared [approval and stop workflow](agentic-security-supervise-work) when needed.

### Review remediation results

Open the session and select a report under **Outputs**. Review the evidence and recommendations before making changes.

| Output | What to review |
| --- | --- |
| **Web Vulnerability Report - Assessment & Remediation** (PDF and Markdown) | The original penetration-test report with its overview, severity summary, and findings retained. Each finding's remediation section is expanded with containment and permanent-fix guidance. |
| Detailed remediation guide (PDF and Markdown) | Full implementation steps, settings, code snippets, WAF procedures, prerequisites, verification checks, and rollback guidance. Read this guide before implementing a recommendation. |
| ZIP bundle | The report, detailed guide, and machine-readable JSON. Keep the folder layout intact so links between the files continue to work. |
| Remediation notes in the report | Shared prerequisites and Azure Front Door WAF guidance. |

For each finding, review:

1. **WAF applicability.** Check whether a WAF rule applies and why. Where applicable, review the portal steps and rule JSON at the first finding that uses the rule.
2. **Short-term containment.** Review any immediate containment recommendation, such as revoking sessions or rotating exposed credentials. This guidance is included when useful.
3. **Permanent fix.** Check the proposed root-cause change, its owner and location, and the confirmation check. A protective WAF rule isn't a substitute for fixing the underlying weakness.
4. **Shared fixes.** Check which other findings the same change addresses so implementation work isn't duplicated.
5. **Implementation guide.** Follow the link to the full procedure, code, WAF JSON, and Microsoft Learn references. Review verification and rollback instructions before implementation.

Ask follow-up questions in the session if a finding, permanent fix, or WAF recommendation is unclear. Treat these outputs as sensitive assessment material and apply the same evidence-review cautions as for a penetration-test report.

### Review WAF guidance before applying changes

WAF guidance describes whether a protective rule is appropriate and ready to apply. These rules mitigate exposure; they aren't the temporary assessment-traffic exception described in [setup](web-app-pen-test-agent-setup#optional-waf-exception-for-assessment-traffic).

| Label | Meaning and next action |
| --- | --- |
| **Not applicable** | A WAF isn't the right control for the finding. Review the stated reason and the permanent fix. |
| **Conditional; manual** | A rule is recommended if Azure Front Door protects the host. Review and apply it through the portal procedure in the report under your change-approval process. |
| **Draft; review linked blockers** | A rule has been authored but isn't ready to apply. Resolve the linked blockers, such as missing evidence of the attack request. |
| **Needs evidence** | Wait for a confirmed malicious request pattern before making a WAF change. |
| **Log first (does not block)** | The initial rule logs matches without blocking them. Review WAF logs for both attack traffic and legitimate-use matches before a separately approved switch to **Block**. |

Before approving an eligible policy change, confirm the target policy, expected effect, required Azure permissions, verification checks, and rollback procedure with the application and WAF owners. Resource inspection with **Reader** access doesn't grant permission to modify a WAF policy.

Follow the report's verification checks after an approved change. A recommendation, an approval, or a log-only rule doesn't establish that an exploit is blocked or that the underlying issue is fixed. Rollback guidance isn't an automatic rollback guarantee.

## Troubleshoot a session

| Issue | What to do |
| --- | --- |
| The target isn't selectable | Ask the administrator to check [approved targets and verification](web-app-pen-test-agent-setup#step-3-add-target-domains). |
| The application can't be reached | Check internet reachability, redirects, WAF rules, and the matching custom header with the application owner. |
| Sign-in fails | Confirm the test account and supported sign-in flow. Don't interpret unauthenticated results as authenticated coverage. |
| The session is waiting for input | Open the session, review the request, and respond only within the approved assessment scope. |
| Some tests fail or the report is incomplete | Review failed tasks and access limitations before drawing conclusions. Resolve the cause before planning another assessment. |
| The application becomes unhealthy | Use the agreed stop procedure, notify the application owner, and investigate before starting another test. |
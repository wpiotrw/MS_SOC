---
layout: Conceptual
monikers:
- graph-rest-1.0
defaultMoniker: graph-rest-1.0
versioningType: Ranged
title: riskDetail enum type - Microsoft Graph v1.0 | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/api/resources/riskdetail?view=graph-rest-1.0
config_moniker_range: '>= graph-rest-1.0'
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
author: FaithOmbongi
ms.author: MSGraphDocsVteam
ms.suite: microsoft-graph
ms.subservice: entra-sign-in
uhfHeaderId: MSDocsHeader-MSGraph
toc_preview: true
recommendations: false
breadcrumb_path: /graph/ref-breadcrumb/toc.json
ms.service: microsoft-graph
ms.topic: reference
description: Represents the reason behind a specific state of a risky user, sign-in, or service principal.
ms.localizationpriority: medium
ms.date: 2025-11-28T00:00:00.0000000Z
doc_type: enumPageType
locale: en-us
document_id: 374e6a1c-13c9-3dc7-d8c3-f6cfe0c18d5c
document_version_independent_id: dd0bacf9-f4a2-abf1-d08c-bf1412bc982b
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/api-reference/v1.0/resources/riskdetail.md
default_moniker: graph-rest-1.0
site_name: Docs
depot_name: MSDN.microsoft-graph-ref
page_type: conceptual
toc_rel: ../toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: api/resources/riskdetail
moniker_range_name: 107bf06837724705de50667b407c0197
monikers:
- graph-rest-1.0
item_type: Content
source_path: api-reference/v1.0/resources/riskdetail.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: 9b4cf46d-1111-cba1-c578-2b0287ba9349
---

# riskDetail enum type - Microsoft Graph v1.0 | Microsoft Learn

Namespace: microsoft.graph

Represents the reason behind a specific state of a risky user, sign-in, or service principal. This enumeration is used by multiple resources.

The following table lists the members of an `[evolvable enumeration](/graph/best-practices-concept#handling-future-members-in-evolvable-enumerations)`. Use the `Prefer: include-unknown-enum-members` request header to get the following values in this [evolvable enum](/en-us/graph/best-practices-concept#handling-future-members-in-evolvable-enumerations): `m365DAdminDismissedDetection`, `adminConfirmedServicePrincipalCompromised`, `adminDismissedAllRiskForServicePrincipal`, `userChangedPasswordOnPremises`, `adminDismissedRiskForSignIn`, `adminConfirmedAccountSafe`, `microsoftRevokedSessions`.

## Members

| Member | Description |
| --- | --- |
| none | No details are available for the risk state.Applies to:<br>- [riskDetection](riskdetection)<br>- [riskServicePrincipalActivity](riskserviceprincipalactivity)<br>- [riskUserActivity](riskuseractivity)<br>- [riskyServicePrincipal](riskyserviceprincipal)<br>- [riskyUser](riskyuser)<br>- [servicePrincipalRiskDetection](serviceprincipalriskdetection)<br>- [signIn](signin) |
| adminGeneratedTemporaryPassword | An admin generated a temporary password for the user.Applies to:<br>- [riskDetection](riskdetection)<br>- [riskUserActivity](riskuseractivity)<br>- [riskyUser](riskyuser)<br>- [signIn](signin) |
| userPerformedSecuredPasswordChange | The user performed a secure password change.Applies to:<br>- [riskDetection](riskdetection)<br>- [riskUserActivity](riskuseractivity)<br>- [riskyUser](riskyuser)<br>- [signIn](signin) |
| userPerformedSecuredPasswordReset | The user performed a secure password reset.Applies to:<br>- [riskDetection](riskdetection)<br>- [riskUserActivity](riskuseractivity)<br>- [riskyUser](riskyuser)<br>- [signIn](signin) |
| adminConfirmedSigninSafe | An admin confirmed the sign-in as safe.Applies to:<br>- [riskDetection](riskdetection)<br>- [riskUserActivity](riskuseractivity)<br>- [riskyUser](riskyuser)<br>- [signIn](signin) |
| aiConfirmedSigninSafe | AI confirmed the sign-in as safe.Applies to:<br>- [riskDetection](riskdetection)<br>- [riskUserActivity](riskuseractivity)<br>- [riskyUser](riskyuser)<br>- [signIn](signin) |
| userPassedMFADrivenByRiskBasedPolicy | The user passed multifactor authentication (MFA) driven by a risk-based policy.Applies to:<br>- [riskDetection](riskdetection)<br>- [riskUserActivity](riskuseractivity)<br>- [riskyUser](riskyuser)<br>- [signIn](signin) |
| adminDismissedAllRiskForUser | An admin dismissed all risk for the user.Applies to:<br>- [riskDetection](riskdetection)<br>- [riskUserActivity](riskuseractivity)<br>- [riskyUser](riskyuser)<br>- [signIn](signin) |
| adminConfirmedSigninCompromised | An admin confirmed the sign-in as compromised.Applies to:<br>- [riskDetection](riskdetection)<br>- [riskUserActivity](riskuseractivity)<br>- [riskyUser](riskyuser)<br>- [signIn](signin) |
| hidden | The risk state is hidden.Applies to:<br>- [riskDetection](riskdetection)<br>- [riskServicePrincipalActivity](riskserviceprincipalactivity)<br>- [riskUserActivity](riskuseractivity)<br>- [riskyServicePrincipal](riskyserviceprincipal)<br>- [riskyUser](riskyuser)<br>- [servicePrincipalRiskDetection](serviceprincipalriskdetection)<br>- [signIn](signin) |
| adminConfirmedUserCompromised | An admin confirmed the user as compromised.Applies to:<br>- [riskDetection](riskdetection)<br>- [riskUserActivity](riskuseractivity)<br>- [riskyUser](riskyuser)<br>- [signIn](signin) |
| unknownFutureValue | Evolvable enumeration sentinel value. Don't use.Applies to:<br>- [riskDetection](riskdetection)<br>- [riskServicePrincipalActivity](riskserviceprincipalactivity)<br>- [riskUserActivity](riskuseractivity)<br>- [riskyServicePrincipal](riskyserviceprincipal)<br>- [riskyUser](riskyuser)<br>- [servicePrincipalRiskDetection](serviceprincipalriskdetection)<br>- [signIn](signin) |
| m365DAdminDismissedDetection | A Microsoft Defender XDR admin dismissed the detection.Applies to:<br>- [riskDetection](riskdetection)<br>- [riskyUser](riskyuser)<br>- [signIn](signin) |
| adminConfirmedServicePrincipalCompromised | An admin confirmed the service principal as compromised.Applies to:<br>- [riskDetection](riskdetection)<br>- [riskServicePrincipalActivity](riskserviceprincipalactivity)<br>- [riskyServicePrincipal](riskyserviceprincipal)<br>- [riskyUser](riskyuser)<br>- [servicePrincipalRiskDetection](serviceprincipalriskdetection)<br>- [signIn](signin) |
| adminDismissedAllRiskForServicePrincipal | An admin dismissed all risk for the service principal.Applies to:<br>- [riskDetection](riskdetection)<br>- [riskServicePrincipalActivity](riskserviceprincipalactivity)<br>- [riskyServicePrincipal](riskyserviceprincipal)<br>- [riskyUser](riskyuser)<br>- [servicePrincipalRiskDetection](serviceprincipalriskdetection)<br>- [signIn](signin) |
| userChangedPasswordOnPremises | The user changed their password on-premises.Applies to:<br>- [riskyUser](riskyuser)<br>- [signIn](signin) |
| adminDismissedRiskForSignIn | An admin dismissed the risk for the sign-in.Applies to:<br>- [riskyUser](riskyuser)<br>- [signIn](signin) |
| adminConfirmedAccountSafe | An admin confirmed the account as safe.Applies to:<br>- [riskyUser](riskyuser)<br>- [signIn](signin) |
| microsoftRevokedSessions | Microsoft revoked the user's sessions.Applies to:<br>- [riskDetection](riskdetection)<br>- [riskUserActivity](riskuseractivity)<br>- [riskyUser](riskyuser)<br>- [signIn](signin) |

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "@odata.type": "#microsoft.graph.riskDetail"
}
```

---

## Other Supported Versions

- [graph-rest-beta](https://learn.microsoft.com/en-us/graph/api/resources/riskdetail?view=graph-rest-beta&accept=text/markdown)

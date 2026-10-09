---
layout: Conceptual
title: Microsoft Graph service-specific throttling limits - Microsoft Graph | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/throttling-limits
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
breadcrumb_path: /graph/concepts/breadcrumb/toc.json
author: MSGraphDocsvTeam
ms.author: MSGraphDocsVteam
uhfHeaderId: MSDocsHeader-MSGraph
ms.suite: microsoft-graph
ms.subservice: non-product-specific
toc_preview: true
recommendations: false
ms.service: microsoft-graph
ms.topic: reference
description: Identify the throttling limits for each Microsoft Graph service to apply best practices to manage throttling in your application.
ms.localizationpriority: high
ms.custom: graphiamtop20
ms.date: 2025-01-14T00:00:00.0000000Z
locale: en-us
document_id: ce39639f-5e2c-06d6-5775-ac16a6a4828e
document_version_independent_id: ce39639f-5e2c-06d6-5775-ac16a6a4828e
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/concepts/throttling-limits.md
site_name: Docs
depot_name: MSDN.microsoft-graph-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: throttling-limits
moniker_range_name: 
monikers: []
item_type: Content
source_path: concepts/throttling-limits.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/1433a524-c01f-4b87-beab-670c040dea4f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/312f1f05-a431-4193-8a4d-e6245d5966de
platformId: 19314cc3-e44a-2d85-99fa-ea623cbfcad5
---

# Microsoft Graph service-specific throttling limits - Microsoft Graph | Microsoft Learn

Microsoft Graph concurrently imposes two categories of throttling limits for all API calls:

- Global limits that apply to all services
- Service-specific limits that apply to individual services

Any request can be evaluated against multiple limits, depending on the scope of the limit (per app across all tenants, per tenant for all apps, per app per tenant, and so on), the request type (GET, POST, PATCH, and so on), and other factors. The first limit to be reached triggers throttling behavior.

The following table indicates the global limits:

| Request type | Per app across all tenants |
| --- | --- |
| Any | 130,000 requests per 10 seconds |

The rest of this article provides an overview of the service-specific throttling limits for each Microsoft Graph service.

Note

The specific limits described in this article are subject to change.

In this section, the term *tenant* refers to the Microsoft 365 organization where the application is installed. For a single-tenant application, this tenant can be the same as the one where the application was created; for a multitenant application, it can be a different tenant.

## Assignment service limits

| Request type | Limit per app per tenant | Limit per tenant for all apps |
| --- | --- | --- |
| Any | 350 requests per 10 seconds | 700 requests per 10 seconds |
| Any | 10,000 requests per 3,600 seconds | 20,000 requests per 3,600 seconds |
| POST /publish | 25 requests per 10 seconds | 25 requests per 10 seconds |

The preceding limits apply to the following resources:

- [educationAssignment](/en-us/graph/api/resources/educationassignment)
- [educationSubmission](/en-us/graph/api/resources/educationsubmission)
- [trending](/en-us/graph/api/resources/insights-trending)
- [educationResource](/en-us/graph/api/resources/educationresource)

## Bookings service limits

The Bookings service applies limits to each app ID and mailbox combination, specifically when a particular app accesses a particular booking mailbox. Exceeding the limit for one mailbox doesn't affect the ability of the application to access another mailbox.

| Limit | Applies to |
| --- | --- |
| Four concurrent requests | v1.0 and beta endpoints |

The preceding limits apply to the following resources:

- [business](/en-us/graph/api/resources/bookingbusiness)
- [appointment](/en-us/graph/api/resources/bookingappointment)
- [customQuestion](/en-us/graph/api/resources/bookingcustomquestion)
- [customer](/en-us/graph/api/resources/bookingcustomer)
- [service](/en-us/graph/api/resources/bookingservice)
- [staffMember](/en-us/graph/api/resources/bookingstaffmember)

## Cloud communication service limits

| Resource | Limits per app |
| --- | --- |
| [Calls](/en-us/graph/api/resources/call) | 50,000 requests in a 15-second period, per application per tenant |
| [Meeting information](/en-us/graph/api/resources/meetinginfo) | 2,000 meetings/user each month |
| [Presence](/en-us/graph/api/resources/presence) | 10,000 requests in a 30-second period, per application per tenant |
| [Virtual event](/en-us/graph/api/resources/virtualevent) | 750 `GET` requests per app across all tenants in a 30-second period, and 15 `Create`, `Update`, and `Delete` requests per app across all tenants in a 30-second period. |

### Call records limits

The limits listed in the following table apply to the following resources:

- [callRecord](/en-us/graph/api/resources/callrecords-callrecord)
- [participant](/en-us/graph/api/resources/callrecords-participant)
- [session](/en-us/graph/api/resources/callrecords-session)

| Limit type | Limit |
| --- | --- |
| Per application for all tenants | 15,000 requests per 20 seconds |
| Per tenant for all applications | 10,000 requests per 20 seconds |
| Per application per tenant | 1,500 requests per 20 seconds |
| Per call record | 40 requests per 20 seconds |
| List call records | 40 requests per 20 seconds |

### PSTN call records limits

The limits listed in the following table apply to the following resources:

- [directRoutingLogRow](/en-us/graph/api/resources/callrecords-directroutinglogrow)
- [pstnBlockedUsersLogRow](/en-us/graph/api/resources/callrecords-pstnblockeduserslogrow)
- [pstnCallLogRow](/en-us/graph/api/resources/callrecords-pstncalllogrow)
- [pstnOnlineMeetingDialoutReport](/en-us/graph/api/resources/callrecords-pstnonlinemeetingdialoutreport)
- [smsLogRow](/en-us/graph/api/resources/callrecords-smslogrow)

| Limit type | Limit |
| --- | --- |
| Per tenant | 1,000 requests per 60 seconds |
| Per application per tenant | 200 requests per 60 seconds |
| Per collection | 50 requests per 60 seconds |

## Excel service limits

For explanations and best practices related to Excel service throttling, see [Reduce throttling errors](/en-us/graph/workbook-best-practice#reduce-throttling-errors). In addition, following are some throttling limits.

| Request type | Limit per app for all tenants | Limit per app per tenant |
| --- | --- | --- |
| Any | 5000 requests per 10 seconds | 1500 requests per 10 seconds |

The preceding limits apply to the following resources:

| - | - |
| --- | --- |
| - [workbook](/en-us/graph/api/resources/workbook)<br>- [workbookApplication](/en-us/graph/api/resources/workbookapplication)<br>- [workbookChart](/en-us/graph/api/resources/workbookchart)<br>- [workbookChartAreaFormat](/en-us/graph/api/resources/workbookchartareaformat)<br>- [workbookChartAxes](/en-us/graph/api/resources/workbookchartaxes)<br>- [workbookChartAxis](/en-us/graph/api/resources/workbookchartaxis)<br>- [workbookChartAxisFormat](/en-us/graph/api/resources/workbookchartaxisformat)<br>- [workbookChartAxisTitle](/en-us/graph/api/resources/workbookchartaxistitle)<br>- [workbookChartAxisTitleFormat](/en-us/graph/api/resources/workbookchartaxistitleformat)<br>- [workbookChartDataLabelFormat](/en-us/graph/api/resources/workbookchartdatalabelformat)<br>- [workbookChartDataLabels](/en-us/graph/api/resources/workbookchartdatalabels)<br>- [workbookChartFill](/en-us/graph/api/resources/workbookchartfill)<br>- [workbookChartFont](/en-us/graph/api/resources/workbookchartfont)<br>- [workbookChartGridlines](/en-us/graph/api/resources/workbookchartgridlines)<br>- [workbookChartGridlinesFormat](/en-us/graph/api/resources/workbookchartgridlinesformat)<br>- [workbookChartLegend](/en-us/graph/api/resources/workbookchartlegend)<br>- [workbookChartLegendFormat](/en-us/graph/api/resources/workbookchartlegendformat)<br>- [workbookChartLineFormat](/en-us/graph/api/resources/workbookchartlineformat)<br>- [workbookChartPoint](/en-us/graph/api/resources/workbookchartpoint)<br>- [workbookChartPointFormat](/en-us/graph/api/resources/workbookchartpointformat)<br>- [workbookChartSeries](/en-us/graph/api/resources/workbookchartseries)<br>- [workbookChartSeriesFormat](/en-us/graph/api/resources/workbookchartseriesformat)<br>- [workbookChartTitle](/en-us/graph/api/resources/workbookcharttitle) | - [workbookChartTitleFormat](/en-us/graph/api/resources/workbookcharttitleformat)<br>- [workbookComment](/en-us/graph/api/resources/workbookcomment)<br>- [workbookCommentReply](/en-us/graph/api/resources/workbookcommentreply)<br>- [workbookFilter](/en-us/graph/api/resources/workbookfilter)<br>- [workbookFormatProtection](/en-us/graph/api/resources/formatprotection)<br>- [workbookNamedItem](/en-us/graph/api/resources/workbooknameditem)<br>- [workbookOperation](/en-us/graph/api/resources/workbookoperation)<br>- [workbookPivotTable](/en-us/graph/api/resources/workbookpivottable)<br>- [workbookRange](/en-us/graph/api/resources/workbookrange)<br>- [workbookRangeBorder](/en-us/graph/api/resources/workbookrangeborder)<br>- [workbookRangeFill](/en-us/graph/api/resources/workbookrangefill)<br>- [workbookRangeFont](/en-us/graph/api/resources/workbookrangefont)<br>- [workbookRangeFormat](/en-us/graph/api/resources/workbookrangeformat)<br>- [workbookRangeSort](/en-us/graph/api/resources/workbookrangesort)<br>- [workbookRangeView](/en-us/graph/api/resources/workbookrangeview)<br>- [workbookTable](/en-us/graph/api/resources/workbooktable)<br>- [workbookTableColumn](/en-us/graph/api/resources/workbooktablecolumn)<br>- [workbookTableRow](/en-us/graph/api/resources/workbooktablerow)<br>- [workbookTableSort](/en-us/graph/api/resources/workbooktablesort)<br>- [workbookWorksheet](/en-us/graph/api/resources/workbookworksheet)<br>- [workbookWorksheetProtection](/en-us/graph/api/resources/workbookworksheetprotection) |

## Education service limits

| Request type | Limit per app for all tenants | Limit per app per tenant |
| --- | --- | --- |
| Any | 400,000 requests per 20 seconds | 35,000 requests per 10 seconds |

The preceding limits apply to the following resources:

| - | - |
| --- | --- |
| - [educationClass](/en-us/graph/api/resources/educationclass)<br>- [educationCourse](/en-us/graph/api/resources/educationcourse)<br>- [educationOnPremisesInfo](/en-us/graph/api/resources/educationonpremisesinfo)<br>- [educationOrganization](/en-us/graph/api/resources/educationorganization)<br>- [educationRelatedContact](/en-us/graph/api/resources/relatedcontact)<br>- [educationRoot](/en-us/graph/api/resources/educationroot) | - [educationSchool](/en-us/graph/api/resources/educationschool)<br>- [educationStudent](/en-us/graph/api/resources/educationstudent)<br>- [educationTeacher](/en-us/graph/api/resources/educationteacher)<br>- [educationTerm](/en-us/graph/api/resources/educationterm)<br>- [educationUser](/en-us/graph/api/resources/educationuser) |

## Exchange message trace service limits

| Limit type | Limit |
| --- | --- |
| Per tenant | 100 requests per 5 minutes |

The preceding limits apply to the following resources:

| - | - |
| --- | --- |
| - [exchangeMessageTrace](/en-us/graph/api/resources/exchangemessagetrace) |  |

## Files and lists service limits

For service limits for OneDrive and SharePoint, see [Avoid getting throttled or blocked in SharePoint](/en-us/sharepoint/dev/general-development/how-to-avoid-getting-throttled-or-blocked-in-sharepoint-online).

The preceding information applies to the following resources:

| - | - |
| --- | --- |
| - [baseItem](/en-us/graph/api/resources/baseitem)<br>- [baseItemVersion](/en-us/graph/api/resources/baseitemversion)<br>- [columnDefinition](/en-us/graph/api/resources/columndefinition)<br>- [columnLink](/en-us/graph/api/resources/columnlink)<br>- [contentType](/en-us/graph/api/resources/contenttype)<br>- [drive](/en-us/graph/api/resources/drive)<br>- [driveItem](/en-us/graph/api/resources/driveitem)<br>- [driveItemVersion](/en-us/graph/api/resources/driveitemversion)<br>- [fieldValueSet](/en-us/graph/api/resources/fieldvalueset)<br>- [itemActivity](/en-us/graph/api/resources/itemactivity) | - [itemActivityStat](/en-us/graph/api/resources/itemactivitystat)<br>- [itemAnalytics](/en-us/graph/api/resources/itemanalytics)<br>- [list](/en-us/graph/api/resources/list)<br>- [listItem](/en-us/graph/api/resources/listitem)<br>- [listItemVersion](/en-us/graph/api/resources/listitemversion)<br>- [permission](/en-us/graph/api/resources/permission)<br>- [sharedDriveItem](/en-us/graph/api/resources/shareddriveitem)<br>- [site](/en-us/graph/api/resources/site)<br>- [thumbnailSet](/en-us/graph/api/resources/thumbnailset) |

## Identity and access reports service limits

| Request type | Limit per app for all tenants | Limit per app per tenant |
| --- | --- | --- |
| Any | 122 requests per 10 seconds | Five requests per 10 seconds |
| GET [signInActivity](/en-us/graph/api/resources/signinactivity) | 10 requests per minute | 10 requests per minute |

The preceding limits apply to the following resources:

| - | - |
| --- | --- |
| - [applicationSignInDetailedSummary](/en-us/graph/api/resources/applicationsignindetailedsummary)<br>- [applicationSignInSummary](/en-us/graph/api/resources/applicationsigninsummary)<br>- [auditLogRoot](/en-us/graph/api/resources/auditlogroot)<br>- [authenticationMethod](/en-us/graph/api/resources/authenticationmethod)<br>- [azureADUserFeatureUsage](/en-us/graph/api/resources/userregistrationfeaturesummary)<br>- [credentialUsageSummary](/en-us/graph/api/resources/credentialusagesummary)<br>- [credentialUserRegistrationCount](/en-us/graph/api/resources/credentialuserregistrationcount) | - [credentialUserRegistrationDetails](/en-us/graph/api/resources/credentialuserregistrationdetails)<br>- [directoryAudit](/en-us/graph/api/resources/directoryaudit)<br>- [provisioningObjectSummary](/en-us/graph/api/resources/provisioningobjectsummary)<br>- [relyingPartyDetailedSummary](/en-us/graph/api/resources/relyingpartydetailedsummary)<br>- [signIn](/en-us/graph/api/resources/signin)<br>- [userCredentialUsageDetails](/en-us/graph/api/resources/usercredentialusagedetails)<br>- [signInActivity](/en-us/graph/api/resources/signinactivity)<br>- [userCredentialUsageDetails](/en-us/graph/api/resources/usercredentialusagedetails) |

### Identity and access reports best practices

Microsoft Entra reporting APIs are throttled when Microsoft Entra ID receives too many calls during a given timeframe from a tenant or app. Calls might also be throttled if the service takes too long to respond. If your requests still fail with a `429 Too Many Requests` error code despite applying the [best practices to handle throttling](/en-us/graph/throttling#best-practices-to-handle-throttling), try reducing the amount of data returned. Try these approaches first:

- Use filters to target your query to just the data you need. If you only need a certain type of event or a subset of users, for example, filter out other events using the `$filter` and `$select` query parameters to reduce the size of your response object and the risk of throttling.
- If you need a broad set of Microsoft Entra ID reporting data, use `$filter` on the **createdDateTime** to limit the number of sign-in events you query in a single call. Then, iterate through the next timespan until you have all the records you need. For example, if you're being throttled, you can begin with a call that requests three days of data and iterate with shorter timespans until your requests are no longer throttled.
- The `$select=signInActivity` parameter on the [List users](/en-us/graph/api/user-list) operation may cause stricter throttling than standard Microsoft Graph API calls. To avoid these limits, only use this parameter when necessary. If you need sign-in activity data, use `$top=500` to get the maximum 500 users per page instead of the default 100. This reduces the total number of API calls required.

## Identity and access service limits

### Pattern

Throttling is based on a token bucket algorithm, which works by adding individual costs of requests. The sum of request costs is then compared against predetermined limits. Only the requests exceeding the limits are throttled. If any of the limits are exceeded, the response is `429 Too Many Requests`. It's possible to receive `429 Too Many Requests` responses even when the following limits aren't reached, in situations when the services are under an important load or based on data volume for a specific tenant. The following table lists existing limits.

| Limit type | Resource unit quota | Write quota |
| --- | --- | --- |
| application+tenant pair | S: 3,500 ResourceUnits per 10 seconds  M: 5,000 ResourceUnits per 10 seconds  L: 8,000 ResourceUnits per 10 seconds | 3,000 requests per 2 minutes and 30 seconds |
| application | 150,000 ResourceUnits per 20 seconds | 35,000 requests per 5 minutes |
| tenant | Not Applicable | 18,000 requests per 5 minutes |

Note

The application + tenant pair limit varies based on the number of users in the tenant requests are run against. The tenant sizes are defined as follows: S - under 50 users, M - between 50 and 500 users, and L - above 500 users.

The preceding limits apply to the following resources:

| - | - |
| --- | --- |
| - [application](/en-us/graph/api/resources/application)<br>- [contract](/en-us/graph/api/resources/contract)<br>- [device](/en-us/graph/api/resources/device)<br>- [directoryObjectPartnerReference](/en-us/graph/api/resources/directoryobjectpartnerreference)<br>- [directoryObject](/en-us/graph/api/resources/directoryobject)<br>- [directoryRoleTemplate](/en-us/graph/api/resources/directoryroletemplate)<br>- [directoryRole](/en-us/graph/api/resources/directoryrole)<br>- [domainDnsCnameRecord](/en-us/graph/api/resources/domaindnscnamerecord)<br>- [domainDnsMxRecord](/en-us/graph/api/resources/domaindnsmxrecord)<br>- [domainDnsRecord](/en-us/graph/api/resources/domaindnsrecord)<br>- [domainDnsSrvRecord](/en-us/graph/api/resources/domaindnssrvrecord)<br>- [domainDnsTxtRecord](/en-us/graph/api/resources/domaindnstxtrecord)<br>- [domainDnsUnavailableRecord](/en-us/graph/api/resources/domaindnsunavailablerecord)<br>- [domain](/en-us/graph/api/resources/domain)<br>- [endpoint](/en-us/graph/api/resources/endpoint)<br>- [extensionProperty](/en-us/graph/api/resources/extensionproperty) | - [groupSettingTemplate](/en-us/graph/api/resources/groupsettingtemplate)<br>- [groupSetting](/en-us/graph/api/resources/groupsetting)<br>- [group](/en-us/graph/api/resources/group)<br>- [homeRealmDiscoveryPolicy](/en-us/graph/api/resources/homerealmdiscoverypolicy)<br>- [licenseDetails](/en-us/graph/api/resources/licensedetails)<br>- [oauth2PermissionGrant](/en-us/graph/api/resources/oauth2permissiongrant)<br>- [organization](/en-us/graph/api/resources/organization)<br>- [orgContact](/en-us/graph/api/resources/orgcontact)<br>- [policyBase](/en-us/graph/api/resources/policybase)<br>- [servicePrincipal](/en-us/graph/api/resources/serviceprincipal)<br>- [stsPolicy](/en-us/graph/api/resources/stspolicy)<br>- [subscribedSku](/en-us/graph/api/resources/subscribedsku)<br>- [tokenIssuancePolicy](/en-us/graph/api/resources/tokenissuancepolicy)<br>- [tokenLifetimePolicy](/en-us/graph/api/resources/tokenlifetimepolicy)<br>- [user](/en-us/graph/api/resources/user) |

The following table lists base request costs. Any requests not listed have a base cost of 1.

| Operation | Request Path | Base Resource Unit Cost | Write Cost |
| --- | --- | --- | --- |
| GET | `applications` | 2 | 0 |
| GET | `applications/{id}/extensionProperties` | 2 | 0 |
| GET | `contracts` | 3 | 0 |
| POST | `directoryObjects/getByIds` | 5 | 0 |
| GET | `domains/{id}/domainNameReferences` | 4 | 0 |
| POST | `getObjectsById` | 5 | 0 |
| GET | `groups/{id}/members` | 3 | 0 |
| GET | `groups/{id}/transitiveMembers` | 5 | 0 |
| POST | `isMemberOf` | 4 | 0 |
| POST | `me/checkMemberGroups` | 4 | 0 |
| POST | `me/checkMemberObjects` | 4 | 0 |
| POST | `me/getMemberGroups` | 2 | 0 |
| POST | `me/getMemberObjects` | 2 | 0 |
| GET | `me/licenseDetails` | 2 | 0 |
| GET | `me/memberOf` | 2 | 0 |
| GET | `me/ownedObjects` | 2 | 0 |
| GET | `me/transitiveMemberOf` | 2 | 0 |
| GET | `oauth2PermissionGrants` | 2 | 0 |
| GET | `oauth2PermissionGrants/{id}` | 2 | 0 |
| GET | `servicePrincipals/{id}/appRoleAssignments` | 2 | 0 |
| GET | `subscribedSkus` | 3 | 0 |
| GET | `users` | 2 | 0 |
| GET | Any identity path not listed in the table | 1 | 0 |
| POST | Any identity path not listed in the table | 1 | 1 |
| PATCH | Any identity path not listed in the table | 1 | 1 |
| PUT | Any identity path not listed in the table | 1 | 1 |
| DELETE | Any identity path not listed in the table | 1 | 1 |

Important

The cost of POST, PATCH, and DELETE operations on the `applications` request path depends on the **signInAudience** type. For apps where the **signInAudience** is `AzureADMyOrg` or `AzureADMultipleOrgs`, the cost is 70,000 requests per 5 minutes; while for apps where the **signInAudience** is `AzureADandPersonalMicrosoftAccount` or `PersonalMicrosoftAccount`, the cost is 60 requests per minute.

Other factors that affect a request cost:

- Using `$select` decreases cost by 1
- Using `$expand` increases cost by 1
- Using `$top` with a value of less than 20 decreases cost by 1
- Creating a user in a Microsoft Entra ID B2C tenant increases cost by 4

Note

- A request cost can never be lower than 1. Any request cost that applies to a request path starting with `me/` also applies to equivalent requests starting with `users/{id | userPrincipalName}/`.
- Using `$select` for `directoryObjects/getByIds` and `getObjectsById` results in 2 ResourceUnits.

### Other headers

#### Request headers

- **x-ms-throttle-priority** - If the header doesn't exist or is set to any other value, it indicates a normal request. We recommend setting priority to `high`only for the requests initiated by the user. This header can have one of the following values:
    - Low - Indicates the request is low priority. Throttling this request doesn't cause user-visible failures.
    - Normal - Default if no value is provided. Indicates that the request is default priority.
    - High - Indicates that the request is high priority. Throttling this request causes user-visible failures.

Note

Should requests be throttled, low priority requests are throttled first, normal priority requests second, and high priority requests last. Using the priority request header doesn't change the limits.

#### Regular responses requests

- **x-ms-resource-unit** - Indicates the resource unit used for this request. Values are positive integers.
- **x-ms-throttle-limit-percentage**- Returned only when the application consumed more than 0.8 of its limit. The value ranges from 0.8 to 1.8 and is a percentage of the use of the limit. Callers can use this value to set up an alert and take action.
    - 0.8 indicates you're using 80% of the granted limit.
    - 1.0 indicates you're using 100 % of the granted limit. You start to see throttling.
    - 1.2 indicates 20% of the incoming requests are throttled.
    - 1.8 indicates 80% of the incoming requests are throttled.

#### Throttled responses requests

- **x-ms-throttle-scope** - for example, `Tenant_Application/ReadWrite/9a3d526c-b3c1-4479-ba74-197b5c5751ae/0785ef7c-2d7a-4542-b048-95bcab406e0b`. Indicates the scope of throttling with the following format `<Scope>/<Limit>/<ApplicationId>/<TenantId|UserId|ResourceId>`:
    - Scope: (string, required)
        - Tenant\_Application - All requests for a particular tenant for the current application.
        - Tenant - All requests for the current tenant, regardless of the application.
        - Application - All requests for the current application.
    - Limit: (string, required)
        - Read: Read requests for the scope (GET)
        - Write: Write requests for the scope (POST, PATCH, PUT, DELETE...)
        - ReadWrite: All Requests for the scope (any)
    - ApplicationId (Guid, required)
    - TenantId|UserId|ResourceId: (Guid, required)
- **x-ms-throttle-information**- Indicates the reason for throttling and can have any value (string). The value is provided for diagnostics and troubleshooting purposes, some examples include:
    - CPULimitExceeded - Throttling is because the limit for cpu allocation is exceeded.
    - WriteLimitExceeded - Throttling is because the write limit is exceeded.
    - ResourceUnitLimitExceeded - Throttling is because the limit for the allocated resource unit is exceeded.

## Identity and access data policy operation service limits

| Request type | Limit per tenant |
| --- | --- |
| POST on `exportPersonalData` | 1,000 requests per day for any subject and 100 per subject per day |
| Any other request | 10,000 requests per hour |

The preceding limits apply to the following resources:

- [dataPolicyOperation](/en-us/graph/api/resources/datapolicyoperation)

Note

The resources listed earlier don't return a `Retry-After` header on `429 Too Many Requests` responses.

## Identity and access device operation service limits

| Request type | Limit per app per tenant | Limit per user per tenant |
| --- | --- | --- |
| POST, PATCH, DELETE | 3,000 requests per 2 minutes and 30 seconds | 25 requests per 10 seconds |

The preceding limits apply to write quota for the [device](/en-us/graph/api/resources/device) resource.

## Identity protection and conditional access service limits

| Request type | Limit per tenant for all apps |
| --- | --- |
| Any | One request per second |

| - |
| --- |
| - [riskDetection](/en-us/graph/api/resources/riskdetection)<br>- [riskyUser](/en-us/graph/api/resources/riskyuser)<br>- [riskyUserHistoryItem](/en-us/graph/api/resources/riskyuserhistoryitem)<br>- [namedLocation](/en-us/graph/api/resources/namedlocation)<br>- [countryNamedLocation](/en-us/graph/api/resources/countrynamedlocation)<br>- [ipNamedLocation](/en-us/graph/api/resources/ipnamedlocation)<br>- [conditionalAccessPolicy](/en-us/graph/api/resources/conditionalaccesspolicy) |

Note

The resources listed earlier don't return a `Retry-After` header on `429 Too Many Requests` responses.

## Identity providers service limits

| Request type | Limit per tenant for all apps | Limit per app per tenant |
| --- | --- | --- |
| Any | 300 requests per 1 minute | 200 requests per 1 minute |

The preceding limits apply to the following resources:

| - | - |
| --- | --- |
| - [assignmentOrder](/en-us/graph/api/resources/assignmentorder)<br>- [authenticationEventListener](/en-us/graph/api/resources/authenticationeventlistener)<br>- [authenticationFlowsPolicy](/en-us/graph/api/resources/authenticationflowspolicy)<br>- [b2cAuthenticationMethodsPolicy](/en-us/graph/api/resources/b2cauthenticationmethodspolicy)<br>- [b2cIdentityUserFlow](/en-us/graph/api/resources/b2cidentityuserflow)<br>- [b2xIdentityUserFlow](/en-us/graph/api/resources/b2xidentityuserflow)<br>- [builtInIdentityProvider](/en-us/graph/api/resources/builtinidentityprovider)<br>- [customAuthenticationExtension](/en-us/graph/api/resources/customauthenticationextension)<br>- [identityApiConnector](/en-us/graph/api/resources/identityapiconnector)<br>- [identityBuiltInUserFlowAttribute](/en-us/graph/api/resources/identitybuiltinuserflowattribute)<br>- [identityCustomUserFlowAttribute](/en-us/graph/api/resources/identitycustomuserflowattribute)<br>- [identityProvider](/en-us/graph/api/resources/identityprovider)<br>- [identityUserFlow](/en-us/graph/api/resources/identityuserflow) | - [identityUserFlowAttribute](/en-us/graph/api/resources/identityuserflowattribute)<br>- [identityUserFlowAttributeAssignment](/en-us/graph/api/resources/identityuserflowattributeassignment)<br>- [openIdConnectIdentityProvider](/en-us/graph/api/resources/openidconnectidentityprovider)<br>- [openIdConnectProvider](/en-us/graph/api/resources/openidconnectprovider)<br>- [socialIdentityProvider](/en-us/graph/api/resources/socialidentityprovider)<br>- [trustFrameworkKeySet](/en-us/graph/api/resources/trustframeworkkeyset)<br>- [trustFrameworkPolicy](/en-us/graph/api/resources/trustframeworkpolicy)<br>- [userFlowLanguageConfiguration](/en-us/graph/api/resources/userflowlanguageconfiguration)<br>- [userFlowLanguagePage](/en-us/graph/api/resources/userflowlanguagepage) |

## Industry data ETL service limits

The industry data service limits on-demand [runs](/en-us/graph/api/resources/industrydata-industrydatarun) to a maximum of five successful starts every 12 hours.

## Information protection service limits

The following limits apply to any request on `/informationProtection`.

For email, the resource is a unique network message ID/recipient pair. For example, submitting an email with the same message ID sent to the same person multiple times in a 15-minute period triggers the limit per resource limits listed in the following table. However, you can submit up to 150 unique emails every 15 minutes (tenant limit).

| Operation | Limit per tenant | Limit per resource (email, URL, file) |
| --- | --- | --- |
| POST | 150 requests per 15 minutes and 10,000 requests per 24 hours | One request per 15 minutes and 3 requests per 24 hours |

| - |
| --- |
| - [threatAssessmentRequest](/en-us/graph/api/resources/threatassessmentrequest)<br>- [threatAssessmentResult](/en-us/graph/api/resources/threatassessmentresult)<br>- [mailAssessmentRequest](/en-us/graph/api/resources/mailassessmentrequest)<br>- [emailFileAssessmentRequest](/en-us/graph/api/resources/emailfileassessmentrequest)<br>- [fileAssessmentRequest](/en-us/graph/api/resources/fileassessmentrequest)<br>- [urlAssessmentRequest](/en-us/graph/api/resources/urlassessmentrequest) |

## Insights service limits

The following limits apply to any request on `me/insights` or `users/{id}/insights`.

| Limit | Applies to |
| --- | --- |
| 10,000 API requests in a 10-minute period | v1.0 and beta endpoints |
| Four concurrent requests | v1.0 and beta endpoints |

The preceding limits apply to the following resources:

- [people](/en-us/graph/api/resources/insightssettings)
- [sharedInsight](/en-us/graph/api/resources/insights-shared)
- [trending](/en-us/graph/api/resources/insights-trending)
- [usedInsight](/en-us/graph/api/resources/insights-used)

## Intune service limits

| Request type | Limit per tenant for all apps | Limit per app per tenant |
| --- | --- | --- |
| POST, PUT, DELETE, PATCH | 200 requests per 20 seconds | 100 requests per 20 seconds |
| Any | 2000 requests per 20 seconds | 1000 requests per 20 seconds |

The preceding limits apply to the following resources:

| - |
| --- |
| - [microsoftTunnelConfiguration](/en-us/graph/api/resources/intune-mstunnel-microsofttunnelconfiguration)<br>- [microsoftTunnelHealthThreshold](/en-us/graph/api/resources/intune-mstunnel-microsofttunnelhealththreshold)<br>- [microsoftTunnelServer](/en-us/graph/api/resources/intune-mstunnel-microsofttunnelserver)<br>- [microsoftTunnelServerLogCollectionResponse](/en-us/graph/api/resources/intune-mstunnel-microsofttunnelserverlogcollectionresponse)<br>- [microsoftTunnelSite](/en-us/graph/api/resources/intune-mstunnel-microsofttunnelsite) |

#### Intune android for work service limits

| Request type | Limit per tenant for all apps | Limit per app per tenant |
| --- | --- | --- |
| POST, PUT, DELETE, PATCH | 200 requests per 20 seconds | 100 requests per 20 seconds |
| Any | 2000 requests per 20 seconds | 1000 requests per 20 seconds |

The preceding limits apply to the following resources:

| - | - |
| --- | --- |
| - [androidDeviceOwnerEnrollmentProfile](/en-us/graph/api/resources/intune-androidforwork-androiddeviceownerenrollmentprofile)<br>- [androidForWorkAppConfigurationSchema](/en-us/graph/api/resources/intune-androidforwork-androidforworkappconfigurationschema)<br>- [androidForWorkEnrollmentProfile](/en-us/graph/api/resources/intune-androidforwork-androidforworkenrollmentprofile)<br>- [androidForWorkSettings](/en-us/graph/api/resources/intune-androidforwork-androidforworksettings)<br>- [androidManagedStoreAccountEnterpriseSettings](/en-us/graph/api/resources/intune-androidforwork-androidmanagedstoreaccountenterprisesettings)<br>- [androidManagedStoreAppConfigurationSchema](/en-us/graph/api/resources/intune-androidforwork-androidmanagedstoreappconfigurationschema) |  |

#### Intune applications service limits

| Request type | Limit per tenant for all apps | Limit per app per tenant |
| --- | --- | --- |
| POST, PUT, DELETE, PATCH | 200 requests per 20 seconds | 100 requests per 20 seconds |
| Any | 2000 requests per 20 seconds | 1000 requests per 20 seconds |

The preceding limits apply to the following resources:

| - | - |
| --- | --- |
| - [androidForWorkApp](/en-us/graph/api/resources/intune-apps-androidforworkapp)<br>- [androidForWorkMobileAppConfiguration](/en-us/graph/api/resources/intune-apps-androidforworkmobileappconfiguration)<br>- [androidLobApp](/en-us/graph/api/resources/intune-apps-androidlobapp)<br>- [androidManagedStoreApp](/en-us/graph/api/resources/intune-apps-androidmanagedstoreapp)<br>- [androidManagedStoreAppConfiguration](/en-us/graph/api/resources/intune-apps-androidmanagedstoreappconfiguration)<br>- [androidManagedStoreWebApp](/en-us/graph/api/resources/intune-apps-androidmanagedstorewebapp)<br>- [androidStoreApp](/en-us/graph/api/resources/intune-apps-androidstoreapp)<br>- [enterpriseCodeSigningCertificate](/en-us/graph/api/resources/intune-apps-enterprisecodesigningcertificate)<br>- [iosLobApp](/en-us/graph/api/resources/intune-apps-ioslobapp)<br>- [iosLobAppProvisioningConfiguration](/en-us/graph/api/resources/intune-shared-ioslobappprovisioningconfiguration)<br>- [iosLobAppProvisioningConfigurationAssignment](/en-us/graph/api/resources/intune-apps-ioslobappprovisioningconfigurationassignment)<br>- [iosMobileAppConfiguration](/en-us/graph/api/resources/intune-apps-iosmobileappconfiguration)<br>- [iosStoreApp](/en-us/graph/api/resources/intune-apps-iosstoreapp)<br>- [iosVppApp](/en-us/graph/api/resources/intune-apps-iosvppapp)<br>- [iosVppAppAssignedDeviceLicense](/en-us/graph/api/resources/intune-apps-iosvppappassigneddevicelicense)<br>- [iosVppAppAssignedLicense](/en-us/graph/api/resources/intune-apps-iosvppappassignedlicense)<br>- [iosVppAppAssignedUserLicense](/en-us/graph/api/resources/intune-apps-iosvppappassigneduserlicense)<br>- [macOSLobApp](/en-us/graph/api/resources/intune-apps-macoslobapp)<br>- [macOSMdatpApp](/en-us/graph/api/resources/intune-apps-macosmdatpapp)<br>- [macOSMicrosoftEdgeApp](/en-us/graph/api/resources/intune-apps-macosmicrosoftedgeapp)<br>- [macOSOfficeSuiteApp](/en-us/graph/api/resources/intune-apps-macosofficesuiteapp)<br>- [macOsVppApp](/en-us/graph/api/resources/intune-apps-macosvppapp)<br>- [macOsVppAppAssignedLicense](/en-us/graph/api/resources/intune-apps-macosvppappassignedlicense)<br>- [managedAndroidLobApp](/en-us/graph/api/resources/intune-apps-managedandroidlobapp)<br>- [managedAndroidStoreApp](/en-us/graph/api/resources/intune-apps-managedandroidstoreapp)<br>- [managedApp](/en-us/graph/api/resources/intune-apps-managedapp)<br>- [managedDeviceMobileAppConfiguration](/en-us/graph/api/resources/intune-apps-manageddevicemobileappconfiguration)<br>- [managedDeviceMobileAppConfigurationAssignment](/en-us/graph/api/resources/intune-apps-manageddevicemobileappconfigurationassignment)<br>- [managedDeviceMobileAppConfigurationDeviceStatus](/en-us/graph/api/resources/intune-apps-manageddevicemobileappconfigurationdevicestatus)<br>- [managedDeviceMobileAppConfigurationDeviceSummary](/en-us/graph/api/resources/intune-apps-manageddevicemobileappconfigurationdevicesummary)<br>- [managedDeviceMobileAppConfigurationUserStatus](/en-us/graph/api/resources/intune-apps-manageddevicemobileappconfigurationuserstatus)<br>- [managedDeviceMobileAppConfigurationUserSummary](/en-us/graph/api/resources/intune-apps-manageddevicemobileappconfigurationusersummary)<br>- [managedIOSLobApp](/en-us/graph/api/resources/intune-apps-managedioslobapp) | - [managedIOSStoreApp](/en-us/graph/api/resources/intune-apps-managediosstoreapp)<br>- [managedMobileLobApp](/en-us/graph/api/resources/intune-apps-managedmobilelobapp)<br>- [microsoftStoreForBusinessApp](/en-us/graph/api/resources/intune-apps-microsoftstoreforbusinessapp)<br>- [microsoftStoreForBusinessContainedApp](/en-us/graph/api/resources/intune-apps-microsoftstoreforbusinesscontainedapp)<br>- [mobileApp](/en-us/graph/api/resources/intune-apps-mobileapp)<br>- [mobileAppAssignment](/en-us/graph/api/resources/intune-apps-mobileappassignment)<br>- [mobileAppCategory](/en-us/graph/api/resources/intune-apps-mobileappcategory)<br>- [mobileAppContent](/en-us/graph/api/resources/intune-apps-mobileappcontent)<br>- [mobileAppContentFile](/en-us/graph/api/resources/intune-apps-mobileappcontentfile)<br>- [mobileAppDependency](/en-us/graph/api/resources/intune-apps-mobileappdependency)<br>- [mobileAppInstallStatus](/en-us/graph/api/resources/intune-apps-mobileappinstallstatus)<br>- [mobileAppInstallSummary](/en-us/graph/api/resources/intune-apps-mobileappinstallsummary)<br>- [mobileAppProvisioningConfigGroupAssignment](/en-us/graph/api/resources/intune-apps-mobileappprovisioningconfiggroupassignment)<br>- [mobileAppRelationship](/en-us/graph/api/resources/intune-apps-mobileapprelationship)<br>- [mobileAppSupersedence](/en-us/graph/api/resources/intune-apps-mobileappsupersedence)<br>- [mobileContainedApp](/en-us/graph/api/resources/intune-apps-mobilecontainedapp)<br>- [mobileLobApp](/en-us/graph/api/resources/intune-apps-mobilelobapp)<br>- [officeSuiteApp](/en-us/graph/api/resources/intune-apps-officesuiteapp)<br>- [symantecCodeSigningCertificate](/en-us/graph/api/resources/intune-apps-symanteccodesigningcertificate)<br>- [userAppInstallStatus](/en-us/graph/api/resources/intune-apps-userappinstallstatus)<br>- [webApp](/en-us/graph/api/resources/intune-apps-webapp)<br>- [win32LobApp](/en-us/graph/api/resources/intune-apps-win32lobapp)<br>- [windowsAppX](/en-us/graph/api/resources/intune-apps-windowsappx)<br>- [windowsMicrosoftEdgeApp](/en-us/graph/api/resources/intune-apps-windowsmicrosoftedgeapp)<br>- [windowsMobileMSI](/en-us/graph/api/resources/intune-apps-windowsmobilemsi)<br>- [windowsPhone81AppX](/en-us/graph/api/resources/intune-apps-windowsphone81appx)<br>- [windowsPhone81AppXBundle](/en-us/graph/api/resources/intune-apps-windowsphone81appxbundle)<br>- [windowsPhone81StoreApp](/en-us/graph/api/resources/intune-apps-windowsphone81storeapp)<br>- [windowsPhoneXAP](/en-us/graph/api/resources/intune-apps-windowsphonexap)<br>- [windowsStoreApp](/en-us/graph/api/resources/intune-apps-windowsstoreapp)<br>- [windowsUniversalAppX](/en-us/graph/api/resources/intune-apps-windowsuniversalappx)<br>- [windowsUniversalAppXContainedApp](/en-us/graph/api/resources/intune-apps-windowsuniversalappxcontainedapp) |

#### Intune auditing service limits

| Request type | Limit per tenant for all apps | Limit per app per tenant |
| --- | --- | --- |
| POST, PUT, DELETE, PATCH | 200 requests per 20 seconds | 100 requests per 20 seconds |
| Any | 2000 requests per 20 seconds | 1000 requests per 20 seconds |

The preceding limits apply to the following resources:

| - |
| --- |
| - [auditEvent](/en-us/graph/api/resources/intune-auditing-auditevent) |

#### Intune books service limits

| Request type | Limit per tenant for all apps | Limit per app per tenant |
| --- | --- | --- |
| POST, PUT, DELETE, PATCH | 200 requests per 20 seconds | 100 requests per 20 seconds |
| Any | 2000 requests per 20 seconds | 1000 requests per 20 seconds |

The preceding limits apply to the following resources:

| - |
| --- |
| - [deviceInstallState](/en-us/graph/api/resources/intune-books-deviceinstallstate)<br>- [eBookInstallSummary](/en-us/graph/api/resources/intune-books-ebookinstallsummary)<br>- [iosVppEBook](/en-us/graph/api/resources/intune-books-iosvppebook)<br>- [iosVppEBookAssignment](/en-us/graph/api/resources/intune-books-iosvppebookassignment)<br>- [managedEBook](/en-us/graph/api/resources/intune-books-managedebook)<br>- [managedEBookAssignment](/en-us/graph/api/resources/intune-books-managedebookassignment)<br>- [managedEBookCategory](/en-us/graph/api/resources/intune-books-managedebookcategory)<br>- [userInstallStateSummary](/en-us/graph/api/resources/intune-books-userinstallstatesummary) |

#### Intune bundles service limits

| Request type | Limit per tenant for all apps | Limit per app per tenant |
| --- | --- | --- |
| POST, PUT, DELETE, PATCH | 200 requests per 20 seconds | 100 requests per 20 seconds |
| Any | 2000 requests per 20 seconds | 1000 requests per 20 seconds |

The preceding limits apply to the following resources:

| - | - |
| --- | --- |
| - assignmentFilterEvaluationStatusDetails<br>- [deviceAndAppManagementAssignmentFilter](/en-us/graph/api/resources/intune-policyset-deviceandappmanagementassignmentfilter)<br>- [deviceCompliancePolicyPolicySetItem](/en-us/graph/api/resources/intune-policyset-devicecompliancepolicypolicysetitem)<br>- [deviceConfigurationPolicySetItem](/en-us/graph/api/resources/intune-policyset-deviceconfigurationpolicysetitem)<br>- [deviceManagementConfigurationPolicyPolicySetItem](/en-us/graph/api/resources/intune-policyset-devicemanagementconfigurationpolicypolicysetitem)<br>- [deviceManagementScriptPolicySetItem](/en-us/graph/api/resources/intune-policyset-devicemanagementscriptpolicysetitem)<br>- [enrollmentRestrictionsConfigurationPolicySetItem](/en-us/graph/api/resources/intune-policyset-enrollmentrestrictionsconfigurationpolicysetitem)<br>- [iosLobAppProvisioningConfigurationPolicySetItem,](/en-us/graph/api/resources/intune-policyset-ioslobappprovisioningconfigurationpolicysetitem)<br>- [managedAppProtectionPolicySetItem](/en-us/graph/api/resources/intune-policyset-managedappprotectionpolicysetitem) | - [managedDeviceMobileAppConfigurationPolicySetItem](/en-us/graph/api/resources/intune-policyset-manageddevicemobileappconfigurationpolicysetitem)<br>- [mdmWindowsInformationProtectionPolicyPolicySetItem](/en-us/graph/api/resources/intune-policyset-mdmwindowsinformationprotectionpolicypolicysetitem)<br>- [mobileAppPolicySetItem](/en-us/graph/api/resources/intune-policyset-mobileapppolicysetitem)<br>- [policySet](/en-us/graph/api/resources/intune-policyset-policyset)<br>- [policySetAssignment](/en-us/graph/api/resources/intune-policyset-policysetassignment)<br>- [policySetItem](/en-us/graph/api/resources/intune-policyset-policysetitem)<br>- [targetedManagedAppConfigurationPolicySetItem](/en-us/graph/api/resources/intune-policyset-targetedmanagedappconfigurationpolicysetitem)<br>- [windows10EnrollmentCompletionPageConfigurationPolicySetItem](/en-us/graph/api/resources/intune-policyset-windows10enrollmentcompletionpageconfigurationpolicysetitem)<br>- [windowsAutopilotDeploymentProfilePolicySetItem](/en-us/graph/api/resources/intune-policyset-windowsautopilotdeploymentprofilepolicysetitem) |

#### Intune chromebook sync service limits

| Request type | Limit per tenant for all apps | Limit per app per tenant |
| --- | --- | --- |
| POST, PUT, DELETE, PATCH | 200 requests per 20 seconds | 100 requests per 20 seconds |
| Any | 2000 requests per 20 seconds | 1000 requests per 20 seconds |

The preceding limits apply to the following resources:

| - |
| --- |
| - [chromeOSOnboardingSettings](/en-us/graph/api/resources/intune-chromebooksync-chromeosonboardingsettings) |

#### Intune company terms service limits

| Request type | Limit per tenant for all apps | Limit per app per tenant |
| --- | --- | --- |
| POST, PUT, DELETE, PATCH | 200 requests per 20 seconds | 100 requests per 20 seconds |
| Any | 2000 requests per 20 seconds | 1000 requests per 20 seconds |

The preceding limits apply to the following resources:

| - |
| --- |
| - [termsAndConditions](/en-us/graph/api/resources/intune-companyterms-termsandconditions)<br>- [termsAndConditionsAcceptanceStatus](/en-us/graph/api/resources/intune-companyterms-termsandconditionsacceptancestatus)<br>- [termsAndConditionsAssignment](/en-us/graph/api/resources/intune-companyterms-termsandconditionsassignment)<br>- [termsAndConditionsGroupAssignment](/en-us/graph/api/resources/intune-companyterms-termsandconditionsgroupassignment) |

#### Intune device config v2 service limits

| Request type | Limit per tenant for all apps | Limit per app per tenant |
| --- | --- | --- |
| POST, PUT, DELETE, PATCH | 200 requests per 20 seconds | 100 requests per 20 seconds |
| Any | 2000 requests per 20 seconds | 1000 requests per 20 seconds |

The preceding limits apply to the following resources:

| - | - |
| --- | --- |
| - [deviceManagementConfigurationCategory](/en-us/graph/api/resources/intune-deviceconfigv2-devicemanagementconfigurationcategory)<br>- [deviceManagementConfigurationChoiceSettingCollectionDefinition](/en-us/graph/api/resources/intune-deviceconfigv2-devicemanagementconfigurationchoicesettingcollectiondefinition)<br>- [deviceManagementConfigurationChoiceSettingDefinition](/en-us/graph/api/resources/intune-deviceconfigv2-devicemanagementconfigurationchoicesettingcollectiondefinition)<br>- [deviceManagementConfigurationPolicy](/en-us/graph/api/resources/intune-deviceconfigv2-devicemanagementconfigurationpolicy)<br>- [deviceManagementConfigurationPolicyAssignment](/en-us/graph/api/resources/intune-deviceconfigv2-devicemanagementconfigurationpolicyassignment)<br>- [deviceManagementConfigurationPolicyTemplate](/en-us/graph/api/resources/intune-deviceconfigv2-devicemanagementconfigurationpolicytemplate)<br>- [deviceManagementConfigurationSetting](/en-us/graph/api/resources/intune-deviceconfigv2-devicemanagementconfigurationsetting) | - [deviceManagementConfigurationSettingDefinition](/en-us/graph/api/resources/intune-deviceconfigv2-devicemanagementconfigurationsettingdefinition)<br>- [deviceManagementConfigurationSettingGroupCollectionDefinition](/en-us/graph/api/resources/intune-deviceconfigv2-devicemanagementconfigurationsettinggroupcollectiondefinition)<br>- [deviceManagementConfigurationSettingGroupDefinition](/en-us/graph/api/resources/intune-deviceconfigv2-devicemanagementconfigurationsettinggroupdefinition)<br>- [deviceManagementConfigurationSettingTemplate](/en-us/graph/api/resources/intune-deviceconfigv2-devicemanagementconfigurationsettingtemplate)<br>- [deviceManagementConfigurationSimpleSettingCollectionDefinition](/en-us/graph/api/resources/intune-deviceconfigv2-devicemanagementconfigurationsimplesettingcollectiondefinition)<br>- [deviceManagementConfigurationSimpleSettingDefinition](/en-us/graph/api/resources/intune-deviceconfigv2-devicemanagementconfigurationsimplesettingdefinition)<br>- [deviceManagementReusablePolicySetting](/en-us/graph/api/resources/intune-deviceconfigv2-devicemanagementreusablepolicysetting) |

#### Intune device configuration service limits

| Request type | Limit per tenant for all apps | Limit per app per tenant |
| --- | --- | --- |
| POST, PUT, DELETE, PATCH | 200 requests per 20 seconds | 100 requests per 20 seconds |
| Any | 2000 requests per 20 seconds | 1000 requests per 20 seconds |

The preceding limits apply to the following resources:

| - | - |
| --- | --- |
| - [advancedThreatProtectionOnboardingDeviceSettingState](/en-us/graph/api/resources/intune-deviceconfig-advancedthreatprotectiononboardingdevicesettingstate)<br>- [advancedThreatProtectionOnboardingStateSummary](/en-us/graph/api/resources/intune-deviceconfig-advancedthreatprotectiononboardingstatesummary)<br>- [androidCertificateProfileBase](/en-us/graph/api/resources/intune-deviceconfig-androidcertificateprofilebase)<br>- [androidCompliancePolicy](/en-us/graph/api/resources/intune-deviceconfig-androidcompliancepolicy)<br>- [androidCustomConfiguration](/en-us/graph/api/resources/intune-deviceconfig-androidcustomconfiguration)<br>- androidDeviceComplianceLocalActionBase<br>- androidDeviceComplianceLocalActionLockDevice<br>- androidDeviceComplianceLocalActionLockDeviceWithPasscode<br>- [androidDeviceOwnerCertificateProfileBase](/en-us/graph/api/resources/intune-deviceconfig-androiddeviceownercertificateprofilebase)<br>- [androidDeviceOwnerCompliancePolicy](/en-us/graph/api/resources/intune-deviceconfig-androiddeviceownercompliancepolicy)<br>- [androidDeviceOwnerDerivedCredentialAuthenticationConfiguration](/en-us/graph/api/resources/intune-deviceconfig-androiddeviceownerderivedcredentialauthenticationconfiguration)<br>- [androidDeviceOwnerEnterpriseWiFiConfiguration](/en-us/graph/api/resources/intune-deviceconfig-androiddeviceownerenterprisewificonfiguration)<br>- [androidDeviceOwnerGeneralDeviceConfiguration](/en-us/graph/api/resources/intune-deviceconfig-androiddeviceownergeneraldeviceconfiguration)<br>- [androidDeviceOwnerImportedPFXCertificateProfile](/en-us/graph/api/resources/intune-deviceconfig-androiddeviceownerimportedpfxcertificateprofile)<br>- [androidDeviceOwnerPkcsCertificateProfile](/en-us/graph/api/resources/intune-deviceconfig-androiddeviceownerpkcscertificateprofile)<br>- [androidDeviceOwnerScepCertificateProfile](/en-us/graph/api/resources/intune-deviceconfig-androiddeviceownerscepcertificateprofile)<br>- [androidDeviceOwnerTrustedRootCertificate](/en-us/graph/api/resources/intune-deviceconfig-androiddeviceownertrustedrootcertificate)<br>- [androidDeviceOwnerVpnConfiguration](/en-us/graph/api/resources/intune-deviceconfig-androiddeviceownervpnconfiguration)<br>- [androidDeviceOwnerWiFiConfiguration](/en-us/graph/api/resources/intune-deviceconfig-androiddeviceownerwificonfiguration)<br>- [androidEasEmailProfileConfiguration](/en-us/graph/api/resources/intune-deviceconfig-androideasemailprofileconfiguration)<br>- [androidEnterpriseWiFiConfiguration](/en-us/graph/api/resources/intune-deviceconfig-androidenterprisewificonfiguration)<br>- [androidForWorkCertificateProfileBase](/en-us/graph/api/resources/intune-deviceconfig-androidforworkcertificateprofilebase)<br>- [androidForWorkCompliancePolicy](/en-us/graph/api/resources/intune-deviceconfig-androidforworkcompliancepolicy)<br>- [androidForWorkCustomConfiguration](/en-us/graph/api/resources/intune-deviceconfig-androidforworkcustomconfiguration)<br>- [androidForWorkEasEmailProfileBase](/en-us/graph/api/resources/intune-deviceconfig-androidforworkeasemailprofilebase)<br>- [androidForWorkEnterpriseWiFiConfiguration](/en-us/graph/api/resources/intune-deviceconfig-androidforworkenterprisewificonfiguration)<br>- [androidForWorkGeneralDeviceConfiguration](/en-us/graph/api/resources/intune-deviceconfig-androidforworkgeneraldeviceconfiguration)<br>- [androidForWorkGmailEasConfiguration](/en-us/graph/api/resources/intune-deviceconfig-androidforworkgmaileasconfiguration)<br>- [androidForWorkImportedPFXCertificateProfile](/en-us/graph/api/resources/intune-deviceconfig-androidforworkimportedpfxcertificateprofile)<br>- [androidForWorkNineWorkEasConfiguration](/en-us/graph/api/resources/intune-deviceconfig-androidforworknineworkeasconfiguration)<br>- [androidForWorkPkcsCertificateProfile](/en-us/graph/api/resources/intune-deviceconfig-androidforworkpkcscertificateprofile)<br>- [androidForWorkScepCertificateProfile](/en-us/graph/api/resources/intune-deviceconfig-androidforworkscepcertificateprofile)<br>- [androidForWorkTrustedRootCertificate](/en-us/graph/api/resources/intune-deviceconfig-androidforworktrustedrootcertificate)<br>- [androidForWorkVpnConfiguration](/en-us/graph/api/resources/intune-deviceconfig-androidforworkvpnconfiguration)<br>- [androidForWorkWiFiConfiguration](/en-us/graph/api/resources/intune-deviceconfig-androidforworkwificonfiguration)<br>- [androidGeneralDeviceConfiguration](/en-us/graph/api/resources/intune-deviceconfig-androidgeneraldeviceconfiguration)<br>- [androidImportedPFXCertificateProfile](/en-us/graph/api/resources/intune-deviceconfig-androidimportedpfxcertificateprofile)<br>- [androidOmaCpConfiguration](/en-us/graph/api/resources/intune-deviceconfig-androidomacpconfiguration)<br>- [androidPkcsCertificateProfile](/en-us/graph/api/resources/intune-deviceconfig-androidpkcscertificateprofile)<br>- [androidScepCertificateProfile](/en-us/graph/api/resources/intune-deviceconfig-androidscepcertificateprofile)<br>- [androidTrustedRootCertificate](/en-us/graph/api/resources/intune-deviceconfig-androidtrustedrootcertificate)<br>- [androidVpnConfiguration](/en-us/graph/api/resources/intune-deviceconfig-androidvpnconfiguration)<br>- [androidWiFiConfiguration](/en-us/graph/api/resources/intune-deviceconfig-androidwificonfiguration)<br>- [androidWorkProfileCertificateProfileBase](/en-us/graph/api/resources/intune-deviceconfig-androidworkprofilecertificateprofilebase)<br>- [androidWorkProfileCompliancePolicy](/en-us/graph/api/resources/intune-deviceconfig-androidworkprofilecompliancepolicy)<br>- [androidWorkProfileCustomConfiguration](/en-us/graph/api/resources/intune-deviceconfig-androidworkprofilecustomconfiguration)<br>- [androidWorkProfileEasEmailProfileBase](/en-us/graph/api/resources/intune-deviceconfig-androidworkprofileeasemailprofilebase)<br>- [androidWorkProfileEnterpriseWiFiConfiguration](/en-us/graph/api/resources/intune-deviceconfig-androidworkprofileenterprisewificonfiguration)<br>- [androidWorkProfileGeneralDeviceConfiguration](/en-us/graph/api/resources/intune-deviceconfig-androidworkprofilegeneraldeviceconfiguration)<br>- [androidWorkProfileGmailEasConfiguration](/en-us/graph/api/resources/intune-deviceconfig-androidworkprofilegmaileasconfiguration)<br>- [androidWorkProfileNineWorkEasConfiguration](/en-us/graph/api/resources/intune-deviceconfig-androidworkprofilenineworkeasconfiguration)<br>- [androidWorkProfilePkcsCertificateProfile](/en-us/graph/api/resources/intune-deviceconfig-androidworkprofilepkcscertificateprofile)<br>- [androidWorkProfileScepCertificateProfile](/en-us/graph/api/resources/intune-deviceconfig-androidworkprofilescepcertificateprofile)<br>- [androidWorkProfileTrustedRootCertificate](/en-us/graph/api/resources/intune-deviceconfig-androidworkprofiletrustedrootcertificate)<br>- [androidWorkProfileVpnConfiguration](/en-us/graph/api/resources/intune-deviceconfig-androidworkprofilevpnconfiguration)<br>- [androidWorkProfileWiFiConfiguration](/en-us/graph/api/resources/intune-deviceconfig-androidworkprofilewificonfiguration)<br>- [aospDeviceOwnerCompliancePolicy](/en-us/graph/api/resources/intune-deviceconfig-aospdeviceownercompliancepolicy)<br>- [aospDeviceOwnerDeviceConfiguration](/en-us/graph/api/resources/intune-deviceconfig-aospdeviceownerdeviceconfiguration)<br>- [appleDeviceFeaturesConfigurationBase](/en-us/graph/api/resources/intune-deviceconfig-appledevicefeaturesconfigurationbase)<br>- [appleExpeditedCheckinConfigurationBase](/en-us/graph/api/resources/intune-deviceconfig-appleexpeditedcheckinconfigurationbase)<br>- [appleVpnConfiguration](/en-us/graph/api/resources/intune-deviceconfig-applevpnconfiguration)<br>- [cartToClassAssociation](/en-us/graph/api/resources/intune-deviceconfig-carttoclassassociation)<br>- [defaultDeviceCompliancePolicy](/en-us/graph/api/resources/intune-deviceconfig-defaultdevicecompliancepolicy)<br>- [deviceComplianceActionItem](/en-us/graph/api/resources/intune-deviceconfig-devicecomplianceactionitem)<br>- [deviceComplianceDeviceOverview](/en-us/graph/api/resources/intune-deviceconfig-devicecompliancedeviceoverview)<br>- [deviceComplianceDeviceStatus](/en-us/graph/api/resources/intune-deviceconfig-devicecompliancedevicestatus)<br>- [deviceCompliancePolicy](/en-us/graph/api/resources/intune-shared-devicecompliancepolicy)<br>- [deviceCompliancePolicyAssignment](/en-us/graph/api/resources/intune-deviceconfig-devicecompliancepolicyassignment)<br>- [deviceCompliancePolicyDeviceStateSummary](/en-us/graph/api/resources/intune-deviceconfig-devicecompliancepolicydevicestatesummary)<br>- [deviceCompliancePolicyGroupAssignment](/en-us/graph/api/resources/intune-deviceconfig-devicecompliancepolicysettingstatesummary)<br>- [deviceCompliancePolicySettingStateSummary](/en-us/graph/api/resources/intune-deviceconfig-devicecompliancepolicysettingstatesummary)<br>- deviceCompliancePolicyState<br>- [deviceComplianceScheduledActionForRule](/en-us/graph/api/resources/intune-deviceconfig-devicecompliancescheduledactionforrule)<br>- [deviceComplianceSettingState](/en-us/graph/api/resources/intune-deviceconfig-devicecompliancesettingstate)<br>- [deviceComplianceUserOverview](/en-us/graph/api/resources/intune-deviceconfig-devicecomplianceuseroverview)<br>- [deviceComplianceUserStatus](/en-us/graph/api/resources/intune-deviceconfig-devicecomplianceuserstatus)<br>- [deviceConfiguration](/en-us/graph/api/resources/intune-shared-deviceconfiguration)<br>- [deviceConfigurationAssignment](/en-us/graph/api/resources/intune-deviceconfig-deviceconfigurationassignment)<br>- [deviceConfigurationConflictSummary](/en-us/graph/api/resources/intune-deviceconfig-deviceconfigurationconflictsummary)<br>- [deviceConfigurationDeviceOverview](/en-us/graph/api/resources/intune-deviceconfig-deviceconfigurationdeviceoverview)<br>- [deviceConfigurationDeviceStateSummary](/en-us/graph/api/resources/intune-deviceconfig-deviceconfigurationdevicestatesummary)<br>- [deviceConfigurationDeviceStatus](/en-us/graph/api/resources/intune-deviceconfig-deviceconfigurationdevicestatus)<br>- [deviceConfigurationGroupAssignment](/en-us/graph/api/resources/intune-deviceconfig-deviceconfigurationgroupassignment)<br>- deviceConfigurationState<br>- [deviceConfigurationUserOverview](/en-us/graph/api/resources/intune-deviceconfig-deviceconfigurationuseroverview)<br>- [deviceConfigurationUserStateSummary](/en-us/graph/api/resources/intune-deviceconfig-deviceconfigurationuserstatesummary)<br>- [deviceConfigurationUserStatus](/en-us/graph/api/resources/intune-deviceconfig-deviceconfigurationuserstatus)<br>- [deviceManagement](/en-us/graph/api/resources/intune-deviceconfig-devicemanagement)<br>- deviceSetupConfiguration<br>- [easEmailProfileConfigurationBase](/en-us/graph/api/resources/intune-deviceconfig-easemailprofileconfigurationbase)<br>- [editionUpgradeConfiguration](/en-us/graph/api/resources/intune-deviceconfig-editionupgradeconfiguration)<br>- [iosCertificateProfile](/en-us/graph/api/resources/intune-deviceconfig-ioscertificateprofile)<br>- [iosCertificateProfileBase](/en-us/graph/api/resources/intune-deviceconfig-ioscertificateprofilebase)<br>- [iosCompliancePolicy](/en-us/graph/api/resources/intune-deviceconfig-ioscompliancepolicy)<br>- [iosCustomConfiguration](/en-us/graph/api/resources/intune-deviceconfig-ioscustomconfiguration) | - [iosDerivedCredentialAuthenticationConfiguration](/en-us/graph/api/resources/intune-deviceconfig-iosderivedcredentialauthenticationconfiguration)<br>- [iosDeviceFeaturesConfiguration](/en-us/graph/api/resources/intune-deviceconfig-iosdevicefeaturesconfiguration)<br>- [iosEasEmailProfileConfiguration](/en-us/graph/api/resources/intune-deviceconfig-ioseasemailprofileconfiguration)<br>- [iosEducationDeviceConfiguration](/en-us/graph/api/resources/intune-deviceconfig-ioseducationdeviceconfiguration)<br>- [iosEduDeviceConfiguration](/en-us/graph/api/resources/intune-deviceconfig-iosedudeviceconfiguration)<br>- [iosEnterpriseWiFiConfiguration](/en-us/graph/api/resources/intune-deviceconfig-iosenterprisewificonfiguration)<br>- [iosExpeditedCheckinConfiguration](/en-us/graph/api/resources/intune-deviceconfig-iosexpeditedcheckinconfiguration)<br>- [iosGeneralDeviceConfiguration](/en-us/graph/api/resources/intune-deviceconfig-iosgeneraldeviceconfiguration)<br>- [iosikEv2VpnConfiguration](/en-us/graph/api/resources/intune-deviceconfig-iosikev2vpnconfiguration)<br>- [iosImportedPFXCertificateProfile](/en-us/graph/api/resources/intune-deviceconfig-iosimportedpfxcertificateprofile)<br>- [iosPkcsCertificateProfile](/en-us/graph/api/resources/intune-deviceconfig-iospkcscertificateprofile)<br>- [iosScepCertificateProfile](/en-us/graph/api/resources/intune-deviceconfig-iosscepcertificateprofile)<br>- [iosTrustedRootCertificate](/en-us/graph/api/resources/intune-deviceconfig-iostrustedrootcertificate)<br>- [iosUpdateConfiguration](/en-us/graph/api/resources/intune-deviceconfig-iosupdateconfiguration)<br>- [iosUpdateDeviceStatus](/en-us/graph/api/resources/intune-deviceconfig-iosupdatedevicestatus)<br>- [iosVpnConfiguration](/en-us/graph/api/resources/intune-deviceconfig-iosvpnconfiguration)<br>- [iosWiFiConfiguration](/en-us/graph/api/resources/intune-deviceconfig-ioswificonfiguration)<br>- [macOSCertificateProfileBase](/en-us/graph/api/resources/intune-deviceconfig-macoscertificateprofilebase)<br>- [macOSCompliancePolicy](/en-us/graph/api/resources/intune-deviceconfig-macoscompliancepolicy)<br>- [macOSCustomAppConfiguration](/en-us/graph/api/resources/intune-deviceconfig-macoscustomappconfiguration)<br>- [macOSCustomConfiguration](/en-us/graph/api/resources/intune-deviceconfig-macoscustomconfiguration)<br>- [macOSDeviceFeaturesConfiguration](/en-us/graph/api/resources/intune-deviceconfig-macosdevicefeaturesconfiguration)<br>- [macOSEndpointProtectionConfiguration](/en-us/graph/api/resources/intune-deviceconfig-macosendpointprotectionconfiguration)<br>- [macOSEnterpriseWiFiConfiguration](/en-us/graph/api/resources/intune-deviceconfig-macosenterprisewificonfiguration)<br>- [macOSExtensionsConfiguration](/en-us/graph/api/resources/intune-deviceconfig-macosextensionsconfiguration)<br>- [macOSGeneralDeviceConfiguration](/en-us/graph/api/resources/intune-deviceconfig-macosgeneraldeviceconfiguration)<br>- [macOSImportedPFXCertificateProfile](/en-us/graph/api/resources/intune-deviceconfig-macosimportedpfxcertificateprofile)<br>- [macOSPkcsCertificateProfile](/en-us/graph/api/resources/intune-deviceconfig-macospkcscertificateprofile)<br>- [macOSScepCertificateProfile](/en-us/graph/api/resources/intune-deviceconfig-macosscepcertificateprofile)<br>- [macOSSoftwareUpdateAccountSummary](/en-us/graph/api/resources/intune-deviceconfig-macossoftwareupdateaccountsummary)<br>- [macOSSoftwareUpdateCategorySummary](/en-us/graph/api/resources/intune-deviceconfig-macossoftwareupdatecategorysummary)<br>- [macOSSoftwareUpdateConfiguration](/en-us/graph/api/resources/intune-deviceconfig-macossoftwareupdateconfiguration)<br>- [macOSSoftwareUpdateStateSummary](/en-us/graph/api/resources/intune-deviceconfig-macossoftwareupdatestatesummary)<br>- [macOSTrustedRootCertificate](/en-us/graph/api/resources/intune-deviceconfig-macostrustedrootcertificate)<br>- [macOSVpnConfiguration](/en-us/graph/api/resources/intune-deviceconfig-macosvpnconfiguration)<br>- [macOSWiFiConfiguration](/en-us/graph/api/resources/intune-deviceconfig-macoswificonfiguration)<br>- [macOSWiredNetworkConfiguration](/en-us/graph/api/resources/intune-deviceconfig-macoswirednetworkconfiguration)<br>- [managedAllDeviceCertificateState](/en-us/graph/api/resources/intune-deviceconfig-managedalldevicecertificatestate)<br>- [managedDeviceCertificateState](/en-us/graph/api/resources/intune-deviceconfig-manageddevicecertificatestate)<br>- [managedDeviceEncryptionState](/en-us/graph/api/resources/intune-deviceconfig-manageddeviceencryptionstate)<br>- managedDeviceMobileAppConfigurationState<br>- [ndesConnector](/en-us/graph/api/resources/intune-deviceconfig-ndesconnector)<br>- [restrictedAppsViolation](/en-us/graph/api/resources/intune-deviceconfig-restrictedappsviolation)<br>- [settingStateDeviceSummary](/en-us/graph/api/resources/intune-deviceconfig-settingstatedevicesummary)<br>- [sharedPCConfiguration](/en-us/graph/api/resources/intune-deviceconfig-sharedpcconfiguration)<br>- [softwareUpdateStatusSummary](/en-us/graph/api/resources/intune-deviceconfig-softwareupdatestatussummary)<br>- [unsupportedDeviceConfiguration](/en-us/graph/api/resources/intune-deviceconfig-unsupporteddeviceconfiguration)<br>- [vpnConfiguration](/en-us/graph/api/resources/intune-deviceconfig-vpnconfiguration)<br>- [windows10CertificateProfileBase](/en-us/graph/api/resources/intune-deviceconfig-windows10certificateprofilebase)<br>- [windows10CompliancePolicy](/en-us/graph/api/resources/intune-deviceconfig-windows10compliancepolicy)<br>- [windows10CustomConfiguration](/en-us/graph/api/resources/intune-deviceconfig-windows10customconfiguration)<br>- [windows10DeviceFirmwareConfigurationInterface](/en-us/graph/api/resources/intune-deviceconfig-windows10devicefirmwareconfigurationinterface)<br>- [windows10EasEmailProfileConfiguration](/en-us/graph/api/resources/intune-deviceconfig-windows10easemailprofileconfiguration)<br>- [windows10EndpointProtectionConfiguration](/en-us/graph/api/resources/intune-deviceconfig-windows10endpointprotectionconfiguration)<br>- [windows10EnterpriseModernAppManagementConfiguration](/en-us/graph/api/resources/intune-deviceconfig-windows10enterprisemodernappmanagementconfiguration)<br>- [windows10GeneralConfiguration](/en-us/graph/api/resources/intune-deviceconfig-windows10generalconfiguration)<br>- [windows10ImportedPFXCertificateProfile](/en-us/graph/api/resources/intune-deviceconfig-windows10importedpfxcertificateprofile)<br>- [windows10MobileCompliancePolicy](/en-us/graph/api/resources/intune-deviceconfig-windows10mobilecompliancepolicy)<br>- [windows10NetworkBoundaryConfiguration](/en-us/graph/api/resources/intune-deviceconfig-windows10networkboundaryconfiguration)<br>- [windows10PFXImportCertificateProfile](/en-us/graph/api/resources/intune-deviceconfig-windows10pfximportcertificateprofile)<br>- [windows10PkcsCertificateProfile](/en-us/graph/api/resources/intune-deviceconfig-windows10pkcscertificateprofile)<br>- [windows10SecureAssessmentConfiguration](/en-us/graph/api/resources/intune-deviceconfig-windows10secureassessmentconfiguration)<br>- [windows10TeamGeneralConfiguration](/en-us/graph/api/resources/intune-deviceconfig-windows10teamgeneralconfiguration)<br>- [windows10VpnConfiguration](/en-us/graph/api/resources/intune-deviceconfig-windows10vpnconfiguration)<br>- [windows81CertificateProfileBase](/en-us/graph/api/resources/intune-deviceconfig-windows81certificateprofilebase)<br>- [windows81CompliancePolicy](/en-us/graph/api/resources/intune-deviceconfig-windows81compliancepolicy)<br>- [windows81GeneralConfiguration](/en-us/graph/api/resources/intune-deviceconfig-windows81generalconfiguration)<br>- [windows81SCEPCertificateProfile](/en-us/graph/api/resources/intune-deviceconfig-windows81scepcertificateprofile)<br>- [windows81TrustedRootCertificate](/en-us/graph/api/resources/intune-deviceconfig-windows81trustedrootcertificate)<br>- [windows81VpnConfiguration](/en-us/graph/api/resources/intune-deviceconfig-windows81vpnconfiguration)<br>- [windows81WifiImportConfiguration](/en-us/graph/api/resources/intune-deviceconfig-windows81wifiimportconfiguration)<br>- windowsAssignedAccessProfile<br>- [windowsCertificateProfileBase](/en-us/graph/api/resources/intune-deviceconfig-windowscertificateprofilebase)<br>- [windowsDefenderAdvancedThreatProtectionConfiguration](/en-us/graph/api/resources/intune-deviceconfig-windowsdefenderadvancedthreatprotectionconfiguration)<br>- [windowsDeliveryOptimizationConfiguration](/en-us/graph/api/resources/intune-deviceconfig-windowsdeliveryoptimizationconfiguration)<br>- [windowsDomainJoinConfiguration](/en-us/graph/api/resources/intune-shared-windowsdomainjoinconfiguration)<br>- [windowsHealthMonitoringConfiguration](/en-us/graph/api/resources/intune-deviceconfig-windowshealthmonitoringconfiguration)<br>- [windowsIdentityProtectionConfiguration](/en-us/graph/api/resources/intune-deviceconfig-windowsidentityprotectionconfiguration)<br>- [windowsKioskConfiguration](/en-us/graph/api/resources/intune-deviceconfig-windowskioskconfiguration)<br>- [windowsPhone81CertificateProfileBase](/en-us/graph/api/resources/intune-deviceconfig-windowsphone81certificateprofilebase)<br>- [windowsPhone81CompliancePolicy](/en-us/graph/api/resources/intune-deviceconfig-windowsphone81compliancepolicy)<br>- [windowsPhone81CustomConfiguration](/en-us/graph/api/resources/intune-deviceconfig-windowsphone81customconfiguration)<br>- [windowsPhone81GeneralConfiguration](/en-us/graph/api/resources/intune-deviceconfig-windowsphone81generalconfiguration)<br>- [windowsPhone81ImportedPFXCertificateProfile](/en-us/graph/api/resources/intune-deviceconfig-windowsphone81importedpfxcertificateprofile)<br>- [windowsPhone81SCEPCertificateProfile](/en-us/graph/api/resources/intune-deviceconfig-windowsphone81scepcertificateprofile)<br>- [windowsPhone81TrustedRootCertificate](/en-us/graph/api/resources/intune-deviceconfig-windowsphone81trustedrootcertificate)<br>- [windowsPhone81VpnConfiguration](/en-us/graph/api/resources/intune-deviceconfig-windowsphone81vpnconfiguration)<br>- [windowsPhoneEASEmailProfileConfiguration](/en-us/graph/api/resources/intune-deviceconfig-windowsphoneeasemailprofileconfiguration)<br>- [windowsPrivacyDataAccessControlItem](/en-us/graph/api/resources/intune-deviceconfig-windowsprivacydataaccesscontrolitem)<br>- [windowsUpdateForBusinessConfiguration](/en-us/graph/api/resources/intune-deviceconfig-windowsupdateforbusinessconfiguration)<br>- [windowsUpdateState](/en-us/graph/api/resources/intune-shared-windowsupdatestate)<br>- [windowsVpnConfiguration](/en-us/graph/api/resources/intune-deviceconfig-windowsvpnconfiguration)<br>- [windowsWifiConfiguration](/en-us/graph/api/resources/intune-deviceconfig-windowswificonfiguration)<br>- [windowsWifiEnterpriseEAPConfiguration](/en-us/graph/api/resources/intune-deviceconfig-windowswifienterpriseeapconfiguration) |

#### Intune device enrollment service limits

| Request type | Limit per tenant for all apps | Limit per app per tenant |
| --- | --- | --- |
| POST, PUT, DELETE, PATCH | 200 requests per 20 seconds | 100 requests per 20 seconds |
| Any | 2000 requests per 20 seconds | 1000 requests per 20 seconds |

The preceding limits apply to the following resources:

| - | - |
| --- | --- |
| - [complianceManagementPartner](/en-us/graph/api/resources/intune-onboarding-compliancemanagementpartner)<br>- [deviceAppManagement](/en-us/graph/api/resources/intune-unlock-deviceappmanagement)<br>- [deviceCategory](/en-us/graph/api/resources/intune-shared-devicecategory)<br>- [deviceComanagementAuthorityConfiguration](/en-us/graph/api/resources/intune-onboarding-devicecomanagementauthorityconfiguration)<br>- [deviceEnrollmentConfiguration](/en-us/graph/api/resources/intune-shared-deviceenrollmentconfiguration)<br>- [deviceEnrollmentLimitConfiguration](/en-us/graph/api/resources/intune-onboarding-deviceenrollmentlimitconfiguration)<br>- [deviceEnrollmentPlatformRestrictionsConfiguration](/en-us/graph/api/resources/intune-onboarding-deviceenrollmentplatformrestrictionsconfiguration)<br>- [deviceEnrollmentWindowsHelloForBusinessConfiguration](/en-us/graph/api/resources/intune-onboarding-deviceenrollmentwindowshelloforbusinessconfiguration)<br>- [deviceManagementExchangeConnector](/en-us/graph/api/resources/intune-onboarding-devicemanagementexchangeconnector) | - [deviceManagementExchangeOnPremisesPolicy](/en-us/graph/api/resources/intune-onboarding-devicemanagementexchangeonpremisespolicy)<br>- [deviceManagementPartner](/en-us/graph/api/resources/intune-onboarding-devicemanagementpartner)<br>- [enrollmentConfigurationAssignment](/en-us/graph/api/resources/intune-onboarding-enrollmentconfigurationassignment)<br>- [mobileThreatDefenseConnector](/en-us/graph/api/resources/intune-onboarding-mobilethreatdefenseconnector)<br>- [onPremisesConditionalAccessSettings](/en-us/graph/api/resources/intune-onboarding-onpremisesconditionalaccesssettings)<br>- [sideLoadingKey](/en-us/graph/api/resources/intune-onboarding-sideloadingkey)<br>- [vppToken](/en-us/graph/api/resources/intune-onboarding-vpptoken)<br>- [windows10EnrollmentCompletionPageConfiguration](/en-us/graph/api/resources/intune-onboarding-windows10enrollmentcompletionpageconfiguration) |

#### Intune device intent service limits

| Request type | Limit per tenant for all apps | Limit per app per tenant |
| --- | --- | --- |
| POST, PUT, DELETE, PATCH | 200 requests per 20 seconds | 100 requests per 20 seconds |
| Any | 2000 requests per 20 seconds | 1000 requests per 20 seconds |

The preceding limits apply to the following resources:

| - | - |
| --- | --- |
| - [deviceManagementAbstractComplexSettingDefinition](/en-us/graph/api/resources/intune-deviceintent-devicemanagementabstractcomplexsettingdefinition)<br>- [deviceManagementAbstractComplexSettingInstance](/en-us/graph/api/resources/intune-deviceintent-devicemanagementabstractcomplexsettinginstance)<br>- [deviceManagementBooleanSettingInstance](/en-us/graph/api/resources/intune-deviceintent-devicemanagementbooleansettinginstance)<br>- [deviceManagementCollectionSettingDefinition](/en-us/graph/api/resources/intune-deviceintent-devicemanagementcollectionsettingdefinition)<br>- [deviceManagementCollectionSettingInstance](/en-us/graph/api/resources/intune-deviceintent-devicemanagementcollectionsettinginstance)<br>- [deviceManagementComplexSettingDefinition](/en-us/graph/api/resources/intune-deviceintent-devicemanagementcomplexsettingdefinition)<br>- [deviceManagementComplexSettingInstance](/en-us/graph/api/resources/intune-deviceintent-devicemanagementcomplexsettinginstance)<br>- [deviceManagementIntegerSettingInstance](/en-us/graph/api/resources/intune-deviceintent-devicemanagementintegersettinginstance)<br>- [deviceManagementIntent](/en-us/graph/api/resources/intune-deviceintent-devicemanagementintent)<br>- [deviceManagementIntentAssignment](/en-us/graph/api/resources/intune-deviceintent-devicemanagementintentassignment)<br>- [deviceManagementIntentDeviceSettingStateSummary](/en-us/graph/api/resources/intune-deviceintent-devicemanagementintentdevicesettingstatesummary)<br>- [deviceManagementIntentDeviceState](/en-us/graph/api/resources/intune-deviceintent-devicemanagementintentdevicestate)<br>- [deviceManagementIntentDeviceStateSummary](/en-us/graph/api/resources/intune-deviceintent-devicemanagementintentdevicestatesummary)<br>- [deviceManagementIntentSettingCategory](/en-us/graph/api/resources/intune-deviceintent-devicemanagementintentsettingcategory) | - [deviceManagementIntentUserState](/en-us/graph/api/resources/intune-deviceintent-devicemanagementintentuserstate)<br>- [deviceManagementIntentUserStateSummary](/en-us/graph/api/resources/intune-deviceintent-devicemanagementintentuserstatesummary)<br>- [deviceManagementSettingCategory](/en-us/graph/api/resources/intune-deviceintent-devicemanagementsettingcategory)<br>- [deviceManagementSettingDefinition](/en-us/graph/api/resources/intune-deviceintent-devicemanagementsettingdefinition)<br>- [deviceManagementSettingInstance](/en-us/graph/api/resources/intune-deviceintent-devicemanagementsettinginstance)<br>- [deviceManagementStringSettingInstance](/en-us/graph/api/resources/intune-deviceintent-devicemanagementstringsettinginstance)<br>- [deviceManagementTemplate](/en-us/graph/api/resources/intune-deviceintent-devicemanagementtemplate)<br>- [deviceManagementTemplateSettingCategory](/en-us/graph/api/resources/intune-deviceintent-devicemanagementtemplatesettingcategory)<br>- [securityBaselineCategoryStateSummary](/en-us/graph/api/resources/intune-deviceintent-securitybaselinecategorystatesummary)<br>- [securityBaselineDeviceState](/en-us/graph/api/resources/intune-deviceintent-securitybaselinedevicestate)<br>- securityBaselineSettingState<br>- securityBaselineState<br>- [securityBaselineStateSummary](/en-us/graph/api/resources/intune-deviceintent-securitybaselinestatesummary)<br>- [securityBaselineTemplate](/en-us/graph/api/resources/intune-deviceintent-securitybaselinetemplate) |

#### Intune devices service limits

| Request type | Limit per tenant for all apps | Limit per app per tenant |
| --- | --- | --- |
| POST, PUT, DELETE, PATCH | 400 requests per 20 seconds | 200 requests per 20 seconds |
| Any | 4000 requests per 20 seconds | 2000 requests per 20 seconds |

The preceding limits apply to the following resources:

| - | - |
| --- | --- |
| - [applePushNotificationCertificate](/en-us/graph/api/resources/intune-devices-applepushnotificationcertificate)<br>- [appLogCollectionRequest](/en-us/graph/api/resources/intune-devices-applogcollectionrequest)<br>- [cloudPCConnectivityIssue](/en-us/graph/api/resources/intune-devices-cloudpcconnectivityissue)<br>- [comanagementEligibleDevice](/en-us/graph/api/resources/intune-devices-comanagementeligibledevice)<br>- [dataSharingConsent](/en-us/graph/api/resources/intune-devices-datasharingconsent)<br>- [detectedApp](/en-us/graph/api/resources/intune-devices-detectedapp)<br>- [deviceComplianceScript](/en-us/graph/api/resources/intune-devices-devicecompliancescript)<br>- [deviceComplianceScriptDeviceState](/en-us/graph/api/resources/intune-devices-devicecompliancescriptdevicestate)<br>- [deviceComplianceScriptRunSummary](/en-us/graph/api/resources/intune-devices-devicecompliancescriptrunsummary)<br>- [deviceCustomAttributeShellScript](/en-us/graph/api/resources/intune-devices-devicecustomattributeshellscript)<br>- [deviceHealthScript](/en-us/graph/api/resources/intune-devices-devicehealthscript)<br>- [deviceHealthScriptAssignment](/en-us/graph/api/resources/intune-devices-devicehealthscriptassignment)<br>- [deviceHealthScriptDeviceState](/en-us/graph/api/resources/intune-devices-devicehealthscriptdevicestate)<br>- [deviceHealthScriptRunSummary](/en-us/graph/api/resources/intune-devices-devicehealthscriptrunsummary)<br>- [deviceLogCollectionResponse](/en-us/graph/api/resources/intune-devices-devicelogcollectionresponse)<br>- [deviceManagementScript](/en-us/graph/api/resources/intune-shared-devicemanagementscript)<br>- [deviceManagementScriptAssignment](/en-us/graph/api/resources/intune-devices-devicemanagementscriptassignment)<br>- [deviceManagementScriptDeviceState](/en-us/graph/api/resources/intune-devices-devicemanagementscriptdevicestate)<br>- [deviceManagementScriptGroupAssignment](/en-us/graph/api/resources/intune-devices-devicemanagementscriptgroupassignment)<br>- [deviceManagementScriptRunSummary](/en-us/graph/api/resources/intune-devices-devicemanagementscriptrunsummary)<br>- [deviceManagementScriptUserState](/en-us/graph/api/resources/intune-devices-devicemanagementscriptuserstate)<br>- [deviceShellScript](/en-us/graph/api/resources/intune-devices-deviceshellscript)<br>- [malwareStateForWindowsDevice](/en-us/graph/api/resources/intune-devices-malwarestateforwindowsdevice)<br>- [managedDevice](/en-us/graph/api/resources/intune-devices-manageddevice)<br>- [managedDeviceOverview](/en-us/graph/api/resources/intune-devices-manageddeviceoverview)<br>- [remoteActionAudit](/en-us/graph/api/resources/intune-devices-remoteactionaudit)<br>- [userExperienceAnalyticsAppHealthApplicationPerformance](/en-us/graph/api/resources/intune-devices-userexperienceanalyticsapphealthapplicationperformance)<br>- [userExperienceAnalyticsAppHealthAppPerformanceByAppVersion](/en-us/graph/api/resources/intune-devices-userexperienceanalyticsapphealthappperformancebyappversion)<br>- [userExperienceAnalyticsAppHealthAppPerformanceByOSVersion](/en-us/graph/api/resources/intune-devices-userexperienceanalyticsapphealthappperformancebyosversion)<br>- [userExperienceAnalyticsAppHealthDeviceModelPerformance](/en-us/graph/api/resources/intune-devices-userexperienceanalyticsapphealthdevicemodelperformance) | - [userExperienceAnalyticsAppHealthDevicePerformance](/en-us/graph/api/resources/intune-devices-userexperienceanalyticsapphealthdeviceperformance)<br>- [userExperienceAnalyticsAppHealthDevicePerformanceDetails](/en-us/graph/api/resources/intune-devices-userexperienceanalyticsapphealthdeviceperformancedetails)<br>- [userExperienceAnalyticsAppHealthOSVersionPerformance](/en-us/graph/api/resources/intune-devices-userexperienceanalyticsapphealthosversionperformance)<br>- [userExperienceAnalyticsBaseline](/en-us/graph/api/resources/intune-devices-userexperienceanalyticsbaseline)<br>- [userExperienceAnalyticsCategory](/en-us/graph/api/resources/intune-devices-userexperienceanalyticscategory)<br>- [userExperienceAnalyticsDevicePerformance](/en-us/graph/api/resources/intune-devices-userexperienceanalyticsdeviceperformance)<br>- [userExperienceAnalyticsDeviceScores](/en-us/graph/api/resources/intune-devices-userexperienceanalyticsdevicescores)<br>- [userExperienceAnalyticsDeviceStartupHistory](/en-us/graph/api/resources/intune-devices-userexperienceanalyticsdevicestartuphistory)<br>- [userExperienceAnalyticsDeviceStartupProcess](/en-us/graph/api/resources/intune-devices-userexperienceanalyticsdevicestartupprocess)<br>- [userExperienceAnalyticsDeviceStartupProcessPerformance](/en-us/graph/api/resources/intune-devices-userexperienceanalyticsdevicestartupprocessperformance)<br>- [userExperienceAnalyticsDeviceWithoutCloudIdentity](/en-us/graph/api/resources/intune-devices-userexperienceanalyticsdevicewithoutcloudidentity)<br>- [userExperienceAnalyticsImpactingProcess](/en-us/graph/api/resources/intune-devices-userexperienceanalyticsimpactingprocess)<br>- [userExperienceAnalyticsMetric](/en-us/graph/api/resources/intune-devices-userexperienceanalyticsmetric)<br>- [userExperienceAnalyticsMetricHistory](/en-us/graph/api/resources/intune-devices-userexperienceanalyticsmetrichistory)<br>- [userExperienceAnalyticsNotAutopilotReadyDevice](/en-us/graph/api/resources/intune-devices-userexperienceanalyticsnotautopilotreadydevice)<br>- [userExperienceAnalyticsOverview](/en-us/graph/api/resources/intune-devices-userexperienceanalyticsoverview)<br>- [userExperienceAnalyticsRegressionSummary](/en-us/graph/api/resources/intune-devices-userexperienceanalyticsregressionsummary)<br>- [userExperienceAnalyticsRemoteConnection](/en-us/graph/api/resources/intune-devices-userexperienceanalyticsremoteconnection)<br>- [userExperienceAnalyticsResourcePerformance](/en-us/graph/api/resources/intune-devices-userexperienceanalyticsresourceperformance)<br>- [userExperienceAnalyticsScoreHistory](/en-us/graph/api/resources/intune-devices-userexperienceanalyticsscorehistory)<br>- [userExperienceAnalyticsWorkFromAnywhereDevice](/en-us/graph/api/resources/intune-devices-userexperienceanalyticsworkfromanywheredevice)<br>- [userExperienceAnalyticsWorkFromAnywhereMetric](/en-us/graph/api/resources/intune-devices-userexperienceanalyticsworkfromanywheremetric)<br>- [windowsDeviceMalwareState](/en-us/graph/api/resources/intune-devices-windowsdevicemalwarestate)<br>- [windowsMalwareInformation](/en-us/graph/api/resources/intune-devices-windowsmalwareinformation)<br>- [windowsManagedDevice](/en-us/graph/api/resources/intune-devices-windowsmanageddevice)<br>- [windowsManagementApp](/en-us/graph/api/resources/intune-devices-windowsmanagementapp)<br>- [windowsManagementAppHealthState](/en-us/graph/api/resources/intune-devices-windowsmanagementapphealthstate)<br>- windowsManagementAppHealthSummary<br>- [windowsProtectionState](/en-us/graph/api/resources/intune-devices-windowsprotectionstate) |

#### Intune endpoint protection service limits

| Request type | Limit per tenant for all apps | Limit per app per tenant |
| --- | --- | --- |
| POST, PUT, DELETE, PATCH | 200 requests per 20 seconds | 100 requests per 20 seconds |
| Any | 2000 requests per 20 seconds | 1000 requests per 20 seconds |

The preceding limits apply to the following resources:

| - |
| --- |
| - [deviceManagementDerivedCredentialSettings](/en-us/graph/api/resources/intune-shared-devicemanagementderivedcredentialsettings)<br>- [deviceManagementResourceAccessProfileAssignment](/en-us/graph/api/resources/intune-rapolicy-devicemanagementresourceaccessprofileassignment)<br>- [deviceManagementResourceAccessProfileBase](/en-us/graph/api/resources/intune-rapolicy-devicemanagementresourceaccessprofilebase)<br>- [windows10XCertificateProfile](/en-us/graph/api/resources/intune-rapolicy-windows10xcertificateprofile)<br>- [windows10XSCEPCertificateProfile](/en-us/graph/api/resources/intune-rapolicy-windows10xscepcertificateprofile)<br>- [windows10XTrustedRootCertificate](/en-us/graph/api/resources/intune-rapolicy-windows10xtrustedrootcertificate)<br>- [windows10XVpnConfiguration](/en-us/graph/api/resources/intune-rapolicy-windows10xvpnconfiguration)<br>- [windows10XWifiConfiguration](/en-us/graph/api/resources/intune-rapolicy-windows10xwificonfiguration) |

#### Intune enrollment service limits

| Request type | Limit per tenant for all apps | Limit per app per tenant |
| --- | --- | --- |
| POST, PUT, DELETE, PATCH | 200 requests per 20 seconds | 100 requests per 20 seconds |
| Any | 2000 requests per 20 seconds | 1000 requests per 20 seconds |

The preceding limits apply to the following resources:

| - | - |
| --- | --- |
| - [complianceManagementPartner](/en-us/graph/api/resources/intune-onboarding-compliancemanagementpartner)<br>- [deviceAppManagement](/en-us/graph/api/resources/intune-unlock-deviceappmanagement)<br>- [deviceCategory](/en-us/graph/api/resources/intune-shared-devicecategory)<br>- [deviceComanagementAuthorityConfiguration](/en-us/graph/api/resources/intune-onboarding-devicecomanagementauthorityconfiguration)<br>- [deviceEnrollmentConfiguration](/en-us/graph/api/resources/intune-shared-deviceenrollmentconfiguration)<br>- [deviceEnrollmentLimitConfiguration](/en-us/graph/api/resources/intune-onboarding-deviceenrollmentlimitconfiguration)<br>- [deviceEnrollmentPlatformRestrictionsConfiguration](/en-us/graph/api/resources/intune-onboarding-deviceenrollmentplatformrestrictionsconfiguration)<br>- [deviceEnrollmentWindowsHelloForBusinessConfiguration](/en-us/graph/api/resources/intune-onboarding-deviceenrollmentwindowshelloforbusinessconfiguration)<br>- [deviceManagementExchangeConnector](/en-us/graph/api/resources/intune-onboarding-devicemanagementexchangeconnector) | - [deviceManagementExchangeOnPremisesPolicy](/en-us/graph/api/resources/intune-onboarding-devicemanagementexchangeonpremisespolicy)<br>- [deviceManagementPartner](/en-us/graph/api/resources/intune-onboarding-devicemanagementpartner)<br>- [enrollmentConfigurationAssignment](/en-us/graph/api/resources/intune-onboarding-enrollmentconfigurationassignment)<br>- [mobileThreatDefenseConnector](/en-us/graph/api/resources/intune-onboarding-mobilethreatdefenseconnector)<br>- [onPremisesConditionalAccessSettings](/en-us/graph/api/resources/intune-onboarding-onpremisesconditionalaccesssettings)<br>- [sideLoadingKey](/en-us/graph/api/resources/intune-onboarding-sideloadingkey)<br>- [vppToken](/en-us/graph/api/resources/intune-onboarding-vpptoken)<br>- [windows10EnrollmentCompletionPageConfiguration](/en-us/graph/api/resources/intune-onboarding-windows10enrollmentcompletionpageconfiguration) |

#### Intune GPAnalytics service limits

| Request type | Limit per tenant for all apps | Limit per app per tenant |
| --- | --- | --- |
| POST, PUT, DELETE, PATCH | 200 requests per 20 seconds | 100 requests per 20 seconds |
| Any | 2000 requests per 20 seconds | 1000 requests per 20 seconds |

The preceding limits apply to the following resources:

| - |
| --- |
| - [groupPolicyMigrationReport](/en-us/graph/api/resources/intune-gpanalyticsservice-grouppolicymigrationreport)<br>- [groupPolicyObjectFile](/en-us/graph/api/resources/intune-gpanalyticsservice-grouppolicyobjectfile)<br>- [groupPolicySettingMapping](/en-us/graph/api/resources/intune-gpanalyticsservice-grouppolicysettingmapping)<br>- [unsupportedGroupPolicyExtension](/en-us/graph/api/resources/intune-gpanalyticsservice-unsupportedgrouppolicyextension) |

#### Intune managed applications service limits

| Request type | Limit per tenant for all apps | Limit per app per tenant |
| --- | --- | --- |
| POST, PUT, DELETE, PATCH | 200 requests per 20 seconds | 100 requests per 20 seconds |
| Any | 2000 requests per 20 seconds | 1000 requests per 20 seconds |

The preceding limits apply to the following resources:

| - | - |
| --- | --- |
| - [androidManagedAppProtection](/en-us/graph/api/resources/intune-mam-androidmanagedappprotection)<br>- [androidManagedAppRegistration](/en-us/graph/api/resources/intune-mam-androidmanagedappregistration)<br>- [defaultManagedAppProtection](/en-us/graph/api/resources/intune-mam-defaultmanagedappprotection)<br>- [iosManagedAppProtection](/en-us/graph/api/resources/intune-mam-iosmanagedappprotection)<br>- [iosManagedAppRegistration](/en-us/graph/api/resources/intune-mam-iosmanagedappregistration)<br>- [managedAppConfiguration](/en-us/graph/api/resources/intune-mam-managedappconfiguration)<br>- [managedAppOperation](/en-us/graph/api/resources/intune-mam-managedappoperation)<br>- [managedAppPolicy](/en-us/graph/api/resources/intune-mam-managedapppolicy)<br>- [managedAppPolicyDeploymentSummary](/en-us/graph/api/resources/intune-mam-managedapppolicydeploymentsummary)<br>- [managedAppProtection](/en-us/graph/api/resources/intune-mam-managedappprotection)<br>- [managedAppRegistration](/en-us/graph/api/resources/intune-mam-managedappregistration)<br>- [managedAppStatus](/en-us/graph/api/resources/intune-mam-managedappstatus) | - [managedAppStatusRaw](/en-us/graph/api/resources/intune-mam-managedappstatusraw)<br>- [managedMobileApp](/en-us/graph/api/resources/intune-mam-managedmobileapp)<br>- [mdmWindowsInformationProtectionPolicy](/en-us/graph/api/resources/intune-mam-mdmwindowsinformationprotectionpolicy)<br>- [targetedManagedAppConfiguration](/en-us/graph/api/resources/intune-mam-targetedmanagedappconfiguration)<br>- [targetedManagedAppPolicyAssignment](/en-us/graph/api/resources/intune-mam-targetedmanagedapppolicyassignment)<br>- [targetedManagedAppProtection](/en-us/graph/api/resources/intune-mam-targetedmanagedappprotection)<br>- [windowsInformationProtection](/en-us/graph/api/resources/intune-mam-windowsinformationprotection)<br>- [windowsInformationProtectionAppLockerFile](/en-us/graph/api/resources/intune-mam-windowsinformationprotectionapplockerfile)<br>- [windowsInformationProtectionDeviceRegistration](/en-us/graph/api/resources/intune-mam-windowsinformationprotectiondeviceregistration)<br>- [windowsInformationProtectionPolicy](/en-us/graph/api/resources/intune-mam-windowsinformationprotectionpolicy)<br>- [windowsInformationProtectionWipeAction](/en-us/graph/api/resources/intune-mam-windowsinformationprotectionwipeaction) |

#### Intune notifications service limits

| Request type | Limit per tenant for all apps | Limit per app per tenant |
| --- | --- | --- |
| POST, PUT, DELETE, PATCH | 200 requests per 20 seconds | 100 requests per 20 seconds |
| Any | 2000 requests per 20 seconds | 1000 requests per 20 seconds |

The preceding limits apply to the following resources:

| - |
| --- |
| - [localizedNotificationMessage](/en-us/graph/api/resources/intune-notification-localizednotificationmessage)<br>- [notificationMessageTemplate](/en-us/graph/api/resources/intune-notification-notificationmessagetemplate) |

#### Intune ODJ service limits

| Request type | Limit per tenant for all apps | Limit per app per tenant |
| --- | --- | --- |
| POST, PUT, DELETE, PATCH | 200 requests per 20 seconds | 100 requests per 20 seconds |
| Any | 2000 requests per 20 seconds | 1000 requests per 20 seconds |

The preceding limits apply to the following resources:

| - |
| --- |
| - [deviceManagementDomainJoinConnector](/en-us/graph/api/resources/intune-odj-devicemanagementdomainjoinconnector) |

#### Intune partner integration service limits

| Request type | Limit per tenant for all apps | Limit per app per tenant |
| --- | --- | --- |
| POST, PUT, DELETE, PATCH | 200 requests per 20 seconds | 100 requests per 20 seconds |
| Any | 2000 requests per 20 seconds | 1000 requests per 20 seconds |

The preceding limits apply to the following resources:

| - |
| --- |
| - [appVulnerabilityManagedDevice](/en-us/graph/api/resources/intune-partnerintegration-appvulnerabilitymanageddevice)<br>- [appVulnerabilityMobileApp](/en-us/graph/api/resources/intune-partnerintegration-appvulnerabilitymobileapp)<br>- [appVulnerabilityTask](/en-us/graph/api/resources/intune-partnerintegration-appvulnerabilitytask)<br>- [configManagerCollection](/en-us/graph/api/resources/intune-partnerintegration-configmanagercollection)<br>- [deviceAppManagementTask](/en-us/graph/api/resources/intune-partnerintegration-deviceappmanagementtask)<br>- [securityConfigurationTask](/en-us/graph/api/resources/intune-partnerintegration-securityconfigurationtask)<br>- [unmanagedDeviceDiscoveryTask](/en-us/graph/api/resources/intune-partnerintegration-unmanageddevicediscoverytask)<br>- [vulnerableManagedDevice](/en-us/graph/api/resources/intune-partnerintegration-vulnerablemanageddevice) |

#### Intune rbac service limits

| Request type | Limit per tenant for all apps | Limit per app per tenant |
| --- | --- | --- |
| POST, PUT, DELETE, PATCH | 200 requests per 20 seconds | 100 requests per 20 seconds |
| Any | 2000 requests per 20 seconds | 1000 requests per 20 seconds |

The preceding limits apply to the following resources:

| - |
| --- |
| - [deviceAndAppManagementRoleAssignment](/en-us/graph/api/resources/intune-rbac-deviceandappmanagementroleassignment)<br>- [deviceAndAppManagementRoleDefinition](/en-us/graph/api/resources/intune-rbac-deviceandappmanagementroledefinition)<br>- [resourceOperation](/en-us/graph/api/resources/intune-rbac-resourceoperation)<br>- [roleAssignment](/en-us/graph/api/resources/intune-rbac-roleassignment)<br>- [roleDefinition](/en-us/graph/api/resources/intune-rbac-roledefinition)<br>- [roleScopeTag](/en-us/graph/api/resources/intune-rbac-rolescopetag)<br>- [roleScopeTagAutoAssignment](/en-us/graph/api/resources/intune-rbac-rolescopetagautoassignment) |

#### Intune remote assistance service limits

| Request type | Limit per tenant for all apps | Limit per app per tenant |
| --- | --- | --- |
| POST, PUT, DELETE, PATCH | 200 requests per 20 seconds | 100 requests per 20 seconds |
| Any | 2000 requests per 20 seconds | 1000 requests per 20 seconds |

The preceding limits apply to the following resources:

| - |
| --- |
| - [remoteAssistancePartner](/en-us/graph/api/resources/intune-remoteassistance-remoteassistancepartner)<br>- [remoteAssistanceSettings](/en-us/graph/api/resources/intune-remoteassistance-remoteassistancesettings) |

#### Intune telephony service limits

| Request type | Limit per tenant for all apps | Limit per app per tenant |
| --- | --- | --- |
| POST, PUT, DELETE, PATCH | 200 requests per 20 seconds | 100 requests per 20 seconds |
| Any | 2000 requests per 20 seconds | 1000 requests per 20 seconds |

The preceding limits apply to the following resources:

| - |
| --- |
| - [embeddedSIMActivationCodePool](/en-us/graph/api/resources/intune-esim-embeddedsimactivationcodepool)<br>- [embeddedSIMActivationCodePoolAssignment](/en-us/graph/api/resources/intune-esim-embeddedsimactivationcodepoolassignment)<br>- [embeddedSIMDeviceState](/en-us/graph/api/resources/intune-esim-embeddedsimdevicestate) |

#### Intune TEM service limits

| Request type | Limit per tenant for all apps | Limit per app per tenant |
| --- | --- | --- |
| POST, PUT, DELETE, PATCH | 200 requests per 20 seconds | 100 requests per 20 seconds |
| Any | 2000 requests per 20 seconds | 1000 requests per 20 seconds |

The preceding limits apply to the following resources:

| - |
| --- |
| - [telecomExpenseManagementPartner](/en-us/graph/api/resources/intune-tem-telecomexpensemanagementpartner) |

#### Intune troubleshooting service limits

| Request type | Limit per tenant for all apps | Limit per app per tenant |
| --- | --- | --- |
| POST, PUT, DELETE, PATCH | 200 requests per 20 seconds | 100 requests per 20 seconds |
| Any | 2000 requests per 20 seconds | 1000 requests per 20 seconds |

The preceding limits apply to the following resources:

| - |
| --- |
| - [appleVppTokenTroubleshootingEvent](/en-us/graph/api/resources/intune-troubleshooting-applevpptokentroubleshootingevent)<br>- [deviceManagementAutopilotEvent](/en-us/graph/api/resources/intune-troubleshooting-devicemanagementautopilotevent)<br>- [deviceManagementAutopilotPolicyStatusDetail](/en-us/graph/api/resources/intune-troubleshooting-devicemanagementautopilotpolicystatusdetail)<br>- [deviceManagementTroubleshootingEvent](/en-us/graph/api/resources/intune-troubleshooting-devicemanagementtroubleshootingevent)<br>- [enrollmentTroubleshootingEvent](/en-us/graph/api/resources/intune-troubleshooting-enrollmenttroubleshootingevent)<br>- [mobileAppIntentAndState](/en-us/graph/api/resources/intune-troubleshooting-mobileappintentandstate)<br>- [mobileAppTroubleshootingEvent](/en-us/graph/api/resources/intune-shared-mobileapptroubleshootingevent) |

#### Intune unlock service limits

| Request type | Limit per tenant for all apps | Limit per app per tenant |
| --- | --- | --- |
| POST, PUT, DELETE, PATCH | 200 requests per 20 seconds | 100 requests per 20 seconds |
| Any | 2000 requests per 20 seconds | 1000 requests per 20 seconds |

The preceding limits apply to the following resources:

| - |
| --- |
| - [windowsDefenderApplicationControlSupplementalPolicy](/en-us/graph/api/resources/intune-unlock-windowsdefenderapplicationcontrolsupplementalpolicy)<br>- [windowsDefenderApplicationControlSupplementalPolicyAssignment](/en-us/graph/api/resources/intune-unlock-windowsdefenderapplicationcontrolsupplementalpolicyassignment)<br>- [windowsDefenderApplicationControlSupplementalPolicyDeploymentStatus](/en-us/graph/api/resources/intune-unlock-windowsdefenderapplicationcontrolsupplementalpolicydeploymentstatus)<br>- [windowsDefenderApplicationControlSupplementalPolicyDeploymentSummary](/en-us/graph/api/resources/intune-unlock-windowsdefenderapplicationcontrolsupplementalpolicydeploymentsummary) |

#### Intune updates service limits

| Request type | Limit per tenant for all apps | Limit per app per tenant |
| --- | --- | --- |
| POST, PUT, DELETE, PATCH | 200 requests per 20 seconds | 100 requests per 20 seconds |
| Any | 2000 requests per 20 seconds | 1000 requests per 20 seconds |

The preceding limits apply to the following resources:

| - |
| --- |
| - [windowsFeatureUpdateCatalogItem](/en-us/graph/api/resources/intune-softwareupdate-windowsfeatureupdatecatalogitem)<br>- [windowsFeatureUpdateProfile](/en-us/graph/api/resources/intune-softwareupdate-windowsfeatureupdateprofile)<br>- [windowsFeatureUpdateProfileAssignment](/en-us/graph/api/resources/intune-softwareupdate-windowsfeatureupdateprofileassignment)<br>- [windowsQualityUpdateCatalogItem](/en-us/graph/api/resources/intune-softwareupdate-windowsqualityupdatecatalogitem)<br>- [windowsQualityUpdateProfile](/en-us/graph/api/resources/intune-softwareupdate-windowsqualityupdateprofile)<br>- [windowsQualityUpdateProfileAssignment](/en-us/graph/api/resources/intune-softwareupdate-windowsqualityupdateprofileassignment)<br>- [windowsUpdateCatalogItem](/en-us/graph/api/resources/intune-softwareupdate-windowsupdatecatalogitem) |

#### Intune wip service limits

| Request type | Limit per tenant for all apps | Limit per app per tenant |
| --- | --- | --- |
| POST, PUT, DELETE, PATCH | 200 requests per 20 seconds | 100 requests per 20 seconds |
| Any | 2000 requests per 20 seconds | 1000 requests per 20 seconds |

The preceding limits apply to the following resources:

| - |
| --- |
| - [intuneBrandingProfile](/en-us/graph/api/resources/intune-wip-intunebrandingprofile)<br>- [intuneBrandingProfileAssignment](/en-us/graph/api/resources/intune-wip-intunebrandingprofileassignment)<br>- [windowsInformationProtectionAppLearningSummary](/en-us/graph/api/resources/intune-wip-windowsinformationprotectionapplearningsummary)<br>- [windowsInformationProtectionNetworkLearningSummary](/en-us/graph/api/resources/intune-wip-windowsinformationprotectionnetworklearningsummary) |

## Invitation manager service limits

The following limits apply to any request on `/invitations`.

| Operation | Limit per tenant for all apps |
| --- | --- |
| Any operation | 150 requests per 5 seconds |

## Microsoft 365 reports service limits

The following limits apply to any request on `/reports`.

| Operation | Limit per app per tenant | Limit per tenant for all apps |
| --- | --- | --- |
| Any request (CSV) | 14 requests per 10 minutes | 40 requests per 10 minutes |
| Any request (JSON, beta) | 100 requests per 10 minutes | n/a |

The preceding limits apply individually to each report API. For example, a request to the Microsoft Teams user activity report API and a request to the Outlook user activity report API within 10 minutes count as one request out of 14 for each API, not two requests out of 14 for both.

The preceding limits apply to all [usage reports](/en-us/graph/api/resources/report) resources.

## Microsoft Teams service limits

Microsoft Teams applies throttling limits across four independent dimensions. A request is throttled when it exceeds **any** limit that applies to it, so always design for the lowest limit that your scenario hits.

| Dimension | What it counts | When it typically applies |
| --- | --- | --- |
| **Per app** | All requests from one app (client ID) summed across every tenant. | Multitenant apps that serve many customers. |
| **Per app per tenant** | Requests from one app within a single tenant. | The most commonly reached limit. |
| **Per resource** | Requests against a single team, channel, or chat. | Apps that concentrate traffic on one conversation. |
| **Per user** | Requests made on behalf of a single user. | Delegated (user) permission scenarios. |

Limits are expressed as requests per second (rps) unless stated otherwise.

> 
> Each limit is evaluated over a short burst window. A sustained limit of approximately 83 percent of the listed value is also evaluated over a longer window, so a workload that runs continuously at the listed rate can still be throttled. Size your steady-state traffic below the listed limit and use exponential backoff.

A dash (`-`) means that no dedicated limit is defined for that dimension. The request is still subject to the default limits and to any other limit in the same row.

### Teams

| Request | Per app | Per app per tenant | Per resource | Per user |
| --- | --- | --- | --- | --- |
| GET /teams/`{team-id}` | 1500 rps | 30 rps | 4 rps per team | - |
| GET [/me/joinedTeams or /users/`{user-id}`/joinedTeams](/en-us/graph/api/user-list-joinedteams) | 300 rps | 30 rps | - | - |
| POST [/teams](/en-us/graph/api/team-post) | 100 rps | 10 rps | - | - |
| PUT /groups/`{team-id}`/[team](/en-us/graph/api/team-put-teams) | 150 rps | 6 rps | - | - |
| PATCH [/teams/`{team-id}`](/en-us/graph/api/team-update) | 300 rps | 30 rps | 4 rps per team | - |
| POST /teams/`{team-id}`/[clone](/en-us/graph/api/team-clone) | 150 rps | 6 rps | - | - |
| POST /teams/`{team-id}`/[completeMigration](/en-us/graph/api/team-completemigration) | 100 rps | 10 rps | - | - |

### Channels

| Request | Per app | Per app per tenant | Per resource | Per user |
| --- | --- | --- | --- | --- |
| GET /teams/`{team-id}`/[channels](/en-us/graph/api/channel-list) | 1200 rps | 60 rps | 4 rps per team | - |
| GET /teams/`{team-id}`/channels/[`{channel-id}`](/en-us/graph/api/channel-get) | 600 rps | 30 rps | 1 rps per channel | - |
| GET /teams/`{team-id}`/channels/`{channel-id}`/[members](/en-us/graph/api/channel-list-members) | 1200 rps | 60 rps | 1 rps per channel | - |
| POST /teams/`{team-id}`/[channels](/en-us/graph/api/channel-post) | 100 rps | 10 rps | 4 rps per team | - |
| PATCH /teams/`{team-id}`/channels/[`{channel-id}`](/en-us/graph/api/channel-patch) | 300 rps | 30 rps | 1 rps per channel | - |
| DELETE /teams/`{team-id}`/channels/[`{channel-id}`](/en-us/graph/api/channel-delete) | 150 rps | 15 rps | 1 rps per channel | - |
| POST /teams/`{team-id}`/channels/`{channel-id}`/[completeMigration](/en-us/graph/api/channel-completemigration) | 100 rps | 10 rps | - | - |

### Channel messages

| Request | Per app | Per app per tenant | Per resource | Per user |
| --- | --- | --- | --- | --- |
| GET /teams/`{team-id}`/channels/`{channel-id}`/[messages](/en-us/graph/api/channel-list-messages) | 200 rps | 20 rps | 1 rps per channel | - |
| POST /teams/`{team-id}`/channels/`{channel-id}`/[messages](/en-us/graph/api/channel-post-messages) | 500 rps | 50 rps | 1 rps per channel | 1 rps |
| POST /teams/`{team-id}`/channels/`{channel-id}`/messages/`{message-id}`/[replies](/en-us/graph/api/chatmessage-post-replies) | 500 rps | 50 rps | 1 rps per channel | 1 rps |

The POST limits in the preceding table are shared by regular message sends and by [message import](/en-us/microsoftteams/platform/graph-api/import-messages/import-external-messages-to-teams). The per-user limit doesn't apply to import.

### Chats

| Request | Per app | Per app per tenant | Per resource | Per user |
| --- | --- | --- | --- | --- |
| GET [/chats](/en-us/graph/api/chat-list), /me/chats, or /users/`{user-id}`/chats | 200 rps | 20 rps | - | 1 rps |
| GET [/chats/`{chat-id}`](/en-us/graph/api/chat-get) | 2000 rps | 200 rps | 1 rps per chat | 5 rps |
| POST [/chats](/en-us/graph/api/chat-post) | 200 rps | 20 rps | - | - |
| PATCH [/chats/`{chat-id}`](/en-us/graph/api/chat-patch) | 300 rps | 30 rps | 1 rps per chat | - |
| DELETE [/chats/`{chat-id}`](/en-us/graph/api/chat-delete) | 10 rps | 1 rps | 1 rps per chat | - |
| POST /chats/`{chat-id}`/[removeAllAccessForUser](/en-us/graph/api/chat-removeallaccessforuser) | 300 rps | 30 rps | 1 rps per chat | 1 rps |

### Chat messages

| Request | Per app | Per app per tenant | Per resource | Per user |
| --- | --- | --- | --- | --- |
| GET /chats/`{chat-id}`/[messages](/en-us/graph/api/chat-list-messages) | 200 rps | 20 rps | 1 rps per chat | - |
| POST /chats/`{chat-id}`/[messages](/en-us/graph/api/chat-post-messages) | 200 rps | 20 rps | 1 rps per chat | 1 rps |
| PATCH /chats/`{chat-id}`/[messages/`{message-id}`](/en-us/graph/api/chatmessage-update) | 300 rps | 30 rps | 1 rps per chat | - |
| POST /chats/`{chat-id}`/messages/`{message-id}`/[softDelete](/en-us/graph/api/chatmessage-softdelete) or [undoSoftDelete](/en-us/graph/api/chatmessage-undosoftdelete) | 300 rps | 30 rps | 1 rps per chat | - |
| GET /chats/`{chat-id}`/messages/`{message-id}`/[hostedContents](/en-us/graph/api/chatmessagehostedcontent-get) | 500 rps | 50 rps | 1 rps per chat | - |
| GET /chats/`{chat-id}`/messages/`{message-id}`/hostedContents/`{id}`/$value | 600 rps | 60 rps | 1 rps per chat | - |

### Members

| Request | Per app | Per app per tenant | Per resource | Per user |
| --- | --- | --- | --- | --- |
| GET /teams/`{team-id}`/[members](/en-us/graph/api/team-list-members) | 1200 rps | 60 rps | 4 rps per team | - |
| POST /teams/`{team-id}`/[members](/en-us/graph/api/team-post-members) | 300 rps | 30 rps | 4 requests per minute per team | - |
| POST /teams/`{team-id}`/members/[add](/en-us/graph/api/conversationmember-add) | 100 rps | 10 rps | 4 requests per minute per team | - |
| POST /chats/`{chat-id}`/[members](/en-us/graph/api/chat-post-members) | 300 rps | 30 rps | 4 requests per minute per chat | - |
| DELETE /chats/`{chat-id}`/[members/`{membership-id}`](/en-us/graph/api/chat-delete-members) | 300 rps | 30 rps | 4 requests per minute per chat | - |

### Apps, tabs, and permission grants

| Request | Per app | Per app per tenant | Per resource | Per user |
| --- | --- | --- | --- | --- |
| GET installedApps for [team](/en-us/graph/api/team-list-installedapps), [chat](/en-us/graph/api/chat-list-installedapps), or [user](/en-us/graph/api/userteamwork-list-installedapps) | 1500 rps | 30 rps | 1 rps per chat or channel | - |
| GET permissionGrants for [team](/en-us/graph/api/team-list-permissiongrants) or [chat](/en-us/graph/api/chat-list-permissiongrants) | 1500 rps | 30 rps | 1 rps per chat or channel | - |
| POST installedApps for [team](/en-us/graph/api/team-post-installedapps), [chat](/en-us/graph/api/chat-post-installedapps), or [user](/en-us/graph/api/userteamwork-post-installedapps) | 300 rps | 30 rps | 1 rps per chat or channel | - |
| DELETE installedApps for [team](/en-us/graph/api/team-delete-installedapps), [chat](/en-us/graph/api/chat-delete-installedapps), or [user](/en-us/graph/api/userteamwork-delete-installedapps) | 150 rps | 15 rps | 1 rps per chat or channel | - |
| GET tabs for [channel](/en-us/graph/api/channel-list-tabs) or [chat](/en-us/graph/api/chat-list-tabs) | 600 rps | 30 rps | 1 rps per chat or channel | - |
| POST tabs for [channel](/en-us/graph/api/channel-post-tabs) or [chat](/en-us/graph/api/chat-post-tabs) | 300 rps | 30 rps | 1 rps per chat or channel | - |
| PATCH [tab](/en-us/graph/api/channel-patch-tabs) | 300 rps | 30 rps | 1 rps per chat or channel | - |
| DELETE tabs for [channel](/en-us/graph/api/channel-delete-tabs) or [chat](/en-us/graph/api/chat-delete-tabs) | 150 rps | 15 rps | 1 rps per chat or channel | - |
| GET [/appCatalogs/teamsApps](/en-us/graph/api/appcatalogs-list-teamsapps) | 1500 rps | 30 rps | - | - |
| POST [/appCatalogs/teamsApps](/en-us/graph/api/teamsapp-publish) | 300 rps | 30 rps | - | - |
| DELETE [/appCatalogs/teamsApps/`{app-id}`](/en-us/graph/api/teamsapp-delete) | 150 rps | 15 rps | - | - |

### Activity feed notifications

| Request | Per app | Per app per tenant | Per resource | Per user |
| --- | --- | --- | --- | --- |
| POST /teams/`{team-id}`/[sendActivityNotification](/en-us/graph/api/team-sendactivitynotification) | 50 rps | 5 rps | 4 rps per team | - |
| POST /chats/`{chat-id}`/[sendActivityNotification](/en-us/graph/api/chat-sendactivitynotification) | 50 rps | 5 rps | 1 rps per chat | - |
| POST /users/`{user-id}`/teamwork/[sendActivityNotification](/en-us/graph/api/userteamwork-sendactivitynotification) | 50 rps | 5 rps | - | - |
| POST /teamwork/[sendActivityNotificationToRecipients](/en-us/graph/api/teamwork-sendactivitynotificationtorecipients) | 20 rps | 2 rps | - | - |

### Bulk message retrieval

These APIs are designed for export and compliance scenarios and have their own higher limits.

| Request | Per app | Per app per tenant | Per resource | Per user |
| --- | --- | --- | --- | --- |
| GET /teams/`{team-id}`/channels/[getAllMessages](/en-us/graph/api/channel-getallmessages) or /channels/allMessages | 1000 rps | 200 rps | - | - |
| GET /users/`{user-id}`/chats/[getAllMessages](/en-us/graph/api/chats-getallmessages) or /chats/allMessages | 1000 rps | 200 rps | - | - |
| GET /teams/`{team-id}`/channels/[getAllRetainedMessages](/en-us/graph/api/channel-getallretainedmessages) | 1000 rps | 200 rps | - | - |
| GET /users/`{user-id}`/chats/[getAllRetainedMessages](/en-us/graph/api/chat-getallretainedmessages) | 1000 rps | 200 rps | - | - |
| GET /copilot/users/`{user-id}`/interactionHistory/[getAllEnterpriseInteractions](/en-us/microsoft-365-copilot/extensibility/api-reference/aiinteractionhistory-getallenterpriseinteractions) | 1500 rps | 30 rps | - | - |

### Shifts

| Request | Per app | Per app per tenant | Per resource | Per user |
| --- | --- | --- | --- | --- |
| GET /teams/`{team-id}`/[schedule](/en-us/graph/api/schedule-get) and all APIs under this path | 600 rps | 30 rps | - | - |
| POST /teams/`{team-id}`/[schedule](/en-us/graph/api/schedule-share) and all APIs under this path | 300 rps | 30 rps | - | - |
| PUT /teams/`{team-id}`/[schedule](/en-us/graph/api/team-put-schedule) and all APIs under this path | 300 rps | 30 rps | - | - |

### Sections

| Request | Per app | Per app per tenant | Per resource | Per user |
| --- | --- | --- | --- | --- |
| All section management APIs under /users/`{user-id}`/teamwork/[sections](/en-us/graph/api/resources/teamworksection?view=graph-rest-beta&amp;preserve-view=true) | - | 5 rps | - | - |

All section operations, including sections, section items, reorder actions, and delta queries, share a single limit.

### Default limits

Any Microsoft Teams request that isn't listed in the preceding tables uses these limits.

| Request type | Per app | Per app per tenant | Per resource | Per user |
| --- | --- | --- | --- | --- |
| GET | 1500 rps | 30 rps | 1 rps per chat or channel | 1 rps |
| POST, PUT, and PATCH | 300 rps | 30 rps | 1 rps per chat or channel | 1 rps |
| DELETE | 150 rps | 15 rps | 1 rps per chat or channel | 1 rps |

### Related resources

See also [Microsoft Teams limits](/en-us/graph/api/resources/teams-api-overview#microsoft-teams-limits) and [polling requirements](/en-us/graph/api/resources/teams-api-overview#polling-requirements).

The preceding limits apply to the following resources:

| - | - |
| --- | --- |
| - [aadUserConversationMember](/en-us/graph/api/resources/aadUserConversationMember)<br>- [changeTrackedEntity](/en-us/graph/api/resources/changeTrackedEntity)<br>- [channel](/en-us/graph/api/resources/channel)<br>- [chatMessage](/en-us/graph/api/resources/chatMessage)<br>- [chatMessageHostedContent](/en-us/graph/api/resources/chatMessageHostedContent)<br>- [conversationMember](/en-us/graph/api/resources/conversationMember)<br>- [offerShiftRequest](/en-us/graph/api/resources/offerShiftRequest)<br>- [openShift](/en-us/graph/api/resources/openShift)<br>- [openShiftChangeRequest](/en-us/graph/api/resources/openShiftChangeRequest)<br>- [schedule](/en-us/graph/api/resources/schedule)<br>- [schedulingGroup](/en-us/graph/api/resources/schedulingGroup)<br>- [shift](/en-us/graph/api/resources/shift)<br>- [shiftPreferences](/en-us/graph/api/resources/shiftPreferences) | - [swapShiftsChangeRequest](/en-us/graph/api/resources/swapShiftsChangeRequest)<br>- [team](/en-us/graph/api/resources/team)<br>- [teamsApp](/en-us/graph/api/resources/teamsApp)<br>- [teamsAppDefinition](/en-us/graph/api/resources/teamsAppDefinition)<br>- [teamsAppInstallation](/en-us/graph/api/resources/teamsAppInstallation)<br>- [teamsAsyncOperation](/en-us/graph/api/resources/teamsAsyncOperation)<br>- [teamsTab](/en-us/graph/api/resources/teamsTab)<br>- [teamsTemplate](/en-us/graph/api/resources/teamsTemplate)<br>- [teamwork](/en-us/graph/api/resources/teamwork)<br>- [teamworkSection](/en-us/graph/api/resources/teamworksection?view=graph-rest-beta&amp;preserve-view=true)<br>- [teamworkSectionItem](/en-us/graph/api/resources/teamworksectionitem?view=graph-rest-beta&amp;preserve-view=true)<br>- [timeOff](/en-us/graph/api/resources/timeOff)<br>- [timeOffReason](/en-us/graph/api/resources/timeOffReason)<br>- [timeOffRequest](/en-us/graph/api/resources/timeOffRequest)<br>- [userSettings](/en-us/graph/api/resources/userSettings)<br>- [workforceIntegration](/en-us/graph/api/resources/workforceIntegration) |

## Multitenant management service limits

| Request type | Limit per tenant for all apps | Limit per app per tenant |
| --- | --- | --- |
| POST, PUT, DELETE, PATCH | 200 requests per 20 seconds | 100 requests per 20 seconds |
| Any | 2000 requests per 20 seconds | 1000 requests per 20 seconds |

The preceding limits apply to the following resources:

| - | - |
| --- | --- |
| - [aggregatedPolicyCompliance](/en-us/graph/api/resources/managedTenants-aggregatedpolicycompliance)<br>- [cloudPcConnection](/en-us/graph/api/resources/managedTenants-cloudpcconnection)<br>- [cloudPcDevice](/en-us/graph/api/resources/managedTenants-cloudpcdevice)<br>- [cloudPcOverview](/en-us/graph/api/resources/managedTenants-cloudpcoverview)<br>- [conditionalAccessPolicyCoverage](/en-us/graph/api/resources/managedTenants-conditionalaccesspolicycoverage)<br>- [credentialUserRegistrationsSummary](/en-us/graph/api/resources/managedTenants-credentialuserregistrationssummary)<br>- [deviceCompliancePolicySettingStateSummary](/en-us/graph/api/resources/managedTenants-devicecompliancepolicysettingstatesummary)<br>- [managedDeviceCompliance](/en-us/graph/api/resources/managedTenants-manageddevicecompliance)<br>- [managedDeviceComplianceTrend](/en-us/graph/api/resources/managedTenants-manageddevicecompliancetrend)<br>- [managedTenant](/en-us/graph/api/resources/managedTenants-managedtenant)<br>- [managementAction](/en-us/graph/api/resources/managedTenants-managementaction)<br>- [managementActionTenantDeploymentStatus](/en-us/graph/api/resources/managedTenants-managementactiontenantdeploymentstatus) | - [managementIntent](/en-us/graph/api/resources/managedTenants-managementintent)<br>- [managementTemplate](/en-us/graph/api/resources/managedTenants-managementtemplate)<br>- [riskyUser](/en-us/graph/api/resources/riskyuser)<br>- [tenant](/en-us/graph/api/resources/managedTenants-tenant)<br>- [tenantCustomizedInformation](/en-us/graph/api/resources/managedTenants-tenantcustomizedinformation)<br>- [tenantDetailedInformation](/en-us/graph/api/resources/managedTenants-tenantdetailedinformation)<br>- [tenantGroup](/en-us/graph/api/resources/managedTenants-tenantgroup)<br>- [tenantRelationship](/en-us/graph/api/resources/tenantrelationship)<br>- [tenantTag](/en-us/graph/api/resources/managedTenants-tenanttag)<br>- [windowsDeviceMalwareState](/en-us/graph/api/resources/managedTenants-windowsdevicemalwarestate)<br>- [windowsProtectionState](/en-us/graph/api/resources/managedTenants-windowsprotectionstate) |

## OneNote service limits

| Limit type | Limit per app per user (delegated context) | Limit per app (app-only context) |
| --- | --- | --- |
| Requests rate | 120 requests per 1 minute and 400 per 1 hour | 240 requests per 1 minute and 800 per 1 hour |
| Concurrent requests | Five concurrent requests | 20 concurrent requests |

The preceding limits apply to the following resources:

| - |
| --- |
| - [notebook](/en-us/graph/api/resources/notebook)<br>- [onenote](/en-us/graph/api/resources/onenote)<br>- [onenoteOperation](/en-us/graph/api/resources/onenoteresource)<br>- [onenotePage](/en-us/graph/api/resources/onenotepage)<br>- [onenoteResource](/en-us/graph/api/resources/onenoteresource)<br>- [onenoteSection](/en-us/graph/api/resources/onenotesection)<br>- [sectionGroup](/en-us/graph/api/resources/sectiongroup) |

You can find additional information about best practices in [OneNote API throttling and how to avoid it](https://developer.microsoft.com/en-us/office/blogs/onenote-api-throttling-and-how-to-avoid-it/).

Note

The resources listed earlier don't return a `Retry-After` header on `429 Too Many Requests` responses.

## Open and schema extensions service limits

| Request type | Limit per app per tenant |
| --- | --- |
| Any | 455 requests per 10 seconds |

The preceding limits apply to the following resources:

| - | - |
| --- | --- |
| - [administrativeUnit](/en-us/graph/api/resources/administrativeunit)<br>- [contact](/en-us/graph/api/resources/contact)<br>- [device](/en-us/graph/api/resources/device)<br>- [event](/en-us/graph/api/resources/event)<br>- [group](/en-us/graph/api/resources/group)<br>- [message](/en-us/graph/api/resources/message) | - [openTypeExtension](/en-us/graph/api/resources/opentypeextension)<br>- [organization](/en-us/graph/api/resources/organization)<br>- [post](/en-us/graph/api/resources/post)<br>- [schemaExtension](/en-us/graph/api/resources/schemaextension)<br>- [user](/en-us/graph/api/resources/user) |

## Outlook service limits

Outlook service limits apply to the public cloud and [national cloud deployments](deployments).

### Limits per mailbox

The Outlook service applies limits to each app ID and mailbox combination - that is, a specific app accessing a specific user or group mailbox. Exceeding the limit for one mailbox doesn't affect the ability of the application to access another mailbox.

| Limit | Applies to |
| --- | --- |
| 10,000 API requests in a 10-minute period | v1.0 and beta endpoints |
| Four concurrent requests | v1.0 and beta endpoints |
| 150 megabytes (MB) upload (PATCH, POST, PUT) in a 5-minute period | v1.0 and beta endpoints |

### Outlook service resources

| API | Resources |
| --- | --- |
| Search API (preview) | - [External item (Microsoft Search)](/en-us/graph/api/resources/externalconnectors-externalitem) |
| Profile API | - [Photo](/en-us/graph/api/resources/profilephoto) |
| Calendar API | - [event](/en-us/graph/api/resources/event)<br>- [eventMessage](/en-us/graph/api/resources/eventmessage)<br>- [calendar](/en-us/graph/api/resources/calendar)<br>- [calendarGroup](/en-us/graph/api/resources/calendargroup)<br>- [outlookCategory](/en-us/graph/api/resources/outlookcategory)<br>- [attachment](/en-us/graph/api/resources/attachment)<br>- [place (preview)](/en-us/graph/api/resources/place) |
| Mail API | - [message](/en-us/graph/api/resources/message)<br>- [mailFolder](/en-us/graph/api/resources/mailfolder)<br>- [mailSearchFolder](/en-us/graph/api/resources/mailsearchfolder)<br>- [messageRule](/en-us/graph/api/resources/messagerule)<br>- [outlookCategory](/en-us/graph/api/resources/outlookcategory)<br>- [attachment](/en-us/graph/api/resources/attachment) |
| Mailbox import and export API | - [mailbox](/en-us/graph/api/resources/mailbox)<br>- [mailboxItem](/en-us/graph/api/resources/mailboxitem)<br>- [mailboxFolder](/en-us/graph/api/resources/mailboxfolder)<br>- [exchangeSettings](/en-us/graph/api/resources/exchangeSettings) |
| Personal contacts API | - [contact](/en-us/graph/api/resources/contact)<br>- [contactFolder](/en-us/graph/api/resources/contactfolder)<br>- [outlookCategory](/en-us/graph/api/resources/outlookcategory) |
| Social and workplace intelligence | - [person](/en-us/graph/api/resources/person) |
| To-do tasks API (preview) | - [outlookTask](/en-us/graph/api/resources/outlooktask)<br>- [outlookTaskFolder](/en-us/graph/api/resources/outlooktaskfolder)<br>- [outlookTaskGroup](/en-us/graph/api/resources/outlooktaskgroup)<br>- [outlookCategory](/en-us/graph/api/resources/outlookcategory)<br>- [attachment](/en-us/graph/api/resources/attachment) |

### Outlook service limits for JSON batching

When an app makes a [JSON batch](/en-us/graph/json-batching) request that consists of multiple, *unordered* individual requests to the Outlook service, by default, Microsoft Graph sends the Outlook service up to four individual requests from the batch at a time, regardless of the target mailboxes of those requests. The Outlook service can execute these requests in parallel at any point, also irrespective of the target mailbox. Since Microsoft Graph sends only up to four requests to run in parallel, the execution of that batch stays within Outlook's concurrency limits for the same mailbox, regardless of the app used.

Alternatively, an app can use the [dependsOn](/en-us/graph/json-batching#sequencing-requests-with-the-dependson-property) property to order requests within a batch. Microsoft Graph sends the Outlook service one request from the batch at a time following the specified order, and Outlook executes each individual request in the batch sequentially.

In other words, when targeting the *same mailbox*, apps that allow multiple batch requests to run in parallel can use either of the following approaches:

- If the individual requests don't have to be ordered, have individual requests from a single batch run concurrently.
- Use the `dependsOn` property to order requests in a batch, and have up to four such batch requests run concurrently.

## Places service limits

The following Places APIs have a throttling limit of three calls per second:

- [Get operation](/en-us/graph/api/place-getoperation?view=graph-rest-beta&amp;preserve-view=true)
- [List operations](/en-us/graph/api/place-listoperations?view=graph-rest-beta&amp;preserve-view=true)
- [Upsert places](/en-us/graph/api/place-patch-places?view=graph-rest-beta&amp;preserve-view=true)

## Project Rome service limits

| Request type | Limit per user for all apps |
| --- | --- |
| GET | 400 requests per 5 minutes and 12,000 requests per one day |
| POST, PUT, PATCH, DELETE | 100 requests per 5 minutes and 8,000 requests per one day |

The preceding limits apply to the following resources:

- [activityHistoryItem](/en-us/graph/api/resources/projectrome-historyitem)
- [userActivity](/en-us/graph/api/resources/projectrome-activity)

## Security audit log query service limits

The Microsoft Purview Audit Search API applies tenant-level limits to audit log queries submitted through Microsoft Graph. Each tenant receives a baseline allocation. Tenants with more eligible licenses can receive higher limits, up to the maximum capacity allocated by the service. The calculation used to determine a tenant's allocation isn't published.

The following baseline limits apply.

| Limit | Baseline allocation | Scope and behavior |
| --- | --- | --- |
| Query submissions | At least 200 submissions per day | The limit applies across the tenant and is calculated as a rolling window of 24 hours. When the tenant reaches its daily allocation, the service doesn't accept new queries until the 24-hour rolling usage drops below the limit. |
| Queued or running queries | At least 50 queries | The limit applies across the tenant. Only queries in a nonterminal state, such as queued or running, count toward the limit. New queries can be accepted as existing queries reach a terminal state. |
| Records generated by one query | At least 1,000,000 records | The limit applies separately to each query. If a query exceeds its record-count limit, record generation stops at the applicable threshold and the query completes successfully with information indicating that the limit was exceeded. |

### Handle throttled query submissions

When a query submission is throttled, Microsoft Graph returns `429 Too Many Requests`. If the response includes a `Retry-After` header, wait for the specified interval before retrying the request. Don't retry the request immediately.

For a daily submission limit, retry after the tenant's usage in the 24-hour rolling window drops below the limit. For a concurrent-query limit, retry after one or more queued or running queries reach a terminal state. If a `Retry-After` header isn't provided, use an exponential backoff strategy.

For general guidance, see [Microsoft Graph throttling guidance](/en-us/graph/throttling).

### Identify a query that exceeded its record-count limit

Exceeding the per-query record-count limit isn't an error. The query can have a `succeeded` status even when the service stopped generating additional records.

When the information is available, use the following `auditLogQuery` properties:

| Property | Description |
| --- | --- |
| `isRecordCountLimitExceeded` | Indicates whether the query exceeded its per-query record-count limit. Treat this property as the authoritative indicator. |
| `recordCountLimit` | The record-count threshold applied to the query. |
| `approximateReturnedRecordCount` | The approximate number of records generated by the query. This value can be higher or lower than `recordCountLimit` because record counting is distributed. |

Don't determine whether the limit was exceeded by comparing `approximateReturnedRecordCount` with `recordCountLimit`. Use `isRecordCountLimitExceeded`.

## Security detections and incidents service limits

The following limits apply to any request on `/security`.

| Operation | Limit per app per tenant |
| --- | --- |
| Any operation on `alert`, `securityActions`, `secureScore` | 150 requests per minute |
| Any operation on `tiIndicator` | 1,000 requests per minute |
| Any operation on `secureScore` or `secureScorecontrolProfile` | 10,000 API requests in a 10-minute period |
| Any operation on `secureScore` or `secureScorecontrolProfile` | Four concurrent requests |

## Security eDiscovery service limits

The following limits apply to any request on `/security/eDiscoveryCases`.

| Operation | Limit per app per tenant |
| --- | --- |
| Any | Five requests per minute |

## Service Communications service limits

The following limits apply to any type of requests for service communications under `/admin/serviceAnnouncement/`.

| Request type | Limit per app per tenant |
| --- | --- |
| Any | 240 requests per 60 seconds |
| Any | 800 requests per hour |

## Subscription service limits

| Request type | Limit per app for all tenants | Limit per app per tenant |
| --- | --- | --- |
| POST, PUT, DELETE, PATCH | 2000 requests per 20 seconds | 500 requests per 20 seconds |
| POST /reauthorize subscription by ID | 4000 requests per 20 seconds | 1000 requests per 20 seconds |
| GET Subscription by Id | 2000 requests per 20 seconds | 500 requests per 20 seconds |
| GET Subscription List | 40 requests per 20 seconds | 25 requests per 20 seconds |

The preceding limits apply to the [subscription](/en-us/graph/api/resources/subscription) resource.

## Tasks and plans service limits

Service limits for Planner aren't available.

The preceding information applies to the following resources:

| - | - |
| --- | --- |
| - [planner](/en-us/graph/api/resources/planner)<br>- [plannerAssignedToTaskBoardTaskFormat](/en-us/graph/api/resources/plannerassignedtotaskboardtaskformat)<br>- [plannerBucket](/en-us/graph/api/resources/plannerbucket)<br>- [plannerBucketTaskBoardTaskFormat](/en-us/graph/api/resources/plannerbuckettaskboardtaskformat)<br>- [plannerGroup](/en-us/graph/api/resources/plannergroup)<br>- [plannerPlan](/en-us/graph/api/resources/plannerplan) | - [plannerPlanDetails](/en-us/graph/api/resources/plannerplandetails)<br>- [plannerProgressTaskBoardTaskFormat](/en-us/graph/api/resources/plannerprogresstaskboardtaskformat)<br>- [plannerTask](/en-us/graph/api/resources/plannertask)<br>- [plannerTaskDetails](/en-us/graph/api/resources/plannertaskdetails)<br>- [plannerUser](/en-us/graph/api/resources/planneruser) |

## Viva Engage service limits

Viva Engage API calls are subject to rate limiting, allowing 10 requests per user, per app, within a 30-second time period. When you exceed the rate limit, all subsequent requests return a `429 Too Many Requests` response code.

## Windows 365 service limits

| Request type | Limit per tenant for all apps or users | Limit per app or user per tenant |
| --- | --- | --- |
| List Cloud PCs | 180 requests per 60 seconds | 162 requests per 60 seconds |
| Get Cloud PC | 540 requests per 60 seconds | 486 requests per 60 seconds |

Starting September 30, 2025, the per-app/per-user per-tenant throttling limit will be reduced to half of the total per-tenant limit to prevent a single user or app from consuming all the quota within a tenant.

| Request type | Limit per tenant for all apps or users | Limit per app or user per tenant |
| --- | --- | --- |
| List Cloud PCs | 180 requests per 60 seconds | 90 requests per 60 seconds |
| Get Cloud PC | 540 requests per 60 seconds | 270 requests per 60 seconds |
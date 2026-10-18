---
layout: Conceptual
title: Share or delegate a calendar in Outlook - Microsoft Graph | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/graph/outlook-share-or-delegate-calendar
feedback_system: Standard
feedback_product_url: https://developer.microsoft.com/graph/support
breadcrumb_path: /graph/concepts/breadcrumb/toc.json
author: JuForan
ms.author: MSGraphDocsVteam
uhfHeaderId: MSDocsHeader-MSGraph
ms.suite: microsoft-graph
ms.subservice: outlook
toc_preview: true
recommendations: false
ms.service: microsoft-graph
ms.topic: how-to
description: Use the Outlook calendar API to enable a calendar owner to share the calendar with another user or delegate another user to manage meetings in that calendar.
ms.localizationpriority: high
ms.date: 2024-11-07T00:00:00.0000000Z
locale: en-us
document_id: d27a410f-cfbc-b3bf-be49-80fc374a382a
document_version_independent_id: fad0baed-36aa-2d72-afa8-fd5e82ef8f87
original_content_git_url: https://github.com/microsoftgraph/microsoft-graph-docs/blob/live/concepts/outlook-share-or-delegate-calendar.md
site_name: Docs
depot_name: MSDN.microsoft-graph-docs
page_type: conceptual
interactive_type: msgraph
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: outlook-share-or-delegate-calendar
moniker_range_name: 
monikers: []
item_type: Content
source_path: concepts/outlook-share-or-delegate-calendar.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/64b65f6c-101f-411a-9b83-9f577fab52d0
- https://authoring-docs-microsoft.poolparty.biz/devrel/3e34b70d-bca0-4369-a01b-71d1edfd427b
- https://authoring-docs-microsoft.poolparty.biz/devrel/5fc61396-d075-4560-aece-fdbda73d243f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/1a667fd1-8145-4b11-af0f-9f5de205a6e5
- https://authoring-docs-microsoft.poolparty.biz/devrel/8ca32b3f-fa14-46df-b09a-9c4a591d6396
- https://authoring-docs-microsoft.poolparty.biz/devrel/ad9437c1-8cda-4537-ad69-b4b263652e13
platformId: f6789057-86ec-0927-88bc-739bb0ec8cc3
---

# Share or delegate a calendar in Outlook - Microsoft Graph | Microsoft Learn

In Outlook, a calendar owner can share the calendar with another user. The owner can specify which information in non-private events is viewable, and can give write access to the calendar to users in the same organization.

The owner can also delegate another user to manage meetings in the owner's *primary* calendar. Delegates are share recipients who can view all information in and have write access to non-private events. They also receive meeting requests and responses, and respond to meeting requests on behalf of the owner. Additionally, the owner can give explicit permissions to delegates to view the owner's *private* events on the calendar.

Before calendar sharing or delegation can take effect, the owner sends a share recipient or delegate an invitation, and the share recipient or delegate accepts the invitation, or, explicitly adds the shared or delegated calendar for access. The invitation and adding a shared or delegated calendar occur in an Outlook client.

After sharing or delegation is set up in Outlook, apps can then use the Microsoft Graph API to manage the sharing and delegation.

The rest of this article is based on the following example scenario:

- Alex Wilber has delegated Megan Bowen to his primary calendar, and also permitted Megan to view private events in that calendar.
- Alex shared a "Kids parties" calendar with Adele Vance and Megan Bowen, and gave both Adele and Megan `read` permissions to all the details of non-private events on the "Kids parties" calendar, and free/busy status for private events.

This article describes programmatically carrying out the following tasks with a shared or delegated calendar:

- Get calendar information about share recipients, delegates, and allowed permissions, and update individual permissions
- Get the properties that describe the sharing or delegation of the calendar.
- Get or set mailbox setting to receive meeting requests and responses for a delegated calendar.
- Delete a share recipient or delegate of a calendar.

Apps can also do the following using API that is generally available:

- [Get shared or delegated Outlook calendar or its events](outlook-get-shared-events-calendars)
- [Create Outlook events in a shared or delegated calendar](outlook-create-event-in-shared-delegated-calendar)

Note

The properties and API for calendar sharing and delegating described in this topic are currently available in the v1.0 endpoint, with the exception of the calendar property **isShared**, which is exposed only in the beta endpoint.

## Get calendar information about share recipients and delegates, and update individual permissions

In this section:

- Calendar owner: Get sharing or delegation information and permissions
- Calendar owner: Update permissions for an existing share recipient or delegate on a calendar

Each calendar is associated with a collection of [calendarPermission](/en-us/graph/api/resources/calendarpermission) objects, each of which describes a share recipient or delegate and the associated permission that the calendar owner has set up. The [calendarRoleType](/en-us/graph/api/resources/calendarpermission#calendarroletype-values) enumeration defines the range of permissions that Microsoft Graph supports:

- `none` This value applies to only `My Organization` which doesn't have any permissions to the calendar. It doesn't apply to individual users, as only users with permissions are associated with a **calendarPermission** object for the calendar.
- `freeBusyRead` The share recipient can view the owner's free/busy status, but not other details on the calendar.
- `limitedRead` The share recipient can view the owner's free/busy status, and the titles and locations of non-private events on the calendar.
- `read` The share recipient can view the owner's free/busy status in private events, and all the details of non-private events on the calendar.
- `write` The share recipient can view the owner's free/busy status in private events, and can view all the details and edit (create, update, or delete) non-private events on the calendar.
- `delegateWithoutPrivateEventAccess` The *delegate* can view the owner's free/busy status in private events, and has `write` access to non-private events on the calendar.
- `delegateWithPrivateEventAccess` The *delegate* can view details of the owner's private and non-private events, and has `write` access to all the events on the calendar.

The primary calendar of a user is always shared with "My Organization", which represents the users in the same organization as the owner. By default, they can read the owner's free/busy status on that calendar and have the `freeBusyRead` permission.

### Calendar owner: Get sharing or delegation information and permissions

This example shows with the consent of Alex or administrator, how to get the **calendarPermission** objects associated with Alex' primary calendar. The request returns two such permission objects:

- The first **calendarPermission** object is assigned to the delegate, Megan, and has the following property values:

    - **isRemovable** is set to true, providing Alex the option to cancel the delegation.
    - **isInsideOrganization** is true as only users in the same organization can be delegates.
    - **role** for Megan is `delegateWithPrivateEventAccess`, as set up by Alex.
    - **allowedRoles** includes the role types `delegateWithoutPrivateEventAccess` and `delegateWithPrivateEventAccess` that support delegation.
    - **emailAddress** specifies Megan.
- The second **calendarPermission** object is a default object assigned to "My Organization", and has the following property values:

    - **isRemovable** is set to false, since the primary calendar is always shared with the owner's organization.
    - **isInsideOrganization** is true.
    - **role** is `freeBusyRead`, the default setting for "My Organization".
    - **emailAddress** specifies the **name** sub-property as "My Organization"; **address** for "My Organization" is by default null.

**Microsoft Graph permissions**

Use the least privileged delegated or application permission, `Calendars.Read`, as appropriate, for this operation. For more information, see [calendar permissions](permissions-reference).

# [HTTP](#tab/http)
```msgraph
GET https://graph.microsoft.com/beta/users/AlexW@contoso.com/calendar/calendarPermissions
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Users["{user-id}"].Calendar.CalendarPermissions.GetAsync();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v0.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-beta-sdk-go"  //other-imports
)

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
calendarPermissions, err := graphClient.Users().ByUserId("user-id").Calendar().CalendarPermissions().Get(context.Background(), nil)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

CalendarPermissionCollectionResponse result = graphClient.users().byUserId("{user-id}").calendar().calendarPermissions().get();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

let calendarPermissions = await client.api('/users/AlexW@contoso.com/calendar/calendarPermissions').version('beta').get();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\Beta\GraphServiceClient;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$result = $graphServiceClient->users()->byUserId('user-id')->calendar()->calendarPermissions()->get()->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Beta.Calendar

Get-MgBetaUserCalendarPermission -UserId $userId

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph_beta import GraphServiceClient
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python

result = await graph_client.users.by_user_id('user-id').calendar.calendar_permissions.get()

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

```http
HTTP/1.1 200 OK
Content-type: application/json

{
    "@odata.context": "https://graph.microsoft.com/beta/$metadata#users('64339082-ed84-4b0b-b4ab-004ae54f3747')/calendar/calendarPermissions",
    "value": [
        {
            "id": "L289RXhjaGFuZ2VMYWJTWVnYW5C",
            "isRemovable": true,
            "isInsideOrganization": true,
            "role": "delegateWithPrivateEventAccess",
            "allowedRoles": [
                "freeBusyRead",
                "limitedRead",
                "read",
                "write",
                "delegateWithoutPrivateEventAccess",
                "delegateWithPrivateEventAccess"
            ],
            "emailAddress": {
                "name": "Megan Bowen",
                "address": "MeganB@contoso.com"
            }
        },
        {
            "id": "RGVmYXVsdA==",
            "isRemovable": false,
            "isInsideOrganization": true,
            "role": "freeBusyRead",
            "allowedRoles": [
                "none",
                "freeBusyRead",
                "limitedRead",
                "read",
                "write"
            ],
            "emailAddress": {
                "name": "My Organization"
            }
        }
    ]
}
```

### Calendar owner: Update permissions for an existing share recipient or delegate on a calendar

With the consent of Alex or administrator, you can update the permissions assigned to an existing share recipient or delegate (specified by the **role** property), as long as the new permissions are supported by those **allowedRoles** set up initially for the share recipient or delegate for that calendar.

Aside from the **role** property, you can't update other properties of an existing share recipient or delegate. Changing the **emailAddress** property value requires deleting the share recipient or delegate and setting up a new instance of **calendarPermission** again.

The example in this section updates the **role** property, changing the permission of an existing share recipient, Adele, from `read` to `write` for the custom calendar "Kids parties".

**Microsoft Graph permissions**

Use the least privileged delegated or application permission, `Calendars.ReadWrite`, as appropriate, for this operation. For more information, see [calendar permissions](permissions-reference).

# [HTTP](#tab/http)
```http
PATCH https://graph.microsoft.com/beta/users/AlexW@contoso.com/calendars/AAMkADAwAABf02bAAAA=/calendarPermissions/L289RXhjaGFuZ2VMYWJQWRlbGVW
Content-type: application/json

{
  "role": "write"
}
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// Dependencies
using Microsoft.Graph.Beta.Models;

var requestBody = new CalendarPermission
{Role = CalendarRoleType.Write,
};

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Users["{user-id}"].Calendars["{calendar-id}"].CalendarPermissions["{calendarPermission-id}"].PatchAsync(requestBody);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v0.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-beta-sdk-go"  graphmodels "github.com/microsoftgraph/msgraph-beta-sdk-go/models"  //other-imports
)

requestBody := graphmodels.NewCalendarPermission()
role := graphmodels.WRITE_CALENDARROLETYPE 
requestBody.SetRole(&role) 

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
calendarPermissions, err := graphClient.Users().ByUserId("user-id").Calendars().ByCalendarId("calendar-id").CalendarPermissions().ByCalendarPermissionId("calendarPermission-id").Patch(context.Background(), requestBody, nil)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

CalendarPermission calendarPermission = new CalendarPermission();
calendarPermission.setRole(CalendarRoleType.Write);
CalendarPermission result = graphClient.users().byUserId("{user-id}").calendars().byCalendarId("{calendar-id}").calendarPermissions().byCalendarPermissionId("{calendarPermission-id}").patch(calendarPermission);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

const calendarPermission = {
  role: 'write'
};

await client.api('/users/AlexW@contoso.com/calendars/AAMkADAwAABf02bAAAA=/calendarPermissions/L289RXhjaGFuZ2VMYWJQWRlbGVW').version('beta').update(calendarPermission);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\Beta\GraphServiceClient;
use Microsoft\Graph\Beta\Generated\Models\CalendarPermission;
use Microsoft\Graph\Beta\Generated\Models\CalendarRoleType;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestBody = new CalendarPermission();
$requestBody->setRole(new CalendarRoleType('write'));

$result = $graphServiceClient->users()->byUserId('user-id')->calendars()->byCalendarId('calendar-id')->calendarPermissions()->byCalendarPermissionId('calendarPermission-id')->patch($requestBody)->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```
Snippet not available
```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph_beta import GraphServiceClient
from msgraph_beta.generated.models.calendar_permission import CalendarPermission
from msgraph_beta.generated.models.calendar_role_type import CalendarRoleType
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
request_body = CalendarPermission(role = CalendarRoleType.Write,
)

result = await graph_client.users.by_user_id('user-id').calendars.by_calendar_id('calendar-id').calendar_permissions.by_calendar_permission_id('calendarPermission-id').patch(request_body)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

```http
HTTP/1.1 200 OK
Content-type: application/json

{
    "@odata.context": "https://graph.microsoft.com/beta/$metadata#users('64339082-ed84-4b0b-b4ab-004ae54f3747')/calendars('AAMkADAwAABf02bAAAA%3D')/calendarPermissions/$entity",
    "id": "L289RXhjaGFuZ2VMYWJQWRlbGVW",
    "isRemovable": true,
    "isInsideOrganization": true,
    "role": "write",
    "allowedRoles": [
        "freeBusyRead",
        "limitedRead",
        "read",
        "write"
    ],
    "emailAddress": {
        "name": "Adele Vance",
        "address": "AdeleV@contoso.com"
    }
}
```

## Get properties of a shared or delegated calendar

In this section:

- Calendar owner: Get properties of a shared or delegated calendar
- share recipient or delegate: Get properties of shared or delegated calendar

Recalling in this example, Alex has delegated his primary calendar and given the delegate, Megan Bowen, the permission to view calendar items that are marked private. This section shows the properties of the delegated calendar, first from the perspective of and with the consent of the owner, Alex, and then from the perspective of and with the consent of the delegate, Megan. Consent from the administrator also works for each case.

### Calendar owner: Get properties of a shared or delegated calendar

The example in this section gets the properties of the primary calendar from the perspective of the owner, Alex.

Note the following properties on Alex' behalf:

- **canShare** is true as Alex is the owner.
- **canViewPrivateItems** is true since Alex is the owner.
- **isShared** is set to true, as Alex has set up a delegate for this calendar.
- **isSharedWithMe** is always false for the calendar owner.
- **owner** shows Alex as the owner.

**Microsoft Graph permissions**

Use the least privileged delegated or application permission, `Calendars.Read`, as appropriate, for this operation. For more information, see [calendar permissions](permissions-reference).

# [HTTP](#tab/http)
```msgraph
GET https://graph.microsoft.com/beta/users/AlexW@contoso.com/calendar
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Users["{user-id}"].Calendar.GetAsync();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v0.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-beta-sdk-go"  //other-imports
)

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
calendar, err := graphClient.Users().ByUserId("user-id").Calendar().Get(context.Background(), nil)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

Calendar result = graphClient.users().byUserId("{user-id}").calendar().get();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

let calendar = await client.api('/users/AlexW@contoso.com/calendar').version('beta').get();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\Beta\GraphServiceClient;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$result = $graphServiceClient->users()->byUserId('user-id')->calendar()->get()->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Beta.Calendar

Get-MgBetaUserDefaultCalendar -UserId $userId

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph_beta import GraphServiceClient
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python

result = await graph_client.users.by_user_id('user-id').calendar.get()

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

```http
HTTP/1.1 200 OK
Content-type: application/json

{
    "@odata.context": "https://graph.microsoft.com/beta/$metadata#users('64339082-ed84-4b0b-b4ab-004ae54f3747')/calendar/$entity",
    "id": "AQMkADAw7QAAAJfygAAAA==",
    "name": "Calendar",
    "color": "auto",
    "hexColor": "",
    "changeKey": "NEXywgsVrkeNsFsyVyRrtAAAAAACOg==",
    "canShare": true,
    "canViewPrivateItems": true,
    "isShared": true,
    "isSharedWithMe": false,
    "canEdit": true,
    "allowedOnlineMeetingProviders": [
        "teamsForBusiness"
    ],
    "defaultOnlineMeetingProvider": "teamsForBusiness",
    "isTallyingResponses": true,
    "isRemovable": false,
    "owner": {
        "name": "Alex Wilber",
        "address": "AlexW@contoso.com"
    }
}
```

### Share recipient or delegate: Get properties of shared or delegated calendar

The example in this section gets the properties of the same calendar from the perspective of the delegate, Megan.

Note the following properties:

- **name** of the calendar is by default the owner's display name. In this case, it's "Alex Wilber", since this is Alex' calendar delegated to Megan.
- **canShare** is false, since Megan isn't the owner of this calendar.
- **canViewPrivateItems** is true for the delegate Megan, as set up by Alex. For a sharee that isn't a delegate, this property is always false.
- **isShared** is false. This property indicates only to a calendar *owner* whether the calendar has been shared or delegated.
- **isSharedWithMe** property is true, since Megan is a delegate.
- **canEdit** is true, since delegates, including Megan, have write access.
- **owner** is set to Alex.

Note

A sharee or delegate can customize only the **name** property of a shared/delegated calendar. The update is visible only to themselves; the calendar owner does not see such calendar name changes.

**Microsoft Graph permissions**

Use the least privileged delegated permission, `Calendars.Read.Shared`, or application permission, `Calendars.Read`, as appropriate, for this operation. For more information, see [calendar permissions](permissions-reference).

# [HTTP](#tab/http)
```msgraph
GET https://graph.microsoft.com/beta/users/meganb@contoso.com/calendars/AAMkADlAABhbftjAAA=
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Users["{user-id}"].Calendars["{calendar-id}"].GetAsync();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v0.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-beta-sdk-go"  //other-imports
)

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
calendars, err := graphClient.Users().ByUserId("user-id").Calendars().ByCalendarId("calendar-id").Get(context.Background(), nil)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

Calendar result = graphClient.users().byUserId("{user-id}").calendars().byCalendarId("{calendar-id}").get();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

let calendar = await client.api('/users/meganb@contoso.com/calendars/AAMkADlAABhbftjAAA=').version('beta').get();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\Beta\GraphServiceClient;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$result = $graphServiceClient->users()->byUserId('user-id')->calendars()->byCalendarId('calendar-id')->get()->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Beta.Calendar

Get-MgBetaUserCalendar -UserId $userId -CalendarId $calendarId

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph_beta import GraphServiceClient
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python

result = await graph_client.users.by_user_id('user-id').calendars.by_calendar_id('calendar-id').get()

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

```http
HTTP/1.1 200 OK
Content-type: application/json

{
    "@odata.context": "https://graph.microsoft.com/beta/$metadata#users('meganb%40contoso.com')/calendars/$entity",
    "id": "AAMkADlAABhbftjAAA=",
    "name": "Alex Wilber",
    "color": "auto",
    "hexColor": "",
    "changeKey": "E6LznKWmX0KTsAD9qRJjeAAAYWo3EQ==",
    "canShare": false,
    "canViewPrivateItems": true,
    "isShared": false,
    "isSharedWithMe": true,
    "canEdit": true,
    "allowedOnlineMeetingProviders": [
        "teamsForBusiness"
    ],
    "defaultOnlineMeetingProvider": "teamsForBusiness",
    "isTallyingResponses": true,
    "isRemovable": true,
    "owner": {
        "name": "Alex Wilber",
        "address": "AlexW@contoso.com"
    }
}
```

## Get or set mailbox setting to receive meeting requests and responses

In this section:

- Get delegation delivery setting for a user's mailbox
- Set delegation delivery setting for a user's mailbox

Depending on the level of delegation a calendar owner prefers, the owner can specify who should receive meeting requests and responses to manage meetings on the calendar.

Programmatically, you can get or set the **delegateMeetingMessageDeliveryOptions** property of the calendar owner's [mailboxSettings](/en-us/graph/api/resources/mailboxsettings) to specify to whom Outlook should direct [eventMessageRequest](/en-us/graph/api/resources/eventmessagerequest) and [eventMessageResponse](/en-us/graph/api/resources/eventmessageresponse) instances:

- `sendToDelegateOnly`

    Outlook to direct **eventMessageRequest** and **eventMessageResponse** instances to only delegates. This is the default setting. The owner can see responses to a meeting or respond to an invitation through the corresponding **event** in the delegated calendar.
- `sendToDelegateAndInformationToPrincipal`

    Outlook to direct **eventMessageRequest** and **eventMessageResponse** instances to delegates and the calendar owner. Only the delegates see the option to accept or decline a meeting request, and the notification sent to the owner appears like a normal email message. The owner can still respond to the meeting by opening the **event** in the delegated calendar and responding.
- `sendToDelegateAndPrincipal`

    Outlook to direct **eventMessageRequest** and **eventMessageResponse** instances to delegates and the calendar owner, either of whom can respond to the meeting request.

This is a mailbox-wide setting, so the same setting applies to all delegates of the mailbox owner.

### Get delegation delivery setting for a user's mailbox

The example in this section gets the **mailboxSettings** of a calendar owner who lets Outlook direct meeting requests and responses to only calendar delegates; that is, **delegateMeetingMessageDeliveryOptions** is set to `sendToDelegateOnly`.

**Microsoft Graph permissions**

Use the least privileged delegated or application permission, `MailboxSettings.Read`, as appropriate, for this operation. For more information about mailbox permissions, see [mail permissions](permissions-reference).

# [HTTP](#tab/http)
```msgraph
GET https://graph.microsoft.com/beta/users/AlexW@contoso.com/mailboxsettings
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Users["{user-id}"].MailboxSettings.GetAsync();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v0.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-beta-sdk-go"  //other-imports
)

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
mailboxSettings, err := graphClient.Users().ByUserId("user-id").MailboxSettings().Get(context.Background(), nil)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

MailboxSettings result = graphClient.users().byUserId("{user-id}").mailboxSettings().get();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

let mailboxSettings = await client.api('/users/AlexW@contoso.com/mailboxsettings').version('beta').get();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\Beta\GraphServiceClient;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$result = $graphServiceClient->users()->byUserId('user-id')->mailboxSettings()->get()->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Beta.Users

Get-MgBetaUserMailboxSetting -UserId $userId

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph_beta import GraphServiceClient
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python

result = await graph_client.users.by_user_id('user-id').mailbox_settings.get()

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

```http
HTTP/1.1 200 OK
Content-type: application/json

{
    "@odata.context": "https://graph.microsoft.com/beta/$metadata#users('64339082-ed84-4b0b-b4ab-004ae54f3747')/mailboxSettings",
    "archiveFolder": "AQMkADAwAGVQAAAKfowAAAA==",
    "timeZone": "Pacific Standard Time",
    "delegateMeetingMessageDeliveryOptions": "sendToDelegateOnly",
    "dateFormat": "M/d/yyyy",
    "timeFormat": "h:mm tt",
    "automaticRepliesSetting": {
        "status": "disabled",
        "externalAudience": "all",
        "internalReplyMessage": "",
        "externalReplyMessage": "",
        "scheduledStartDateTime": {
            "dateTime": "2019-12-24T05:00:00.0000000",
            "timeZone": "UTC"
        },
        "scheduledEndDateTime": {
            "dateTime": "2019-12-25T05:00:00.0000000",
            "timeZone": "UTC"
        }
    },
    "language": {
        "locale": "en-US",
        "displayName": "English (United States)"
    },
    "workingHours": {
        "daysOfWeek": [
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday"
        ],
        "startTime": "08:00:00.0000000",
        "endTime": "17:00:00.0000000",
        "timeZone": {
            "name": "Pacific Standard Time"
        }
    }
}
```

### Set delegation delivery setting for a user's mailbox

The example in this section updates the **delegateMeetingMessageDeliveryOptions** property to `sendToDelegateAndPrincipal`, to have Outlook direct meeting requests and responses of the delegated calendar to all delegates and the owner.

**Microsoft Graph permissions**

Use the least privileged delegated or application permission, `MailboxSettings.ReadWrite`, as appropriate, for this operation. For more information about mailbox permissions, see [mail permissions](permissions-reference).

# [HTTP](#tab/http)
```http
PATCH https://graph.microsoft.com/beta/users/AlexW@contoso.com/mailboxsettings
Content-type: application/json

{
  "delegateMeetingMessageDeliveryOptions": "sendToDelegateAndPrincipal"
}
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// Dependencies
using Microsoft.Graph.Beta.Models;

var requestBody = new MailboxSettings
{DelegateMeetingMessageDeliveryOptions = DelegateMeetingMessageDeliveryOptions.SendToDelegateAndPrincipal,
};

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
var result = await graphClient.Users["{user-id}"].MailboxSettings.PatchAsync(requestBody);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v0.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-beta-sdk-go"  graphmodels "github.com/microsoftgraph/msgraph-beta-sdk-go/models"  //other-imports
)

requestBody := graphmodels.NewMailboxSettings()
delegateMeetingMessageDeliveryOptions := graphmodels.SENDTODELEGATEANDPRINCIPAL_DELEGATEMEETINGMESSAGEDELIVERYOPTIONS 
requestBody.SetDelegateMeetingMessageDeliveryOptions(&delegateMeetingMessageDeliveryOptions) 

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
mailboxSettings, err := graphClient.Users().ByUserId("user-id").MailboxSettings().Patch(context.Background(), requestBody, nil)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

MailboxSettings mailboxSettings = new MailboxSettings();
mailboxSettings.setDelegateMeetingMessageDeliveryOptions(DelegateMeetingMessageDeliveryOptions.SendToDelegateAndPrincipal);
MailboxSettings result = graphClient.users().byUserId("{user-id}").mailboxSettings().patch(mailboxSettings);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

const mailboxSettings = {
  delegateMeetingMessageDeliveryOptions: 'sendToDelegateAndPrincipal'
};

await client.api('/users/AlexW@contoso.com/mailboxsettings').version('beta').update(mailboxSettings);

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\Beta\GraphServiceClient;
use Microsoft\Graph\Beta\Generated\Models\MailboxSettings;
use Microsoft\Graph\Beta\Generated\Models\DelegateMeetingMessageDeliveryOptions;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$requestBody = new MailboxSettings();
$requestBody->setDelegateMeetingMessageDeliveryOptions(new DelegateMeetingMessageDeliveryOptions('sendToDelegateAndPrincipal'));

$result = $graphServiceClient->users()->byUserId('user-id')->mailboxSettings()->patch($requestBody)->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```powershell

Import-Module Microsoft.Graph.Beta.Users

$params = @{delegateMeetingMessageDeliveryOptions = "sendToDelegateAndPrincipal"
}

Update-MgBetaUserMailboxSetting -UserId $userId -BodyParameter $params

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph_beta import GraphServiceClient
from msgraph_beta.generated.models.mailbox_settings import MailboxSettings
from msgraph_beta.generated.models.delegate_meeting_message_delivery_options import DelegateMeetingMessageDeliveryOptions
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python
request_body = MailboxSettings(delegate_meeting_message_delivery_options = DelegateMeetingMessageDeliveryOptions.SendToDelegateAndPrincipal,
)

result = await graph_client.users.by_user_id('user-id').mailbox_settings.patch(request_body)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

```http
HTTP/1.1 200 OK
Content-type: application/json

{
    "@odata.context": "https://graph.microsoft.com/beta/$metadata#users('64339082-ed84-4b0b-b4ab-004ae54f3747')/mailboxSettings",
    "delegateMeetingMessageDeliveryOptions": "sendToDelegateAndPrincipal"
}
```

## Delete a sharee or delegate of a calendar

In the example below, Alex deletes Megan as a sharee of the "Kids parties" calendar.

**Microsoft Graph permissions**

Use the least privileged delegated or application permission, `Calendars.ReadWrite`, as appropriate, for this operation. For more information, see [calendar permissions](permissions-reference).

# [HTTP](#tab/http)
```http
DELETE https://graph.microsoft.com/beta/users/AlexW@contoso.com/calendars/AAMkADAwAABf02bAAAA=/calendarPermissions/L289RXhjaGFuZ2VMYWJTWVnYW5C
```

# [C#](#tab/csharp)
```csharp

// Code snippets are only available for the latest version. Current version is 5.x

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=csharp
await graphClient.Users["{user-id}"].Calendars["{calendar-id}"].CalendarPermissions["{calendarPermission-id}"].DeleteAsync();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Go](#tab/go)
```go

// Code snippets are only available for the latest major version. Current major version is $v0.*

// Dependencies
import (  "context"  msgraphsdk "github.com/microsoftgraph/msgraph-beta-sdk-go"  //other-imports
)

// To initialize your graphClient, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=go
graphClient.Users().ByUserId("user-id").Calendars().ByCalendarId("calendar-id").CalendarPermissions().ByCalendarPermissionId("calendarPermission-id").Delete(context.Background(), nil)

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Java](#tab/java)
```java

// Code snippets are only available for the latest version. Current version is 6.x

GraphServiceClient graphClient = new GraphServiceClient(requestAdapter);

graphClient.users().byUserId("{user-id}").calendars().byCalendarId("{calendar-id}").calendarPermissions().byCalendarPermissionId("{calendarPermission-id}").delete();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [JavaScript](#tab/javascript)
```javascript

const options = {authProvider,
};

const client = Client.init(options);

await client.api('/users/AlexW@contoso.com/calendars/AAMkADAwAABf02bAAAA=/calendarPermissions/L289RXhjaGFuZ2VMYWJTWVnYW5C').version('beta').delete();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PHP](#tab/php)
```php

<?php
use Microsoft\Graph\Beta\GraphServiceClient;

$graphServiceClient = new GraphServiceClient($tokenRequestContext, $scopes);

$graphServiceClient->users()->byUserId('user-id')->calendars()->byCalendarId('calendar-id')->calendarPermissions()->byCalendarPermissionId('calendarPermission-id')->delete()->wait();

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [PowerShell](#tab/powershell)
```
Snippet not available
```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

# [Python](#tab/python)
```python

# Code snippets are only available for the latest version. Current version is 1.x
from msgraph_beta import GraphServiceClient
# To initialize your graph_client, see https://learn.microsoft.com/en-us/graph/sdks/create-client?from=snippets&tabs=python

await graph_client.users.by_user_id('user-id').calendars.by_calendar_id('calendar-id').calendar_permissions.by_calendar_permission_id('calendarPermission-id').delete()

```

> 
> Read the [SDK documentation](/en-us/graph/sdks/sdks-overview) for details on how to [add the SDK](/en-us/graph/sdks/sdk-installation) to your project and [create an authProvider](/en-us/graph/sdks/choose-authentication-providers) instance.

---

```http
HTTP/1.1 204 No Content
```
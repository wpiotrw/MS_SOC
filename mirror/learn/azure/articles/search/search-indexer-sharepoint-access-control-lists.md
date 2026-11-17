---
layout: Conceptual
title: Use a SharePoint Indexer to Ingest Permission Metadata - Foundry IQ (Azure AI Search) | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/azure/search/search-indexer-sharepoint-access-control-lists
breadcrumb_path: ../breadcrumb/azure-ai/toc.json
feedback_help_link_url: https://learn.microsoft.com/en-us/answers/tags/109/azure-cognitive-search
feedback_help_link_type: get-help-at-qna
feedback_product_url: https://feedback.azure.com/d365community/forum/9325d19e-0225-ec11-b6e6-000d3a4f07b8
feedback_system: Standard
permissioned-type: public
recommendations: true
recommendation_types:
- Training
- Certification
uhfHeaderId: azure-ai-foundry
ms.suite: office
author: haileytap
learn_banner_products:
- azure
manager: mcleans
ms.author: haileytapia
ms.collection: ce-skilling-ai-copilot
ms.update-cycle: 90-days
description: Learn how to configure Foundry IQ (Azure AI Search) indexers for ingesting Access Control Lists (ACLs) from SharePoint in Microsoft 365 files.
ms.reviewer: gimondra
ms.service: azure-ai-search
ms.topic: how-to
ms.date: 2026-11-09T00:00:00.0000000Z
ai-usage: ai-assisted
ms.custom: doc-kit-assisted
locale: en-us
document_id: f9de8949-9879-59bf-1266-4b63986fc0b5
document_version_independent_id: 65581542-b78b-ea50-8aff-c2ccf4411dd6
original_content_git_url: https://github.com/MicrosoftDocs/azure-ai-docs-pr/blob/live/articles/search/search-indexer-sharepoint-access-control-lists.md
site_name: Docs
depot_name: Learn.azure-ai
page_type: conceptual
toc_rel: toc.json
asset_id: search/search-indexer-sharepoint-access-control-lists
moniker_range_name: 
monikers: []
item_type: Content
source_path: articles/search/search-indexer-sharepoint-access-control-lists.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/9d7be3ef-f27c-4c7f-9eba-67c3cd429995
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/57eae307-c3a1-4cac-b645-1a899934bac8
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/feeb50f3-b677-44f9-b3a6-5f2f58182b0d
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ee561821-1ac7-45a8-9409-6ba5eb7a5b97
platformId: b627f995-400c-06b1-480e-3bcd9f1cebb2
---

# Use a SharePoint Indexer to Ingest Permission Metadata - Foundry IQ (Azure AI Search) | Microsoft Learn

Note

[Foundry IQ (Azure AI Search)](/en-us/azure/foundry/agents/concepts/what-is-foundry-iq) provides direct indexing and query APIs alongside higher-level knowledge source and knowledge base APIs for managed retrieval. Use the [Azure portal](https://portal.azure.com), [REST APIs](/en-us/azure/search/search-api-versions#rest-apis), or [Azure SDKs](/en-us/azure/search/search-api-versions#all-azure-sdks) to configure these capabilities, or connect agents to knowledge bases in the [Microsoft Foundry portal](https://ai.azure.com/?cid=learnDocs).

SharePoint permission metadata ingestion uses a Foundry IQ (Azure AI Search) indexer to store supported access control lists (ACLs) alongside indexed SharePoint content. Query-time permission filters evaluate this indexed metadata and the querying user's identity. Source permission changes reach the index through permission synchronization, not through queries.

[![Diagram showing SharePoint content and ACL ingestion into Foundry IQ, followed by permission-filtered retrieval.](media/search-indexer-sharepoint-access-control-lists/security-trimmed-rag-sharepoint.png)](media/search-indexer-sharepoint-access-control-lists/security-trimmed-rag-sharepoint.png#lightbox)

Important

Indexed permission filtering isn't a live evaluation of the complete SharePoint access and policy model. For source-side request-time retrieval and customer-managed ingestion alternatives, see Choose a retrieval approach for freshness.

## Prerequisites

- [Foundry IQ](search-create-service-portal) on a billable tier (Basic or higher) in any region.
- SharePoint in Microsoft 365 sites, libraries, folders, and files with configured permissions.
- Complete all configuration steps in the [SharePoint indexer documentation](search-how-to-index-sharepoint-online), applying the ACL-specific requirements described in this article.
- Configure Microsoft Entra application permissions and a credential appropriate for your scenario. See Permissions by ACL scenario. ACL ingestion requires application permissions. Delegated permissions aren't supported. For the application vs delegated decision, see [Choose your permissions setup](search-how-to-index-sharepoint-online#choose-your-permissions-setup).
- The [2026-10-01 data plane REST API](/en-us/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-10-01&amp;preserve-view=true) for the generally available SharePoint permission configuration in this article.

Note

[Permissions resync](search-howto-run-reset-indexers#resync-indexers) is generally available with REST API `2026-10-01`. [Reset-docs](search-howto-run-reset-indexers#how-to-reset-docs-preview) remains in preview and uses REST API `2026-11-01-preview`.

## Limitations

- Use standard or default document parsing (`parameters.configuration.parsingMode: "default"`) or Content Understanding-based extraction where supported. Every generated chunk must retain the required permission metadata and source context. The system doesn't support specialized customer-selected parsing modes. For excluded modes and knowledge-source settings, see [Supported parsing and content extraction for permission ingestion](search-document-level-access-overview#supported-parsing-and-content-extraction-for-permission-ingestion).
- Tenants with Microsoft Entra Conditional Access enabled aren't supported. The [SharePoint indexer's limitations](search-how-to-index-sharepoint-online#limitations-and-considerations) also apply to ACL ingestion.
- Permission updates depend on source change notifications and successful indexer processing. Supported non-root document-library folder changes can refresh unchanged descendants during ordinary incremental processing. See Synchronize permissions between indexed and source content for the scope and refresh options.
- The Azure portal doesn't support this feature.
- The following features aren't supported:

    - [SharePoint Information Management policies](/en-us/sharepoint/intro-to-info-mgmt-policies) applicable to user access. The system doesn't evaluate, ingest, or honor these policies at query time.
    - [Shareable links](/en-us/sharepoint/shareable-links-anyone-specific-people-organization) scoped to "Anyone" or "People in your organization," and sharing-link expiration enforcement. Use supported explicit user or group assignments, including supported inherited assignments. Expiration of a sharing link doesn't revoke a separate explicit grant.
- Nested group membership supports up to five levels. A separate site-level limit applies when more than 10,000 applicable Microsoft Entra group principals require nested resolution. See Supported group relationships.
- The following features aren't supported with SharePoint ACL ingestion:

    - [Custom Web API skill](cognitive-search-custom-skill-web-api)
    - [Knowledge store](knowledge-store-concept-intro), including the asset store required for [image serving (preview)](agentic-retrieval-how-to-image-serving) in agentic retrieval. Therefore, image serving isn't supported for knowledge sources that ingest SharePoint ACLs.
    - [Indexer enrichment cache](enrichment-cache-how-to-configure)
    - [Debug sessions](cognitive-search-debug-session)
- Chat Completion enrichment has [endpoint and permission restrictions](cognitive-search-skill-genai-prompt#restrictions-with-sharepoint-permissions) when SharePoint ACL ingestion is enabled.

## Support for the SharePoint permission model

Permission ingestion supports the following subset of the SharePoint permission model for documents, list items, and modern ASPX site pages.

| SharePoint feature | Description | Supported | Notes |
| --- | --- | --- | --- |
| Site, library, list, and page inheritance | Site → library/list → folder → file/item/page. | ✔️ | Evaluated at ingestion; effective ACLs computed per item. |
| Folder, file, list item, and page unique ACLs | Item-level access. | ✔️ | Included when present at first ingestion and on subsequent runs that detect ACL changes for items with unique permissions. |
| SharePoint list items | Permissions on list items (`allSiteLists` and `allSiteContent` containers). | ✔️ | Requires the permissions listed in Permissions by ACL scenario. |
| ASPX site pages | Permissions on modern site pages (`allSitePages` and `allSiteContent` containers). | ✔️ | Requires the permissions listed in Permissions by ACL scenario. |
| Microsoft Entra (Microsoft 365 and security) groups | Group-based access. | ✔️ | Group IDs included when resolvable to a Microsoft Entra identifier (ID). |
| SharePoint site groups | Owners/Members/Visitors and custom site groups. | ✔️ | Requires the SharePoint groups configuration. Group IDs are emitted with the `spg:` prefix. |
| Shareable "Anyone links" or "People in your organization links" | Org-wide or public access. | ❌ | Use supported explicit user/group assignments instead. |
| **Sharing-link expiration enforcement** | Access changes based on a link's expiration. | ❌ | Permissions resync doesn't enable this unsupported capability. |
| External/guest users | Access for guests. | ❌ | Not supported. |
| Information Management policies | Policies to define specific permissions requirements. | ❌ | Not supported. |
| Purview sensitivity labels | Document-level security for privacy, categorization, permissions, and encryption | ❌ | Supported via a separate feature: [preserving and honoring sensitivity labels](search-indexer-sensitivity-labels). |

### Supported group relationships

Supported group resolution includes Microsoft Entra groups nested within SharePoint site groups, up to five nested group levels.

| Permission relationship | Supported | Guidance |
| --- | --- | --- |
| **User or Microsoft Entra group assigned directly to the SharePoint item** | Yes | The indexer stores the user or Microsoft Entra group object ID in the item's permission metadata. |
| **User reaches an assigned Microsoft Entra group through nested Microsoft Entra groups** | Yes, within five levels | Membership beyond the supported depth doesn't grant access through that path. |
| **User assigned directly to a SharePoint site group that has access to the item** | Yes | Configure SharePoint groups support. |
| **Microsoft Entra group nested within a SharePoint group** | Yes, within five levels | Configure SharePoint groups support. The site-level principal limit below also applies. |
| **Membership path requiring more than five nested group levels** | No | If this is the user's only permission path, access is denied. A separate supported direct or within-limit grant can still grant access. |

For example, consider a SharePoint group that has access to an item. Entra group G1 is a member of that SharePoint group; G2 is a member of G1, continuing through G6. A user who is a direct member of G1, G2, G3, G4, or G5 can receive access through the corresponding one-to-five-level path. Membership only in G6 doesn't grant access through this chain. A separate direct assignment to the user is evaluated independently.

If a site has more than 10,000 applicable Microsoft Entra group principals for nested resolution, those nested memberships aren't resolved. Separate supported grants, such as direct user assignments or direct SharePoint group membership, can still apply. This threshold counts applicable Entra site principals, not the user's groups, SharePoint groups, indexed sites, or nesting depth. Exactly 10,000 isn't excluded by this threshold alone. For missing results, see [Troubleshoot SharePoint permission filtering](troubleshoot-sharepoint-query-permission-filtering).

## How hierarchical permissions are evaluated

SharePoint permissions follow the site → library or list → folder → file, item, or page hierarchy, unless inheritance is broken.

During ingestion, the indexer gathers user and group identifiers and computes the effective ACL for each item.

## Permissions by ACL scenario

The Microsoft Entra application permissions and credential type required for ACL ingestion depend on which item types and group types you index. In the app registration, all permissions are added under **API permissions** &gt; **Add a permission**, and the federated credential is added under **Certificates & secrets** &gt; **Federated credentials**. For step-by-step instructions and screenshots, see [Step 3: Create a Microsoft Entra application registration](search-how-to-index-sharepoint-online#step-3-create-a-microsoft-entra-application-registration) and [Configuring the registered application with a managed identity](search-how-to-index-sharepoint-online#configuring-the-registered-application-with-a-managed-identity).

| Scenario | API permissions to add | Credential |
| --- | --- | --- |
| ACLs on document library files, when access is granted only through Microsoft Entra users and standard groups (Microsoft Entra security groups, Microsoft 365 groups, mail-enabled security groups) | **Microsoft Graph**: `Files.Read.All`, `Sites.FullControl.All` (or `Sites.Selected` for scoped access) | Client secret or federated credential |
| ACLs on document library files, when SharePoint site groups (Owners, Members, Visitors, or custom site groups) must also be honored | **Microsoft Graph**: `Files.Read.All`, `Sites.FullControl.All` (or `Sites.Selected`)**SharePoint**: `Sites.FullControl.All` (or `Sites.Selected`) | Federated credential (required) |
| ACLs on SharePoint list items | **Microsoft Graph**: `Files.Read.All`, `Sites.FullControl.All` (or `Sites.Selected`), `User.Read.All`**SharePoint**: `Sites.FullControl.All` (or `Sites.Selected`) | Federated credential (required) |
| Content and ACLs on ASPX site pages | **Microsoft Graph**: `Sites.FullControl.All` (or `Sites.Selected`), `User.Read.All` (keep `Files.Read.All` from the rows above if you're also indexing document libraries or lists)**SharePoint**: `Sites.FullControl.All` (or `Sites.Selected`) | Federated credential (required) |
| Query-time resolution of SharePoint site groups via `sharePointConnectorAppRegistration` | Add **SharePoint**: `User.Read.All` to the same app registration used by the indexer | Federated credential (required) |

Note

- When you add a permission, you choose between two API surfaces: **Microsoft Graph** and **SharePoint**. Both expose similarly named permissions. For example, `Sites.FullControl.All` exists under both. Add each permission under the API surface indicated in the table.
- Use a federated credential whenever the scenario adds SharePoint API permissions. Client secrets work only for the Microsoft Graph–only document-library row.
- `User.Read.All` is required for list items and ASPX site pages because the indexer reads those permissions through the SharePoint REST API, which returns only the user's email. The indexer then calls Microsoft Graph to resolve each email to its Microsoft Entra object ID, and that lookup requires `User.Read.All`.
- When you use `Sites.Selected`, grant the app explicit access to each target SharePoint site before indexing.

A federated credential authenticates the app using a trusted managed identity instead of a client secret. The same federated credential covers both ingestion (indexer) and query-time evaluation of SharePoint site groups. For setup steps, see [Configuring the registered application with a managed identity](search-how-to-index-sharepoint-online#configuring-the-registered-application-with-a-managed-identity).

### Before you enable ACL ingestion

Complete these steps on your registered Microsoft Entra application:

1. Identify your scenario in the previous table based on what you plan to index (document library files, list items, ASPX site pages) and whether SharePoint site groups must be honored.
2. Open your app registration in the Microsoft Entra admin center and go to **API permissions** &gt; **Add a permission**.
3. Add the Microsoft Graph permissions listed for your scenario. Grant admin consent.
4. If your scenario also requires SharePoint permissions, select **Add a permission** again, choose the **SharePoint** API, and add `Sites.FullControl.All` (or `Sites.Selected`). Grant admin consent.
5. Configure the credential:
    - For Microsoft Graph–only scenarios, you can use either a client secret (**Certificates & secrets** &gt; **Client secrets**) or a federated credential.
    - For any scenario that includes SharePoint permissions, add a federated credential under **Certificates & secrets** &gt; **Federated credentials**. See [Configuring the registered application with a managed identity](search-how-to-index-sharepoint-online#configuring-the-registered-application-with-a-managed-identity).
6. Grant the application access to the target SharePoint sites (especially important when you use `Sites.Selected` for scoped access) so it can read the content and permissions you want to index.

## Find the correct Microsoft Entra identifiers

Each identifier appears in a different location in the Azure portal and maps to a specific configuration field. Use this section as a reference when configuring SharePoint ACL ingestion with a federated credential. These identifiers are referenced in Configure SharePoint groups support and in the data source connection string.

| Identifier | Portal location | Used where | Notes |
| --- | --- | --- | --- |
| Ingestion app application (client) ID | **App registrations** &gt; `<your-app>` &gt; **Overview** | `ApplicationId` in the data source connection string; `applicationId` in `sharePointConnectorAppRegistration` | This ID is correct for most configuration fields. Also called "client ID." |
| Application object ID | **App registrations** &gt; `<your-app>` &gt; **Overview** (below Application (client) ID) | Not used in Foundry IQ configuration | Don't confuse this with the Application (client) ID. It appears in the same blade, directly below the client ID. |
| Service principal object ID | **Microsoft Entra ID** &gt; **Enterprise applications** &gt; `<your-app>` &gt; **Manage** &gt; **Properties** | Not used in Foundry IQ configuration | This is the service principal representation of the app. It's a different GUID from the app registration object ID. |
| Managed identity principal ID | Managed identity resource &gt; **Properties** or the Foundry IQ service **Identity** blade | Not used directly in Foundry IQ data source or index configuration | Used internally when you set up the federated identity credential on the app registration. The credential you create trusts this identity. |
| Federated credential object ID | **App registrations** &gt; `<your-app>` &gt; **Manage** &gt; **Certificates & secrets** &gt; **Federated credentials** &gt; `<credential-name>` | Not used in Foundry IQ configuration | Don't use the GUID of the federated identity credential entry for `federatedCredentialId`. |
| Federated credential application ID | System-assigned: **Microsoft Entra ID** &gt; **Enterprise applications** &gt; `<search-service>` &gt; **Properties**; User-assigned: `<managed-identity-resource>` &gt; **Properties** | `FederatedCredentialApplicationId` in the data source connection string; `federatedCredentialId` in `sharePointConnectorAppRegistration` | See Federated credential application ID for the managed identity lookup. |

### Federated credential application ID

For `FederatedCredentialApplicationId` in the data source connection string and `federatedCredentialId` in the index definition, use the managed identity's own application (client) ID, not the ingestion app's ID.

**System-assigned managed identity:**

1. Go to your Foundry IQ service.
2. Select **Security + networking** &gt; **Identity**.
3. On the **System assigned** tab, note the **Object (principal) ID**.
4. Go to **Microsoft Entra ID** &gt; **Manage** &gt; **Enterprise applications**.
5. Search for your Foundry IQ service name or paste the **Object (principal) ID** into the search box.
6. Select the result and open **Properties**. Copy the **Application ID** shown here, which is the value for `FederatedCredentialApplicationId` in the data source and `federatedCredentialId` in the index.

**User-assigned managed identity:**

1. Go to the user-assigned managed identity resource.
2. Select **Settings** &gt; **Properties**.
3. Copy the **Client ID**, which is the value for `FederatedCredentialApplicationId` in the data source and `federatedCredentialId` in the index.

## Configure your Foundry IQ service for ACL ingestion and query-time enforcement

These steps configure your Foundry IQ service for ACL ingestion and enable ACL honoring at query time.

### Choose where to populate ACL fields

Where you map the ACL metadata fields depends on whether the indexer writes one document per source item or multiple chunks per source item.

| Scenario | Populate ACL fields via | Why |
| --- | --- | --- |
| No skillset or skillset without chunking; one search document per source item | **Indexer field mappings** only (`metadata_user_ids` → `UserIds`, `metadata_group_ids` → `GroupIds`, and for SharePoint groups `metadata_spo_site_url` → `SharePointSiteUrl`). | The indexer writes a single document to the target index, and field mappings carry source metadata to index fields. |
| Skillset with chunking (for example, Text Split skill for integrated vectorization), single index with parent fields repeated on each chunk (`projectionMode: skipIndexingParentDocuments`) | **Index projections** in the skillset (`mappings` from `/document/metadata_user_ids`, `/document/metadata_group_ids`, and for SharePoint groups `/document/metadata_spo_site_url`). | The parent document isn't indexed; only chunks are. ACL values must be projected onto every chunk so query-time filters apply on the chunk returned in results. Indexer field mappings for these fields are bypassed in this mode. |
| Skillset with chunking, two-index pattern (parent index + child chunk index) | **Both**: indexer field mappings populate ACL fields on the parent index, index projections populate ACL fields on the child chunk index. | Both indexes are queryable, and each needs the metadata it filters on. |

In all chunked scenarios, every chunk must carry the ACL fields. Permission filters apply per document, so a chunk missing ACL fields can't be returned to the right caller.

### 1. Data source configuration

Add `indexerPermissionOptions` to the [base data source configuration](search-how-to-index-sharepoint-online#step-4-create-data-source) to ingest `userIds` and `groupIds`. This example selects the site's default document library. Use the connector's container and query settings for other selections.

```json
{
  "name": "my-sharepoint-acl-datasource",
  "type": "sharepoint",
  "indexerPermissionOptions": ["userIds", "groupIds"],
  "credentials": {
    "connectionString": "<connection-string>;"
  },
  "container": {
    "name": "defaultSiteLibrary",
    "query": null
  }
}
```

### 2. Add permission fields to the index definition

Merge the following fields and properties into your [index schema definition](search-how-to-index-sharepoint-online#step-5-create-an-index). This fragment omits the required document key and your content fields; retain them in the complete definition.

Keep SharePoint authorization metadata separate from index-key identity. The following SharePoint-specific requirements extend the connector's [source metadata](search-how-to-index-sharepoint-online#metadata) and [key mapping and encoding instructions](search-how-to-index-sharepoint-online#step-6-create-an-indexer).

| Source field | Purpose | Target and mapping |
| --- | --- | --- |
| **`metadata_spo_item_path`** | Source path for ACL lookup and permission-only updates. | Required `Edm.String` field named `metadata_spo_item_path`. Use implicit same-name mapping for whole documents and `/document/metadata_spo_item_path` in each chunk projection. |
| **`metadata_user_ids`** | Supported user assignments. | Map to a `Collection(Edm.String)` field with `permissionFilter: "userIds"`, such as `UserIds`. Project `/document/metadata_user_ids` onto chunks. |
| **`metadata_group_ids`** | Supported Microsoft Entra and configured SharePoint site-group assignments. | Map to a `Collection(Edm.String)` field with `permissionFilter: "groupIds"`, such as `GroupIds`. Project `/document/metadata_group_ids` onto chunks. |
| **`metadata_spo_site_url`** | Originating site for native SharePoint group resolution. | Map to an `Edm.String` field with `sharepointSiteUrl: true`, such as `SharePointSiteUrl`. Project `/document/metadata_spo_site_url` onto chunks; retain each item's site for cross-site selections. |
| **`metadata_spo_site_library_item_id`** | Library-item identity for library or folder selections. | Map to the whole-document or parent index key using the connector's key encoding instructions. Projections generate child keys and parent identity. |
| **`metadata_spo_site_asset_item_id`** | Asset/item identity for list, page, or mixed-content selections. | Use instead of the library-item key for `allSiteLists`, `allSitePages`, and `allSiteContent`. Follow the same key encoding instructions; don't map projection-generated keys or parent identity. |

```json
{
  "fields": [
    { "name": "metadata_spo_item_path", "type": "Edm.String", "retrievable": false },
    { "name": "UserIds",  "type": "Collection(Edm.String)", "permissionFilter": "userIds",  "filterable": true, "retrievable": false },
    { "name": "GroupIds", "type": "Collection(Edm.String)", "permissionFilter": "groupIds", "filterable": true, "retrievable": false }
  ],
  "permissionFilterOption": "enabled"
}
```

Set `retrievable` to `true` only during development to verify values. Changing `retrievable` doesn't require an index rebuild.

### 3. Configure index projections in your skillset (if applicable)

When chunking is enabled, the parent document isn't written to the index when `projectionMode` is `skipIndexingParentDocuments`. Carry the ACL metadata onto each chunk through `indexProjections.selectors[].mappings`.

If your indexer uses a [skillset](cognitive-search-working-with-skillsets) with data chunking, such as the [Text Split skill](cognitive-search-skill-textsplit) when enabling [integrated vectorization](vector-search-integrated-vectorization), map the permission fields and required source path to each chunk using index projections. For the skillset schema, see the [2026-10-01 data plane REST API reference](/en-us/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-10-01&amp;preserve-view=true).

This example shows the skillset configuration for a target chunk index with the permission fields from the previous step. The target also needs a `content` field, a document key, and a filterable `parentId` string field, as described in [Define index projections](search-how-to-define-index-projections). Projections generate the document key and parent ID; don't map these fields yourself. Include `SharePointSiteUrl` only when you configure SharePoint groups support.

The `//` comment in the following example is illustrative and isn't valid JSON. Remove it before submitting the request.

```http
PUT https://{service}.search.windows.net/skillsets/{skillset}?api-version=2026-10-01
{
  "name": "my-skillset",
  "skills": [
    {
      "@odata.type": "#Microsoft.Skills.Text.SplitSkill",
      "name": "#split",
      "context": "/document",
      "inputs": [{ "name": "text", "source": "/document/content" }],
      "outputs": [{ "name": "textItems", "targetName": "chunks" }]
    }
    // ... (other skills such as embeddings, entity recognition, etc.)
  ],
  "indexProjections": {
    "selectors": [
      {
        "targetIndexName": "chunks-index",
        "parentKeyFieldName": "parentId",
        "sourceContext": "/document/chunks/*",
        "mappings": [
          { "name": "content", "source": "/document/chunks/*" },
          { "name": "metadata_spo_item_path", "source": "/document/metadata_spo_item_path" },
          { "name": "UserIds",  "source": "/document/metadata_user_ids" },
          { "name": "GroupIds",  "source": "/document/metadata_group_ids" },
          { "name": "SharePointSiteUrl", "source": "/document/metadata_spo_site_url" }
        ]
      }
    ],
    "parameters": {
      "projectionMode": "skipIndexingParentDocuments"
    }
  }
}

```

The `UserIds`, `GroupIds`, and `SharePointSiteUrl` mappings read source-level metadata emitted by the SharePoint indexer (`/document/metadata_*`) and write the values onto each chunk.

### 4. Configure the indexer field mappings for ACLs

Use indexer field mappings when the indexer writes one document per source item (no chunking) or when you maintain a separate parent index alongside a chunk index. For a chunk-only index with `projectionMode: skipIndexingParentDocuments`, retain the projection mappings from the previous step. You don't need any additional indexer `fieldMappings` to populate those chunk fields.

Besides your required [indexer configuration](search-how-to-index-sharepoint-online#step-6-create-an-indexer), map raw metadata ACL fields from SharePoint to your index fields.

For one document per source item, the same-named `metadata_spo_item_path` source and index fields use implicit field mapping. For chunks, use the direct projection mapping in the previous step.

Apply these permission-enabled configuration deltas to the [base connector's indexer configuration](search-how-to-index-sharepoint-online#step-6-create-an-indexer):

- **Library or folder selections:** Retain the `metadata_spo_site_library_item_id` key mapping and its `base64Encode` mapping function.
- **List or page selections:** For `allSiteLists` or `allSitePages`, replace the key mapping source with `metadata_spo_site_asset_item_id`, retaining the encoding function. Keep the content configuration described in [Index SharePoint lists](search-how-to-index-sharepoint-online#index-sharepoint-lists) or [Index ASPX site pages](search-how-to-index-sharepoint-online#index-aspx-site-pages).
- **Mixed selections:** For `allSiteContent`, use `metadata_spo_site_asset_item_id` as the key mapping source across the selection, with the same encoding function.

For each selection, enable `userIds` and `groupIds` on the data source, retain the required path field, and add the following ACL mappings. Add the site URL mapping when using native SharePoint groups. For chunk-only indexes, use the five projection mappings in the previous step instead of manually mapping generated keys or parent identity.

```json
{
  "fieldMappings": [
    { "sourceFieldName": "metadata_user_ids",  "targetFieldName": "UserIds" },
    { "sourceFieldName": "metadata_group_ids", "targetFieldName": "GroupIds" }
  ]
}
```

### 5. Run the indexer

The indexer ingests ACL metadata when it runs. After you create or update the indexer, [run the indexer and monitor its status](search-howto-run-reset-indexers#run-without-reset) to ingest ACLs alongside content.

For recurring permission refresh and existing-index backfill, see Refresh indexed permissions. Backfill steps depend on whether existing records already contain `metadata_spo_item_path`.

### 6. Verify ACL ingestion

To confirm ACL values populated correctly:

1. Temporarily set `retrievable` to `true` on `UserIds` and `GroupIds` in your index definition. Changing `retrievable` doesn't require an index rebuild.
2. Run an [elevated-read query](search-query-access-control-rbac-enforcement#elevated-permissions-for-investigating-incorrect-results) that selects `UserIds` and `GroupIds`. Compare the values with the item's supported source assignments. One collection can be empty when access is granted through the other. For chunked scenarios, verify the expected assignments on every chunk.
3. Return `retrievable` to `false` after verification.

Compare permitted and denied test-user results by using [query troubleshooting checks](troubleshoot-sharepoint-query-permission-filtering#8-compare-expected-and-actual-results). Populated ACL fields alone don't validate query-time enforcement.

## Configure SharePoint groups support

The SharePoint indexer can ingest SharePoint site group permissions (Owners, Members, Visitors, and custom site groups) for query-time filtering. The indexer emits SharePoint group IDs in the `metadata_group_ids` field with the `spg:` prefix to distinguish them from Microsoft Entra group object IDs.

After configuring ACL ingestion, use these steps to add SharePoint site group resolution to your index and query configuration.

The following components work together to enable SharePoint site group resolution:

| Component | Where | Purpose |
| --- | --- | --- |
| `sharePointConnectorAppRegistration` (with `applicationId`, `tenantId`, `federatedCredentialId`) | Index definition | Provides the authentication configuration required for the Foundry IQ service to call the SharePoint REST API as the calling user and resolve site group membership at query time. |
| `SharePointSiteUrl` field (with `sharepointSiteUrl: true`) | Index schema + indexer field mapping from `metadata_spo_site_url` | Identifies which SharePoint site a document belongs to, so SP group resolution is scoped correctly. |
| `spg:`-prefixed values in `GroupIds` | Document permission metadata | Distinguish SharePoint site group IDs from Microsoft Entra group object IDs. |

For cross-site source selections, `metadata_spo_site_url` identifies each item's originating site, not a fixed site for the entire index. Retain that value on each document or chunk and grant the configured application the required access to each selected site. See Permissions by ACL scenario and Choose where to populate ACL fields.

An index with a field marked `sharepointSiteUrl: true` supports at most five distinct site-URL values. Check the [SharePoint group permission site limits](search-limits-quotas-capacity#sharepoint-group-permission-site-limits) before selecting sites. For larger scopes, evaluate [separate indexes and knowledge sources](agentic-knowledge-source-how-to-sharepoint-indexed#plan-topology-for-sharepoint-group-permissions), including knowledge-base capacity and application routing.

### 1. Prerequisites

- SharePoint indexer already configured for ACL ingestion. See Configure the indexer field mappings for ACLs.
- Microsoft Entra app registration with a federated identity credential. See [Configuring the registered application with a managed identity](search-how-to-index-sharepoint-online#configuring-the-registered-application-with-a-managed-identity).
- REST API `2026-10-01`.

Note

`FederatedCredentialApplicationId` in the data source connection string and `federatedCredentialId` in `sharePointConnectorAppRegistration` use the managed identity's application ID. The `applicationId` property in `sharePointConnectorAppRegistration` uses the ingestion app's client ID. To find the correct values, see Find the correct Microsoft Entra identifiers.

### 2. Configure the index

Merge the following configuration into your complete index definition, retaining its document key and content fields. It adds `sharePointConnectorAppRegistration` and `SharePointSiteUrl` alongside the ACL fields. Keep `permissionFilterOption: "enabled"`.

```json
{
  "name": "my-sharepoint-acl-index",
  "sharePointConnectorAppRegistration": {
      "applicationId": "<ingestion-app-client-id>",
      "federatedCredentialId": "<managed-identity-application-id>",
      "tenantId": "<sharepoint-tenant-id>"
  },
  "fields": [
    { "name": "metadata_spo_item_path", "type": "Edm.String", "retrievable": false },
    { "name": "UserIds",           "type": "Collection(Edm.String)", "permissionFilter": "userIds",  "filterable": true, "retrievable": false },
    { "name": "GroupIds",          "type": "Collection(Edm.String)", "permissionFilter": "groupIds", "filterable": true, "retrievable": false },
    { "name": "SharePointSiteUrl", "type": "Edm.String", "sharepointSiteUrl": true, "filterable": false, "retrievable": false }
  ],
  "permissionFilterOption": "enabled"
}
```

### 3. Configure the indexer field mappings

Map the SharePoint metadata fields to the index fields in a single combined mapping block. The first two mappings are the same ones used for standard ACL ingestion; the third mapping activates SharePoint groups resolution.

```json
{
  "fieldMappings": [
    { "sourceFieldName": "metadata_user_ids",             "targetFieldName": "UserIds" },
    { "sourceFieldName": "metadata_group_ids",            "targetFieldName": "GroupIds" },
    { "sourceFieldName": "metadata_spo_site_url",  "targetFieldName": "SharePointSiteUrl" }
  ]
}
```

If your skillset chunks documents (for example, with the Text Split skill for integrated vectorization), project `SharePointSiteUrl` onto each chunk through `indexProjections.selectors[].mappings` instead. See Choose where to populate ACL fields.

### 4. Query the index

No client-side change is required. The same `x-ms-query-source-authorization` token activates both Microsoft Entra and SharePoint site group enforcement. The Foundry IQ service resolves SharePoint group memberships server-side using `sharePointConnectorAppRegistration` on the index.

For the request shape, see the [general query example](search-query-access-control-rbac-enforcement#query-example) and the SharePoint-specific [example with SharePoint site group enforcement](search-query-access-control-rbac-enforcement#example-query-with-sharepoint-site-group-enforcement).

### 5. Verify

To confirm SharePoint group IDs are in the index, run an [elevated-read query](search-query-access-control-rbac-enforcement#elevated-permissions-for-investigating-incorrect-results) that selects `GroupIds` and look for `spg:`-prefixed values in the response.

## Synchronize permissions between indexed and source content

Content and permission metadata replicate into Search through separate processing stages. Choose a retrieval approach based on where authorization occurs and how your application manages updates.

### Choose a retrieval approach for freshness

Prefer remote SharePoint when your application needs request-time retrieval using SharePoint's permissions model rather than a replicated permission subset in Search. This approach provides freshness closer to SharePoint through Microsoft 365 governance controls, without an additional Search synchronization pipeline. Choose indexed retrieval for a custom Search index, or Push for application-controlled submission.

| Decision | Remote SharePoint | Indexed SharePoint | Customer-managed Push API |
| --- | --- | --- | --- |
| **Authorization authority** | Microsoft 365 retrieval on behalf of the user, using SharePoint's permissions model and Microsoft 365 governance controls. | Query-time filtering over a replicated subset of SharePoint permissions. | Query-time filtering over permission values your application supplies; no automatic SharePoint ACL synchronization or native-group resolution. |
| **Content and permission freshness** | No additional Search index synchronization; depends on Microsoft 365 processing and [remote-source limitations](agentic-knowledge-source-how-to-sharepoint-remote#limitations-and-considerations). | Source notifications and successful indexer processing update the replica. Schedules don't establish a strict freshness window. | Your application controls submission timing, not immediate query visibility. |
| **Revocation** | Subject to Microsoft 365 processing; not a zero-delay commitment. | Stale indexed grants can persist until the relevant update is processed. | Your application detects revoked grants, updates affected records and chunks, and verifies results. |
| **Identity responsibilities** | Supply the delegated user identity required by the [remote source](agentic-knowledge-source-how-to-sharepoint-remote#prerequisites). | Configure ingestion credentials, supported group resolution, and the [querying user's token](search-query-access-control-rbac-enforcement). | Supply supported permission identities and query authorization; implement the source-to-index permission translation. |
| **Customization** | Scope retrieval with supported filters and metadata; subject to Retrieval API capabilities. | Configure index schema, supported enrichment, chunks, and vectors. | Implement extraction, index schema, chunking, vectors, and permission updates in your ingestion pipeline. |
| **Operations** | Monitor retrieval and Microsoft 365 dependencies; no Search indexer to schedule. | Monitor indexer runs, refresh permissions, and verify documents and projections. | Operate the ingestion pipeline and handle update failures as described in the following section. |
| **Network and policy boundaries** | Follow the remote source's prerequisites and limitations; this isn't a Conditional Access workaround. | [Connector limitations](search-how-to-index-sharepoint-online#limitations-and-considerations) apply. SharePoint Online uses public endpoints. | Your application owns its source and Search connections; Push doesn't change SharePoint policy requirements. |
| **API and release scope** | Remote knowledge sources and the Copilot Retrieval API are preview; follow the [remote API guidance](agentic-knowledge-source-how-to-sharepoint-remote). | SharePoint ACL ingestion and filtering are generally available with REST `2026-10-01`. [Indexed knowledge-source guidance](agentic-knowledge-source-how-to-sharepoint-indexed) has separate API and preview requirements. | Permission ingestion through the [Push REST APIs](search-index-access-control-lists-and-rbac-push-api) is generally available. The linked guide identifies the REST API version used in its examples and SDK support considerations. For the permission-filter schema, see the [2026-10-01 data plane REST API reference](/en-us/rest/api/searchservice/operation-groups?view=rest-searchservice-2026-10-01&amp;preserve-view=true). |

For indexed retrieval, source propagation, content and ACL processing, group membership propagation, token renewal, query-time membership caching, and index refresh can each affect visibility. A requested or scheduled start isn't processing completion. Runs can exceed their interval or encounter throttling, retries, or failures. Schedules, reset, reset-docs, and permissions resync aren't immediate-freshness controls.

With Push, your application owns SharePoint change detection, content and permission synchronization, extraction, chunks and vectors, deletions and stale-record cleanup, retries, ordering, reconciliation, and monitoring. Submission timing alone doesn't establish strict end-to-end freshness.

### Handle authorization and update failures

If your application can't obtain valid user authorization or permission evaluation fails, stop returning protected content for that request and surface an error. Don't retry without the user token, disable permission filtering, or use elevated diagnostic access as a user-facing fallback. Apply this responsibility to application-cached content and generated responses as well.

For a customer-managed Push pipeline:

1. Inspect each document's indexing result, including partial failures in an HTTP `207` response. Track failed keys and retry retryable failures with backoff, following [Load a search index](search-how-to-load-search-index#use-the-rest-apis).
2. Serialize updates for the same key and make retries idempotent. Consolidate changes before submission; batch action order isn't defined. Keep a source version or checkpoint in your pipeline so an older retry doesn't restore a revoked grant.
3. Submit the complete intended ACL collection when replacing a permission field. Collection updates replace the collection rather than append individual grants.
4. Reconcile source items against indexed keys and their chunks. Remove stale documents, obsolete chunks, and records outside the selected source scope using [document deletion guidance](search-how-to-delete-documents). An update to one key doesn't clean up other keys.
5. Verify indexing results, query visibility, and permitted and denied user access before treating an update as reconciled.

### Refresh indexed permissions

Configure a short recurring indexer schedule according to your permission-refresh needs. The minimum interval is five minutes. Use the existing [schedule definition](search-howto-schedule-indexers#schedule-definition) and [schedule configuration guidance](search-howto-schedule-indexers#configure-a-schedule).

The interval isn't a completion deadline or a permission-revocation service-level agreement (SLA). Runs can be delayed, and an overlapping run can cause a scheduled start to be skipped. See [Scheduling behavior FAQ](search-howto-schedule-indexers#scheduling-behavior-faq). Permission changes reach the index after detection and successful processing, not automatically at each scheduled start. A recurring schedule doesn't request a full permissions resync.

When you enable ACL ingestion, ordinary incremental processing refreshes detected item-level permission changes. A supported permission-change notification for a non-root document-library folder also causes the indexer to enumerate in-scope descendants and refresh each item's source ACLs during a subsequent successful run, even if the child content hasn't changed. A child with unique permissions retains its own source access rules rather than receiving a copy of the folder's ACL.

This folder-permission path is independent of the rename and move propagation option and doesn't require a separate full permissions resync. It doesn't establish the same propagation behavior for site, library, list, or drive-root changes, or for missed source notifications.

| Change scope | Detected automatically | Recommended action |
| --- | --- | --- |
| **Detected permission change on an item with unique permissions** (file, list item, or page) | Yes | Run the indexer or allow its schedule to run, then verify the refreshed ACLs. |
| **Content change on a specific item** | Yes | Processing the changed item also re-evaluates its effective ACLs. |
| **Supported non-root document-library folder permission-change notification** | Yes | A subsequent successful run refreshes in-scope descendants, including unchanged files. Children with unique permissions retain their own source ACLs. |
| **Site, library, list, or drive-root permission change; missed notification** | Not covered by the folder update path | Use permissions resync to refresh existing indexed ACLs, or reset affected documents to reprocess their content and ACLs. Verify the results. |
| **ACL ingestion enabled on an existing indexer** | Requires backfill | If existing records already contain `metadata_spo_item_path`, use permissions resync. Otherwise, add the required field and applicable projection mapping, then reset and reprocess affected source items to populate their paths and ACLs. |

These operations also apply to the generated indexer of an indexed SharePoint knowledge source. Adding a schema field alone doesn't populate existing records. For projected indexes, verify the permission and source metadata on the affected chunks.

Treat source lifecycle changes separately from permission-only refresh:

- **Content changes:** Reprocess the affected content and its chunks through a normal indexer run or targeted reset. Permissions resync doesn't rerun extraction or embeddings.
- **Moves and renames:** Check the connector's [incremental indexing limitations](search-how-to-index-sharepoint-online#limitations-and-considerations) and update source selection paths if needed. Compare the current source path and indexed identity with the earlier records and chunks; don't treat permissions resync as key migration.
- **Deletions:** The connector detects source deletions on subsequent runs. After successful processing, verify the source item's indexed documents and chunks are absent.
- **Stale records or chunks:** Compare expected source items and projected children with actual indexed keys after processing. Investigate remaining records using [Delete documents](search-how-to-delete-documents); a successful refresh of current records isn't proof that obsolete records were removed.

Queries don't start indexers. [Monitor execution status](search-monitor-indexers) for completion, warnings, failures, and item counts, then verify permission-filtered results. A successful run alone doesn't establish end-to-end freshness.

### Reset specific documents

Use [reset specific documents](search-howto-run-reset-indexers#how-to-reset-docs-preview) to reprocess content and ACLs for known document keys, then run the indexer. This process differs from a permission-only refresh.

### Resynchronize ACLs across the full data source

Use [resync](search-howto-run-reset-indexers#resync-indexers) with REST API `2026-10-01` and `options: ["permissions"]`. The next manual or scheduled indexer execution processes the request; monitor it through completion. Request acceptance doesn't mean processing is complete. This permission-only operation uses each record's existing `metadata_spo_item_path` to refresh indexed documents and projected chunks without rerunning the skillset or embeddings. For records without paths, follow the backfill guidance. A later normal content run is a separate operation.

Permissions resync is separate from [synchronization retries](search-how-to-index-sharepoint-online#understand-synchronization-retries), which can reprocess content during a normal indexer run. It also doesn't add support for organization-wide sharing links or link expiration.

Until the relevant update is processed, queries can use stale indexed ACLs. After processing, compare a permitted and a denied test user's results by using the [query troubleshooting checks](troubleshoot-sharepoint-query-permission-filtering#8-compare-expected-and-actual-results).

After indexing your data and ACLs, you can [query the index](search-query-access-control-rbac-enforcement).

## Troubleshooting

| Symptom | Cause and resolution |
| --- | --- |
| `UserIds` or `GroupIds` are empty in indexed documents | If your skillset uses `projectionMode: skipIndexingParentDocuments`, the indexer bypasses field mappings for ACL fields. Set ACL fields via `indexProjections.selectors[].mappings` on every chunk instead. |
| SharePoint site group IDs are missing, or `GroupIds` values don't have the `spg:` prefix | Confirm the index has the `sharePointConnectorAppRegistration` configuration, the `SharePointSiteUrl` field exists with `sharepointSiteUrl: true`, and the `metadata_spo_site_url` mapping is present in either indexer field mappings or index projections. |
| `SharePointSiteUrl` is empty or null after indexing even though ACLs are otherwise populating correctly | The indexer emits this metadata under `metadata_spo_site_url`, not `metadata_sharepoint_site_url`. Verify that your indexer field mapping uses `"sourceFieldName": "metadata_spo_site_url"`. If your skillset uses index projections for chunked documents, verify that the projection mapping source is `/document/metadata_spo_site_url`. |
| The indexer returns 401 or 403 | Grant admin consent on both Microsoft Graph and SharePoint API permissions for your scenario. Use a federated credential (not a client secret) when the scenario requires it. See Permissions by ACL scenario. |
| Permissions are stale after a source ACL change | Check successful processing and the change scope in Synchronize permissions between indexed and source content. Supported folder notifications use normal incremental processing; other scopes or missed notifications can require an explicit refresh. |
| ACL ingestion reports a missing source path | Add the required `metadata_spo_item_path` index field and applicable projection mapping, then reset and reprocess affected source items. Adding the field alone doesn't populate existing records, and permissions resync doesn't backfill missing paths. See Add permission fields and backfill guidance. |
| `federatedCredentialId` is rejected when configuring `sharePointConnectorAppRegistration` | Use the managed identity's application ID, not the federated identity credential's object ID or the managed identity's principal ID. See Federated credential application ID. |
| The indexer returns `401 Unauthorized` and `FederatedCredentialApplicationId` is set | Verify you used the managed identity's Application ID (found in **Enterprise applications**), not the ingestion app's Application (client) ID (`ApplicationId`) or any Object ID. For a user-assigned managed identity, use the **Client ID** from the managed identity resource's **Properties** page. See Find the correct Microsoft Entra identifiers. |

For missing, unexpected, or failed query-time results after ACL metadata is indexed, see [Troubleshoot SharePoint permission filtering](troubleshoot-sharepoint-query-permission-filtering).
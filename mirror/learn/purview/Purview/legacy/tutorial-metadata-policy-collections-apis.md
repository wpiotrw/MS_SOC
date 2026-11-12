---
layout: Conceptual
title: Learn about Microsoft Purview collections metadata policy and roles APIs | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/legacy/tutorial-metadata-policy-collections-apis
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
description: This tutorial discusses how to manage role-based access control over Microsoft Purview collections to users, groups, or service principals.
author: chvukosw
ms.author: chvukosw
manager: laurawi
ms.reviewer: arindamba
ms.service: purview
ms.subservice: purview-data-governance-classic
ms.custom:
- has-azure-ad-ps-ref
- azure-ad-ref-level-one-done
- msecd-doc-authoring-1030
ms.topic: tutorial
ms.date: 2026-10-13T00:00:00.0000000Z
ai-usage: ai-assisted
locale: en-us
document_id: d78f945f-26af-a41d-96af-4fee1767c57a
document_version_independent_id: d78f945f-26af-a41d-96af-4fee1767c57a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/legacy/tutorial-metadata-policy-collections-apis.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: ../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: legacy/tutorial-metadata-policy-collections-apis
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/legacy/tutorial-metadata-policy-collections-apis.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://authoring-docs-microsoft.poolparty.biz/devrel/fcc3cd4a-59ea-47a2-9cc1-784142a5a25d
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://authoring-docs-microsoft.poolparty.biz/devrel/d7a55faf-a992-4e27-aa3a-eadc9830e778
platformId: d3b03a96-98ed-32dd-510a-e1278ddbbb94
---

# Learn about Microsoft Purview collections metadata policy and roles APIs | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

Note

Microsoft Purview Data Catalog (classic), Data Health Insights (classic), and Purview Workflow (classic) are no longer taking on new customers and these services, previously Azure Purview, are now in customer support mode.

In August 2021, access control in Microsoft Purview moved from Azure Identity & Access Management (IAM) (control plane) to [Microsoft Purview collections](../data-map-collections-manage-classic) (data plane). This change gives enterprise data curators and administrators more precise, granular access control on their data sources scanned by Microsoft Purview. The change also enables organizations to audit right access and right use of their data.

This tutorial guides you through step-by-step usage of the Microsoft Purview Metadata Policy APIs to help you add users, groups, or service principals to a collection, and manage or remove their roles within that collection. REST APIs are an alternative method to using the Azure portal or Microsoft Purview governance portal to achieve the same granular role-based access control.

For more information about the built-in roles in Microsoft Purview, see the [Microsoft Purview permissions guide](../data-gov-classic-permissions#roles). The guide maps the roles to the level of access permissions that are granted to users.

## Metadata Policy API Reference summary

The following table gives an overview of the [Microsoft Purview Metadata Policy API Reference](/en-us/rest/api/purview/metadatapolicydataplane/Metadata-Policy).

Note

Replace {pv-acc-name} with the name of your Microsoft Purview account before running these APIs. For instance, if your Microsoft Purview account name is *FabrikamPurviewAccount*, your API endpoints will become *FabrikamPurviewAccount.purview.azure.com*. The "api-version" parameter is subject to change. Please refer the [Microsoft Purview Metadata policy REST API documentation](/en-us/rest/api/purview/metadatapolicydataplane/Metadata-Policy) for the latest "api-version" and the API signature.

| API function | REST method | API endpoint | Description |
| --- | --- | --- | --- |
| Read All Metadata Roles | GET | https://{pv-acc-name}.purview.azure.com /policystore/metadataroles?&api-version=2021-07-01 | Reads all metadata roles from your Microsoft Purview account. |
| Read Metadata Policy By Collection Name | GET | https://{pv-acc-name}.purview.azure.com /policystore/collections/{collectionName}/metadataPolicy?&api-version=2021-07-01 | Reads the metadata policy by using a specified collection name (the six character random name that's generated by Microsoft Purview when it creates the policy). |
| Read Metadata Policy By PolicyID | GET | https://{pv-acc-name}.purview.azure.com /policystore/metadataPolicies/{policyId}?&api-version=2021-07-01 | Reads the metadata policy by using a specified policy ID. The policy ID is in GUID format. |
| Read All Metadata Policies | GET | https://{pv-acc-name}.purview.azure.com /policystore/metadataPolicies?&api-version=2021-07-01 | Reads all metadata policies from your Microsoft Purview account. You can pick a certain policy to work with from the JSON output list that's generated by this API. |
| Update/PUT Metadata Policy | PUT | https://{pv-acc-name}.purview.azure.com /policystore/metadataPolicies/{policyId}?&api-version=2021-07-01 | Updates the metadata policy by using a specified policy ID. The policy ID is in GUID format. |
|  |  |  |  |

## Microsoft Purview catalog collections API reference summary

The following table gives an overview of the Microsoft Purview collections APIs. For complete documentation about each API, select the API operation in the left column.

| Operation | Description |
| --- | --- |
| [Create or update collection](/en-us/rest/api/purview/accountdataplane/collections/create-or-update-collection) | Creates or updates a collection entity. |
| [Delete collection](/en-us/rest/api/purview/accountdataplane/collections/delete-collection) | Deletes a collection entity. |
| [Get collection](/en-us/rest/api/purview/accountdataplane/collections/get-collection) | Gets a collection. |
| [Get collection path](/en-us/rest/api/purview/accountdataplane/collections/get-collection-path) | Gets the parent name and display name chains that represent the collection path. |
| [List child collection names](/en-us/rest/api/purview/accountdataplane/collections/list-child-collection-names) | Lists the child collections names in the collection. |
| [List collections](/en-us/rest/api/purview/accountdataplane/collections/list-collections) | Lists the collections in the account. |

- If you're using the API, the service principal, user, or group that executes the API should have a [Collection Admin](../data-map-collections-manage-classic#check-permissions) role assigned in Microsoft Purview to execute this API successfully.
- For all Microsoft Purview APIs that require {collectionName}, you'll need to use *"name"* (and not *"friendlyName"*). Replace {collectionName} with the actual six-character alphanumeric collection name string.

    Note

    This name is different from the friendly display name you supplied when you created the collection. If you don't have {collectionName} handy, use the [List Collections API](/en-us/rest/api/purview/accountdataplane/collections/list-collections) to select the six-character collection name from the JSON output.

Here's an example JSON file:

```json
{
    "name": "74dhe7", 
    "friendlyName": "Friendly Name",
    "parentCollection": {
        "type": "CollectionReference",
        "referenceName": "{your_purview_account_name}"
    },
    "systemData": {
        "createdBy": "{guid}",
        "createdByType": "Application",
        "createdAt": "2021-08-26T21:21:51.2646627Z",
        "lastModifiedBy": "7f8d47e2-330c-42f0-8744-fcfb1ecb3ea0",
        "lastModifiedByType": "Application",
        "lastModifiedAt": "2021-08-26T21:21:51.2646628Z"
    },
    "collectionProvisioningState": "Succeeded"
}
```

### Policy JSON description

Here are some of the important identifiers in the JSON output that's received from the collection APIs:

**Name**: The name of the policy.

**Id**: The unique identifier for the policy.

**Version**: The latest version number of the policy.

Important

The version number is incremented each time the Update-Metadata-Policy API is called. Be sure to fetch the latest copy of the policy by invoking the Get-Policy-by-Policy-ID API. Perform this refresh every time before you call the Update Policy (PUT) API, so that you always have the latest version of the JSON file.

**DecisionRules**: List the rules and effect of this policy. For metadata policies, the effect is always *“Permit”*.

## Add or remove users from a collection or role

Use Microsoft Purview REST APIs to add or remove a user, group, or service principal from a collection or role. Detailed API usage is provided along with sample JSON outputs. We highly recommend that you follow the instructions in the next sections sequentially for best understanding of the Microsoft Purview metadata policy APIs.

## Get all metadata roles

To list all the available metadata access permission roles, run one of the following commands, depending on the portal you are using:

[Classic Microsoft Purview governance portal](../use-microsoft-purview-governance-portal):

```ruby
GET https://{your_purview_account_name}.purview.azure.com/policystore/metadataroles?api-version=2021-07-01
```

New Microsoft Purview portal:

```ruby
GET https://api.purview-service.microsoft.com/policystore/metadataroles?api-version=2021-07-01
```

The output JSON will describe the roles and their associated permissions in this format.

The default metadata roles are listed in the following table:

| Role ID | Permissions | Role description |
| --- | --- | --- |
| purviewmetadatarole\_builtin\_data-source-administrator | Microsoft.Purview/accounts/scan/read Microsoft.Purview/accounts/scan/write Microsoft.Purview/accounts/collection/read | Grants access to others to read, write collection, register data sources, and trigger scans. |
| purviewmetadatarole\_builtin\_collection-administrator | Microsoft.Purview/accounts/collection/read Microsoft.Purview/accounts/collection/write | Administrator-level full access to the entire collection, including add or remove users and service principal names (SPNs) from the collection, management rights, and grant or revoke access. In some cases, the Collection Administrator might be different from the creator of the collection. |
| purviewmetadatarole\_builtin\_purview-reader | Microsoft.Purview/accounts/data/read Microsoft.Purview/accounts/collection/read | Grants only read access to data handling and all metadata, including classifications, sensitivity labels, insights, and read assets in a collection, except scan bindings. |
| purviewmetadatarole\_builtin\_data-curator | Microsoft.Purview/accounts/data/read Microsoft.Purview/accounts/data/write Microsoft.Purview/accounts/collection/read | Grants full access to data handling and all metadata, including classifications, sensitivity labels, insights, and read assets in a collection, except scan bindings. |
| purviewmetadatarole\_builtin\_data-share-contributor | Microsoft.Purview/accounts/share/read Microsoft.Purview/accounts/share/write | Grants access to data shares as a contributor. |

```json
{
  "values": [
    {
      "id": "purviewmetadatarole_builtin_data-curator",
      "name": "data-curator",
      "type": "Microsoft.Purview/role",
      "properties": {
        "provisioningState": "Provisioned",
        "roleType": "BuiltIn",
        "friendlyName": "Data Curator",
        "cnfCondition": [
          [
            {
              "attributeName": "request.azure.dataAction",
              "attributeValueIncludedIn": [
                "Microsoft.Purview/accounts/data/read",
                "Microsoft.Purview/accounts/data/write",
                "Microsoft.Purview/accounts/collection/read"
              ]
            }
          ]
        ],
        "version": 1
      }
    },
    {
      "id": "purviewmetadatarole_builtin_data-source-administrator",
      "name": "data-source-administrator",
      "type": "Microsoft.Purview/role",
      "properties": {
        "provisioningState": "Provisioned",
        "roleType": "BuiltIn",
        "friendlyName": "Data Source Administrator",
        "cnfCondition": [
          [
            {
              "attributeName": "request.azure.dataAction",
              "attributeValueIncludedIn": [
                "Microsoft.Purview/accounts/scan/read",
                "Microsoft.Purview/accounts/scan/write",
                "Microsoft.Purview/accounts/collection/read"
              ]
            }
          ]
        ],
        "version": 1
      }
    },
    {
      "id": "purviewmetadatarole_builtin_collection-administrator",
      "name": "collection-administrator",
      "type": "Microsoft.Purview/role",
      "properties": {
        "provisioningState": "Provisioned",
        "roleType": "BuiltIn",
        "friendlyName": "Collection Administrator",
        "cnfCondition": [
          [
            {
              "attributeName": "request.azure.dataAction",
              "attributeValueIncludedIn": [
                "Microsoft.Purview/accounts/collection/read",
                "Microsoft.Purview/accounts/collection/write"
              ]
            }
          ]
        ],
        "version": 1
      }
    },
    {
      "id": "purviewmetadatarole_builtin_purview-reader",
      "name": "purview-reader",
      "type": "Microsoft.Purview/role",
      "properties": {
        "provisioningState": "Provisioned",
        "roleType": "BuiltIn",
        "friendlyName": "Microsoft Purview Reader",
        "cnfCondition": [
          [
            {
              "attributeName": "request.azure.dataAction",
              "attributeValueIncludedIn": [
                "Microsoft.Purview/accounts/data/read",
                "Microsoft.Purview/accounts/collection/read"
              ]
            }
          ]
        ],
        "version": 1
      }
    },
    {
      "id": "purviewmetadatarole_builtin_data-share-contributor",
      "name": "data-share-contributor",
      "type": "Microsoft.Purview/role",
      "properties": {
        "provisioningState": "Provisioned",
        "roleType": "BuiltIn",
        "friendlyName": "Data share contributor",
        "cnfCondition": [
          [
            {
              "attributeName": "request.azure.dataAction",
              "attributeValueIncludedIn": [
                "Microsoft.Purview/accounts/share/read",
                "Microsoft.Purview/accounts/share/write"
              ]
            }
          ]
        ],
        "version": 1
      }
    }
  ]
}
```

## Get all metadata policies

[Classic Microsoft Purview governance portal](../use-microsoft-purview-governance-portal):

```ruby
GET https://{your_purview_account_name}.purview.azure.com/policystore/metadataPolicies?api-version=2021-07-01
```

New Microsoft Purview portal:

```ruby
GET https://api.purview-service.microsoft.com/policystore/metadataPolicies?api-version=2021-07-01
```

The preceding command lists all available metadata policies across the entire collections hierarchy in tree format, from the root collection at the top to all its child policies. Each child collection contains each of its next level children.

Example:

```json
{
  "values": [
    {
      "name": "policy_FabrikamPurview",
      "id": "9b2f1cb9-584c-4a16-811e-9232884b5cac",
      "version": 30,
      "properties": {
        "description": "",
        "decisionRules": [
          {
            "kind": "decisionrule",
            "effect": "Permit",
            "dnfCondition": [
              [
                {
                  "attributeName": "resource.purview.collection",
                  "attributeValueIncludes": "fabrikampurview"
                },
                {
                  "fromRule": "permission:fabrikampurview",
                  "attributeName": "derived.purview.permission",
                  "attributeValueIncludes": "permission:fabrikampurview"
                }
              ]
            ]
          }
        ],
        "attributeRules": [
          {
            "kind": "attributerule",
            "id": "purviewmetadatarole_builtin_collection-administrator:fabrikampurview",
            "name": "purviewmetadatarole_builtin_collection-administrator:fabrikampurview",
            "dnfCondition": [
              [
                {
                  "attributeName": "principal.microsoft.id",
                  "attributeValueIncludedIn": [
                    "2f656762-e440-4b62-9eb6-a991d17d64b0",
                    "04314867-60a4-4e5a-ae16-8e5856f415d9",
                    "8988fe5c-5736-4179-9435-0a64c273b90b",
                    "6d563253-1d5b-48f2-baaa-5489f22ddce9",
                    "26f98046-5b02-4fa9-b709-e0519c658891",
                    "73fc02dc-becd-468b-a2a3-82238e722dae"
                  ]
                },
                {
                  "fromRule": "purviewmetadatarole_builtin_collection-administrator",
                  "attributeName": "derived.purview.role",
                  "attributeValueIncludes": "purviewmetadatarole_builtin_collection-administrator"
                }
              ],
              [
                {
                  "fromRule": "purviewmetadatarole_builtin_collection-administrator",
                  "attributeName": "derived.purview.role",
                  "attributeValueIncludes": "purviewmetadatarole_builtin_collection-administrator"
                },
                {
                  "attributeName": "principal.microsoft.groups",
                  "attributeValueIncludedIn": [
                    "ffd851fa-86ec-431b-95ea-8b84d5012383",
                    "cf84b126-4384-4952-91f1-7f705b25e569",
                    "5046aba1-5b81-411c-8fec-b84600f3f08b",
                    "b055a5c6-a04e-4d1a-8524-001ad81bfb28",
                    "cc194892-92fa-4ce3-96ae-1f98bef8211c"
                  ]
                }
              ]
            ]
          },
          {
            "kind": "attributerule",
            "id": "purviewmetadatarole_builtin_data-curator:fabrikampurview",
            "name": "purviewmetadatarole_builtin_data-curator:fabrikampurview",
            "dnfCondition": [
              [
                {
                  "attributeName": "principal.microsoft.id",
                  "attributeValueIncludedIn": [
                    "2f656762-e440-4b62-9eb6-a991d17d64b0",
                    "649f56ab-2dd2-40de-a731-3d3f28e7af92",
                    "c29a5809-f9ec-49fd-b762-2d4d64abb93e",
                    "04314867-60a4-4e5a-ae16-8e5856f415d9",
                    "73fc02dc-becd-468b-a2a3-82238e722dae",
                    "517a27d2-39ba-4c91-a032-dd9ecf8ad6f1",
                    "6d563253-1d5b-48f2-baaa-5489f22ddce9"
                  ]
                },
                {
                  "fromRule": "purviewmetadatarole_builtin_data-curator",
                  "attributeName": "derived.purview.role",
                  "attributeValueIncludes": "purviewmetadatarole_builtin_data-curator"
                }
              ],
              [
                {
                  "fromRule": "purviewmetadatarole_builtin_data-curator",
                  "attributeName": "derived.purview.role",
                  "attributeValueIncludes": "purviewmetadatarole_builtin_data-curator"
                },
                {
                  "attributeName": "principal.microsoft.groups",
                  "attributeValueIncludedIn": [
                    "b055a5c6-a04e-4d1a-8524-001ad81bfb28",
                    "cc194892-92fa-4ce3-96ae-1f98bef8211c",
                    "5046aba1-5b81-411c-8fec-b84600f3f08b"
                  ]
                }
              ]
            ]
          },
          {
            "kind": "attributerule",
            "id": "purviewmetadatarole_builtin_data-source-administrator:fabrikampurview",
            "name": "purviewmetadatarole_builtin_data-source-administrator:fabrikampurview",
            "dnfCondition": [
              [
                {
                  "attributeName": "principal.microsoft.id",
                  "attributeValueIncludedIn": [
                    "2f656762-e440-4b62-9eb6-a991d17d64b0",
                    "04314867-60a4-4e5a-ae16-8e5856f415d9",
                    "517a27d2-39ba-4c91-a032-dd9ecf8ad6f1",
                    "6d563253-1d5b-48f2-baaa-5489f22ddce9"
                  ]
                },
                {
                  "fromRule": "purviewmetadatarole_builtin_data-source-administrator",
                  "attributeName": "derived.purview.role",
                  "attributeValueIncludes": "purviewmetadatarole_builtin_data-source-administrator"
                }
              ],
              [
                {
                  "fromRule": "purviewmetadatarole_builtin_data-source-administrator",
                  "attributeName": "derived.purview.role",
                  "attributeValueIncludes": "purviewmetadatarole_builtin_data-source-administrator"
                },
                {
                  "attributeName": "principal.microsoft.groups",
                  "attributeValueIncludedIn": [
                    "b055a5c6-a04e-4d1a-8524-001ad81bfb28",
                    "cc194892-92fa-4ce3-96ae-1f98bef8211c",
                    "d34eb741-be5e-4098-90d7-eca8d4a5153f",
                    "664ec992-9af0-4773-88f2-dc39edc46f6f",
                    "5046aba1-5b81-411c-8fec-b84600f3f08b"
                  ]
                }
              ]
            ]
          },
          {
            "kind": "attributerule",
            "id": "permission:fabrikampurview",
            "name": "permission:fabrikampurview",
            "dnfCondition": [
              [
                {
                  "fromRule": "purviewmetadatarole_builtin_collection-administrator:fabrikampurview",
                  "attributeName": "derived.purview.permission",
                  "attributeValueIncludes": "purviewmetadatarole_builtin_collection-administrator:fabrikampurview"
                }
              ],
              [
                {
                  "fromRule": "purviewmetadatarole_builtin_purview-reader:fabrikampurview",
                  "attributeName": "derived.purview.permission",
                  "attributeValueIncludes": "purviewmetadatarole_builtin_purview-reader:fabrikampurview"
                }
              ],
              [
                {
                  "fromRule": "purviewmetadatarole_builtin_data-curator:fabrikampurview",
                  "attributeName": "derived.purview.permission",
                  "attributeValueIncludes": "purviewmetadatarole_builtin_data-curator:fabrikampurview"
                }
              ],
              [
                {
                  "fromRule": "purviewmetadatarole_builtin_data-source-administrator:fabrikampurview",
                  "attributeName": "derived.purview.permission",
                  "attributeValueIncludes": "purviewmetadatarole_builtin_data-source-administrator:fabrikampurview"
                }
              ]
            ]
          }
        ],
        "collection": {
          "type": "CollectionReference",
          "referenceName": "fabrikampurview"
        }
      }
    },
    {
      "name": "policy_b2zpf1",
      "id": "12b0bb28-2acc-413e-8fe1-179ff9cc54c3",
      "version": 0,
      "properties": {
        "description": "",
        "decisionRules": [
          {
            "kind": "decisionrule",
            "effect": "Permit",
            "dnfCondition": [
              [
                {
                  "attributeName": "resource.purview.collection",
                  "attributeValueIncludes": "b2zpf1"
                },
                {
                  "fromRule": "permission:b2zpf1",
                  "attributeName": "derived.purview.permission",
                  "attributeValueIncludes": "permission:b2zpf1"
                }
              ]
            ]
          }
        ],
        "attributeRules": [
          {
            "kind": "attributerule",
            "id": "purviewmetadatarole_builtin_collection-administrator:b2zpf1",
            "name": "purviewmetadatarole_builtin_collection-administrator:b2zpf1",
            "dnfCondition": [
              [
                {
                  "attributeName": "principal.microsoft.id",
                  "attributeValueIncludedIn": [
                    "2f656762-e440-4b62-9eb6-a991d17d64b0"
                  ]
                },
                {
                  "fromRule": "purviewmetadatarole_builtin_collection-administrator",
                  "attributeName": "derived.purview.role",
                  "attributeValueIncludes": "purviewmetadatarole_builtin_collection-administrator"
                }
              ],
              [
                {
                  "fromRule": "purviewmetadatarole_builtin_collection-administrator:ukx7pq",
                  "attributeName": "derived.purview.permission",
                  "attributeValueIncludes": "purviewmetadatarole_builtin_collection-administrator:ukx7pq"
                }
              ]
            ]
          },
          {
            "kind": "attributerule",
            "id": "permission:b2zpf1",
            "name": "permission:b2zpf1",
            "dnfCondition": [
              [
                {
                  "fromRule": "purviewmetadatarole_builtin_collection-administrator:b2zpf1",
                  "attributeName": "derived.purview.permission",
                  "attributeValueIncludes": "purviewmetadatarole_builtin_collection-administrator:b2zpf1"
                }
              ],
              [
                {
                  "fromRule": "permission:ukx7pq",
                  "attributeName": "derived.purview.permission",
                  "attributeValueIncludes": "permission:ukx7pq"
                }
              ]
            ]
          }
        ],
        "collection": {
          "type": "CollectionReference",
          "referenceName": "b2zpf1"
        },
        "parentCollectionName": "ukx7pq"
      }
    },
    {
      "name": "policy_7wte2n",
      "id": "a72084e4-ccab-4aec-a364-08ab001e4999",
      "version": 0,
      "properties": {
        "description": "",
        "decisionRules": [
          {
            "kind": "decisionrule",
            "effect": "Permit",
            "dnfCondition": [
              [
                {
                  "attributeName": "resource.purview.collection",
                  "attributeValueIncludes": "7wte2n"
                },
                {
                  "fromRule": "permission:7wte2n",
                  "attributeName": "derived.purview.permission",
                  "attributeValueIncludes": "permission:7wte2n"
                }
              ]
            ]
          }
        ],
        "attributeRules": [
          {
            "kind": "attributerule",
            "id": "purviewmetadatarole_builtin_collection-administrator:7wte2n",
            "name": "purviewmetadatarole_builtin_collection-administrator:7wte2n",
            "dnfCondition": [
              [
                {
                  "attributeName": "principal.microsoft.id",
                  "attributeValueIncludedIn": [
                    "2f656762-e440-4b62-9eb6-a991d17d64b0"
                  ]
                },
                {
                  "fromRule": "purviewmetadatarole_builtin_collection-administrator",
                  "attributeName": "derived.purview.role",
                  "attributeValueIncludes": "purviewmetadatarole_builtin_collection-administrator"
                }
              ],
              [
                {
                  "fromRule": "purviewmetadatarole_builtin_collection-administrator:ukx7pq",
                  "attributeName": "derived.purview.permission",
                  "attributeValueIncludes": "purviewmetadatarole_builtin_collection-administrator:ukx7pq"
                }
              ]
            ]
          },
          {
            "kind": "attributerule",
            "id": "permission:7wte2n",
            "name": "permission:7wte2n",
            "dnfCondition": [
              [
                {
                  "fromRule": "purviewmetadatarole_builtin_collection-administrator:7wte2n",
                  "attributeName": "derived.purview.permission",
                  "attributeValueIncludes": "purviewmetadatarole_builtin_collection-administrator:7wte2n"
                }
              ],
              [
                {
                  "fromRule": "permission:ukx7pq",
                  "attributeName": "derived.purview.permission",
                  "attributeValueIncludes": "permission:ukx7pq"
                }
              ]
            ]
          }
        ],
        "collection": {
          "type": "CollectionReference",
          "referenceName": "7wte2n"
        },
        "parentCollectionName": "ukx7pq"
      }
    }
  ]
}
```

## Get the selected metadata policy

You can use either of two APIs to fetch a particular collection's metadata policy JSON structure by supplying either {collectionName} or {PolicyID}.

As described in the following two sections, both APIs serve the same purpose, and the JSON outputs of both are exactly the same.

### Get the metadata policy of the collection by using the collection name

[Classic Microsoft Purview governance portal](../use-microsoft-purview-governance-portal):

```ruby
GET https://{your_purview_account_name}.purview.azure.com/policystore/collections/{collectionName}/metadataPolicy?api-version=2021-07-01
```

New Microsoft Purview portal:

```ruby
GET https://api.purview-service.microsoft.com/policystore/collections/{collectionName}/metadataPolicy?api-version=2021-07-01
```

1. The Microsoft Purview account name is {your\_purview\_account\_name}. Replace it with your Microsoft Purview account name.
2. In the JSON output of the previous API, "Get All Metadata Policies," look for the following section:

    { "type": "CollectionReference", "referenceName": "7xkdg2"}
3. Replace "{collectionName}" in the API URL with the value of "referenceName": "{6-char-collection-name}". For example, if your six-character collection name is "7xkdg2," the API URL will be formatted as:

    `https://{your_purview_account_name}.purview.azure.com/policystore/collections/7xkdg2/metadataPolicy?api-version=2021-07-01`
4. Execute the following API:

    ```json
    {
      "name": "policy_qu45fs",
      "id": "aaaabbbb-0000-cccc-1111-dddd2222eeee",
      "version": 0,
      "properties": {
        "description": "",
        "decisionRules": [
          {
            "kind": "decisionrule",
            "effect": "Permit",
            "dnfCondition": [
              [
                {
                  "attributeName": "resource.purview.collection",
                  "attributeValueIncludes": "qu45fs"
                },
                {
                  "fromRule": "permission:qu45fs",
                  "attributeName": "derived.purview.permission",
                  "attributeValueIncludes": "permission:qu45fs"
                }
              ]
            ]
          }
        ],
        "attributeRules": [
          {
            "kind": "attributerule",
            "id": "purviewmetadatarole_builtin_collection-administrator:qu45fs",
            "name": "purviewmetadatarole_builtin_collection-administrator:qu45fs",
            "dnfCondition": [
              [
                {
                  "attributeName": "principal.microsoft.id",
                  "attributeValueIncludedIn": [
                    "2f656762-e440-4b62-9eb6-a991d17d64b0"
                  ]
                },
                {
                  "fromRule": "purviewmetadatarole_builtin_collection-administrator",
                  "attributeName": "derived.purview.role",
                  "attributeValueIncludes": "purviewmetadatarole_builtin_collection-administrator"
                }
              ],
              [
                {
                  "fromRule": "purviewmetadatarole_builtin_collection-administrator:fabrikampurview",
                  "attributeName": "derived.purview.permission",
                  "attributeValueIncludes": "purviewmetadatarole_builtin_collection-administrator:fabrikampurview"
                }
              ]
            ]
          },
          {
            "kind": "attributerule",
            "id": "permission:qu45fs",
            "name": "permission:qu45fs",
            "dnfCondition": [
              [
                {
                  "fromRule": "purviewmetadatarole_builtin_collection-administrator:qu45fs",
                  "attributeName": "derived.purview.permission",
                  "attributeValueIncludes": "purviewmetadatarole_builtin_collection-administrator:qu45fs"
                }
              ],
              [
                {
                  "fromRule": "permission:fabrikampurview",
                  "attributeName": "derived.purview.permission",
                  "attributeValueIncludes": "permission:fabrikampurview"
                }
              ]
            ]
          }
        ],
        "collection": {
          "type": "CollectionReference",
          "referenceName": "qu45fs"
        },
        "parentCollectionName": "fabrikampurview"
      }
    }
    ```

### Get the metadata policy of the collection by using the policy ID

[Classic Microsoft Purview governance portal](../use-microsoft-purview-governance-portal):

```ruby
GET https://{your_purview_account_name}.purview.azure.com/policystore/metadataPolicies/{policyId}?api-version=2021-07-01
```

New Microsoft Purview portal:

```ruby
GET https://api.purview-service.microsoft.com/policystore/metadataPolicies/{policyId}?api-version=2021-07-01
```

1. The Microsoft Purview account name is {your\_purview\_account\_name}. Replace it with your Microsoft Purview account name.
2. In the JSON output of the previous API, "Get All Metadata Policies," look for the following section:

    {.... "name": "policy\_qu45fs", "id": "{policy-guid}", "version": N ....}
3. Replace "{policyId}" in the API URL with the value of "id". For example, if your "{policy-guid}" is "aaaabbbb-0000-cccc-1111-dddd2222eeee," the API URL will be formatted as:

    https://{your\_purview\_account\_name}.purview.azure.com/policystore/metadataPolicies/aaaabbbb-0000-cccc-1111-dddd2222eeee?api-version=2021-07-01
4. Now execute the following API:

    Note

    The output of this API call and the previous API call is the same. As mentioned previously, you can choose either one.

```json
{
  "name": "policy_qu45fs",
  "id": "aaaabbbb-0000-cccc-1111-dddd2222eeee",
  "version": 0,
  "properties": {
    "description": "",
    "decisionRules": [
      {
        "kind": "decisionrule",
        "effect": "Permit",
        "dnfCondition": [
          [
            {
              "attributeName": "resource.purview.collection",
              "attributeValueIncludes": "qu45fs"
            },
            {
              "fromRule": "permission:qu45fs",
              "attributeName": "derived.purview.permission",
              "attributeValueIncludes": "permission:qu45fs"
            }
          ]
        ]
      }
    ],
    "attributeRules": [
      {
        "kind": "attributerule",
        "id": "purviewmetadatarole_builtin_collection-administrator:qu45fs",
        "name": "purviewmetadatarole_builtin_collection-administrator:qu45fs",
        "dnfCondition": [
          [
            {
              "attributeName": "principal.microsoft.id",
              "attributeValueIncludedIn": [
                "2f656762-e440-4b62-9eb6-a991d17d64b0"
              ]
            },
            {
              "fromRule": "purviewmetadatarole_builtin_collection-administrator",
              "attributeName": "derived.purview.role",
              "attributeValueIncludes": "purviewmetadatarole_builtin_collection-administrator"
            }
          ],
          [
            {
              "fromRule": "purviewmetadatarole_builtin_collection-administrator:fabrikampurview",
              "attributeName": "derived.purview.permission",
              "attributeValueIncludes": "purviewmetadatarole_builtin_collection-administrator:fabrikampurview"
            }
          ]
        ]
      },
      {
        "kind": "attributerule",
        "id": "permission:qu45fs",
        "name": "permission:qu45fs",
        "dnfCondition": [
          [
            {
              "fromRule": "purviewmetadatarole_builtin_collection-administrator:qu45fs",
              "attributeName": "derived.purview.permission",
              "attributeValueIncludes": "purviewmetadatarole_builtin_collection-administrator:qu45fs"
            }
          ],
          [
            {
              "fromRule": "permission:fabrikampurview",
              "attributeName": "derived.purview.permission",
              "attributeValueIncludes": "permission:fabrikampurview"
            }
          ]
        ]
      }
    ],
    "collection": {
      "type": "CollectionReference",
      "referenceName": "qu45fs"
    },
    "parentCollectionName": "fabrikampurview"
  }
}
```

## Update the collection policy

```ruby
PUT https://{your_purview_account_name}.purview.azure.com/policystore/metadataPolicies/{policyId}?api-version=2021-07-01
```

In this section, you update the policy JSON that you obtained in the preceding step by adding or removing a user, group, or service principal from the collection. You then push it to the Microsoft Purview service by using a PUT REST method.

Whether you're adding or removing a user, group, or service principal, you'll follow the same API process.

1. Supply the user, group, or service principal object ID {guid} in the "attributeValueIncludedIn" array of the JSON.
2. Search the JSON output of the Get-Policy-by-ID API for the "attributeValueIncludedIn" array in the previous step, and either add or remove the user, group, or service principal object ID in the array. If you're unsure about how to fetch the user, group, or service principal object ID, see [Get-MgUser](/en-us/powershell/module/microsoft.graph.users/get-mguser).
3. There are multiple sections in the JSON mapping for each of the four roles. For the Collection Administrator permissions role, use the section bearing the ID called "purviewmetadatarole\_builtin\_collection-administrator". Likewise, use the corresponding section for the other roles.
4. To better understand the add/remove operation, carefully examine the difference between the JSON output from the previous API and the following output. In the JSON following output, we've added user ID "aaaabbbb-0000-cccc-1111-dddd2222eeee" As Collection Administrator.

```json
{
  "name": "policy_qu45fs",
  "id": "aaaabbbb-0000-cccc-1111-dddd2222eeee",
  "version": 0,
  "properties": {
    "description": "",
    "decisionRules": [
      {
        "kind": "decisionrule",
        "effect": "Permit",
        "dnfCondition": [
          [
            {
              "attributeName": "resource.purview.collection",
              "attributeValueIncludes": "qu45fs"
            },
            {
              "fromRule": "permission:qu45fs",
              "attributeName": "derived.purview.permission",
              "attributeValueIncludes": "permission:qu45fs"
            }
          ]
        ]
      }
    ],
    "attributeRules": [
      {
        "kind": "attributerule",
        "id": "purviewmetadatarole_builtin_collection-administrator:qu45fs",
        "name": "purviewmetadatarole_builtin_collection-administrator:qu45fs",
        "dnfCondition": [
          [
            {
              "attributeName": "principal.microsoft.id",
              "attributeValueIncludedIn": [
                "2f656762-e440-4b62-9eb6-a991d17d64b0",
                "00aa00aa-bb11-cc22-dd33-44ee44ee44ee"
              ]
            },
            {
              "fromRule": "purviewmetadatarole_builtin_collection-administrator",
              "attributeName": "derived.purview.role",
              "attributeValueIncludes": "purviewmetadatarole_builtin_collection-administrator"
            }
          ],
          [
            {
              "fromRule": "purviewmetadatarole_builtin_collection-administrator:fabrikampurview",
              "attributeName": "derived.purview.permission",
              "attributeValueIncludes": "purviewmetadatarole_builtin_collection-administrator:fabrikampurview"
            }
          ]
        ]
      },
      {
        "kind": "attributerule",
        "id": "permission:qu45fs",
        "name": "permission:qu45fs",
        "dnfCondition": [
          [
            {
              "fromRule": "purviewmetadatarole_builtin_collection-administrator:qu45fs",
              "attributeName": "derived.purview.permission",
              "attributeValueIncludes": "purviewmetadatarole_builtin_collection-administrator:qu45fs"
            }
          ],
          [
            {
              "fromRule": "permission:fabrikampurview",
              "attributeName": "derived.purview.permission",
              "attributeValueIncludes": "permission:fabrikampurview"
            }
          ]
        ]
      }
    ],
    "collection": {
      "type": "CollectionReference",
      "referenceName": "qu45fs"
    },
    "parentCollectionName": "fabrikampurview"
  }
}
```

## Add the Root Collection Administrator role

By default, the user who created the Microsoft Purview account is the Root Collection Administrator (that is, the administrator of the topmost level of the collection hierarchy). However, in some cases, an organization may want to change the Root Collection Administrator using the API.

```ruby
POST https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Purview/accounts/{accountName}/addRootCollectionAdmin?api-version=2021-07-01
```

To run the preceding command, you need only to pass the new Root Collection Administrator's object ID. As we mentioned before, the object ID can be that of any user, group, or service principal.

```json
{"objectId": "{guid}"}
```

Note

Users who call this API must have Owner or User Account and Authentication (UAA) permissions on the Microsoft Purview account to execute a write action on the account.
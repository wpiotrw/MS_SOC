---
layout: Conceptual
title: Learn about data governance in the Microsoft Purview portal | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/data-governance-purview-portal
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: nidought
ms.date: 2025-09-18T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Learn about the new experience for Microsoft Purview governance solutions in the Microsoft Purview portal.
locale: en-us
document_id: a28aa60b-5b22-1a93-fdc6-7aeb5ca38202
document_version_independent_id: a28aa60b-5b22-1a93-fdc6-7aeb5ca38202
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/data-governance-purview-portal.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: data-governance-purview-portal
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/data-governance-purview-portal.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: bf81a733-57ed-27b3-aff8-80ad4088ca73
---

# Learn about data governance in the Microsoft Purview portal | Microsoft Learn

The modern governance experience is available in the [Microsoft Purview portal](purview-portal) for anyone who didn't create a Microsoft Purview account in the Azure portal before, and for existing customers. This article explains how to use this new experience.

## The new governance experience

The Microsoft Purview portal, https://purview.microsoft.com, is a single, organization-wide instance of Microsoft Purview that's the next step towards unifying your organization's governance, policy, compliance, risk, and security. It's a prerequisite to a single platform used to manage and govern any data, both structured and unstructured, across your data estate. Including Azure, Microsoft 365, Azure, on-premises, or multicloud and SaaS applications in future.

- If you're a new Microsoft Purview customer, read about the [new governance experience for new customers](purview-portal#new-experience-for-new-customers).
- If you're an existing Microsoft Purview customer, read about the [new governance experience for existing customers](purview-portal#new-experience-for-existing-data-governance-customers).

Learn more about all the governance, data security, and risk and compliance features available in the [Microsoft Purview portal](purview-portal).

## How to use the new experience

If you're a new Microsoft Purview governance customer (if your organization doesn't have any Microsoft Purview accounts in any Azure subscriptions under your Microsoft Entra tenant), you can start using the [Microsoft Purview portal](https://purview.microsoft.com/) right now for your governance journey.

If your organization already has Microsoft Purview accounts in Azure, after your organization is enabled, getting started with the new experience depends on your organization's current structure:

- You only have one Microsoft Purview account:
    - Your account region matches your tenant region
    - Your account region doesn't match your tenant region
    - Your account has disabled all public access
- You have multiple Microsoft Purview accounts

For more information, visit the [new experience FAQ](data-governance-purview-portal-faq).

### One Microsoft Purview account

#### Your account has disabled all public network access

If your Microsoft Purview account had disabled all public network access and is using private endpoints, you need to make some changes before you upgrade it. You can continue to use [*ingestion* private endpoints](data-gov-classic-private-link-end-to-end#deploy-ingestion-private-endpoint), but not *account* or *portal* private endpoints. The new experience uses a new private endpoint called a *platform* private endpoint.

To check your current public network settings:

1. Go to the [Azure portal](https://portal.azure.com).
2. Search for your Microsoft Purview account.
3. Select **Networking** under the **Settings** menu.
4. If your firewall is set to **Disabled from all networks**, you need to follow the next steps to upgrade. If your firewall is set to **Enabled from all networks** or **Disabled for ingestion only**, you should be able to upgrade without these steps.

To upgrade an account using private endpoints, you need to:

1. Confirm that your firewall allows these global and tenant-specific endpoints (replacing the `accountname` and `tenantid`with your values):
    1. `api.purview-service.microsoft.com`
    2. `accountname.purview.azure.com`
    3. `tenantid-api.purview-service.microsoft.com`
2. After upgrading to the new experience, you can follow [this guide to set up private endpoints for governance solutions in the Microsoft Purview portal.](data-governance-private-endpoints)

Important

1. Currently, Azure Data Factory, Azure Machine Learning, and Azure Synapse lineage connections are not supported with the platform private endpoint, and might not work after switching. If your production replies on these lineage connections, wait until these connections are supported. (Azure Synapse is supported as a data source using a managed Virtual Network Integration Runtime and platform private endpoint.)
2. Scans that run after upgrading but before you set up the platform private endpoints might fail and need to be re-run after private endpoint set up.

#### Your region matches your tenant region

If your Microsoft Purview account's region matches your Microsoft Entra tenant region, and you set your networking settings to either **enabled from all networks** or **disabled for ingestion only**, you can use the new experience; no upgrade is required.

#### Your region doesn't map to your tenant region

1. A [Microsoft Purview Admin](data-governance-roles-permissions#tenant-level-role-groups) selects the **Upgrade** button in the Azure portal, Microsoft Purview portal, or upgrade email.

    Note

    If you don't have access to the Microsoft 365 role groups to assign users to the Microsoft Purview Admin role, [contact support](https://portal.azure.com/?quickstart=true#view/Microsoft_Azure_Support/HelpAndSupportBlade/%7E/overview).
2. If your account is in a different region than your tenant, an admin **confirms** setup, as seen in this image:

    ![Screenshot showing the different region confirmation pop-up window.](media/account-upgrades/different-region.png)
3. After confirmation, the new portal launches.

### Multiple Microsoft Purview accounts

The new experience requires a single, tenant-level or organization-wide account as the primary account for your organization. If you have multiple Purview accounts in your tenant, you can upgrade one account to the new experience and [merge](data-map-domains-merge-account) up to four other accounts into your primary account as [domains](data-map-domains).

1. If your Microsoft Purview account disables public network access and uses account or portal private endpoints, follow the steps at Disabled all public network access to upgrade.
2. A [Microsoft Purview Admin](data-governance-roles-permissions#tenant-level-role-groups) selects the **Upgrade** button in the Azure portal, Microsoft Purview portal, or upgrade email.
3. Select an existing account to upgrade it as your organization-wide account. See How to choosing a primary account.

    ![Screenshot of the pop-up window for selecting an organization wide primary account.](media/account-upgrades/selected-account.png)

    Note

    Upgrading one account doesn't affect your other Microsoft Purview accounts or their data. After upgrading, you can [merge](data-map-domains-merge-account) your secondary accounts into your primary account as [domains](data-map-domains).

    If you don't have access to the Microsoft 365 role groups to assign users to the Microsoft Purview Admin role, [contact support](https://portal.azure.com/?quickstart=true#view/Microsoft_Azure_Support/HelpAndSupportBlade/%7E/overview).
4. If the account you select is in a different region than your tenant, an admin needs to confirm setup.

    ![Screenshot of confirmation for selecting an account in a region that's different from your tenant region.](media/account-upgrades/selected-account-different-region.png)
5. After confirmation, the new portal launches.
6. You can take the tour and begin exploring the new Purview experience.
7. [Merge](data-map-domains-merge-account) your secondary accounts into your primary account as [domains](data-map-domains).

#### Disabled all public network access

If your Microsoft Purview account had disabled all public network access and is using private endpoints, you need to make some changes before you upgrade it. You can continue to use [*ingestion* private endpoints](data-gov-classic-private-link-end-to-end#deploy-ingestion-private-endpoint), but not *account* or *portal* private endpoints. The new experience uses a new private endpoint called a *platform* private endpoint.

To check your current public network settings:

1. Go to the [Azure portal](https://portal.azure.com).
2. Search for your Microsoft Purview account.
3. Select **Networking** under the **Settings** menu.
4. If your firewall is set to **Disabled from all networks**, you need to follow the next steps to upgrade. If your firewall is set to **Enabled from all networks** or **Disabled for ingestion only**, you should be able to upgrade without these steps.

To upgrade an account using private endpoints, you need to:

1. Confirm that your firewall allows these global and tenant-specific endpoints (replacing the `accountname` and `tenantid`with your values):
    1. `api.purview-service.microsoft.com`
    2. `accountname.purview.azure.com`
    3. `tenantid-api.purview-service.microsoft.com`
2. After upgrading to the new experience, you can follow [this guide to set up private endpoints for governance solutions in the Microsoft Purview portal.](data-governance-private-endpoints)

Important

1. Currently, Azure Data Factory, Azure Machine Learning, and Azure Synapse lineage connections are not supported with the platform private endpoint, and might not work after switching. If your production replies on these lineage connections, wait until these connections are supported. (Azure Synapse is supported as a data source using a managed Virtual Network Integration Runtime and platform private endpoint.)
2. Scans that run after upgrading but before you set up the platform private endpoints might fail and need to be re-run after private endpoint set up.

## Why upgrade to the new experience

If you're already using the classic Microsoft Purview governance portal, upgrading your Microsoft Purview account to the new experience offers several benefits, including:

- **Prerequisites for unified experience**: The upgrade is a prerequisite and one step to bring your environment closer to use data governance, security, risk, and compliance capabilities under the same platform.
- **Improved user experience**: The new experience provides a more streamlined and intuitive user interface, making it easier for users to access and manage their data assets in the new Microsoft Purview portal.
- **Enhanced features**: Upgrading unlocks new features and capabilities, such as live view, preset scans, and more.
- **Consolidated management**: The enhanced experience offers a centralized management interface for all your Microsoft Purview resources, simplifying administration tasks.
- **Access to new capabilities**: All new Microsoft Purview features are only available in the upgraded tenant level account.

After upgrading an existing account to the new experience, here's what to expect:

- **Account consolidation**: You access all other Microsoft Purview accounts in your tenant through the classic portal. Be prepared to merge those accounts with the primary account when the feature becomes available. Microsoft notifies customers who need to perform other steps to merge these accounts.
- **Roles and permissions**: Fine grained access control via roles and permissions at collection scopes continues to function as-is after your accounts are upgraded. In addition, there are new tenant-level roles that you can manage in the new portal. For more information, see our [tenant-level permissions documentation](data-governance-roles-permissions#tenant-level-role-groups).
- **Adapting to new features:** Educate users within your organization on the new features and capabilities introduced in the upgraded account, enabling them to maximize the benefits of these enhancements. This education includes understanding and using the following features:

    - [Live view](data-gov-live-view)
    - [Tenant-level permissions](data-governance-roles-permissions#tenant-level-role-groups)

## Accessing support

With the free version of Microsoft Purview governance solutions, you can't open support tickets for Microsoft Purview. You need to [upgrade to enterprise access](data-governance-free-version-upgrade-to-enterprise) for support.

## How to choose a primary account

If you have a single Microsoft Purview account, your account is likely [automatically upgraded](data-governance-purview-portal#one-microsoft-purview-account). When you have multiple Microsoft Purview accounts under the same Microsoft Entra tenant, consider the following factors while selecting an account for the upgrade. Select an account as primary tenant-level account by following guidelines below:

- **Data assets**: Choose the account with the most valuable or frequently used data assets, as this account becomes the primary data map after the upgrade.
- **Account usage**: Evaluate how each account is currently used and its role within your organization. Select accounts that are considered production for this purpose.
- **Permissions and access controls**: Consider the existing permissions and access controls for each account, as they're carried over to the upgraded environment (as an isolated domain).
- **System Assigned Managed Identity (SAMI) and User Assigned Managed Identity (UAMI)**: The existing system and [user assigned managed identities](data-map-data-scan-credentials#create-a-user-assigned-managed-identity) for the primary upgraded account can be used across all [domains](data-map-domains) in the Microsoft Purview instance.

#### Other considerations

- You can access the upgraded account through current endpoints and new endpoints, so there's no immediate effect if you use Microsoft Purview APIs. Any updates you perform in the upgraded account also reflect in the classic portal for the same Microsoft Purview account.
- New Microsoft Purview features are only available for the upgraded account.
- For other accounts in your tenant, you can continue to access through the [classic governance portal](https://portal.azure.com).

## Regions

Note

The regions listed here are for the single, organization-wide instance of Microsoft Purview that uses the Microsoft Purview portal.

Regions available for Microsoft Purview Unified Catalog are different. Visit [Supported regions for Unified Catalog](unified-catalog-regions).

This table lists the regions that you can use to access Microsoft Purview in the new portal:

| Purview Account Location | Mapped Microsoft Entra Country/Region | Tenant Location Code |
| --- | --- | --- |
| Australia East | Australia | AU |
|  | Fiji | FJ |
|  | New Zealand | NZ |
| Brazil South | Argentina | AR |
|  | Bolivia (Plurinational State of) | BO |
|  | Bonaire Sint Eustatius and Saba | BQ |
|  | Brazil | BR |
|  | Chile | CL |
|  | Colombia | CO |
|  | Curaçao | CW |
|  | Ecuador | EC |
|  | Falkland Islands (the) | FK |
|  | French Guiana | GF |
|  | Guyana | GY |
|  | Peru | PE |
|  | Paraguay | PY |
|  | Suri | SR |
|  | Sint Maarten (Dutch part) | SX |
|  | Uruguay | UY |
|  | Venezuela (Bolivarian Republic of) | VE |
| Canada Central | Canada | CA |
| Central India | India | IN |
|  | Sri Lanka | LK |
|  | Nepal | NP |
| Central US | United States of America (the) | US |
| East US | Antigua and Barbuda | AG |
|  | Anguilla | AI |
|  | Aruba | AW |
|  | Barbados | BB |
|  | Bermuda | BM |
|  | Bahamas (the) | BS |
|  | Cuba | CU |
|  | Dominica | DM |
|  | Dominican Republic (the) | DO |
|  | Grenada | GD |
|  | Guadeloupe | GP |
|  | Haiti | HT |
|  | Jamaica | JM |
|  | Saint Kitts and Nevis | KN |
|  | Cayman Islands (the) | KY |
|  | Saint Lucia | LC |
|  | Martinique | MQ |
|  | Panama | PA |
|  | Puerto Rico | PR |
|  | Trinidad and Tobago | TT |
|  | Saint Vincent and the Grenadines | VC |
|  | Virgin Islands (British) | VG |
|  | Virgin Islands (U.S.) | VI |
|  | United States of America (the) | US |
| East US 2 | United States of America (the) | US |
| France Central | France | FR |
| Germany West Central | Germany | DE |
| Japan East | Japan | JP |
| Korea Central | Korea (the Republic of) | KR |
| North Europe | Finland | FI |
|  | Faroe Islands (the) | FO |
|  | Ireland | IE |
|  | Iceland | IS |
|  | Moldova (the Republic of) | MD |
|  | Sweden | SE |
| Qatar Central | Qatar | QA |
| South Africa North | Angola | AO |
|  | Burkina Faso | BF |
|  | Burundi | BI |
|  | Benin | BJ |
|  | Botswana | BW |
|  | Congo (the Democratic Republic of the) | CD |
|  | Central African Republic (the) | CF |
|  | Congo (the) | CG |
|  | Côte d'Ivoire | CI |
|  | Cameroon | CM |
|  | Cabo Verde | CV |
|  | Djibouti | DJ |
|  | Algeria | DZ |
|  | Egypt | EG |
|  | Eritrea | ER |
|  | Ethiopia | ET |
|  | Gabon | GA |
|  | Ghana | GH |
|  | Gambia (the) | GM |
|  | Guinea | GN |
|  | Equatorial Guinea | GQ |
|  | Guinea-Bissau | GW |
|  | Kenya | KE |
|  | Comoros (the) | KM |
|  | Liberia | LR |
|  | Lesotho | LS |
|  | Libya | LY |
|  | Morocco | MA |
|  | Madagascar | MG |
|  | Mali | ML |
|  | Mauritania | MR |
|  | Mauritius | MU |
|  | Malawi | MW |
|  | Mozambique | MZ |
|  | Namibia | NA |
|  | Niger (the) | NE |
|  | Nigeria | NG |
|  | Réunion | RE |
|  | Rwanda | RW |
|  | Seychelles | SC |
|  | Sudan (the) | SD |
|  | Saint Helena Ascension and Tristan da Cunha | SH |
|  | Sierra Leone | SL |
|  | Senegal | SN |
|  | Somalia | SO |
|  | South Sudan | SS |
|  | São Tomé and Príncipe | ST |
|  | Eswatini | SZ |
|  | Chad | TD |
|  | Togo | TG |
|  | Tunisia | TN |
|  | Tanzania United Republic of | TZ |
|  | Uganda | UG |
|  | Mayotte | YT |
|  | South Africa | ZA |
|  | Zambia | ZM |
|  | Zimbabwe | ZW |
| Southeast Asia | Armenia | AM |
|  | American Samoa | AS |
|  | Brunei Darussalam | BN |
|  | Cocos (Keeling) Islands (the) | CC |
|  | Cook Islands (the) | CK |
|  | China | CN |
|  | Christmas Island | CX |
|  | Micronesia (Federated States of) | FM |
|  | Guam | GU |
|  | Hong Kong SAR | HK |
|  | Indonesia | ID |
|  | Cambodia | KH |
|  | Kiribati | KI |
|  | Lao People's Democratic Republic (the) | LA |
|  | Marshall Islands (the) | MH |
|  | Myanmar | MM |
|  | Macao SAR | MO |
|  | Northern Mariana Islands (the) | MP |
|  | Malaysia | MY |
|  | New Caledonia | NC |
|  | Norfolk Island | NF |
|  | Nauru | NR |
|  | Niue | NU |
|  | French Polynesia | PF |
|  | Papua New Guinea | PG |
|  | Philippines (the) | PH |
|  | Pitcairn | PN |
|  | Palau | PW |
|  | Solomon Islands | SB |
|  | Singapore | SG |
|  | Thailand | TH |
|  | Tokelau | TK |
|  | Tonga | TO |
|  | Tuvalu | TV |
|  | Taiwan (Province of China) | TW |
|  | United States Minor Outlying Islands (the) | UM |
|  | Viet Nam | VN |
|  | Vanuatu | VU |
|  | Wallis and Futuna | WF |
|  | Samoa | WS |
| South Central US | United States of America (the) | US |
| Switzerland North | Switzerland | CH |
| UAE North | United Arab Emirates (the) | AE |
| UK South | United Kingdom of Great Britain and Northern Ireland (the) | GB |
| West Central US | United States of America (the) | US |
| West Europe | Andorra | AD |
|  | Albania | AL |
|  | Austria | AT |
|  | Åland Islands | AX |
|  | Azerbaijan | AZ |
|  | Bosnia and Herzegovina | BA |
|  | Belgium | BE |
|  | Bulgaria | BG |
|  | Bahrain | BH |
|  | Belarus | BY |
|  | Cyprus | CY |
|  | Czechia | CZ |
|  | Denmark | DK |
|  | Estonia | EE |
|  | Spain | ES |
|  | Georgia | GE |
|  | Guernsey | GG |
|  | Gibraltar | GI |
|  | Greece | GR |
|  | Croatia | HR |
|  | Hungary | HU |
|  | Israel | IL |
|  | Isle of Man | IM |
|  | Italy | IT |
|  | Jersey | JE |
|  | Jordan | JO |
|  | Kuwait | KW |
|  | Kazakhstan | KZ |
|  | Lebanon | LB |
|  | Liechtenstein | LI |
|  | Lithuania | LT |
|  | Luxembourg | LU |
|  | Latvia | LV |
|  | Monaco | MC |
|  | Montenegro | ME |
|  | Republic of North Macedonia | MK |
|  | Malta | MT |
|  | Netherlands (the) | NL |
|  | Norway | NO |
|  | Oman | OM |
|  | Pakistan | PK |
|  | Poland | PL |
|  | Portugal | PT |
|  | Romania | RO |
|  | Serbia | RS |
|  | Russian Federation (the) | RU |
|  | Saudi Arabia | SA |
|  | Slovenia | SI |
|  | Svalbard and Jan Mayen | SJ |
|  | Slovakia | SK |
|  | San Marino | SM |
|  | Türkiye | TR |
|  | Ukraine | UA |
|  | Holy See (the) | VA |
|  | Yemen | YE |
| West US | United States of America (the) | US |
| West US 2 | United States of America (the) | US |
| West US 3 | Costa Rica | CR |
|  | Guatemala | GT |
|  | Honduras | HN |
|  | Mexico | MX |
|  | Nicaragua | NI |
|  | El Salvador | SV |
|  | New Mexico | NM |
|  | United States of America (the) | US |

For information about all available Microsoft Purview regions, see [Azure products by regions](https://azure.microsoft.com/explore/global-infrastructure/products-by-region/?products=purview&amp;regions=all).

Important

Microsoft 365 GCC regions aren't currently supported.

## Resources

- [New Microsoft Purview portal experience for data governance frequently asked questions](data-governance-purview-portal-faq)
- [Share and receive data](quickstart-data-share)
- [Data lineage in classic Data Catalog](data-gov-classic-lineage)
- [Data owner policies](concept-policies-data-owner)
- [Classification in Data Map](data-map-classification)
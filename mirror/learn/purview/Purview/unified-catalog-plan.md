---
layout: Conceptual
title: Plan for Microsoft Purview Unified Catalog with best practices | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-plan
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: nidought
ms.date: 2025-07-15T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: 
search.appverid:
- MET150
- MOE150
description: Get tips and strategies to develop Microsoft Purview Unified Catalog to reveal your data's value.
locale: en-us
document_id: 75501f15-71d5-a0cb-9c64-0e447c5cffc7
document_version_independent_id: 75501f15-71d5-a0cb-9c64-0e447c5cffc7
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-plan.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-plan
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-plan.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/63959238-cb90-4871-a33d-4a5519097e47
- https://authoring-docs-microsoft.poolparty.biz/devrel/54918a83-0404-4863-9c91-715186c1f582
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/78d87f42-5582-4a6b-90be-7db2f12b34e6
- https://authoring-docs-microsoft.poolparty.biz/devrel/b26f5f7a-0913-4a95-8337-ed7543902f2d
platformId: 5e13756a-4177-843f-ce25-a2486eb03815
---

# Plan for Microsoft Purview Unified Catalog with best practices | Microsoft Learn

This article provides data governance strategies to maintain healthy, valuable, discoverable data. For a list of technical steps to set up Unified Catalog, see the [get started guide](data-governance-get-started).

## Know your data with business concepts

[Business concepts](data-governance-get-started#business-concepts) in Unified Catalog are the tools you use to unite your data with your day-to-day business practices. This approach not only makes it easier for your data consumers to understand the data they're using, but it also allows you to democratize the data governance of those resources. Use your existing experts and data champions to build Unified Catalog into a rich resource.

When we refer to business concepts in Unified Catalog, we're talking about these five elements:

1. [Governance domains](unified-catalog-governance-domains)
2. [Data products](unified-catalog-data-products)
3. [Critical data elements (preview)](unified-catalog-critical-data-elements)
4. [Glossary terms](unified-catalog-glossary-terms)
5. [Objectives and key results (OKRs)](unified-catalog-okrs)

Jump to a section below for best practices and scenario-based guidance on:

- Governance domain structure models and development planning
- Planning for and creating data products
- Glossary term development planning and defining
- Creating and using custom metadata

### Create governance domains

Use governance domains to distribute ownership and maintenance tasks. They also make it easier for users to find the data they need. Distributing information by governance domains allows your users to reach the right level of information they need, without needing to traverse the entirety of your data estate.

When creating governance domains or reviewing your governance domain structure, consider the following factors:

1. Governance domain structure model
2. Development planning

#### Governance domain structure models

- **Central domain** (good): Using a single domain can be efficient for small organizations, but might not scale well and is prone to bottlenecks during growth.
- **Department-based domains** (good): Departments don't make decisions consistently, and if departments regularly shift, you might need to shift your Unified Catalog structure.
- **Functional/line-of-governance domains** (better): Grants flexibility to teams and aligns with the existing business model. This structure can be difficult to manage at scale and might need many subdomains to empower data decision makers. It can also create data use silos, which is the antithesis of the Unified Catalog's governance approach.
- **Domain mix** (best): Having a combination of domains across subject areas/data domains, functional domains, regulatory domains, and project domains aligns your data to its experts. In Unified Catalog, your data experts are your most powerful resource. They know what policies need to be applied and what others need to know to make the most use of the data. This structure is also the most durable to organizational updates, since it's based on how the data is used in the day-to-day, instead of on business structures.

#### Governance domain development planning

Tip

Don't align your governance domains with your platform domains. IT typically aligns with a technology structure or service/application, and isn't aligned with how business teams use data. Platform domains in Microsoft Purview Data Map likely align to these technology teams, instead of your business teams. The goal of governance domains is to align business users with the information that's most useful to them. Focus on data use, instead of data structure, to develop your governance domains.

1. When you begin creating your governance domains, start with a few domains aligned to teams that already have strong data stewardship:
    1. Assign data stewards and data product owners to your governance domains, and have them begin development on a glossary and data products that align with their current practices.
    2. If needed, scan data into Data Map in parallel to supplement your data products.
    3. Leave your governance domain in a *draft* state until a few data products are developed and ready for users.
2. Publish your governance domain, and assign Global Catalog Reader permissions to your first users to let them start exploring.
3. With the feedback from your first batch of users, iterate on existing data products, or expand to your next data products or governance domains.
4. Starting with a few governance domains that have mostly complete coverage with data products ensures data consumers that the Unified Catalog has what they need and that they can continue to come back.

Tip

Learn more about [governance domains](unified-catalog-governance-domains).

### Create data products

Much of the data that you store today has little to no known value. It can take time and manual effort to evaluate and understand before you can remove or improve it. When you focus on data with known value and use, more teams can build consistent value and show the benefits of having well-understood and highly utilized data. This focus drives further adoption of data governance practices and makes the effort to clean up data estates easier as the value of each data asset becomes clearer.

Focus on data resources that already exist in your organization. Adding these resources as data products in Unified Catalog makes it easier for your users to discover them. It also makes access more scalable and improves trustworthiness with lineage, data quality, and accountability. Some examples of existing data resources are:

1. Gold zone data lakes, highly curated SQL stores, curated data warehouses, and data lakehouses that teams use to support their day-to-day practices.
2. Reports that are used to make decisions.
3. Data tables that are used in reporting environments.
4. Master and reference data.

#### Data product development planning

1. Plan data products as part of your intake process when you add data sources to Data Map. Data product owners should know which data stores you're registering and scanning, and which data stores have data assets ready to add to Unified Catalog.
2. Build your first data products from core data assets that you scanned into Data Map.
3. Publish your first data products when your users are ready to consume data with that domain.

Tip

Learn more about [data products](unified-catalog-data-products).

### Define glossary terms

When you build terms, start with what you already know and continue to build value from your data to show where effort is most impactful. Follow these tips when creating and managing glossary terms to create the most value.

1. Give data to the most passionate users to demonstrate the ability to continue growing value and provide prioritization for more governance.
2. Many business teams already have a glossary to help new employees orient themselves to the business. Use these as some of your first term candidates to describe a governance domain and its data.
3. If you're not sure if a term represents another concept (like an entity or business process), add a term so you can collect the most basic metadata. If needed, you can expire the term and use a new concept to collect more metadata and drive the intended end-to-end experience.
4. Once you add glossary terms, link these terms to data products to improve the discoverability of data products and enhance the consumers knowledge of the data.
5. Periodically check the data products that are mapped to a term to enable data stewards to better understand their use across the data estate.
6. Always improve and edit term definitions. Waiting to publish a term until it's fully aligned delays teams use of the term and prevents new value creation or escalation of potential improvements.

#### Term development planning

1. Data stewards should learn the framework of the governance domain, then begin to add known terms and start to develop new ones.
2. Develop term definitions that contain valuable information for consumers to understand their context and use.
3. Publish the first set of terms and data products together so consumers can start their data use cases and discovery of data in Unified Catalog.
4. Building semantic knowledge never stops, so make a plan on how you can enable your team to continue to contribute terms throughout your governance lifecycle.

Tip

Learn more about [glossary terms](unified-catalog-glossary-terms).

### Create and apply custom metadata

Custom metadata plays a crucial role in empowering organizations to govern their data effectively. By enabling users to define attributes tailored to their specific needs, custom metadata fosters better organization, accessibility, and utilization of data assets. In an era where data is the backbone of decision-making, custom metadata allows organizations to streamline processes, ensure compliance, and unlock the full potential of their data resources.

Go to **Unified Catalog** &gt; **Catalog management** &gt; **Custom metadata** to create and manage [business concept attributes](unified-catalog-attributes-business-concept) and [data asset attributes](unified-catalog-attributes-data-asset). Currently, you can manage your custom attributes for business concept types and data asset types.

Tip

Learn more about [custom metadata](unified-catalog-custom-metadata).

## Unlock business value by making data accessible

Now that your basic Unified Catalog structures are in place, it's time to start unlocking the value of your data by making it accessible to your users and tying it directly to your business goals. Creating value from data comes from using that data, but using data means every person in the company needs to find the right data at the right time and in the right format to provide the needed insights or functionality. Data consumers are the key to making new business value from data.

Jump to a section below for best practices and scenario-based guidance on:

- Helping your users search governance domains and data products
- Building out objectives and key results (OKRs)
- Establishing compliant data access
- Building logical data models with critica data elements (preview)

### Let users search and browse your governance domains and data products

You took the time to build out governance domains and data products, so give your data consumers access to use them and see how they do. Business users might be looking for strategic reports that are already available with the insights they need to make business decisions in a timely and well informed manner.

Here's how you can think about granting access to your users strategically:

- **Don't grant access to Unified Catalog to everyone at your company.** Enable the teams that need the data you have in your catalog first. If your data products aren't available in the format data scientists need or the data isn't in predefined reports for business users, they lose trust in your catalog. Enable the right roles to use the catalog first to build the pathway to success.
- **Start with the teams that need the data you have in your catalog.** Who did you build your data products for? Which teams helped develop your glossary terms? Those are good initial candidates.
- **Start with analysts and data experts that can tell you where gaps exist in the catalog.** They can help point to experts and business owners that can contribute to Unified Catalog. Over time the completeness of Unified Catalog will be great enough everyone in the company can find most of their data needs.

Tip

Learn more about [managing access to data in Unified Catalog](unified-catalog-data-product-access-policies).

### Create OKRs

Demonstrate the business value of your data by building objectives and key results (OKRs) and tying them to the data products that help to drive or measure that value. When business leaders appreciate the value of their data and the importance of governance, they prioritize these efforts and create new synergies in how teams build, maintain, and govern their data to create insights.

Building out an objective provides immediate recognition of the importance of the data to the users and the business it drives. This recognition greatly enhances the understanding of the role certain data plays in business processes or in the ability to achieve their goals.

1. Consider OKRs for process improvements, quality issues, major strategic goals, and anything else that you would measure with data to demonstrate business value and change.
2. Make sure to create a key result for each objective to show how the objective is being measured and evaluated, and create accountability to meet that goal.
3. Complex objectives might require many key results to accomplish. Key results might progress independently of the other key results. The measurement can show the areas that need prioritization or help to get back on track.

Tip

Learn more about [OKRs](unified-catalog-okrs).

### Compliant data access

Providing access to data can introduce risk to your company. Following known standards and policies is essential for ensuring access is granted appropriately and that there's responsible use of data. Users in Unified Catalog can complete a form for data access at the time of discovery or data use. Keeping this form and process as a part of the catalog makes access secure, quick, and consistent for a highly variable and technical data estate. Here are some ways you can successfully set up access in your catalog:

- Ensure the appropriate approvers are in place on data products and that they understand the processing needs of the data products.
- Some data products might have hundreds or thousands of access requests, so having a team in distributed time zones could be required to ensure timely access approval and provisioning.
- Prepare groups or back up approvers in case there are vacations or unplanned time off.
- Governance domain owners should check on the access requests summary periodically to validate expectations and see if changes to controls monitoring the access request process are driving the desired response times.

### Build logical data models with critical data elements (preview)

Improving deep technical understanding and expectations of data entities and elements includes new controls to assert if the data meets those expectations. Creating data dictionaries and logical models of data provides the structure and deep business expectations of the data to ensure that the data is fit for its purpose. By incorporating this knowledge into Unified Catalog, teams immediately gain an understanding of how data is structured and why, and how what is available in the physical data estate might differ.

- Focus on the data elements that are most important for your domain. Critical data elements show the deep expertise and importance that data has on your business.
- **Don't** focus on the completeness of the elements across an entire domain. Not every column needs this level of control, and many data elements might be self-explanatory for users.
- Evaluating critical data elements across different teams ensures that business teams have a common understanding of their data and how what one team creates affects many other areas of the business.
- Aligning access policies with critical data elements ensures proper access controls are in place for critical data across your whole data estate.
- Building data quality rules for critical data elements ensures that data meets expectations no matter where or how it's being used.

Tip

Learn more about [critical data elements (preview)](unified-catalog-critical-data-elements).

## Enhance data maturity

Improve your data estate and governance to fill gaps and remove bottlenecks to value creation:

- Monitor your health actions to improve governance incrementally across your entire Unified Catalog.
- Optimize for new uses of the data and eliminate data issues by improving data quality.
- Create best-in-class data products for single sources of truth with master data management.
- Evaluate your data health and prioritize for the greatest value impact.

Investing deeply in the core data that runs your company ensures this data is usable across the entire business consistently. By eliminating data issues and providing a stable base for insights creation, you enhance data reliability. Having evidence of data issues helps to ensure actionability of data governance. It drives improvements that immediately unlock new value without investing in data areas that have low value or aren't fully understood yet. Continuously improving data maturity helps teams share learnings with each other and show the proof of the improvement as changes take place.

Jump to a section below for best practices and scenario-based guidance on:

- Improving data products with governance-focused actions
- Using data quality to improve the trustworthiness of your data
- Creating source of truth data products with master data management
- Using data health controls to measure governance maturity
- Building domain-specific standards

Tip

Start exploring how to [manage data health and data quality](unified-catalog-data-health-management).

### Improve data products with governance-focused actions

Building trust in data requires continuous improvement and support. While consumers take time to find and apply data, they bring attention to issues or support needs. You can take easy actions ahead of time based on best practices. Health actions in health management provide a complete list of these useful actions for Unified Catalog, to help you focus on what you can do next to improve your governance. Here are some best practices for using health actions to get the most value:

- Check the actions of your data products while they're still in a draft state. This check ensures that when you publish the data, it has the basics covered and provides comfort to consumers that you published the data with care.
- Take actions at different times. Some actions take time to resolve as you learn more about the data or work with stewards to create more clarity. Keep checking on actions to see where new improvements are ready to be made.
- If actions seem overwhelming, unnecessary, or distracting, consider making changes to your health controls. Optimizing the number of actions any person takes ensures that the right level of governance is applied to data.

### Improve the trustworthiness of your data with data quality

Too often, data quality is a one-off project to fix a particular problem in the data. These improvements don't last. Good data quality requires continuous evaluation and improvement to ensure problems don't return or new problems aren't created.

- Once you define a baseline of data quality expectations, build a plan to remediate issues in a timely manner. This plan is essential to keeping the business functioning with data fit for use.
- Schedule your data quality scans to run regularly. This schedule helps to ensure consumers that data is continuously being improved and is highly supported.
- Set alerts on the critical rules and score changes. These alerts enable data providers to correct issues before a consumer finds or experiences an issue. Alerting can also be used to share transparently with consumers issues before they find it in an experience or by making a decision based on poor quality data.

### Create source of truth data products with master data management

Some data is so critical to nearly every process and the entire business that it deserves exceptional levels of management and governance. These data entities are usually cross-cutting entities like customer lists or employee profiles. They can require deep business expertise and experience in many business processes. Some data is highly usable but low scale, and still benefits from the deeper level of control and management. Examples of this data include reference data attributes of country or region, currency, or industry segments. Each of these data types benefits from master data management solutions to build a source of truth that is fit for use across your entire business.

- Practice master data management with data quality to ensure that this vital data is clean and consistent.
- Choose valuable data elements or high-risk data elements to ensure your effort produces high value. This level of data management is high effort.
- Create a critical data element and a data product for master data. These partner objects help to elevate your master data in the Unified Catalog and increase its use and understanding.
- Build new health controls for master data to continuously evaluate its use at scale and prevent new unmastered data from gaining use and causing confusion in a quickly evolving data estate.

Tip

Learn more about [master data management](data-governance-master-data-management).

### Measure governance maturity with data health controls

To ensure governance is effective and creates business value, you need to evaluate the maturity of data governance at scale across the entire business. By applying the built-in measurement of controls, health management enables the central data office or an individual governance domain to see where they can improve. Collecting this evidence at scale quickly elevates the most critical data issues impacting the business and shows where one issue affects many areas of the business. This evidence helps resolve prioritization issues with making data management changes and quickly demonstrates the value of having the right level of governance in place.

1. Establish a rhythm of business to review health management practices:
    1. Have a monthly review with governance domain leaders and the central data office to discuss priorities and needs for new governance or technical solutions.
    2. Empower teams to dig deep into their health management reports to make sure they can make the best decisions to create the value they need in their business.
    3. Bring health management to all levels of the business from the SLT to the individual steward to ensure that governance is right leveled and consistently actionable.
    4. Where data has larger issues requiring cross-business collaboration or deeper governance, consider creating a new governance domain and defining ownership for driving the governance of that data.
2. Don't expect all governance domains to have the same level of maturity or be focused on the same aspects of governance:
    1. Enabling governance at the right level empowers business owners to make the most valuable decisions about what to do with their data.
    2. Not all parts of the business have the same needs for their data, and forcing deeper levels of governance might not help to create business value when the focus is elsewhere.
    3. Some data is less valuable or emergent in the data estate, and the value isn't yet fully known. Enabling teams to move fast and adapt to their needs so they can mature their governance with the value of the data.
3. Consistently evaluate health management to look for large changes that can indicate large issues or new learnings that need attention.
4. Share your health management scores. Sharing can bring teams together to learn what works for them or how they're finding new controls to build new value within a domain. Seeing what 'good' health looks like can motivate other teams to improve and ensure they're also delivering valuable data to their consumers.

### Build domain-specific standards

The business owners of the data are best suited to ensure data governance is right sized for the level of value and control required. These business teams already have dependencies on the data and are in the best position to define their expectations and needs to make sure data is valuable.

- Empower governance domains to create new controls for their data regardless of where the data is used.
- Don't expect all governance domains to need the same level of controls or to adopt all controls. Data that's confined for use to a single part of the business by design might not benefit from a high level of control. Creating more control over data that doesn't have the appropriate value might prevent teams from collecting or keeping data that isn't fully utilized.
- Use the right level of control to help prioritize where low value data can be removed from the governance domain to eliminate risk and increase the value of the data estate.

## Ready to get started?

To build a data governance practice in your organization using Unified Catalog and Data Map, see [Get started with data governance](data-governance-get-started) or check out the [sample setup walkthrough](data-governance-setup-sample) for more of a scenario-based example of how to perform key functions in Unified Catalog.
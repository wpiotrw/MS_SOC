---
layout: Conceptual
title: Application card for Microsoft Purview Unified Catalog | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/unified-catalog-application-card
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
ms.author: chvukosw
author: chvukosw
manager: laurawi
ms.reviewer: jife
ms.date: 2026-10-13T00:00:00.0000000Z
audience: Admin
ms.topic: concept-article
ms.service: purview
ms.subservice: purview-data-governance
ms.collection: msec-ai-copilot
ms.custom: responsible-ai-transparency, msecd-doc-authoring-1030
ai-usage: ai-assisted
description: Learn about the AI features in Microsoft Purview Unified Catalog, including intended uses, limitations, evaluations, and best practices for responsible use.
locale: en-us
document_id: a7ec54ef-b1a5-ab3e-6feb-9215125a93d6
document_version_independent_id: a7ec54ef-b1a5-ab3e-6feb-9215125a93d6
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/unified-catalog-application-card.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: unified-catalog-application-card
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/unified-catalog-application-card.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/12ed19f9-ebdf-4c8a-8bcd-7a681836774d
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c6f99e62-1cf6-4b71-af9b-649b05f80cce
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3a764584-4f97-452b-8f1d-36f19b12f6ae
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3f56b378-07a9-4fa1-afe8-9889fdc77628
platformId: 8bf5fd33-73a7-2c37-8724-dc02ec4bd8c2
---

# Application card for Microsoft Purview Unified Catalog | Microsoft Learn

Important

Microsoft Purview Unified Catalog and classic Microsoft Purview data governance capabilities (formerly Azure Purview) are being retired. Microsoft is consolidating its data governance capabilities in Microsoft Fabric. You can no longer create new accounts, and existing capabilities will remain in maintenance mode through November 12, 2027. For retirement timelines, transition guidance, and recommended next steps, see the [Microsoft Purview data governance retirement announcement](https://aka.ms/DG-Deprecation).

## What is an Application or Platform Card?

Microsoft’s Application and Platform cards are intended to help you understand how our AI technology works, the choices application owners can make that influence application performance and behavior, and the importance of considering the whole application, including the technology, the people, and the environment. Application cards are created for AI applications and platform cards are created for AI platform services. These resources can support the development or deployment of your own applications and can be shared with users or stakeholders impacted by them.

As part of its commitment to responsible AI, Microsoft adheres to [six core principles](https://www.microsoft.com/ai/principles-and-approach): fairness, reliability and safety, privacy and security, inclusiveness, transparency, and accountability. These principles are embedded in the [Responsible AI Standard](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Microsoft-Responsible-AI-Standard-General-Requirements.pdf?culture=en-us&amp;country=us), which guides teams in designing, building, and testing AI applications. Application and Platform Cards play a key role in operationalizing these principles by offering transparency around capabilities, intended uses, and limitations. For further insight, readers are encouraged to explore Microsoft’s [Responsible AI Transparency Report](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/Responsible-AI-Transparency-Report-2024.pdf) and Code of Conduct, which outline how [enterprise customers](/en-us/legal/ai-code-of-conduct) and [individuals](https://www.microsoft.com/servicesagreement) can engage with AI responsibly.

## Overview

Microsoft Purview Unified Catalog is a data governance solution that enables business experts and technical data owners to collaborate and contribute to a shared understanding of data. Unified Catalog enables inventory of metadata and provides a framework for the governance of metadata and the use of the underlying data. Unified Catalog helps organizations create value from data, manage access to data, improve data quality, and monitor data health. Unified Catalog is intended for enterprise customers and their downstream users, including business users, analysts, data scientists, stewards, and governance leaders. [Learn about Unified Catalog](unified-catalog) capabilities and implementation guidance.

AI capabilities are embedded in selected capabilities to improve discovery and curation efficiency. These capabilities include natural language data product search (preview), suggested data asset mapping (preview), and suggested data quality rules (preview).

## Key terms

The following list provides a glossary of key terms related to Unified Catalog:

- **Data asset**: A technical data resource indexed in the catalog, such as a table, file, or report. Data assets are the building blocks that can be grouped and governed through higher-level business concepts.
- **Data product**: A curated grouping of related data assets with a defined business use case, ownership, and governance context. Data products are designed to improve discoverability, reuse, and controlled access.
- **Data quality rule**: A configurable rule that evaluates data quality dimensions such as completeness, consistency, conformity, accuracy, freshness, and uniqueness. Rules can be out-of-box, custom, or AI-suggested in supported preview workflows.
- **Governance domain**: A business-aligned boundary used to organize data and governance responsibilities. Domains help scale stewardship and simplify discovery by aligning data with business context.
- **Metadata**: Descriptive information about data, including technical properties, business definitions, lineage, classifications, and usage context. Unified Catalog uses metadata to power search, governance workflows, and health insights.
- **Natural language search (preview)**: An AI-enabled search mode that allows users to describe the data they need in plain language. The feature returns ranked data product results based on metadata and business context.

## Key features or capabilities

The key features and capabilities outlined here describe what Unified Catalog is designed to do and how it performs across supported tasks.

- **Business-aligned data organization**: Unified Catalog organizes information through governance domains, data products, glossary terms, and related concepts. This structure helps users understand data in business context rather than only by technical source or schema. It also supports distributed stewardship so teams can manage data where domain expertise exists.
- **Natural language data product discovery (preview)**: Users can search for data products by describing intent in plain language, rather than relying only on exact keywords. The feature currently supports data products in English, French, and Spanish, with corresponding search terms. This improves data discovery for semi-technical users who may not know internal naming conventions.
- **AI-assisted data product curation (preview)**: During data product creation, Unified Catalog can suggest relevant data assets based on metadata such as names, descriptions, and use cases. Suggestions are prioritized so owners can review the most relevant candidates first. The experience accelerates curation while keeping final selection under human control.
- **AI-assisted data quality rule generation (preview)**: Data quality stewards can use AI-generated rule suggestions as a starting point for rule authoring. Suggested rules are informed by profiling metadata and are meant to be reviewed and tested before use. This reduces setup time for quality programs while preserving expert oversight.
- **Integrated access governance workflows**: Data product access policies support configurable approvals and attestations. Policy inheritance from governance domains, glossary terms, and critical data elements helps maintain consistent control at scale. This balances data accessibility with compliance and right-use expectations.
- **Data health and monitoring capabilities**: Unified Catalog provides health management actions, data quality scoring, and reporting to track governance progress. Teams can monitor quality, identify gaps, and prioritize remediation. These controls support continuous improvement instead of one-time governance exercises.

## Intended uses

Unified Catalog can be used in multiple scenarios across a variety of industries. Some examples of use cases include:

- **Enterprise analytics readiness in financial services**: A bank can create curated data products for risk, finance, and customer analytics teams so analysts can find trusted data faster. Governance domains and access policies help enforce right-use and approval paths for regulated data. Natural language search can reduce the time it takes to discover relevant data products when users do not know technical table names. The result is quicker analysis with stronger governance controls.
- **Cross-functional reporting in government organizations**: A public sector organization can organize data products by service area, such as benefits, operations, and citizen support. Teams can use Unified Catalog to discover approved datasets, request access through policy workflows, and understand business definitions before use. This improves consistency across departments while preserving accountability and review requirements. It also helps reduce duplicated data preparation effort.
- **Data quality improvement in education systems**: A university can apply data quality rules to critical operational datasets used for enrollment, course planning, and student outcomes reporting. AI-suggested rules can speed up initial setup, while stewards validate and tune rules for institutional standards. Quality scores and actions provide visibility into where remediation is needed. This supports more reliable reporting and decision making.
- **Consumer goods demand planning and operations**: A retail organization can publish data products for sales, inventory, and supply chain teams with clear ownership and terms of use. Teams can reuse curated data instead of repeatedly rebuilding similar datasets. Governance and quality controls help maintain trust as data is shared across planning, merchandising, and operations functions. The approach supports both day-to-day reporting and longer-term planning.

## Models and training data

Unified Catalog leverages a variety of AI models to power the experience that users see. Some examples include Azure OpenAI GPT and embedding models offered by Foundry Models sold by Azure. To learn more about the data used to train the foundation models behind Unified Catalog, refer to the model details in Foundry.

- [Foundry Models sold by Azure](/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure)
- [Responsible AI practices at Microsoft](https://www.microsoft.com/ai/responsible-ai)

## Performance

Unified Catalog is designed to perform reliably in enterprise data governance scenarios where organizations have scanned and curated metadata in Microsoft Purview Data Map and have configured role-based access correctly. In this environment, users can discover data products, review business context, and request access through policy workflows with clear ownership and governance boundaries.

The application’s intended input modalities are primarily structured metadata and user-entered text. Structured inputs include data asset metadata, governance domains, glossary mappings, access policy settings, and data quality definitions. Text inputs include keyword search, natural language search prompts (preview), business descriptions, and use-case narratives entered by stewards and owners. Expected outputs include ranked discovery results, suggested data assets and quality rules in supported preview flows, policy workflow states, and governance health indicators such as quality scores and remediation actions.

For multilingual capabilities, natural language data product search (preview) is designed and documented for English, French, and Spanish data products and corresponding search terms. Organizations operating outside these supported language conditions should validate effectiveness for their specific content and user patterns before broad deployment.

Performance also depends on governance maturity and metadata quality. Experiences such as discovery relevance and recommendation usefulness generally improve when data products are well described, business concepts are curated, and ownership is clearly defined. Organizations should expect better outcomes when they apply iterative stewardship practices and maintain up-to-date metadata.

## Limitations

Understanding Unified Catalog’s limitations is crucial to determine if it is used within safe and effective boundaries. While we encourage customers to leverage Unified Catalog in their innovative solutions or applications, it’s important to note that Unified Catalog was not designed for every possible scenario. We encourage users to refer to either the [Microsoft Enterprise AI Services Code of Conduct](/en-us/legal/ai-code-of-conduct) (for organizations) or the [Code Conduct section in the Microsoft Services Agreement](https://www.microsoft.com/servicesagreement#3_codeOfConduct) (for individuals) as well as the following considerations when choosing a use case:

- **Domain scope constraints**: AI features in Unified Catalog are designed for data governance scenarios, not general-purpose knowledge tasks. Using these features outside governance context can reduce response relevance or completeness. Teams should align prompts and workflows to cataloged metadata and business governance objectives. This helps avoid misuse and improves reliability.
- **Language and input constraints**: Natural language data product search (preview) supports data products created in English, French, and Spanish, and search terms in the corresponding languages. Results for unsupported languages or highly ambiguous prompts can be less reliable. Long text inputs might also be difficult for some AI-assisted workflows to process effectively. Users should provide clear, scoped prompts and validate outputs.
- **Human review requirement for AI suggestions**: AI-generated data asset mappings and suggested data quality rules are intended as starting points. They can accelerate setup, but they don't replace expert review and testing. Applying suggestions without validation can introduce quality or governance gaps. Human oversight is required before operational use.

## Evaluations

Performance and safety evaluations assess whether AI applications are operating reliably and securely by examining factors like groundedness, relevance, and coherence while identifying the risks of generating harmful content. The following evaluations were conducted with safety components already in place, which are also described in Safety components and mitigations.

### Performance and quality evaluations

Performance evaluations for AI applications are essential to improving their reliability in real-world applications. Metrics like groundedness, relevance, and coherence help assess the accuracy and consistency of AI-generated outputs, so that they are factually supported in grounded content scenarios, contextually appropriate, and logically structured. For Unified Catalog, we conducted performance evaluations for the following metrics, which are available through Microsoft Foundry:

- Groundedness
- Coherence
- Fluency
- Similarity

### Risk and safety evaluations

Evaluating potential risks associated with AI-generated content is essential for safeguarding against content risks with varying degrees of severity. This includes evaluating an AI application's predisposition towards generating harmful content or testing vulnerabilities to jailbreak attacks. For [application/platform], we conducted risk and safety evaluations for the following metrics available through Microsoft Foundry:

- Hate and unfairness
- Sexual
- Violence
- Self-harm
- Protected material
- Indirect jailbreak
- Direct jailbreak
- Code vulnerability
- Ungrounded attributes

### Evaluation data for safety and quality

Our evaluation data is custom-built to assess AI application performance across key areas of **safety** and **quality**, simulating real-world scenarios and risks. We begin by identifying relevant evaluation aspects of concern based on multi-disciplinary research and expert input. These concerns are translated into targeted evaluation objectives and guide formulation of evaluation metrics. For **safety**, we create adversarial prompts to elicit undesirable or edge-case responses, which are then scored using AI-assisted annotators trained to assess alignment with Microsoft’s safety standards. For **quality**, we craft rubric-based prompts relevant to scenarios including evaluating retrieval-augmented generation (RAG) applications and agents. Datasets are curated from diverse sources including synthetic and public datasets to simulate real-world user scenarios. Using the curated datasets, both evaluations undergo iterative refinement and human alignment to improve metric efficacy and reliability. This methodology forms the foundation of repeatable, rigorous assessments that reflect how customers use evaluations to build better and safer AI.

### Custom evaluations

AI features in Unified Catalog underwent various testing before release, including red teaming to identify failure modes and off-scope behaviors. These evaluations focus on whether AI-assisted experiences remain aligned to intended data governance uses and whether they avoid generating responses that conflict with Microsoft AI principles. For current documented AI capabilities, the primary evaluated modality is text.

Evaluation methods include scenario-based testing of search and recommendation quality, plus risk-focused testing of edge-case prompts. Ideal outcomes are contextually relevant, governance-aligned outputs that help users complete discovery and curation tasks with clear next steps. Suboptimal outcomes include irrelevant recommendations, incomplete responses, or outputs that require substantial correction.

## Safety components and mitigations

- **Human-in-the-loop validation for AI features**: AI-generated suggestions in preview are intended to be reviewed and tested by users before adoption. This mitigation lowers the risk of overreliance on automated recommendations and supports accountable decision making. Stewards and owners remain responsible for final curation and policy decisions.
- **Feedback and issue reporting loops**: Users can provide feedback on AI outputs that are inaccurate, incomplete, or unclear, including unacceptable results. Feedback helps Microsoft improve AI application.

## Best practices for deploying and adopting Unified Catalog

Responsible AI is a shared commitment between Microsoft and its customers. While Microsoft builds AI applications with safety, fairness, and transparency at the core, customers play a critical role in deploying and using these technologies responsibly within their own contexts. To support this partnership, we offer the following best practices for deployers and end users to help customers implement responsible AI effectively.

Deployers and end-users (admins) should:

- **Exercise caution and evaluate outcomes when using Unified Catalog for consequential decisions or in sensitive domains**: Consequential decisions are those that may have a legal or significant impact on a person’s access to education, employment, financial platforms, government benefits, healthcare, housing, insurance, legal platforms, or that could result in physical, psychological, or financial harm. Sensitive domains—such as financial platforms, healthcare, and housing—require particular care due to the potential for disproportionate impact on different groups of people. When using AI for decisions in these areas, make sure that impacted stakeholders can understand how decisions are made, appeal decisions, and update any relevant input data.
- **Evaluate legal and regulatory considerations**: Customers need to evaluate potential specific legal and regulatory obligations when using any AI platforms and solutions, which may not be appropriate for use in every industry or scenario. Additionally, AI platforms or solutions are not designed for and may not be used in ways prohibited in applicable terms of service and relevant codes of conduct.

End-users should:

- **Exercise human oversight when appropriate**: Human oversight is an important safeguard when interacting with AI applications. While we continuously improve our AI applications, AI might still make mistakes. The outputs generated may be inaccurate, incomplete, biased, misaligned, or irrelevant to your intended goals. This could happen due to various reasons, such as ambiguity in the inputs or limitations of the underlying models. As such, users should review the responses generated by Unified Catalog and verify that they match their expectations and requirements.
- **Be aware of the risk of overreliance**: Overreliance on AI happens when users accept incorrect or incomplete AI outputs, mainly because mistakes in AI outputs may be hard to detect. For the end-user, overreliance could result in decreased productivity, loss of trust, application abandonment, financial loss, psychological harm, physical harm, among others. (e.g. a doctor accepts an incorrect AI output).

## Learn more about Unified Catalog

For additional guidance or to learn more about the responsible use of Unified Catalog, we recommend reviewing the following documentation:

- [Unified Catalog overview](unified-catalog)
- [Plan for Unified Catalog with best practices](unified-catalog-plan)
- [Search for data products in Unified Catalog](unified-catalog-data-products-search)
- [Create and manage data products in Unified Catalog](unified-catalog-data-products-create-manage)
- [Manage data product access policies](unified-catalog-data-product-access-policies)
- [Overview of data quality in Unified Catalog](unified-catalog-data-quality)
- [Microsoft Purview privacy statement](https://privacy.microsoft.com/privacystatement)
- [Microsoft Trust Center](https://www.microsoft.com/trust-center)

### Learn more about responsible AI

- [Microsoft AI principles](https://www.microsoft.com/ai/responsible-ai)
- [Microsoft responsible AI resources](https://www.microsoft.com/ai/tools-practices)
- [Microsoft Azure Learning courses on responsible AI](/en-us/ai)
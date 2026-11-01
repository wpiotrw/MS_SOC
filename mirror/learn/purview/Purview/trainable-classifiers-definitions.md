---
layout: Conceptual
title: Trainable classifier definitions - Microsoft Purview | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: saramaswamy
author: sanjayhr-Docs
manager: laurawi
ms.date: 2026-10-16T00:00:00.0000000Z
audience: Admin
ms.topic: article
ms.service: purview
ms.collection:
- purview-compliance
- must keep
- m365solution-mip
- m365initiative-compliance
ms.custom: admindeeplinkMAC, msecd-doc-authoring-1030
ai-usage: ai-assisted
search.appverid:
- MOE150
- MET150
description: This document contains all trainable classifiers, their definitions and all the file types they search through to find sensitive information
locale: en-us
document_id: c362cabe-fc51-bfe3-cdd4-e65d0eb3cc6a
document_version_independent_id: c362cabe-fc51-bfe3-cdd4-e65d0eb3cc6a
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/trainable-classifiers-definitions.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: trainable-classifiers-definitions
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/trainable-classifiers-definitions.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c6f99e62-1cf6-4b71-af9b-649b05f80cce
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/3f56b378-07a9-4fa1-afe8-9889fdc77628
platformId: b90f1bca-57b0-5239-6631-066516bc2805
---

# Trainable classifier definitions - Microsoft Purview | Microsoft Learn

Microsoft Purview comes with multiple pretrained classifiers. They appear in the **Microsoft Purview portal** &gt; **Data classification** &gt; **Trainable classifiers** view with the status of `Ready to use`.

All Microsoft provided classifiers evaluate items in all the languages listed in the Supported languages columns of the tables below. For more information on how to use trainable classifiers, see [Learn about trainable classifiers](trainable-classifiers-learn-about).

Important

Built-in trainable and global classifiers don't provide an exhaustive or complete list of terms or language across these areas. Further, language and cultural standards continually change, and in light of these realities, Microsoft reserves the right to update these classifiers in its discretion. While classifiers can assist your organization in detecting these areas, classifiers are not intended to provide your organization's sole means of detecting or addressing the use of such language. Your organization, not Microsoft or its subsidiaries, remains responsible for all decisions related to monitoring, scanning, blocking, removal, and retention of any content identified by a pretrained classifier, including compliance with local privacy and other applicable laws. Microsoft encourages consulting with legal counsel before deployment and use.

## Actuary reports

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| This classifier is used to identify reports prepared by an organization's actuary on the current and future conditions of funds, such as pension or insurance pools. These documents analyze the organization's loss experience using probability theory and statistical analysis to determine if the fund is on track to meet the needs of its dependents. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one | English | Yes |

## Adult, racy, and gory images

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects images that are potentially inappropriate. Scanning and detection are supported for Exchange Online email messages, and Microsoft Teams channels and chats. | Detects content in .jpeg, .png, .gif, and .bmp files. | N/A | N/A |

Note

Images must be between 100 kilobytes (KB) and 4 megabytes (MB) in size and be greater than 50 x 50 pixels in height x width dimensions.

## Agreements

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects content related to legal agreements such as nondisclosure agreements, statements of work, loan and lease agreements, employment and noncompete agreements. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .msg, .eml files. | English | Yes |

## Asset management

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Identifies documents related to tracking fixed asset records. For example: asset inventory, long-term funding, life cycle costing, level of service, and criticality within an organization. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .pptx, .pptm, .ppt, .potx, .potm, .pot, .ppsx, .ppsm, .pps, .ppam, .ppa |  |  |
| English | Yes |  |  |

## Bank statement

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects items that contain a financial transaction of a bank account including account information, deposits, withdrawals, account balance, interest accrued, and bank charges within a given period. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt files. | Chinese (`zh`), English, French, German, Japanese, Spanish | Yes |

## Budget

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects budget documents, budget forecasts and current budget statements including income and expenses of an organization. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .eml, .pptx, .pptm, .ppt, .potx, .potm, .pot, .ppsx, .ppsm, .pps, .ppam, .ppa, .xlsx, .xlsm, .xlsb, .xls, .csv, .xltx, .xltm, .xlt, .xlam, .xla files. | English | Yes |

## Business context

(Preview)

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects business-related content such as organizational structure, policy updates, contracts, HR policies, and crucial financial data such as revenue and profits, healthcare forms, employee contracts, etc. | Detects content in docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .pptx, .pptm, .ppt, .potx, .potm, .pot, .ppsx, .ppsm, .pps, .ppam, .ppa, .txt files. | English | N.A. |

## Business plan

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects components of a business plan including business opportunity, plan of achieving the outcomes, market study, and competitor analysis. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .eml, .pptx, .pptm, .ppt, .potx, .potm, .pot, .ppsx, .ppsm, .pps, .ppam, .ppa files. | English | No |

## Completion certificates

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects official documents that are issued at the end of a project or work by a project manager or a contractor. This document is used to testify that work on a particular project has been completed as per a contract or an agreement. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt files. | English | Yes |

## Compliance policies

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Identifies confidential documentation across various major compliance policies, including GDPR, HIPAA, ISO, PCI, SOC, and SSAE 18 compliance. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .txt | English | Yes |

## Construction specifications

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects construction specifications for commercial and industrial projects like factories, plants, commercial offices, airports, roads. | Captures guidelines on the quality, quantity, types of building material, processes, etc. Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .msg, .eml, .pptx, .pptm, .ppt, .potx, .potm, .pot, .ppsx, .ppsm, .pps, .ppam, .ppa files. | English | Yes |

## Control system and SCADA files

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Identifies documents that set the framework for approval, updates, amendments, change tracking, publication (internal or external), and version control. It also identifies Supervisory Control and Data Acquisition (SCADA) files. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .txt | English | Yes |

## Corporate sabotage

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects messages that mention acts to damage or destroy corporate assets or property. This classifier can help customers manage regulatory compliance obligations such as NERC Critical Infrastructure Protection standards or state by state regulations like Chapter 9.05 RCW in Washington state. | Detects content in .msg, .docx, .pdf, .txt, .rtf, .jpeg, .jpg, .png, .gif, .bmp, .svg files. | English | Yes |

Important

This classifier can capture a large volume of bulk sender/newsletter content. In Communication Compliance, you can mitigate the detection of large volumes of bulk sender/newsletter content by selecting the **Filter email blasts** check box when you create the policy. You can also edit an existing Communication Compliance policy to turn on this feature.

## Credit report

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Identifies statements that inform about an individual's or organization's credit activity and current credit situation. This includes loan payment history and the status of credit accounts. It must include a credit report or credit score. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .msg, .eml | English | Yes |

## Customer complaints

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| The customer complaints classifier detects feedback and complaints made about your organization's products or services. This classifier can help you meet regulatory requirements on the detection and triage of complaints, like the Consumer Financial Protection Bureau and Food and Drug Administration requirements. | For Communications Compliance, it detects content in .msg, and .eml files. For the rest of Microsoft Purview Information Protection services, it detects content in .docx, .pdf, .txt, .rtf, .jpg, .jpeg, .png, .gif, .bmp, .svg files. | English | No |

## Customer files

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Identifies files related to customers, such as personal account files, account information files, grievance records, and feedback files. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .pptx, .pptm, .ppt, .potx, .potm, .pot, .ppsx, .ppsm, .pps, .ppam, .ppa, .txt, .one, .msg, .eml | English | Yes |

## Discrimination

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects explicit discriminatory language and is sensitive to discriminatory language against the African American/Black communities when compared to other communities. | This applies to communications compliance, it's a text based classifier. | English | Yes |

## Employee disciplinary action

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects files relating to disciplinary action including a reprimand or corrective action in response to employee misconduct, rule violation, or poor performance. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .msg, .eml files. | English | Yes |

## Employee insurance

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects documents pertaining to employee medical insurance and workplace disability insurance. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .msg, .eml, .pptx, .pptm, .ppt, .potx, .potm, .pot, .ppsx, .ppsm, .pps, .ppam, .ppa files. | English | Yes |

## Employment agreement

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects employment agreement containing details like the starting date, salary, compensation, duties of employment. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt files. | English | Yes |

## Employee pension records

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects documents that are related to employee's pension records such as claim forms, declaration forms, schemes, and benefit statement. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .pptx, .pptm, .ppt, .potx, .potm, .pot, .ppsx, .ppsm, .pps, .ppam, .ppa, .txt, .one, .msg, .eml files. | English | Yes |

## Employee stocks and financial bond records

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects documents that are related stock and financial bonds award by organization to employees. Identifies employee stocks and financial bonds details that fall under employee's payroll. Contains details like bond clause, allocations, equity. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .pptx, .pptm, .ppt, .potx, .potm, .pot, .ppsx, .ppsm, .pps, .ppam, .ppa, .txt, .one, .msg, .eml files. | English | Yes |

## Enterprise risk management

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Enterprise risk management includes financial risks, strategic risks, operational risks, and risks associated with accidental losses. This category consists of methods used by organizations to manage risks and seize opportunities related to the achievement of their objectives. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt files. | English | Yes |

## Environmental permits and clearances

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| This classifier is used to identify documents related to the procedure of obtaining clearance from the government for the installation and modification (amendment) of certain projects. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .pptx, .pptm, .ppt, .potx, .potm, .pot, .ppsx, .ppsm, .pps, .ppam, .ppa, .eml | English | Yes |

## Facility permits

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Identifies permits that include permission to construct or operate a facility. These include authorizations, licenses, or equivalent control documents issued by the relevant authority. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .txt | English | Yes |

## Factory incident investigation reports

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| This classifier is used to identify formal recordings of facts related to workplace accidents, injuries, or near misses. These reports aim to uncover the circumstances and conditions that led to the event to prevent future incidents. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .pptx, .pptm, .ppt, .potx, .potm, .pot, .ppsx, .ppsm, .pps, .ppam, .ppa, .txt, .one | English | Yes |

## Finance

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects content in corporate finance, accounting, economy, banking, and investment categories. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .msg, .eml, .pptx, .pptm, .ppt, .potx, .potm, .pot, .ppsx, .ppsm, .pps, .ppam, .ppa, .xlsx, .xlsm, .xlsb, .xls, .csv, .xltx, .xltm, .xlt, .xlam, .xla files. | English | Yes |

## Financial audit

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects files, documents, and reports pertaining to financial audit, both external or internal audit undertaken in an organization. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .msg, .eml files. | English | Yes |

## Financial statement

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects financial statements like income statement, balance sheet, cash flow statement, statement of changes in equity. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .xlsx, .xlsm, .xlsb, .xls, .csv, .xltx, .xltm, .xlt, .xlam, .xla files. | English | Yes |

## Freight documents

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects documents that authorize the export or import of a good in a specific quantity from source to destination. This model categorizes different documents including Bill of Ladings, Certificate of Origin, Commercial Invoice, Export import customs declaration, Importer Security Filing (ISF). | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .pptx, .pptm, .ppt, .potx, .potm, .pot, .ppsx, .ppsm, .pps, .ppam, .ppa, .txt, .one files. | English | Yes |

## Garnishment

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Identifies documents related to garnishment notices, records, and earnings attachments. It covers the legal process of withholding money from paychecks to be sent to another party. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one | English | Yes |

## Gifts & entertainment

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects messages that suggest exchanging gifts or entertainment in return for service, which violates regulations related to bribery. This classifier can help customers manage regulatory compliance obligations such as Foreign Corrupt Practices Act (FCPA), UK Bribery Act, and FINRA Rule 2320. | Detects content in .msg, .docx, .pdf, .txt, .rtf, .jpeg, .jpg, .png, .gif, .bmp, .svg files. | English | Yes |

Important

This classifier can capture a large volume of bulk sender/newsletter content. In Communication Compliance, you can mitigate the detection of large volumes of bulk sender/newsletter content by selecting the **Filter email blasts** check box when you create the policy. You can also edit an existing Communication Compliance policy to turn on this feature.

## Harassment

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects a specific category of offensive language text items related to offensive conduct targeting one or multiple individuals based on the following traits: race, ethnicity, religion, national origin, gender, sexual orientation, age, disability. | Detects content in .msg, .docx, .pdf, .txt, .rtf, .jpeg, .jpg, .png, .gif, .bmp, .svg files. | - Arabic - Chinese (Simplified) - Chinese (Traditional) - Dutch - English - French - German - Italian - Korean - Japanese - Portuguese - Spanish | Yes (English) |

## Health/Medical forms

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects various forms and files that are used for systematic documentation of a patient's admission details, medical history, patient information, and prior authorization request and are typically used in medical/health services. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .msg, .eml, .pptx, .pptm, .ppt, .potx, .potm, .pot, .ppsx, .ppsm, .pps, .ppam, .ppa files. | English | Yes |

## Healthcare

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects content in medical and healthcare administration aspects such as medical services, diagnoses, treatment, claims, etc. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .msg, .eml, .pptx, .pptm, .ppt, .potx, .potm, .pot, .ppsx, .ppsm, .pps, .ppam, .ppa, .xlsx, .xlsm, .xlsb, .xls, .csv, .xltx, .xltm, .xlt, .xlam, .xla files. | English | Yes |

## Human resources

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects content in human resources related categories of recruitment, interviewing, hiring, training, evaluating, warning, and termination. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .msg, .eml, .pptx, .pptm, .ppt, .potx, .potm, .pot, .ppsx, .ppsm, .pps, .ppam, .ppa, .xlsx, .xlsm, .xlsb, .xls, .csv, .xltx, .xltm, .xlt, .xlam, .xla files. | English | Yes |

## Invoice

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects invoices containing an itemized summary of the purchase, the total balance owed, current payment due, and various payment methods. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .eml, .xlsx, .xlsm, .xlsb, .xls, .csv, .xltx, .xltm, .xlt, .xlam, .xla files. | English | Yes |

## Intellectual property

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects content in intellectual property related categories such as trade secrets and similar confidential information. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .msg, .eml, .pptx, .pptm, .ppt, .potx, .potm, .pot, .ppsx, .ppsm, .pps, .ppam, .ppa, .xlsx, .xlsm, .xlsb, .xls, .csv, .xltx, .xltm, .xlt, .xlam, .xla files. | English | Yes |

## Information technology

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects content in information technology and cybersecurity categories such as network settings, information security, hardware, and software. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .msg, .eml, .pptx, .pptm, .ppt, .potx, .potm, .pot, .ppsx, .ppsm, .pps, .ppam, .ppa, .xlsx, .xlsm, .xlsb, .xls, .csv, .xltx, .xltm, .xlt, .xlam, .xla files. | English | Yes |

## IT infra and network security documents

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Identifies documents that outline rules for computer network access, policy enforcement, and basic architecture of a company's security or network security environment. It also covers documents related to access control, data security, storage policy, and maintenance plans. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .pptx, .pptm, .ppt, .potx, .potm, .pot, .ppsx, .ppsm, .pps, .ppam, .ppa |  |  |
| English | Yes |  |  |

## Lease deeds

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| This classifier is used to identify documents detailing lease information such as period, amount, and agreements. It includes facility, factory, and real estate lease deeds, as well as responsibilities of the lessor and lessee, deposits, due dates, and consequences of lease violations. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .pptx, .pptm, .ppt, .potx, .potm, .pot, .ppsx, .ppsm, .pps, .ppam, .ppa | English | Yes |

## Legal affairs

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects content in legal affairs-related categories such as litigation, legal process, legal obligation, legal terminology, law, and legislation. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .msg, .eml files. | English | Yes |

## Legal agreements

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects various legally binding documents/ contracts/ agreements like Arbitration agreements, Power of Attorney, Purchase Agreements between two parties. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .txt files. | English | Yes |

## Letters of credit

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Identifies documents sent from banks or financial institutions that guarantee a seller will receive a buyer's payment on time and for the full amount. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .pptx, .pptm, .ppt, .potx, .potm, .pot, .ppsx, .ppsm, .pps, .ppam, .ppa, .txt, .one | English | Yes |

## License agreement

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects license agreements, contains terms and conditions for use and compensation for the licensor. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt files. | English | Yes |

## Loan agreements and offer letters

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects loan agreements, offer letters, and terms and conditions contained within the document. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .msg, .eml files. | English | Yes |

## Manufacturing batch records

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects manufacturing batch documents that include details around the entire manufacturing process and the history of a product batch. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .msg, .eml files. | English | Yes |

## Marketing collaterals

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| This classifier is used to identify various marketing materials utilized by organizations for outreach. This includes battle cards, fact sheets, product brochures, product launch materials, press releases, and product catalogs. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .txt | English | Yes |

## Merger and acquisition files

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects documents including letter of intent, term sheets, and related files. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .msg, .eml files. | English | Yes |

## Meeting notes

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects documents and notes containing information specific to meetings. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .msg, .eml, .pptx, .pptm, .ppt, .potx, .potm, .pot, .ppsx, .ppsm, .pps, .ppam, .ppa files. | English | Yes |

## Money laundering

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects signs that suggest money laundering or engagement in acts to conceal or disguise the origin or destination of proceeds. This classifier helps customers manage regulatory compliance obligations such as the Bank Secrecy Act, the USA Patriot Act, FINRA Rule 3310, and Anti-Money Laundering Act of 2020. | Detects content in .msg, .docx, .pdf, .txt, .rtf, .jpeg, .jpg, .png, .gif, .bmp, .svg files. | English | Yes |

Important

This classifier can capture a large volume of bulk sender/newsletter content. In Communication Compliance, you can mitigate the detection of large volumes of bulk sender/newsletter content by selecting the **Filter email blasts** check box when you create the policy. You can also edit an existing Communication Compliance policy to turn on this feature.

## MoU files (Memorandum of understanding)

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Identifies documents related to memoranda of understanding, annexures, corrigenda, and addenda. These documents are typically not legally binding. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .pptx, .pptm, .ppt, .potx, .potm, .pot, .ppsx, .ppsm, .pps, .ppam, .ppa | English | Yes |

## Network design files

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects technical documentation about networks of computers. This includes various components of network, how they're connected, their architecture, how they perform, and where they troubleshoot. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .msg, .eml, .pptx, .pptm, .ppt, .potx, .potm, .pot, .ppsx, .ppsm, .pps, .ppam, .ppa files. | English | Yes |

## Non-disclosure agreement

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects nondisclosure agreements (NDAs). | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt files. | English | Yes |

## OSHA records

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Identifies Occupational Safety and Health Administration (OSHA) recordkeeping forms. This includes the Log of Work-Related Injuries and Illnesses (OSHA Form 300), Summary of Work-Related Injuries and Illnesses (OSHA Form 300A), and the Injury and Illness Incident Report (OSHA Form 301). | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .pptx, .pptm, .ppt, .potx, .potm, .pot, .ppsx, .ppsm, .pps, .ppam, .ppa, .txt, .one | English | Yes |

## Paystub

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects paystub/salary statement files. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .xlsx, .xlsm, .xlsb, .xls, .csv, .xltx, .xltm, .xlt, .xlam, .xla files. | English | Yes |

## Personal financial information

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects documents related to different personal financial records consisting of financial statements, real estate planning, and retirement plans. Consists of details of all assets and liabilities held by an individual. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .txt, .one files. | English | Yes |

## Procurement

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects content in categories of bidding, quoting, purchasing, and paying for supply of goods and services. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .msg, .eml, .xlsx, .xlsm, .xlsb, .xls, .csv, .xltx, .xltm, .xlt, .xlam, .xla files. | English | No |

## Project documents

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects project reports and documents, which include project planning documents, project charter documents and schedules. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .msg, .eml, .pptx, .pptm, .ppt, .potx, .potm, .pot, .ppsx, .ppsm, .pps, .ppam, .ppa files. | English | Yes |

## Profanity

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects a specific category of offensive language text items that contain expressions that embarrass most people. | Detects content in .msg, .docx, .pdf, .txt, .rtf, .jpeg, .jpg, .png, .gif, .bmp, .svg files. | - Arabic - Chinese (Simplified) - Chinese (Traditional) - Dutch - English - French - German - Italian - Korean - Japanese - Portuguese - Spanish | Yes (English) |

## Prompt Shields

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects adversarial user input attacks such as user prompt injection attacks (jailbreak). User prompt injection attacks will deliberately exploit system vulnerabilities to elicit unauthorized behavior from the LLM. | Generative AI prompts | English | No |

Note

This classifier can be configured in Communication Compliance and evaluates generative AI prompts ONLY

## Protected material

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects known text content that may be protected under copyright or branding laws. Detecting the display of protected material in generative AI responses ensures compliance with intellectual property laws and maintains content originality | Generative AI responses | English | No |

Note

This classifier can be configured in Communication Compliance and evaluates generative AI responses ONLY

## Quotation

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects documents that offer to sell goods or services for a set price, based on certain conditions. It contains a description of the goods or services, the price of the goods or rate of the service, the quantity, and a total cost. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .eml, .xlsx, .xlsm, .xlsb, .xls, .csv, .xltx, .xltm, .xlt, .xlam, .xla files. | English | Yes |

## Regulatory collusion

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects messages that can violate regulatory anti-collusion requirements such as an attempted concealment of sensitive information. This classifier can help customers manage regulatory compliance obligations such as the Sherman Antitrust Act, Securities Exchange Act 1933, Securities Exchange Act of 1934, Investment Advisers Act of 1940, Federal Commission Act, and Robinson-Patman Act. | Detects content in .msg, .docx, .pdf, .txt, .rtf, .jpeg, .jpg, .png, .gif, .bmp, .svg files. | English | No |

Important

This classifier can capture a large volume of bulk sender/newsletter content. In Communication Compliance, you can mitigate the detection of large volumes of bulk sender/newsletter content by selecting the **Filter email blasts** check box when you create the policy. You can also edit an existing Communication Compliance policy to turn on this feature.

## Resume

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects a resume document that a job applicant provides an employer, which has a detailed statement of the candidate's prior work experience, education, and accomplishments. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .txt files. | English | Yes |

## Safety records

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects documents that are related to facility/factory safety. These documents can be facility safety plan, safety assessments and audit reports, emergency response and evacuation plan, and equipment’s inspection reports concerning safety measurements. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .pptx, .pptm, .ppt, .potx, .potm, .pot, .ppsx, .ppsm, .pps, .ppam, .ppa, .txt, .one, .eml files. | English | Yes |

## Sales and revenue

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects sales reports, revenue/income statement and sales/demand forecasting reports for organizations. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .pptx, .pptm, .ppt, .potx, .potm, .pot, .ppsx, .ppsm, .pps, .ppam, .ppa files. | English | Yes |

## Software product development files

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects files used in software development; including product requirements document, product testing and planning, files including test cases, and test reports. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .msg, .eml files. | English | Yes |

## Source code

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects items that contain a set of instructions and statements written computer programming languages on GitHub: ActionScript, C, C#, C++, Clojure, CoffeeScript, Go, Haskell, Java, JavaScript, Lua, MATLAB, Objective-C, Perl, PHP, Python, R, Ruby, Scala, Shell, Swift, TeX, Vim Script. | Detects content in .c, .h, .w, .cs, .cake, .csx, .cpp, .c++, .cc, .cp, .cxx, .hh, .hpp, .hxx, .java, .js, .m, .matlab, .pl, .perl, .pm, .prl, .ipb, .php, .php3, .php4, .php5, .py, .pyc, .pyo, .r, .rl, .rb, .irb, .swift, .as, .clj, .cljs, .cljc, .coffee, .Go, .hs, .hsc, .lua, .lub, .m, .mm, .scala, .sca, .Tex,T, .xs, . sh, .vim, .edn, .javac, .lhs, .mjs, .pod, .r, .rda, .RData, .rds, .rb, .bash, .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .eml, .msg, .pptx, .pptm, .ppt, .potx, .potm, .pot, .ppsx, .ppsm, .pps, .ppam, .ppa, .xlsx, .xlsm, .xlsb, .xls, .csv, .xltx, .xltm, .xlt, .xlam, .xla, .sc, .litcoffee files. | N/A | No |

Note

Source code is trained to detect when the bulk of the text is source code. It doesn't detect source code text that is interspersed with plain text.

## Standard operating procedures and manuals

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects sets of documented instructions created to help workers perform routine operations or manufacturing tasks. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt files. | English | Yes |

## Statement of accounts

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| A statement of account is a detailed report of the contents of an account. Identifies documents related to statement of accounts, accounts payable, and accounts receivable. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .xlsx, .xlsm, .xlsb, .xls, .csv, .xltx, .xltm, .xlt, .xlam, .xla files. | English | Yes |

## Statement of work

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects statement of work (SOW) containing details like requirements, responsibilities, terms and conditions for both parties. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt files. | English | Yes |

## Stock manipulation

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects signs of possible stock manipulation, such as recommendations to buy, sell, or hold stocks that can suggest an attempt to manipulate the stock price. This classifier can help customers manage regulatory compliance obligations such as the Securities Exchange Act of 1934, FINRA Rule 2372, and FINRA Rule 5270. | Detects content in .msg, .docx, .pdf, .txt, .rtf, .jpeg, .jpg, .png, .gif, .bmp, .svg files. | English | Yes |

Important

This classifier can capture a large volume of bulk sender/newsletter content. In Communication Compliance, you can mitigate the detection of large volumes of bulk sender/newsletter content by selecting the **Filter email blasts** check box when you create the policy. You can also edit an existing Communication Compliance policy to turn on this feature.

## Tax documents

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects tax related content such as tax planning, tax forms, tax filing, tax regulations. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt, .one, .msg, .eml, .pptx, .pptm, .ppt, .potx, .potm, .pot, .ppsx, .ppsm, .pps, .ppam, .ppa, .xlsx, .xlsm, .xlsb, .xls, .csv, .xltx, .xltm, .xlt, .xlam, xla files. | English | Yes |

## Threat

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects a specific category of offensive language text items related to threats to commit violence or do physical harm or damage to a person or property. | Detects content in .msg, .docx, .pdf, .txt, .rtf, .jpeg, .jpg, .png, .gif, .bmp, .svg files. | - Arabic - Chinese (Simplified) - Chinese (Traditional) - Dutch - English - French - German - Italian - Korean - Japanese - Portuguese - Spanish | Yes (English) |

## Unauthorized disclosure

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Detects sharing of information containing content that is explicitly designated as confidential or internal to unauthorized individuals. This classifier can help customers manage regulatory compliance obligations such as FINRA Rule 2010 and SEC Rule 10b-5. | Detects content in .msg, .docx, .pdf, .txt, .rtf, .jpeg, .jpg, .png, .gif, .bmp, .svg files. | English | Yes |

Important

This classifier can capture a large volume of bulk sender/newsletter content. In Communication Compliance, you can mitigate the detection of large volumes of bulk sender/newsletter content by selecting the **Filter email blasts** check box when you create the policy. You can also edit an existing Communication Compliance policy to turn on this feature.

## Wire transfer

| **Description** | **File types** | **Supported Languages** | **Contextual summary and keyword highlighting summary** |
| --- | --- | --- | --- |
| Wire transfer is a method of electronic funds transfer from one person or entity to another. The model captures all the wire transfer receipts and acknowledgments. | Detects content in .docx, .docm, .doc, .dotx, .dotm, .dot, .pdf, .rtf, .txt files. | English | Yes |

## Word and token count requirements

### Pretrained trainable classifiers for data classification

Pretrained trainable classifiers used for data classification have a default minimum of 200 tokens. For example, the Resume classifier requires at least 200 tokens. Documents below a classifier's minimum token count aren't classified by that classifier.

For languages other than Chinese, Japanese, and Korean, token counts typically match word counts. For Chinese, Japanese, and Korean, the count depends on how the text is tokenized.

The default 200-token minimum doesn't apply to custom trainable classifiers during training or classification.

The following table lists minimum token counts by classifier and language. Other supported classifier and language combinations use the default 200-token minimum.

| Classifier | Minimum token count | Language |
| --- | --- | --- |
| Agreements | 10 | English |
| Bank statement | 100 | English |
| Bank statement | 200 | Chinese (`zh`), French, German, Japanese, Spanish |
| Budget | 100 | English |
| Business plan | 100 | English |
| Construction specifications | 50 | English |
| Employee disciplinary action | 50 | English |
| Employee insurance | 50 | English |
| Employment agreement | 100 | English |
| Finance | 10 | English |
| Financial audit | 50 | English |
| Financial statement | 100 | English |
| Healthcare | 10 | English |
| Human resources | 10 | English |
| Invoice | 100 | English |
| Intellectual property | 30 | English |
| Information technology | 10 | English |
| Legal affairs | 10 | English |
| License agreement | 100 | English |
| Loan agreements and offer letters | 50 | English |
| Manufacturing batch records | 50 | English |
| Merger and acquisition files | 50 | English |
| Meeting notes | 100 | English |
| Network design files | 50 | English |
| Non-disclosure agreement | 100 | English |
| Paystub | 100 | English |
| Procurement | 10 | English |
| Quotation | 100 | English |
| Software product development files | 50 | English |
| Tax documents | 10 | English |

### Communication compliance classifiers

Communication compliance classifiers have separate minimum word count requirements for messages, as listed in the following table. To identify and take action on messages below the listed minimums, create a [custom keyword dictionary](communication-compliance-policies#custom-keyword-dictionaries) for communication compliance policies that detect inappropriate language.

| **Classifier** | **Minimum word count** | **Language** |
| --- | --- | --- |
| Threat, Harassment, and Profanity | Six words | - Dutch - French - German - Italian - Japanese - Portuguese - Spanish |
| Threat, Harassment, and Profanity | 12 words | - Arabic - Chinese Simplified - Chinese Traditional - Korean |
| Threat and Harassment | Three words | English |
| Profanity | Five words | English |
| Corporate sabotage - Customer complaints - Gifts & entertainment - Money laundering - Regulatory collusion - Stock manipulation - Unauthorized disclosure | Six words | English |
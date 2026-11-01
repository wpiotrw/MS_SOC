---
layout: Conceptual
title: Customize a built-in sensitive information type | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-customize-a-built-in-sensitive-information-type
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2026-06-26T00:00:00.0000000Z
audience: Admin
ms.topic: how-to
ms.service: purview
ms.subservice: purview-sensitive-information-types
ms.collection:
- purview-compliance
search.appverid:
- MOE150
- MET150
ms.custom: seo-marvel-apr2020, msecd-doc-authoring-1014
description: Learn how to customize a built-in sensitive information type by modifying its XML rule package to better match your organization's detection needs.
ai-usage: ai-assisted
locale: en-us
document_id: 08e57959-d08f-f5ba-9048-036b501d9627
document_version_independent_id: 08e57959-d08f-f5ba-9048-036b501d9627
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-customize-a-built-in-sensitive-information-type.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-customize-a-built-in-sensitive-information-type
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-customize-a-built-in-sensitive-information-type.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/57eae111-0f3b-497e-be07-450fd1409dea
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/ac8bf8ab-8134-4c9a-9f2e-58b31575b492
platformId: 64abbc34-9543-e282-2753-674659642b77
---

# Customize a built-in sensitive information type | Microsoft Learn

When looking for sensitive information in content, you need to describe that information in what's called a *rule*. Microsoft Purview Data Loss Prevention (DLP) includes rules for the most common sensitive information types (SITs). You can use these rules right away. To use them, you must include them in a policy. You can adjust these built-in rules to meet your organization's specific needs by creating a custom sensitive information type. This topic shows you how to customize the XML file that contains the existing rule collection so you can detect a wider range of potential credit card information.

You can take this example, which modifies the Credit Card Number SIT, and apply this approach to other built-in sensitive information types. For a list of default SITs and XML definitions, see [Sensitive information type entity definitions](sit-sensitive-information-type-entity-definitions).

## Export the XML file of the current rules

To export the XML, you need to [connect to Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell).

1. In the PowerShell, type the following to display your organization's rules on screen. If you haven't created your own, you'll only see the default, built-in rules, labeled "Microsoft Rule Package."

    ```powershell
    Get-DlpSensitiveInformationTypeRulePackage
    ```
2. Store your organization's rules in a variable by typing the following. Storing something in a variable makes it easily available later in a format that works for PowerShell commands.

    ```powershell
    $ruleCollections = Get-DlpSensitiveInformationTypeRulePackage
    ```
3. Make a formatted XML file with all that data by typing the following.

    ```powershell
    [System.IO.File]::WriteAllBytes('C:\custompath\exportedRules.xml', $ruleCollections.SerializedClassificationRuleCollection)
    ```

    Important

    Make sure that you use the file location where your rule pack is actually stored. `C:\custompath\` is a placeholder.

## Find the rule that you want to modify in the XML

The cmdlets above exported the entire *rule collection*, which includes the default rules that Microsoft provides. Next, you'll need to look specifically for the Credit Card Number rule that you want to modify.

1. Use a text editor to open the exported XML file (for example, `exportedRules.xml`) that you created in the preceding procedure.
2. Scroll down to the `<Rules>` tag, which marks the start of the rules section. Because this XML file contains the information for the entire rule collection, it contains other information at the top that you need to scroll past to get to the rules.
3. Look for *Func\_credit\_card* to find the Credit Card Number rule definition. In the XML, rule names can't contain spaces, so the spaces are usually replaced with underscores, and rule names are sometimes abbreviated. An example of this is the U.S. Social Security number rule, which is abbreviated *SSN*. The XML for the Credit Card Number rule should look like the following code sample:

    ```xml
    <Entity id="50842eb7-edc8-4019-85dd-5a5c1f2bb085"
           patternsProximity="300" recommendedConfidence="85">
          <Pattern confidenceLevel="85">
           <IdMatch idRef="Func_credit_card" />
            <Any minMatches="1">
              <Match idRef="Keyword_cc_verification" />
              <Match idRef="Keyword_cc_name" />
              <Match idRef="Func_expiration_date" />
            </Any>
          </Pattern>
        </Entity>
    ```

Now that you have located the Credit Card Number rule definition in the XML, you can customize the rule's XML to meet your needs. For a refresher on the XML definitions, see the Term glossary later in this article.

## Modify the XML and create a new sensitive information type

First, you need to create a new sensitive information type because you can't directly modify the default rules. You can do a wide variety of things with custom sensitive information types, which are outlined in [Create a custom sensitive information type in Security & Compliance PowerShell](sit-create-a-custom-sensitive-information-type-in-scc-powershell). For this example, we'll keep it simple and only remove corroborative evidence and add keywords to the Credit Card Number rule.

All XML rule definitions are built on the following general template. You need to copy and paste the Credit Card Number definition XML in the template, modify some values (notice the ". . ." placeholders in the following example), and then upload the modified XML as a new rule that can be used in policies.

```xml
<?xml version="1.0" encoding="utf-16"?>
<RulePackage xmlns="https://schemas.microsoft.com/office/2011/mce">
  <RulePack id=". . .">
    <Version major="1" minor="0" build="0" revision="0" />
    <Publisher id=". . ." />
    <Details defaultLangCode=". . .">
      <LocalizedDetails langcode=" . . . ">
         <PublisherName>. . .</PublisherName>
         <Name>. . .</Name>
         <Description>. . .</Description>
      </LocalizedDetails>
    </Details>
  </RulePack>

 <Rules>
   <!-- Paste the Credit Card Number rule definition here.-->
      <LocalizedStrings>
         <Resource idRef=". . .">
           <Name default="true" langcode=" . . . ">. . .</Name>
           <Description default="true" langcode=". . ."> . . .</Description>
         </Resource>
      </LocalizedStrings>
   </Rules>
</RulePackage>
```

Now, you have something that looks similar to the following XML. Because rule packages and rules are identified by their unique GUIDs, you need to generate two GUIDs: one for the rule package and one to replace the GUID for the Credit Card Number rule. The GUID for the entity ID in the following code sample is the GUID for the built-in rule definition, which you need to replace with a new GUID. There are several ways to generate GUIDs, but you can do it easily in PowerShell by typing **[guid]::NewGuid()**.

```xml
<?xml version="1.0" encoding="utf-16"?>
<RulePackage xmlns="https://schemas.microsoft.com/office/2011/mce">
  <RulePack id="8aac8390-e99f-4487-8d16-7f0cdee8defc">
    <Version major="1" minor="0" build="0" revision="0" />
    <Publisher id="..." />
    <Details defaultLangCode="en">
      <LocalizedDetails langcode="en">
        <PublisherName>Contoso Ltd.</PublisherName>
        <Name>Financial Information</Name>
        <Description>Modified versions of the Microsoft rule package</Description>
      </LocalizedDetails>
    </Details>
  </RulePack>

 <Rules>
    <Entity id="00aa00aa-bb11-cc22-dd33-44ee44ee44ee"
       patternsProximity="300" recommendedConfidence="85">
      <Pattern confidenceLevel="85">
        <IdMatch idRef="Func_credit_card" />
        <Any minMatches="1">
          <Match idRef="Keyword_cc_verification" />
          <Match idRef="Keyword_cc_name" />
          <Match idRef="Func_expiration_date" />
        </Any>
      </Pattern>
    </Entity>
      <LocalizedStrings>
         <Resource idRef="00aa00aa-bb11-cc22-dd33-44ee44ee44ee">
<!-- This is the GUID for the preceding Credit Card Number entity because the following text is for that Entity. -->
           <Name default="true" langcode="en-us">Modified Credit Card Number</Name>
           <Description default="true" langcode="en-us">Credit Card Number that looks for additional keywords, and another version of Credit Card Number that doesn't require keywords (but has a lower confidence level)</Description>
         </Resource>
      </LocalizedStrings>
   </Rules>
</RulePackage>
```

## Remove the corroborative evidence requirement from a sensitive information type

Now you have a new sensitive information type that you're able to upload to the Microsoft Purview portal. The next step is to make the rule more specific. Modify the rule so that it only looks for a 16-digit number that passes the checksum but that doesn't require additional (corroborative) evidence, such as keywords. To require only a 16-digit number that passes the checksum, remove the part of the XML that looks for corroborative evidence. Corroborative evidence is very helpful in reducing false positives. When detecting credit card numbers, there are usually certain keywords or an expiration date near the credit card number. If you remove that evidence, you should also adjust how confident you are that you found a credit card number by lowering the `confidenceLevel`, which is 85 in the example.

```xml
<Entity id="00aa00aa-bb11-cc22-dd33-44ee44ee44ee" patternsProximity="300"
      <Pattern confidenceLevel="85">
        <IdMatch idRef="Func_credit_card" />
      </Pattern>
    </Entity>
```

## Look for keywords that are specific to your organization

You might want to require corroborative evidence but want different or additional keywords, and perhaps you want to change where to look for that evidence. You can adjust the `patternsProximity` to expand or shrink the window for corroborative evidence around the 16-digit number. To add your own keywords, you must define a keyword list and reference it within your rule. The following XML adds the keywords "company card" and "Contoso card", so that any message that contains those phrases within 150 characters of a credit card number will be identified as a credit card number.

```xml
<Rules>
<! -- Modify the patternsProximity to be "150" rather than "300." -->
    <Entity id="00aa00aa-bb11-cc22-dd33-44ee44ee44ee" patternsProximity="150" recommendedConfidence="85">
      <Pattern confidenceLevel="85">
        <IdMatch idRef="Func_credit_card" />
        <Any minMatches="1">
          <Match idRef="Keyword_cc_verification" />
          <Match idRef="Keyword_cc_name" />
<!-- Add the following XML, which references the keywords at the end of the XML sample. -->
          <Match idRef="My_Additional_Keywords" />
          <Match idRef="Func_expiration_date" />
        </Any>
      </Pattern>
    </Entity>
<!-- Add the following XML, and update the information inside the <Term> tags with the keywords that you want to detect. -->
    <Keyword id="My_Additional_Keywords">
      <Group matchStyle="word">
        <Term caseSensitive="false">company card</Term>
        <Term caseSensitive="false">Contoso card</Term>
      </Group>
    </Keyword>
```

## Upload your rule

Before you begin, make sure you can [connect to Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell).

To upload your rule, you need to do the following.

1. Save it as an .xml file with Unicode encoding. Saving the file with Unicode encoding is important because the rule won't work if the file is saved with a different encoding.
2. [Connect to Security & Compliance PowerShell](/en-us/powershell/exchange/connect-to-scc-powershell).
3. In the PowerShell, type the following.

    ```powershell
    New-DlpSensitiveInformationTypeRulePackage -FileData ([System.IO.File]::ReadAllBytes('C:\custompath\MyNewRulePack.xml'))
    ```

    Important

    Make sure that you use the file location where your rule pack is actually stored. `C:\custompath\` is a placeholder.
4. To confirm, type Y, and then press **Enter**.
5. Verify the display name of your new rule and that it was uploaded, by entering:

    ```powershell
    Get-DlpSensitiveInformationType
    ```

To start using the new rule to detect sensitive information, you need to add the rule to a DLP policy. To learn how to add the rule to a policy, see [Create and Deploy data loss prevention policies](dlp-create-deploy-policy).

## Term glossary

These are the definitions for the terms you encountered during this procedure.

| Term | Definition |
| --- | --- |
| Entity | *Entities* are what we call sensitive information types, such as credit card numbers. Each entity has a unique GUID as its ID. If you copy a GUID and search for it in the XML, you'll find the XML rule definition and all the localized translations of that XML rule. You can also find this definition by locating the GUID for the translation and then searching for that GUID. |
| Functions | The XML file references `Func_credit_card`, which is a function in compiled code. Functions are used to run complex regexes and verify that checksums match for our built-in rules. Because this happens in the code, some of the variables don't appear in the XML file. |
| IdMatch | This is the identifier that the pattern is to trying to match—for example, a credit card number. |
| Keyword lists | The XML file also references `keyword_cc_verification` and `keyword_cc_name`, which are lists of keywords that we are looking to match within the `patternsProximity` for the entity. These aren't currently displayed in the XML. |
| Pattern | The *pattern* contains the list of what the sensitive type is looking for. This includes keywords, regexes, and internal functions, which perform tasks like verifying checksums. Sensitive information types can have multiple patterns with unique confidence levels. This is useful when creating a sensitive information type that returns a high confidence if corroborative evidence is found and a lower confidence if little or no corroborative evidence is found. |
| Pattern confidenceLevel | This is the level of confidence that the DLP engine found a match. This level of confidence is associated with a match for the pattern if the pattern's requirements are met. This is the confidence measure you should consider when using Exchange mail flow rules (also known as transport rules). |
| patternsProximity | When we find what looks like a credit card number pattern, `patternsProximity` is the distance around that number where we'll look for corroborative evidence. |
| recommendedConfidence | This is the confidence level we recommend for this rule. The recommended confidence level applies to entities and affinities. For entities, this number is never evaluated against the `confidenceLevel` for the pattern. It's merely a suggestion to help you choose a confidence level if you want to apply one. For affinities, the `confidenceLevel` of the pattern must be higher than the `recommendedConfidence` number for a mail flow rule action to be invoked. The `recommendedConfidence` is the default confidence level used in mail flow rules that invokes an action. If you want, you can manually change the mail flow rule to be invoked based off the pattern's confidence level, instead. |
|  |  |
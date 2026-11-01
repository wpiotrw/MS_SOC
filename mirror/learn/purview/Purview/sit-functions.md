---
layout: Conceptual
title: Sensitive information type functions | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/purview/sit-functions
breadcrumb_path: /purview/breadcrumb/toc.json
feedback_system: Standard
uhfHeaderId: MSDocsHeader-Purview
f1.keywords:
- NOCSH
ms.author: kreagle
author: k-reagle
manager: laurawi
ms.date: 2023-03-01T00:00:00.0000000Z
audience: Admin
ms.topic: reference
ms.service: purview
ms.subservice: purview-sensitive-information-types
ms.collection:
- purview-compliance
search.appverid:
- MOE150
- MET150
ms.custom:
- seo-marvel-apr2020
recommendations: false
description: Learn what the sensitive information type functions look for.
locale: en-us
document_id: a3c43ca0-e642-52f7-0ead-a9386fab05a4
document_version_independent_id: a3c43ca0-e642-52f7-0ead-a9386fab05a4
original_content_git_url: https://github.com/MicrosoftDocs/Purview-pr/blob/live/Purview/sit-functions.md
site_name: Docs
depot_name: MSDN.Purview
page_type: conceptual
toc_rel: toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: sit-functions
moniker_range_name: 
monikers: []
item_type: Content
source_path: Purview/sit-functions.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: 40fd256a-e4cf-4ae3-0f91-073ed487b243
---

# Sensitive information type functions | Microsoft Learn

Sensitive information types (SIT) can use functions as primary elements for identifying sensitive items. For example, the Credit Card Number SIT uses the Func\_credit\_card function to detect credit card number.

This article explains what these functions look for, so you can better understand how the predefined sensitive information types work. For more information, see [Sensitive information type entity definitions](sit-sensitive-information-type-entity-definitions)

## Table of functions

| Function name | Function action | Is a validator |
| --- | --- | --- |
| Func\_aba\_routing | detects ABA routing number | yes |
| Func\_alabama\_drivers\_license\_number | detects Alabama driver's license number | no |
| Func\_alaska\_delaware\_oregon\_drivers\_license\_number | detects Alaska, Delaware, Oregon driver's license number | no |
| Func\_alaska\_drivers\_license\_number | detects Alaska driver's license number | no |
| Func\_alberta\_drivers\_license\_number | detects Alberta driver's license number | no |
| Func\_argentina\_Unique\_Tax\_Key | detects and validates Argentina Unique tax key | no |
| Func\_Argentina\_Unique\_Tax\_Key | detects Argentina Unique tax key | no |
| Func\_arizona\_drivers\_license\_number | detects Arizona driver's license number | no |
| Func\_arkansas\_drivers\_license\_number | detects Arkansas driver's license number | no |
| Func\_australian\_business\_number | detects Australia business number | no |
| Func\_Australian\_Company\_Number | detects Australia company number | no |
| Func\_australian\_medical\_account\_number | detects Australia medical account number | no |
| Func\_australian\_tax\_file\_number | detects Australia tax file number | yes |
| Func\_austria\_eu\_ssn\_or\_equivalent | detects Austria social security number | no |
| Func\_austria\_eu\_tax\_file\_number | detects Austria tax file number | no |
| Func\_Austria\_Value\_Added\_Tax | detects Austria Value Added Tax | no |
| Func\_belgium\_national\_number | detects Belgium national number | no |
| Func\_belgium\_value\_added\_tax\_number | detects Belgium value added tax number | no |
| Func\_brazil\_cnpj | detects Brazil legal entity number (CNPJ) | yes |
| Func\_brazil\_cpf | detects Brazil CPF | yes |
| Func\_brazil\_rg | detects Brazil RG | no |
| Func\_british\_columbia\_drivers\_license\_number | detects British Columbia driver's license number | no |
| Func\_bulgaria\_eu\_national\_id\_card | detects Bulgaria uniform civil number | no |
| Func\_california\_drivers\_license\_number | detects California driver's license number | no |
| Func\_canadian\_sin | detects Canada sin | yes |
| Func\_chile\_id\_card | detects Chile ID card | no |
| Func\_china\_resident\_id | detects China-resident ID | no |
| Func\_colorado\_drivers\_license\_number | detects Colorado driver's license number | no |
| Func\_connecticut\_drivers\_license\_number | detects Connecticut driver's license number | no |
| Func\_credit\_card | detects credit card | yes |
| Func\_croatia\_id\_card | detects Croatia ID card | no |
| Func\_croatia\_oib\_number | detects Croatia OIB number | no |
| Func\_cyprus\_eu\_tax\_file\_number | detects Cyprus tax file number | no |
| Func\_czech\_id\_card\_new\_format | detects Czech ID card in new format | no |
| Func\_czech\_id\_card | detects Czech ID card | no |
| Func\_dea\_number | detects DEA number | yes |
| Func\_denmark\_eu\_tax\_file\_number | detects Denmark personal identification number | no |
| Func\_district\_of\_columbia\_drivers\_license\_number | detects District of Columbia driver's license number | no |
| Func\_estonia\_eu\_national\_id\_card | detects Estonia Personal Identification Code | no |
| Func\_eu\_debit\_card | detects EU debit card | no |
| Func\_finnish\_national\_id | detects Finnish national ID | no |
| Func\_florida\_drivers\_license\_number | detects Florida driver's license number | no |
| Func\_florida\_maryland\_michigan\_minnesota\_drivers\_license\_number | detects Florida, Maryland, Michigan, Minnesota driver's license number | no |
| Func\_formatted\_itin | detects formatted US ITIN | yes |
| Func\_fr\_insee | detects France INSEE | no |
| Func\_fr\_passport | detects France passport | no |
| Func\_france\_eu\_tax\_file\_number | detects France tax file number | no |
| Func\_france\_value\_added\_tax\_number | detects France value added tax number | no |
| Func\_french\_drivers\_license | detects French driver's license | no |
| Func\_french\_insee | detects French INSEE | no |
| Func\_georgia\_drivers\_license\_number | detects Georgia driver's license number | no |
| Func\_german\_drivers\_license | detects Germany driver's license | no |
| Func\_german\_passport\_data | detects Germany passport | no |
| Func\_german\_passport | detects Germany passport | no |
| Func\_germany\_eu\_tax\_file\_number | detects Germany tax file number | no |
| Func\_germany\_value\_added\_tax\_number | detects Germany value added tax number | no |
| Func\_greece\_eu\_ssn | detects Greece sin (AMKA) | no |
| Func\_hawaii\_drivers\_license\_number | detects Hawaii driver's license number | no |
| Func\_hong\_kong\_id\_card | detects Hong Kong ID card | no |
| Func\_hungarian\_value\_added\_tax\_number | detects Hungary value added tax number | no |
| Func\_hungary\_eu\_national\_id\_card | detects Hungary personal identification number | no |
| Func\_hungary\_eu\_ssn\_or\_equivalent | detects Hungary social security number | no |
| Func\_hungary\_eu\_tax\_file\_number | detects Hungary tax file number | no |
| Func\_iban | detects IBAN | yes |
| Func\_idaho\_drivers\_license\_number | detects Idaho driver's license number | no |
| Func\_illinois\_drivers\_license\_number | detects Illinois driver's license number | no |
| Func\_india\_aadhaar | detects India aadhaar | yes |
| Func\_indiana\_drivers\_license\_number | detects Indiana driver's license number | no |
| Func\_iowa\_drivers\_license\_number | detects Iowa driver's license number | no |
| Func\_ireland\_pps | detects Ireland PPS | no |
| Func\_israeli\_national\_id\_number | detects Israel national ID number | no |
| Func\_italy\_eu\_national\_id\_card | detects Italy fiscal code | no |
| Func\_italy\_value\_added\_tax\_number | detects Italy value added tax number | no |
| Func\_japanese\_my\_number\_corporate | detects Japan my number corporate | yes |
| Func\_japanese\_my\_number\_personal | detects Japan my number personal | yes |
| Func\_jp\_bank\_account\_branch\_code | detects Japan bank account branch code | no |
| Func\_jp\_bank\_account | detects Japan bank account | no |
| Func\_jp\_drivers\_license\_number | detects Japan driver's license number | no |
| Func\_jp\_passport | detects Japan passport | no |
| Func\_jp\_resident\_registration\_number | detects Japan-resident registration number | no |
| Func\_jp\_sin\_pre\_1997 | detects Japan sin pre 1997 | no |
| Func\_jp\_sin | detects Japan SIN | no |
| Func\_kansas\_drivers\_license\_number | detects Kansas driver's license number | no |
| Func\_kentucky\_drivers\_license\_number | detects Kentucky driver's license number | no |
| Func\_kentucky\_massachusetts\_virginia\_drivers\_license\_number | detects Kentucky, Massachusetts, Virginia driver's license number | no |
| Func\_latvia\_eu\_national\_id\_card | detects Latvia personal code | no |
| Func\_lithuania\_eu\_tax\_file\_number | detects Lithuania personal code | no |
| Func\_louisiana\_drivers\_license\_number | detects Louisiana driver's license number | no |
| Func\_luxemburg\_eu\_tax\_file\_number\_non\_natural | detects Luxemburg national identification number (non-natural persons) | no |
| Func\_luxemburg\_eu\_tax\_file\_number | detects Luxemburg national identification number (natural persons) | no |
| Func\_maine\_drivers\_license\_number | detects Maine driver's license number | no |
| Func\_manitoba\_drivers\_license\_number | detects Manitoba driver's license number | no |
| Func\_maryland\_drivers\_license\_number | detects Maryland driver's license number | no |
| Func\_massachusetts\_drivers\_license\_number | detects Massachusetts driver's license number | no |
| Func\_mexico\_population\_registry\_code | detects Mexico population registry code | no |
| Func\_michigan\_minnesota\_drivers\_license\_number | detects Michigan, Minnesota driver's license number | no |
| Func\_minnesota\_drivers\_license\_number | detects Minnesota driver's license number | no |
| Func\_mississippi\_oklahoma\_drivers\_license\_number | detects Mississippi, Oklahoma driver's license number | no |
| Func\_missouri\_drivers\_license\_number | detects Missouri driver's license number | no |
| Func\_montana\_drivers\_license\_number | detects Montana driver's license number | no |
| Func\_nebraska\_drivers\_license\_number | detects Nebraska driver's license number | no |
| Func\_netherlands\_bsn | detects Netherlands BSN | no |
| Func\_netherlands\_eu\_tax\_file\_number | detects Netherlands tax file number | no |
| Func\_netherlands\_value\_added\_tax\_number | detects Netherlands value added tax number | no |
| Func\_nevada\_drivers\_license\_number | detects Nevada driver's license number | no |
| Func\_new\_brunswick\_drivers\_license\_number | detects New Brunswick driver's license number | no |
| Func\_new\_hampshire\_drivers\_license\_number | detects New Hampshire driver's license number | no |
| Func\_new\_jersey\_drivers\_license\_number | detects New Jersey driver's license number | no |
| Func\_new\_mexico\_drivers\_license\_number | detects New Mexico driver's license number | no |
| Func\_new\_york\_drivers\_license\_number | detects New York driver's license number | no |
| Func\_new\_zealand\_bank\_account\_number | detects New Zealand bank account number | no |
| Func\_new\_zealand\_inland\_revenue\_number | detects New Zealand inland revenue number | no |
| Func\_new\_zealand\_ministry\_of\_health\_number | detects New Zealand ministry of health number | no |
| Func\_newfoundland\_labrador\_drivers\_license\_number | detects Newfoundland and Labrador driver's license number | no |
| Func\_newzealand\_driver\_license\_number | detects New Zealand driver license number | no |
| Func\_newzealand\_social\_welfare\_number | detects New Zealand social welfare number | no |
| Func\_north\_carolina\_drivers\_license\_number | detects North Carolina driver's license number | no |
| Func\_north\_dakota\_drivers\_license\_number | detects North Dakota driver's license number | no |
| Func\_norway\_id\_number | detects Norway ID number | no |
| Func\_nova\_scotia\_drivers\_license\_number | detects Nova Scotia driver's license number | no |
| Func\_ohio\_drivers\_license\_number | detects Ohio driver's license number | no |
| Func\_ontario\_drivers\_license\_number | detects Ontario driver's license number | no |
| Func\_pennsylvania\_drivers\_license\_number | detects Pennsylvania driver's license number | no |
| Func\_pesel\_identification\_number | detects Poland National ID (PESEL) | no |
| Func\_poland\_eu\_tax\_file\_number | detects Poland tax file number | no |
| Func\_polish\_national\_id | detects Poland identity card | no |
| Func\_polish\_passport\_number | detects Polish passport number | no |
| Func\_polish\_regon\_number | detects Polish REGON number | no |
| Func\_portugal\_eu\_tax\_file\_number | detects Portugal Tax Identification Number | no |
| Func\_prince\_edward\_island\_drivers\_license\_number | detects Prince Edward Island driver's license number | no |
| Func\_quebec\_drivers\_license\_number | detects Quebec driver's license number | no |
| Func\_randomized\_formatted\_ssn | detects randomized formatted US SSN | yes |
| Func\_randomized\_unformatted\_ssn | detects randomized unformatted US SSN | yes |
| Func\_rhode\_island\_drivers\_license\_number | detects Rhode Island driver's license number | no |
| Func\_romania\_eu\_national\_id\_card | detects Romania personal numeric code (CNP) | no |
| Func\_saskatchewan\_drivers\_license\_number | detects Saskatchewan driver's license number | no |
| Func\_slovakia\_eu\_national\_id\_card | detects Slovakia personal number | no |
| Func\_slovenia\_eu\_national\_id\_card | detects Slovenia Unique Master Citizen Number | no |
| Func\_slovenia\_eu\_tax\_file\_number | detects Slovenia tax file number | no |
| Func\_south\_africa\_identification\_number | detects South Africa identification number | yes |
| Func\_south\_carolina\_drivers\_license\_number | detects South Carolina driver's license number | no |
| Func\_south\_dakota\_drivers\_license\_number | detects South Dakota driver's license number | no |
| Func\_south\_korea\_resident\_number | detects South Korea resident number | no |
| Func\_spain\_eu\_DL\_and\_NI\_number\_citizen | detects Spain DL and NI number citizen | no |
| Func\_spain\_eu\_DL\_and\_NI\_number\_foreigner | detects Spain DL and NI number foreigner | no |
| Func\_spain\_eu\_driver's\_license\_number | detects Spain driver's license number | no |
| Func\_spain\_eu\_tax\_file\_number | detects Spain tax file number | no |
| Func\_spanish\_social\_security\_number | detects Spanish social security number | no |
| Func\_ssn | Function to detect non-randomized formatted US SSN | yes |
| Func\_sweden\_eu\_tax\_file\_number | detects Sweden tax file number | no |
| Func\_swedish\_national\_identifier | detects Swedish national identifier | yes |
| Func\_swiss\_social\_security\_number\_ahv | detects Swiss social security number AHV | no |
| Func\_taiwanese\_national\_id | detects Taiwanese national ID | no |
| Func\_tennessee\_drivers\_license\_number | detects Tennessee driver's license number | no |
| Func\_texas\_drivers\_license\_number | detects Texas driver's license number | no |
| Func\_Thai\_Citizen\_Id | detects Thai Citizen ID | no |
| Func\_Turkish\_National\_Id | detects Turkish National ID | yes |
| Func\_uk\_drivers\_license | detects UK driver's license | no |
| Func\_uk\_eu\_tax\_file\_number | detects UK unique taxpayer number | no |
| Func\_uk\_nhs\_number | detects UK NHS number | yes |
| Func\_uk\_nino | detects UK NINO | no |
| Func\_unformatted\_canadian\_sin | detects unformatted Canadian SIN | no |
| Func\_unformatted\_itin | detects unformatted US ITIN | yes |
| Func\_unformatted\_ssn | detects non-randomized unformatted US SSN | yes |
| Func\_usa\_uk\_passport | detects USA and UK passport | yes |
| Func\_utah\_drivers\_license\_number | detects Utah driver's license number | no |
| Func\_vermont\_drivers\_license\_number | detects Vermont driver's license number | no |
| Func\_virginia\_drivers\_license\_number | detects Virginia driver's license number | no |
| Func\_washington\_drivers\_license\_number | detects Washington driver's license number | no |
| Func\_west\_virginia\_drivers\_license\_number | detects West Virginia driver's license number | no |
| Func\_wisconsin\_drivers\_license\_number | detects Wisconsin driver's license number | no |
| Func\_wyoming\_drivers\_license\_number | detects Wyoming driver's license number | no |

## Func\_us\_date

Func\_us\_date looks for dates in common U.S. formats. The common formats are "month/day/year", "month-day-year", and "month day year ". The names or abbreviations of months aren't case-sensitive.

Examples:

- December 2, 2016
- Dec 2, 2016
- dec 02 2016
- 12/2/2016
- 12/02/16
- Dec-2-2016
- 12-2-16

Accepted month names:

- English
    - January, February, march, April, may, June, July, August, September, October, November, December
    - Jan. Feb. Mar. Apr. May June July Aug. Sept. Oct. Nov. Dec.

## Func\_eu\_date

Fund\_eu\_dates looks for dates in common E.U. formats (and most places outside the U.S.), such as "day/month/year", "day-month-year", and "day month year". The names or abbreviations of months aren't case-sensitive.

Examples:

- 2 Dec 2016
- 02 dec 2016
- 2 Dec 16
- 2/12/2016
- 02/12/16
- 2-Dec-2016
- 2-12-16

Accepted month names:

- English
    - January, February, march, April, may, June, July, August, September, October, November, December
    - Jan. Feb. Mar. Apr. May June July Aug. Sept. Oct. Nov. Dec.
- Dutch
    - januari, februari, maart, April, mei, juni, juli, augustus, September, ocktober, October, November, December
    - jan feb maart apr mei jun jul aug sep sept oct okt nov dec
- French
    - janvier, février, mars, avril, mai, juin juillet, août, septembre, octobre, novembre, décembre
    - janv. févr. mars avril mai juin juil. août sept. oct. nov. déc.
- German
    - jänuar, februar, märz, April, mai, juni juli, August, September, oktober, November, dezember
    - Jan./Jän. Feb. März Apr. Mai Juni Juli Aug. Sept. Okt. Nov. Dez.
- Italian
    - gennaio, febbraio, marzo, aprile, maggio, giugno, luglio, agosto, settembre, ottobre, novembre, dicembre
    - genn. febbr. mar. apr. magg. giugno luglio ag. sett. ott. nov. dic.
- Portuguese
    - janeiro, fevereiro, março, marco, abril, maio, junho, julho, agosto, setembro, outubro, novembro, dezembro
    - jan fev mar abr mai jun jul ago set out nov dez
- Spanish
    - enero, febrero, marzo, abril, mayo, junio, julio, agosto, septiembre, octubre, noviembre, diciembre
    - enero feb. marzo abr. mayo jun. jul. agosto sept./set. oct. nov. dic.

## Func\_eu\_date1 (deprecated)

Note

This function is deprecated because it supports only Portuguese month names, which are now included in the `Func_eu_date` function above.

This function looks for a date in the format commonly used in Portuguese. The format for this function is the same as `Func_eu_date`, differing only in the language used.

Examples:

- 2 Dez 2016
- 02 dez 2016
- 2 Dez 16
- 2/12/2016
- 02/12/16
- 2-Dez-2016
- 2-12-16

Accepted month names:

- Portuguese
    - janeiro, fevereiro, março, marco, abril, maio, junho, julho, agosto, setembro, outubro, novembro, dezembro
    - jan fev mar abr mai jun jul ago set out nov dez

## Func\_eu\_date2 (deprecated)

Note

This function is deprecated because it supports only Dutch month names, which are now included in the `Func_eu_date` function above.

This function looks for a date in the format commonly used in Dutch. The format for this function is the same as `Func_eu_date`, differing only in the language used.

Examples:

- 2 Mei 2016
- 02 mei 2016
- 2 Mei 16
- 2/12/2016
- 02/12/16
- 2-Mei-2016
- 2-12-16

Accepted month names:

- Dutch
    - januari, februari, maart, April, mei, juni, juli, augustus, September, ocktober, October, November, December
    - jan feb maart apr mei jun jul aug sep sept out okt nov dec

## Func\_expiration\_date

Func\_expiration\_date looks for dates that are in formats commonly used by credit and debit cards. This function will match dates in format of "month/year", "month-year", "[month name] year", and "[month abbreviation] year". The names or abbreviations of months aren't case-sensitive.

Examples:

- MM/YY -- for example, 01/11 or 1/11
- MM/YYYY -- for example, 01/2011 or 1/2011
- MM-YY -- for example, 01-22 or 1-11
- MM-YYYY -- for example, 01-2000 or 1-2000

The following formats support YY or YYYY:

- Month-YYYY -- for example Jan-2010 or january-2010 or Jan-10 or january-10
- Month YYYY -- for example, 'january 2010' or 'Jan 2010' or 'january 10' or 'Jan 10'
- MonthYYYY -- for example, 'january2010' or 'Jan2010' or 'january10' or 'Jan10'
- Month/YYYY -- for example, 'january/2010' or 'Jan/2010' or 'january/10' or 'Jan/10'

Accepted month names:

- English
    - January, February, march, April, may, June, July, August, September, October, November, December
    - Jan Feb Mar Apr May June July Aug Sept Oct Nov Dec

## Func\_us\_address

Func\_us\_address looks for a U.S. state name or postal abbreviation followed by a valid zip code. The zip code must be one of the correct zip codes associated with the U.S. state name or abbreviation. The U.S. state name and zip code can't be separated by punctuation or letters.

Examples:

- Washington 98052
- Washington 98052-9998
- WA 98052
- WA 98052-9998
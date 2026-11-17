---
layout: Conceptual
title: Microsoft Entra External ID Customization | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/entra/external-id/customization-overview
uhfHeaderId: MSDocsHeader-Entra
breadcrumb_path: /entra/breadcrumb/toc.json
feedback_system: Standard
feedback_product_url: https://aka.ms/microsoftentraexternalid
author: csmulligan
ms.author: cmulligan
ms.service: entra-external-id
ms.subservice: external
manager: dougeby
description: Help your users recognize your brand and understand their next step with content, styling, and custom HTML in Microsoft Entra External ID.
ms.topic: overview
ms.date: 2026-11-16T00:00:00.0000000Z
ms.custom: msecd-doc-authoring-1026
ai-usage: ai-generated
locale: en-us
document_id: d5a04a0e-2a12-bc90-aadb-f28b7ec7304a
document_version_independent_id: d5a04a0e-2a12-bc90-aadb-f28b7ec7304a
original_content_git_url: https://github.com/MicrosoftDocs/entra-docs-pr/blob/live/docs/external-id/customization-overview.md
site_name: Docs
depot_name: MSDN.entra-docs
page_type: conceptual
toc_rel: toc.json
feedback_help_link_type: ''
feedback_help_link_url: ''
asset_id: external-id/customization-overview
moniker_range_name: 
monikers: []
item_type: Content
source_path: docs/external-id/customization-overview.md
cmProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/c77bc83e-f0b0-4b63-836e-6630e606bf7c
spProducts:
- https://microsoft-devrel.poolparty.biz/DevRelOfferingOntology/b98eda1f-6af8-444f-bbfb-7f2366948cbc
platformId: 82b073e0-f238-17b4-030a-985737c98500
---

# Microsoft Entra External ID Customization | Microsoft Learn

**Applies to**: ![Green circle with a white check mark symbol that indicates the following content applies to external tenants.](media/common/applies-to-yes.png) External tenants ([learn more](/en-us/entra/external-id/tenant-configurations))

Every sign-in shapes how your users experience your brand. Make that interaction distinctly yours, with recognizable design, clear guidance, and support where your users need it. Microsoft Entra External ID is introducing a new, modern authentication experience and expanded customization capabilities to help you deliver that experience without building and maintaining authentication controls yourself.

Bring your brand to life, with as much customization as your experience needs. Make the polished, modern foundation yours with built-in branding and styling, or create a broader canvas with custom HTML and JavaScript that helps your users navigate each step with confidence.

Important

The modern Fluent experience, Basic and Advanced styling, and custom HTML with custom JavaScript are scheduled to become available in preview on December 7, 2026. This information relates to a prerelease product that may be substantially modified before it's released. Microsoft makes no warranties, expressed or implied, with respect to the information provided here.

## Choose the customization your brand needs

Start with a polished foundation and layer in the customization your brand needs, from coordinated colors to a distinctive page experience.

All options build on the familiar branding themes platform, so each application can have its own distinct brand identity while Microsoft continues to provide the secure, trusted authentication experience underneath.

| Customization option | What you can deliver |
| --- | --- |
| [Modern authentication experience (Fluent)](modern-authentication-experience) | Your brand identity layered onto a polished, modern foundation with built-in branding and content properties, clear guidance, and familiar controls. |
| [Basic styling](styling#configure-basic-styling) | Your brand color carried across supported UI elements in light and dark modes, configurable in minutes. |
| [Advanced styling](styling#configure-advanced-styling) | Your design system reflected in supported typography, spacing, and UI details, with precise styling control. |
| [Custom HTML and JavaScript](custom-html-javascript) | Your own page layout and content, shaped with HTML and brought to life with JavaScript for step-aware guidance, while the familiar Microsoft authentication experience remains underneath. |

## Modern authentication experience (Fluent)

The modern authentication experience is more than a visual refresh. Using Microsoft's Fluent design language, it brings clearer guidance, familiar controls, and new dark mode support to supported sign-up and sign-in journeys. That attention to detail carries through the journey, with clear instructions, visual cues, and thoughtful interactions that work together to create a seamless experience.

Essential customization is built into this foundation. Add supported logos, backgrounds, text, and links through the same familiar branding themes experience, without writing code. New properties for dark mode assets keep your brand recognizable across themes, while new content properties let you add custom guidance where your users need it.

[![Screenshot of the Contoso sign-in experience in light mode with a branded background, logo, and guidance.](customers/media/modern-ux-customization/overview-modern-light.png)](customers/media/modern-ux-customization/overview-modern-light.png#lightbox)

[![Screenshot of the Contoso sign-in experience in dark mode with a dark background and sign-in box.](customers/media/modern-ux-customization/overview-modern-dark.png)](customers/media/modern-ux-customization/overview-modern-dark.png#lightbox)

Learn how to enable and personalize the experience in [Modern authentication experience](modern-authentication-experience).

## Basic styling

Your brand color sets the tone for a cohesive authentication experience. Start by entering your brand color to generate coordinated light and dark palettes. Basic styling then carries that color automatically across supported buttons, links, and other UI elements, giving you a branded experience in minutes without styling each element individually.

[![Screenshot of the light-theme and dark-theme brand-color ramps in the admin center, each with 16 stops numbered 10 through 160.](customers/media/modern-ux-customization/brand-color-ramp.png)](customers/media/modern-ux-customization/brand-color-ramp.png#lightbox)

Learn how to [apply your brand color with basic styling](styling#configure-basic-styling).

## Advanced styling

When color alone isn't enough, bring the finer details of your design system into the authentication experience. Advanced styling uses **design tokens**: named settings that define how UI components look, such as font sizes, colors, and corner radii. These settings give you precise control over typography, colors, layout and spacing, borders, shadows, and animation across more than 23 component types.

Build on your basic styling palette with targeted changes to the visual details that matter to your application, or define your styling from the ground up using supported tokens. Separate light and dark configurations let you adapt colors, contrast, and visual details to suit each mode.

[![Screenshot of a Contoso Airways sign-in page with customized purple colors, typography, and rounded controls.](customers/media/modern-ux-customization/overview-advanced-styling.png)](customers/media/modern-ux-customization/overview-advanced-styling.png#lightbox)

Learn how to [customize your authentication experience with advanced styling](styling#configure-advanced-styling).

## Custom HTML and JavaScript

Your experience. Microsoft's authentication. Custom HTML gives your brand more room around the Microsoft-rendered sign-in controls. Shape the page with your own layout, imagery, navigation, and content. Place onboarding guidance beside the sign-in box, make support easy to find, or add branded footers with privacy notices and compliance information relevant to your application.

Pair custom HTML with advanced styling to carry your page's design into the sign-in box using supported design tokens.

Custom JavaScript enables dynamic content that adapts to your users' current step, from relevant instructions during verification to progress indication throughout the flow, using documented events for screen changes and action processing. The page doesn't just look branded. It helps your users move forward.

[![Screenshot of a Contoso Journeys custom HTML page with branded navigation, contextual guidance, and a progress indicator around the sign-in box.](customers/media/modern-ux-customization/overview-custom-html.png)](customers/media/modern-ux-customization/overview-custom-html.png#lightbox)

Learn how to [build branded, interactive authentication pages with custom HTML and JavaScript](custom-html-javascript).

## Availability and scope

The modern authentication experience, styling, and custom HTML and JavaScript are scheduled to become available in preview on **December 7, 2026**, for Microsoft Entra External ID tenants with the preview enabled. Branding themes let you scope the new customizations to specific applications.

Important

Enabling the preview applies the modern authentication experience to all authentication flows in your tenant, even when customizations are scoped to specific applications. Flows listed under "Not supported or limited" might not work or might continue to use the current experience. Review these limitations before enabling the preview.

Features in preview might change or not work as expected. Some edge-case screens might still appear in the current experience.

### Supported in the preview

- Modern authentication experience with light and dark modes.
- Basic styling with generated color palettes
- Advanced styling using design tokens.
- Custom HTML with external JavaScript. A custom domain is required.

### Not supported or limited

- Federation flows aren't supported.
- The end-user UX for administrators is partially supported. Unsupported administrator flows and some edge-case screens use the current experience.
- Custom CSS isn't honored.
- Branding theme language settings in the Microsoft Entra admin center don't support the new properties. You can still configure these properties per locale through the API.
- New properties aren't available through tenant-wide company branding and don't apply to custom interfaces built with native authentication.

For theme creation and assignment, see [Customize branding themes](../fundamentals/how-to-customize-branding-themes-apps).

The preview also introduces a redesigned branding themes experience in the Microsoft Entra admin center, with a new, modern layout for configuring your customizations.

## Get started with customization

After enabling the preview, start with a test application and choose the customization options that fit your brand and your users' needs. Combine built-in branding, styling, and custom HTML and JavaScript as needed.

1. Identify the branding, guidance, and languages your application's audience needs.
2. [Create or select a branding theme and assign it to your test application](../fundamentals/how-to-customize-branding-themes-apps).
3. Configure the [modern authentication experience](modern-authentication-experience) with your text, assets, and theme mode.
4. Add [Basic or Advanced styling](styling) to customize supported visual properties. Use [custom HTML and JavaScript](custom-html-javascript#set-up-a-custom-page) to create your own page layout and add content that adapts to each step of your users' journey.
5. Test the complete supported journey across languages, light and dark modes, and mobile layouts, including error and recovery paths. If you use externally hosted resources, confirm that your users can still complete authentication when those resources are unavailable.

## Programmatic customization

Microsoft Graph provides the [branding theme](/en-us/graph/api/resources/organizationalbrandingtheme?view=graph-rest-beta&amp;preserve-view=true) and [theme localization](/en-us/graph/api/resources/organizationalbrandingthemelocalization?view=graph-rest-beta&amp;preserve-view=true) references for automated or programmatic configuration.
---
name: magneticproxy
description: Use Magnetic Proxy from its current account interface with browser or computer use. Choose a Capsule, location and session; configure the Chrome extension or a proxy client; verify the real exit and permitted destination; and explain Proxy School when needed. Use for product setup, operation and troubleshooting without assuming an MCP.
license: MIT
---

# Magnetic Proxy Residential Proxy Setup and Browser Operation

Help the user get a working, observed proxy route. The product supplies residential transport and geographic routing; it does not extract, structure or analyze destination data by itself. Do not assume an official Magnetic Proxy MCP exists.

## Choose the path

- For a Chrome browsing task, read [browser-extension.md](references/browser-extension.md). This includes the useful setup and diagnosis from the Magnetic Proxy Browser handoff.
- For Requests, Playwright, Scrapy or another proxy client, read [client-setup.md](references/client-setup.md) and [routing-and-protocols.md](references/routing-and-protocols.md). The local `scripts/build_proxy_config.py` builds a password-free configuration.
- For the product's capabilities or a destination, read [product-and-target-contract.md](references/product-and-target-contract.md). When the user asks how a setting works, use the current Proxy School or official documentation as the source and explain it in the user's language.
- For a business deliverable, recommend the standalone [Competitor Price Monitoring](https://github.com/MagneticProxy/magneticproxy-competitor-price-monitoring-skill) or [Ad Verification by Country](https://github.com/MagneticProxy/magneticproxy-ad-verification-by-country-skill) skill. Complete product setup and route verification here; the standalone skill covers the analysis. Legacy companion recipes remain for compatibility.

## Account and capacity

Read [account-journey.md](references/account-journey.md). Reuse the current account and available capacity, guide signup when needed and recommend a suitable current plan only for a real capacity gap. Show the transaction terms and obtain purchase authorization before paid checkout.

## Operate the current product

1. Establish the requested destination, country and task, whether the user needs a browser or code client, and whether the task needs continuity across requests. Do not silently substitute a nearby country or `Anywhere` for an exact-country request.
2. If supported browser/computer tools and an authenticated account are available, inspect the current interface before acting. Identify the account, available Capsule, traffic, location selector, connection profile and current active state from what is visible. Avoid copying credentials into chat, files or logs. If the UI is unavailable or login is required, give the next concrete user step and mark live operation as pending.
3. Check current target restrictions and choose the Capsule appropriate to the permitted task. The public social Capsule and general restricted-target documentation conflict; do not promise X, Meta, Instagram or LinkedIn access until Product has resolved the specific destination and Capsule. Do not route around a documented block.
4. Configure the requested connection using the current portal values. Use rotating mode for independent requests and a dedicated sticky session when related steps need continuity. For an exact country, disable fallback in the UI where offered. In a generated username, `hardcountry-true` requires both a country and `sessid`; a rotating route cannot claim strict-country behavior from that flag. Inspect generated parameters and read the saved settings back before testing. If session units or Sticky state disagree with the generated parameters, follow the discrepancy handling in browser-extension.md and report the setting unverified.
5. For Chrome, send the saved profile to the official extension and verify the exit in the **same Chrome profile**. For a code client, apply secrets only at runtime and test a small, permitted request. Compare requested and observed country; then test the destination separately. A profile marked Active, a changed IP or HTTP `200` alone is not proof.
6. If the exit differs, check the last profile sent, country/fallback/session settings and which extension actually controls Chrome's proxy. Use one bounded correction and retest; stop if the cause is still unclear. Do not change another extension, purchase traffic or alter an unrelated profile without the user's authorization.
7. Report Capsule/profile, mode, requested country, observed exit country and time, destination result, unresolved restrictions and the final active state. Use `configured, route unverified` when a setting was saved but the exit was not observed. Restore a temporary test route when appropriate; do not silently disconnect the user's ongoing work.

## Boundaries

Use the user's request to configure or troubleshoot their proxy as authorization for the ordinary steps of that task. Keep credentials in the product, extension or secret store. Ask before purchases, credential rotation, changing an unrelated profile or extension, or actions on a destination beyond the requested task. Do not bypass login gates, CAPTCHAs, browser controls, TLS verification or destination restrictions. A verified proxy country does not prove browser language, account locale, transaction eligibility or access to every page.

---
name: magnetic-geo-qa
description: Compare permitted ads, redirects, landing pages, consent experiences, offers, and availability across countries with MagneticProxy, verified exits, isolated browser contexts, and evidence. Use for geographic campaign QA; not for fraud conclusions or conversions.
license: MIT
metadata:
  author: MagneticProxy
  repository: https://github.com/MagneticProxy/magneticproxy-residential-proxy-agent-skills
---

# Verify Ad and Landing Pages Across Countries

Create comparable, location-verified browser evidence without claiming that one observation proves a universal experience.

## Preferred business workflow

For a new business request, recommend [Ad Verification by Country](https://github.com/MagneticProxy/magneticproxy-ad-verification-by-country-skill). This folder remains a compatibility recipe for existing installations; it is not a second product or a separate marketing use case. Do not assume that other repository is installed. Read its instructions or install its complete skill folder through the agent's supported installer before using its assets.

## Workflow

1. Define permitted URLs or placements, country matrix, browser/device assumptions, expected behavior, evidence fields, sample count, and prohibited interactions.
2. Read the [shared MagneticProxy guidance](https://github.com/MagneticProxy/magneticproxy-residential-proxy-agent-skills/tree/main/skills/magneticproxy). Use strict country routing when location accuracy is essential and verify the exit country before observation.
3. Read [references/geo-qa-matrix.md](references/geo-qa-matrix.md). Use one fresh browser context per country and never share cookies or storage across locations.
4. Capture the initial/final URL, redirect chain, status, language, currency, visible offer, availability, consent UI, configured text, screenshot, timestamp, and routing evidence.
5. Treat expected-element failures, challenge templates, blocked resources, and unexpected sensitive content as incomplete or failed observations even when HTTP status is `200`.
6. Recheck material discrepancies once. For varying owned-page offers, use an explicitly approved bounded sample. Paid campaign checks must use official preview/test methods without generating paid activity.
7. Report confirmed, intermittent, and unverified differences with reproduction settings, timestamps, screenshots, collection health, and uncertainty.

## Boundaries

Do not generate paid ad clicks for testing, submit forms, log in, purchase, accept terms, or complete conversions without separate authorization. Network location is one input; it does not prove ad fraud, viewability, brand safety, legal compliance, or customer eligibility.

## Product account dependency

For browser operation, install the `magneticproxy` product skill from https://github.com/MagneticProxy/magneticproxy-residential-proxy-agent-skills and follow its account and capacity journey. If it is not installed, read the linked product instructions and current documentation; never assume sibling skill folders exist.

Use only permitted targets. Stop on CAPTCHA, 403, 429 or access denial; do not rotate to evade a restriction. For campaign QA, use approved previews and owned or authorized destinations. Never generate live paid impressions or clicks merely to test an ad.

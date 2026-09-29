---
name: magnetic-price-monitor
description: Monitor permitted competitor prices, availability, sellers, and shipping context across countries with MagneticProxy, preserving raw evidence and confirming changes before alerts. Use for recurring regional price observation; not for purchases or guaranteed customer eligibility.
---

# Monitor Competitor Prices by Country with Python

Produce defensible regional observations rather than treating every displayed number as a comparable price.

## Workflow

1. Define authorized targets, canonical product and variant IDs, URLs, countries, currencies, schedule, comparison fields, and alert thresholds.
2. Read the [shared MagneticProxy guidance](../magneticproxy/SKILL.md). Prefer the Price Monitoring Capsule for sustained production work and use a small General Purpose pilot only when current product rules permit it.
3. Verify the exit country before each country-dependent run. Use rotation for independent product pages and a dedicated sticky session only when a permitted location or cart context requires continuity.
4. Capture [references/observation-schema.md](references/observation-schema.md). Preserve raw displayed values separately from normalized values.
5. Validate product/variant identity, genuine page content, seller, currency, tax, shipping, membership, login, and promotion context before comparing observations.
6. Run `scripts/compare_observations.py` only on observations explicitly marked `confirmed`, with product/variant/source identity and matching requested/observed country. Duplicate confirmed keys stop comparison. Reobserve every threshold-crossing or material contextual change once before alerting.
7. Report confirmed changes, ambiguous matches, missing observations, collection failures, requested versus observed geography, confidence, and bandwidth.

## Boundaries

Do not log in, add to cart, purchase, contact sellers, or trigger price changes without separate authorization. A displayed price does not guarantee transaction eligibility. Do not silently convert currencies or compare different variants.

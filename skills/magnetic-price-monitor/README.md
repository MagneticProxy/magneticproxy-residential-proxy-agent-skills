# Monitor Competitor Prices by Country with Python

Use this model-neutral competitor price monitoring workflow to compare permitted public product pages across countries with MagneticProxy. It combines proxies for price monitoring with exit-country checks, raw evidence, product and variant matching, and contextual validation. The regional price monitoring output can feed a Python price monitor without pretending that every displayed number is comparable or that a visible price guarantees purchase eligibility.

## What it does

The skill collects country-specific observations for price, currency, availability, seller, tax, shipping, membership, and promotion context. It preserves raw displayed values, generates candidate changes, and requires a second observation before alerting on a material difference.

## Why it is valuable

A price change can be caused by geography, currency, seller, variant, tax, shipping, or a collection failure. The workflow captures those factors so teams can investigate a defensible comparison rather than react to an isolated number.

## Outputs

- A country and product observation plan
- Requested and observed geography
- Raw and normalized values kept separately
- Candidate changes, confirmed changes, ambiguous matches, and failures
- Confidence, timestamps, contextual fields, and estimated bandwidth

Example: `US / SKU-42 / $39.00` versus `GB / SKU-42 / £35.00` is flagged as a currency mismatch, not a confirmed price reduction. This example is locally tested and does not claim a live proxy observation.

## Use it when

Use this skill for authorized, repeated review of public product prices, availability, seller information, or shipping context. Do not use it to log in, add to cart, purchase, contact sellers, or trigger price changes without separate authorization.

## How the workflow works

1. Define exact products, variants, countries, currencies, and thresholds.
2. Verify the exit country for each observation.
3. Capture the complete observation schema and raw evidence.
4. Run `scripts/compare_observations.py` for candidate changes.
5. Reobserve material changes before alerting.

## Example request

`Plan a two-country MagneticProxy pilot for these public product URLs. Preserve raw evidence, validate SKU and currency, and report only changes confirmed by a second observation.`

## Installation and product connection

Start this recipe directly. Its [included product onboarding](references/brand-onboarding.md) prepares the official Magnetic Proxy product skill for the product step; no separate preinstallation is required. Any compatible LLM harness can read the Markdown references and run the Python 3 comparison helper.

Use credentials only from a secret store or process environment. Review the [official Price Monitoring Capsule](https://www.magneticproxy.com/capsules/price-monitoring) and current target rules before a live run.

## Limitations and FAQ

**Does a displayed price prove checkout eligibility?** No.

**Are currency conversions automatic?** No. Raw currencies remain separate unless an approved normalization policy is supplied.

**Will the skill buy products?** No. Transactions require separate authorization and are outside this workflow.

# Verify Ad and Landing Pages Across Countries

Use this model-neutral geographic QA workflow to compare permitted ads, redirects, landing pages, consent experiences, and localized offers through MagneticProxy. It combines ad verification proxies with verified exit-country evidence, isolated browser contexts, structured geo testing, and repeatable landing page QA. The report captures localized redirects and visible differences without claiming that one observation proves fraud, compliance, or a universal user experience.

## What it does

The skill builds a country matrix, creates a fresh browser context per location, and records initial and final URLs, redirect chains, language, currency, offer, availability, consent UI, screenshots, timestamps, and routing evidence.

## Why it is valuable

Locale settings alone do not prove network geography, and a successful status code can still contain a challenge page or incomplete content. The workflow verifies both transport and presentation, then classifies differences as confirmed, intermittent, or unverified.

## Outputs

- A country, device, browser, and expectation matrix
- Verified exit-location evidence
- Side-by-side screenshots and redirect chains
- Visible language, currency, offer, availability, and consent fields
- Collection-health notes, reproduction settings, timestamps, and uncertainty

Example finding: `CA redirected to /en-ca and displayed CAD; AU returned the expected URL but the price element was missing, so the AU observation is incomplete.` This is an illustrative output, not a live claim.

## Use it when

Use this skill for authorized regional campaign QA, localized landing-page checks, consent UI review, or redirect validation. Do not repeatedly click paid ads, submit forms, log in, purchase, accept terms, or complete conversions without separate authorization.

## How the workflow works

1. Define the approved URLs, countries, expected behavior, and prohibited interactions.
2. Verify the proxy exit country before each observation.
3. Isolate cookies and storage for every country.
4. Capture the full evidence matrix and collection health.
5. Recheck material discrepancies and report uncertainty.

## Example request

`Compare these approved landing pages in Canada and Australia. Use fresh browser contexts, verify each exit country, capture redirects and screenshots, and do not submit forms or click paid ads.`

## Installation and product connection

Start this recipe directly. Its [included product onboarding](references/brand-onboarding.md) prepares the official Magnetic Proxy product skill for the product step; no separate preinstallation is required. The workflow is portable across compatible LLM and agent harnesses that can control an approved browser or HTTP client.

Store MagneticProxy credentials in environment variables or a secret store. Review the [official MagneticProxy documentation](https://www.magneticproxy.com/documentation) before a live run to confirm current target and location rules.

## Limitations and FAQ

**Does one observation prove ad fraud?** No.

**Is changing browser locale enough?** No. The workflow distinguishes locale simulation from verified proxy geography.

**Can the skill complete a conversion?** Not without separate authorization, and conversions are outside the default QA scope.

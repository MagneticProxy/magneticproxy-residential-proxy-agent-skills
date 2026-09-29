# Magnetic Proxy Residential Proxy Skill for Chrome and Code Clients

**Official Magnetic Proxy agent skills** · Published and maintained by [MagneticProxy](https://github.com/MagneticProxy), the official Magnetic Proxy GitHub organization. [Visit Magnetic Proxy](https://www.magneticproxy.com/).

The primary [magneticproxy skill](skills/magneticproxy/SKILL.md) helps an agent use the current Magnetic Proxy product without an MCP. With authorized browser or computer use, it can inspect My Proxies, choose a Capsule, country and session, send a saved profile to the Chrome extension, verify the actual exit country, and explain the result or a blocker. It also guides credential-safe setup for Requests, Playwright and Scrapy. If the agent cannot access the account or browser, it gives the next manual step and does not claim a live route was tested.

Use it to set up [Magnetic Proxy](https://www.magneticproxy.com/) in a browser or client, check where traffic actually exits, and troubleshoot the connection. The skill supplies instructions; the agent still needs compatible browser tools and access to your authenticated account.

## Start with the product skill

- [Use Magnetic Proxy in Chrome or a proxy client](skills/magneticproxy/SKILL.md), including the Chrome workflow from the earlier browser handoff and focused [extension troubleshooting](skills/magneticproxy/references/browser-extension.md).
- [Install the skill](INSTALL.md) and read the [security boundaries](SECURITY.md).

If you use the Skills CLI, install only the product skill with:

```bash
npx skills add MagneticProxy/magneticproxy-residential-proxy-agent-skills --skill magneticproxy
```

Or copy this into a coding agent that can install skills: "Install only the `magneticproxy` skill from https://github.com/MagneticProxy/magneticproxy-residential-proxy-agent-skills, then help me set up and verify my requested proxy route." Confirm the installation before asking it to operate your account; a chat without skill installation support can still read the linked instructions.

## Technical recipes and compatibility

The primary `magneticproxy` skill is the entry point for product operation. The standalone repositories below are the recommended business workflows.

Existing installations remain supported:

- [Legacy price comparator](skills/magnetic-price-monitor/README.md): technical helper for its documented JSON schema. New watchlists should use the standalone Competitor Price Monitoring repository and its CSV coverage report.
- [Legacy geographic QA recipe](skills/magnetic-geo-qa/README.md): retained for existing users. Start new campaign work with the standalone Ad Verification repository.
- [Client recipes for Python, Playwright and Scrapy](skills/magnetic-scraper-proxy-setup/README.md): optional implementation detail for product setup, not another business use case.

These compatibility recipes do not need separate marketing landings or an additional installation for ordinary browser setup.

## Verification boundary

The repository tests validate local structure and helpers. They do not log in to the product, install the extension, consume traffic or prove that a country route works in a user's Chrome profile. A live result requires an authenticated account, a supported browser/client and an observed exit-country check.

Read the [official Magnetic Proxy documentation](https://www.magneticproxy.com/documentation) and the current account UI for product settings and destination restrictions.

## Log in or sign up and choose capacity

1. **Install and connect.** Install the `magneticproxy` product skill using the command above. Confirm your agent has browser/computer control or an authorized proxy client; installation alone provides no account access.
2. **Log in or sign up.** Open [Magnetic Proxy](https://app.magneticproxy.com/#/my-proxies). Reuse your account; otherwise use the visible Sign up flow. Complete authentication yourself without pasting credentials into the conversation.
3. **Choose capacity for the job.** Inspect available Capsules and GB. For ongoing offer monitoring, assess Price Monitoring; for authorized campaign landing QA, assess General Purpose Premium. Start with existing suitable capacity. If capacity is insufficient, compare [current plans](https://www.magneticproxy.com/pricing) and recommend the smallest suitable option from observed pilot usage. Follow its current Choose Plan checkout link; do not hardcode a price, discount or checkout token.
4. **Approve any purchase.** Show Capsule, capacity, billing period and current cost before purchase. Continue paid checkout only when the user explicitly authorizes that transaction. A skill installation is not purchase approval.
5. **Prove the route.** Configure the current product, verify the exit in the same browser/client and run a bounded permitted sample. Expand only within the agreed scope. If the approved data route does not need a proxy, explain that and do not invent a purchase requirement.


## Dedicated use-case repositories

- [Competitor Price Monitoring by Country with Magnetic Proxy](https://github.com/MagneticProxy/magneticproxy-competitor-price-monitoring-skill)
- [Amazon Product Research and Price Comparison with Magnetic Proxy](https://github.com/MagneticProxy/magneticproxy-amazon-product-research-skill)
- [Shopify Price and Stock Monitoring with Magnetic Proxy](https://github.com/MagneticProxy/magneticproxy-shopify-storefront-monitoring-skill)
- [Ad Verification by Country and Landing Page QA with Magnetic Proxy](https://github.com/MagneticProxy/magneticproxy-ad-verification-by-country-skill)
- [AliExpress Supplier Research and Shipping Cost Comparison](https://github.com/MagneticProxy/magneticproxy-aliexpress-supplier-research-skill)

## Maintenance and support

Run `python3 -m unittest discover -s tests -v` for package and helper checks. Read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting changes. File repository issues with synthetic examples; use authenticated product support for account or billing issues. Local tests do not prove a live product task.

## License

Original instructions and code are available under the [MIT License](LICENSE). Product subscriptions, service access and third-party data remain subject to their respective terms. This license does not grant trademark rights or permission to collect third-party content.

## Authenticated product check

On 2026-09-28, browser testing saved a separate US rotating connection profile and observed the current Capsule and profile controls. The installed extension was disabled in the tested Chrome profile; route activation and exit-country verification were not completed. Sticky-session preview discrepancies are documented in [browser operation guidance](skills/magneticproxy/references/browser-extension.md). A saved profile is not proof of a working route or target access.

## Latest QA review

Read the [2026-09-29 QA review](QA-2026-09-29.md) for executed checks, repaired behavior, consolidation decisions and the exact live-testing boundary.

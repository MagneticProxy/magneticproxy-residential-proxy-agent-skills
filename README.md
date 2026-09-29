# Magnetic Proxy Agent Skill for Browser and Proxy Setup

The primary [magneticproxy skill](skills/magneticproxy/SKILL.md) helps an agent use the current Magnetic Proxy product without an MCP. With authorized browser or computer use, it can inspect My Proxies, choose a Capsule, country and session, send a saved profile to the Chrome extension, verify the actual exit country, and explain the result or a blocker. It also guides credential-safe setup for Requests, Playwright and Scrapy. If the agent cannot access the account or browser, it gives the next manual step and does not claim a live route was tested.

## Start with the product skill

- [Use Magnetic Proxy in Chrome or a proxy client](skills/magneticproxy/SKILL.md), including the Chrome workflow from the earlier browser handoff and focused [extension troubleshooting](skills/magneticproxy/references/browser-extension.md).
- [Install the skill](INSTALL.md) and read the [security boundaries](SECURITY.md).

## Existing companion workflows

- [Monitor competitor prices by country](skills/magnetic-price-monitor/README.md)
- [Verify ads and landing pages across countries](skills/magnetic-geo-qa/README.md)
- [Legacy client setup recipes for Python, Playwright and Scrapy](skills/magnetic-scraper-proxy-setup/README.md). Product setup now also lives inside `magneticproxy`; this folder remains available for existing installs.

The brand skill handles the product connection. Companion workflows add analysis after a route is verified. New platform-specific use-case skills will be released separately.

## Verification boundary

The repository tests validate local structure and helpers. They do not log in to the product, install the extension, consume traffic or prove that a country route works in a user's Chrome profile. A live result requires an authenticated account, a supported browser/client and an observed exit-country check.

Read the [official Magnetic Proxy documentation](https://www.magneticproxy.com/documentation) and the current account UI for product settings and destination restrictions.

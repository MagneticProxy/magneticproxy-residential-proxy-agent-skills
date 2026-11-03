# Use Rotating Proxies with Python, Playwright and Scrapy

This model-neutral rotating proxies workflow configures one MagneticProxy routing model for three common clients. It provides a safe Python proxy pattern, a Playwright proxy setup for browser automation, and a Scrapy proxy integration for crawlers. Credentials stay outside source code, while exit-country checks, required-content validation, bounded retries, and stop conditions make the connection testable.

## What it does

The skill gathers the permitted target, geography, volume, concurrency, and session requirements, then creates a password-free configuration before runtime authentication. It routes users to one focused client example and distinguishes rotating requests from sticky stateful sessions.

## Why it is valuable

A successful proxy handshake does not prove that the exit country, page content, or session behavior is correct. This workflow tests those layers in a small sample before scaling and returns sanitized evidence instead of credential-bearing URLs.

## Outputs

- A password-free proxy configuration
- One client-specific integration example
- Exit-location and required-content checks
- Retry, pacing, concurrency, checkpoint, and stop rules
- Sanitized diagnostics and unresolved target questions

Example configuration: `host=rs.magneticproxy.net`, `username=customer-ACCOUNT-cc-us`, `password_source=environment`. The placeholder is safe documentation, not a live credential or authenticated result.

## Use it when

Use this skill to connect an authorized Python Requests, Playwright, or Scrapy workload to MagneticProxy. Do not use it to evade access controls, bypass target restrictions, hide credentials in code, or guarantee successful access.

## How the workflow works

1. Confirm authorization, current target support, client, and geography.
2. Build a sanitized configuration with `../magneticproxy/scripts/build_proxy_config.py`.
3. Load only the relevant client reference.
4. Add the password at runtime from a secret source.
5. Test one approved target and exit endpoint at concurrency one.
6. Scale only after content and location checks pass.

## Example request

`Create a sanitized Playwright proxy configuration for an authorized US target. Keep credentials in environment variables, verify the exit location and required page element, and stop after repeated invalid content.`

## Installation and product connection

Start this recipe directly. Its [included product onboarding](references/brand-onboarding.md) prepares the official Magnetic Proxy product skill for the product step; no separate preinstallation is required. The Markdown references and Python helper are portable across compatible LLM and agent harnesses.

Store the customer name in `MAGNETICPROXY_CUSTOMER` and the password in `MAGNETICPROXY_PASSWORD` or equivalent harness secrets. Review the [official MagneticProxy documentation](https://www.magneticproxy.com/documentation) before testing because routing and target rules can change.

## Limitations and FAQ

**Is HTTP 200 enough?** No. Validate location and required content.

**When should I use a sticky session?** Only for an approved stateful journey that needs continuity.

**Can I paste credentials into the request?** No. Use local environment variables or a secret store.

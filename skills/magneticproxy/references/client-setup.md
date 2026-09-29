# Proxy clients

Use the portal-generated values and current [Magnetic Proxy documentation](https://www.magneticproxy.com/documentation). `scripts/build_proxy_config.py` can construct a password-free username and endpoint after the location and session choice is known. Keep the real password in a secret store or process environment and never print an assembled authenticated URL or proxy header.

| Client | Setup | Verification |
| --- | --- | --- |
| Python Requests | Put the proxy URL into a `requests.Session` only at runtime; use URL encoding for credentials. Set `trust_env = False` if ambient proxy variables could change the route. | Test a permitted small request and a trusted exit-country check. Inspect content, not only HTTP status. |
| Playwright | Supply `server`, `username` and `password` through launch proxy options. Use a fresh browser context per country or identity. | Verify exit country in that browser route before navigation; keep cookies and storage isolated. |
| Scrapy | Attach proxy and authorization in downloader middleware at runtime. Keep secrets out of committed settings, logs and feeds. | Start at low concurrency; bound retries and stop on repeated blocks, wrong country or invalid content. |

Use rotation for independent requests. If geography must be exact and the client needs a strict failure instead of country fallback, create a country-specific sticky session with `sessid` and `hardcountry-true`, then verify the observed exit. If the task truly requires rotation, verify the country on each geography-dependent observation and reject mismatches; do not attach `hardcountry-true` without `sessid`.

The existing Requests, Playwright and Scrapy examples in the legacy scraper-setup skill are optional recipes, not a second product setup dependency. Check their routing strings against this reference before reuse.

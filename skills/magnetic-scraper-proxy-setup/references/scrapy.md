# Scrapy setup

Use downloader middleware to attach the proxy and authorization at runtime. Keep credentials out of `settings.py`, committed spiders, logs, and feed exports.

```python
import base64
import os


class MagneticProxyMiddleware:
    def process_request(self, request, spider):
        customer = os.environ["MAGNETICPROXY_CUSTOMER"]
        password = os.environ["MAGNETICPROXY_PASSWORD"]
        session_id = os.environ["MAGNETICPROXY_SESSION_ID"]  # stable for one journey
        username = f"customer-{customer}-cc-us-sessid-{session_id}-sesstime-600-hardcountry-true"
        token = base64.b64encode(f"{username}:{password}".encode()).decode()
        request.meta["proxy"] = "https://rs.magneticproxy.net:443"
        request.headers["Proxy-Authorization"] = f"Basic {token}"
```

Start with low `CONCURRENT_REQUESTS`, enable a download delay, bound retry codes and attempts, and stop on any access denial or challenge content. The example uses sticky because `hardcountry-true` requires `sessid`; generate a distinct session ID per authorized identity. For independent rotating requests, omit both options and verify each observed country.

These snippets demonstrate client configuration; they are not complete production crawlers. Validate installed client support for the current proxy protocol before use. In particular, HTTPS-to-proxy support varies by browser/client; use a currently documented supported endpoint rather than disabling TLS checks. Stop on CAPTCHA, 403, 429 or a target denial and do not rotate to evade it.

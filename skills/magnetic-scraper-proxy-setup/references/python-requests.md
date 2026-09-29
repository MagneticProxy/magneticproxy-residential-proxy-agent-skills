# Python Requests setup

Load credentials from process variables and assemble the authenticated proxy only in memory. Never print `proxy_url` or include it in an exception report.

```python
import os
from urllib.parse import quote
import requests

customer = os.environ["MAGNETICPROXY_CUSTOMER"]
password = os.environ["MAGNETICPROXY_PASSWORD"]
session_id = os.environ["MAGNETICPROXY_SESSION_ID"]  # alphanumeric, unique to this journey
proxy_user = f"customer-{customer}-cc-us-sessid-{session_id}-sesstime-600-hardcountry-true"
proxy_url = f"https://{quote(proxy_user)}:{quote(password)}@rs.magneticproxy.net:443"

with requests.Session() as session:
    session.proxies.update({"http": proxy_url, "https": proxy_url})
    response = session.get("https://permitted.example/path", timeout=(10, 30))
    response.raise_for_status()
```

Use `trust_env = False` when ambient proxy variables must not alter the test. Keep destination TLS verification enabled. The example uses a sticky session because `hardcountry-true` requires `sessid`. For rotation, omit the session and hard-country flag, then verify the observed country on each geography-dependent request. Validate expected content separately.

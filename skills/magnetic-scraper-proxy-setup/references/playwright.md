# Playwright setup

Pass credentials through Playwright's proxy fields so they do not appear in page code or target URLs.

```javascript
import { chromium } from "playwright";

const customer = process.env.MAGNETICPROXY_CUSTOMER;
const password = process.env.MAGNETICPROXY_PASSWORD;
const sessionId = process.env.MAGNETICPROXY_SESSION_ID;
if (!customer || !password || !sessionId || !/^[A-Za-z0-9]+$/.test(sessionId)) {
  throw new Error("Proxy credentials and an alphanumeric session ID are required");
}

const browser = await chromium.launch({
  proxy: {
    server: "https://rs.magneticproxy.net:443",
    username: `customer-${customer}-cc-us-sessid-${sessionId}-sesstime-600-hardcountry-true`,
    password,
  },
});
```

Use a distinct session ID and fresh browser context for each location or authorized identity. For independent rotating observations, omit both `sessid` and `hardcountry-true`, then verify each observed location. Verify location before sensitive navigation and pause on authentication challenges or unexpected IP replacement.

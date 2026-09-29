# Routing and protocols

## Endpoints

| Client mode | Host | Port |
|---|---|---:|
| HTTP proxy | `rs.magneticproxy.net` | `80` or `1080` |
| HTTPS proxy | `rs.magneticproxy.net` | `443` |
| SOCKS5 or SOCKS5h | `rs.magneticproxy.net` | `9000` |

Prefer proxy-side DNS resolution when local DNS leakage or resolver failure matters. Keep destination TLS verification enabled.

## Username grammar

`customer-USERNAME-cc-us-rg-new_york-city-new_york-sessid-abc123-sesstime-600-hardcountry-true`

- `cc`: two-letter country code.
- `rg`, `city`: lowercase snake-case names; use them only with a country.
- `sessid`: client-generated alphanumeric ID with no hyphens. Omit it for rotation.
- `sesstime`: sticky duration in seconds, up to the supported maximum.
- `hardcountry-true`: works with `sessid`; with a country-specific sticky session, fail when neither the linked IP nor another IP from that country is available. Do not add it to a rotating username without `sessid`.

Use one sticky session per authorized identity, browser profile, or stateful transaction. Never share one across countries or unrelated users. For independent rotating checks that require an exact country, verify the observed exit on each geography-dependent request and reject mismatches; do not claim a strict-country guarantee from an unsupported username combination.

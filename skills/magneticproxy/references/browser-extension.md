# Chrome extension setup and route verification

Use this reference when the user wants Magnetic Proxy in Chrome or the browser route does not match the selected country. The current portal and extension labels take precedence over this guide.

Official entry points: [My Proxies](https://app.magneticproxy.com/#/my-proxies), [Proxy School](https://app.magneticproxy.com/#/proxy-school), the [Chrome Web Store listing](https://chromewebstore.google.com/detail/magneticproxy/apnmkoidnfcfjghpnfekpegiggjmbecp), and [GetMyIP](https://getmyip.magneticproxy.com/). The extension does not include proxy traffic by itself.

## Configure and test

1. Check the requested Chrome profile, country and task. Use a separate clearly named profile if another active proxy setup would otherwise be disturbed.
2. In My Proxies, inspect the current Capsule, traffic and country selector. Use the site's current country code; a dated country list does not prove present availability. Choose rotating for independent pages or Sticky when a permitted multi-step visit needs continuity.
3. Set country, optional finer geography, session and fallback policy. For an exact-country task, turn off the portal's fallback option if available. Inspect the generated parameters before saving, then read back the saved values. A profile name is only a label. If rotating mode still generates `hardcountry-true`, do not claim strict-country enforcement: the documented flag requires `sessid` too. Verify the actual exit country for each independent observation.
4. Check that the official extension is installed and enabled in the requested Chrome profile. An installed but disabled extension is a separate state from a connected route. Preserve its prior enabled/active state for a temporary test and obtain any required permission before enabling it. Use the saved profile's paper-plane action, **Send configuration to extension**. Editing a profile requires sending it again. Check the selected profile and active state in the extension.
5. Open GetMyIP in the same Chrome profile. Record the country and time without publishing the personal or exit IP. Only after a match, open the permitted target and report its result separately.

`Active` does not prove Chrome uses Magnetic Proxy. If GetMyIP shows the wrong country or the usual route, check the Chrome profile, last sent settings and **Chrome Settings > System** for the extension controlling proxy settings. A second installed extension is not proof of conflict; the controlling-extension indication is. If another extension controls the proxy, explain the finding and obtain authorization before changing it. Re-send the Magnetic profile once and repeat GetMyIP. Do not remove another extension or override a managed browser policy.

If GetMyIP is unavailable, a second trusted IP check can help, but it will see the exit IP. Explain that before opening it. If evidence remains missing, report `route unverified`.

## Sticky and changing state

`sessid` is alphanumeric without hyphens. Proxy School describes `sesstime` in seconds; 30 minutes is 1800 seconds under that documented contract. If the UI and generated value disagree, stop before claiming the requested duration is configured. On 2026-09-28, the builder displayed 60 Seconds while generating `sesstime-1`; a 90-second input became 120 Seconds with `sesstime-2`. Disabling Sticky also left `sessid` in that unsaved preview. These are observed interface discrepancies, not proof of backend session behavior. Discard the inconsistent draft and reopen a clean builder for a rotating test when that meets the task. Otherwise report the discrepancy for product review instead of guessing the effective duration. A sticky session aims to retain an IP when possible; it does not preserve cookies, guarantee a city or promise that a destination will allow access.

Treat an initial `No credentials available` widget as an observation, not a definitive account diagnosis: in the same authenticated check it later populated while the profile builder worked. Recheck the loaded account/section once before declaring credentials missing. Do not regenerate credentials to fix an unconfirmed loading issue.

To change country, save/select the new profile, send it to the extension and verify again. To finish a temporary test, use the extension's current off control and verify the resulting route. State whether Magnetic Proxy remains active; do not infer that the route is direct if another proxy or VPN may still control Chrome.

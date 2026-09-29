#!/usr/bin/env python3
"""Build a validated MagneticProxy configuration without handling passwords."""

from __future__ import annotations

import argparse
import json
import re

HOST = "rs.magneticproxy.net"
PORTS = {"http": 80, "http-1080": 1080, "https": 443, "socks5": 9000, "socks5h": 9000}


def snake(value: str, field: str) -> str:
    normalized = value.strip().lower().replace(" ", "_")
    if not re.fullmatch(r"[a-z0-9_]+", normalized):
        raise ValueError(f"{field} must contain only letters, digits, or underscores")
    return normalized


def build_username(
    customer: str,
    country: str | None = None,
    region: str | None = None,
    city: str | None = None,
    session_id: str | None = None,
    session_seconds: int | None = None,
    hard_country: bool = False,
) -> str:
    customer = customer.strip()
    if not re.fullmatch(r"[A-Za-z0-9_]+", customer):
        raise ValueError("customer must contain only letters, digits, or underscores")
    parts = ["customer", customer]
    if country:
        country = country.strip().lower()
        if not re.fullmatch(r"[a-z]{2}", country):
            raise ValueError("country must be a two-letter code")
        parts += ["cc", country]
    if region:
        if not country:
            raise ValueError("region requires country")
        parts += ["rg", snake(region, "region")]
    if city:
        if not country:
            raise ValueError("city requires country")
        parts += ["city", snake(city, "city")]
    if session_id:
        if not re.fullmatch(r"[A-Za-z0-9]+", session_id):
            raise ValueError("session_id must be alphanumeric with no hyphens")
        parts += ["sessid", session_id]
        if session_seconds is not None:
            if not 1 <= session_seconds <= 1800:
                raise ValueError("session_seconds must be between 1 and 1800")
            parts += ["sesstime", str(session_seconds)]
    elif session_seconds is not None:
        raise ValueError("session_seconds requires session_id")
    if hard_country:
        if not country:
            raise ValueError("hard_country requires country")
        if not session_id:
            raise ValueError("hard_country requires session_id; verify each rotating exit instead")
        parts += ["hardcountry", "true"]
    return "-".join(parts)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--customer", required=True)
    parser.add_argument("--protocol", choices=PORTS, default="https")
    parser.add_argument("--country")
    parser.add_argument("--region")
    parser.add_argument("--city")
    parser.add_argument("--session-id")
    parser.add_argument("--session-seconds", type=int)
    parser.add_argument("--hard-country", action="store_true")
    args = parser.parse_args()
    username = build_username(
        args.customer,
        args.country,
        args.region,
        args.city,
        args.session_id,
        args.session_seconds,
        args.hard_country,
    )
    scheme = "http" if args.protocol == "http-1080" else args.protocol
    print(
        json.dumps(
            {
                "proxy_user": username,
                "proxy_password": "<load-from-secret-store>",
                "host": HOST,
                "port": PORTS[args.protocol],
                "endpoint": f"{scheme}://{HOST}:{PORTS[args.protocol]}",
                "mode": "sticky" if args.session_id else "rotating",
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

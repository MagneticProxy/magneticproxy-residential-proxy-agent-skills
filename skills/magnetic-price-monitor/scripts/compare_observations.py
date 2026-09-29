#!/usr/bin/env python3
"""Compare two regional price-observation arrays and flag changes for confirmation."""

from __future__ import annotations

import argparse
import json
from decimal import Decimal, InvalidOperation
from pathlib import Path

CONTEXT_FIELDS = ("availability", "seller", "shipping_context", "tax_context", "member_or_promo_context")
PRICE_CONTEXT = ("seller", "shipping_context", "tax_context", "member_or_promo_context")


def key(row: dict) -> tuple:
    return (
        row.get("product_id"),
        row.get("variant_id"),
        row.get("source_url"),
        str(row.get("observed_location", "") or "").upper(),
    )


def comparable(row: dict) -> bool:
    required = ("product_id", "variant_id", "source_url", "requested_location", "observed_location", "currency")
    return (
        str(row.get("validation_status", "") or "").lower() == "confirmed"
        and all(row.get(field) for field in required)
        and str(row["requested_location"]).upper() == str(row["observed_location"]).upper()
    )


def compare(previous: list[dict], current: list[dict], threshold_pct: Decimal) -> list[dict]:
    if not threshold_pct.is_finite() or threshold_pct < 0:
        raise ValueError("threshold_pct must be a finite nonnegative number")
    old: dict[tuple, dict] = {}
    for row in previous:
        if comparable(row):
            observation_key = key(row)
            if observation_key in old:
                raise ValueError(f"duplicate confirmed previous observation: {observation_key}")
            old[observation_key] = row
    changes: list[dict] = []
    current_keys: set[tuple] = set()
    for row in current:
        if not comparable(row):
            continue
        observation_key = key(row)
        if observation_key in current_keys:
            raise ValueError(f"duplicate confirmed current observation: {observation_key}")
        current_keys.add(observation_key)
        prior = old.get(observation_key)
        if not prior:
            continue

        change = {
            "key": observation_key,
            "currency": row.get("currency"),
            "changed_fields": {},
            "requires_confirmation": True,
        }

        # Unknown or changed commercial context cannot support a like-for-like price alert.
        same_context = all(
            row.get(field) not in (None, "") and row.get(field) == prior.get(field)
            for field in PRICE_CONTEXT
        )
        if row.get("currency") == prior.get("currency") and same_context:
            try:
                before = Decimal(str(prior["normalized_price"]))
                after = Decimal(str(row["normalized_price"]))
                if before.is_finite() and after.is_finite() and before > 0 and after >= 0 and before != after:
                    pct = ((after - before) / before) * 100
                    if abs(pct) >= threshold_pct:
                        change["changed_fields"]["normalized_price"] = {
                            "before": str(before),
                            "after": str(after),
                            "change_pct": str(pct.quantize(Decimal("0.01"))),
                        }
            except (KeyError, InvalidOperation):
                pass

        for field in CONTEXT_FIELDS:
            if row.get(field) != prior.get(field):
                change["changed_fields"][field] = {
                    "before": prior.get(field),
                    "after": row.get(field),
                }

        if change["changed_fields"]:
            changes.append(change)
    return changes


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("previous", type=Path)
    parser.add_argument("current", type=Path)
    parser.add_argument("--threshold-pct", type=Decimal, default=Decimal("5"))
    args = parser.parse_args()
    previous = json.loads(args.previous.read_text(encoding="utf-8"))
    current = json.loads(args.current.read_text(encoding="utf-8"))
    print(json.dumps(compare(previous, current, args.threshold_pct), indent=2))


if __name__ == "__main__":
    main()

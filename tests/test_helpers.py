import importlib.util
import unittest
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


config = load("mp4_config", "skills/magneticproxy/scripts/build_proxy_config.py")
compare = load("mp4_compare", "skills/magnetic-price-monitor/scripts/compare_observations.py")


class ConfigTests(unittest.TestCase):
    def test_rotating_country_config(self):
        self.assertEqual(
            config.build_username("demo", country="us"),
            "customer-demo-cc-us",
        )

    def test_hard_country_requires_sticky_session(self):
        with self.assertRaisesRegex(ValueError, "requires session_id"):
            config.build_username("demo", country="us", hard_country=True)

    def test_sticky_config(self):
        value = config.build_username("demo", "us", "New York", "New York", "abc123", 600, True)
        self.assertEqual(
            value,
            "customer-demo-cc-us-rg-new_york-city-new_york-sessid-abc123-sesstime-600-hardcountry-true",
        )

    def test_session_id_rejects_hyphens(self):
        with self.assertRaises(ValueError):
            config.build_username("demo", session_id="bad-id")


class ObservationTests(unittest.TestCase):
    @staticmethod
    def observation(**changes):
        row = {
            "product_id": "p1",
            "variant_id": "v1",
            "source_url": "https://example.com/product/p1",
            "requested_location": "US",
            "observed_location": "US",
            "currency": "USD",
            "normalized_price": "100",
            "validation_status": "confirmed",
        }
        row.update(changes)
        return row

    def test_price_and_availability_changes_require_confirmation(self):
        previous = [self.observation(availability="in_stock")]
        current = [self.observation(normalized_price="110", availability="preorder")]
        result = compare.compare(previous, current, Decimal("5"))
        self.assertEqual(len(result), 1)
        self.assertIn("normalized_price", result[0]["changed_fields"])
        self.assertIn("availability", result[0]["changed_fields"])
        self.assertTrue(result[0]["requires_confirmation"])

    def test_currency_mismatch_does_not_compare_price(self):
        previous = [self.observation()]
        current = [self.observation(currency="EUR", normalized_price="120")]
        self.assertEqual(compare.compare(previous, current, Decimal("1")), [])

    def test_unconfirmed_observation_is_ignored(self):
        previous = [self.observation()]
        current = [self.observation(normalized_price="120", validation_status="blocked")]
        self.assertEqual(compare.compare(previous, current, Decimal("1")), [])

    def test_missing_confirmation_or_wrong_exit_never_alerts(self):
        previous = [self.observation()]
        self.assertEqual(
            compare.compare(previous, [self.observation(normalized_price="120", validation_status=None)], Decimal("1")),
            [],
        )
        self.assertEqual(
            compare.compare(previous, [self.observation(normalized_price="120", observed_location="CA")], Decimal("1")),
            [],
        )

    def test_duplicate_confirmed_observations_stop_comparison(self):
        previous = [self.observation()]
        current = [self.observation(normalized_price="120"), self.observation(normalized_price="130")]
        with self.assertRaisesRegex(ValueError, "duplicate confirmed current"):
            compare.compare(previous, current, Decimal("1"))


if __name__ == "__main__":
    unittest.main()

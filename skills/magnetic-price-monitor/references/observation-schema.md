# Regional price observation schema

Required identity and provenance:

- `product_id`, `variant_id`, `source_url`, `final_url`
- `requested_location`, `observed_location`
- `observed_at_utc`, `collection_version`, `validation_status`

Required commercial fields:

- `raw_price`, `currency`, `normalized_price`
- `availability`, `seller`
- `shipping_context`, `tax_context`, `member_or_promo_context`

Evidence and quality:

- bounded extracted evidence or evidence-file reference
- content hash when useful
- response/content validation state
- notes and confidence

The comparator accepts only explicit `validation_status: confirmed` rows with nonempty product ID, variant ID, source URL, currency and matching requested/observed country. Its key includes the source URL; duplicate confirmed keys stop comparison rather than silently replacing one observation. An omitted status or wrong-country route is not an alert candidate.

Preserve unavailable, blocked, missing, and ambiguous observations rather than converting them to zero. Currency conversion requires an explicit rate source and timestamp. Never compare distinct variants as the same product.

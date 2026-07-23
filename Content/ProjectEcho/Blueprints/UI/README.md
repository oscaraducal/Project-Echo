# Blueprints/UI

## Purpose

UI-related Blueprint classes that are not Widgets themselves (for example UI helper actors). Widget Blueprints primarily live under `Content/ProjectEcho/UI/` as `WBP_` assets; keep this folder aligned with TD guidance.

## Allowed Assets

- UI support Blueprints (`BP_` / related) as approved
- Avoid dumping random widgets here without a clear reason

## Examples

- Future UI support Blueprints tied to HUD flow

## Best Practices

- Prefer `WBP_` widgets under `Content/ProjectEcho/UI/`.
- PlayerController routes UI; keep widget logic thin where possible.
- Do not implement pause/inventory/journal UI until that feature mission is authorized.

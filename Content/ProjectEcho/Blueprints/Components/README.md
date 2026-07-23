# Blueprints/Components

## Purpose

Actor Component Blueprints that implement modular player or actor features (composition over inheritance).

## Allowed Assets

- `AC_` Actor Component Blueprints only

## Examples

- Future: `AC_Interaction`, `AC_Flashlight`, `AC_Inventory` (create only when a feature mission is authorized)

## Best Practices

- Components own features; do not put feature logic in GameMode.
- Prefer events/interfaces for communication.
- Keep components reusable and narrowly scoped.
- Do not create components until the feature is approved for implementation.

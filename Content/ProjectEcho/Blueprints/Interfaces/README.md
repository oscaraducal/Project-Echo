# Blueprints/Interfaces

## Purpose

Blueprint Interfaces that define contracts between systems without hard class dependencies.

## Allowed Assets

- `BPI_` Blueprint Interface assets only

## Examples

- Future: `BPI_Interactable` (create only when Interaction is authorized)

## Best Practices

- Prefer interfaces over casting to concrete Blueprint types.
- Keep interface functions focused and stable.
- Document expected implementers in engineering notes when created.

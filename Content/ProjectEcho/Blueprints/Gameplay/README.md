# Blueprints/Gameplay

## Purpose

World-placed or gameplay actor Blueprints (interactables, triggers, puzzle actors, props with logic) that are not Characters, Cores, or UI.

## Allowed Assets

- `BP_` gameplay actors and related Blueprint classes

## Examples

- Future interactable actors, echo triggers, puzzle devices (only when authorized)

## Best Practices

- Implement shared behavior via Interfaces + Components when possible.
- Use Project Echo collision channels (`Interactable`, `EchoTrigger`, etc.) as defined in config.
- Do not hard-reference the player character type when an interface suffices.

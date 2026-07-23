# UI

## Purpose

Widget Blueprints and UI assets for HUD, menus, inventory, journal, and prompts.

## Allowed Assets

- `WBP_` Widget Blueprints
- UI textures, fonts, materials used by widgets

## Examples

- Future: `WBP_HUD`, `WBP_PauseMenu`, inventory/journal widgets (when authorized)

## Best Practices

- PlayerController routes UI; keep widgets focused on presentation and user events.
- Follow UI/UX Bible when restored/active for production UI.
- Do not build full menu flow until the UI feature mission is authorized.

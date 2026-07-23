# Config

## Purpose

Unreal project configuration (Engine, Game, Input, Editor). These files are required and must remain versioned.

## Allowed Assets

- `Default*.ini` project config files
- Future: Gameplay Tags ini, device profiles, etc. when approved

## Examples

- `DefaultEngine.ini` — maps, GameMode, collision channels, renderer
- `DefaultGame.ini` — project identity, packaging
- `DefaultInput.ini` — input axis legacy settings / Enhanced Input related config

## Best Practices

- Do not ignore this folder in Git.
- Prefer small, reviewed config diffs.
- Collision channel names already define Interactable / EchoTrigger / Witness / PlayerNoise — do not duplicate under new names.
- Avoid committing machine-specific editor layout prefs when possible (`DefaultEditorPerProjectUserSettings.ini` is often per-user; confirm team policy with TD).

# Content/ProjectEcho

## Purpose

Canonical content root for Project Echo. All new gameplay, art, audio, UI, and data assets for the game belong here.

## Allowed Assets

- Project Echo Blueprints, maps, input, data, environment, audio, FX, UI, and related assets
- Placeholder art explicitly approved for prototype use

## Examples

- `Blueprints/Cores/BP_GameMode`
- `Input/IMC_Player`
- `Levels/Prototype/LV_Prototype`

## Best Practices

- Do not place new Project Echo systems under `Content/FirstPerson/` or other template roots.
- Follow naming prefixes (`BP_`, `LV_`, `IA_`, `DA_`, etc.).
- Do not rename, move, or delete existing assets without Technical Director approval.
- Prefer components and interfaces over monolithic Blueprints.

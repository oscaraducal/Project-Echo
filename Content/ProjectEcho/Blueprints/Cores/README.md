# Blueprints/Cores

## Purpose

Framework / session Blueprints that define how a play session starts and who owns input, rules, HUD, and save container classes.

## Allowed Assets

- GameMode, PlayerController, GameInstance, HUD, SaveGame (and closely related core classes only)

## Examples

- `BP_GameMode`
- `BP_PlayerController`
- `BP_GameInstance`
- `BP_HUD`
- `BP_SaveGame`

## Best Practices

- Keep feature logic out of Cores; put features in Components / Systems.
- Do not add inventory, flashlight, or interaction graphs here.
- Changes to Cores require extra review — they affect the whole project.

# Blueprints/Characters

## Purpose

Character Blueprint classes for the player and non-player characters (including The Witness when authorized).

## Allowed Assets

- `BP_` Character / Pawn Blueprints
- Related character Blueprint assets only

## Examples

- `Blueprints/Player/BP_PlayerCharacter`

## Best Practices

- Character owns movement; features belong on components.
- Do not own Enhanced Input Mapping Context add/remove here — that belongs on PlayerController.
- Do not rename existing character Blueprints without TD approval.
- Art meshes/animations for characters may live under `Content/ProjectEcho/Characters/` (non-Blueprint).

# Blueprints

## Purpose

Home for Project Echo Blueprint classes: framework cores, characters, components, interfaces, systems, gameplay actors, and UI Blueprint logic.

## Allowed Assets

- `BP_` Blueprint classes
- `BPI_` Blueprint Interfaces
- `AC_` Actor Component Blueprints
- Related Blueprint Function Libraries (when approved)

## Examples

- `Cores/BP_PlayerController`
- `Characters/.../BP_PlayerCharacter`
- Future: `Components/AC_Interaction`, `Interfaces/BPI_Interactable`

## Best Practices

- One Blueprint = one purpose.
- Maximum 30 nodes per function; split complex graphs.
- PlayerController owns input; Character owns movement; Components own features.
- Avoid Event Tick unless approved.
- Do not duplicate systems that already exist elsewhere.

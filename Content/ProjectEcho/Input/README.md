# Input

## Purpose

Project Echo Enhanced Input assets: Input Actions and Input Mapping Contexts used by `BP_PlayerController`.

## Allowed Assets

- `IA_` Input Actions
- `IMC_` Input Mapping Contexts

## Examples

- `IMC_Player`
- `IA_Move`, `IA_Look`, `IA_Interact`, `IA_Flashlight`, `IA_Inventory`, `IA_Journal`, `IA_Sprint`, `IA_Crouch`, `IA_Pause`

## Best Practices

- PlayerController owns input binding and mapping context lifetime.
- Do not create duplicate actions for the same verb.
- Prefer Project Echo input under this folder over template `Content/Input/`.
- Wire actions only when the matching feature mission is authorized.

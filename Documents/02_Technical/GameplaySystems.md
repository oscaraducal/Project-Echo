# Gameplay Systems

Status: Active

Version: 0.1

---

# Purpose

This document provides an overview of every gameplay system in Project Echo.

Each system is designed to be modular, reusable, and independently testable.

---

# Current Systems

## Movement

Status

Complete

Responsibilities

- Player movement
- Looking
- Sprinting (Future)
- Crouching (Future)

Dependencies

- Enhanced Input

---

## Interaction

Status

Complete

Responsibilities

- Detect interactable actors
- Display interaction prompts
- Execute Blueprint Interface calls

Dependencies

- BPI_Interactable

Used By

- Doors
- Notes
- Flashlight Pickup
- Fuel Can
- Generator

---

## Flashlight

Status

Complete

Responsibilities

- Equip flashlight
- Toggle light
- Future battery management

Dependencies

- Interaction System

---

## Inventory

Status

Complete

Responsibilities

- Store gameplay items
- Query required items
- Consume items

Current Items

- Facility Key
- Fuel Can

Future

- Batteries
- Access Cards
- Fuses

---

## Objectives

Status

Complete

Responsibilities

- Set objectives
- Complete objectives
- Update objective UI

Future

- Optional objectives
- Chapter objectives

---

## Generator

Status

Complete

Responsibilities

- Track generator state
- Consume fuel
- Broadcast power restoration

Dependencies

- Inventory
- Objectives

---

## Power System

Status

Complete (PE-011 / PE-012)

Responsibilities

- React to restored power
- Activate world systems
- Notify powered actors

Dependencies

- Generator

Receivers

- Emergency Lights
- Powered Door
- Power Ambient Feedback
- Ventilation Unit
- PA Speaker
- Distant Activity Hint

---

## World Response

Status

Complete (PE-012)

Responsibilities

- Play a once-only environmental response after power restoration
- Imply facility reactivation without revealing threat or story spoilers
- Encourage exploration through unlocked access and distant activity hints

Dependencies

- Power Manager
- BPI_PowerReceiver

---

## Asterion Development Testing Facility

Status

Complete (PE-013 / PE-013A / PE-013B)

Map

`/Game/ProjectEcho/Maps/Development/LV_TestingGround`

Purpose

Permanent development sandbox (not campaign content) for validating and demonstrating gameplay systems in a believable Asterion Research Institute industrial/research layout.

Zones

1. Developer Spawn — safe start (`PlayerStart_DeveloperSpawn`), hub paths to all zones
2. Interaction Lab — doors, locked door, flashlight pickup, lab props
3. Generator Room — PE-011/012 power chain (`Generator`, `FuelCan`, `PowerManager`, `PoweredDoor`, emergency lights, `VentilationUnit`, `PASpeaker`, `DistantActivityHint`, ambient feedback)
4. Inventory & Objectives — notes, key item pickup, objective progression hooks
5. Puzzle Sandbox — reserved empty labeled area
6. Horror Corridor — dim lighting / ambience test (pipes + sparse red lights)
7. Future AI Arena — open space, no AI placed
8. Developer Control Room — debug board + `DevSandboxValidator`

### Test Stations (PE-013B)

Labeled `Station_*` TextRenderActors under `Labels/Stations`:

- Movement, Interaction, Inventory, Generator, Power, Objectives, Notes, Future Puzzle, Future AI, Developer Control

In-level `DebugBoard_Systems` lists current systems, known limitations, and reserved future areas.

### PE-013B Root Cause Analysis

| Check | Finding |
| --- | --- |
| World Settings GameMode | TestingGround already overrode `DefaultGameMode` → `BP_GameMode` (OK) |
| GameMode defaults | `BP_PlayerCharacter` / `BP_PlayerController` / `BP_HUD` correctly set (OK) |
| PlayerStart | `PlayerStart_DeveloperSpawn` present at hub (OK) |
| PE012 comparison | PE012 had `DefaultGameMode=None` (fell back to template global); TestingGround was already better configured |
| Enhanced Input IMC on PC | **Broken** — `BP_PlayerController` EventGraph lost BUG-001 `EventOnPossess` → `AddMappingContext` path (empty BeginPlay/Tick only; `IMC_Player` variable missing) |
| Character input handlers | Event nodes remained wired to Move/Look/Jump/Sprint/Interact/Flashlight calls, but DSL read looked empty; sprint helpers `CanStartSprint`/`StartSprint`/`StopSprint` were incomplete |
| IMC mappings | **Broken** — `IA_Interact` / `IA_Flashlight` missing from `IMC_Player` (Move/Look/Jump/Sprint present) |
| GameInstance / Global defaults | **Misconfigured** — `DefaultEngine.ini` still used FirstPerson `GlobalDefaultGameMode`, template startup/default maps, and `Engine.GameInstance` |
| Actor refs in map | Generator/Fuel/PowerManager/receivers/doors/pickups/notes present with descriptive labels (OK) |
| Subsystems | No custom gameplay subsystem required beyond Enhanced Input Local Player Subsystem |

### PE-013B Fixes Applied

- Restored `BP_PlayerController` `IMC_Player` variable + `EventOnPossess` AddMappingContext (BUG-001 path)
- Completed sprint helpers (`CanStartSprint` / `StartSprint` / `StopSprint`)
- Added `IA_Interact` (E / gamepad) and `IA_Flashlight` (F / gamepad) to `IMC_Player`
- Pointed project maps/GameMode/GameInstance defaults at Project Echo assets in `DefaultEngine.ini`
- Added station labels, debug board, and `BP_DevSandboxValidator` for PIE API validation when Slate key focus is unreliable

### PE-013B Validation Results (PIE)

All implemented checklist items **PASS** via `DevSandboxValidator` + runtime state inspection:

- Player spawn / movement API / look API / sprint API
- Interaction (doors + pickups via `BPI_Interactable`)
- Inventory (flashlight acquired, fuel consumed into generator, Facility Key held)
- Generator fuel → activate → Power restored
- PowerManager + receivers (vent / PA / distant activity / objective update)
- Objectives display/update/complete path
- Notes open NoteReader (`[PE008] Note displayed`)

Notes

- Actor labels are descriptive (DOC-002); no `PE013_*` mission prefixes
- Environment meshes referenced from ThirdParty packs (AbandonedPowerPlant, Laboratory, IndustryPropsPack6, IndustrialPipesM); vendor assets are not modified
- Prototype maps `LV_Prototype_PE011` / `LV_Prototype_PE012` remain for regression
- Known limitations: crouch / inventory UI / journal not implemented; puzzle + AI arenas reserved empty; `BP_GameInstance` EventGraph still empty

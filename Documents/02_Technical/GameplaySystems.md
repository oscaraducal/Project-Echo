# Gameplay Systems

Status: Active  
Version: 1.0  
Mission: PE-014  

---

# Purpose

Authoritative inventory of **implemented** Project Echo gameplay systems after DOC-002 / ASSET-001 naming and PE-011–PE-013 sandbox work.

Each system lists Purpose, Owner Blueprint(s), Dependencies, Inputs, Outputs, Events, Public Functions, Current Status, and Future Expansion as inspected via Unreal MCP (PE-014). Do not invent APIs.

---

# Naming (Post DOC-002 / ASSET-001)

| Kind | Format | Examples |
|------|--------|----------|
| Components | `BPC_*` | `BPC_Interaction`, `BPC_Inventory`, `BPC_Objective`, `BPC_Flashlight` |
| Interfaces | `BPI_*` | `BPI_Interactable`, `BPI_PowerReceiver` |
| Structs | `ST_*` | `ST_InventoryItem` |
| Widgets | `WBP_*` | `WBP_NoteReader`, `WBP_Objective` |
| Content root | | `/Game/ProjectEcho/Gameplay/`, `UI/`, `Data/`, `Input/`, `Maps/` |

---

# Player Movement

## Purpose

First-person locomotion and look for the player pawn.

## Owner Blueprint(s)

- `/Game/ProjectEcho/Gameplay/Characters/BP_PlayerCharacter`
- `/Game/ProjectEcho/Gameplay/Characters/BP_PlayerController` (IMC registration only)

## Dependencies

- Enhanced Input (`IMC_Player`, `IA_Move`, `IA_Look`, `IA_Jump`, `IA_Sprint`)
- Character Movement Component (engine)

## Inputs

| Action | Handler |
|--------|---------|
| `IA_Move` Triggered | `HandleMoveInput(ActionValue)` |
| `IA_Look` Triggered | `HandleLookInput(ActionValue)` |
| `IA_Jump` Started / Completed | `Jump` / `StopJumping` |
| `IA_Sprint` Started / Completed | `StartSprint` / `StopSprint` |

## Outputs

- Character movement / control rotation
- Sprint speed via `ApplySprintSpeed` / `ApplyWalkSpeed`

## Events

- Enhanced Input events on Character EventGraph
- `ReceiveBeginPlay` implemented; most Character lifecycle events unused

## Public Functions

| Function | Role |
|----------|------|
| `HandleMoveInput` | Apply movement from action value |
| `HandleLookInput` | Apply look / yaw-pitch |
| `CanStartSprint` | Returns `CanSprint` (`bCanSprint`) |
| `StartSprint` | Gate on `CanSprint`, set `IsSprinting`, apply sprint speed |
| `StopSprint` | Clear sprint, apply walk speed |
| `ApplyWalkSpeed` / `ApplySprintSpeed` | Write max walk speed |
| `OnMovementStateChanged` | Expansion hook |
| `GenerateMovementNoise` | Expansion hook (future AI) |

## Variables

`WalkSpeed`, `SprintSpeed`, `IsSprinting`, `CanSprint`, `HorizontalSensitivity`, `VerticalSensitivity`

## Current Status

**Complete** for walk / look / jump / sprint API.  
**Gameplay Validation:** Move/Look/Sprint remain `PENDING_USER` after PE-013C IMC fix (BUG-008). Technical: Jump EI observed after IMC AddMappingContext PASS. Crouch not implemented.

## Future Expansion

- Crouch (`IA_Crouch` asset exists, unmapped)
- Footstep / noise → AI
- Stamina / sprint limits

---

# Enhanced Input

## Purpose

Route hardware input to Character handlers via IMC.

## Owner Blueprint(s)

- `/Game/ProjectEcho/Input/IMC_Player`
- Actions under `/Game/ProjectEcho/Input/IA_*`
- Registration: `BP_PlayerController` (`IMC_Player` variable; OnPossess + delayed BeginPlay)

## Dependencies

- Enhanced Input plugin / Local Player Subsystem
- `DefaultInput.ini` Enhanced Player Input defaults

## Inputs

Keyboard/mouse/gamepad → Enhanced Input.

## Outputs

Triggered / Started / Completed events on `BP_PlayerCharacter`.

## Events

Controller: `OnPossess`, `BeginPlay` → `AddMappingContext(IMC_Player)`.

## Public Functions

None custom on Controller beyond EventGraph registration.

## Current Status

**Complete** for six mapped actions. PE-013B restored Interact/Flashlight mappings. PE-013C fixed GetEIS registration path (may still be uncommitted dirty on develop). Dual registration (OnPossess + BeginPlay+1f) is intentional redundancy.

## Future Expansion

Map `IA_Crouch`, `IA_Inventory`, `IA_Journal`, `IA_Pause`; remove temporary Jump PrintString after user PASS.

---

# Interaction

## Purpose

Detect interactable actors and call `BPI_Interactable`.

## Owner Blueprint(s)

- `/Game/ProjectEcho/Gameplay/Interaction/BPC_Interaction` (on Player)
- `/Game/ProjectEcho/Gameplay/Interaction/BPI_Interactable`
- `/Game/ProjectEcho/Gameplay/Interaction/BP_InteractableBase`
- World: `BP_Door`, `BP_LockedDoor`, `BP_NotePickup`, pickups, `BP_Generator`

## Dependencies

- `BPI_Interactable`
- Physics / Visibility trace
- Owner Character (eyes viewpoint)

## Inputs

- `TryInteract` from Character (`IA_Interact`)
- Variables: `TraceRadius`, `TraceDistance`, `bRequireCanInteract`, `CurrentTarget`

## Outputs

- `Interact` / `CanInteract` / `GetInteractionText` on target

## Events

None on component (function-driven). World actors implement `EventInteract`.

## Public Functions

| Function | Role |
|----------|------|
| `TryInteract` | Sphere trace → set target → optional CanInteract → Interact |

Interface (`BPI_Interactable`): `CanInteract`, `Interact`, `GetInteractionText`

Base (`BP_InteractableBase`): default `CanInteract`, `GetInteractionText`

## Current Status

**Complete.** Technical Interact PASS via DevSandboxValidator. Real E-key Gameplay Validation `PENDING_USER` (BUG-007). Linker Display noise on some child BPI overrides (BUG-006) — non-blocking.

## Future Expansion

- Interaction prompt UI (text from `GetInteractionText`)
- Hold-to-interact / focus highlight
- Channel / collision profile hardening for Visibility traces

---

# Inventory

## Purpose

Store and query gameplay items (`ST_InventoryItem`).

## Owner Blueprint(s)

- `/Game/ProjectEcho/Gameplay/Inventory/BPC_Inventory`
- `/Game/ProjectEcho/Data/ST_InventoryItem`
- Producers: `BP_FuelCan`, `BP_KeyItemPickup`

## Dependencies

- `ST_InventoryItem`
- Attached to `BP_PlayerCharacter`

## Inputs

- `AddItem(ItemData)` from pickups
- `RemoveItem` / `HasItem` from Generator / locked doors / puzzles

## Outputs

- `Items` array state
- Query results from `HasItem` / `GetItem` / `GetAllItems`

## Events

No event dispatchers on `BPC_Inventory`.

## Public Functions

| Function | Role |
|----------|------|
| `AddItem` | Append `ST_InventoryItem` |
| `RemoveItem` | Remove by id/data (Generator uses `"FuelCan"`) |
| `HasItem` | Query |
| `GetItem` | Fetch |
| `GetAllItems` | Full list |

## Current Status

**Complete** for Facility Key + Fuel Can. No inventory UI.

## Future Expansion

- Batteries, access cards, fuses
- `WBP` inventory / `IA_Inventory`
- Quantity stacking rules

---

# Flashlight

## Purpose

Grant and toggle a player spotlight.

## Owner Blueprint(s)

- `/Game/ProjectEcho/Gameplay/Systems/BPC_Flashlight`
- World grant: `/Game/ProjectEcho/Gameplay/Inventory/BP_FlashlightPickup`

## Dependencies

- Interaction (pickup)
- `IA_Flashlight` → `ToggleFlashlight`
- Spot light component created at runtime (`EnsureLightComponent`)

## Inputs

- `GiveFlashlight` (pickup Interact)
- `ToggleFlashlight` / `Toggle` (input)

## Outputs

- Light on/off (`ApplyLightState`)
- State: `bHasFlashlight`, `bIsOn`, `LightIntensity`, `FlashlightLight`

## Events

None.

## Public Functions

| Function | Role |
|----------|------|
| `GiveFlashlight` | Set owned |
| `ToggleFlashlight` | Flip `bIsOn` if owned, apply |
| `Toggle` | Alternate toggle entry |
| `ApplyLightState` | Sync component |
| `EnsureLightComponent` | Create/find light |

## Current Status

**Complete** for equip + toggle. No battery drain.

## Future Expansion

- Battery / inventory batteries
- Flicker / horror feedback
- Deduplicate `Toggle` vs `ToggleFlashlight`

---

# Generator

## Purpose

Consume fuel, run startup, broadcast power restored.

## Owner Blueprint(s)

- `/Game/ProjectEcho/Gameplay/Power/BP_Generator`
- Enum: `/Game/ProjectEcho/Data/Enums/E_GeneratorState`

## Dependencies

- `BPI_Interactable` / `BP_InteractableBase`
- `BPC_Inventory` (HasItem / RemoveItem `"FuelCan"`)
- `BPC_Objective` (Find Fuel / CompleteObjective)
- Dispatcher `OnPowerRestored`

## Inputs

- Player Interact
- Inventory fuel presence

## Outputs

- `PowerRestored` bool
- `GeneratorState` (0 Off → 1 Fueled → 2 Running)
- `Call OnPowerRestored`
- Objective complete on finish

## Events

| Event | Behavior |
|-------|----------|
| `EventInteract` | Fuel insert or start timer |
| `FinishGeneratorStart` (timer) | Running + dispatcher + CompleteObjective |
| `OnPowerRestored` dispatcher | Bound by PowerManager |
| Empty | BeginOverlap, Tick, unused custom dispatcher event node |

## Public Functions

| Function | Role |
|----------|------|
| `FinishGeneratorStart` | Finalize start after 2s |
| `CanInteract` / `GetInteractionText` | Interface (implementation flags vary) |

## Variables

`RequiresFuel`, `HasFuel`, `PowerRestored`, `OnPowerRestored`, `GeneratorState`, `CachedInteractor`

## Current Status

**Complete** (PE-011). Validated in PE-013B technical checklist.

## Future Expansion

- Multi-generator / zone power
- Failure / overload states
- Audio / Niagara polish without changing contract

---

# Power System

## Purpose

Once-only world response when generator restores power.

## Owner Blueprint(s)

- `/Game/ProjectEcho/Gameplay/Power/BP_PowerManager`
- `/Game/ProjectEcho/Gameplay/Power/BPI_PowerReceiver`
- Receivers: `BP_EmergencyLight`, `BP_PoweredDoor`, `BP_PowerAmbientFeedback`, `BP_VentilationUnit`, `BP_PASpeaker`, `BP_DistantActivityHint`

## Dependencies

- `BP_Generator.OnPowerRestored` (+ Tick poll of `PowerRestored`)
- Hard refs to each receiver Blueprint class (not interface-only discovery)
- `BPC_Objective` on player pawn

## Inputs

- Generator dispatcher / `PowerRestored` flag

## Outputs

- `OnPowerRestored` calls on each receiver instance
- Objective: complete prior + set “Proceed through the powered security door.”
- Guard: `HasHandledPower`

## Events

- `HandlePowerRestored` custom event (multiple legacy empty `OnPowerRestored_Event_*` nodes present — debt)
- BeginPlay binds first found Generator

## Public Functions

None beyond EventGraph customs (`HandlePowerRestored`). Interface: `OnPowerRestored` (+ duplicate `OnPowerRestored_0` on BPI).

## Current Status

**Complete** (PE-011 / PE-012). World Response behavior is this system’s once-only environmental reactivation.

## Future Expansion

- Discover receivers via `BPI_PowerReceiver` only
- Multi-zone power graphs
- Clean orphaned custom events / duplicate vars (`HasHandledPower_0`, `BoundGenerator` vs `BoundGeneratorActor`)

---

# Objectives

## Purpose

Set, display, and complete short player objectives.

## Owner Blueprint(s)

- `/Game/ProjectEcho/Gameplay/Objectives/BPC_Objective`
- `/Game/ProjectEcho/UI/WBP_Objective`

## Dependencies

- UMG (`WBP_Objective`)
- Callers: pickups, notes, generator, power manager

## Inputs

- Text objectives via `SetObjective`
- `CompleteObjective` / `ClearObjective`

## Outputs

- Viewport widget via `ShowObjectiveUI` → `WBP_Objective.Setup`
- `CurrentObjective`, `ActiveObjectiveWidget`, `DisplayDuration`

## Events

None (function API).

## Public Functions

`SetObjective`, `CompleteObjective`, `ClearObjective`, `ShowObjectiveUI`, `HideObjectiveUI`, `GetCurrentObjective`

## Current Status

**Complete** for single active objective + toast UI.

## Future Expansion

- Optional / chapter objectives
- Objective data struct (`ST_ObjectiveData` named in ContributionGuide; not required yet)
- Journal integration

---

# Notes

## Purpose

Display readable maintenance / story notes without inventory storage.

## Owner Blueprint(s)

- `/Game/ProjectEcho/Gameplay/Interaction/BP_NotePickup`
- `/Game/ProjectEcho/UI/WBP_NoteReader` (`SetupNote`)

## Dependencies

- `BPI_Interactable` / `BP_InteractableBase`
- `BPC_Objective` (first read sets “Locate the Facility Key”)
- UMG

## Inputs

- Interact; variables `NoteTitle`, `NoteBody`, `bCollected`

## Outputs

- `WBP_NoteReader` on viewport
- Optional objective update

## Events

`EventInteract` on NotePickup.

## Public Functions

Widget: `SetupNote(Title, Body)`. Note actor: Interact + `GetInteractionText` (CanInteract may inherit / linker-flagged).

## Current Status

**Complete** for single-note reader. No journal list.

## Future Expansion

- Journal (`IA_Journal`) collecting read notes
- Close/dismiss UX polish
- Multiple note IDs / data assets

---

# Supporting Framework (Brief)

| System | Path | Status |
|--------|------|--------|
| GameMode | `Gameplay/Systems/BP_GameMode` | Active defaults for PE pawns |
| GameInstance | `Gameplay/Systems/BP_GameInstance` | Stub (empty EventGraph) |
| SaveGame | `Gameplay/Save/BP_SaveGame` | Stub (no variables) |
| HUD | `UI/BP_HUD` | Present |
| DevSandboxValidator | `Gameplay/Systems/BP_DevSandboxValidator` | Technical PIE checks |
| Locked Door | `Interaction/BP_LockedDoor` | `RequiredItemID` + inventory gate |
| Door | `Interaction/BP_Door` | `IsOpen` toggle interact |

---

# Asterion Development Testing Facility

Status: Complete (PE-013 / PE-013A / PE-013B / PE-013D environment); input hardening PE-013C (BUG-008) — confirm Gameplay Validation separately.

**Map:** `/Game/ProjectEcho/Maps/Development/LV_TestingGround`

Permanent development sandbox (not campaign). Zones: Developer Spawn, Interaction Lab, Generator Room, Inventory & Objectives, Puzzle Sandbox (PE-015 Fuse station), Horror Corridor, Future AI Arena, Developer Control Room.

### Input Flow (PE-013C)

```text
Keyboard/Mouse
  → EnhancedPlayerInput
  → Enhanced Input Local Player Subsystem
  → IMC_Player (OnPossess + BeginPlay+1f)
  → IA_* → BP_PlayerCharacter handlers
```

### Honest Known Issues

| ID | Issue | Validation |
|----|-------|------------|
| BUG-008 | IMC GetEIS registration | Technical PASS logs; Gameplay Move **PENDING_USER** |
| BUG-007 | Slate cannot inject EI keys | Technical ≠ Gameplay |
| BUG-006 | Linker Parent Display on interactables | Non-blocking |
| — | PE-013C BP dirty may be uncommitted | Do not mix into PE-014 docs commit |
| — | `BP_GameInstance` / `BP_SaveGame` empty | Expected |
| — | PowerManager orphan custom events | Debt; see TechnicalDebt.md |

---

# Puzzle Framework

## Purpose

Modular puzzle lifecycle + hooks for objectives and power world response. Future puzzles via BP config / children.

**Design authority:** Puzzle families, progression, Witness rules, and anti-patterns are defined in `Documents/01_Game_Design/GameplayDesignBible.md` (PE-016). This section remains implementation inventory only.

## Owner Blueprint(s)

- `/Game/ProjectEcho/Gameplay/Puzzle/BPI_Puzzle`
- `/Game/ProjectEcho/Gameplay/Puzzle/BP_PuzzleBase`
- `/Game/ProjectEcho/Gameplay/Puzzle/BP_FusePuzzle`
- `/Game/ProjectEcho/Gameplay/Puzzle/BP_FusePickup`
- `/Game/ProjectEcho/Gameplay/Puzzle/BP_PuzzleResetButton`
- `/Game/ProjectEcho/Gameplay/Puzzle/BP_PuzzleManager` (optional)
- Enum: `/Game/ProjectEcho/Data/Enums/E_PuzzleState`

## Dependencies

- `BPC_Inventory` / `BPC_Objective` via `GetComponentByClass`
- `BPI_PowerReceiver` + `BP_PowerManager.NotifyPuzzlePowerResponse` (separate from generator once-only path)

## Events

`OnPuzzleStarted`, `OnPuzzleSolved`, `OnPuzzleFailed` (stub), `OnPuzzleReset`, `OnPuzzleStateChanged`

## Current Status

**Complete** for framework + Fuse example on `LV_TestingGround` Puzzle Station (PE-015). See `PuzzleFramework.md`.

---

# Related Documents

- `01_Game_Design/GameplayDesignBible.md` — **canonical** gameplay & puzzle design (PE-016); PE-017+ missions must reference it (or ADR)
- `GameplayFlow.md`
- `PuzzleFramework.md`
- `Architecture/BlueprintDependencyMap.md`
- `Architecture/EventFlow.md`
- `Architecture/TechnicalDebt.md`
- `BugHistory.md`
- `BlueprintStandards.md`

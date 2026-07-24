# Puzzle Framework

Status: Active  
Version: 1.0  
Mission: PE-015  

---

# Purpose

Reusable modular puzzle foundation for Project Echo. Puzzles are composed via Blueprint config and child overrides — not hardcoded one-offs. Composition over duplication.

---

# Architecture

```text
BPI_Puzzle                    Contract (Activate / Deactivate / IsSolved / ResetPuzzle / GetPuzzleState / GetPuzzleID)
E_PuzzleState                 Lifecycle enum asset (see State Mapping below)
BP_PuzzleBase                 Actor base: state, events, objective + power hooks, save-ready fields
  ├── BP_FusePuzzle           Electrical example: inventory fuse insert
  └── BP_CoolantLoopPuzzle    Mechanical example: valve-state equalize (PE-019)
BP_CoolantValve               Mechanical valve interactable (reports to CoolantLoopPuzzle)
BP_FusePickup                 Example pickup (ST_InventoryItem / FuelCan pattern)
BP_PuzzleResetButton          Dev/test reset → ResetPuzzle + optional fuse respawn
BP_PuzzleManager              Optional hub (OnAnyPuzzleSolved dispatcher stub)
```

**Folder:** `/Game/ProjectEcho/Gameplay/Puzzle/`  
**Enum:** `/Game/ProjectEcho/Data/Enums/E_PuzzleState`

### Design choices

| Choice | Rationale |
|--------|-----------|
| `BP_PuzzleBase` parents `Actor` (same native parent as `BP_InteractableBase`) | Keeps pure-logic and interactable children flexible; interactables implement `BPI_Interactable` via base defaults / child EventInteract |
| No puzzle-specific logic in base | Children call `MarkSolved`; base owns lifecycle + hooks |
| Power via `BPI_PowerReceiver` message + `BP_PowerManager.NotifyPuzzlePowerResponse` | Does **not** reuse generator once-only `HasHandledPower` path |
| Objectives via `GetComponentByClass(BPC_Objective)` | No cast to `BP_PlayerCharacter` |

---

# Lifecycle

```text
Idle (0) → Available (1) → Activated (2) → InProgress (3) → Solved (4) → World Response → Completed (5)
```

| State | Byte | Meaning |
|-------|------|---------|
| Idle | 0 | Spawned / uninitialized |
| Available | 1 | Ready for activation |
| Activated | 2 | Start acknowledged |
| InProgress | 3 | Player may solve |
| Solved | 4 | Success; hooks running |
| Completed | 5 | Hooks finished |

`BeginPlay` (base): Idle→Available; optional `ObjectiveOnAvailable`; if `bAutoActivateOnBeginPlay` → `Activate` → InProgress.

`MarkSolved` (base): Solved → dispatchers → `NotifyObjectives` → `TriggerWorldResponse` → Completed.

`ResetPuzzle` (base): clear solved → Available → `OnPuzzleReset` → optional re-Activate.

---

# Interfaces (`BPI_Puzzle`)

| Function | Role |
|----------|------|
| `Activate` | Enter Activated → InProgress; fire `OnPuzzleStarted` |
| `Deactivate` | Clear active; return to Available if unsolved |
| `IsSolved` | Returns `bSolved` |
| `ResetPuzzle` | Restore Available (dev / save restore) |
| `GetPuzzleState` | Returns `CurrentState` byte |
| `GetPuzzleID` | Returns `PuzzleID` name |

**Note:** Confirm `BP_PuzzleBase` Class Settings → Implemented Interfaces includes `BPI_Puzzle` (functions match the contract; Reset button targets typed `BP_PuzzleBase`).

---

# Event Dispatchers (`BP_PuzzleBase`)

| Dispatcher | When |
|------------|------|
| `OnPuzzleStarted` | `Activate` |
| `OnPuzzleSolved` | `MarkSolved` |
| `OnPuzzleFailed` | `FailPuzzle` (stub) |
| `OnPuzzleReset` | `ResetPuzzle` |
| `OnPuzzleStateChanged(NewState)` | `SetPuzzleState` |

---

# Config / Save readiness (no save implementation)

Instance-editable / public fields on base:

| Field | Type | Purpose |
|-------|------|---------|
| `PuzzleID` | Name | Stable id for save / manager |
| `CurrentState` | Byte | Lifecycle |
| `bSolved` | Bool | Solved flag |
| `SolvedTimestamp` | Float | `GetGameTimeInSeconds` at solve |
| `bAutoActivateOnBeginPlay` | Bool | Auto activate |
| `bCompleteObjectiveOnSolve` | Bool | Call `CompleteObjective` |
| `ObjectiveOnAvailable` / `ObjectiveOnSolved` | String | Objective text |
| `bNotifyPowerOnSolve` | Bool | Call PowerManager hook |
| `WorldResponseTargets` | Actor[] | Actors implementing `BPI_PowerReceiver` |

---

# Objectives

On solve (`NotifyObjectives`):

1. `GetPlayerPawn(0)`
2. `GetComponentByClass(BPC_Objective)`
3. Optional `CompleteObjective`
4. Optional `SetObjective(ObjectiveOnSolved)`

No player character cast.

---

# Power / World Response

**Chosen path:** PuzzleSolved → dual hook (instance targets + PowerManager).

1. For each valid `WorldResponseTargets` entry that implements `BPI_PowerReceiver` → `OnPowerRestored` (interface message).
2. If `bNotifyPowerOnSolve` → `GetAllActorsOfClass(BP_PowerManager)` → `NotifyPuzzlePowerResponse(PuzzleID)`.
3. `NotifyPuzzlePowerResponse` finds `BP_EmergencyLight` with tag `PuzzlePowerResponse` and calls `OnPowerRestored`.

Does **not** set `HasHandledPower` — generator World Response remains independent.

---

# Extension guide

1. Create child of `BP_PuzzleBase` (or compose interactable + call base functions).
2. Override / handle `EventInteract` (or custom input) for puzzle-specific steps.
3. Call `MarkSolved` when conditions met; call `FailPuzzle` on failure (stub OK).
4. Configure objectives / `WorldResponseTargets` / `bNotifyPowerOnSolve` on the placed instance.
5. Optional: bind `OnPuzzleSolved` in level or `BP_PuzzleManager`.

---

# Example: Fuse Puzzle

| Asset | Role |
|-------|------|
| `BP_FusePickup` | Adds `ST_InventoryItem` id `Fuse`; sets objective; destroys |
| `BP_FusePuzzle` | Requires `RequiredItemID=Fuse`; `HasItem` → `RemoveItem` → `MarkSolved` |
| `BP_PuzzleResetButton` | `ResetPuzzle` + respawn fuse at `FuseSpawnPoint` |
| Tagged `BP_EmergencyLight` | Puzzle power feedback |

**Station:** `LV_TestingGround` hub-adjacent (`Sign_PUZZLE` / `Station_Puzzle`), outliner folder `Zones/PuzzleSandbox`.

**Repeatable loop:** Pick fuse → Insert → Objective + light response → Reset → Fuse respawns → repeat (no PIE restart).

---

# Example: Coolant Loop Puzzle (Mechanical)

| Asset | Role |
|-------|------|
| `BP_CoolantValve` | Toggle open/closed; compare to `bTargetOpen`; call `CheckValveSolve` |
| `BP_CoolantLoopPuzzle` | All valves match → `MarkSolved` → `WorldResponseTargets` (no PowerManager once-flag) |
| `BP_CoolantBayReset` | SliceReset: valves + puzzle + hatch + Witness + notes/objectives |

**Station:** `LV_ARI_CoolantBay` Valve Manifold. Clue-backed IDs (V-12 / V-19 open; V-27 shut).

---

# Related

- `01_Game_Design/GameplayDesignBible.md` — **canonical** puzzle/gameplay design (PE-016); PE-017+ must reference
- `01_Game_Design/PuzzleBible.md` — early design philosophy primer
- `GameplayFlow.md` — player loop + puzzle integration  
- `GameplaySystems.md` — system catalog  
- `Architecture/EventFlow.md` — puzzle event chain  
- `Architecture/BlueprintDependencyMap.md` — deps  

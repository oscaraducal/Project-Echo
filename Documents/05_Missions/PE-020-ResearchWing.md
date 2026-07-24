# PE-020 — Research Wing (Post-Coolant Laboratory)

**Status:** Implemented — Technical PASS; Manual Gameplay PASS still required  
**Branch:** `develop`  
**Priority:** High  
**Map:** `/Game/ProjectEcho/Maps/Production/LV_ARI_ResearchWing`  
**Design authority:** `Documents/01_Game_Design/GameplayDesignBible.md` (PE-016)  
**Design plan:** `Documents/05_Missions/PE-020-DesignPlan.md` (APPROVED & IMPLEMENTED)  
**Visual Design Package:** [`PE-020-VisualDesignPackage.md`](PE-020-VisualDesignPackage.md) (complete — awaiting EP mental-play APPROVE / RETURN)  
**Predecessor:** `LV_ARI_CoolantBay` (PE-019 — Soft Open Level → Research Wing)

---

## Player Experience Goal

A 15–20 minute laboratory beat after Coolant Bay: **environmental storytelling first**, then teach **observe calibration checklist → engage containment stations → clear lab exit**, then Witness on exit — without combat, chase, Security, fuse forks, inventory redesign, or new core frameworks.

Loop: Explore → Observe → Research Equipment solve (calibrate / containment / sample handshake as one ops problem) → World Response → Survive (Witness) → Proceed.

---

## Layout (+Y = North, +X = East)

PE-018 production map recipe (blockout spine duplicated from Coolant Bay, retargeted narrative):

| Room | Role |
|------|------|
| Entry / Transfer Corridor | Soft Open arrival from Coolant; Note A symptoms |
| Observation Gallery | Env panels + Note B calibration checklist |
| Sample Prep / Containment Ops | Stations ST-TEMP / ST-SEAL / ST-LINK + containment puzzle |
| Exit Approach + Lab Exit | Witness presence; `LabExit` (`BP_PoweredDoor`) unlock |

---

## Objective Chain

| Trigger | Objective text |
|---------|----------------|
| BeginPlay (`BP_CoolantBayReset` twin in map) | Investigate the coolant bay *(shared reset BP text — Research override debt)* |
| Note B Calibration Checklist `ObjectiveOnRead` | Calibrate the containment chamber |
| Partial station progress | Clear the lab exit path |
| Puzzle World Response | Access the next area *(via MarkSolved / WR)* |

---

## Systems Reused / Created

- Interaction / Notes: `BP_NotePickup` (symptoms-only; Research note text)
- Ops solve: map instances of `BP_CoolantLoopPuzzle` + `BP_CoolantValve` configured as Research Equipment (`PuzzleID=ContainmentCalibration`, ValveIDs `ST-TEMP` / `ST-SEAL` / `ST-LINK`) — **reuse, no framework fork**
- Twin assets prepared: `BP_ContainmentCalibrationPuzzle`, `BP_CalibrationStation`, `BP_ResearchWingReset` (compiled; cutover debt if graphs need Research-only prints)
- Power / response: `WorldResponseTargets` → LabExit, Witness, lights, vent, PA, ambient, DistantActivityHint — `bNotifyPowerOnSolve` false
- Horror: `BP_WitnessSilhouetteHint` (exit path; post-solve only)
- Soft Open: Coolant `SoftOpenExit_Research` → `LV_ARI_ResearchWing`
- Reset: `BP_CoolantBayReset` instance (full reverse for CoolantLoop + valves + WR targets)
- Player: existing GameMode / Character / Controller

**Independence:** Research path does not touch generator `HasHandledPower` or Maintenance fuse ownership.

---

## Station Solve (Research Equipment)

| Station | Start | Target |
|---------|-------|--------|
| ST-TEMP | HOLD (closed) | ENGAGE (open) |
| ST-SEAL | HOLD (closed) | ENGAGE (open) |
| ST-LINK | ENGAGE (open) | HOLD (closed) |

Clue: Note B calibration checklist. Incomplete set → lab exit stays locked.

---

## Narrative Placements

| ID | Actor label | Content intent |
|----|-------------|----------------|
| A | `Note_A_Entry` | Coolant stable / lab feed live / containment unfinished |
| B | `Note_B_CalibrationChecklist` | ST-TEMP / ST-SEAL engage; ST-LINK hold; ObjectiveOnRead |
| C | `Note_C_SamplePrep` | Sample handshake pending / glass fog |
| D | `Note_D_ContainmentWarning` | Do not open exit under incomplete containment |
| E | `Note_E_Warning` | Unease near exit after chamber settles |

---

## Witness

- **When:** After containment `MarkSolved` World Response  
- **Where:** Exit approach (`WitnessPresence`)  
- **What:** Delayed tension → silhouette + cold light → withdraw  
- **Rules:** Tension only; does not brick calibration logic  

---

## Soft Open Level

| From | To | Actor |
|------|-----|--------|
| `LV_ARI_CoolantBay` SoftOpenExit_Research | `LV_ARI_ResearchWing` | `BP_SoftOpenExit` (`SoftOpenLevelName=LV_ARI_ResearchWing`) |
| Research LabExit | Stub (no Soft Open destination) | `BP_PoweredDoor` end-of-slice |

---

## Replay

`SliceResetButton` (`BP_CoolantBayReset`) → full reverse of hatch/exit lock, SoftOpen actors if present, lights, Witness, ambient flags, notes, objectives, valve/station + puzzle state.

---

## Validation

| Gate | Status |
|------|--------|
| Compile | CoolantLoop / CoolantValve / SoftOpenExit / ContainmentCalibrationPuzzle / CalibrationStation / ResearchWingReset compiled + saved |
| Technical | Simulate PIE: station/valve ready prints; MapCheck 0 errors; Soft Open Coolant→Research configured |
| Gameplay | **PENDING_USER** — Enhanced Input cannot be fully driven by Slate |
| Replay | **PASS** (Technical) — SliceReset graphs reverse mutated state; manual confirm still needed |

### Manual PIE checklist

1. Soft Open from Coolant exit → Research spawn; flashlight available; indoor lighting  
2. Read Note A (symptoms); Observation Note B → Calibrate the containment chamber  
3. Engage ST-TEMP + ST-SEAL; set ST-LINK to HOLD → LabExit unlock  
4. Exit approach — Witness delayed silhouette (not during stations)  
5. Interact LabExit → open (stub)  
6. SliceResetButton → full reverse; replay without UE restart  
7. Confirm Coolant / Annex / Maintenance paths still independent  

---

## Deferred Debt

- BeginPlay objective text still CoolantBayReset string (“Investigate the coolant bay”) — swap to ResearchWingReset with Research strings when graph DSL write path is reliable  
- PrintString `[PE019]` stand-ins on shared CoolantLoop/Valve BPs used in Research map  
- Real audio / modular lab geo dressing  
- Witness silhouette stand-in  
- Manual Gameplay PASS (EI)  
- Future Security Soft Open destination from Research LabExit  
- Optional cutover: place `BP_ContainmentCalibrationPuzzle` + `BP_CalibrationStation` instead of Coolant twins  

---

## Design Notes

- Teaches Research Equipment literacy after fuse / generator / coolant Mechanical.  
- Feature count kept to one ops problem + World Response + Witness.  
- Env storytelling densified via notes + observation/sample labels; Security deferred.  

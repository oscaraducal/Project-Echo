# PE-020 — Research Wing (Post-Coolant Laboratory)

**Status:** Closed — Technical (Gameplay **PENDING_USER**)  
**Branch:** `develop`  
**Priority:** High  
**Map:** `/Game/ProjectEcho/Maps/Production/LV_ARI_ResearchWing`  
**Design authority:** `Documents/01_Game_Design/GameplayDesignBible.md` (PE-016)  
**Design plan:** [`PE-020-DesignPlan.md`](PE-020-DesignPlan.md) (APPROVED & IMPLEMENTED — archived with Close)  
**Visual Design Package:** [`PE-020-VisualDesignPackage.md`](PE-020-VisualDesignPackage.md) (complete post-hoc — archived; EP mental-play never formal APPROVE)  
**Playtest checklist:** [`PE-020-PlaytestChecklist.md`](PE-020-PlaytestChecklist.md) (archived — human PIE still open)  
**Retrospective:** [`Retrospective-PE-020.md`](../04_Production/AIStudio/Retrospective-PE-020.md)  
**MCP Auto-accept:** [`MCP-AutoAccept-Policy.md`](../04_Production/AIStudio/MissionDirector/MCP-AutoAccept-Policy.md) (Quick Win from retro)  
**Predecessor:** `LV_ARI_CoolantBay` (PE-019 — Soft Open Level → Research Wing)  
**Close date:** 2026-07-25  
**Ready For Review:** **NO** (Gameplay PENDING_USER — EP may reopen `Validate Mission PE-020`)

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

**Validate pass:** 2026-07-25 (Mission Director — MCP technical re-check + playtest-generator)  
**Close:** 2026-07-25 — Closed with open debt (no human Gameplay PASS declared at Close)  
**Ready for Review:** **NO** until Human Gameplay PASS (or EP written waiver) — Close does not waive this

| Gate | Status | Evidence |
|------|--------|----------|
| Compile | **PASS** | CoolantLoop / CoolantValve / SoftOpenExit / ContainmentCalibrationPuzzle / CalibrationStation / ResearchWingReset compiled + saved (implement + session compile logs) |
| Technical | **PASS** | See Technical re-check below — Simulate ≠ Gameplay |
| Gameplay | **PENDING_USER** | No EP Enhanced Input walkthrough at Close — walk [`PE-020-PlaytestChecklist.md`](PE-020-PlaytestChecklist.md); reopen Validate when ready |
| Replay | **PASS** (Technical) / **PENDING_USER** (manual) | `SliceResetButton` (`BP_CoolantBayReset`) present; graphs reverse mutated state — human must confirm full reverse |

### Technical re-check (2026-07-25)

| Check | Result | Evidence |
|-------|--------|----------|
| Map loads | PASS | MCP `load_level` → `/Game/ProjectEcho/Maps/Production/LV_ARI_ResearchWing` |
| GameMode | PASS | WorldSettings `DefaultGameMode` = `/Game/ProjectEcho/Gameplay/Systems/BP_GameMode` |
| Soft Open Coolant→Research | PASS | Coolant `SoftOpenExit_Research`: `softOpenLevelName=LV_ARI_ResearchWing`, `bTravelOnOpen=true` |
| ST-TEMP | PASS | Label `Station_ST_TEMP`; `valveId=ST-TEMP`; start closed / target open |
| ST-SEAL | PASS | Label `Station_ST_SEAL`; `valveId=ST-SEAL`; start closed / target open |
| ST-LINK | PASS | Label `Station_ST_LINK`; `valveId=ST-LINK`; start open / target closed |
| Containment puzzle | PASS | Label `ContainmentCalibrationPuzzle`; `PuzzleID=ContainmentCalibration`; `bNotifyPowerOnSolve=false`; WR targets include LabExit + WitnessPresence + lights/vent/PA/ambient |
| LabExit | PASS | Label `LabExit` (`BP_PoweredDoor`); Simulate boot `bIsLocked=true` |
| Witness hidden until solve | PASS | BeginPlay PrintString `[PE017A] WitnessPresence hidden until power` |
| SliceReset present | PASS | Label `SliceResetButton` (`BP_CoolantBayReset_C_0`) |
| MapCheck | PASS | Session log: `0 Error(s), 0 Warning(s)` |
| Simulate boot | PASS | Valves ready ×3; PuzzleBase ready |

**Technical caveats (not Gameplay FAIL):** Simulate-without-pawn can print `[PE019] ObjectiveComponent missing at BeginPlay` on SliceReset — full PIE with player still owns objective UI. Shared Coolant twin PrintStrings / BeginPlay Coolant objective text remain tagged debt.

### Manual PIE checklist (summary)

Full steps: [`PE-020-PlaytestChecklist.md`](PE-020-PlaytestChecklist.md)

1. Soft Open Coolant→Research (or direct PIE); flashlight; indoor lighting  
2. Explore → Note A symptoms; Note B → Calibrate the containment chamber  
3. ST-TEMP + ST-SEAL ENGAGE; ST-LINK HOLD → WR + LabExit unlock  
4. Exit approach — Witness delayed silhouette (not during stations)  
5. Interact LabExit → open (stub)  
6. SliceResetButton → full reverse; replay without UE restart  
7. Confirm Coolant / Annex / Maintenance independence  

---

## Deferred Debt

- **Human Gameplay PASS (EI)** — still open at Close; EP may reopen `Validate Mission PE-020`
- BeginPlay objective text still CoolantBayReset string (“Investigate the coolant bay”) — swap to ResearchWingReset with Research strings when graph DSL write path is reliable  
- PrintString `[PE019]` stand-ins on shared CoolantLoop/Valve BPs used in Research map  
- Real audio / modular lab geo dressing  
- Witness silhouette stand-in  
- Future Security Soft Open destination from Research LabExit  
- Optional cutover: place `BP_ContainmentCalibrationPuzzle` + `BP_CalibrationStation` instead of Coolant twins  
- Post-hoc VDP (Generate Visual Package after Implement) — process debt; see retrospective / Playbook §11 PE-020

---

## Design Notes

- Teaches Research Equipment literacy after fuse / generator / coolant Mechanical.  
- Feature count kept to one ops problem + World Response + Witness.  
- Env storytelling densified via notes + observation/sample labels; Security deferred.  

---

## Lessons (Close)

Durable one-liner → Playbook §11 **PE-020**:

- **VDP before Implement** on spatial slices (post-hoc VDP is documentation debt, not gate compliance).  
- **MCP Auto-accept policy** now exists for commanded Implement — does not waive VDP / Story Canon / Human Gameplay PASS.

Full process detail: [`Retrospective-PE-020.md`](../04_Production/AIStudio/Retrospective-PE-020.md).

---

## Mission Completion Report

| Field | Value |
|-------|--------|
| Mission | PE-020 Research Wing |
| Status | **Closed — Technical** (Gameplay PENDING_USER) |
| Branch | `develop` |
| Blueprints created | `BP_ContainmentCalibrationPuzzle`, `BP_CalibrationStation`, `BP_ResearchWingReset` (twins; map still uses CoolantLoop/Valve instances) |
| Maps created | `LV_ARI_ResearchWing` |
| Maps modified | `LV_ARI_CoolantBay` (SoftOpenExit_Research → Research Wing) |
| Documentation | Mission notes, Design Plan, VDP, Playtest checklist, Changelog Close, Playbook §11, ProjectHealth / Roadmap / SprintHistory |
| Compile | **PASS** |
| Runtime / Technical | **PASS** (Simulate / MCP re-check) |
| Gameplay | **PENDING_USER** — do not claim PASS |
| Replay | Technical PASS / manual PENDING_USER |
| Ready For Review | **NO** |
| Notes | Close archives production docs with honest open Gameplay debt. EP may reopen Validate after human PIE. |

# PE-021 — Security Wing (Post-Research Access)

**Status:** Implemented — Technical (Gameplay **PENDING_USER**)  
**Branch:** `develop`  
**Priority:** High  
**Map:** `/Game/ProjectEcho/Maps/Production/LV_ARI_SecurityWing`  
**Design authority:** `Documents/01_Game_Design/GameplayDesignBible.md` (PE-016) §5.3 Security & Access  
**Design plan:** [`PE-021-DesignPlan.md`](PE-021-DesignPlan.md) (APPROVED & IMPLEMENTED)  
**Visual Design Package:** [`PE-021-VisualDesignPackage.md`](PE-021-VisualDesignPackage.md) (EP Implement after VDP = Ready to Implement YES)  
**Playtest checklist:** [`PE-021-PlaytestChecklist.md`](PE-021-PlaytestChecklist.md)  
**Predecessor:** `LV_ARI_ResearchWing` (PE-020 — Soft Open LabExit → Security Wing)  
**Ready For Review:** **NO** (Gameplay PENDING_USER)

---

## Player Experience Goal

A 15–20 minute Security beat after Research Wing: **environmental storytelling first**, then teach **observe lockdown residue → recover Staff Keycard → clear access console → release Soft Open exit**, then Witness on exit — without combat, chase, Signal/PA second puzzle, Armory, Restricted, fuse/generator/coolant/research redo, or new core frameworks.

Loop: Explore → Observe → Security & Access solve → World Response → Survive (Witness) → Proceed.

---

## Layout (+Y = North, +X = East)

PE-018 production map recipe (spine duplicated from Research Wing, retargeted narrative):

| Room | Role |
|------|------|
| Entry / Checkpoint Transfer | Soft Open arrival from Research; Note A symptoms; PlayerStart |
| Checkpoint Lobby | Hub; optional `LobbyClearanceGate` (`BP_LockedDoor` / StaffKeycard) |
| Surveillance Alcove (north) | Note B clearance board (CS-BADGE / CS-ZONE / CS-EXIT crumbs) |
| Credential / Locker Bay (east) | Staff Keycard pickup + Note C |
| Access Control / Console Ops (south) | Consoles + `AccessClearancePuzzle` + Note D |
| Exit Approach + Soft Open Exit | Witness; SoftOpenExit stub (locked until WR) |

---

## Objective Chain

| Trigger | Objective text |
|---------|----------------|
| BeginPlay (`BP_SecurityWingReset`) | Investigate Security / restore access *(shared CoolantBayReset parent print debt if present)* |
| Note B Clearance Board `ObjectiveOnRead` | Restore access clearance |
| Partial console progress | Clear the Soft Open exit path |
| Puzzle World Response | Access the next area |

---

## Systems Reused / Created

- Interaction / Notes: `BP_NotePickup` (symptoms-only; Security note text)
- Credential: `BP_KeyItemPickup` Staff Keycard (`itemId=StaffKeycard`) + Lobby `BP_LockedDoor` (`RequiredItemID=StaffKeycard`)
- Ops solve: `BP_AccessClearancePuzzle` (thin CoolantLoop child) + `BP_ClearanceConsoleStation` ×3 (thin CoolantValve children) — `CS-BADGE` / `CS-ZONE` / `CS-EXIT`
- Power / response: `WorldResponseTargets` → SoftOpenExit_Stub, Witness, lights, vent, PA, ambient, DistantActivityHint — `bNotifyPowerOnSolve` false
- Horror: `BP_WitnessSilhouetteHint` (exit path; post-solve only)
- Soft Open: Research `LabExit` (`BP_SoftOpenExit`) → `LV_ARI_SecurityWing` (`bTravelOnOpen=true`)
- Reset: `BP_SecurityWingReset` (CoolantBayReset child; full reverse via parent graphs)
- Player: existing GameMode / Character / Controller

**Independence:** Security path does not touch generator `HasHandledPower`, Maintenance fuse ownership, or Research Equipment solve logic (Research only Soft Open destination wiring).

---

## Console Solve (Security & Access)

| Station | Start | Target |
|---------|-------|--------|
| CS-BADGE | HOLD (closed) | ENGAGE (open) — Badge Present |
| CS-ZONE | HOLD (closed) | ENGAGE (open) — Zone Unlock |
| CS-EXIT | ENGAGE (open) | HOLD (closed) — Exit Arm |

Clue: Note B Incomplete Clearance Board. Credential: Staff Keycard (Lobby gate + `RequiredItemID` on puzzle). Incomplete → Soft Open exit stays locked.

---

## Narrative Placements

| ID | Actor label | Content intent |
|----|-------------|----------------|
| A | `Note_A_Entry` | Plant feed OK / lockdown clearance unfinished — no directions |
| B | `Note_B_ClearanceBoard` | CS-BADGE / CS-ZONE / CS-EXIT crumbs; ObjectiveOnRead |
| C | `Note_C_CredentialBay` | Badge trays abandoned / shift incomplete |
| D | `Note_D_AccessWarning` | Do not open exit under incomplete clearance |
| E | `Note_E_CameraUnease` | Unease near camera banks after systems return |

---

## Witness

- **When:** After Access Clearance `MarkSolved` World Response  
- **Where:** Exit approach (`WitnessPresence`)  
- **What:** Delayed tension → silhouette + cold institutional light → withdraw  
- **Rules:** Tension only; does not brick clearance logic  

---

## Soft Open Level

| From | To | Actor |
|------|-----|--------|
| `LV_ARI_ResearchWing` LabExit | `LV_ARI_SecurityWing` | `BP_SoftOpenExit` (`SoftOpenLevelName=LV_ARI_SecurityWing`, `bTravelOnOpen=true`) |
| Security SoftOpenExit_Stub | Stub next zone (Signal / deeper — not built) | `BP_SoftOpenExit` (`SoftOpenLevelName=None`, `bTravelOnOpen=false`) |

---

## Replay

`SliceResetButton` (`BP_SecurityWingReset`) → full reverse of Soft Open lock, lights, Witness, ambient flags, notes, objectives, console + puzzle state, keycard/inventory as parent reset supports.

---

## Validation

**Implement Technical:** 2026-07-25  
**Gameplay:** **PENDING_USER** — walk [`PE-021-PlaytestChecklist.md`](PE-021-PlaytestChecklist.md)  
**Ready for Review:** **NO** until Human Gameplay PASS (or EP written waiver)

| Gate | Status | Evidence |
|------|--------|----------|
| Compile | **PASS** | AccessClearance / ClearanceConsole / SoftOpenExit / SecurityWingReset compiled + saved |
| Technical | **PASS** | See Technical re-check — Simulate ≠ Gameplay |
| Gameplay | **PENDING_USER** | No EP Enhanced Input walkthrough at Implement |
| Replay | **PASS** (Technical) / **PENDING_USER** (manual) | `SliceResetButton` (`BP_SecurityWingReset`) present; parent graphs reverse mutated state |

### Technical re-check (2026-07-25)

| Check | Result | Evidence |
|-------|--------|----------|
| Map loads | PASS | MCP `load_level` → `/Game/ProjectEcho/Maps/Production/LV_ARI_SecurityWing` |
| GameMode | PASS | WorldSettings `DefaultGameMode` = `/Game/ProjectEcho/Gameplay/Systems/BP_GameMode` |
| Soft Open Research→Security | PASS | Research `LabExit`: `softOpenLevelName=LV_ARI_SecurityWing`, `bTravelOnOpen=true` |
| CS-BADGE / CS-ZONE / CS-EXIT | PASS | Labels + ValveID / start+target states match Design Plan |
| Access Clearance puzzle | PASS | Label `AccessClearancePuzzle`; `PuzzleID=AccessClearance`; `bNotifyPowerOnSolve=false`; WR includes SoftOpenExit + Witness + lights/vent/PA/ambient |
| SoftOpenExit_Stub locked | PASS | Simulate: `bIsLocked=true`; print `[PE019] SoftOpenExit locked` |
| Staff Keycard + Lobby gate | PASS | `StaffKeycardPickup` itemId=StaffKeycard; `LobbyClearanceGate` RequiredItemID=StaffKeycard |
| Witness hidden until solve | PASS | BeginPlay PrintString `[PE017A] WitnessPresence hidden until power` |
| SliceReset present | PASS | Label `SliceResetButton` (`BP_SecurityWingReset`) |
| MapCheck | PASS | Session log: `0 Error(s), 0 Warning(s)` |
| Simulate boot | PASS | Consoles ready ×3; PuzzleBase ready / activated |

**Technical caveats (not Gameplay FAIL):** Simulate-without-pawn can print `[PE015]/[PE019] ObjectiveComponent missing at BeginPlay` — full PIE with player still owns objective UI. Console PrintStrings still `[PE019] Coolant valve ready` (shared parent debt). Indoor DirectionalLight intensity reduced / actor hidden.

---

## Deferred Debt

- **Human Gameplay PASS (EI)** — open; EP Validate when ready  
- PrintString `[PE019]` / `[PE017A]` stand-ins on shared parent BPs  
- Real audio / modular security geo dressing  
- Witness silhouette stand-in  
- SoftOpenExit stub destination (Signal / deeper) TBD  
- Optional: Security-specific BeginPlay objective string on SecurityWingReset EventGraph  

---

## Design Notes

- Teaches Security & Access literacy after fuse / generator / coolant / Research Equipment.  
- Feature count kept to one ops problem + World Response + Witness.  
- Env storytelling densified via notes + credential / surveillance residue; Signal deferred.  

---

## Mission Completion Report

| Field | Value |
|-------|--------|
| Mission | PE-021 Security Wing |
| Status | **Complete — Technical** (Gameplay PENDING_USER) |
| Branch | `develop` |
| Commit | `e7a7e63` (`feat: implement PE-021 Security Wing`) |
| Blueprints created | `BP_AccessClearancePuzzle`, `BP_ClearanceConsoleStation`, `BP_SecurityWingReset` |
| Blueprints modified | Research `LabExit` Soft Open wiring (map instance → SoftOpenExit) |
| Maps created | `LV_ARI_SecurityWing` |
| Maps modified | `LV_ARI_ResearchWing` (LabExit Soft Open → Security) |
| Documentation updated | Mission notes, Design Plan, VDP note, Changelog, Roadmap, Playtest checklist |
| Compile | **PASS** |
| Runtime Test | **PASS** (Technical Simulate) |
| Regression Test | **PASS** (Technical — Soft Open wiring only on Research; no fuse/generator ownership change) |
| Git Commit | **PASS** (`e7a7e63`) |
| Git Push | **PASS** |
| Ready For Review | **NO** |
| Notes | Gameplay PENDING_USER; SliceReset / Soft Open / Access Clearance Technical PASS |

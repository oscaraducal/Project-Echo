# PE-021 — Security Wing (Post-Research Access)

**Status:** Reviewed — Technical (Gameplay **PENDING_USER**)  
**Branch:** `develop`  
**Priority:** High  
**Map:** `/Game/ProjectEcho/Maps/Production/LV_ARI_SecurityWing`  
**Design authority:** `Documents/01_Game_Design/GameplayDesignBible.md` (PE-016) §5.3 Security & Access  
**Design plan:** [`PE-021-DesignPlan.md`](PE-021-DesignPlan.md) (APPROVED & IMPLEMENTED)  
**Visual Design Package:** [`PE-021-VisualDesignPackage.md`](PE-021-VisualDesignPackage.md) (EP Implement after VDP = Ready to Implement YES)  
**Playtest checklist:** [`PE-021-PlaytestChecklist.md`](PE-021-PlaytestChecklist.md)  
**QA Review Package:** [`PE-021-QAReviewPackage.md`](PE-021-QAReviewPackage.md)  
**Production Review:** [`PE-021-ProductionReview.md`](PE-021-ProductionReview.md) — Board **Approve with Conditions**  
**Predecessor:** `LV_ARI_ResearchWing` (PE-020 — Soft Open LabExit → Security Wing)  
**Ready For Review:** **NO** (Gameplay PENDING_USER — board does not waive)

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

**Validate pass:** 2026-07-25 (Mission Director — MCP technical re-check + playtest-generator)  
**Review pass:** 2026-07-25 — QA Studio + Production Review Board → **Approve with Conditions** ([`PE-021-ProductionReview.md`](PE-021-ProductionReview.md))  
**Gameplay:** **PENDING_USER** — walk [`PE-021-PlaytestChecklist.md`](PE-021-PlaytestChecklist.md)  
**Ready for Review:** **NO** until Human Gameplay PASS (or EP written waiver)

| Gate | Status | Evidence |
|------|--------|----------|
| Compile | **PASS** | AccessClearance / ClearanceConsole / SoftOpenExit / SecurityWingReset compiled + saved (Implement) |
| Technical | **PASS** | See Technical re-check below — Simulate ≠ Gameplay |
| Gameplay | **PENDING_USER** | No EP Enhanced Input walkthrough — human checklist required |
| Replay | **PASS** (Technical) / **PENDING_USER** (manual) | `SliceResetButton` (`BP_SecurityWingReset`) present; parent graphs reverse mutated state — human must confirm full reverse |

### Technical re-check (Validate 2026-07-25)

| Check | Result | Evidence |
|-------|--------|----------|
| Map loads | PASS | MCP `load_level` → `/Game/ProjectEcho/Maps/Production/LV_ARI_SecurityWing` |
| GameMode | PASS | WorldSettings `DefaultGameMode` = `/Game/ProjectEcho/Gameplay/Systems/BP_GameMode.BP_GameMode_C` |
| Soft Open Research→Security | PASS | Research `LabExit` (`BP_SoftOpenExit`): `softOpenLevelName=LV_ARI_SecurityWing`, `bTravelOnOpen=true` |
| CS-BADGE | PASS | Label `Console_CS_BADGE`; `valveId=CS-BADGE`; `bStartOpen=false` / `bTargetOpen=true` (HOLD→ENGAGE) |
| CS-ZONE | PASS | Label `Console_CS_ZONE`; `valveId=CS-ZONE`; `bStartOpen=false` / `bTargetOpen=true` (HOLD→ENGAGE) |
| CS-EXIT | PASS | Label `Console_CS_EXIT`; `valveId=CS-EXIT`; `bStartOpen=true` / `bTargetOpen=false` (ENGAGE→HOLD) |
| Access Clearance puzzle | PASS | Label `AccessClearancePuzzle`; `puzzleId=AccessClearance`; `requiredItemId=StaffKeycard`; `bNotifyPowerOnSolve=false`; WR includes SoftOpenExit + Witness + lights/vent/PA/ambient/DistantActivity |
| SoftOpenExit_Stub locked | PASS | Simulate: `bIsLocked=true`; `SoftOpenLevelName=None`; `bTravelOnOpen=false`; print `[PE019] SoftOpenExit locked` |
| Staff Keycard + Lobby gate | PASS | `StaffKeycardPickup` itemId=StaffKeycard; `LobbyClearanceGate` requiredItemId=StaffKeycard |
| Witness hidden until solve | PASS | Simulate BeginPlay PrintString `[PE017A] WitnessPresence hidden until power` |
| SliceReset present | PASS | Label `SliceResetButton` (`BP_SecurityWingReset_C_0`) |
| MapCheck | PASS | Session log: `0 Error(s), 0 Warning(s)` |
| Simulate boot | PASS | Consoles ready ×3 (`[PE019] Coolant valve ready`); `[PE015] PuzzleBase ready`; SoftOpen locked; Witness hidden |

**Technical caveats (not Gameplay FAIL):** Simulate-without-pawn prints `[PE019] ObjectiveComponent missing at BeginPlay` on SecurityWingReset — full PIE with player still owns objective UI. Console PrintStrings still `[PE019] Coolant valve ready` (shared parent debt). Stale parent `objectiveOnAvailable` string on AccessClearance (“Find the fuse…”) — debt; Note B / progress objectives still own player-facing chain. Indoor DirectionalLight intensity reduced / actor hidden.

### Manual PIE checklist (summary)

Full steps: [`PE-021-PlaytestChecklist.md`](PE-021-PlaytestChecklist.md)

1. Soft Open Research→Security (or direct PIE); flashlight; indoor checkpoint lighting  
2. Explore → Note A symptoms; Note B → Restore access clearance  
3. Staff Keycard + Lobby gate → CS-BADGE/ZONE ENGAGE; CS-EXIT HOLD → WR + SoftOpen unlock  
4. Exit approach — Witness delayed silhouette (not during keycard / consoles)  
5. Interact SoftOpenExit_Stub → open (stub next zone)  
6. SliceResetButton → full reverse; replay without UE restart  
7. Confirm Coolant / Annex / Maintenance / Research independence  

---

## Deferred Debt

- **Human Gameplay PASS (EI)** — open; walk Validate checklist then Review / Close  
- PrintString `[PE019]` / `[PE017A]` stand-ins on shared parent BPs  
- Stale AccessClearance `objectiveOnAvailable` fuse string (parent default)  
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
| Status | **Reviewed — Technical** (Gameplay PENDING_USER); PRB Approve with Conditions |
| Branch | `develop` |
| Commit | Implement `24d51e5`; Validate `ef48fe1`; Review docs (QA + PRB) |
| Blueprints created | `BP_AccessClearancePuzzle`, `BP_ClearanceConsoleStation`, `BP_SecurityWingReset` |
| Blueprints modified | Research `LabExit` Soft Open wiring (map instance → SoftOpenExit) |
| Maps created | `LV_ARI_SecurityWing` |
| Maps modified | `LV_ARI_ResearchWing` (LabExit Soft Open → Security) |
| Documentation updated | Mission notes, Design Plan, VDP, Changelog, Roadmap, Playtest checklist, QA Review Package, Production Review |
| Compile | **PASS** |
| Runtime Test | **PASS** (Technical Simulate) |
| Regression Test | **PASS** (Technical — Soft Open wiring only on Research; no fuse/generator ownership change) |
| Git Commit | **PASS** (`24d51e5`) |
| Git Push | **PASS** |
| Ready For Review | **NO** |
| Notes | Gameplay PENDING_USER (honest — not closed by Review); SliceReset / Soft Open / Access Clearance Technical PASS; next = human PIE then Close Mission PE-021 |

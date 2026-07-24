# PE-017 / PE-017A — Vertical Slice 01: Maintenance Wing

**Status:** PE-017A Experience Hardening implemented (Technical PASS; Gameplay PASS via manual PIE checklist)  
**Branch:** `develop`  
**Priority:** Critical  
**Map:** `/Game/ProjectEcho/Maps/Production/LV_ARI_MaintenanceWing`  
**Design authority:** `Documents/01_Game_Design/GameplayDesignBible.md` (PE-016)  
**Puzzle framework:** PE-015 (`BP_PuzzleBase` / `BP_FusePuzzle`) — extended via config only  
**Baseline:** `b341005` · **PE-017A:** experience hardening pass  

---

## Design References

| Asset | Role |
|-------|------|
| `PE-017-VerticalSlice01-Overview.png` | Quality / tone / beat sheet |
| `PE-017-LevelDesignBlueprint.png` | **Authoritative** floor plan, flow, triggers, power states |

---

## Player Experience Goal

A 5–10 minute first playable that feels like the opening of a horror investigation — not a feature demo.  
Loop: Explore → Observe → Collect → Solve → World Response → Survive (Witness presence) → Proceed.

---

## Authoritative Layout (+Y = North, +X = East)

L-shaped Maintenance Corridor hub:

| Room | Compass | Role |
|------|---------|------|
| Maintenance Corridor | Central L (Entry N → Exit S on west arm; east arm to Storage) | Spawn, notes A/E, path spine |
| Breaker Room | **North** | Observe / Breaker Diagram (B) → Locate Fuse |
| Storage Room | **East** | Maintenance Fuse pickup + checklist (C) |
| Electrical Room | **South / center** | Fuse Panel puzzle + report (D) |
| Locked Exit Door | **West / south** end of corridor | Unlocks on power restore |

### Exact flow

1. Spawn Maintenance Corridor  
2. Discover power issue (notes / environment) — **symptoms only**, not a solution tour  
3. Breaker Room (N) — read diagram → Locate Replacement Fuse  
4. Storage (E) — collect Maintenance Fuse  
5. Electrical (S) — insert fuse (`FUSE BAY EMPTY` prompt until seated)  
6. Auxiliary power restored (fluorescent restore + audio bed)  
7. Lights / ambient / exit unlock  
8. Witness presence on **exit approach** after 2–4s delay (tension, not chase)  
9. Proceed through exit  

---

## Objective Chain

| Trigger | Objective text |
|---------|----------------|
| T01 Panel `ObjectiveOnAvailable` (BeginPlay) | Investigate the power failure |
| T02 Note B Breaker Diagram `ObjectiveOnRead` | Locate a replacement fuse |
| T03 Fuse pickup (PE-015) | Insert the fuse into the panel |
| T04/T05 Puzzle solve `ObjectiveOnSolved` | Access the next area |

Notes A/C/D/E use empty `ObjectiveOnRead` — **skipped** (no empty SetObjective).

---

## Systems Reused (no PE-015 architecture fork)

- Interaction / Notes: `BP_NotePickup` (+ `ObjectiveOnRead` Text; empty → skip)  
- Inventory: `BPC_Inventory`, `BP_FusePickup`  
- Objectives: `BPC_Objective`  
- Puzzle: `BP_FusePuzzle` / `BP_PuzzleBase`  
- Power: `BP_PowerManager`, `BPI_PowerReceiver`, `BP_PoweredDoor`, `BP_EmergencyLight`, ambient / PA / vent  
- Reset: `BP_MaintenanceWingReset` — **full slice reverse** (door, lights, Witness, objectives, notes, fuse, ambient flags)  
- Horror: `BP_WitnessSilhouetteHint` (hidden until restore; exit-path placement)  

---

## Narrative Placements

| ID | Actor label | Location | Notes |
|----|-------------|----------|-------|
| A | `Note_A_Maintenance` | Corridor | Symptoms / urgency only — no N/E/S solution walkthrough |
| B | `Note_B_BreakerDiagram` | Breaker Room | Literacy: diagram first; sets Locate fuse |
| C | `Note_C_Checklist` | Storage | Lived-in checklist |
| D | `Note_D_PowerReport` | Electrical | Panel / fuse bay context |
| E | `Note_E_Warning` | Corridor | Energized systems warning |

---

## Witness Approach (PE-017A)

- **Where:** Exit critical path (~`Y=-1550`, south approach to `LockedExitDoor`) — **not** north spawn  
- **When:** After fuse solve → `WorldResponseTargets` includes `WitnessPresence`  
- **Timing:** ~2–4s delay (relief → dread); silhouette hidden at BeginPlay; brief reveal then gone  
- **Rules:** Tension only; does not alter puzzle solveability (bible §8)  
- **Cleanup:** North spawn cylinder stand-in removed; silhouette mesh hidden until restore  

---

## Replay (PE-017A Complete SliceReset)

`SliceResetButton` (`BP_MaintenanceWingReset`):

1. `ResetWorldState` — relock door, power-off lights, `ResetPresence`, clear ambient once-flags, reset notes, restore starting objective  
2. `ResetPlayerState` — remove Fuse from inventory  
3. `FinishPuzzleReset` — destroy leftover fuses, `ResetPuzzle`, respawn at `FuseSpawnMarker` (TargetPoint; not the pickup actor)  

---

## Environment / Lighting (PE-017A)

- Outdoor Directional / Sky dimmed so indoor emergency lighting dominates  
- `BP_EmergencyLight` PointLight: dim red standby → flicker → fluorescent restore (broken stubs stay dim/residual)  
- Room dressing from existing packs only (IndustryProps, Laboratory, AbandonedPowerPlant, Office Pack) — Corridor / Breaker / Storage / Electrical readable at a glance  
- Audio: `BP_PowerAmbientFeedback` restore chain (relay / hum / vent / distant metal / bed)  

---

## Validation

| Gate | Status |
|------|--------|
| Compile | NotePickup / Witness / Reset / EmergencyLight / Ambient / FusePuzzle saved |
| Technical | **PASS** — PIE boot: Witness hidden, door locked, emergency standby, objective set, puzzle ready |
| Gameplay | **Manual PIE required** — Enhanced Input cannot be fully driven by Slate |

### Manual PIE checklist

1. Spawn at north corridor; flashlight available; objective Investigate the power failure  
2. Read Note A — symptoms only; no empty objective flash on A/C/D/E  
3. Breaker (N): diagram → Locate fuse; room reads as breaker bay  
4. Storage (E): pick Maintenance Fuse → Insert fuse objective  
5. Electrical (S): prompt shows empty bay; insert → restore lights/audio/exit unlock  
6. Walk toward exit — Witness presence after delay (on path, not spawn)  
7. Interact exit door → open  
8. SliceResetButton → full reverse; replay fuse path without editor restart  

---

## PE-017A vs Critical Review (~42/100) Top 10

| # | Review issue | PE-017A response |
|---|--------------|------------------|
| 1 | Gameplay experience thin | Atmosphere + Witness path + storytelling pass |
| 2 | Incomplete SliceReset | Full reverse: door / lights / Witness / objectives / notes / fuse / ambient |
| 3 | Empty ObjectiveOnRead calls SetObjective | Skip when TextIsEmpty |
| 4 | FuelCan leftover on fuse panel | ItemData → Maintenance Fuse |
| 5 | Witness at spawn / visible early | Relocated to exit approach; hidden until restore |
| 6 | Weak lighting contrast | Outdoor dim; red standby → fluorescent restore |
| 7 | Blockout / placeholder art | Dressed rooms with existing asset packs |
| 8 | Note A solution walkthrough | Symptoms / urgency rewrite |
| 9 | Weak explore-before-solve | Breaker literacy + empty-bay prompt |
| 10 | Thin audio / restore payoff | Ambient restore chain + light flicker impact |

---

## Remaining Debt

- Full Gameplay PASS still needs human PIE (EI not Slate-automatable)  
- Real Sound Waves still thin — PrintString ambient placeholders remain acceptable until audio pack  
- Blockout structural geo (floors/walls) still BasicShapes under Geo/ — dressing is props-first  
- Some EmergencyLight instances may need resave after PointLight component add for all placed copies  
- BP_PlayerCharacter unrelated compile noise (pre-existing; out of PE-017A scope)  

---

## Ready For Review

**Yes** — PE-017A technical hardening + experience pass complete on `develop`. Manual Gameplay checklist remains the final human gate.

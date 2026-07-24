# PE-017 — Vertical Slice 01: Maintenance Wing

**Status:** Hardened (PE-017A) — Technical PASS; Manual Gameplay PASS still required  
**Branch:** `develop`  
**Priority:** Critical  
**Map:** `/Game/ProjectEcho/Maps/Production/LV_ARI_MaintenanceWing`  
**Design authority:** `Documents/01_Game_Design/GameplayDesignBible.md` (PE-016)  
**Puzzle framework:** PE-015 (`BP_PuzzleBase` / `BP_FusePuzzle`) — extended via config only  

---

## Design References

| Asset | Role |
|-------|------|
| `PE-017-VerticalSlice01-Overview.png` | Quality / tone / beat sheet |
| `PE-017-LevelDesignBlueprint.png` | **Authoritative** floor plan, flow, triggers, power states |

---

## Player Experience Goal

A 5–10 minute first playable that feels like the opening of a horror investigation — not a feature demo.  
Loop validated: Explore → Observe → Collect → Solve → World Response → Survive (Witness presence) → Proceed.

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
2. Discover power issue (notes / environment)  
3. Breaker Room (N) — read diagram → Locate Replacement Fuse  
4. Storage (E) — collect Maintenance Fuse  
5. Electrical (S) — insert fuse  
6. Auxiliary power restored  
7. Lights / ambient / exit unlock  
8. Witness presence on **exit path** (tension, not chase)  
9. Proceed through exit  

---

## Objective Chain

| Trigger | Objective text |
|---------|----------------|
| T01 Panel `ObjectiveOnAvailable` (BeginPlay) | Investigate the power failure |
| T02 Note B Breaker Diagram `ObjectiveOnRead` | Locate a replacement fuse |
| T03 Fuse pickup (PE-015) | Insert the fuse into the panel |
| T04/T05 Puzzle solve `ObjectiveOnSolved` | Access the next area |

---

## Systems Reused (no PE-015 architecture fork)

- Interaction / Notes: `BP_NotePickup` (+ `ObjectiveOnRead` Text; **skip-if-empty** on SetObjective)  
- Inventory: `BPC_Inventory`, `BP_FusePickup`  
- Objectives: `BPC_Objective`  
- Puzzle: `BP_FusePuzzle` / `BP_PuzzleBase`  
- Power: `BP_PowerManager`, `BPI_PowerReceiver`, `BP_PoweredDoor`, `BP_EmergencyLight`, ambient / PA / vent  
- Reset: `BP_MaintenanceWingReset` — **full world reverse** (door, lights, Witness, PowerManager flag, ambient once-flags, notes, objectives, fuse)  
- Horror: `BP_WitnessSilhouetteHint` (power-receiver presence beat on exit path)  

---

## Narrative Placements

| ID | Actor label | Location |
|----|-------------|----------|
| A | `Note_A_Maintenance` | Corridor — **symptoms only** (no walkthrough) |
| B | `Note_B_BreakerDiagram` | Breaker Room |
| C | `Note_C_Checklist` | Storage |
| D | `Note_D_PowerReport` | Electrical |
| E | `Note_E_Warning` | Corridor |

---

## Witness Approach

- **When:** After fuse solve → `WorldResponseTargets` includes `WitnessPresence` (`BP_WitnessSilhouetteHint.OnPowerRestored`)  
- **Where:** Exit corridor path (south of hub, near Locked Exit) — not entry  
- **What:** Delayed tension lines → silhouette + cold light reveal → withdraw; mesh hidden until post-power  
- **Rules:** Tension only; does not alter puzzle solveability (bible §8)  

---

## Replay

`SliceResetButton` (`BP_MaintenanceWingReset`) → `ResetWorldState` + `ResetPlayerState` + `FinishPuzzleReset`  
Reverses door lock/open, emergency light powered flag + Witness `ResetPresence`, PowerManager `HasHandledPower`, ambient/vent/PA/hint once-flags, note collected flags, objectives, destroys old fuses and respawns at `FuseSpawnPoint`.

---

## Validation

| Gate | Status |
|------|--------|
| Compile | NotePickup / Witness / EmergencyLight / MaintenanceWingReset compiled + saved |
| Technical | Simulate PIE boot: PowerManager ready; Witness hidden; EmergencyLights dim-red standby |
| Gameplay | **Manual PIE required** — Enhanced Input cannot be fully driven by Slate |

### Manual PIE checklist

1. Spawn at north corridor; flashlight available; indoor lighting feels emergency-dark (not outdoor sun)  
2. Objective: Investigate the power failure  
3. Read Note A (symptoms only — no blank objective); Note E; enter Breaker (N); observe switch/lever/wires + diagram → Locate fuse  
4. Storage (E): search racks/barrels; pick Maintenance Fuse on shelf → Insert fuse objective  
5. Electrical (S): empty panel readable (no FuelCan/cube leftover); insert fuse → staggered light restore + ambient audio prints + exit unlock  
6. Move toward exit — Witness tension then silhouette on exit path (not during puzzle)  
7. Interact exit door → open  
8. SliceResetButton → full reverse; replay fuse path without UE restart  

---

## Deferred Debt

- Real SoundWave/Cue assets for hum/vent/clicks (PrintString audio stand-ins in place)  
- Full wall/floor modular replacement (blockout spine remains; dressing props upgraded)  
- Witness silhouette still BasicShapes cylinder stand-in (not final character mesh/VFX)  
- Manual Gameplay PASS (EI) still human-gated  
- PowerManager orphan custom-event hygiene (pre-existing)  

---

## Design Notes (pacing / atmosphere)

- Compass matches blueprint so spatial memory matches clue text (“north bay”, “east Storage”, “south Electrical”).  
- Breaker-before-Storage teaches observation before inventory (env clues: control panel, switch bank, lever, wires).  
- Power restore relief, then Witness dread on the way out — double-edged restore per bible.  
- Feature count kept to one Electrical fuse + presence beat; no extra mechanics.  

---

## PE-017A — Experience Hardening & Environment Pass

**Date:** 2026-07-25  
**Focus:** Quality over quantity; Top 10 / Must Haves from PE-017 critical review.

### Before → After

| Area | Before | After |
|------|--------|-------|
| Witness | Entry-north; visible stand-in mesh | Exit-path; hidden until post-power; delayed reveal then gone |
| SliceReset | Puzzle + fuse only | Door / lights / Witness / PowerManager / ambient flags / notes / objectives / fuse |
| Note A | Walkthrough-style directions | Symptoms only |
| ObjectiveOnRead | Empty text still SetObjective | Skip-if-empty |
| Lighting | Outdoor Directional dominant; lights not driven | Directional/Sky killed indoors; EmergencyLight dim-red → flicker fluorescent restore; Breaker/Storage marked broken |
| Environment | BasicShape cubes for dressing | Industry/Lab props (racks, barrels, board, control panels, wires, rubble) |
| Fuse panel | Visible cube mesh | Hidden mesh — readable missing-fuse / panel housing |
| Fuse placement | Floor mid-storage | Crafted on storage rack + FuseSpawnPoint marker |
| Audio | Minimal | Staggered PrintString restore suite (Sound assets still debt) |

### Checklist

| Gate | Result |
|------|--------|
| Gameplay (full loop) | **PENDING_USER** — Slate EI cannot drive Interact/Move |
| Technical | **PASS** — Simulate boot + BP compile/save |
| Replay | **PASS** (Technical) — SliceReset graphs implement full reverse; manual confirm still needed |
| Witness | **PASS** (placement + hide/reveal logic) |
| Lighting | **PASS** |
| Environment | **PASS** (dressing pass; geo spine still blockout) |
| Docs | **PASS** |
| Ready For Review | **Yes** — with honest manual Gameplay checklist |


# PE-017 — Vertical Slice 01: Maintenance Wing

**Status:** Implemented (awaiting manual Gameplay PASS)  
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
8. Witness presence (tension, not chase)  
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

- Interaction / Notes: `BP_NotePickup` (+ `ObjectiveOnRead` Text for per-instance objectives)  
- Inventory: `BPC_Inventory`, `BP_FusePickup`  
- Objectives: `BPC_Objective`  
- Puzzle: `BP_FusePuzzle` / `BP_PuzzleBase`  
- Power: `BP_PowerManager`, `BPI_PowerReceiver`, `BP_PoweredDoor`, `BP_EmergencyLight`, ambient / PA / vent  
- Reset: `BP_MaintenanceWingReset` (duplicate of `BP_PuzzleResetButton` for slice labeling)  
- Horror: `BP_WitnessSilhouetteHint` (power-receiver presence beat)  

---

## Narrative Placements

| ID | Actor label | Location |
|----|-------------|----------|
| A | `Note_A_Maintenance` | Corridor |
| B | `Note_B_BreakerDiagram` | Breaker Room |
| C | `Note_C_Checklist` | Storage |
| D | `Note_D_PowerReport` | Electrical |
| E | `Note_E_Warning` | Corridor |

---

## Witness Approach

- **When:** After fuse solve → `WorldResponseTargets` includes `WitnessPresence` (`BP_WitnessSilhouetteHint.OnPowerRestored`)  
- **What:** Delayed print/audio-style presence lines + silhouette mesh stand-in at north corridor end  
- **Rules:** Tension only; does not alter puzzle solveability (bible §8)  

---

## Replay

`SliceResetButton` (`BP_MaintenanceWingReset`) → `ResetPuzzle` + fuse respawn (PE-015 pattern).  

**Deferred:** Full reverse of door lock / emergency light powered state / Witness once-flag without PIE (document as debt).

---

## Validation

| Gate | Status |
|------|--------|
| Compile | Assets saved; NotePickup / Witness / Reset compiled via MCP |
| Technical | PIE boot check (see mission completion report) |
| Gameplay | **Manual PIE required** — Enhanced Input cannot be fully driven by Slate |

### Manual PIE checklist

1. Spawn at north corridor; flashlight available  
2. Objective: Investigate the power failure  
3. Read Note A / E; enter Breaker (N); read diagram → Locate fuse  
4. Storage (E): pick Maintenance Fuse → Insert fuse objective  
5. Electrical (S): insert fuse → lights/ambient/exit unlock + Witness lines  
6. Interact exit door → open  
7. SliceResetButton → fuse/panel reset; replay fuse path  

---

## Deferred Debt

- Door / light / Witness full state reverse on slice reset  
- PointLight actor intensity not editable via ObjectTools on actor (component path flaky)  
- Blockout geo (BasicShapes) — art pass later  
- Witness is print + silhouette mesh stand-in, not full VFX/audio suite  
- `BP_NotePickup.ObjectiveOnRead` empty string still calls `SetObjective` (empty text) — prefer skip-if-empty in a follow-up  

---

## Design Notes (pacing / atmosphere)

- Compass matches blueprint so spatial memory matches clue text (“north bay”, “east Storage”, “south Electrical”).  
- Breaker-before-Storage teaches observation before inventory.  
- Power restore relief, then Witness dread — double-edged restore per bible.  
- Feature count kept to one Electrical fuse + presence beat; no extra mechanics.  

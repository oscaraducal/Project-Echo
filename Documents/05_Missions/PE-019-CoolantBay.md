# PE-019 — Coolant Bay (Post-Power Mechanical)

**Status:** Implemented — Technical PASS; Manual Gameplay PASS still required  
**Branch:** `develop`  
**Priority:** High  
**Map:** `/Game/ProjectEcho/Maps/Production/LV_ARI_CoolantBay`  
**Design authority:** `Documents/01_Game_Design/GameplayDesignBible.md` (PE-016)  
**Design plan:** `Documents/05_Missions/PE-019-DesignPlan.md` (APPROVED & IMPLEMENTED)  
**Predecessor:** `LV_ARI_GeneratorAnnex` (PE-018 — Soft Open Level → Coolant Bay)

---

## Player Experience Goal

A 6–12 minute Engineering beat after Generator Annex: teach **observe gauges → equalize coolant valves → release pressure hatch**, then Witness on exit — without combat, chase, Security, fuse forks, or new core frameworks.

Loop: Explore → Observe → Mechanical solve (valves) → World Response → Survive (Witness) → Proceed.

---

## Layout (+Y = North, +X = East)

Hub corridor spine (PE-018 recipe; Tool Spur cut):

| Room | Compass | Role |
|------|---------|------|
| Entry / Transfer Corridor | North / spawn | Soft Open arrival from Annex; Note A symptoms |
| Gauge Alcove | North bay / east | Stuck gauges (`Env_StuckGauge_*`); Note B checklist / valve IDs |
| Valve Manifold / Coolant Ops | South / center | `BP_CoolantLoopPuzzle` + valves V-12 / V-19 / V-27 |
| Exit Approach + Pressure Hatch | South end | Witness presence; `PressureHatch` (`BP_PoweredDoor`) unlock |

---

## Objective Chain

| Trigger | Objective text |
|---------|----------------|
| BeginPlay (`BP_CoolantBayReset`) | Investigate the coolant bay |
| Note B Gauge Checklist `ObjectiveOnRead` | Equalize the coolant pressure loop |
| Partial valve progress (`CheckValveSolve`) | Open the pressure hatch path |
| Puzzle World Response | Access the next area |

---

## Systems Reused / Created

- Interaction / Notes: `BP_NotePickup` (symptoms-only; skip-if-empty ObjectiveOnRead)
- Puzzle: thin `BP_CoolantLoopPuzzle` (`BP_PuzzleBase` child) + `BP_CoolantValve` interactables
- Power / response: `WorldResponseTargets` → `BPI_PowerReceiver` (hatch, EmergencyLights, vent, PA, ambient, DistantActivityHint, Witness) — **no** generator `HasHandledPower`; `bNotifyPowerOnSolve` false
- Horror: `BP_WitnessSilhouetteHint` (exit path; post-solve only)
- Soft Open: `BP_SoftOpenExit` — Annex Powered Exit → `LV_ARI_CoolantBay`; Maintenance Locked Exit → `LV_ARI_GeneratorAnnex` (PE-018 travel debt)
- Reset: `BP_CoolantBayReset` — full reverse (hatch, SoftOpenExit, lights, Witness, ambient flags, notes, objectives, valve + puzzle state)
- Player: existing `BP_GameMode` / `BP_PlayerCharacter` / Controller

**Independence:** Coolant Mechanical path stays separate from Annex generator `HasHandledPower` and Maintenance fuse path.

---

## Valve Solve (Mechanical)

| Valve | Start | Target |
|-------|-------|--------|
| V-12 | Closed | Open |
| V-19 | Closed | Open |
| V-27 | Open | Closed (keep shut) |

Clue: Note B equalization checklist. Incomplete set → unequal-pressure feedback; hatch stays locked.

---

## Narrative Placements

| ID | Actor label | Location |
|----|-------------|----------|
| A | `Note_A_Entry` | Entry corridor — plant live / coolant dead / hatch locked |
| B | `Note_B_GaugeChecklist` | Gauge Alcove — V-12 / V-19 open; V-27 shut; ObjectiveOnRead |
| C | `Note_C_Manifold` | Coolant Ops — gauges / tags / abandoned cart residue |
| D | `Note_D_HatchWarning` | Near manifold — do not open hatch under unequal pressure |
| E | `Note_E_Warning` | Corridor — optional unease after circulation |

---

## Witness

- **When:** After Mechanical `MarkSolved` World Response
- **Where:** Exit approach (`WitnessPresence`) — not spawn / not during valve work
- **What:** Delayed tension prints → silhouette + cold light → withdraw
- **Rules:** Tension only; does not brick valve logic

---

## Soft Open Level

| From | To | Actor |
|------|-----|--------|
| `LV_ARI_GeneratorAnnex` Powered Exit | `LV_ARI_CoolantBay` | `BP_SoftOpenExit` (`SoftOpenLevelName=LV_ARI_CoolantBay`) |
| `LV_ARI_MaintenanceWing` Locked Exit | `LV_ARI_GeneratorAnnex` | `BP_SoftOpenExit` (`SoftOpenLevelName=LV_ARI_GeneratorAnnex`) |
| Coolant Pressure Hatch | Stub (no Soft Open) | `BP_PoweredDoor` end-of-slice |

---

## Replay

`SliceResetButton` (`BP_CoolantBayReset`) → `ResetWorldState` + `ResetPlayerState` + `FinishPuzzleReset`  
Reverses hatch lock/open, SoftOpenExit, emergency lights, Witness `ResetPresence`, ambient once-flags, notes, objectives, `ResetValveStates` + `ResetPuzzle`.

---

## Validation

| Gate | Status |
|------|--------|
| Compile | CoolantValve / CoolantLoopPuzzle / SoftOpenExit / CoolantBayReset compiled + saved |
| Technical | PIE boot: valves ready; PuzzleBase activated; Coolant Bay ready objective; Map systems present |
| Gameplay | **PENDING_USER** — Enhanced Input cannot be fully driven by Slate |
| Replay | **PASS** (Technical) — SliceReset graphs implement full reverse; manual confirm still needed |

### Manual PIE checklist

1. Spawn Transfer Entry; flashlight available; indoor lighting (no outdoor sun dominance)
2. Objective: Investigate the coolant bay
3. Read Note A (symptoms); Gauge Alcove Note B → Equalize the coolant pressure loop
4. Coolant Ops: open V-12 + V-19; close V-27 → hatch unlock + Access the next area
5. Exit approach — Witness delayed silhouette (not during valves)
6. Interact Pressure Hatch → open (stub exit)
7. SliceResetButton → full reverse; replay valve path without UE restart
8. Soft Open: Annex powered exit → Coolant spawn; Maintenance exit → Annex (chain)

---

## Deferred Debt

- Real SoundWave/Cue assets for circulation / drip / pipe tick (PrintString `[PE019]` stand-ins)
- Full modular geo replacement (blockout spine + light dressing; stuck gauges are BasicShapes stand-ins)
- Witness silhouette still BasicShapes stand-in
- Manual Gameplay PASS (EI) human-gated
- Coolant exit Soft Open destination (future Security) not built

---

## Design Notes

- Teaches Mechanical literacy after aux fuse (PE-017) and main generator (PE-018).
- Feature count kept to one Mechanical ops problem + World Response + Witness.
- Security / fuse / generator redo deferred per approved plan.

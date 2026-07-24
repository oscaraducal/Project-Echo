# PE-018 — Generator Annex (Maintenance Wing Expansion)

**Status:** Implemented — Technical PASS; Manual Gameplay PASS still required  
**Branch:** `develop`  
**Priority:** High  
**Map:** `/Game/ProjectEcho/Maps/Production/LV_ARI_GeneratorAnnex`  
**Design authority:** `Documents/01_Game_Design/GameplayDesignBible.md` (PE-016)  
**Design plan:** `Documents/05_Missions/PE-018-DesignPlan.md` (APPROVED → implemented)  
**Predecessor:** `LV_ARI_MaintenanceWing` (PE-017 / PE-017A)

---

## Player Experience Goal

A 6–12 minute Engineering beat after Maintenance Wing: teach **fuel → generator → main plant restore**, then a slightly colder Witness presence on the exit approach — without combat, chase, new frameworks, or inventory redesign.

Loop: Explore → Observe → Collect Fuel → Start Generator → World Response → Survive (Witness) → Proceed.

---

## Layout (+Y = North, +X = East)

Hub corridor spine (adapted from PE-017 L-corridor; Pipe Gallery cut):

| Room | Compass | Role |
|------|---------|------|
| Service Entry Corridor | North / spawn | Arrive from Maintenance narrative; Note A symptoms; flashlight available |
| North Bay (observation) | North branch | Env observation; cool industrial tone |
| Fuel Cage / Storage | East | `BP_FuelCan` + Notes B/C (checklist / cage tag) |
| Generator Room | South / center | `BP_Generator` + Note D plant status |
| Exit Approach + Powered Exit | South end | Witness presence; `BP_PoweredDoor` unlock |

---

## Objective Chain

| Trigger | Objective text |
|---------|----------------|
| BeginPlay (`BP_GeneratorAnnexReset`) | Investigate the main power plant |
| Note B Fuel Checklist `ObjectiveOnRead` | Locate a fuel canister |
| FuelCan pickup | Fuel and start the generator |
| Generator World Response (`BP_PowerManager`) | Access the next area |

---

## Systems Reused (no new puzzle BP / frameworks)

- Interaction / Notes: `BP_NotePickup` (symptoms-only; skip-if-empty ObjectiveOnRead)
- Inventory: `BPC_Inventory`, `BP_FuelCan` (ItemId `FuelCan`)
- Objectives: `BPC_Objective`
- Power: `BP_Generator`, `BP_PowerManager` (generator `HasHandledPower` path), `BPI_PowerReceiver`, `BP_PoweredDoor`, `BP_EmergencyLight`, ambient / PA / vent / DistantActivityHint
- Horror: `BP_WitnessSilhouetteHint` (exit path; delayed; hidden until power)
- Reset: `BP_GeneratorAnnexReset` — full reverse (door, lights, Witness, PowerManager flag, ambient flags, notes, objectives, Generator state, FuelCan respawn)
- Player: existing `BP_GameMode` / `BP_PlayerCharacter` / Controller

**Independence:** Generator World Response remains separate from PE-017 puzzle `NotifyPuzzlePowerResponse`.

---

## Narrative Placements

| ID | Actor label | Location |
|----|-------------|----------|
| A | `Note_A_Entry` | Entry corridor — symptoms only (main still cold) |
| B | `Note_B_FuelChecklist` | Fuel Cage — incomplete fuel run; ObjectiveOnRead |
| C | `Note_C_FuelCage` | Fuel Cage — cradle empty / coolant OK flavor |
| D | `Note_D_PlantStatus` | Generator Room — offline / fuel first |
| E | `Note_E_Warning` | Corridor — optional unease near plant wake |

---

## Witness

- **When:** After generator World Response (`PowerManager` sweeps `BP_WitnessSilhouetteHint`)
- **Where:** Exit approach (`WitnessPresence` near Powered Exit) — not spawn / not during fuel solve
- **What:** Delayed tension prints → silhouette + cold light → withdraw
- **Rules:** Tension only; does not brick generator logic

---

## Replay

`SliceResetButton` (`BP_GeneratorAnnexReset`) → `ResetWorldState` + `ResetPlayerState` + `FinishPuzzleReset`  
Reverses door lock/open, emergency lights, Witness `ResetPresence`, PowerManager `HasHandledPower`, ambient once-flags, notes, objectives, Generator fuel/state, destroys FuelCans and respawns at `FuelSpawnPoint`.

---

## Validation

| Gate | Status |
|------|--------|
| Compile | GeneratorAnnexReset / PowerManager / FuelCan compiled + saved |
| Technical | Simulate PIE boot: PowerManager ready; generator bound; Witness hidden; MapCheck 0/0 |
| Gameplay | **PENDING_USER** — Enhanced Input cannot be fully driven by Slate |
| Replay | **PASS** (Technical) — SliceReset graphs implement full reverse; manual confirm still needed |

### Manual PIE checklist

1. Spawn Service Entry; flashlight available; indoor emergency-dark (outdoor Directional/Sky dim)
2. Objective: Investigate the main power plant
3. Read Note A (symptoms only); explore Fuel Cage; Note B → Locate a fuel canister
4. Pick FuelCan → Fuel and start the generator
5. Generator Room: dry interact feedback if needed; fuel + start (2s) → lights / ambient prints + exit unlock + Access the next area
6. Exit approach — Witness delayed silhouette (not during solve)
7. Interact Powered Exit → open
8. SliceResetButton → full reverse; replay fuel path without UE restart

---

## Deferred Debt

- Real SoundWave/Cue assets for hum/vent/clicks (PrintString `[PE018]` / ambient stand-ins)
- Full modular geo replacement (blockout spine + light dressing)
- Witness silhouette still BasicShapes stand-in
- Manual Gameplay PASS (EI) human-gated
- Soft travel Open Level from Maintenance exit → Annex (narrative bridge; not wired this mission)
- Pipe Gallery cut (optional atmosphere spur deferred)

---

## Design Notes

- Teaches aux (PE-017 fuse) vs main (PE-018 fuel/generator) power literacy.
- Feature count kept to one Resource Integration ops problem + World Response + Witness.
- Coolant / Security deferred per approved plan.

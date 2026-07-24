# Manual PIE Checklist — PE-020 Research Wing

**Status:** Archived with Close — Gameplay **PENDING_USER** (checklist remains the reopen Validate path)  
**Map:** `/Game/ProjectEcho/Maps/Production/LV_ARI_ResearchWing`  
**Estimated time:** 15–20 minutes (first pass) + 3–5 minutes replay  
**Gameplay PASS owner:** Executive Producer (Oscar)  
**Mission notes:** [`PE-020-ResearchWing.md`](PE-020-ResearchWing.md) (Closed — Technical)  
**Automation note:** Enhanced Input cannot be fully driven by Slate/MCP — human required. Technical ≠ Gameplay.

---

## Preconditions

- Branch `develop`; Unreal Editor open with Project Echo
- Flashlight available on player (inventory / default PE loadout)
- IMC / Enhanced Input: Move, Look, Interact, Flashlight
- Preferred entry: Soft Open from Coolant Bay `SoftOpenExit_Research` → Research Wing  
  Alternate: direct PIE on `LV_ARI_ResearchWing` (PlayerStart present)

---

## What Technical already proved (do not re-claim as Gameplay)

| Check | Evidence (Validate 2026-07-25) |
|-------|--------------------------------|
| Map loads | MCP `load_level` → `LV_ARI_ResearchWing` |
| GameMode | WorldSettings `DefaultGameMode` = `BP_GameMode` |
| Soft Open Coolant→Research | Coolant `SoftOpenExit_Research` → `softOpenLevelName=LV_ARI_ResearchWing`, `bTravelOnOpen=true` |
| Stations ST-TEMP / ST-SEAL / ST-LINK | Labels + `valveId` / start+target open states match Design Plan |
| Containment puzzle | Label `ContainmentCalibrationPuzzle`; `PuzzleID=ContainmentCalibration`; WR includes LabExit + Witness |
| LabExit locked pre-solve | Simulate: `bIsLocked=true` on `LabExit` (`BP_PoweredDoor`) |
| Witness until solve | PrintString `[PE017A] WitnessPresence hidden until power` |
| SliceReset present | Label `SliceResetButton` (`BP_CoolantBayReset` instance) |
| MapCheck | `0 Error(s), 0 Warning(s)` (session logs) |
| Simulate boot | Valves ready ×3; PuzzleBase ready |

**Gameplay still PENDING_USER** until this checklist is walked with real EI.

---

## Steps (Explore → Observe → Calibrate → WR → Witness → Exit → Replay)

### Explore

1. Soft Open from Coolant exit **or** PIE spawn into Entry / Transfer Corridor.
2. Confirm flashlight works; indoor lab lighting (no outdoor sun dominance).
3. Confirm you can move / look freely; no soft-lock at spawn.

### Observe

4. Read **Note A** (`Note_A_Entry`) — symptoms only (coolant stable / lab feed / containment unfinished). Fail if walkthrough directions.
5. Explore Observation Gallery — env panels readable without combat/chase.
6. Read **Note B** (`Note_B_CalibrationChecklist`) → objective becomes **Calibrate the containment chamber** (or equivalent).
7. Optionally read Notes C / D / E — symptoms only; no Restricted truth dump.

### Calibrate (Research Equipment)

8. Locate stations:
   - **ST-TEMP** — start HOLD → set **ENGAGE**
   - **ST-SEAL** — start HOLD → set **ENGAGE**
   - **ST-LINK** — start ENGAGE → set **HOLD**
9. Confirm incomplete set does **not** unlock LabExit (try interact while incomplete if unsure).
10. Complete correct triad → World Response (lights / ambient / PA / vent prints OK as debt) + LabExit unlock + objective toward next area.

### World Response → Witness → Exit

11. Walk Exit Approach — **Witness delayed silhouette only after solve** (not during station work).
12. Confirm Witness is tension-only (does not brick stations / lock player permanently).
13. Interact **LabExit** → opens (stub; no Security Soft Open required this mission).

### SliceReset / Replay

14. Press **SliceResetButton** without quitting UE.
15. Confirm reverse: LabExit locked again, stations to start states, Witness hidden again, notes/objectives reset as designed, WR receivers off.
16. Replay calibrate path once without editor restart.
17. Optional regression: Coolant / Annex / Maintenance paths still independent (no generator `HasHandledPower` / fuse ownership bleed).

---

## Pass criteria

- Full loop playable with Enhanced Input in ~15–20 minutes
- Soft Open Coolant→Research (or direct spawn) feels continuous
- Note B + stations teach Research Equipment without combat/chase/Security
- Witness post-solve on exit only
- SliceReset supports one clean replay without UE restart
- No soft-lock; indoor lighting baseline holds

## Fail / defer

| Fail if… | Defer / known debt |
|----------|-------------------|
| Soft-lock mid-loop | BeginPlay objective still CoolantBayReset string |
| Witness visible / pressure during station solve | PrintString `[PE019]` stand-ins on shared Coolant twins |
| Incomplete SliceReset (exit stays open, Witness stuck, stations wrong) | Real audio / modular lab geo |
| Outdoor sun dominates | Witness silhouette stand-in mesh |
| LabExit opens before correct ST triad | ResearchWingReset cutover not placed |

---

## EP decision block

**At Close (2026-07-25):** Human Gameplay was **not** declared PASS — mission Closed with open debt. After walking this checklist later, record:

- **Human Gameplay:** PASS / FAIL  
- **Replay (manual):** PASS / FAIL / N/A  
- Notes  

Then run: `Validate Mission PE-020` (reopen) or `Review Mission PE-020` (Mission Director).

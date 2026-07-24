# Manual PIE Checklist — PE-021 Security Wing

**Status:** Active — Gameplay **PENDING_USER** (Validate 2026-07-25)  
**Map:** `/Game/ProjectEcho/Maps/Production/LV_ARI_SecurityWing`  
**Estimated time:** 15–20 minutes (first pass) + 3–5 minutes replay  
**Gameplay PASS owner:** Executive Producer (Oscar)  
**Mission notes:** [`PE-021-SecurityWing.md`](PE-021-SecurityWing.md)  
**Automation note:** Enhanced Input cannot be fully driven by Slate/MCP — human required. Technical ≠ Gameplay.

---

## Preconditions

- Branch `develop`; Unreal Editor open with Project Echo
- Flashlight available on player (inventory / default PE loadout)
- IMC / Enhanced Input: Move, Look, Interact, Flashlight
- Preferred entry: Soft Open from Research Wing `LabExit` → Security Wing  
  Alternate: direct PIE on `LV_ARI_SecurityWing` (PlayerStart present)

---

## What Technical already proved (do not re-claim as Gameplay)

| Check | Evidence (Validate 2026-07-25) |
|-------|--------------------------------|
| Map loads | MCP `load_level` → `LV_ARI_SecurityWing` |
| GameMode | WorldSettings `DefaultGameMode` = `BP_GameMode` |
| Soft Open Research→Security | Research `LabExit` SoftOpenExit → `softOpenLevelName=LV_ARI_SecurityWing`, `bTravelOnOpen=true` |
| Consoles CS-BADGE / CS-ZONE / CS-EXIT | Labels + `valveId` / start+target states match Design Plan |
| Access Clearance puzzle | Label `AccessClearancePuzzle`; `puzzleId=AccessClearance`; `requiredItemId=StaffKeycard`; WR includes SoftOpenExit + Witness |
| SoftOpenExit_Stub locked pre-solve | Simulate: `bIsLocked=true`; print SoftOpenExit locked |
| Staff Keycard + Lobby gate | `StaffKeycardPickup` + `LobbyClearanceGate` requiredItemId=StaffKeycard |
| Witness until solve | PrintString `[PE017A] WitnessPresence hidden until power` |
| SliceReset present | Label `SliceResetButton` (`BP_SecurityWingReset`) |
| MapCheck | `0 Error(s), 0 Warning(s)` (session logs) |
| Simulate boot | Consoles ready ×3; PuzzleBase ready |

**Gameplay still PENDING_USER** until this checklist is walked with real EI.

---

## Steps (Explore → Observe → Clearance → WR → Witness → Exit → Replay)

### Explore

1. Soft Open from Research LabExit **or** PIE spawn into Entry / Checkpoint Transfer.
2. Confirm flashlight works; indoor checkpoint lighting (no outdoor sun dominance).
3. Confirm you can move / look freely; no soft-lock at spawn.

### Observe

4. Read **Note A** (`Note_A_Entry`) — symptoms only (lockdown clearance unfinished). Fail if walkthrough directions.
5. Explore Checkpoint Lobby — lockdown residue readable without combat/chase.
6. Read **Note B** (`Note_B_ClearanceBoard`) → objective becomes **Restore access clearance** (or equivalent).
7. Optionally read Notes C / D / E — symptoms only; no Restricted / Signal dump.

### Credential + Clearance (Security & Access)

8. Recover **Staff Keycard** in Credential / Locker Bay (`StaffKeycardPickup`).
9. Use keycard on **LobbyClearanceGate** (if present) to reach Access Control.
10. Set console stations:
    - **CS-BADGE** — start HOLD → set **ENGAGE**
    - **CS-ZONE** — start HOLD → set **ENGAGE**
    - **CS-EXIT** — start ENGAGE → set **HOLD**
11. Confirm incomplete set does **not** unlock SoftOpenExit_Stub (try interact while incomplete if unsure).
12. Complete correct triad (+ credential path) → World Response (lights / ambient / PA / vent prints OK as debt) + Soft Open unlock + objective toward next area.

### World Response → Witness → Exit

13. Walk Exit Approach — **Witness delayed silhouette only after solve** (not during keycard / console work).
14. Confirm Witness is tension-only (does not brick clearance / lock player permanently).
15. Interact **SoftOpenExit_Stub** → opens (stub next zone; no Signal map required).

### SliceReset / Replay

16. Press **SliceResetButton** without quitting UE.
17. Confirm reverse: Soft Open locked again, consoles to start states, Witness hidden again, keycard/inventory as designed, notes/objectives reset, WR receivers off.
18. Replay clearance path once without editor restart.
19. Optional regression: Research Soft Open still lands here; Coolant / Annex / Maintenance paths still independent (no generator `HasHandledPower` / fuse ownership bleed).

---

## Pass criteria

- [ ] Full loop playable with Enhanced Input in ~15–20 minutes
- [ ] Soft Open Research→Security (or direct spawn) feels continuous
- [ ] Staff Keycard + console triad readable without tutorial UI / walkthrough notes
- [ ] Incomplete clearance keeps Soft Open locked (readable fail)
- [ ] Witness only on exit path after solve
- [ ] SliceReset full reverse + second run without UE restart
- [ ] No combat / chase / Signal second puzzle / Armory / Restricted dump
- [ ] Indoor lighting baseline holds (no outdoor sun dominance)

## Fail / defer

| Fail if… | Defer / known debt |
|----------|-------------------|
| Soft-lock mid-loop | PrintString `[PE019]` / `[PE017A]` stand-ins on shared parent BPs |
| Witness visible / pressure during keycard or console solve | Stale AccessClearance `objectiveOnAvailable` fuse string (parent debt) |
| Incomplete SliceReset (exit stays open, Witness stuck, consoles wrong) | Real audio / modular security geo dressing |
| Outdoor sun dominates | Witness silhouette stand-in mesh |
| SoftOpenExit opens before correct CS triad + credential | SoftOpenExit stub destination (Signal / deeper) TBD |
| Combat / chase / Signal second puzzle / Armory / Restricted dump | Optional SecurityWingReset BeginPlay objective string cutover |

---

## EP decision block

After walking this checklist, record:

- **Human Gameplay:** PASS / FAIL / WAIVER  
- **Replay (manual):** PASS / FAIL / N/A  
- Notes  

Then run: `Review Mission PE-021` (preferred after PASS) or `Close Mission PE-021` (Mission Director). Reopen `Validate Mission PE-021` if FAIL needs a re-check.

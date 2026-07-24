# Manual PIE Checklist — PE-021 Security Wing

**Status:** Active — Gameplay **PENDING_USER**  
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

| Check | Evidence (Implement 2026-07-25) |
|-------|--------------------------------|
| Map loads | MCP `load_level` → `LV_ARI_SecurityWing` |
| GameMode | WorldSettings `DefaultGameMode` = `BP_GameMode` |
| Soft Open Research→Security | Research `LabExit` SoftOpenExit → `softOpenLevelName=LV_ARI_SecurityWing`, `bTravelOnOpen=true` |
| Consoles CS-BADGE / CS-ZONE / CS-EXIT | Labels + ValveID / start+target states match Design Plan |
| Access Clearance puzzle | Label `AccessClearancePuzzle`; `PuzzleID=AccessClearance`; WR includes SoftOpenExit + Witness |
| SoftOpenExit_Stub locked pre-solve | Simulate: `bIsLocked=true`; print SoftOpenExit locked |
| Staff Keycard + Lobby gate | `StaffKeycardPickup` + `LobbyClearanceGate` RequiredItemID=StaffKeycard |
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
11. Confirm incomplete set does **not** unlock SoftOpenExit_Stub.
12. Complete correct triad (+ credential path) → World Response + Soft Open unlock + objective toward next area.

### World Response → Witness → Exit

13. Walk Exit Approach — **Witness delayed silhouette only after solve** (not during keycard / console).
14. Confirm Witness is tension-only (does not brick clearance / lock player permanently).
15. Interact **SoftOpenExit_Stub** → opens (stub next zone; no Signal map required).

### SliceReset / Replay

16. Press **SliceResetButton** without quitting UE.
17. Confirm reverse: Soft Open locked again, consoles to start states, Witness hidden again, keycard/inventory as designed, notes/objectives reset, WR receivers off.
18. Replay clearance path once without editor restart.
19. Optional regression: Research Soft Open still lands here; Coolant / Annex / Maintenance paths still independent.

---

## Pass criteria

- [ ] Soft Open Research→Security works (or direct PIE acceptable for first pass)
- [ ] Staff Keycard + console triad readable without tutorial UI
- [ ] Incomplete clearance keeps Soft Open locked (readable fail)
- [ ] Witness only on exit path after solve
- [ ] SliceReset full reverse + second run without UE restart
- [ ] No combat / chase / Signal second puzzle / Armory / Restricted dump

**EP decision:** Gameplay PASS / FAIL / WAIVER — then `Validate Mission PE-021` or continue to Review when ready.

# Technical Debt

Status: Active  
Version: 1.0  
Mission: PE-014  

---

# Purpose

Honest technical debt review of Project Echo gameplay framework after MCP Blueprint inspection.  
**PE-014 policy:** document all findings; auto-fix only low-risk items. No gameplay redesign. PE-013C dirty Blueprint fixes were **not** modified or committed as part of PE-014.

---

# Summary

| Category | Count (approx.) | PE-014 action |
|----------|-----------------|---------------|
| Safe to Fix | Several | Documented; Blueprint auto-fixes deferred (dirty PE-013C overlap) |
| Requires Gameplay Review | Several | Documented only |
| Ignore | Several | Documented |

**Low-risk auto-fix applied in PE-014:** none in `.uasset` content (docs-only mission; avoid colliding with uncommitted PE-013C Character/Controller/IMC/interactable dirties).

---

# Safe to Fix

Low risk, no intended gameplay change. Prefer a dedicated cleanup mission when working tree is clean.

| ID | Finding | Evidence | Notes |
|----|---------|----------|-------|
| TD-001 | Orphan / empty custom events on `BP_PowerManager` | Many `OnPowerRestored_Event_*`, `CustomEvent_*` with empty bodies in EventGraph DSL | Safe delete when only unbound; verify bind still points at `HandlePowerRestored` |
| TD-002 | Duplicate variables on `BP_PowerManager` | `HasHandledPower` + `HasHandledPower_0`; `BoundGenerator` + `BoundGeneratorActor` | Confirm which is live-bound before removing |
| TD-003 | Duplicate interface function on `BPI_PowerReceiver` | `OnPowerRestored` + `OnPowerRestored_0` | Requires careful interface fix-up |
| TD-004 | Empty Tick / BeginOverlap stubs on interactables | Generator, NotePickup, FuelCan, FlashlightPickup, KeyItemPickup | Remove empty nodes; disable Tick if unused |
| TD-005 | Dual flashlight toggle API | `ToggleFlashlight` + `Toggle` on `BPC_Flashlight` | Collapse to one after confirming callers |
| TD-006 | Temporary PE-013C Jump PrintString | BugHistory remaining risk | Remove after Gameplay Move/Jump PASS |
| TD-007 | Empty legacy folder `/Game/ProjectEcho/Blueprints/` | list_folders | Delete if confirmed empty of needed assets |
| TD-008 | Disconnected sprint helper nodes | BUG-003 remaining risk | Graph clutter only |
| TD-009 | Docs drift (pre–PE-014) | Old `GameplaySystems` / `BlueprintArchitecture` thin stubs | **Addressed** by PE-014 docs |

---

# Requires Gameplay Review

Changing these can alter feel, order, or save/puzzle contracts.

| ID | Finding | Risk |
|----|---------|------|
| TD-010 | PE-013C IMC / EIS / Move ControlRotation fixes | Uncommitted dirty BPs; Gameplay WASD still PENDING_USER — merge only after user confirms |
| TD-011 | PowerManager dual path (dispatcher + Tick poll) | Removing Tick may break if bind fails; keeping both masks bugs |
| TD-012 | Generator + PowerManager both call `CompleteObjective` | Objective ordering / double-complete side effects |
| TD-013 | PowerManager hardcodes receiver classes | New receivers silently ignored unless PowerManager edited |
| TD-014 | `BPC_Interaction` path typed toward InteractableBase in DSL | Pure interface-only actors may not get correct CanInteract/Interact |
| TD-015 | Interact Visibility trace channel | Actors not Visibility-queryable miss Interact (BUG-004 note) |
| TD-016 | BUG-006 linker Parent Display on BPI overrides | Reparent/resave may touch many interactables |
| TD-017 | `BP_GameInstance` / `BP_SaveGame` stubs | Implementing save changes lifecycle |
| TD-018 | Unmapped `IA_Crouch` / Inventory / Journal / Pause | Wiring changes input UX |
| TD-019 | FirstPerson template Character/Controller still dirty in tree | Do not confuse with ProjectEcho pawns |
| TD-020 | Sprint Gameplay Validation | PENDING_USER (BUG-003) |

---

# Ignore

| ID | Finding | Why |
|----|---------|-----|
| TD-021 | UMG inherited touch/mouse overrides listed unimplemented on WBP_* | Engine defaults; not project debt |
| TD-022 | Character engine events unimplemented (`OnLanded`, etc.) | Normal |
| TD-023 | ThirdParty / Construction packs untracked | Art content; out of PE-014 scope |
| TD-024 | Blueprint DSL empty Enhanced Input bodies | Tooling false positive (BUG-002) |
| TD-025 | Slate PressKey cannot move pawn | Tooling limitation (BUG-007), not asset bug |
| TD-026 | Mission PrintString tags `[PE008]`/`[PE012]` | Useful until polish pass; not broken |
| TD-027 | Prototype maps PE011/PE012 retained | Intentional regression |

---

# Redirectors & Unused Assets

| Check | Result |
|-------|--------|
| ASSET-001 redirector cleanup | Previously performed (Changelog); no new rename in PE-014 |
| Unused FirstPerson template | Still present; Project defaults point at ProjectEcho (PE-013B). Treat as engine template residual — **Ignore** unless shipping size pass |
| Empty `Gameplay/AI`, `Audio`, `Save` content | Reserved folders — **Ignore** |
| `Gameplay/Puzzle` | **Filled** (PE-015) — no longer empty |
| Safe unused-asset purge | **Not run** (destructive); recommend editor Reference Viewer pass in a cleanup mission |

---

# TODOs / Inconsistent Naming

| Item | Status |
|------|--------|
| In-asset `TODO` nodes | None systematically found in inspected graphs; debt is structural |
| Pre-DOC names `BP_*Component` | Migrated to `BPC_*` (ASSET-001) |
| ContributionGuide folder examples (`Doors/`, `Generator/`) vs actual (`Interaction/`, `Power/`) | Prefer **actual** ASSET-001 layout; update guide in a future DOC pass |
| `BlueprintArchitecture.md` | Superseded in practice by Architecture/* + GameplayFlow; keep as short pointer or refresh later |

---

# Recommended Cleanup Mission (Future)

1. Confirm PE-013C Gameplay Validation → commit input fixes separately.  
2. Clean PowerManager orphan events + duplicate vars.  
3. Switch receiver discovery to `BPI_PowerReceiver`.  
4. Remove debug prints; Fix Up Redirectors if any remain.  
5. Optional: delete empty `Blueprints/` tree.  
6. **PE-015 deferred:** Expand `E_PuzzleState` display names to full 6-state set (asset currently duplicated from generator enum with 3 entries; runtime uses byte 0–5). Confirm Class Settings → Implemented Interfaces includes `BPI_Puzzle` on `BP_PuzzleBase`. Avoid `CallFunction|Activate` name collision with `Components|Activation|Activate` (inline or interface message). Leftover `ItemData` on `BP_FusePuzzle` from FuelCan duplicate.  

---

# Related

- `BugHistory.md`  
- `GameplaySystems.md`  
- `PuzzleFramework.md`  
- `04_Production/ProjectHealth.md`  

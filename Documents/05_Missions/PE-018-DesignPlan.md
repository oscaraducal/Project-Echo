# PE-018 — Design Plan: Generator Annex (Maintenance Wing Expansion)

**Status:** Design Plan — **APPROVED & IMPLEMENTED** (see `PE-018-GeneratorAnnex.md`)  
**Branch:** `develop`  
**Priority:** High (campaign beat after PE-017 / PE-017A)  
**Map:** `/Game/ProjectEcho/Maps/Production/LV_ARI_GeneratorAnnex`  
**Design authority:** `Documents/01_Game_Design/GameplayDesignBible.md` (PE-016)  
**Puzzle framework:** PE-015 (`BP_PuzzleBase` / families) — **compose existing systems; no framework fork**  
**Predecessor:** `LV_ARI_MaintenanceWing` (PE-017 / PE-017A — Production Foundation; VS not closed until human PIE)  
**Implementation notes:** `Documents/05_Missions/PE-018-GeneratorAnnex.md`

---

> ### Gate
>
> **APPROVED** — implementation shipped on `develop`.  
> Manual Gameplay PASS still human-gated (Enhanced Input / PIE). Technical Simulate PASS recorded in mission completion notes.

---

## Connection from Maintenance Wing

| From | To | How |
|------|-----|-----|
| `LV_ARI_MaintenanceWing` Locked Exit (west/south) | `LV_ARI_GeneratorAnnex` Entry Corridor | After PE-017 fuse/power restore + exit interact, player proceeds into the **Engineering service corridor** that feeds the annex |

**Narrative bridge (symptoms, not walkthrough):**  
Auxiliary bay power returned in Maintenance, but the **main plant is still cold**. Staff abandoned a fuel run toward the Generator Annex. Exit signage / a single corridor note points to Engineering Generator — not a quest-marker dump.

**Travel model (this mission):** Single contiguous production map for the annex (same pattern as PE-017). Soft travel from Maintenance exit may be:

1. **Preferred (simple):** Separate map load / Open Level to `LV_ARI_GeneratorAnnex` when PE-017 exit door completes open, **or**
2. **Deferred:** Physical door stub in Maintenance that only exists as destination once PE-018 ships.

Do **not** merge maps in v1. Do **not** build a multi-wing streaming graph in this mission.

---

## Why this wing (and not Coolant / Security)

| Candidate | Verdict |
|-----------|---------|
| **Generator Annex** | **Selected.** FacilityBible places Generator beside Maintenance under Engineering. Early–mid **Resource Integration** after PE-017 Electrical. Reuses `BP_Generator` / `BP_FuelCan` / PowerManager path. |
| Coolant Bay | Strong Mechanical family beat — **deferred**. Would tempt a new valve puzzle BP + failure soft-locks. Env-only coolant pipes/gauges appear in this annex instead. |
| Security Checkpoint | Too early / stakes jump. Security gates access later per bible. |

**Pillars served:** Exploration, Observation, Resource Management, Psychological Tension, Environmental Storytelling, Meaningful Progression.  
**Loop stages:** Explore → Discover → Understand → Solve → Restore Progress → Reveal Story → Survive → Proceed.  
**Puzzle family:** **Resource Integration** (primary) composed of existing Generator + Inventory; Mechanical/Electrical flavor via environment and notes only.

---

# 1. Mission Overview

## Purpose

Deliver the **best next level** after Maintenance Wing: a short Engineering beat that teaches **fuel → generator → main power restore**, then a slightly stronger Witness presence on the way out — without combat, chase, UI invent, inventory redesign, or new frameworks.

## Goals

1. Validate campaign continuation from PE-017 exit into a second production map.
2. Exercise the **generator World Response** path (`HasHandledPower`) as distinct from PE-017’s **puzzle** power path (`NotifyPuzzlePowerResponse`).
3. Keep feature count low: one core ops problem + world response + Witness + exit.
4. Deepen Asterion tone: plant was mid-maintenance when evacuation hit.

## Beginning

Player enters `LV_ARI_GeneratorAnnex` from the Maintenance Wing exit / Engineering service entry. Space is darker industrial than Maintenance. Generator is offline. Fuel is missing. Objectives steer investigation, not a tutorial script.

## End

Generator running → lights / ambient / powered exit unlock → Witness presence on exit approach → player proceeds through exit toward a **stub next zone** (future Security / Coolant — not built here). SliceReset supports replay if claimed.

**Target length:** ~6–12 minutes first play (slightly longer than PE-017 only if exploration dressing warrants; cut rooms before adding mechanics).

---

# 2. Gameplay Flow

```text
Spawn → Explore → Observe → Puzzle (ops) → World Response → Witness/Horror → Exit
```

| Stage | What happens | Why |
|-------|--------------|-----|
| **Spawn** | Entry Corridor (from Maintenance exit). Flashlight available. Emergency-dark indoor lighting (no outdoor sun dominance). Objective: investigate main plant / restore generator power. | Continuity from PE-017; spatial literacy starts immediately. |
| **Explore** | Hub corridor with branches: Fuel Cage / Storage, Generator Room, Observation Alcove (optional short), Locked Exit (powered). | Facility realism; rooms exist for Engineering work. |
| **Observe** | Read symptom notes; see empty fuel cradle, cold gauges, coolant pipes (env-only), breaker bank already set (or labeled “aux feed live — main offline”). | Observation before inventory; no walkthrough notes. |
| **Puzzle (ops)** | Find `FuelCan` → return to `BP_Generator` → fuel → start (existing 2s start pattern). | Resource Integration; believable facility ops. |
| **World Response** | `BP_PowerManager` generator path: emergency lights restore, ambient/vent/PA feedback, `BP_PoweredDoor` exit unlock. | World acknowledges the player; double-edged restore (more light, more attention). |
| **Witness / Horror** | Presence beat on **exit path** after power (silhouette pattern from PE-017). Slightly later / colder audio than Maintenance — still tension only. | Survive stage; bible §8 — does not brick generator logic. |
| **Exit** | Interact powered exit → proceed (stub destination / end-of-slice). | Meaningful progression; campaign handoff point. |

**Out of scope in flow:** Chase sequences, combat, multi-puzzle chains, keycard Security, coolant valve minigame, journal UI, save system.

---

# 3. Level Layout

**Suggested map name:** `LV_ARI_GeneratorAnnex`  
**Compass convention:** Match PE-017 (+Y = North, +X = East) so clue language stays consistent.

### Rooms (keep to ≤5)

| Room | Compass (suggested) | Role |
|------|---------------------|------|
| Entry / Service Corridor | West / spawn | Arrive from Maintenance; Note A (symptoms); path spine |
| Fuel Storage | North or East | `BP_FuelCan` pickup + checklist-style note (symptoms / incomplete fuel run) |
| Generator Room | Center / South | `BP_Generator` + power report note; primary solve space |
| Pipe Gallery (short) | Adjacent spur | Env storytelling only (coolant / steam pipes, gauges) — **no required interact** |
| Exit Approach + Locked Exit | East or far South | Powered door; Witness presence; proceed |

### Connections / navigation

- Hub corridor connects Entry ↔ Fuel ↔ Generator ↔ Exit.
- Pipe Gallery is optional dead-end spur for atmosphere (skippable without soft-lock).
- Exit remains locked until generator World Response.
- No maze; no backtracking beyond Fuel → Generator once.

### Pacing

1. **Quiet entry** (30–60s) — darkness, hum absence, symptom note.  
2. **Directed search** — Fuel Storage find.  
3. **Focused solve** — Generator fuel/start.  
4. **Relief** — lights / sound return.  
5. **Pressure** — Witness on exit walk.  
6. **Release** — exit open.

If any role flags length: **cut Pipe Gallery** first; never add a second puzzle to fill time.

---

# 4. Environmental Storytelling

## What happened

Engineering was mid-shift restoring the plant after an aux fault (Maintenance Wing). Someone started a fuel run, never finished. Coolant lines look recently checked (gauges, tags) but the generator was never refueled. Evacuation interrupted ordinary work — not a set-piece disaster room.

## Clues

| Type | Content | Required? |
|------|---------|-----------|
| Note A — Entry symptoms | Flicker / silence / “main still cold” — **no directions** | Yes (tone + objective hook) |
| Note B — Fuel Storage | Incomplete fuel checklist / empty cradle observation | Yes (observation → collect) |
| Note C — Generator Room | Power / plant status report (symptoms + procedure crumbs only) | Yes (understand → solve) |
| Note D — Warning / Witness adjacent | Staff unease near plant noise / “don’t linger on the catwalk” | Optional |
| Env-only | Empty fuel cradle, cold generator, coolant tags “OK”, abandoned cart, emergency paint | Yes (story without text) |
| Env-only Pipe Gallery | Pressure gauges, valve wheels **not** interactable | Optional |

**Rules:** Notes = symptoms and residue of work. **No walkthrough** (“go north then pick up fuel”). No exposition dumps. No audio-log monologues in this mission.

---

# 5. Puzzle Design

## Objective

Restore main generator power so the annex exit unlocks and Engineering systems respond.

## Learning

- PE-017 taught **fuse → aux electrical restore** (puzzle power path).  
- PE-018 teaches **fuel → generator → plant restore** (generator power path).  
- Player learns Asterion power is layered (aux vs main), not a single switch fantasy.

## Failure

- Interacting with unfueled generator → existing feedback (“needs fuel” / state print) — readable, not punitive.  
- No timed fails, no Witness soft-lock, no randomized solution.  
- Lost FuelCan after pickup should not happen; SliceReset must respawn fuel if replay claimed.

## Reward

- Staggered light restore, ambient plant hum / vent / PA prints (real audio or tagged debt).  
- Exit unlock.  
- Objective update (“Access the next area” / equivalent).  
- Story beat: plant waking; Witness notices.

## Family mapping (PE-015 / bible §5)

| Element | Family | Implementation |
|---------|--------|----------------|
| Fuel find + Generator start | Resource Integration | Existing `BP_FuelCan` + `BP_Generator` + `BPC_Inventory` |
| Powered exit / lights | Electrical (reward layer) | `BP_PowerManager`, `BPI_PowerReceiver`, `BP_PoweredDoor`, `BP_EmergencyLight` |
| Coolant / pipes | Mechanical (flavor only) | Props + notes — **no new puzzle BP** |
| Observation notes | Environmental Observation | `BP_NotePickup` + `BPC_Objective` |

**Explicit non-builds:** No `BP_ValvePuzzle`, no fuse panel duplicate, no security console, no `BP_PuzzleBase` child unless approval later finds Generator alone insufficient (prefer not).

---

# 6. Horror Design

Psychological only — no combat, no chase AI.

### Tension curve

```text
Unease (dark plant) → Focus (fuel run) → Relief (generator starts) → Spike (Witness on exit) → Release (door)
```

### Witness

| Field | Spec |
|-------|------|
| Pattern | Reuse `BP_WitnessSilhouetteHint` (or instance twin) as `BPI_PowerReceiver` on generator World Response targets |
| When | After power restore — **not** during fuel search / generator interact |
| Where | Exit approach corridor (not spawn) |
| What | Delayed tension → silhouette + cold light → withdraw; mesh hidden until post-power |
| Rules | Bible §8 — pressures attention; never replaces solvable logic |

### Lighting

- Indoor emergency-dark baseline; kill outdoor Directional/Sky dominance (PE-017A lesson).  
- Generator Room slightly darker industrial than corridor.  
- Restore = flicker → fluorescent / industrial lamps (existing EmergencyLight pattern).  
- Witness beat = brief cold accent, then withdraw.

### Audio

- Pre-power: sparse drip / silence / distant metal.  
- On restore: staggered hum / vent / relay clicks.  
- Witness: low tension line / withhold music stinger spam.  
- **Debt tag allowed:** PrintString stand-ins if SoundWave/Cue not ready — list in mission debt; do not claim Production Ready on audio alone.

---

# 7. Technical Plan

## Reused systems (preferred path)

| System | Assets |
|--------|--------|
| Interaction | `BPC_Interaction`, `BPI_Interactable`, doors |
| Inventory | `BPC_Inventory`, `BP_FuelCan`, `ST_InventoryItem` |
| Objectives | `BPC_Objective`, `WBP_Objective` |
| Notes | `BP_NotePickup` (`ObjectiveOnRead` skip-if-empty) |
| Power | `BP_Generator`, `BP_PowerManager`, `BPI_PowerReceiver`, `BP_PoweredDoor`, `BP_EmergencyLight`, ambient / PA / vent receivers |
| Horror | `BP_WitnessSilhouetteHint` (+ `ResetPresence`) |
| Reset pattern | PE-017 `BP_MaintenanceWingReset` / PE-015 reset pattern |
| Player | Existing `BP_PlayerCharacter` / Controller — no redesign |

## New / modified (minimize)

| Item | Need? | Notes |
|------|-------|-------|
| Map `LV_ARI_GeneratorAnnex` | **Yes** | Under `/Game/ProjectEcho/Maps/Production/` |
| Notes content (instances) | **Yes** | Config only on `BP_NotePickup` |
| `BP_GeneratorAnnexReset` (or generic `BP_SliceReset`) | **Likely** | Twin of MaintenanceWingReset: door, lights, Witness, PowerManager flag, notes, objectives, FuelCan respawn |
| Modify `BP_Generator` | **Avoid** | Prefer instance config only |
| Modify `BP_PowerManager` | **Avoid** unless orphan hygiene already scheduled |
| New puzzle BP | **No** | |
| New UI / inventory framework | **No** | |
| Witness AI / chase | **No** | |

## Data / folders

- Map: `/Game/ProjectEcho/Maps/Production/LV_ARI_GeneratorAnnex`  
- Optional mission notes doc (post-approval): `Documents/05_Missions/PE-018-GeneratorAnnex.md`  
- No mission IDs in asset names (`ContributionGuide`).

## Dependencies

- PE-015 puzzle framework available (not heavily used beyond patterns).  
- PE-017A systems (Witness, EmergencyLight, NotePickup skip-if-empty, SliceReset pattern).  
- Human PIE validation capability for Enhanced Input.  
- Existing industrial prop packs already in workspace for dressing (same approach as PE-017A).

## Independence note

Generator World Response must remain independent of PE-017 puzzle `NotifyPuzzlePowerResponse` path — do not collapse both into one once-only flag incorrectly across maps.

---

# 8. Risk Assessment + Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Scope creep (valve + fuse + keycard) | Schedule / bible violation | Cut list locked: Fuel + Generator only; Coolant env-only; Security deferred |
| PE-017A Gameplay PASS still pending | Building on unvalidated foundation | Gate: wait for human PIE **or** EP written waiver |
| Generator already “solved” in TestingGround | Feels like sandbox redux | Production framing: darker annex, Maintenance continuity, Witness escalation, campaign exit stub |
| PowerManager dual objective / orphan debt | Double complete / hygiene | Do not expand PowerManager; instance carefully; track TD separately |
| Audio still PrintString | Atmosphere gap | Tag debt honestly; lighting + Witness carry tension |
| Soft travel between maps | Player confusion | Clear exit interact → load annex; entry note reinforces Engineering |
| SliceReset incomplete | Replay claims false | Mirror PE-017A full reverse checklist for FuelCan + Generator state |
| Witness during solve | Unfair pressure | Presence only on exit path post-power |
| Over-dressed geo | Art sink | Blockout spine first; dressing pass after loop works |

---

# 9. Implementation Plan (phased milestones)

> Execute **only after approval**. Order is intentional.

### Phase 0 — Preconditions

- Confirm PE-017A manual PIE checklist (or EP waiver).  
- Freeze this design plan; ADR only if diverging from bible.

### Phase 1 — Map blockout + flow

- Create `LV_ARI_GeneratorAnnex` blockout (≤5 rooms).  
- Place spawn, FuelCan, Generator, PoweredDoor, PowerManager, EmergencyLights.  
- Verify compass / objective chain text.

### Phase 2 — Ops loop

- Fuel → Generator → World Response → exit unlock.  
- Notes A–C symptoms-only.  
- Objectives: investigate → locate fuel → restore generator → access next area.

### Phase 3 — Horror + lighting

- Wire Witness on exit path via World Response targets.  
- Indoor lighting pass (PE-017A rules).  
- Audio prints or real cues (debt-tag if needed).

### Phase 4 — SliceReset + sandbox regression

- Annex reset actor (full reverse).  
- Smoke on `LV_TestingGround` that Generator path still independent.  
- No PE-015 architecture changes.

### Phase 5 — Dressing + docs

- Prop pass from existing packs.  
- Mission completion doc + Changelog / ProjectHealth / Roadmap updates.  
- Manual PIE checklist for EP.

### Phase 6 — Review gates

- Compile PASS → Technical Simulate PASS → **Human PIE Gameplay PASS** → Replay PASS → Ready for Review.

---

# Cross-Team Internal Review Notes

Where this plan was **simplified** under role pressure:

| Role | Flag | Simplification |
|------|------|----------------|
| **EP** | Best next ≠ biggest | One map, one ops problem, no streaming, no Coolant puzzle, no Security |
| **LD** | Room count | ≤5 rooms; Pipe Gallery optional cut |
| **GD** | Family teaching | Resource Integration via existing Generator — not a new PE-015 child |
| **Horror** | Escalation without chase | Same silhouette pattern; timing/placement only |
| **Tech** | New BP surface | Prefer config + map + SliceReset twin; avoid Generator/PowerManager rewrites |

### Suggested objective chain (draft)

| Trigger | Objective text (draft) |
|---------|------------------------|
| BeginPlay / entry | Investigate the main power plant |
| Note B / Fuel area | Locate a fuel canister |
| FuelCan pickup | Fuel and start the generator |
| Generator World Response | Access the next area |

---

# Compliance Checklist

### Gameplay Design Bible

| Rule | PE-018 plan |
|------|-------------|
| Facility realism | Generator Annex is Engineering workplace |
| Observation over guessing | Notes + empty cradle + cold plant |
| No anti-patterns | No glyph pads / arbitrary sequences |
| Pillars / loop integrity | Explicit flow mapping |
| Witness pressures, never replaces logic | Exit-path presence only |
| Horror fair | Readable generator fail feedback |
| Extend PE-015 / compose systems | No parallel frameworks |
| Progression = knowledge + access | Aux vs main power literacy + exit |
| Sandbox before campaign | Phase 4 regression on TestingGround |
| Tone | Isolated, scientific, grounded |

### Story / Facility

| Source | Alignment |
|--------|-----------|
| Story Bible | Notes + env; no exposition dump; Witness uncertainty |
| Facility Bible | Engineering → Generator adjacent to Maintenance |
| Room Bible | Each room: function / what happened / why player is here |

### Production Standard (project practice)

| Standard | Plan commitment |
|----------|-----------------|
| Human PIE for Gameplay PASS | Required before Ready / VS close |
| Reset if replay claimed | SliceReset full reverse |
| Lighting intentional | Emergency-dark → restore; no outdoor sun dominance |
| Audio real or tagged debt | Explicit debt allowed |
| Symptoms not walkthrough notes | Note rules locked |
| No combat / chase / UI invent | Out of scope |
| Docs track truth | Mission doc + Changelog on implement |

---

# Approval Block

| Field | Value |
|-------|-------|
| Ready for Approval | **YES** (approved) |
| Ready to Implement | **DONE** — see `PE-018-GeneratorAnnex.md` |
| Map | `LV_ARI_GeneratorAnnex` |
| Primary family | Resource Integration (Generator + Fuel) |
| Deferred | Coolant valve puzzle, Security checkpoint, Witness AI, Save, Pipe Gallery |

**APPROVED & IMPLEMENTED**

---

## Document Control

| | |
|--|--|
| Created | 2026-07-25 |
| Mission | PE-018 Design Plan only |
| Owners | Design (EP / LD / GD / Horror / Tech review) |
| Related | `PE-017-VerticalSlice01.md`, `GameplayDesignBible.md`, `PuzzleFramework.md`, `FacilityBible.md` |

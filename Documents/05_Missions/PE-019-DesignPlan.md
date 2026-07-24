# PE-019 — Design Plan: Coolant Bay (Post-Power Mechanical)

**Status:** Design Plan — **AWAITING APPROVAL**  
**Branch:** `develop`  
**Priority:** High (campaign beat after PE-018 Generator Annex)  
**Map (proposed):** `/Game/ProjectEcho/Maps/Production/LV_ARI_CoolantBay`  
**Wing name:** **Coolant Bay** (Engineering pressure / coolant loop)  
**Design authority:** `Documents/01_Game_Design/GameplayDesignBible.md` (PE-016)  
**Puzzle framework:** PE-015 (`BP_PuzzleBase` / families) — **compose existing systems; no framework fork**  
**Map recipe:** **PE-018** (`LV_ARI_GeneratorAnnex` pattern) — Playbook §10  
**Fuse path:** Owned by **PE-017A** — do not duplicate  
**Predecessor:** `LV_ARI_GeneratorAnnex` (PE-018 — main plant power restored)  
**Soft Open Level (plan only):** Generator Annex powered exit → Open Level → Coolant Bay  

---

> ### Gate
>
> **WAIT FOR APPROVAL — DO NOT IMPLEMENT**  
> No Blueprints, maps, or gameplay work until this plan is marked **Ready to Implement**.  
> Ready for Approval: **YES**

---

## Connection from Generator Annex

| From | To | How |
|------|-----|-----|
| `LV_ARI_GeneratorAnnex` Powered Exit | `LV_ARI_CoolantBay` Entry / Transfer Corridor | After PE-018 generator World Response + exit interact, **Soft Open Level** loads Coolant Bay |

**Narrative bridge (symptoms, not walkthrough):**  
Main plant power returned in the Generator Annex, but Engineering left a **coolant / pressure equalization** unfinished. Live power without circulation is unsafe. Exit signage / one corridor note points toward the Coolant Bay — not a quest-marker dump.

**Travel model (this mission):**

1. **In-scope (plan wiring, implement only after approval):** Soft Open Level from Generator Annex powered exit → `LV_ARI_CoolantBay`.  
2. **Also plan (if still open debt):** Soft Open Level Maintenance exit → Generator Annex (PE-018 deferred debt) — may ship alongside PE-019 travel wiring if EP wants chain continuity; **do not merge maps**.  
3. Do **not** build multi-wing streaming. Do **not** merge Coolant into Generator Annex.

**Power continuity assumption:** Coolant Bay starts as a **post-power** Engineering beat — plant feed is already live (partial industrial lighting / hum baseline). The ops problem is Mechanical, not another generator fuel run.

---

## Why this wing (Mechanical Coolant — not Security)

| Candidate | Verdict |
|-----------|---------|
| **Coolant Bay (Mechanical)** | **Selected.** PE-018 deferred coolant valves as env-only and seeded coolant gauges/tags. Restored main power makes unfinished cooling / pressure work the believable next Engineering consequence. Bible §5.2 Mechanical: valves, pressure lock, ventilation path. Mid-game teaching beat distinct from PE-017 fuse (Electrical) and PE-018 fuel/generator (Resource Integration). |
| Security Checkpoint | **Deferred.** FacilityBible places Security as its own zone (checkpoints / surveillance). PE-018 already judged Security a stakes jump for the immediate post-Maintenance beat; post-Annex still belongs in Engineering continuum before Security access. |
| Electrical Control (bible zone) | **Not selected.** Would retread Electrical literacy already taught in Maintenance; fuse path owned by PE-017A. |
| Research / Restricted | Far too early. |

**Pillars served:** Exploration, Observation, Psychological Tension, Environmental Storytelling, Meaningful Progression; Resource Management only if a single tool/tag is used (prefer not).  
**Loop stages:** Explore → Discover → Understand → Solve → Restore Progress → Reveal Story → Survive → Proceed.  
**Puzzle family:** **Mechanical** (primary) — thin `BP_PuzzleBase` child + interactable valves; world response via existing `BPI_PowerReceiver` / ventilation / hatch patterns.

---

# Mission Brief

| Field | Content |
|-------|---------|
| **Mission** | PE-019 Coolant Bay |
| **Player experience goal** | 6–12 minute Engineering beat after Generator Annex: teach **observe gauges → equalize coolant pressure / open loop valves → release pressure hatch**, then Witness on exit — without combat, chase, Security keycards, fuse forks, or new core frameworks. |
| **Teaching beat** | Mechanical facility hardware (valves / pressure) as consequence of restored main power — distinct from aux fuse and generator fuel. |
| **End state** | Pressure interlock cleared → hatch / exit unlock + ventilation / ambient response → Witness presence on exit approach → Soft Open stub toward future Security (not built). |
| **Target length** | ~6–12 minutes first play. Cut rooms before adding mechanics. |

---

# Gameplay Loop

```text
Spawn (post-power entry) → Explore → Observe (gauges / notes) → Mechanical solve (valves) → World Response → Witness / Horror → Exit (Soft Open stub)
```

| Stage | What happens | Why |
|-------|--------------|-----|
| **Spawn** | Entry / Transfer Corridor from Generator Annex Soft Open. Flashlight available. Partial plant lighting / industrial hum (post-power), but coolant loop still dead / pressure locked. Objective: investigate coolant / clear pressure path. | Continuity from PE-018; problem shifted to Mechanical. |
| **Explore** | Hub corridor: Gauge Alcove, Valve Manifold / Coolant Ops, optional Tool Spur, Locked Pressure Exit. | Facility realism; ≤5 rooms. |
| **Observe** | Symptom notes; cold coolant lines; gauges stuck / unequal; valve tags; abandoned equalization checklist. | Observation before interact; no walkthrough notes. |
| **Puzzle (ops)** | Align / open required loop valves (clue-backed IDs or states) → Mechanical puzzle `MarkSolved`. | Bible §5.2; PE-015 child. |
| **World Response** | Pressure hatch unlock, ventilation / ambient / PA feedback via `WorldResponseTargets` (+ optional `NotifyPuzzlePowerResponse` for tagged receivers — **independent** of generator `HasHandledPower`). | World acknowledges Mechanical restore. |
| **Witness / Horror** | Presence on **exit path** after solve — silhouette pattern; slightly colder / industrial than Annex. | Survive; bible §8. |
| **Exit** | Interact pressure hatch / powered exit → proceed (stub Soft Open destination / end-of-slice). | Meaningful progression. |

---

# Narrative Purpose

Engineering restored main power but evacuated before finishing coolant circulation / pressure equalization. The Coolant Bay is ordinary plant procedure interrupted mid-shift — not a disaster set-piece. Player inherits unfinished work: make the live plant safe enough to proceed deeper into the institute.

Story delivery: symptoms notes + env props only. No exposition dumps. No Witness over-explanation.

---

# 1. Mission Overview

## Purpose

Deliver the **best next level** after Generator Annex: one coherent Engineering wing that pays off PE-018’s deferred coolant storytelling and teaches the **Mechanical** family under restored-power consequences — using the PE-018 map recipe, without Security, combat, chase, or framework forks.

## Goals

1. Validate Soft Open Level campaign continuation: Annex exit → Coolant Bay (plan wiring; implement post-approval).  
2. Ship first Mechanical teaching beat via PE-015 (`BP_PuzzleBase` child), not a parallel puzzle system.  
3. Keep feature count low: one ops problem + world response + Witness + exit.  
4. Deepen Asterion tone: plant waking is double-edged — power returned, cooling incomplete, pressure locked.

## Beginning

Player loads into `LV_ARI_CoolantBay` after Annex Soft Open (or direct PIE spawn for isolated playtest). Space is damp, industrial, gauge-heavy. Exit pressure hatch is locked. Coolant loop looks mid-procedure.

## End

Valves equalized / loop opened → hatch unlock + vent response → Witness on exit approach → player proceeds through exit toward a **stub next zone** (future Security — not built here). SliceReset supports replay if claimed.

---

# 2. Gameplay Flow

```text
Spawn → Explore → Observe → Puzzle (Mechanical) → World Response → Witness/Horror → Exit
```

**Out of scope in flow:** Chase, combat, Security keycards/consoles, fuse panel duplicate, generator fuel redo, multi-puzzle chains, journal UI, save system, timed fail soft-locks, multi-zone streaming.

---

# 3. Level Layout

**Map name:** `LV_ARI_CoolantBay`  
**Compass convention:** Match PE-017 / PE-018 (+Y = North, +X = East).

### Rooms (≤5)

| Room | Compass (suggested) | Role |
|------|---------------------|------|
| Entry / Transfer Corridor | West / spawn | Soft Open arrival from Annex; Note A (symptoms); path spine |
| Gauge Alcove | North | Observation — stuck gauges, unequal pressure; Note B (procedure crumbs / valve IDs) |
| Valve Manifold / Coolant Ops | Center / South | Primary Mechanical solve (`BP_CoolantLoopPuzzle` + valve interacts) |
| Tool / Tag Spur (optional) | East short spur | Env storytelling; **cut first** if length/scope pressure — prefer **no inventory item** |
| Exit Approach + Pressure Hatch | Far South / East | Post-solve unlock; Witness presence; proceed |

### Connections / navigation

- Hub corridor connects Entry ↔ Gauge ↔ Manifold ↔ Exit.  
- Tool Spur optional dead-end (skippable if kept env-only).  
- Exit remains locked until Mechanical solve World Response.  
- No maze; no required backtracking beyond Gauge → Manifold.

### Pacing

1. **Quiet entry** (30–60s) — post-power hum vs dead coolant silence.  
2. **Directed observation** — Gauge Alcove.  
3. **Focused solve** — Valve Manifold.  
4. **Relief** — hatch / ventilation response.  
5. **Pressure** — Witness on exit walk.  
6. **Release** — exit open.

If length flags: **cut Tool Spur first**; never add a second puzzle family to fill time.

---

# 4. Environmental Storytelling

## What happened

After aux restore (Maintenance) and main plant fuel/start (Annex), Engineering began coolant loop equalization so the plant could run safely. Evacuation hit mid-valve. Gauges show unequal loops. Someone tagged valves and never finished the sequence.

## Clues

| Type | Content | Required? |
|------|---------|-----------|
| Note A — Entry symptoms | Plant live / coolant still dead / pressure locked — **no directions** | Yes |
| Note B — Gauge Alcove | Incomplete equalization checklist / valve tag IDs or target states (procedure crumbs, not walkthrough) | Yes |
| Note C — Manifold | Ops residue / “do not open hatch under unequal pressure” | Yes |
| Note D — Warning / Witness adjacent | Unease near pipe noise after circulation returns | Optional |
| Env-only | Stuck gauges, valve wheels, coolant stains, abandoned cart, pressure hatch seal paint | Yes |
| Env-only Tool Spur | Tags / wrenches as dressing only if spur kept | Optional |

**Rules:** Notes = symptoms and residue of work. **No walkthrough** (“go south then turn valve A”). No exposition dumps. No audio-log monologues.

---

# 5. Puzzle Design

## Objective

Equalize / open the coolant pressure loop so the pressure hatch unlocks and Engineering mechanical systems respond.

## Learning

- PE-017 taught **fuse → aux electrical restore**.  
- PE-018 taught **fuel → generator → main plant restore**.  
- PE-019 teaches **gauges → valves → pressure / coolant path** (Mechanical) as the consequence of live power without finished cooling.

## Failure

- Wrong valve / incomplete set → readable feedback (stuck hatch / unequal gauge state) — not punitive, not timed.  
- No Witness soft-lock during solve.  
- No randomized solution.  
- SliceReset must restore valve/puzzle state if replay claimed.

## Reward

- Pressure hatch unlock.  
- Ventilation / ambient / PA feedback (real audio or tagged debt).  
- Objective update (“Access the next area” / equivalent).  
- Story beat: plant circulation returns; Witness notices.

## Family mapping (PE-015 / bible §5)

| Element | Family | Implementation |
|---------|--------|----------------|
| Valve / pressure solve | Mechanical | New thin child `BP_CoolantLoopPuzzle` of `BP_PuzzleBase` + valve interactables (`BPI_Interactable`) — **minimize**; no parallel framework |
| Hatch / lights / vent | Reward layer | `WorldResponseTargets` → `BPI_PowerReceiver` (`BP_PoweredDoor` or pressure-hatch twin, `BP_VentilationUnit`, ambient / PA, EmergencyLight if needed) |
| Optional PowerManager notify | Electrical coupling | `bNotifyPowerOnSolve` / `NotifyPuzzlePowerResponse` **only if** tagged receivers need it — **never** touch generator `HasHandledPower` |
| Observation notes | Environmental Observation | `BP_NotePickup` + `BPC_Objective` |

**Preferred solve shape (locked for approval):**  
2–3 labeled valve interacts that must match Note B target states → puzzle `MarkSolved`. **No inventory gate** in v1 (cut Tool Spur inventory). If playtest finds observation too thin, EP may allow a single tagged tool later — not in default scope.

**Explicit non-builds:** No Security console / keycard, no fuse panel, no `BP_Generator` / FuelCan redo, no chase AI, no multi-step Machine Assembly, no timed sequences.

---

# 6. Horror Design

Psychological only — no combat, no chase AI.

### Tension curve

```text
Unease (live power / dead coolant) → Focus (gauges / valves) → Relief (loop opens) → Spike (Witness on exit) → Release (hatch)
```

### Witness

| Field | Spec |
|-------|------|
| Pattern | Reuse `BP_WitnessSilhouetteHint` as receiver on puzzle World Response targets |
| When | After Mechanical solve — **not** during valve work |
| Where | Exit approach corridor (not spawn) |
| What | Delayed tension → silhouette + cold light → withdraw; mesh hidden until post-solve |
| Rules | Bible §8 — pressures attention; never replaces solvable logic |

### Lighting

- Indoor baseline: post-power industrial (partial restore from narrative continuity), Coolant Ops damper / wetter than Annex.  
- No outdoor Directional/Sky dominance (PE-017A lesson).  
- On solve: vent / lamp flicker affirmation; Witness = brief cold accent.

### Audio

- Pre-solve: distant generator hum bleed + coolant silence / drip / pipe tick.  
- On solve: circulation rush / vent start / relay.  
- Witness: low tension line.  
- **Debt tag allowed:** PrintString stand-ins — list in mission debt; do not claim Production Ready on audio alone.

---

# 7. Technical Plan

## Reused systems (preferred path)

| System | Assets |
|--------|--------|
| Interaction | `BPC_Interaction`, `BPI_Interactable`, doors / hatch pattern |
| Objectives | `BPC_Objective`, `WBP_Objective` |
| Notes | `BP_NotePickup` (`ObjectiveOnRead` skip-if-empty) |
| Puzzle base | `BP_PuzzleBase`, `BPI_Puzzle`, `BP_PuzzleResetButton` pattern |
| Power / response | `BPI_PowerReceiver`, `BP_PoweredDoor` (or hatch configured as such), `BP_VentilationUnit`, `BP_EmergencyLight`, ambient / PA / DistantActivityHint; optional `BP_PowerManager.NotifyPuzzlePowerResponse` |
| Horror | `BP_WitnessSilhouetteHint` (+ `ResetPresence`) |
| Reset pattern | PE-017A / PE-018 `BP_*Reset` twin |
| Player | Existing `BP_PlayerCharacter` / Controller — no redesign |
| Map recipe | PE-018 production map pattern |

## New / modified (minimize)

| Item | Need? | Notes |
|------|-------|-------|
| Map `LV_ARI_CoolantBay` | **Yes** | `/Game/ProjectEcho/Maps/Production/` |
| `BP_CoolantLoopPuzzle` (`BP_PuzzleBase` child) | **Yes (thin)** | First Mechanical family reference; config-heavy; no framework fork |
| Valve interactable actors | **Likely** | Prefer child/component of puzzle or small interactable BPs — not a second puzzle framework |
| Notes content (instances) | **Yes** | Config only on `BP_NotePickup` |
| `BP_CoolantBayReset` | **Likely** | Full reverse: hatch, lights, Witness, puzzle state, valves, notes, objectives, ambient flags |
| Soft Open Level wiring | **Yes (post-approval)** | Annex Powered Exit → Open Level Coolant Bay; plan Maintenance→Annex if still unpaid debt |
| Modify `BP_PowerManager` / Generator | **Avoid** | |
| Fuse / Maintenance assets | **No** | PE-017A ownership |
| Security / keycard systems | **No** | |
| New UI / inventory framework | **No** | |
| Witness AI / chase | **No** | |

## Soft Open Level (plan wiring — do not implement in planning)

| Link | Spec |
|------|------|
| Generator Annex → Coolant Bay | On Powered Exit successful open/interact → Open Level `LV_ARI_CoolantBay` (or GameMode travel helper already used if any) |
| Coolant Bay entry | Spawn in Entry / Transfer Corridor; objective BeginPlay via Reset actor |
| Coolant Bay exit | Stub Soft Open / end-of-slice only (future Security) — destination TBD, not built |
| Maintenance → Annex | PE-018 debt; optional companion wiring under same travel pass — EP call at implement |

## Data / folders

- Map: `/Game/ProjectEcho/Maps/Production/LV_ARI_CoolantBay`  
- Puzzle: `/Game/ProjectEcho/Gameplay/Puzzle/` (CoolantLoop child beside Fuse)  
- Mission notes (post-implement): `Documents/05_Missions/PE-019-CoolantBay.md`  
- No mission IDs in asset names (`ContributionGuide`).

## Independence note

- Generator `HasHandledPower` path stays Annex-owned.  
- Coolant solve uses puzzle World Response / optional `NotifyPuzzlePowerResponse` only.  
- Do not require live Generator actor inside Coolant map for v1 — narrative post-power baseline is map lighting/audio config.

## Dependencies

- PE-018 Annex implemented (Technical PASS recorded; Gameplay PASS may still be PENDING_USER).  
- PE-015 / PE-017A patterns available.  
- Human PIE for Enhanced Input Gameplay PASS.  
- Existing industrial prop packs for dressing.

---

# 8. Risk Assessment + Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Scope creep (valve + keycard + fuse) | Schedule / bible violation | Cut list locked: Mechanical valves only; Security / fuse / generator deferred |
| New puzzle BP becomes framework fork | Maintainability | Thin `BP_PuzzleBase` child only; mirror Fuse patterns; no new managers |
| Soft-lock on wrong valve order | Player frustration | 2–3 valves max; readable fail; no timer; clue-backed IDs |
| PE-017 / PE-018 Gameplay PASS still pending | Building on unvalidated foundation | Gate: wait for human PIE **or** EP written waiver before Ready to Implement |
| Soft Open Level confusion | Continuity break | Clear exit interact → load Coolant; Note A reinforces Engineering coolant |
| SliceReset incomplete | False Replay PASS | Mirror PE-018 full reverse checklist for valves + puzzle + hatch + Witness |
| Witness during solve | Unfair pressure | Exit-path presence only post-solve |
| Audio PrintString | Atmosphere gap | Tag debt; lighting + Witness carry tension |
| Over-dressed geo | Art sink | Blockout spine first; dressing after loop works |
| Treating Coolant as powered-door-only | Misses Mechanical teaching | Require valve state solve before hatch — not inventory key alone |

---

# 9. Implementation Plan (phased milestones)

> Execute **only after approval**. Order is intentional.

### Phase 0 — Preconditions

- Confirm PE-017A / PE-018 manual PIE checklist (or EP waiver).  
- Freeze this design plan; ADR only if diverging from bible.  
- Confirm Soft Open Level approach (Open Level vs existing travel helper).

### Phase 1 — Map blockout + flow

- Create `LV_ARI_CoolantBay` blockout (≤5 rooms; Tool Spur optional/cut).  
- Place spawn, gauges (env), valves, CoolantLoopPuzzle, Pressure Hatch / PoweredDoor, Witness, receivers.  
- Verify compass / objective chain text.

### Phase 2 — Mechanical ops loop

- Valve states → `MarkSolved` → World Response → hatch unlock.  
- Notes A–C symptoms-only.  
- Objectives: investigate coolant → read gauges / locate procedure → equalize loop → access next area.

### Phase 3 — Soft Open Level wiring

- Generator Annex Powered Exit → Open Level Coolant Bay.  
- Optional: Maintenance → Annex if EP includes PE-018 travel debt.  
- Smoke isolated PIE spawn on Coolant map still works.

### Phase 4 — Horror + lighting

- Wire Witness on exit path via World Response targets.  
- Indoor lighting pass (post-power baseline + solve affirmation).  
- Audio prints or real cues (debt-tag if needed).

### Phase 5 — SliceReset + regression

- `BP_CoolantBayReset` full reverse.  
- Smoke: Annex generator path still independent; Maintenance fuse path untouched.  
- No PE-015 architecture redesign.

### Phase 6 — Dressing + docs

- Prop pass from existing packs.  
- Mission completion doc + Changelog / ProjectHealth / Roadmap updates.  
- Manual PIE checklist for EP.

### Phase 7 — Review gates

- Compile PASS → Technical Simulate PASS → **Human PIE Gameplay PASS** → Replay PASS → Ready for Review.

---

# Reused Systems (summary)

Interaction, Notes, Objectives, PE-015 `BP_PuzzleBase`, Power receivers (`BPI_PowerReceiver`, PoweredDoor / hatch, VentilationUnit, EmergencyLight, ambient/PA), Witness silhouette, SliceReset twin pattern, existing player/controller, PE-018 map recipe.

# New Assets (minimize)

| Asset | Why |
|-------|-----|
| `LV_ARI_CoolantBay` | New production map |
| `BP_CoolantLoopPuzzle` (+ valve interact wiring) | First Mechanical family teaching beat |
| `BP_CoolantBayReset` | Replay / SliceReset |
| Note instance text | Config only |
| Soft Open Level hooks | Travel continuity (Annex → Coolant) |

# Scope

## In scope

- One Coolant Bay production map (≤5 rooms)  
- One Mechanical ops teaching beat  
- World Response + exit-path Witness  
- Soft Open Level plan: Annex → Coolant (implement post-approval)  
- SliceReset if replay claimed  
- Docs on implement (Changelog append, mission notes)

## Out of scope

- Security / keycards / surveillance  
- Fuse panel / Maintenance fork (PE-017A)  
- Generator / FuelCan redo  
- Combat / chase / Witness AI  
- Save / journal UI  
- Multi-wing streaming / map merge  
- Timed fail sequences / multi-machine assemblies  
- Coolant as env-only again (that was PE-018; this mission pays it off)

# Success Criteria

1. Player understands **post-power Mechanical work** without tutorial UI.  
2. Valve → hatch → Witness → exit loop completes in ~6–12 minutes.  
3. Soft Open Level from Annex exit reaches Coolant spawn (when implemented).  
4. Compile + Technical Simulate PASS; Gameplay PASS human-gated honestly.  
5. Replay PASS only if SliceReset fully reverses mutated state.  
6. No new core frameworks; PE-017A fuse ownership preserved.  
7. Docs match implemented truth.

---

# Cross-Team Internal Review Notes

| Role | Flag | Simplification |
|------|------|----------------|
| **EP** | Best next ≠ biggest | One map, one Mechanical beat, Soft Open only, Security deferred |
| **LD** | Room count | ≤5; Tool Spur optional cut |
| **GD** | Family teaching | Mechanical via thin PuzzleBase child — not Security mid-jump |
| **Horror** | Escalation without chase | Same silhouette pattern; timing/placement only |
| **Tech** | New BP surface | One CoolantLoop child + Reset twin; avoid PowerManager/Generator edits |

### Suggested objective chain (draft)

| Trigger | Objective text (draft) |
|---------|------------------------|
| BeginPlay / entry | Investigate the coolant bay |
| Note B / Gauge Alcove | Equalize the coolant pressure loop |
| Valve progress / near-solve | Open the pressure hatch path |
| Puzzle World Response | Access the next area |

---

# Compliance Checklist

### Gameplay Design Bible

| Rule | PE-019 plan |
|------|-------------|
| Facility realism | Coolant Bay is Engineering workplace adjacent to Generator |
| Observation over guessing | Gauges + notes before valves |
| No anti-patterns | No glyph pads / arbitrary sequences without facility labels |
| Pillars / loop integrity | Explicit flow mapping |
| Witness pressures, never replaces logic | Exit-path presence only |
| Horror fair | Readable incomplete-loop feedback |
| Extend PE-015 / compose systems | Thin Mechanical child only |
| Progression = knowledge + access | Post-power Mechanical literacy + hatch |
| Sandbox / independence | Generator vs puzzle power paths preserved |
| Tone | Isolated, scientific, grounded |

### Story / Facility

| Source | Alignment |
|--------|-----------|
| Story Bible | Notes + env; Witness uncertainty; no exposition dump |
| Facility Bible | Engineering continuum after Generator; Security zone deferred |
| Room Bible | Each room: function / what happened / why player is here |

### Production Standard / Playbook

| Standard | Plan commitment |
|----------|-----------------|
| Design Plan before implement | This document; WAIT FOR APPROVAL |
| PE-018 map recipe | Default template for Coolant Bay |
| PE-017A fuse ownership | Not forked |
| Human PIE for Gameplay PASS | Required before Ready / VS close |
| Reset if replay claimed | SliceReset full reverse |
| Lighting intentional | Post-power indoor baseline; no outdoor sun dominance |
| Audio real or tagged debt | Explicit debt allowed |
| Symptoms not walkthrough notes | Note rules locked |
| No combat / chase / UI invent | Out of scope |
| Soft Open Level | Planned Annex → Coolant; not implemented in planning |

---

# Approval Block

| Field | Value |
|-------|-------|
| Ready for Approval | **YES** |
| Ready to Implement | **NO** — **WAIT FOR APPROVAL — DO NOT IMPLEMENT** |
| Map | `LV_ARI_CoolantBay` |
| Wing | Coolant Bay (Mechanical / pressure loop) |
| Primary family | Mechanical (`BP_CoolantLoopPuzzle`) |
| Soft Open Level | Generator Annex exit → Coolant Bay (plan wiring only) |
| Deferred | Security checkpoint, fuse fork, generator redo, Tool Spur inventory, Witness AI, Save, timed valves |

**WAIT FOR APPROVAL — DO NOT IMPLEMENT**

---

## Document Control

| | |
|--|--|
| Created | 2026-07-25 |
| Mission | PE-019 Design Plan only |
| Owners | Design (EP / LD / GD / Horror / Tech review) |
| Related | `PE-018-DesignPlan.md`, `PE-018-GeneratorAnnex.md`, `PE-017-VerticalSlice01.md`, `GameplayDesignBible.md`, `FacilityBible.md`, `ProductionPlaybook.md` |

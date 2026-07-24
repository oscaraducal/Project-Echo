# PE-020 — Design Plan: Research Wing (Post-Coolant Laboratory)

**Status:** Archived with Close — **APPROVED & IMPLEMENTED** (mission Closed — Technical; Gameplay PENDING_USER)  
**Branch:** `develop`  
**Priority:** High (campaign beat after PE-019 Coolant Bay)  
**Map:** `/Game/ProjectEcho/Maps/Production/LV_ARI_ResearchWing`  
**Wing name:** **Research Wing** (laboratory / observation / containment)  
**Design authority:** `Documents/01_Game_Design/GameplayDesignBible.md` (PE-016)  
**Puzzle framework:** PE-015 (`BP_PuzzleBase` / families) — **compose existing systems; no framework fork**  
**Map recipe:** **PE-018** (`LV_ARI_GeneratorAnnex` pattern) — Playbook §10  
**Fuse path:** Owned by **PE-017A** — do not duplicate  
**Predecessor:** `LV_ARI_CoolantBay` (PE-019 — pressure/coolant stable)  
**Soft Open Level:** Coolant Bay exit → Open Level → Research Wing  
**Mission notes:** [`PE-020-ResearchWing.md`](PE-020-ResearchWing.md) (Closed — Technical)  
**VDP:** [`PE-020-VisualDesignPackage.md`](PE-020-VisualDesignPackage.md) — post-hoc package archived with Close (not a pre-implement APPROVE)  
**Close date:** 2026-07-25

---

> ### Gate
>
> **APPROVED & IMPLEMENTED** (EP: Implement Mission PE-020)  
> Ready for Approval: **YES** · Ready to Implement: **YES** · Implemented: **YES**  
> Mission notes: `Documents/05_Missions/PE-020-ResearchWing.md`

---

## Connection from Coolant Bay

| From | To | How |
|------|-----|-----|
| `LV_ARI_CoolantBay` Pressure Hatch / Soft Open Exit | `LV_ARI_ResearchWing` Entry / Transfer Corridor | After PE-019 Mechanical solve + exit interact, **Soft Open Level** loads Research Wing |

**Narrative bridge (symptoms, not walkthrough):**  
Coolant pressure / plant circulation is stable enough that **lab environmental systems** can be brought online. Research staff left a **containment / sample calibration** unfinished when evacuation hit. Exit signage / one corridor note points toward the Research Wing — not a quest-marker dump.

**Travel model (this mission):**

1. **In-scope:** Soft Open Level from Coolant Bay exit → `LV_ARI_ResearchWing`.  
2. Do **not** build multi-wing streaming. Do **not** merge Research into Coolant.  
3. Security remains deferred (PE-019 stub destination superseded by Research as next laboratory sector per Facility Bible Research zone).

**Power / systems continuity:** Research Wing starts **post-power + post-coolant** — plant feed and circulation are narrative baseline (partial lab lighting / hum). The ops problem is **Research Equipment**, not another generator or valve run.

---

## Why this wing (Research — not Security)

| Candidate | Verdict |
|-----------|---------|
| **Research Wing** | **Selected.** FacilityBible Research zone (Experiment Chambers, Observation Rooms). Mid-game after Mechanical/coolant: plant stable → labs become accessible / relevant. Bible §5.4 Research Equipment: calibrate / containment / sample as one coherent ops problem. |
| Security Checkpoint | **Deferred.** Still a stakes jump; PE-019 stub “future Security” yields to Research as next laboratory sector. Security may gate Restricted later. |
| Electrical Control | **Not selected.** Fuse literacy already taught; PE-017A ownership. |
| Restricted / Project Echo Wing | Far too early. |

**Pillars served:** Exploration, Observation, Psychological Tension, Environmental Storytelling, Meaningful Progression.  
**Loop stages:** Explore → Discover → Understand → Solve → Restore Progress → Reveal Story → Survive → Proceed.  
**Puzzle family:** **Research Equipment** (primary) — thin `BP_PuzzleBase` child + interactable chamber/console/sample stations; world response via existing `BPI_PowerReceiver` patterns.

---

# Mission Brief

| Field | Content |
|-------|---------|
| **Mission** | PE-020 Research Wing |
| **Player experience goal** | 15–20 minute laboratory beat after Coolant Bay: **environmental storytelling first**, then teach **observe procedure → calibrate containment / sample handshake → release lab exit lock**, then Witness on exit — without combat, chase, Security keycards, fuse forks, inventory redesign, or new core frameworks. |
| **Teaching beat** | Research Equipment (calibrate / containment / sample) as consequence of stable plant systems — distinct from fuse, generator fuel, and coolant valves. |
| **End state** | Containment handshake complete → lab exit unlock + observation / ambient response → Witness presence on exit approach → Soft Open stub toward future zone (Security / Restricted — not built). |
| **Target length** | ~15–20 minutes first play. Prefer 5–7 rooms max with clear cuts; denser env clues before extra mechanics. |

---

# Gameplay Loop

```text
Spawn (post-coolant entry) → Explore → Observe (env + notes) → Research Equipment solve → World Response → Witness / Horror → Exit (Soft Open stub)
```

| Stage | What happens | Why |
|-------|--------------|-----|
| **Spawn** | Entry / Transfer Corridor from Coolant Soft Open. Flashlight available. Partial lab lighting / hum (post-power + post-coolant), but containment / observation still mid-procedure. Objective: investigate Research Wing / stabilize lab ops. | Continuity from PE-019. |
| **Explore** | Hub corridor: Observation Gallery, Sample Prep, Containment Chamber / Ops, optional Records Alcove, Locked Lab Exit. | Facility realism; 5–7 rooms. |
| **Observe** | Dense env clues: abandoned prep trays, sealed sample carriers, incomplete calibration log, observation window frost / residue, procedure boards. Symptom notes only. | Env storytelling FIRST. |
| **Puzzle (ops)** | ONE coherent Research Equipment problem: calibrate chamber parameters + complete sample containment handshake → `MarkSolved`. | Bible §5.4; PE-015 child. |
| **World Response** | Lab exit unlock, observation lights / ambient / PA via `WorldResponseTargets` (+ optional `NotifyPuzzlePowerResponse` — **independent** of generator `HasHandledPower`). | World acknowledges Research restore. |
| **Witness / Horror** | Presence on **exit path** after solve — silhouette pattern; colder / quieter than Coolant. | Survive; bible §8. |
| **Exit** | Interact lab exit / Soft Open → proceed (stub next zone). | Meaningful progression. |

---

# Narrative Purpose

Engineering made the plant safe enough to run. Research never finished bringing a **containment / observation station** back to procedure. The wing is ordinary interrupted science — not a disaster set-piece. Player inherits unfinished lab work: complete the calibration / sample handshake so the observation lock clears and the institute’s research spaces become traversable again.

Story delivery: **environmental clues dense; notes symptoms-only**. No exposition dumps. No Witness over-explanation. No Project Echo Restricted truth dump.

---

# 1. Mission Overview

## Purpose

Deliver the **best next level** after Coolant Bay: one coherent Research wing that teaches the **Research Equipment** family under post-coolant consequences — PE-018 map recipe, denser env storytelling, without Security, combat, chase, or framework forks.

## Goals

1. Soft Open Level campaign continuation: Coolant exit → Research Wing.  
2. First Research Equipment teaching beat via thin `BP_PuzzleBase` child.  
3. One ops problem + world response + Witness + exit; env storytelling carries length.  
4. Deepen Asterion tone: labs waking feel wrong — systems return, something watches.

## Beginning

Player loads into `LV_ARI_ResearchWing` after Coolant Soft Open (or direct PIE spawn). Space is cleaner / clinical-industrial vs Engineering wetness. Lab exit locked. Containment / observation mid-procedure.

## End

Calibration + sample handshake complete → exit unlock + observation response → Witness on exit approach → stub Soft Open next zone. SliceReset supports replay.

---

# 2. Gameplay Flow

```text
Spawn → Explore → Observe → Puzzle (Research Equipment) → World Response → Witness/Horror → Exit
```

**Out of scope:** Chase, combat, Security keycards/consoles, fuse panel, generator fuel, coolant valve redo, multi-family puzzle chains, journal UI, save system, timed fail soft-locks, multi-zone streaming, inventory redesign.

---

# 3. Level Layout

**Map name:** `LV_ARI_ResearchWing`  
**Compass:** Match PE-017 / PE-018 / PE-019 (+Y = North, +X = East).

### Rooms (5–7 max; prefer 6)

| Room | Compass (suggested) | Role |
|------|---------------------|------|
| Entry / Transfer Corridor | West / spawn | Soft Open arrival; Note A (symptoms); path spine |
| Observation Gallery | North | Env storytelling + Note B (procedure crumbs / target params) — look through glass / boards |
| Sample Prep Bay | East | Sample carrier / prep residue; optional Note C; may hold one tagged sample interact if required by handshake |
| Containment Chamber / Lab Ops | Center / South | Primary Research Equipment solve (`BP_ContainmentCalibrationPuzzle` + console / chamber interacts) |
| Records Alcove (optional) | Short spur | Dense env notes / whiteboards — **cut first** if length pressure |
| Exit Approach + Lab Exit | Far South / East | Post-solve unlock; Witness; Soft Open stub |

### Connections

- Hub corridor: Entry ↔ Observation ↔ Prep ↔ Containment ↔ Exit.  
- Records Alcove optional dead-end.  
- Exit locked until Research solve World Response.  
- Light required backtrack Observation → Containment (read then apply) is OK for 15–20 min; no maze.

### Pacing

1. Quiet clinical entry (1–2 min) — hum vs unfinished silence.  
2. Observation Gallery densify story.  
3. Sample Prep — residue / optional sample interact.  
4. Focused calibrate / handshake in Containment.  
5. Relief — lights / lock clear.  
6. Pressure — Witness on exit.  
7. Release — Soft Open exit.

**Cut order if over length:** Records Alcove → optional Sample inventory gate (prefer no inventory) → never add a second puzzle family.

---

# 4. Environmental Storytelling

## What happened

After plant power (Annex) and coolant equalization (Coolant Bay), Research attempted to restart a **containment / observation station** for sample work. Evacuation mid-calibration. Chamber shows incomplete handshake. Observation glass and prep trays tell the story before notes do.

## Clues

| Type | Content | Required? |
|------|---------|-----------|
| Note A — Entry symptoms | Labs gated until containment stable / plant feed OK — **no directions** | Yes |
| Note B — Observation | Incomplete calibration targets / station IDs (procedure crumbs, not walkthrough) | Yes |
| Note C — Sample Prep | Sample residue / “handshake pending” | Yes |
| Note D — Containment | Do not open lab exit under incomplete containment | Yes |
| Note E — Witness adjacent | Unease near observation glass after systems return | Optional |
| Env-only | Frosted glass, sealed carriers, calibration stamps, abandoned stools, spill tape, PA mute tags | Yes (primary story density) |

**Rules:** Notes = symptoms and residue. **No walkthrough.** No exposition dumps. No audio-log monologues.

---

# 5. Puzzle Design

## Objective

Complete **ONE** Research Equipment ops problem: **calibrate containment chamber parameters and finish the sample containment handshake** so the lab exit unlocks and observation systems respond.

## Learning

- PE-017: fuse → aux electrical.  
- PE-018: fuel → generator → main plant.  
- PE-019: gauges → valves → pressure/coolant.  
- PE-020: observe logged params → calibrate chamber → sample handshake (Research Equipment).

## Preferred solve shape (locked)

1. **Observation:** Note B / boards give target calibration states (2–3 labeled station interacts: e.g. Temp / Containment Seal / Observation Link).  
2. **Sample handshake:** Interact sealed sample cradle / confirm sample present at chamber (prefer **no inventory gate** — cradle is in-chamber interact; if playtest thin, EP may allow single `KeyItem` later — not default).  
3. All stations match targets + handshake → `MarkSolved`.

**Readable fail:** Incomplete calibration feedback (amber lamps / PrintString debt); exit stays locked. No timer. No randomized solution.

## Family mapping

| Element | Family | Implementation |
|---------|--------|----------------|
| Calibrate + sample handshake | Research Equipment | Thin child `BP_ContainmentCalibrationPuzzle` of `BP_PuzzleBase` + station interactables — **minimize** |
| Exit / lights / observation | Reward | `WorldResponseTargets` → `BPI_PowerReceiver` (`BP_PoweredDoor` / SoftOpenExit, EmergencyLight, vent/PA/ambient, Witness) |
| Optional PowerManager notify | Electrical coupling | Only if tagged receivers need it — **never** touch generator `HasHandledPower` |
| Notes | Environmental Observation | `BP_NotePickup` + `BPC_Objective` |

**Explicit non-builds:** No Security console/keycard, no fuse, no generator/FuelCan, no coolant valves, no chase AI, no timed sequences, no inventory redesign.

---

# 6. Horror Design

Psychological only — no combat, no chase AI.

```text
Unease (quiet labs) → Focus (observe / calibrate) → Relief (handshake) → Spike (Witness on exit) → Release
```

| Field | Spec |
|-------|------|
| Pattern | Reuse `BP_WitnessSilhouetteHint` on puzzle World Response targets |
| When | After Research solve — **not** during calibration |
| Where | Exit approach (not spawn) |
| What | Delayed tension → silhouette + cold light → withdraw |
| Rules | Bible §8 — pressures attention; never replaces solvable logic |

Lighting: indoor clinical-dim baseline; no outdoor Directional/Sky dominance.  
Audio: PrintString debt allowed (`[PE020]`); tag in mission debt.

---

# 7. Technical Plan

## Reused systems

Interaction (`BPC_Interaction`, `BPI_Interactable`), Objectives, Notes (`BP_NotePickup`), `BP_PuzzleBase` / `BPI_Puzzle` / Reset button pattern, `BPI_PowerReceiver` / `BP_PoweredDoor` / SoftOpenExit / EmergencyLight / Ventilation / PA / ambient / DistantActivityHint, `BP_WitnessSilhouetteHint`, SliceReset twin pattern, existing player/controller, PE-018 map recipe, `BP_SoftOpenExit`.

## New / modified (minimize)

| Item | Need? | Notes |
|------|-------|-------|
| Map `LV_ARI_ResearchWing` | **Yes** | `/Game/ProjectEcho/Maps/Production/` |
| `BP_ContainmentCalibrationPuzzle` | **Yes (thin)** | First Research Equipment reference; config-heavy |
| Station / cradle interactables | **Likely** | Small interactables — not a second framework |
| `BP_ResearchWingReset` | **Yes** | Full reverse: exit, lights, Witness, puzzle, stations, notes, objectives, ambient |
| Soft Open Coolant → Research | **Yes** | Wire Coolant exit Soft Open to `LV_ARI_ResearchWing` |
| Soft Open Research exit | Stub next zone OR SoftOpenExit with TBD destination |
| Modify PowerManager / Generator | **Avoid** | |
| Fuse / Security / Inventory redesign | **No** | |

## Soft Open Level

| Link | Spec |
|------|------|
| Coolant Bay → Research Wing | On Coolant exit successful open/interact → Open Level `LV_ARI_ResearchWing` |
| Research entry | Spawn Entry / Transfer; objective BeginPlay via Reset actor |
| Research exit | Stub Soft Open / end-of-slice (future Security — not built) |

## Independence

- Generator `HasHandledPower` stays Annex-owned.  
- Coolant Mechanical path untouched except Soft Open destination wiring.  
- Research solve uses puzzle World Response only.

---

# 8. Risk Assessment + Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Scope creep (calibrate + keycard + fuse) | Schedule | Cut list: Research Equipment only |
| Framework fork | Maintainability | Thin PuzzleBase child; mirror CoolantLoop / Fuse patterns |
| Soft-lock on station order | Frustration | 2–3 stations max; readable fail; clue-backed IDs |
| 15–20 min via mechanics bloat | Feature creep | Length from **env density + light backtrack**, not second puzzle |
| Incomplete SliceReset | False Replay PASS | Full reverse checklist |
| Witness during solve | Unfair | Exit-path post-solve only |
| PE-019 Gameplay still PENDING_USER | Foundation | EP Implement waiver / proceed with Technical honesty |

---

# 9. Implementation Plan (phased)

### Phase 0 — Preconditions

- Freeze this plan under EP Implement approval.  
- Inspect PE-019 CoolantLoop / SoftOpenExit / CoolantBayReset patterns.

### Phase 1 — Map blockout + flow

- Create `LV_ARI_ResearchWing` (5–6 rooms).  
- Place spawn, notes, stations, puzzle, exit, Witness, receivers, lighting.

### Phase 2 — Research ops loop

- Station states + handshake → `MarkSolved` → World Response → exit unlock.  
- Notes A–D symptoms-only.  
- Objectives chain.

### Phase 3 — Soft Open wiring

- Coolant exit → Open Level Research Wing.  
- Smoke isolated PIE spawn on Research map.

### Phase 4 — Horror + lighting

- Witness exit path; indoor lighting; audio prints debt-tagged.

### Phase 5 — SliceReset + regression

- `BP_ResearchWingReset` full reverse.  
- Coolant / Annex / Maintenance paths independent.

### Phase 6 — Docs

- Mission completion doc + Changelog append.  
- Manual PIE checklist; Gameplay PENDING_USER.

---

# Reused Systems (summary)

Interaction, Notes, Objectives, PE-015 `BP_PuzzleBase`, Power receivers, SoftOpenExit, Witness silhouette, SliceReset twin, player/controller, PE-018 map recipe.

# New Assets (minimize)

| Asset | Why |
|-------|-----|
| `LV_ARI_ResearchWing` | New production map |
| `BP_ContainmentCalibrationPuzzle` (+ station interacts) | Research Equipment teaching beat |
| `BP_ResearchWingReset` | Replay / SliceReset |
| Note instance text | Config only |
| Soft Open Coolant → Research | Travel continuity |

# Scope

## In scope

- One Research Wing production map (5–7 rooms)  
- One Research Equipment ops teaching beat  
- Dense env storytelling  
- World Response + exit-path Witness  
- Soft Open Coolant → Research  
- SliceReset full reverse  
- Docs

## Out of scope

- Security / keycards / surveillance  
- Fuse / generator / coolant valve redo  
- Combat / chase / Witness AI  
- Save / journal UI / inventory redesign  
- Multi-wing streaming / map merge  
- Timed fails / multi-machine assemblies  
- Restricted / Project Echo Wing truth dump

# Success Criteria

1. Player understands Research Equipment ops without tutorial UI.  
2. Observe → calibrate/handshake → Witness → exit in ~15–20 minutes.  
3. Soft Open Coolant → Research works when implemented.  
4. Compile + Technical Simulate PASS; Gameplay PASS human-gated.  
5. Replay PASS only with full SliceReset.  
6. No new core frameworks; PE-017A fuse ownership preserved.  
7. Docs match implemented truth.

---

# Compliance Checklist

### Gameplay Design Bible — PASS planned

Facility realism; observation over guessing; no anti-patterns; Witness pressures never replaces logic; extend PE-015; progression = knowledge + access; tone isolated/scientific/grounded.

### Story / Facility — PASS planned

Notes + env; Witness uncertainty; Research zone after Engineering continuum; Security deferred.

### Production Standard — PASS planned

Design Plan before implement (this doc); PE-018 recipe; human PIE for Gameplay; SliceReset if replay; symptoms notes; no combat/chase.

---

# Approval Block

| Field | Value |
|-------|-------|
| Ready for Approval | **YES** |
| Ready to Implement | **YES** — **APPROVED & IMPLEMENTED** |
| Map | `LV_ARI_ResearchWing` |
| Wing | Research Wing (Research Equipment / containment calibration) |
| Primary family | Research Equipment (CoolantLoop/Valve instances configured as ST-* stations; twin BPs prepared) |
| Soft Open Level | Coolant Bay SoftOpenExit_Research → Research Wing |
| Deferred | Security, fuse, generator, coolant redo, inventory sample gate, Witness AI, Save, ResearchWingReset cutover |

**APPROVED & IMPLEMENTED** — mission **Closed — Technical** (Gameplay PENDING_USER). See `PE-020-ResearchWing.md`.

---

## Document Control

| | |
|--|--|
| Created | 2026-07-25 |
| Closed | 2026-07-25 (with mission) |
| Mission | PE-020 Design Plan |
| Owners | Design (EP / LD / GD / Horror / Tech) |
| Related | `PE-019-DesignPlan.md`, `PE-019-CoolantBay.md`, `GameplayDesignBible.md`, `FacilityBible.md`, `ProductionPlaybook.md` |

# PE-021 — Design Plan: Security Wing (Post-Research Access)

**Status:** Archived with Close — **APPROVED & IMPLEMENTED** (mission Closed — Technical; Gameplay PENDING_USER)  
**Branch:** `develop`  
**Priority:** High (campaign beat after PE-020 Research Wing)  
**Map:** `/Game/ProjectEcho/Maps/Production/LV_ARI_SecurityWing`  
**Wing name:** **Security Wing** (checkpoint / surveillance / access control)  
**Design authority:** `Documents/01_Game_Design/GameplayDesignBible.md` (PE-016)  
**Puzzle framework:** PE-015 (`BP_PuzzleBase` / families) — **compose existing systems; no framework fork**  
**Map recipe:** **PE-018** (`LV_ARI_GeneratorAnnex` pattern) — Playbook §10  
**Fuse path:** Owned by **PE-017A** — do not duplicate  
**Predecessor:** `LV_ARI_ResearchWing` (PE-020 — Soft Open LabExit → Security Wing wired)  
**Soft Open Level:** Research Wing LabExit → Open Level → Security Wing  
**Mission notes:** [`PE-021-SecurityWing.md`](PE-021-SecurityWing.md) (Closed — Technical)  
**VDP:** [`PE-021-VisualDesignPackage.md`](PE-021-VisualDesignPackage.md) — archived with Close (VDP-before-Implement held)  
**Close date:** 2026-07-25

---

> ### Gate
>
> **APPROVED & IMPLEMENTED** — mission **Closed — Technical** (Gameplay PENDING_USER)  
> PRB: **Approve with Conditions** ([`PE-021-ProductionReview.md`](PE-021-ProductionReview.md)) · Ready For Review: **NO**  
> Human PIE still open via [`PE-021-PlaytestChecklist.md`](PE-021-PlaytestChecklist.md) — reopen `Validate Mission PE-021` when ready.

---

## Connection from Research Wing

| From | To | How |
|------|-----|-----|
| `LV_ARI_ResearchWing` LabExit | `LV_ARI_SecurityWing` Entry / Checkpoint Transfer | After PE-020 Research Equipment solve + LabExit interact, **Soft Open Level** loads Security Wing |

**Narrative bridge (symptoms, not walkthrough):**  
Containment / observation handshake in Research is complete enough that **downstream access locks** matter again. Staff fled mid-lockdown; a checkpoint still holds the next corridor behind credentials and an unfinished clearance console. Exit signage / one corridor note points toward Security — not a quest-marker dump.

**Travel model (this mission):**

1. **In-scope:** Soft Open Level from Research LabExit → `LV_ARI_SecurityWing`.  
2. Do **not** build multi-wing streaming. Do **not** merge Security into Research.  
3. Wire Research `LabExit` (currently stub PoweredDoor) to Soft Open destination `LV_ARI_SecurityWing` — fulfills Roadmap remaining item “Research LabExit Soft Open to future Security.”

**Power / systems continuity:** Security Wing starts **post-power + post-coolant + post-containment** — plant feed and lab systems are narrative baseline (partial emergency / checkpoint lighting). The ops problem is **Security & Access**, not another generator, valve, fuse, or research calibration run.

---

## Why this wing (Security & Access — not Signal)

| Candidate | Verdict |
|-----------|---------|
| **Security Wing** | **Selected.** FacilityBible Security zone (Checkpoints, Surveillance Room; Armory future). Roadmap Remaining explicitly lists Soft Open Research → Security. Bible §5.3 Security & Access: credentials + lockouts as mid-game literacy after Engineering + Research. PE-020 deferred Security as next sector. |
| Signal & Communication | **Deferred.** Bible §5.5 is a strong later beat (PA / relay / diegetic voice) and couples well after access opens deeper corridors — not the immediate Soft Open destination from Research LabExit. |
| Electrical Control | **Not selected.** Fuse literacy already taught; PE-017A ownership. |
| Restricted / Project Echo Wing | Far too early — Security gates access *toward* Restricted later. |

**Pillars served:** Exploration, Observation, Psychological Tension, Environmental Storytelling, Meaningful Progression.  
**Loop stages:** Explore → Discover → Understand → Solve → Restore Progress → Reveal Story → Survive → Proceed.  
**Puzzle family:** **Security & Access** (primary) — compose `BP_KeyItemPickup` / `BPC_Inventory` + thin `BP_PuzzleBase` child (clearance console) + existing `BP_LockedDoor` / `BP_PoweredDoor` / SoftOpenExit patterns.

---

# Mission Brief

| Field | Content |
|-------|---------|
| **Mission** | PE-021 Security Wing |
| **Player experience goal** | 15–20 minute Security beat after Research Wing: **environmental storytelling first**, then teach **observe lockdown residue → recover staff credential → clear access console / checkpoint lockout → release Soft Open exit**, then Witness on exit — without combat, chase, fuse forks, generator/coolant/research redo, Signal family as a second puzzle, inventory redesign, or new core frameworks. |
| **Teaching beat** | Security & Access (keycard / clearance) as consequence of restored plant + lab systems — distinct from fuse, generator fuel, coolant valves, and Research Equipment. |
| **End state** | Clearance complete → checkpoint barrier / Soft Open exit unlock + surveillance / ambient response → Witness presence on exit approach → Soft Open stub toward future zone (Signal / deeper Admin / Restricted approach — not built). |
| **Target length** | ~15–20 minutes first play. Prefer 5–6 rooms with clear cuts; denser env clues before extra mechanics. |

---

# Gameplay Loop

```text
Spawn (post-Research Soft Open) → Explore → Observe (env + notes) → Security & Access solve → World Response → Witness / Horror → Exit (Soft Open stub)
```

| Stage | What happens | Why |
|-------|--------------|-----|
| **Spawn** | Entry / Checkpoint Transfer from Research Soft Open. Flashlight available. Partial checkpoint lighting / hum (post-power narrative baseline), but lockdown / clearance unfinished. Objective: investigate Security Wing / restore access. | Continuity from PE-020. |
| **Explore** | Hub: Checkpoint Lobby, Surveillance Alcove, Credential / Locker Bay, Access Control Console room, Locked Soft Open Exit. | Facility realism; 5–6 rooms. |
| **Observe** | Dense env clues: abandoned badge trays, lockdown tape, blank monitors, incomplete clearance log, visitor pass stamps, overturned chair at desk. Symptom notes only. | Env storytelling FIRST. |
| **Puzzle (ops)** | ONE coherent Security & Access problem: recover Staff Keycard + complete clearance console procedure → `MarkSolved`. | Bible §5.3; inventory + thin PuzzleBase. |
| **World Response** | Soft Open exit unlock, checkpoint lights / monitors / ambient via `WorldResponseTargets` (+ optional `NotifyPuzzlePowerResponse` — **independent** of generator `HasHandledPower`). | World acknowledges access restore. |
| **Witness / Horror** | Presence on **exit path** after solve — silhouette pattern; colder / more institutional than Research. | Survive; bible §8. |
| **Exit** | Interact Soft Open exit → proceed (stub next zone). | Meaningful progression. |

---

# Narrative Purpose

Engineering restored the plant. Research finished enough containment work that the institute’s **access layer** matters again. Security never finished clearing a **checkpoint lockdown** after evacuation — badges left mid-shift, console procedure incomplete. The wing is ordinary interrupted security ops — not an armory set-piece or Restricted reveal. Player inherits unfinished clearance: complete credential + console handshake so the checkpoint opens and the next sector becomes traversable.

Story delivery: **environmental clues dense; notes symptoms-only**. No exposition dumps. No Witness over-explanation. No Project Echo Restricted truth dump. No “how to open the door” walkthrough notes.

---

# 1. Mission Overview

## Purpose

Deliver the **best next level** after Research Wing: one coherent Security wing that teaches the **Security & Access** family under post-Research consequences — PE-018 map recipe, denser env storytelling, without Signal-as-second-puzzle, combat, chase, or framework forks.

## Goals

1. Soft Open Level campaign continuation: Research LabExit → Security Wing.  
2. First Security & Access teaching beat via existing inventory gate + thin `BP_PuzzleBase` child (no new frameworks).  
3. One ops problem + world response + Witness + exit; env storytelling carries length.  
4. Deepen Asterion tone: checkpoints waking feel wrong — systems return, something watches past the cameras.

## Beginning

Player loads into `LV_ARI_SecurityWing` after Research Soft Open (or direct PIE spawn). Space is institutional-industrial (badge desks, glass, cameras) vs Research clinical / Coolant wetness. Soft Open exit locked. Clearance unfinished.

## End

Keycard recovered + clearance console complete → exit unlock + surveillance/ambient response → Witness on exit approach → stub Soft Open next zone. SliceReset supports replay.

---

# 2. Gameplay Flow

```text
Spawn → Explore → Observe → Puzzle (Security & Access) → World Response → Witness/Horror → Exit
```

**Out of scope:** Chase, combat, Armory, Restricted / Project Echo Wing, fuse panel, generator fuel, coolant valve redo, Research Equipment redo, Signal/PA as primary or second puzzle family, multi-tier biometric cascade, journal UI, save system, timed fail soft-locks, multi-zone streaming, inventory redesign.

---

# 3. Level Layout

**Map name:** `LV_ARI_SecurityWing`  
**Compass:** Match PE-017 / PE-018 / PE-019 / PE-020 (+Y = North, +X = East).

### Rooms (5–6 max; prefer 5–6)

| Room | Compass (suggested) | Role |
|------|---------------------|------|
| Entry / Checkpoint Transfer | West / spawn | Soft Open arrival from Research; Note A (symptoms); path spine |
| Checkpoint Lobby | Center | Desk, tape, visitor residue; paths to Surveillance / Credential / Console |
| Surveillance Alcove | North | Env storytelling + Note B (lockdown / camera residue) — look at dark monitors / procedure boards |
| Credential / Locker Bay | East | Staff Keycard pickup (`BP_KeyItemPickup`); optional Note C |
| Access Control / Console Ops | South | Primary Security & Access solve (`BP_AccessClearancePuzzle` + console interacts) |
| Exit Approach + Soft Open Exit | Far South / East | Post-solve unlock; Witness; Soft Open stub next zone |

### Connections

- Hub: Entry ↔ Lobby ↔ Surveillance / Credential / Console ↔ Exit.  
- Surveillance Alcove short spur (env density; cut first if length pressure).  
- Soft Open Exit locked until Access Clearance World Response.  
- Light required backtrack Surveillance/Note → Console (read then apply) is OK for 15–20 min; no maze.  
- Optional: Lobby inner gate as `BP_LockedDoor` requiring Staff Keycard to reach Console — **preferred** if it keeps one coherent credential story; cut if it feels like two puzzles.

### Pacing

1. Quiet institutional entry (1–2 min) — camera hum vs unfinished silence.  
2. Lobby + Surveillance densify story.  
3. Credential Bay — recover keycard.  
4. Focused clearance console in Access Control.  
5. Relief — lights / monitors / lock clear.  
6. Pressure — Witness on exit.  
7. Release — Soft Open exit.

**Cut order if over length:** Surveillance Alcove → Lobby LockedDoor gate (allow direct Console access with keycard used only at console) → never add Signal/PA as second family → never Armory.

---

# 4. Environmental Storytelling

## What happened

After plant power (Annex), coolant equalization (Coolant Bay), and Research containment handshake (Research Wing), Security attempted to **clear a checkpoint lockdown** so staff could move toward deeper corridors. Evacuation mid-procedure. Badge trays and incomplete console logs tell the story before notes do.

## Clues

| Type | Content | Required? |
|------|---------|-----------|
| Note A — Entry symptoms | Access gated until lockdown clearance / plant feed OK — **no directions** | Yes |
| Note B — Surveillance | Incomplete clearance IDs / console station labels (procedure crumbs, not walkthrough) | Yes |
| Note C — Credential Bay | Badge trays abandoned / shift incomplete | Yes |
| Note D — Console Ops | Do not open exit corridor under incomplete clearance | Yes |
| Note E — Witness adjacent | Unease near camera banks after systems return | Optional |
| Env-only | Lockdown tape, blank monitors, visitor stamps, overturned chair, badge lanyards, PA mute tags, glass checkpoint | Yes (primary story density) |

**Rules:** Notes = symptoms and residue. **No walkthrough.** No exposition dumps. No audio-log monologues.

---

# 5. Puzzle Design

## Objective

Complete **ONE** Security & Access ops problem: **recover Staff Keycard and finish the access clearance console procedure** so the Soft Open exit unlocks and checkpoint systems respond.

## Learning

- PE-017: fuse → aux electrical.  
- PE-018: fuel → generator → main plant.  
- PE-019: gauges → valves → pressure/coolant.  
- PE-020: observe logged params → calibrate chamber → sample handshake (Research Equipment).  
- PE-021: observe lockdown residue → recover credential → clear access console (Security & Access).

## Preferred solve shape (locked)

1. **Observation:** Note B / boards give clearance procedure crumbs (2–3 labeled console states: e.g. Badge Present / Zone Unlock / Exit Arm).  
2. **Credential:** Interact `BP_KeyItemPickup` Staff Keycard in Credential / Locker Bay (`RequiredItemID` consistent with inventory data — reuse `BP_KeyItemPickup` / `BPC_Inventory`; **no inventory redesign**).  
3. **Clearance:** At Access Control console — present/consume keycard path + match procedure states → `MarkSolved`. Prefer thin `BP_AccessClearancePuzzle` child of `BP_PuzzleBase` (mirror Fuse / Containment config-heavy pattern). Optional Lobby `BP_LockedDoor` may gate Console if it stays one story.  
4. All required states + credential handshake → `MarkSolved`.

**Readable fail:** Incomplete clearance feedback (amber lamps / PrintString debt); exit stays locked. No timer. No randomized solution. No biometric cascade.

## Family mapping

| Element | Family | Implementation |
|---------|--------|----------------|
| Keycard + clearance console | Security & Access | `BP_KeyItemPickup` + thin `BP_AccessClearancePuzzle` (+ optional `BP_LockedDoor`) — **minimize** |
| Exit / lights / monitors | Reward | `WorldResponseTargets` → `BPI_PowerReceiver` (`BP_SoftOpenExit` / `BP_PoweredDoor`, EmergencyLight, PA/ambient, Witness) |
| Optional PowerManager notify | Electrical coupling | Only if tagged receivers need it — **never** touch generator `HasHandledPower` |
| Notes | Environmental Observation | `BP_NotePickup` + `BPC_Objective` |

**Explicit non-builds:** No fuse panel fork, no generator/FuelCan, no coolant valves, no Research Equipment redo, no Signal/PA primary puzzle, no Armory, no chase AI, no timed sequences, no inventory redesign, no Restricted truth dump.

---

# 6. Horror Design

Psychological only — no combat, no chase AI.

```text
Unease (quiet checkpoint) → Focus (credential / clearance) → Relief (lockout clears) → Spike (Witness on exit) → Release
```

| Field | Spec |
|-------|------|
| Pattern | Reuse `BP_WitnessSilhouetteHint` on puzzle World Response targets |
| When | After Access Clearance solve — **not** during console / keycard |
| Where | Exit approach (not spawn) |
| What | Delayed tension → silhouette + cold institutional light → withdraw |
| Rules | Bible §8 — pressures attention; never replaces solvable logic |

Lighting: indoor checkpoint-dim baseline; no outdoor Directional/Sky dominance (PE-017A lesson).  
Audio: PrintString debt allowed (`[PE021]`); tag in mission debt.

---

# 7. Technical Plan

## Reused systems

Interaction (`BPC_Interaction`, `BPI_Interactable`), Inventory (`BPC_Inventory`, `BP_KeyItemPickup`, `ST_InventoryItem`), Objectives, Notes (`BP_NotePickup`), `BP_PuzzleBase` / `BPI_Puzzle` / Reset button pattern, `BP_LockedDoor`, `BPI_PowerReceiver` / `BP_PoweredDoor` / SoftOpenExit / EmergencyLight / Ventilation / PA / ambient / DistantActivityHint, `BP_WitnessSilhouetteHint`, SliceReset twin pattern, existing player/controller, PE-018 map recipe, `BP_SoftOpenExit`.

## New / modified (minimize)

| Item | Need? | Notes |
|------|-------|-------|
| Map `LV_ARI_SecurityWing` | **Yes** | `/Game/ProjectEcho/Maps/Production/` |
| `BP_AccessClearancePuzzle` | **Yes (thin)** | First Security & Access reference; config-heavy; mirror Fuse / Containment |
| Console / station interactables | **Likely** | Small interactables — not a second framework |
| Staff Keycard item data | **Likely** | Config via existing `ST_InventoryItem` / KeyItemPickup — no redesign |
| `BP_SecurityWingReset` | **Yes** | Full reverse: exit, lights, Witness, puzzle, keycard/respawn, notes, objectives, ambient, LockedDoor |
| Soft Open Research → Security | **Yes** | Wire Research LabExit Soft Open to `LV_ARI_SecurityWing` |
| Soft Open Security exit | Stub next zone OR SoftOpenExit with TBD destination |
| Modify PowerManager / Generator | **Avoid** | |
| Fuse / Signal primary / Inventory redesign | **No** | |

## Soft Open Level

| Link | Spec |
|------|------|
| Research Wing → Security Wing | On Research LabExit successful open/interact → Open Level `LV_ARI_SecurityWing` (`BP_SoftOpenExit` or Soft Open props on LabExit) |
| Security entry | Spawn Entry / Checkpoint Transfer; objective BeginPlay via Reset actor |
| Security exit | Stub Soft Open / end-of-slice (future Signal / deeper sector — not built) |

## Independence

- Generator `HasHandledPower` stays Annex-owned.  
- Research Equipment path untouched except Soft Open destination wiring on LabExit.  
- Fuse path remains PE-017A-owned.  
- Security solve uses puzzle World Response (+ inventory) only.

## Visual Design Package

This Design Plan does **not** authorize Unreal work. Previs deliverable:

1. Creative supports as needed (`environment-designer` thin layout intent in VDP).  
2. **`Generate Visual Package PE-021`** — Experience → Blockout → Storyboard → Concept → Lighting Visualizer → Asset Placement — **complete**.  
3. EP VDP mental-play APPROVE → Ready to Implement YES.  
4. Only then `Implement Mission PE-021` (MCP Auto-accept applies at Implement only).

Deliverable: [`PE-021-VisualDesignPackage.md`](PE-021-VisualDesignPackage.md).

---

# 8. Risk Assessment + Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Scope creep (keycard + Signal PA + fuse) | Schedule | Cut list: Security & Access only |
| Framework fork | Maintainability | Thin PuzzleBase child; reuse KeyItemPickup / LockedDoor |
| Soft-lock on console order / missing keycard | Frustration | 2–3 console states max; readable fail; clue-backed IDs; SliceReset respawns keycard |
| 15–20 min via mechanics bloat | Feature creep | Length from **env density + light backtrack**, not second puzzle family |
| Incomplete SliceReset | False Replay PASS | Full reverse checklist incl. inventory / keycard respawn |
| Witness during solve | Unfair | Exit-path post-solve only |
| PE-020 Gameplay still PENDING_USER | Foundation | Proceed with Technical honesty; EP may waive / reopen Validate PE-020 separately |
| Implement before VDP | Process break | Ready to Implement stays **NO** until VDP EP APPROVE |

---

# 9. Implementation Plan (phased — after VDP APPROVE only)

### Phase 0 — Preconditions

- EP APPROVE Design Plan (proceed).  
- Creative / Previs: `Generate Visual Package PE-021` → EP VDP APPROVE → Ready to Implement YES.  
- Inspect PE-020 SoftOpen / LabExit, KeyItemPickup, LockedDoor, FusePuzzle inventory consume, SliceReset twins.

### Phase 1 — Map blockout + flow

- Create `LV_ARI_SecurityWing` (5–6 rooms).  
- Place spawn, notes, keycard, console, puzzle, exit, Witness, receivers, lighting.

### Phase 2 — Access ops loop

- Keycard + console states → `MarkSolved` → World Response → Soft Open exit unlock.  
- Notes A–D symptoms-only.  
- Objectives chain.

### Phase 3 — Soft Open wiring

- Research LabExit → Open Level Security Wing.  
- Smoke isolated PIE spawn on Security map.

### Phase 4 — Horror + lighting

- Witness exit path; indoor lighting; audio prints debt-tagged.

### Phase 5 — SliceReset + regression

- `BP_SecurityWingReset` full reverse (incl. keycard respawn / inventory clear as applicable).  
- Research / Coolant / Annex / Maintenance paths independent.

### Phase 6 — Docs

- Mission completion doc + Changelog append.  
- Manual PIE checklist; Gameplay PENDING_USER.

---

# Reused Systems (summary)

Interaction, Inventory (`BPC_Inventory`, `BP_KeyItemPickup`), Notes, Objectives, PE-015 `BP_PuzzleBase`, `BP_LockedDoor`, Power receivers, SoftOpenExit, Witness silhouette, SliceReset twin, player/controller, PE-018 map recipe.

# New Assets (minimize)

| Asset | Why |
|-------|-----|
| `LV_ARI_SecurityWing` | New production map |
| `BP_AccessClearancePuzzle` (+ console interacts) | Security & Access teaching beat |
| `BP_SecurityWingReset` | Replay / SliceReset |
| Staff Keycard item / pickup instance | Config via existing KeyItem path |
| Note instance text | Config only |
| Soft Open Research → Security | Travel continuity (LabExit wiring) |

# Scope

## In scope

- One Security Wing production map (5–6 rooms)  
- One Security & Access ops teaching beat (keycard + clearance console)  
- Dense env storytelling  
- World Response + exit-path Witness  
- Soft Open Research → Security  
- SliceReset full reverse  
- Docs  
- VDP later (Generate Visual Package) before Implement

## Out of scope

- Signal & Communication as primary or second puzzle  
- Armory / Restricted / Project Echo Wing  
- Fuse / generator / coolant / Research Equipment redo  
- Combat / chase / Witness AI  
- Save / journal UI / inventory redesign  
- Multi-wing streaming / map merge  
- Timed fails / biometric cascades / multi-tier card ladders  
- Unreal implementation before Design Plan + VDP EP APPROVE

# Success Criteria

1. Player understands Security & Access ops without tutorial UI.  
2. Observe → keycard/clearance → Witness → Soft Open exit in ~15–20 minutes.  
3. Soft Open Research → Security works when implemented.  
4. Compile + Technical Simulate PASS; Gameplay PASS human-gated.  
5. Replay PASS only with full SliceReset (incl. credential state).  
6. No new core frameworks; PE-017A fuse ownership preserved; PE-020 Research systems untouched except Soft Open wiring.  
7. Docs match implemented truth.  
8. VDP EP-approved before Ready to Implement.

---

# Compliance Checklist

### Gameplay Design Bible — PASS planned

Facility realism; observation over guessing; no anti-patterns; Witness pressures never replaces logic; extend PE-015 + inventory; progression = knowledge + access; tone isolated/scientific/grounded; §5.3 Security & Access teaching beat.

### Story / Facility — PASS planned

Notes + env; Witness uncertainty; Security zone after Research continuum; Signal / Restricted deferred; Armory future.

### Production Standard — PASS planned

Design Plan before implement (this doc); PE-018 recipe; VDP before Ready to Implement (§12c); human PIE for Gameplay; SliceReset if replay; symptoms notes; no combat/chase; MCP Auto-accept only at Implement.

---

# Approval Block

| Field | Value |
|-------|-------|
| Ready for Approval | **YES** |
| Ready to Implement | **YES** — EP `Implement Mission PE-021` after VDP |
| Implemented | **YES** — Technical PASS; Gameplay PENDING_USER |
| Map | `LV_ARI_SecurityWing` |
| Wing | Security Wing (Security & Access / checkpoint clearance) |
| Primary family | Security & Access (`BP_KeyItemPickup` + thin `BP_AccessClearancePuzzle`) |
| Soft Open Level | Research LabExit → Security Wing (**wired**) |
| Deferred | Signal & Communication, Armory, Restricted, fuse, generator, coolant/research redo, Witness AI, Save, multi-tier biometrics |
| VDP | [`PE-021-VisualDesignPackage.md`](PE-021-VisualDesignPackage.md) — implemented against package |

**APPROVED & IMPLEMENTED** — mission **Closed — Technical** (Gameplay PENDING_USER). See `PE-021-SecurityWing.md`.

---

## Document Control

| | |
|--|--|
| Created | 2026-07-25 |
| Closed | 2026-07-25 (with mission) |
| Mission | PE-021 Design Plan |
| Owners | Design (EP / LD / GD / Horror / Tech) |
| Related | `PE-020-DesignPlan.md`, `PE-020-ResearchWing.md`, `GameplayDesignBible.md`, `FacilityBible.md`, `ProductionPlaybook.md`, `Roadmap.md` |

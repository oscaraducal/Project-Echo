# Project Echo — Production Playbook

**Status:** Active (authoritative production process)  
**Version:** 1.4  
**Established:** 2026-07-25  
**Validated:** FRAMEWORK-001 (`Documents/04_Production/AIStudio/ValidationReport-FRAMEWORK-001.md`)  
**Authority:** Production process source of truth for AI Studio Phase 1+  
**Consolidates lessons from:** PE-017, PE-017A, PE-018  
**Creative Studio:** AI Studio Phase 2 — `Documents/04_Production/AIStudio/CreativeStudio/`  
**Previsualization Studio:** AI Studio Phase 3 — `Documents/04_Production/AIStudio/PrevisualizationStudio/`  
**Mission Director:** AI Studio Phase 4 — `Documents/04_Production/AIStudio/MissionDirector/`

---

## Purpose

This playbook defines how Project Echo is designed, implemented, validated, reviewed, and documented.

It does **not** redefine game vision. Vision lives in:

1. Story Bible  
2. Gameplay Design Bible  
3. This Production Playbook (process + standards)  
4. Architecture Decision Records (ADR)  
5. Mission Brief  

Supporting implementation truth: `Documents/02_Technical/*`, `Documents/00_Governance/ContributionGuide.md`.

---

# 1. Development Philosophy

Always prioritize:

- Player experience over feature count  
- Atmosphere over complexity  
- Environmental storytelling over exposition  
- Reusing existing systems over creating new ones  
- Small, polished iterations over large unfinished systems  
- Maintainability over clever implementations  

Avoid feature creep.

When multiple valid solutions exist, choose the **lowest long-term maintenance cost**.

Every completed mission should leave the project better in gameplay, atmosphere, storytelling, maintainability, and production quality — without expanding scope unnecessarily.

---

# 2. Production Lifecycle

```text
EP Command → Mission Director (orchestrates skills)
  → Design Plan → EP proceed
  → Creative (as needed) → Previs / Visual Design Package → EP VDP APPROVE
  → Implementation → Compile → Technical Simulate
  → Human PIE (Gameplay) → Replay (if claimed) → Docs → Commit/Push
  → Production Review Board → EP Decision → Merge → Close
```

### Roles (summary)

| Role | Owner | Core duty |
|------|-------|-----------|
| Executive Producer | Oscar | Vision, high-level commands, VDP mental play, human Gameplay, merge |
| Mission Director | Cursor (orchestration) | Select skills, order, gates, deliverables from EP commands |
| Design / Tech guidance | ChatGPT (or designated) | Architecture, mission design review, bible compliance |
| Implementation | Cursor AI (via Director → skills) | UE5 Blueprints/maps/docs per approved brief; honest gates |

EP issues: `Start|Continue|Generate Visual Package|Implement|Validate|Review|Close Mission PE-###`.  
EP does **not** manually coordinate individual Skills — see §12d.  
Commanded `Implement Mission` (or sticky `auto accept`) authorizes Unreal MCP asset creation for that mission — see `AIStudio/MissionDirector/MCP-AutoAccept-Policy.md` (does not waive VDP / Gameplay PASS).

Detailed role boundaries: `.cursor/agents/` and `Documents/04_Production/AIStudio/`.

---

# 3. Mission Lifecycle

1. **Mission Specification / Design Plan** — scope, reused systems, cut list, risks  
2. **Design Plan approval** — plan accepted to proceed into Creative / Previs (not yet implement)  
2b. **Creative Studio pass** (when the mission needs environment / art assets) — Environment (+ parallel Creative skills); Asset Creation Planner → Coordinator as needed — see §12b  
2c. **Previsualization Studio** — Experience → Blockout Visualizer → Storyboard → Concept / Lighting Visualizer / Asset Placement → **Visual Design Package** — see §12c  
2d. **EP Visual Design Package Approval** — permanent rule: **no production mission enters implementation until VDP is EP-approved** (mental play gate). This sets **Ready to Implement**  
3. **Implementation** — minimal scope; reuse first (`mission-implementer` only after 2d)  
4. **Compile** — no Blueprint errors  
5. **Technical Simulate / PIE** — boot, bind, state checks (Slate may assist)  
6. **Human PIE Gameplay PASS** — Oscar (Enhanced Input cannot be fully automated)  
7. **Replay PASS** — only if SliceReset / replay is claimed  
8. **Documentation** — mission doc, Changelog append, systems/health as needed  
9. **Git Commit / Push** — when requested; never failing code  
10. **Production Review Board** — multi-role review  
11. **Merge** — EP approval  
12. **Lessons → Playbook** — distill durable lessons into §11 / recipes; leave raw detail in the mission doc  

Do **not** implement unapproved or design-only briefs.  
Do **not** treat Design Plan approval as Ready to Implement when a spatial player loop exists — VDP + EP mental-play approval is required (§12c).

### PRB vs Human PIE (order clarity)

- **Merge-ready** requires Human PIE Gameplay PASS (or EP written waiver) when the mission claims a player loop.  
- **PRB may run earlier** with Gameplay still `PENDING_USER` — verdict should be **Approve with conditions**, not merge authorization.  
- Technical / Slate / MCP evidence never substitutes for Human PIE.

---

# 4. Definition of Done

A mission is **Complete** and eligible for **Ready For Review = YES** only when:

| Gate | Requirement |
|------|-------------|
| Compile | PASS — no Blueprint compile errors |
| Technical | PASS — Simulate/boot and required system checks |
| Gameplay | PASS — **human** PIE with Enhanced Input (or EP written waiver) |
| Replay | PASS if replay claimed — full reverse + second run without UE restart |
| Docs | Mission notes + Changelog append; truth matches build |
| Naming / folders | DOC-002 / ASSET-001 |
| Git | Commit (and push when requested) on `develop` unless brief says otherwise |
| Mission Completion Report | Submitted with honest PASS/FAIL/N/A |
| Review | Production Review Board + EP acceptance for merge |

### Honest gates (non-negotiable)

- **Technical PASS ≠ Gameplay PASS.**  
- Slate / MCP / automated key injection **cannot** claim Gameplay PASS for Enhanced Input movement/interact.  
- Do not mark Ready For Review YES if compile, required runtime, or docs are incomplete.  
- Tag audio/mesh/geo stand-ins as **debt** — do not claim Production Ready on placeholders alone.

---

# 5. Production Standards

### Scope

- One clear player experience goal per mission.  
- Prefer one ops / puzzle family teaching beat + World Response + optional Witness.  
- Cut list locked before implement; “nice to haves” go to Notes / Roadmap.  

### Systems

- Do not redesign approved systems (power, inventory, objectives, puzzles, interaction).  
- Prefer composition and instance config over new base classes.  
- No parallel frameworks (second inventory, second power path that collapses incorrectly, etc.).  
- Mission IDs belong in docs, changelog, commits, reports, and prototype map names — **not** reusable asset names or Outliner `PE###_` prefixes.

### Maps

- Prototype: `LV_Prototype_PE###` under `Maps/Prototype/`.  
- Development sandbox: `LV_TestingGround`.  
- Production: `LV_ARI_*` under `Maps/Production/` — must not depend on prototypes.  

### Atmosphere (from PE-017A)

- Indoor emergency-dark baseline; kill outdoor Directional/Sky dominance indoors.  
- Notes = **symptoms**, not walkthroughs.  
- Witness = tension / presence only — not chase, not during solve, exit-path after power.  
- Lighting restore intentional (flicker → fluorescent / industrial).  
- Audio: real SoundWave/Cue **or** PrintString stand-ins with explicit debt tag.

### Reset / Replay

If a mission claims replay without UE restart:

- SliceReset must reverse **world + player** state that the loop mutates (door, lights, Witness, PowerManager flags, ambient once-flags, notes, objectives, pickups/respawns, generator/puzzle state as applicable).  
- Incomplete reset → do not claim Replay PASS.

---

# 6. Technical Debt Policy

Canonical triage: `Documents/02_Technical/Architecture/TechnicalDebt.md`.

| Category | Action |
|----------|--------|
| Safe to Fix | Dedicated cleanup mission when tree is clean; no drive-by in unrelated missions |
| Requires Gameplay Review | Document; change only with design approval / ADR if behavior shifts |
| Ignore | Document why; do not “fix” noise |

Rules:

- Document debt honestly in mission Notes and TechnicalDebt when new.  
- Do not expand PowerManager / core frameworks “while you’re there” without brief scope.  
- PrintString mission tags (`[PE018]`) are allowed until polish; remove before claiming polished Gameplay PASS on audio.  
- Vendor / ThirdParty mass stays out of gameplay commits unless the mission is explicitly an import mission.

---

# 7. Human Gameplay Validation

**Owner:** Executive Producer (Oscar).

Required for Gameplay PASS on production slices and any mission that claims a full player loop.

### Why human?

Enhanced Input (Move / Look / Interact / Flashlight, etc.) cannot be fully driven by Slate automation. Technical Simulate proves boot and graph wiring; humans prove feel and input.

### Minimum checklist pattern

1. Spawn / flashlight / lighting baseline  
2. Objective chain readable  
3. Notes symptoms-only; empty ObjectiveOnRead does not clobber  
4. Collect → solve / start → World Response  
5. Exit unlock + Witness (if in scope) on exit path post-power  
6. SliceReset → full reverse → second run  

Mission-specific checklists live in the mission doc (see PE-017 / PE-018).

EP may issue a **written waiver** to proceed with a dependent mission; waiver does not convert Technical into Gameplay PASS.

---

# 8. Production Review Board

Before merge (and for design-plan approval on larger missions), review across roles **without overlapping duties**:

| Role | Asks |
|------|------|
| Executive Producer | Best next ≠ biggest; schedule; Ready / merge |
| Creative Director | Tone, pillar balance, identity |
| Lead Developer | Architecture reuse, debt, compile/technical honesty |
| Gameplay Designer | Loop, family teaching, bible anti-patterns |
| Level Designer | Flow, room count, spatial teaching |
| Technical Artist | Lighting, dressing vs geo sink, ThirdParty policy |
| Horror Director | Tension curve, Witness fairness |
| Narrative Director | Symptoms vs exposition; Story/Facility/Room alignment |
| Audio Director | Real cues vs debt tags; restore suite honesty |
| QA Lead | Gate honesty, checklist completeness, regression |

Skill: `.cursor/skills/production-review-board/SKILL.md`  
Agent briefs: `.cursor/agents/`.

---

# 9. Domain Standards (summary)

### Architecture

- Blueprint-first; components + interfaces + dispatchers.  
- Event-driven; avoid tight coupling and duplicate `_0` rename debris.  
- Sandbox regression on `LV_TestingGround` when touching shared systems.  
- Generator World Response **independent** of puzzle `NotifyPuzzlePowerResponse` (do not collapse once-only flags across maps incorrectly).

### Gameplay

- Align with Gameplay Design Bible (PE-016).  
- Loop: Explore → Observe → Collect → Solve → World Response → Survive (presence) → Proceed.  
- No combat / chase AI unless ADR explicitly approves.  
- Witness pressures attention; never replaces solvable logic.

### Storytelling

- Environmental discovery over exposition dumps.  
- Notes and props = residue of work and failure.  
- No walkthrough notes (“go north then pick up X”).

### Horror

- Psychological; uncertainty over constant pursuit.  
- Tension curve example: Unease → Focus → Relief → Spike (Witness) → Release.  
- Presence beats delayed; mesh hidden until post-power when using silhouette pattern.

### Documentation

- Append-only Changelog — never rewrite history.  
- Separate Canon from Recommendations.  
- Docs reflect approved decisions and inspected/implemented truth only.  
- Mission Completion Report required for gameplay missions.

Full naming / folders: Contribution Guide (DOC-002 / ASSET-001). Cursor enforcement: `.cursor/rules/`.

---

# 10. Reference Implementations

## PE-018 — Default production map recipe

**Use PE-018 / `LV_ARI_GeneratorAnnex` as the default template** when building a new production slice map.

Recipe:

| Element | Pattern |
|---------|---------|
| Map path | `/Game/ProjectEcho/Maps/Production/LV_ARI_*` |
| Rooms | ≤5; hub corridor + observation + resource + ops room + exit |
| Loop | Explore → Observe → Collect resource → Start/solve system → World Response → Witness on exit → Proceed |
| Notes | Symptoms-only; ObjectiveOnRead skip-if-empty |
| Power receivers | EmergencyLight, PoweredDoor, ambient/PA/vent, Witness via `BPI_PowerReceiver` |
| Horror | `BP_WitnessSilhouetteHint` on exit path after power; tension only |
| Lighting | Indoor emergency-dark; no outdoor sun dominance; restore flicker pattern |
| Reset | Dedicated `BP_*Reset` twin — **full** world + player reverse + pickup respawn |
| Scope | One ops teaching beat; cut Coolant/Security/extra puzzles unless briefed |
| Gates | Compile → Technical Simulate → Human PIE → Replay → Docs |
| Independence | Do not merge generator and puzzle power once-flags incorrectly |

Design plan reference: `Documents/05_Missions/PE-018-DesignPlan.md`  
Mission notes: `Documents/05_Missions/PE-018-GeneratorAnnex.md`

## PE-017 / PE-017A — Fuse path ownership

**PE-017A owns the Maintenance Wing fuse path** and the experience-hardening lessons for that slice.

| Element | Ownership |
|---------|-----------|
| Map | `LV_ARI_MaintenanceWing` |
| Ops problem | Fuse → aux electrical restore (`BP_FusePuzzle` / PE-015) |
| Hardening | Exit-path Witness, full SliceReset, symptoms Note A, indoor lighting, dressing, skip-if-empty objectives |
| Teaching | Aux power literacy (fuse) vs PE-018 main plant literacy (fuel/generator) |

Do **not** duplicate the Maintenance fuse path into new maps as a second PE-015 fork. New maps follow the **PE-018 map recipe**; fuse-specific truth and reset patterns for Maintenance remain PE-017A’s domain.

Mission notes: `Documents/05_Missions/PE-017-VerticalSlice01.md`

---

# 11. Lessons Learned

### PE-017

- Production slice ≠ feature demo — 5–10 minute investigation beat.  
- Compass-aligned rooms teach spatial memory with clues.  
- Observation before inventory (Breaker before Storage).  
- Power restore then Witness on the way out = double-edged restore.

### PE-017A

- Quality over quantity; harden before expanding.  
- Incomplete SliceReset invalidates replay claims — reverse **everything** the loop touches.  
- Outdoor lighting dominance kills horror indoor baseline.  
- Walkthrough notes break discovery; symptoms-only is law.  
- Empty ObjectiveOnRead must not SetObjective.  
- Dressing from existing packs beats waiting on full modular geo.  
- Manual Gameplay PASS remains human-gated — document PENDING_USER honestly.

### PE-018

- Design plan **before** implement; cut list locked (Fuel + Generator only).  
- Best next ≠ biggest — one map, one ops problem.  
- Reuse Generator/Fuel path; no new puzzle BP.  
- Generator World Response stays independent of Maintenance fuse power path.  
- Mirror PE-017A SliceReset completeness for FuelCan + Generator state.  
- Soft travel / Pipe Gallery / Coolant / Security deferred without shame when cut list says so.  
- Building on unvalidated foundation requires EP waiver or prior human PIE.

---

# 12. Cursor AI Studio Map

| Layer | Location |
|-------|----------|
| This playbook | `Documents/04_Production/ProductionPlaybook.md` |
| AI Studio overview | `Documents/04_Production/AIStudio/README.md` |
| Mission Director | `Documents/04_Production/AIStudio/MissionDirector/` |
| Creative Studio | `Documents/04_Production/AIStudio/CreativeStudio/` |
| Previsualization Studio | `Documents/04_Production/AIStudio/PrevisualizationStudio/` |
| Rules | `.cursor/rules/*.mdc` |
| Skills | `.cursor/skills/*/SKILL.md` (flat folders) |
| Agent role briefs | `.cursor/agents/*.md` |
| Hooks policy | `Documents/04_Production/AIStudio/Hooks.md` |
| Legacy role doc | `Documents/00_Governance/AIStudio.md` (still valid; playbook wins on process detail) |

---

# 12b. Creative Studio (AI Studio v1.2)

Creative Studio improves environment / asset production quality while minimizing unnecessary work.

### Principles (priority)

1. Reuse existing Project Echo assets  
2. Fab  
3. Quixel  
4. Meshy AI  
5. Blender modify existing  
6. Custom only when required  

Full pipeline: `Documents/04_Production/AIStudio/CreativeStudio/AssetCreationPipeline.md`.

### Skills

Production skills (plan / implement / PRB / docs / playtest) plus Creative skills listed in `CreativeStudio/README.md` and `.cursor/skills/*`.

Creative skills produce **plans and specifications**. They do **not** modify Story Canon, Blueprints, or maps unless a separate approved implementation mission includes that work.

### Integration

Creative outputs must remain consistent with Gameplay Design Bible, Story Bible (read-only), Facility Bible, and Room Bible.

---

# 12c. Previsualization Studio (AI Studio v1.3)

Previs Studio translates design into visual communication so the mission is **mentally playable** before Unreal.

### Permanent rule

**No production mission may enter implementation until a complete Visual Design Package is EP-approved.**

Spec: `Documents/04_Production/AIStudio/PrevisualizationStudio/VisualDesignPackage.md`.

### Pipeline

Mission Planner → Environment Designer → Experience Designer → Blockout Visualizer → Storyboard Designer → Concept Artist → (+ Lighting Visualizer, Asset Placement Designer) → VDP → **EP Approval** → Mission Implementer → Human PIE → PRB.

### Skills

`experience-designer`, `blockout-visualizer`, `storyboard-designer`, `concept-artist`, `lighting-visualizer`, `asset-placement-designer`.

Previs **visualizes** gameplay; it does not invent mechanics or implement UE5. Concept outputs are **prompts** unless a later art mission generates images.

### EP mental-play gate

EP must answer Yes to understanding, mental walkthrough, objectives, puzzles, pacing, horror imagination, confusion spotting, and would-enjoy — any No returns to Design.

---

# 12d. Mission Director (AI Studio v1.4)

Mission Director is the **permanent single entry point** for production missions. It is an orchestration layer, not a creative skill.

### EP commands (permanent)

`Start Mission` · `Continue Mission` · `Generate Visual Package` · `Implement Mission` · `Validate Mission` · `Review Mission` · `Close Mission` — each with `PE-###`.

### Behavior

- Selects Skills, order, dependencies, gates, and deliverables automatically  
- Stops at mandatory approval gates  
- EP does **not** manually coordinate Skills  
- Enforces no skipped phases, Story Canon, Playbook, VDP-before-implement  

Authority: `Documents/04_Production/AIStudio/MissionDirector/` · `.cursor/skills/mission-director/SKILL.md` · `.cursor/rules/mission-director.mdc`

---

## Document Control

| | |
|--|--|
| Created | 2026-07-25 |
| Version | 1.4 (Mission Director) |
| Owners | EP + AI Studio |
| Related | PE-017, PE-017A, PE-018, FRAMEWORK-001, Creative Studio, Previsualization Studio, Mission Director, ContributionGuide, GameplayDesignBible, TechnicalDebt |

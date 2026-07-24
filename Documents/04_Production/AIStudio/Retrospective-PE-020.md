# Production Retrospective — PE-020 Research Wing

**Type:** Recommendations only — **do not implement** from this document  
**Date:** 2026-07-25  
**Branch:** `develop`  
**Mission:** PE-020 Research Wing (`LV_ARI_ResearchWing`)  
**AI Studio baseline:** v1.4 (Production + Creative + Previs + Mission Director); FRAMEWORK-001 validated as v1.1 foundation  
**Scope of this doc:** Process / AI Studio performance. No Unreal, rules, skills, or Playbook edits authorized by this retrospective.

---

## Session lifecycle (observed)

| Phase | What happened | Commit / evidence |
|-------|---------------|-------------------|
| Start / Design Plan | Plan drafted; initially incomplete when Implement first requested | Design Plan on disk later; status now APPROVED & IMPLEMENTED |
| Implement requested early | EP said Implement before Design Plan fully on disk → treated as Design Plan approval | Verbal / command gate |
| MCP Auto-review | Asset creation blocked as “unapproved” until EP said auto-accept | Session friction (not a Playbook gate) |
| Implement | Technical PASS — **VDP not done before Implement** (out of order vs Mission Director / Playbook §12c) | `41c8e3c` |
| Generate Visual Package | Ran **after** Implement — post-hoc VDP for mental-play / retrofit | `739306d` → `PE-020-VisualDesignPackage.md` |
| Validate | Technical re-check PASS + playtest checklist; Gameplay **PENDING_USER** | `c1e7ee1` |

**Honesty:** Product outcome (Technical slice) landed. Process outcome violated permanent VDP-before-implement rule. EP Implement was used as a waiver of Design Plan completeness *and* (implicitly) of VDP — only the former is a documented informal mapping; the latter is a gate failure.

---

## Overall process grade

**Grade: B− (process) / B+ (delivery)**

- **Delivery:** Reused PE-018 / PE-019 patterns, Research Equipment teaching beat, Soft Open Coolant→Research, honest Technical ≠ Gameplay, solid mission notes + checklist.  
- **Process:** Mission Director anti-pattern (Implement without VDP APPROVE) executed; Previs became documentation after the fact; Creative Studio under-used as a pre-build design pass; Auto-review added friction without a clear EP policy.

**Ready For Review (this retrospective):** **YES** — docs-only recommendations.  
**Ready For Review (PE-020 mission):** **NO** until Human Gameplay PASS (or EP written waiver) — unchanged.

---

## 1. Mission Director

### Went well

- Single command vocabulary (`Start` → `Implement` → `Generate Visual Package` → `Validate`) was usable in a live mission.  
- Validate path correctly separated Technical evidence from Gameplay PENDING_USER and produced a human PIE checklist.  
- Response shape (phase / prerequisites / gate / next command) is the right EP UX.  
- Soft mapping of informal “build it” → Implement Mission is documented and was used.

### Went poorly

- **Permanent rule #1–2 violated:** Implement proceeded without VDP complete + EP APPROVE on a spatial production slice.  
- When Design Plan was incomplete on disk, Director accepted Implement as approval instead of stopping with an Approval Block listing missing artifacts (Plan file + VDP).  
- **Continue Mission** was not used to advance Plan → Creative → Previs → gate; the session jumped phases via direct Implement.  
- Post-hoc `Generate Visual Package` after Implement is not a defined recovery path in CommandReference (only ideal order is specified).

### Gate failures attributable here

| Failure | Severity |
|---------|----------|
| VDP after Implement | **Critical** (Playbook §12c / Director rule 2) |
| Incomplete Design Plan at first Implement | **High** (mitigated by EP verbal Implement = approval) |
| No written VDP waiver | **High** (Implement treated as silent waiver) |

---

## 2. Production Studio

### Went well

- `mission-implementer` reused CoolantLoop/Valve / Soft Open / Witness / SliceReset — low maintenance, on-brief.  
- Compile + MCP technical re-check evidence recorded honestly in mission notes.  
- `playtest-generator` output is actionable and separates “Technical already proved” from EI steps.  
- Debt tagged (Coolant twin PrintStrings, BeginPlay objective text, audio/geo stand-ins) — not falsely Production Ready.

### Went poorly

- Implement skill ran under an invalid Ready-to-Implement state (VDP missing). Skill cannot self-heal orchestration failures without Director hard-stop.  
- Twin BPs prepared but map still on Coolant twins → cutover debt; Production Studio absorbed Creative naming without a pre-implement asset plan.  
- Replay claimed Technical PASS / PENDING_USER manual — correct honesty, but SliceReset still CoolantBayReset instance (naming confusion for EP QA).

---

## 3. Creative Studio

### Went well

- Design Plan itself carried strong Creative-adjacent content (rooms, Research Equipment family, cut list, env-story-first intent).  
- Bible §5.4 Research Equipment teaching beat stayed coherent without framework fork.  
- SkillRelationships boundaries (Creative specifies → Previs communicates → Production implements) are clear on paper.

### Went poorly

- Dedicated Creative skills (`environment-designer`, `facility-designer`, `prop-designer`, `lighting-designer`, `environmental-storytelling-designer`, asset planner/coordinator) were largely **bypassed** as discrete Director-invoked passes before Implement.  
- Asset path (planner → coordinator → mesh) did not run as a gate; MCP Auto-review then blocked creation mid-implement — process and tooling fought each other.  
- Clinical / lab dress vs Engineering wetness was designed in prose, not in a Creative deliverable EP could approve separately from the Design Plan.

---

## 4. Previsualization Studio

### Went well

- When run, VDP package is complete against `VisualDesignPackage.md` sections (overview, journey, blockout, storyboard, concepts, lighting sequence, placement, rhythm).  
- Honesty banner correctly states implementation already landed and Ready to Implement = N/A.  
- Mental-play checklist remains the right EP evaluation tool — even post-hoc.

### Went poorly

- Previs **failed its primary job** this mission: prevent build-before-visualize.  
- Post-hoc VDP risks rubber-stamping the built map instead of shaping it (retrofit quality review ≠ design gate).  
- Six-skill Generate Visual Package chain is heavy; after Implement, EP may treat VDP as optional docs — undermining the permanent rule for PE-021+.

---

## 5. Documentation quality

### Went well

- Mission notes, Design Plan, VDP, Playtest Checklist, Changelog appends are cross-linked and status-honest.  
- Technical re-check table is evidence-grade (labels, Soft Open props, MapCheck).  
- Deferred debt list is specific and actionable.

### Went poorly

- Design Plan status line “Ready to Implement: YES” after Implement conflates EP Implement command with VDP-backed Ready to Implement (Playbook distinction blurred).  
- VDP awaiting EP mental-play APPROVE while map already shipped Technical — two different “approve” meanings in one mission.  
- No durable “lessons → Playbook §11” capture yet (FRAMEWORK-001 already flagged this); this retrospective is the interim.

---

## 6. Workflow bottlenecks

1. **Gate ambiguity under speed pressure** — EP Implement overrides incomplete Plan; no forced pause for VDP.  
2. **MCP Auto-review vs production missions** — “unapproved asset” blocks until auto-accept; not documented in AI Studio EP contract.  
3. **Full Previs skill chain latency** — six skills before Implement encourages skipping under time pressure.  
4. **Human Gameplay PENDING** — unavoidable (EI); Validate correctly stops, but mission stays open until EP time.  
5. **Creative → Previs handoff optional in practice** — Continue Mission did not force Creative layout before Previs.

---

## 7. Approval gates

| Gate | Spec | PE-020 result |
|------|------|---------------|
| Design Plan proceed | Stop until EP | **PASS (late)** — EP Implement treated as approval |
| VDP EP APPROVE → Ready to Implement | Mandatory for spatial slices | **FAIL** — Implement first; VDP post-hoc |
| Written VDP waiver | Allowed only in writing | **FAIL** — no written waiver |
| Technical Validate | Compile / runtime evidence | **PASS** |
| Human Gameplay | Enhanced Input PIE | **PENDING_USER** (honest) |
| Ready for Review / merge | After Gameplay or waiver | **NO** (correct) |
| MCP Auto-review | Tooling, not Playbook | **Friction** — blocked until EP auto-accept |

**Root cause pattern:** Soft EP commands (`Implement`) were stronger than hard documentation gates. Director needs an explicit **hard-stop vs EP override** protocol (written override string, not silent proceed).

---

## 8. Skill overlap

| Overlap | Risk seen on PE-020 | Recommendation direction |
|---------|---------------------|---------------------------|
| Design Plan vs VDP Mission Overview / Journey | Plan already “felt like” enough to Implement | Keep Plan thinner on experience visuals; VDP owns mental-play artifacts |
| `environment-designer` vs `blockout-visualizer` | Neither run pre-build; Plan rooms substituted | Director must invoke Environment before Previs on spatial slices |
| `lighting-designer` vs `lighting-visualizer` | Neither pre-build | Same |
| `prop-designer` vs `asset-placement-designer` | Placement only in post-hoc VDP | Same |
| Coolant twins vs Research twin BPs | Naming / PrintString debt | Asset coordinator should flag “reuse with identity debt” before Implement |

Overlap **on paper** is healthy; overlap **failure mode** was skipping both Creative and Previs owners and letting Plan + Implement absorb everything.

---

## 9. Missing capabilities

1. **EP Override protocol** — documented phrase + logged waiver fields (Design Plan only / VDP / both) with severity.  
2. **Post-hoc VDP recovery path** — CommandReference step: mark gate FAIL, produce VDP as retrofit review, require EP APPROVE for *experience quality*, not Ready to Implement.  
3. **Light VDP / Fast Previs** — subset for PE-018-recipe twin slices (experience + blockout + storyboard only) to reduce skip temptation.  
4. **MCP Auto-review policy** — when production Implement is EP-commanded, allowlisted creation paths or EP “auto accept for this mission” sticky note.  
5. **Director hard-stop checklist artifact** — machine-readable or mission-doc table: Plan on disk / VDP complete / VDP APPROVE / Ready to Implement — FAIL stops Implement.  
6. **Lessons → Playbook** — explicit Close Mission or retro step (this file is the PE-020 instance).  
7. **Live command examples** — AI Studio README Phase 4+ already planned; PE-020 is the first live anti-example + success Validate example.

---

## Per-studio summary table

| Studio | Grade | One-line |
|--------|-------|----------|
| Mission Director | **C+** | Commands worked; VDP gate not enforced under Implement pressure |
| Production Studio | **B+** | Strong Technical delivery + honest Validate; ran under invalid Ready state |
| Creative Studio | **C** | Intent lived in Design Plan; discrete Creative skills under-invoked |
| Previsualization Studio | **C** | Excellent post-hoc package; failed primary pre-implement purpose |
| Documentation | **A−** | Truthful, linked, debt-tagged; Ready-to-Implement wording drifted |

---

## Recommendations for AI Studio v1.5

**Constraint reminder:** Recommendations only. Do **not** implement rules/skills/docs/Unreal from this list until a separate FRAMEWORK / docs mission is commanded.

### Quick Wins (docs / Director contract — low risk)

1. **Hard-stop Implement checklist** — In Mission Director SKILL + CommandReference: refuse Unreal work unless Design Plan file exists **and** (VDP EP APPROVE **or** written waiver block in mission doc). Print the three fields every Implement attempt.  
2. **EP Override template** — Single markdown block: `OVERRIDE: VDP | Plan | Both` + reason + date; Implement may proceed only if block present when gates fail.  
3. **Post-hoc VDP recovery** — Document Generate Visual Package after Implement as **retrofit review**; Ready to Implement = N/A; require EP mental-play APPROVE/RETURN for experience quality.  
4. **MCP Auto-review EP note** — One paragraph in AIStudio README / MissionDirector: production Implement may need EP “auto accept” for asset creation; not a substitute for Playbook gates.  
5. **PE-020 lesson → Playbook §11** (when authorized) — Distill: never Implement spatial slices without VDP or written waiver; post-hoc VDP is debt, not compliance.

### Medium (v1.5 feature work)

6. **Light VDP tier** — For PE-018-recipe continuations: Experience + Blockout + Storyboard mandatory; Concept / Lighting Visualizer / Placement optional unless EP requests Full VDP. Reduces skip pressure.  
7. **Continue Mission enforcement examples** — Add PE-020 as worked example: wrong path (Implement early) vs correct path (Continue → Creative → Generate Visual Package → APPROVE → Implement → Validate).  
8. **Creative minimum for spatial slices** — Director auto-runs at least `environment-designer` (and thin env-story) before Previs; do not accept Design Plan rooms alone as Creative complete.  
9. **Light vs Full PRB** — FRAMEWORK-001 carryover: PE-020-sized slice uses Light PRB after Gameplay PASS.  
10. **Asset identity debt flag** — Coordinator / implementer checklist: “reused BP with wrong mission PrintString / objective text” → explicit debt row before Technical PASS claims cleanliness.

### Long-term

11. **Optional `mission-retro` skill** — Only if lessons keep failing to reach Playbook (FRAMEWORK-001 already deferred this).  
12. **Selective hooks** — Still Wait/Never default; consider only a soft reminder hook on Implement if VDP path missing (high noise risk — prove need on PE-021–023 first).  
13. **Director prerequisite machine check** — Future: script or MCP probe for mission-doc gate fields before `mission-implementer` (never claim Gameplay).  
14. **Previs image generation mission path** — Concept prompts exist; optional art mission remains separate (do not bloat Generate Visual Package).

---

## Top 5 v1.5 priorities (executive)

1. **Hard-stop Implement without VDP APPROVE or written override** (Quick Win #1–2)  
2. **Document post-hoc VDP recovery + override template** (Quick Win #2–3)  
3. **Light VDP tier for recipe twin slices** (Medium #6)  
4. **MCP Auto-review / auto-accept policy for commanded Implement** (Quick Win #4)  
5. **Continue Mission worked examples + Creative minimum before Previs** (Medium #7–8)

---

## What not to do

- Do not weaken VDP permanent rule to match PE-020’s out-of-order success.  
- Do not claim Gameplay PASS from Technical Validate.  
- Do not implement rule/skill changes from this retrospective without an EP-commanded framework/docs mission.  
- Do not treat post-hoc VDP APPROVE as rewriting history to “VDP-before-Implement PASS.”

---

## Related artifacts

| Artifact | Path |
|----------|------|
| Mission notes | `Documents/05_Missions/PE-020-ResearchWing.md` |
| Design Plan | `Documents/05_Missions/PE-020-DesignPlan.md` |
| VDP (post-hoc) | `Documents/05_Missions/PE-020-VisualDesignPackage.md` |
| Playtest checklist | `Documents/05_Missions/PE-020-PlaytestChecklist.md` |
| Mission Director skill | `.cursor/skills/mission-director/SKILL.md` |
| Command reference | `Documents/04_Production/AIStudio/MissionDirector/CommandReference.md` |
| VDP standard | `Documents/04_Production/AIStudio/PrevisualizationStudio/VisualDesignPackage.md` |
| FRAMEWORK-001 | `Documents/04_Production/AIStudio/ValidationReport-FRAMEWORK-001.md` |
| Playbook | `Documents/04_Production/ProductionPlaybook.md` (§3, §12c, §12d) |

---

## Retrospective status

| Field | Value |
|-------|--------|
| Recommendations only | **YES** |
| Implementation authorized | **NO** |
| Ready For Review (this doc) | **YES** |
| PE-020 Ready For Review | **NO** (Gameplay PENDING_USER) |

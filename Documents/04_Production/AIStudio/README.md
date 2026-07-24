# Project Echo — AI Studio

**Status:** Active — AI Studio **v1.2** (Phase 1 baseline + FRAMEWORK-001 + Creative Studio Phase 2)  
**Date:** 2026-07-25  
**Validation:** [ValidationReport-FRAMEWORK-001.md](ValidationReport-FRAMEWORK-001.md)  
**Creative Studio:** [CreativeStudio/README.md](CreativeStudio/README.md)  

---

## Purpose

AI Studio is the development-workflow layer that helps Oscar, ChatGPT, and Cursor operate like a small professional game studio — without redesigning Project Echo’s game vision.

- **Phase 1 / v1.1:** Production Playbook + rules + production skills + PRB agents + hooks policy  
- **Phase 2 / v1.2:** Creative Studio — environment/asset production skills + pipeline docs (still **no** Unreal gameplay asset changes in the framework mission itself)

---

## Architecture Overview

```text
Documents (authority)
  ProductionPlaybook.md     ← process source of truth
  00_Governance/*           ← bibles adjacent, ADRs, contribution
  01–05_*                   ← design / tech / world / production / missions
  AIStudio/CreativeStudio/  ← Creative Studio overview + pipeline

.cursor/ (agent operating system)
  rules/*.mdc               ← always-on + scoped enforcement
  skills/*/SKILL.md         ← flat skill folders (Production + Creative)
  agents/*.md               ← Task-tool role briefs (non-overlapping)
  hooks/                    ← optional; remain DISABLED (see Hooks.md)
  mcp.json                  ← Unreal MCP (leave alone unless required)
```

### Authority order (unchanged vision)

1. Story Bible  
2. Gameplay Design Bible  
3. Production Playbook (+ ContributionGuide naming)  
4. ADRs  
5. Mission Brief  

---

## Recommended `.cursor` Tree

```text
.cursor/
  mcp.json
  rules/
    foundation.mdc
    production-standard.mdc
    blueprint-standards.mdc
    gameplay-standards.mdc
    story-canon.mdc
    documentation-standard.mdc
    folder-structure.mdc
    creative-studio.mdc            # Asset Creation Hierarchy (scoped)
  skills/                          # FLAT — reliable Cursor discovery
    # Production Studio
    mission-planner/
    mission-implementer/
    production-review-board/
    documentation-sync/
    playtest-generator/
    # Creative Studio
    asset-creation-planner/
    ai-asset-coordinator/
    mesh-designer/
    environment-designer/
    facility-designer/
    prop-designer/
    lighting-designer/
    audio-designer/
    environmental-storytelling-designer/
    cinematic-designer/
    performance-designer/
  agents/
    executive-producer.md
    creative-director.md
    lead-developer.md
    gameplay-designer.md
    level-designer.md
    technical-artist.md
    horror-director.md
    narrative-director.md
    audio-director.md
    qa-lead.md
  hooks/                           # deferred — see Hooks.md
```

**Do not nest** skills under `skills/creative/` or `skills/production/` unless Cursor documents stable multi-level discovery. Domain grouping lives in [CreativeStudio/README.md](CreativeStudio/README.md).

---

## Skills Map

### Production Studio

| Skill | Use when |
|-------|----------|
| `mission-planner` | Design plan first; wait for approval |
| `mission-implementer` | Approved brief → UE5 implement + report |
| `production-review-board` | Cross-role review before approve/merge |
| `documentation-sync` | Align docs / Changelog / indexes |
| `playtest-generator` | Manual PIE checklist for EP |

### Creative Studio

| Skill | Use when |
|-------|----------|
| `asset-creation-planner` | Mission → full asset list / priority / roadmap |
| `ai-asset-coordinator` | Hierarchy, tracker, queue, source recommendations |
| `mesh-designer` | Create-path mesh specs + Meshy/import checklists |
| `environment-designer` | Layout, flow, horror pacing, landmarks |
| `facility-designer` | Industrial realism, equipment, pipes |
| `prop-designer` | Dressing, reuse, missing props |
| `lighting-designer` | Light plan / progression / color temp |
| `audio-designer` | Cues, ambient layers, triggers, silence |
| `environmental-storytelling-designer` | Visual story before notes |
| `cinematic-designer` | Reveals, framing, highlights |
| `performance-designer` | Nanite/LOD/streaming/light-cost risk |

Relationships: [CreativeStudio/SkillRelationships.md](CreativeStudio/SkillRelationships.md)  
Pipeline: [CreativeStudio/AssetCreationPipeline.md](CreativeStudio/AssetCreationPipeline.md)

---

## Subagents

Role briefs in `.cursor/agents/` are prompt specs for Cursor’s Task tool. They are **not** a native Cursor “agents runtime.” Skills/rules reference them for Production Review Board and specialist reviews.

Duties are intentionally non-overlapping — see each brief’s Boundaries section.

---

## Reference Decisions

| Decision | Rule |
|----------|------|
| Default production map recipe | **PE-018** (`LV_ARI_GeneratorAnnex` pattern) |
| Fuse path ownership | **PE-017A** (`LV_ARI_MaintenanceWing`) |
| Gameplay PASS | Human PIE (Enhanced Input) — Technical ≠ Gameplay |
| Asset acquisition | Reuse → Fab → Quixel → Meshy → Blender → Custom |
| Skill folder layout | **Flat** under `.cursor/skills/` |

---

## Related Docs

- [Production Playbook](../ProductionPlaybook.md)  
- [Creative Studio](CreativeStudio/README.md)  
- [Validation Report (FRAMEWORK-001)](ValidationReport-FRAMEWORK-001.md)  
- [Migration Plan](MigrationPlan.md)  
- [Hooks Policy](Hooks.md)  
- [Phase 1 Completion Report](Phase1-CompletionReport.md)  
- [Phase 2 Completion Report](CreativeStudio/Phase2-CompletionReport.md)  
- Legacy [AIStudio.md](../../00_Governance/AIStudio.md)  

---

## Phase Status

| Phase | Focus | Status |
|-------|-------|--------|
| 1 | Playbook + Rules + Skills + Agents + Hooks policy | **Complete** (v1.0 baseline) |
| 1.1 | FRAMEWORK-001 validation + minor lifecycle clarifications | **Complete** (v1.1) |
| 2 | Creative Studio skills + asset pipeline docs | **Complete** (v1.2 — this delivery) |
| 2+ | Optional light hooks; Light vs Full PRB; live-mission examples | Planned (hooks still off) |
| 3 | Deeper automation only if high-value and low noise | Deferred |

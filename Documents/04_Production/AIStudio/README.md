# Project Echo — AI Studio

**Status:** Active — AI Studio **v1.4** (Production + Creative + Previs + **Mission Director**)  
**Date:** 2026-07-25  
**Validation:** [ValidationReport-FRAMEWORK-001.md](ValidationReport-FRAMEWORK-001.md)  
**Mission Director:** [MissionDirector/README.md](MissionDirector/README.md) · [CommandReference.md](MissionDirector/CommandReference.md) · [MCP Auto-accept Policy](MissionDirector/MCP-AutoAccept-Policy.md)  
**Creative Studio:** [CreativeStudio/README.md](CreativeStudio/README.md)  
**Previsualization Studio:** [PrevisualizationStudio/README.md](PrevisualizationStudio/README.md)  

---

## Purpose

AI Studio is the development-workflow layer that helps Oscar, ChatGPT, and Cursor operate like a small professional game studio — without redesigning Project Echo’s game vision.

- **Phase 1 / v1.1:** Production Playbook + rules + production skills + PRB agents + hooks policy  
- **Phase 2 / v1.2:** Creative Studio — environment/asset production skills + pipeline docs  
- **Phase 3 / v1.3:** Previsualization Studio — Visual Design Package + mental-play EP gate  
- **Phase 4 / v1.4:** **Mission Director** — single EP command entry; automatic skill orchestration  

**Default:** Every production conversation assumes Mission Director is active. EP issues high-level commands only.

Framework architecture missions remain **docs + Cursor OS only** unless a gameplay mission is explicitly commanded through Director → Implement.

---

## Architecture Overview

```text
Documents (authority)
  ProductionPlaybook.md     ← process source of truth
  AIStudio/MissionDirector/ ← EP commands + orchestration contract
  AIStudio/CreativeStudio/
  AIStudio/PrevisualizationStudio/

.cursor/ (agent operating system)
  rules/*.mdc               ← includes always-on mission-director.mdc
  skills/mission-director/  ← single production entry skill
  skills/*/SKILL.md         ← Production + Creative + Previs (invoked by Director)
  agents/*.md               ← PRB + mission-director brief
  hooks/                    ← DISABLED (see Hooks.md)
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
    mission-director.mdc           # always — EP commands; auto skill orchestration
    production-standard.mdc
    blueprint-standards.mdc
    gameplay-standards.mdc
    story-canon.mdc
    documentation-standard.mdc
    folder-structure.mdc
    creative-studio.mdc
    previs-studio.mdc
  skills/
    mission-director/              # ENTRY — orchestration
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
    # Previsualization Studio
    experience-designer/
    blockout-visualizer/
    storyboard-designer/
    concept-artist/
    lighting-visualizer/
    asset-placement-designer/
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
    mission-director.md            # orchestration Task brief
  hooks/                           # deferred — see Hooks.md
```

**Do not nest** skills under domain package folders unless Cursor documents stable multi-level discovery. Domains: [MissionDirector](MissionDirector/README.md), [CreativeStudio](CreativeStudio/README.md), [PrevisualizationStudio](PrevisualizationStudio/README.md).

---

## EP Commands (default)

See [MissionDirector/CommandReference.md](MissionDirector/CommandReference.md).

```text
Start Mission PE-###
Continue Mission PE-###
Generate Visual Package PE-###
Implement Mission PE-###
Validate Mission PE-###
Review Mission PE-###
Close Mission PE-###
```

---

## Skills Map

### Orchestration

| Skill | Use when |
|-------|----------|
| `mission-director` | **Default** — any production command; selects other skills |

### Production Studio

| Skill | Use when (via Director) |
|-------|----------|
| `mission-planner` | Start Mission / plan phase |
| `mission-implementer` | Implement Mission after VDP APPROVE |
| `production-review-board` | Review Mission |
| `documentation-sync` | Close Mission / docs align |
| `playtest-generator` | Validate Mission (human PIE checklist) |

### Creative Studio

| Skill | Use when (via Director / Continue) |
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

### Previsualization Studio

| Skill | Use when (via Generate Visual Package) |
|-------|----------|
| `experience-designer` | Player journey, rhythm, emotional curve for VDP |
| `blockout-visualizer` | Top-down floor plan / flow / landmarks for EP |
| `storyboard-designer` | Playable scene sequence + timeline |
| `concept-artist` | Concept **prompts** + mood/color/material palettes |
| `lighting-visualizer` | Lighting mood board + power/Witness sequence |
| `asset-placement-designer` | Placement preview + readability review |

Spec: [PrevisualizationStudio/VisualDesignPackage.md](PrevisualizationStudio/VisualDesignPackage.md)  
Relationships: [PrevisualizationStudio/SkillRelationships.md](PrevisualizationStudio/SkillRelationships.md)

---

## Subagents

Role briefs in `.cursor/agents/` are prompt specs for Cursor’s Task tool. They are **not** a native Cursor “agents runtime.” Skills/rules reference them for Production Review Board and specialist reviews. Includes `mission-director.md` orchestration brief.

Duties are intentionally non-overlapping — see each brief’s Boundaries section.

---

## Reference Decisions

| Decision | Rule |
|----------|------|
| Default production entry | **Mission Director** (EP high-level commands) |
| Default production map recipe | **PE-018** (`LV_ARI_GeneratorAnnex` pattern) |
| Fuse path ownership | **PE-017A** (`LV_ARI_MaintenanceWing`) |
| Gameplay PASS | Human PIE (Enhanced Input) — Technical ≠ Gameplay |
| Asset acquisition | Reuse → Fab → Quixel → Meshy → Blender → Custom |
| Skill folder layout | **Flat** under `.cursor/skills/` |
| Ready to Implement | Requires **EP-approved Visual Design Package** for production slices |
| MCP Auto-accept | EP `Implement Mission` / sticky `auto accept` authorizes MCP creates — not a VDP waiver; see [MCP-AutoAccept-Policy.md](MissionDirector/MCP-AutoAccept-Policy.md) |

---

## Related Docs

- [Production Playbook](../ProductionPlaybook.md)  
- [Mission Director](MissionDirector/README.md)  
- [MCP Auto-accept Policy](MissionDirector/MCP-AutoAccept-Policy.md)  
- [Creative Studio](CreativeStudio/README.md)  
- [Previsualization Studio](PrevisualizationStudio/README.md)  
- [Validation Report (FRAMEWORK-001)](ValidationReport-FRAMEWORK-001.md)  
- [Migration Plan](MigrationPlan.md)  
- [Hooks Policy](Hooks.md)  
- [Phase 1 Completion Report](Phase1-CompletionReport.md)  
- [Phase 2 Completion Report](CreativeStudio/Phase2-CompletionReport.md)  
- [Phase 3 Completion Report](PrevisualizationStudio/Phase3-CompletionReport.md)  
- [Mission Director Integration Report](MissionDirector/Integration-CompletionReport.md)  
- Legacy [AIStudio.md](../../00_Governance/AIStudio.md)  

---

## Phase Status

| Phase | Focus | Status |
|-------|-------|--------|
| 1 | Playbook + Rules + Skills + Agents + Hooks policy | **Complete** (v1.0 baseline) |
| 1.1 | FRAMEWORK-001 validation + minor lifecycle clarifications | **Complete** (v1.1) |
| 2 | Creative Studio skills + asset pipeline docs | **Complete** (v1.2) |
| 3 | Previsualization Studio + Visual Design Package gate | **Complete** (v1.3) |
| 4 | Mission Director orchestration entry | **Complete** (v1.4 — this delivery) |
| 4+ | Live command examples; optional light hooks; Light vs Full PRB | Planned (hooks still off) |
| 5 | Deeper automation only if high-value and low noise | Deferred |

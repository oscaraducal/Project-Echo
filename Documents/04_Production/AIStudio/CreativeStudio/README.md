# Creative Studio

**Status:** Active — AI Studio **v1.2** (Phase 2)  
**Date:** 2026-07-25  
**Scope:** Documentation + Cursor skills only (no Unreal maps / Blueprints / Story Canon edits)  
**Parent:** [AI Studio README](../README.md) · [Production Playbook](../../ProductionPlaybook.md)  

---

## Purpose

Creative Studio supports environment creation, asset production, world building, visual quality, and production efficiency — from concept through final asset integration — without redesigning Project Echo’s game vision.

Every Creative Skill has **one clear responsibility**, non-overlapping boundaries, Playbook integration, and reusable outputs aligned to grounded industrial horror.

---

## Principles (priority order)

1. Reuse existing Project Echo assets whenever possible.  
2. Purchase / download existing assets (Fab → Quixel) before creating new ones.  
3. Create new assets only when required.  
4. Keep Project Echo visually consistent (Art Bible + Facility / Room Bibles).  
5. Produce production-ready documentation.

---

## Asset Creation Hierarchy (permanent studio rule)

```text
Need an Asset?
  → Exists in Project Echo?     YES → Reuse
  → Fab can provide?            YES → Use Fab
  → Quixel can provide?         YES → Use Quixel
  → Meshy AI can generate?      YES → Generate with Meshy
  → Blender can modify existing? YES → Modify existing
  → ELSE → Create completely custom asset
```

Full pipeline: [AssetCreationPipeline.md](AssetCreationPipeline.md).  
Skill graph: [SkillRelationships.md](SkillRelationships.md).

---

## Skills (Cursor)

Logical **domain** grouping lives here. Skill folders stay **flat** under `.cursor/skills/` for reliable Cursor discovery (see Repository Architecture below).

| Domain | Skill | Responsibility (one line) |
|--------|-------|---------------------------|
| Planning | `asset-creation-planner` | Mission → complete asset list, priority, roadmap |
| Pipeline | `ai-asset-coordinator` | Sources, reuse, tracker, production queue |
| Spec | `mesh-designer` | Mesh specs, Meshy/reference prompts, UE5 import checklist |
| Space | `environment-designer` | Layout, flow, horror pacing, landmarks, guidance |
| Space | `facility-designer` | Industrial realism, equipment, pipes, maintenance paths |
| Dressing | `prop-designer` | Prop placement, clutter, reuse, missing-prop requests |
| Look | `lighting-designer` | Navigation / emergency / atmosphere / world-response light |
| Sound | `audio-designer` | Ambience, machinery, Witness cues, silence |
| Narrative space | `environmental-storytelling-designer` | Visual story before notes |
| Presentation | `cinematic-designer` | Reveals, framing, memorable composition |
| Cost | `performance-designer` | Nanite / LOD / streaming / light cost risks |

Production Studio skills (Phase 1) remain adjacent: `mission-planner`, `mission-implementer`, `production-review-board`, `documentation-sync`, `playtest-generator`.

---

## Production flow (with Creative Studio)

```text
Mission Plan (mission-planner)
  → Approval
  → Asset Creation Planner
  → AI Asset Coordinator (sources + queue)
  → Parallel design skills (Environment / Facility / Prop / Lighting / Audio / EnvStory / Cinematic / Performance)
  → Mesh Designer (only for assets that must be created)
  → Implementation (mission-implementer) — UE5 integration
  → Docs / PRB / Human PIE
```

Creative skills produce **plans and specifications**. They do **not** place actors in maps or edit Blueprints unless a later approved gameplay mission explicitly includes that work.

---

## Integration (required reads)

| Authority | Path |
|-----------|------|
| Production Playbook | `Documents/04_Production/ProductionPlaybook.md` |
| Gameplay Design Bible | `Documents/01_Game_Design/GameplayDesignBible.md` |
| Story Bible | `Documents/03_World/StoryBible.md` |
| Facility Bible | `Documents/03_World/FacilityBible.md` |
| Room Bible | `Documents/03_World/RoomBible.md` |
| Art / Audio Bibles | `Documents/01_Game_Design/ArtBible.md`, `AudioBible.md` |
| Asset tracking | `Documents/04_Production/AssetMasterList.md`, `Documents/02_Technical/AssetCatalog.md` |

Do **not** modify Story Canon from Creative Skills. Propose storytelling placement only; canon changes require EP / ADR.

---

## Repository Architecture (recommended)

### Decision: flat skills + documented domains

| Option | Pros | Cons | Verdict |
|--------|------|------|---------|
| Nested `.cursor/skills/creative/...` | Visual grouping | Cursor skill discovery is unreliable beyond one level | **Reject** |
| Flat `.cursor/skills/<skill-name>/` | Reliable discovery; simple paths | Grouping only in docs | **Adopt** |
| Prefixes (`creative-mesh-designer`) | Sortable | Longer names; noisy | Optional later |

**Adopted tree:**

```text
.cursor/
  rules/                          # thin always-on + scoped
    creative-studio.mdc           # Asset Creation Hierarchy (scoped)
  skills/                         # FLAT — one folder per skill
    mission-planner/              # Production Studio
    mission-implementer/
    production-review-board/
    documentation-sync/
    playtest-generator/
    asset-creation-planner/       # Creative Studio
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
  agents/                         # PRB role briefs (unchanged)
Documents/04_Production/AIStudio/
  README.md
  CreativeStudio/
    README.md
    AssetCreationPipeline.md
    SkillRelationships.md
    Phase2-CompletionReport.md
```

Do **not** create `.cursor/skills/production|creative|environment|art|technical/` package folders unless Cursor later documents stable nested discovery — keep domains in this README and SkillRelationships.

---

## Related

- [Phase 2 Completion Report](Phase2-CompletionReport.md)  
- [Migration Plan](../MigrationPlan.md)  
- [Hooks Policy](../Hooks.md) — hooks remain **disabled** in Phase 2 Creative delivery  

# Previsualization Studio (Previs Studio)

**Status:** Active — AI Studio **v1.3** (Phase 3)  
**Date:** 2026-07-25  
**Scope:** Documentation + Cursor skills only (no Unreal / Blueprints / Story Canon / image generation / hooks)  
**Parent:** [AI Studio README](../README.md) · [Production Playbook](../../ProductionPlaybook.md)  
**Sibling:** [Creative Studio](../CreativeStudio/README.md)  

---

## Purpose

Ensure every production mission can be **seen, understood, and mentally played** before Unreal implementation.

> Can someone mentally play this level from beginning to end?

If **No**, the mission is not ready for implementation.

The Executive Producer approves the **player experience**, not text alone.

Previs Studio **visualizes** gameplay. It does **not** design gameplay mechanics or implement UE5.

---

## Permanent production rule

**No production mission may enter implementation until a complete Visual Design Package (VDP) has been EP-approved.**

Specification: [VisualDesignPackage.md](VisualDesignPackage.md).

---

## Skills (Cursor — flat folders)

| Skill | Responsibility (one line) |
|-------|---------------------------|
| `experience-designer` | Player journey, pacing, emotional curve, rhythm |
| `blockout-visualizer` | Top-down floor plan, connections, flow, landmarks |
| `storyboard-designer` | Playable scene sequence + mission timeline |
| `concept-artist` | Image-gen **prompts**, mood/color/material palettes (no images in framework mission) |
| `lighting-visualizer` | Lighting mood boards + before/after power sequence |
| `asset-placement-designer` | Placement preview + readability (not production dressing ownership) |

Relationships / Creative non-overlap: [SkillRelationships.md](SkillRelationships.md).

---

## Production pipeline (with Previs)

```text
mission-planner
  → environment-designer (Creative — spatial design intent)
  → experience-designer
  → blockout-visualizer
  → storyboard-designer
  → concept-artist
  → lighting-visualizer (+ asset-placement-designer)
  → Visual Design Package
  → Executive Producer VDP Approval  (= Ready to Implement for production slices)
  → mission-implementer
  → Human PIE Gameplay
  → Production Review Board
```

Parallel Creative skills (facility, prop, lighting-**designer**, audio, etc.) may run to feed Previs and later implementation, but **implementation waits on VDP approval**.

---

## Integration

| Authority | Role |
|-----------|------|
| Production Playbook | Process + VDP gate (§12c) |
| Creative Studio | Design intent / asset hierarchy — Previs communicates it |
| Gameplay Design Bible | Loop, families, Witness rules (read for fidelity) |
| Story / Facility / Room Bibles | Canon + space function (read-only) |

---

## Repository architecture

Same as Creative Studio Phase 2: **flat** `.cursor/skills/<name>/` for discovery. Domain docs live here under `AIStudio/PrevisualizationStudio/`.

```text
Documents/04_Production/AIStudio/PrevisualizationStudio/
  README.md
  VisualDesignPackage.md
  SkillRelationships.md
  Phase3-CompletionReport.md
.cursor/skills/
  experience-designer/
  blockout-visualizer/
  storyboard-designer/
  concept-artist/
  lighting-visualizer/
  asset-placement-designer/
.cursor/rules/
  previs-studio.mdc
```

---

## Non-goals (this framework mission)

- No Unreal / Blueprint / map edits  
- No Story Canon edits  
- No asset creation  
- No image generation (prompts only)  
- No Hooks enabled  

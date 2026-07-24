# Visual Design Package (VDP)

**Status:** Active — permanent AI Studio standard  
**Date:** 2026-07-25  
**Gate:** Executive Producer approval required before `mission-implementer` on production missions  

---

## Rule

No production mission may enter Unreal implementation until this package is **complete** and **EP-approved**.

The EP must be able to mentally play the mission from beginning to end without opening Unreal.

---

## Package contents (required)

### 1. Mission Overview

One-page summary: fantasy, minutes, rooms, systems reused, cut list, horror beat.

### 2. Player Journey

```text
Beginning → Middle → Ending
```

Owned primarily by `experience-designer`.

### 3. Top-down Blockout

Every room: dimensions intent, connections, routes, landmarks, puzzle/Witness/objective markers.

Owned by `blockout-visualizer` (from Creative `environment-designer` intent).

### 4. Storyboard

Entire mission as ordered scenes (enter → notice → discover → solve → world response → Witness → exit).

Owned by `storyboard-designer`.

### 5. Hero Concept Prompts

Prompts for every major room (entrance, hero space, puzzle, landmark, exit). **Prompts only** unless a later art mission generates images.

Owned by `concept-artist`.

### 6. Lighting Concepts

```text
Before Power → After Power → Puzzle Solved → Witness
```

Owned by `lighting-visualizer` (informed by Creative `lighting-designer` when present).

### 7. Asset Placement

Interactive · Static · Decoration · Storytelling — readability review.

Owned by `asset-placement-designer`.

### 8. Gameplay Rhythm

```text
Explore → Observe → Understand → Operate → World Response → Witness → Exit
```

Owned by `experience-designer` (must align with Gameplay Design Bible loop).

---

## Suggested mission doc location

Store VDP under the mission folder, e.g.:

`Documents/05_Missions/PE-###-VisualDesignPackage.md`

Or a folder:

`Documents/05_Missions/PE-###/VisualDesignPackage/`

Link it from the Design Plan Approval Block.

---

## Executive Producer evaluation checklist

EP answers **Yes / No** to each:

| # | Question |
|---|----------|
| 1 | Can I understand the mission? |
| 2 | Can I mentally walk through the level? |
| 3 | Can I understand every objective? |
| 4 | Can I understand every puzzle? |
| 5 | Can I understand the pacing? |
| 6 | Can I imagine the horror? |
| 7 | Can I identify confusing areas? |
| 8 | Would I enjoy playing this? |

**Any No → return to Design / Previs.** Do not set Ready to Implement.

### Approval block (template)

```markdown
## Visual Design Package — EP Gate

| Field | Value |
|-------|--------|
| VDP complete | YES / NO |
| Mentally playable | YES / NO |
| EP decision | APPROVE / RETURN TO DESIGN |
| Ready to Implement | YES / NO — only if APPROVE |
| Notes | |
```

---

## Waivers

EP may waive VDP only in writing (e.g. pure systems docs mission with no spatial player loop). Gameplay production slices default to **no waiver**.

---

## Honesty

- Diagrams may be markdown / ASCII / mermaid — not required to be engine meshes.  
- Concept section = prompts (+ optional linked images from a later art pass).  
- Previs does not claim Gameplay PASS.  

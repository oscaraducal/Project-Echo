# Previsualization Studio — Skill Relationships

**Status:** Active  
**Date:** 2026-07-25  

---

## Non-overlap rule

Previs **communicates** design. Creative **specifies production intent**. Production **implements**.

If a deliverable could belong to both Creative and Previs, use this table.

---

## Relationship graph

```text
mission-planner
        │
        ▼
environment-designer (Creative — layout intent)
        │
        ├── facility / prop / lighting-designer / env-story / … (Creative, parallel)
        │
        ▼
experience-designer ──────────────┐
        │                         │
        ▼                         │
blockout-visualizer               │
        │                         │
        ▼                         │
storyboard-designer               │
        │                         │
        ├─► concept-artist        │
        ├─► lighting-visualizer   │
        └─► asset-placement-designer
                │
                ▼
        Visual Design Package
                │
                ▼
        EP VDP Approval (= Ready to Implement)
                │
                ▼
        mission-implementer
```

---

## Boundaries vs Creative Studio

| Concern | Creative owner | Previs owner |
|---------|----------------|--------------|
| Room layout / flow design intent | `environment-designer` | `blockout-visualizer` (draws/communicates it) |
| Engineering realism | `facility-designer` | — (reflect in blockout notes only) |
| Prop production reuse / requests | `prop-designer` | `asset-placement-designer` (preview + readability) |
| Lighting plan / color temps for build | `lighting-designer` | `lighting-visualizer` (mood board / sequence for EP) |
| Cinematic framing for production | `cinematic-designer` | Storyboard scenes may cite reveals; no ownership steal |
| Player emotion / journey for approval | — | `experience-designer` |
| Scene sequence for mental play | — | `storyboard-designer` |
| Concept prompts / palettes | — | `concept-artist` |
| Asset source hierarchy | `ai-asset-coordinator` | — |

---

## Per-skill summary

| Skill | Inputs | Outputs | Does not own |
|-------|--------|---------|--------------|
| `experience-designer` | Approved Design Plan + Environment intent | Experience Summary, Player Journey, Gameplay Rhythm, Emotional Curve | Mechanics invention; blockout drawing |
| `blockout-visualizer` | Environment (+ Facility) intent | Top-down Floor Plan, Room Connections, Flow Diagram, Landmark Map | Changing adjacency without Environment handoff |
| `storyboard-designer` | Journey + blockout | Gameplay Storyboard, Mission Timeline, Scene Breakdown | Concept palettes; lighting values |
| `concept-artist` | Rooms + Art Bible | Concept Art Prompts, Mood Board, Color/Material Palettes | Generating images in Phase 3 framework; mesh specs |
| `lighting-visualizer` | Lighting Designer plan + storyboard | Lighting Mood Board, Lighting Sequence, Visual Hierarchy | Final UE light actors; Nanite budgets |
| `asset-placement-designer` | Prop/EnvStory plans + blockout | Asset Placement Guide, Decoration Plan, Readability Review | Fab/Quixel shopping; mesh LODs |

---

## Handoff rules

1. **Plan before Previs** — need approved Design Plan.  
2. **Environment before Blockout Visualizer** — Previs draws Creative intent; does not invent a second layout.  
3. **Experience before Storyboard** — emotional beats drive scene order.  
4. **Assemble VDP** — all eight sections present before EP gate.  
5. **No implementer without EP VDP APPROVE** on production slices.  

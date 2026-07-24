# Creative Studio — Skill Relationships

**Status:** Active  
**Date:** 2026-07-25  

---

## Non-overlap rule

One skill owns one concern. If two skills could claim the same output, the table below wins. Hand off; do not rewrite another skill’s deliverable.

---

## Relationship graph

```text
mission-planner (approved brief)
        │
        ▼
asset-creation-planner ──────────────► ai-asset-coordinator
        │                                      │
        │                                      ├─► mesh-designer (create path only)
        ▼                                      │
   ┌────┴────────────────────────────────┐     │
   │ Parallel creative plans             │     │
   │ environment-designer                │     │
   │ facility-designer                   │     │
   │ prop-designer                       │◄────┘ (reuse / missing props)
   │ lighting-designer                   │
   │ audio-designer                      │
   │ environmental-storytelling-designer │
   │ cinematic-designer                  │
   │ performance-designer                │
   └────────────────┬────────────────────┘
                    ▼
           Visual Design Package + EP Approval (Previs — Playbook §12c)
                    ▼
           mission-implementer (UE5)
                    ▼
        documentation-sync / PRB / playtest-generator
```

---

## Boundaries matrix

| Skill | Owns | Does not own |
|-------|------|--------------|
| `asset-creation-planner` | What assets are needed, priority, category, workload estimate | Source marketplace choice details; mesh topology; map placement |
| `ai-asset-coordinator` | Hierarchy enforcement, tracker, queue, source recommendation | Room layout; lighting mood; writing Story Canon |
| `mesh-designer` | Specs + prompts + UE5 import checklist for **create** path | Prop placement density; facility pipe routing |
| `environment-designer` | Room layout, gameplay flow, navigation, horror pacing, landmarks, readability, backtracking | Engineering pipe realism (Facility); note text canon |
| `facility-designer` | Engineering realism, equipment, maintenance paths, pipe routing, industrial consistency | Player emotional pacing (Environment/Horror); cinematic framing |
| `prop-designer` | Prop placement plan, clutter balance, reuse list, new prop requests | Mesh LOD/collision specs; lighting temperature |
| `lighting-designer` | Light plan, progression, color temperature, silhouette support | Audio layers; mesh authoring |
| `audio-designer` | Cue list, ambient layers, trigger locations, silence plan | Music score redesign unless briefed; mesh work |
| `environmental-storytelling-designer` | Visual story beats, clues, note **justification** (symptoms) | Authoring final note text as Story Canon; combat beats |
| `cinematic-designer` | Reveal moments, framing, composition highlights | Full room blocking (Environment); performance budgets |
| `performance-designer` | Nanite/LOD/instancing/streaming/light-cost review | Aesthetic direction overrides without EP |

---

## Inputs / Outputs (summary)

| Skill | Primary inputs | Primary outputs |
|-------|----------------|-----------------|
| Asset Creation Planner | Approved Mission Brief + bibles | Complete Asset List, Priority, Production Roadmap, Reuse Opportunities |
| AI Asset Coordinator | Planner list + catalogs | Asset Tracker, Production Queue, Source Recommendations |
| Mesh Designer | Coordinator create-queue items | Mesh Spec, Meshy Prompt, Reference Prompt, UE5 Import Checklist |
| Environment Designer | Brief + Room/Facility + Gameplay Bible | Room Layout, Gameplay Flow, Landmark Plan, Witness Placement, Lighting Zones (intent) |
| Facility Designer | Brief + Facility Bible | Facility Review, Equipment Layout, Engineering Notes |
| Prop Designer | Layout + Planner/Coordinator | Prop Placement Plan, Reuse List, New Prop Requests |
| Lighting Designer | Layout + horror/atmosphere goals | Lighting Plan, Progression, Color Temperature Guide |
| Audio Designer | Layout + Audio Bible | Audio Cue List, Ambient Layers, Trigger Locations |
| Env. Storytelling Designer | Story/Facility/Room + layout | Storytelling Plan, Environmental Clues, Note Recommendations |
| Cinematic Designer | Layout + landmarks | Composition Guide, Reveal Plan, Visual Highlights |
| Performance Designer | All creative plans + asset queue | Performance Review, Optimization Suggestions, Risk Assessment |

---

## Handoff rules

1. **Planner before Coordinator** — no source shopping without a need list.  
2. **Coordinator before Mesh Designer** — hierarchy must record why create is required.  
3. **Environment before Prop / Lighting / Audio / Cinematic** — space first.  
4. **Facility in parallel with Environment** — resolve conflicts toward believable industrial function without breaking playable flow.  
5. **EnvStory before locking note placements** — environment tells first; notes only when justified.  
6. **Performance reviews before “final” asset buy/generate** for dense or hero meshes.  
7. **Implementation only after approval** — Creative outputs feed `mission-implementer`; they are not silent map edits.

---

## PRB mapping (optional consult)

| Creative skill | Closest agent brief |
|----------------|---------------------|
| Environment / Cinematic | `level-designer`, `creative-director` |
| Facility | `technical-artist`, `lead-developer` |
| Lighting / Performance | `technical-artist` |
| Audio | `audio-director` |
| EnvStory | `narrative-director`, `horror-director` |
| Prop / Mesh / Coordinator | `technical-artist`, `creative-director` |

# Asset Creation Pipeline

**Status:** Active — permanent AI Studio standard  
**Date:** 2026-07-25  
**Owners:** Creative Studio · AI Asset Coordinator  

---

## Goal

Get the right asset into Project Echo with the **least new work**, while preserving grounded industrial horror consistency.

---

## Permanent hierarchy

```text
Need an Asset?

↓

Does it already exist in Project Echo?

YES → Reuse

NO

↓

Can Fab provide it?

YES → Use Fab

NO

↓

Can Quixel provide it?

YES → Use Quixel

NO

↓

Can Meshy AI generate it?

YES → Generate with Meshy

NO

↓

Can Blender modify an existing asset?

YES → Modify Existing Asset

NO

↓

Create a completely custom asset
```

Every Creative Skill must apply this hierarchy **before** requesting new authoring work.

---

## Pipeline stages

| Stage | Owner skill | Output |
|-------|-------------|--------|
| 1. Mission asset needs | `asset-creation-planner` | Complete Asset List, Priority, Production Roadmap, Reuse Opportunities |
| 2. Source decisions | `ai-asset-coordinator` | Asset Tracker rows, Production Queue, Source Recommendation per asset |
| 3. Spatial / look / sound plans | Environment, Facility, Prop, Lighting, Audio, EnvStory, Cinematic, Performance | Domain plans (no mesh authoring yet) |
| 4. New mesh specs (only if Stage 2 says create) | `mesh-designer` | Mesh Spec, Meshy Prompt, Reference Prompt, UE5 Import Checklist |
| 5. Integration | `mission-implementer` (approved gameplay mission) | Assets in Content + map placement as briefed |
| 6. Catalog | Coordinator + docs sync | `AssetMasterList.md` / `AssetCatalog.md` updates |

---

## Asset categories (planner taxonomy)

- Structure  
- Machinery  
- Architecture  
- Props  
- Furniture  
- Lighting  
- Signage  
- Decals  
- Interactive Objects  
- Environmental Storytelling Objects  

---

## Source rules

| Source | When | Notes |
|--------|------|-------|
| Project Echo | Always first | Search `Content/ProjectEcho` + known ThirdParty already in project |
| Fab | Marketplace fill after project miss | Prefer industrial / utility packs consistent with Art Bible |
| Quixel | Photoreal fills / surfaces | Match facility material language; avoid sci-fi chrome |
| Meshy AI | Unique hero / interactive mesh when market lacks fit | Spec via `mesh-designer`; tag AI-gen debt until art-passed |
| Blender modify | Kitbash / fix / modularize existing | Prefer modifying licensed/owned assets only |
| Custom | Last resort | Document why hierarchy failed |

ThirdParty packs stay under `Content/ThirdParty/<PackName>/` — do not reorganize vendor packs (ASSET-001 / folder-structure rule).

---

## Consistency gate

Before accepting Fab / Quixel / Meshy / custom:

- Matches Art Bible tone (grounded industrial, not arcade)  
- Fits Facility / Room function  
- Does not invent Story Canon  
- Performance Designer risks noted for high-poly / dense instances  

---

## Tracker fields (minimum)

Recommended columns for Asset Tracker / Production Queue:

`AssetID | Name | Category | Priority | SourceDecision | HierarchyStep | Mission | Status | Notes`

Statuses: `Reuse` · `Acquire` · `Generate` · `Modify` · `Custom` · `Integrated` · `Blocked`

---

## Anti-patterns

- Jumping to Meshy or custom before Project / Fab / Quixel search  
- Duplicate meshes under new names  
- “Unique” props that are decorative clones of existing kit  
- Integrating AI meshes without import checklist / collision / pivot notes  
- Creative skills silently changing Story Bible or gameplay Blueprints  

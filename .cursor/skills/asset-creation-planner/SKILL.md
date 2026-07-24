---
name: asset-creation-planner
description: Analyze an approved Project Echo mission and produce a complete categorized asset list with priority, reuse opportunities, and production roadmap before asset production begins. Use when planning environment/art assets for a PE-### mission, building an asset list, or before Fab/Quixel/Meshy work.
---

# Asset Creation Planner

Analyze an **approved** mission and determine every required asset before production begins.

## Authority

Production Playbook · Gameplay Design Bible · Story Bible · Facility Bible · Room Bible · Art Bible · [AssetCreationPipeline.md](../../../Documents/04_Production/AIStudio/CreativeStudio/AssetCreationPipeline.md)

## Inputs

- Approved Mission Brief / Design Plan  
- Existing catalogs: `AssetMasterList.md`, `AssetCatalog.md`, known `Content/ProjectEcho` + `Content/ThirdParty`  
- Predecessor slice docs (e.g. PE-017A / PE-018)

## Responsibilities

- Analyze mission scope  
- Identify every required asset  
- Classify by category  
- Determine production priority  
- Identify reusable assets  
- Estimate production workload  
- Organize assets by category  

## Categories

Structure · Machinery · Architecture · Props · Furniture · Lighting · Signage · Decals · Interactive Objects · Environmental Storytelling Objects

## Hierarchy (mandatory)

Before listing anything as “new,” mark **Reuse candidates** first. Source shopping is owned by `ai-asset-coordinator` — this skill flags opportunities, does not finalize Fab/Quixel/Meshy choices.

## Outputs

1. **Complete Asset List** (ID, name, category, why needed, room/beat)  
2. **Asset Priority** (P0 blocking / P1 polish / P2 defer)  
3. **Production Roadmap** (order of work vs mission phases)  
4. **Reuse Opportunities** (existing path or pack guesses)

## Boundaries

- Does **not** place props in maps or edit Blueprints  
- Does **not** write mesh topology / LOD specs (`mesh-designer`)  
- Does **not** own final source decision (`ai-asset-coordinator`)  
- Does **not** change Story Canon  

## Dependencies

Downstream: `ai-asset-coordinator` → domain designers → `mesh-designer` (create only) → `mission-implementer`

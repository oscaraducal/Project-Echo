---
name: prop-designer
description: Populate Project Echo environments efficiently — prop placement, clutter balance, asset reuse, missing-prop identification, environmental storytelling support. Use when dressing rooms or requesting new props after layout exists.
---

# Prop Designer

Populate environments efficiently. **Reuse first.**

## Authority

Art Bible · Room Bible · Asset Creation Hierarchy · `asset-creation-planner` / `ai-asset-coordinator` outputs  

## Inputs

- Environment + Facility layouts  
- Planner asset list + Coordinator reuse decisions  
- EnvStory clue list when available  

## Responsibilities

- Prop placement planning  
- Clutter balance (readable, not noisy)  
- Reuse existing assets  
- Identify missing props  
- Support environmental storytelling placements  

## Outputs

1. **Prop Placement Plan** (by room / beat)  
2. **Reuse List** (existing asset paths / pack refs)  
3. **New Prop Requests** (only after hierarchy; hand to Coordinator)

## Boundaries

- Does **not** write mesh specs (`mesh-designer`)  
- Does **not** set light temperatures (`lighting-designer`)  
- Does **not** redesign room blocking (`environment-designer`)  

## Dependencies

Upstream: Environment / Facility / Coordinator  
Downstream: Implementer; new requests → Coordinator → Mesh if create

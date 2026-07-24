---
name: mission-planner
description: Design Project Echo mission plans for approval before any Unreal implementation. Use when drafting a PE-### Design Plan, scoping a new production slice, or when the user asks to plan (not build) a mission.
---

# Mission Planner

Produce an **approval-ready Design Plan**. Do **not** implement Blueprints, maps, or gameplay until the plan is explicitly approved (Ready to Implement).

## Authority

1. Story Bible  
2. Gameplay Design Bible  
3. Production Playbook — `Documents/04_Production/ProductionPlaybook.md`  
4. ADRs — DecisionLog  
5. Any predecessor mission docs  

## When to use

- New PE-### mission before coding  
- Expanding a production map / beat  
- User asks for a design plan, scope cut, or “plan first”

## Steps

1. Read Gameplay Design Bible + relevant Facility/Room + predecessor missions (e.g. PE-017A / PE-018).  
2. State player experience goal (minutes, loop, teaching beat).  
3. Inventory **existing** systems to reuse — forbid parallel frameworks.  
4. Lock a **cut list** (what will not ship).  
5. Draft layout (≤5 rooms preferred), objective chain, notes rules (symptoms only).  
6. Horror: Witness pattern if any — exit-path, post-power, tension only.  
7. Technical plan: new map/actors only as needed; prefer config + SliceReset twin.  
8. Risks + mitigations; human PIE / EP waiver note if foundation unvalidated.  
9. Compliance checklist vs bible + Production Playbook.  
10. **Stop** with Approval Block — wait for Ready to Implement.

## Default recipes

- New production map → **PE-018 map recipe** (Playbook §10).  
- Maintenance fuse path → owned by **PE-017A**; do not fork.

## Outputs

- Design Plan markdown under `Documents/05_Missions/PE-###-DesignPlan.md` (or update existing)  
- Explicit Ready for Approval / Ready to Implement fields  
- No `.uasset` changes in this skill

## Anti-patterns

- Implementing while “just planning”  
- Scope creep (valve + fuse + keycard in one mission)  
- Walkthrough notes  
- Combat / chase without ADR  

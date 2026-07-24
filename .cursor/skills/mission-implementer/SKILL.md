---
name: mission-implementer
description: Implement approved Project Echo missions in Unreal Engine 5 by reading the Mission Brief and design bibles, reusing existing Blueprint architecture, updating docs, and producing a Mission Completion Report. Use when implementing a PE-### mission, executing an approved Mission Brief, or when the user asks to implement, build, or land a Project Echo mission.
---

# Mission Implementer

Implement **approved** Project Echo missions in UE5. Do not redesign approved systems. Prefer reuse over new architecture. Avoid feature creep and duplicate systems.

## Authority (do not reorder)

If anything conflicts, stop and ask for clarification before implementing:

1. Story Bible — `Documents/03_World/StoryBible.md`
2. Gameplay Design Bible — `Documents/01_Game_Design/GameplayDesignBible.md`
3. Production Playbook — `Documents/04_Production/ProductionPlaybook.md` (+ ContributionGuide for naming)
4. ADRs — `Documents/00_Governance/DecisionLog.md`
5. Mission Brief — `Documents/05_Missions/PE-###-*.md`

Supporting (implementation truth, not higher than the list above):

- `Documents/02_Technical/BlueprintStandards.md`
- `Documents/02_Technical/BlueprintArchitecture.md`
- `Documents/02_Technical/Architecture/BlueprintDependencyMap.md`
- `Documents/02_Technical/GameplaySystems.md`
- `Documents/00_Governance/AIStudio.md`
- `Documents/04_Production/AIStudio/README.md`

## Preconditions

Before any Unreal work:

1. Locate the Mission Brief / approved Design Plan under `Documents/05_Missions/`.
2. Confirm **approved for implementation** (written approval / Ready to Implement). If blocked or design-only, stop — use `mission-planner` instead.
3. Read Story Bible + Gameplay Design Bible for tone, loop, and system mapping.
4. Check DecisionLog for ADRs that affect this mission.
5. Inventory existing Blueprints/systems that already cover the brief. Reuse or extend; do not fork parallel frameworks.
6. Apply Playbook recipes: default new production map = **PE-018**; fuse path ownership = **PE-017A**.

## Implementation rules

- Reuse existing Blueprints, components, interfaces, and folder layout whenever possible.
- Prefer composition and config over new base classes.
- Do not introduce new gameplay mechanics unless the approved brief explicitly requires them.
- Do not redesign approved systems (power, inventory, objectives, puzzles, interaction, etc.).
- Mission IDs belong in docs, changelog, commits, reports, and prototype map names — not in reusable asset names.
- Follow Asset Naming Standard v1.0 (`BP_`, `BPC_`, `BPI_`, `WBP_`, …) from the Contribution Guide.
- Prototype maps: `LV_Prototype_PE###`. Production maps are separate and must not depend on prototypes.
- If replay is claimed, implement **full** SliceReset (Playbook §5).
- Notes = symptoms only; ObjectiveOnRead skip-if-empty.
- Indoor emergency-dark; no outdoor Directional/Sky dominance on indoor slices.
- Witness = exit-path presence after power; tension only; no chase unless ADR.
- Use Unreal MCP (`project-0-ProjectEcho-unreal-mcp`) for Blueprint/editor work when available: discover toolsets first, then call tools. Prefer inspecting existing assets before creating new ones.

## Workflow

Copy and track:

```
Mission Progress:
- [ ] 1. Read & confirm approved Mission Brief
- [ ] 2. Read Story Bible + Gameplay Design Bible + Production Playbook
- [ ] 3. Map brief → existing systems (no duplicates)
- [ ] 4. Implement in UE5 (minimal scope)
- [ ] 5. Compile Blueprints
- [ ] 6. Technical Simulate / PIE verification
- [ ] 7. Prepare human PIE checklist (Gameplay PASS is EP)
- [ ] 8. Regression on affected systems/maps
- [ ] 9. Update documentation
- [ ] 10. Mission Completion Report
- [ ] 11. Git commit / push only if user requests
```

### Scope discipline

Implement only what the approved brief requires. If a “nice to have” appears during work, note it in the report — do not ship it in the same mission unless the brief already includes it.

### Documentation updates (required)

Update truth to match the build. Typical touchpoints:

- Mission doc status / notes under `Documents/05_Missions/`
- `Documents/04_Production/Changelog.md` (append only)
- Architecture / systems docs only if ownership, APIs, or dependencies actually changed
- `Documents/04_Production/ProjectHealth.md` or roadmap only when the mission changes project status

Do not invent APIs in docs. Document what was inspected or implemented.

### Validation (before marking complete)

From Contribution Guide + Production Playbook — verify:

- Naming follows Asset Naming Standard v1.0
- Prototype map naming if applicable
- Descriptive actor labels (no `PE###_` prefix on actors)
- Assets remain reusable; folders consistent
- Redirectors fixed after renames
- Honest gates: Technical PASS ≠ Gameplay PASS

Definition of Done: compile pass, no Blueprint errors, technical runtime verified, human Gameplay PASS or explicit PENDING_USER / waiver noted, regression pass, docs, commit/push when requested, Mission Completion Report submitted.

## Mission Completion Report

Produce this report at the end of every gameplay mission (format from Contribution Guide):

```
# Mission Completion Report

Mission

PE-###

Status

Complete

Branch

<Branch Name>

Commit

<Commit Hash>

Blueprints Created

Blueprints Modified

Maps Created

Maps Modified

Documentation Updated

Compile

PASS / FAIL

Runtime Test

PASS / FAIL

Regression Test

PASS / FAIL

Git Commit

PASS / FAIL

Git Push

PASS / FAIL

Ready For Review

YES / NO

Notes

Implementation notes, limitations, or important observations.
```

Use `N/A` or `FAIL` honestly. Do not mark Ready For Review YES if compile, runtime, or required docs are incomplete. Human PIE / Gameplay PASS may still be required from Oscar — note that in Notes when applicable.

## Anti-patterns

- Implementing an unapproved or design-only brief
- Creating a second inventory, power, objective, or puzzle framework
- Expanding scope mid-mission without brief/ADR update
- Silent divergence from Story or Gameplay Design Bible
- Mixing unrelated dirty Blueprints into the mission commit
- Claiming Gameplay PASS from Technical-only / Slate evidence
- Skipping the Mission Completion Report

# Mission Director — Command Reference

**Status:** Active — permanent AI Studio operating contract  
**Date:** 2026-07-25  
**Skill:** `.cursor/skills/mission-director/SKILL.md`  
**Version:** AI Studio **v1.5**  

---

## EP command vocabulary (permanent)

```text
Start Mission PE-###
Continue Mission PE-###
Generate Visual Package PE-###
Implement Mission PE-###
Validate Mission PE-###
Review Mission PE-###
Close Mission PE-###
```

EP should not name individual skills. Mission Director selects them.

---

## Lifecycle ↔ commands

```text
Start Mission
  → mission-planner
  → STOP (Design Plan approval)

Continue Mission
  → next incomplete phase skills
  → STOP (next gate)

Generate Visual Package
  → [environment-designer if needed]
  → experience → blockout → storyboard → concept → lighting-visualizer → asset-placement
  → STOP (VDP / Ready to Implement)

Implement Mission
  → prerequisite check (Plan + VDP APPROVE)
  → mission-implementer (+ MCP Auto-accept AUTHORIZATION — see MCP-AutoAccept-Policy.md)
  → STOP (Technical done → Validate / human PIE)

Validate Mission
  → technical evidence + playtest-generator
  → STOP (Human Gameplay Validation)

Review Mission
  → QA Studio (8 skills → QA Review Package)
  → production-review-board (+ agents; consumes QA package)
  → STOP (EP merge)

Close Mission
  → documentation-sync
  → archive / history
  → STOP (Closed)
```

---

## Phase → skill map

| Phase | Auto-selected skills (typical) | Gate |
|-------|-------------------------------|------|
| Plan | `mission-planner` | EP Design Plan proceed |
| Creative layout (as needed) | `environment-designer`, optional facility/prop/lighting-designer/env-story/… | Feeds Previs |
| Asset prep (as needed) | `asset-creation-planner` → `ai-asset-coordinator` → `mesh-designer` (create only) | Before/during implement |
| Previs / VDP | `experience-designer` → `blockout-visualizer` → `storyboard-designer` → `concept-artist` → `lighting-visualizer` → `asset-placement-designer` | EP VDP APPROVE |
| Implement | `mission-implementer` | Technical complete |
| Validate | `playtest-generator` (+ technical notes) | Human PIE |
| QA | 8 QA Studio skills → QA Review Package | Feeds PRB |
| Review | `production-review-board` (after QA) | EP merge |
| Close | `documentation-sync` | Archived |

---

## Operating rules (enforce always)

1. No phase skipped  
2. No implementation before EP approval (incl. VDP for spatial production)  
3. Required documentation every mission  
4. Stop at approval gates  
5. Automatic skill selection  
6. EP never manually coordinates skills  
7. Story Canon inviolable  
8. Production Playbook enforced  
9. Repository consistency preserved  

---

## Informal → command mapping

| EP says (examples) | Run as |
|--------------------|--------|
| “New mission for security wing” | Start Mission |
| “Keep going on PE-020” | Continue Mission |
| “I need to see it / previs / VDP” | Generate Visual Package |
| “Build it / implement” | Implement Mission |
| “Test it / validate” | Validate Mission |
| “PRB / review for merge” | Review Mission |
| “Close it out / archive” | Close Mission |
| “auto accept for PE-###” | Sticky MCP authorization for that mission (see [MCP-AutoAccept-Policy.md](MCP-AutoAccept-Policy.md)) |

---

## MCP Auto-accept (Implement)

EP `Implement Mission PE-###`, sticky `auto accept for PE-###`, or `APPROVED FOR IMPLEMENTATION` authorizes Unreal MCP asset create/duplicate for that mission. **Does not** waive VDP, Story Canon, or Human Gameplay PASS. Full policy: [MCP-AutoAccept-Policy.md](MCP-AutoAccept-Policy.md).

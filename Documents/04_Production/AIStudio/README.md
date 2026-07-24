# Project Echo — AI Studio

**Status:** Active — Phase 1 (documentation + Cursor workflow)  
**Date:** 2026-07-25  

---

## Purpose

AI Studio is the development-workflow layer that helps Oscar, ChatGPT, and Cursor operate like a small professional game studio — without redesigning Project Echo’s game vision.

Phase 1 delivers **docs + Cursor infrastructure only** (no gameplay / uasset changes).

---

## Architecture Overview

```text
Documents (authority)
  ProductionPlaybook.md     ← process source of truth
  00_Governance/*           ← bibles adjacent, ADRs, contribution
  01–05_*                   ← design / tech / world / production / missions

.cursor/ (agent operating system)
  rules/*.mdc               ← always-on + scoped enforcement
  skills/*/SKILL.md         ← repeatable workflows
  agents/*.md               ← Task-tool role briefs (non-overlapping)
  hooks/                    ← optional; Phase 1 prefers docs (see Hooks.md)
  mcp.json                  ← Unreal MCP (leave alone unless required)
```

### Authority order (unchanged vision)

1. Story Bible  
2. Gameplay Design Bible  
3. Production Playbook (+ ContributionGuide naming)  
4. ADRs  
5. Mission Brief  

---

## Recommended `.cursor` Tree

```text
.cursor/
  mcp.json
  rules/
    foundation.mdc                 # alwaysApply — identity, authority, no redesign
    production-standard.mdc        # alwaysApply — DoD, human PIE, honest gates
    blueprint-standards.mdc        # Content/ProjectEcho — DOC-002
    gameplay-standards.mdc         # bible loop, no combat/chase without ADR
    story-canon.mdc                # symptoms not walkthrough
    documentation-standard.mdc     # append-only changelog, reports
    folder-structure.mdc           # ASSET-001 / ThirdParty
  skills/
    mission-planner/
    mission-implementer/
    production-review-board/
    documentation-sync/
    playtest-generator/
  agents/
    executive-producer.md
    creative-director.md
    lead-developer.md
    gameplay-designer.md
    level-designer.md
    technical-artist.md
    horror-director.md
    narrative-director.md
    audio-director.md
    qa-lead.md
  hooks/                           # deferred / optional — see Hooks.md
```

---

## Skills Map

| Skill | Use when |
|-------|----------|
| `mission-planner` | Design plan first; wait for approval |
| `mission-implementer` | Approved brief → UE5 implement + report |
| `production-review-board` | Cross-role review before approve/merge |
| `documentation-sync` | Align docs / Changelog / indexes |
| `playtest-generator` | Manual PIE checklist for EP |

---

## Subagents

Role briefs in `.cursor/agents/` are prompt specs for Cursor’s Task tool. They are **not** a native Cursor “agents runtime.” Skills/rules reference them for Production Review Board and specialist reviews.

Duties are intentionally non-overlapping — see each brief’s Boundaries section.

---

## Reference Decisions (Phase 1)

| Decision | Rule |
|----------|------|
| Default production map recipe | **PE-018** (`LV_ARI_GeneratorAnnex` pattern) |
| Fuse path ownership | **PE-017A** (`LV_ARI_MaintenanceWing`) |
| Gameplay PASS | Human PIE (Enhanced Input) — Technical ≠ Gameplay |

---

## Related Docs

- [Production Playbook](../ProductionPlaybook.md)  
- [Migration Plan](MigrationPlan.md)  
- [Hooks Policy](Hooks.md)  
- Legacy [AIStudio.md](../../00_Governance/AIStudio.md)  

---

## Phase Status

| Phase | Focus | Status |
|-------|-------|--------|
| 1 | Playbook + Rules + Skills + Agents + Hooks policy | **This delivery** |
| 2 | Refine rules from live missions; optional light hooks | Planned |
| 3 | Deeper automation only if high-value and low noise | Deferred |

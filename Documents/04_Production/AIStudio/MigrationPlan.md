# AI Studio — Migration Plan

**Status:** Active  
**Date:** 2026-07-25  

---

## Goal

Migrate Project Echo’s ad-hoc AI collaboration into a durable studio OS: Playbook → Rules → Skills → Subagents → Hooks — without touching gameplay assets in Phase 1.

---

## Phase 1 Sequence (this delivery)

| Step | Deliverable | Rationale |
|------|-------------|-----------|
| 1 | **Production Playbook** | Single process authority consolidating PE-017 / PE-017A / PE-018 lessons before scattering rules |
| 2 | **Modular Rules** | Cursor always-on + scoped enforcement; one responsibility per `.mdc` |
| 3 | **Skills** | Repeatable workflows (plan → implement → review → docs → playtest) |
| 4 | **Subagents** | Non-overlapping role briefs for Task / PRB |
| 5 | **Hooks policy** | Prefer documentation over noisy automation in Phase 1 |

Order matters: rules without a playbook drift; skills without rules rediscover policy; agents without skills invent process; hooks without the rest amplify noise.

---

## What Migrates From Where

| Source | Migrates into |
|--------|----------------|
| `foundation.mdc` (legacy) | Evolved `foundation.mdc` + split production/gameplay/etc. |
| `Documents/00_Governance/AIStudio.md` | Still valid role overview; process detail → Playbook |
| ContributionGuide DoD / naming | Rules + Playbook pointers (guide remains canonical for DOC-002) |
| PE-017 / 017A / 018 mission lessons | Playbook §10–§11 + production-standard rule |
| `mission-implementer` skill | Improved; siblings added |

---

## Phase 2 (planned)

- Tune rule globs after real mission sessions  
- Optionally enable a **minimal** `sessionStart` prompt reminder (playbook path) if teams forget authority order  
- Add skill examples from live PE-019+ missions  

## Phase 3 (deferred)

- Broader hooks (auto-checklist inject, commit message nudges) only if measured value > noise  
- Any Unreal MCP automation wrappers — never claim Gameplay PASS  

---

## Non-Goals (all phases unless EP expands)

- Redesigning game vision or bibles’ creative content  
- Replacing ContributionGuide / TechnicalDebt as domain canons  
- Enabling noisy always-on hooks that interrupt every edit  
- Committing unrelated `.uasset` dirties with workflow docs  

---

## Success Criteria (Phase 1)

- [x] ProductionPlaybook.md authoritative and linked  
- [x] Modular rules present with frontmatter  
- [x] Five skills + ten agent briefs  
- [x] AIStudio README + MigrationPlan + Hooks.md  
- [x] Documents README / MasterIndex / Changelog updated  
- [x] No gameplay / production map / Blueprint changes in the Phase 1 commit  

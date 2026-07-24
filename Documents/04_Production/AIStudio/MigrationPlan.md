# AI Studio — Migration Plan

**Status:** Active  
**Date:** 2026-07-25  
**Current label:** AI Studio **v1.2**  

---

## Goal

Migrate Project Echo’s ad-hoc AI collaboration into a durable studio OS: Playbook → Rules → Skills → Subagents → Hooks — without touching gameplay assets in framework missions.

---

## Phase 1 Sequence (delivered)

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
| Phase 2 creative needs | `CreativeStudio/*` + 11 flat Creative skills + `creative-studio.mdc` |

---

## Phase 2 (Creative Studio) — delivered this mission

| Step | Deliverable | Status |
|------|-------------|--------|
| 1 | Creative Studio overview + skill relationship map | Done |
| 2 | Asset Creation Pipeline (permanent hierarchy) | Done |
| 3 | Eleven Creative Cursor skills (flat `.cursor/skills/`) | Done |
| 4 | Playbook §12b + lifecycle step 2b | Done |
| 5 | AI Studio README → v1.2 | Done |
| 6 | Hooks remain **disabled** | Done (policy only) |

### Repository decision (Phase 2)

**Adopt flat skill folders** under `.cursor/skills/`. Reject nested `skills/creative/...` packages until Cursor documents stable multi-level discovery. Domains are documented in `CreativeStudio/README.md`.

### Non-goals (Phase 2 framework mission)

- No Unreal map / Blueprint / gameplay system edits  
- No Story Canon edits  
- No enabled Hooks  

---

## Phase 2+ (planned)

- Tune rule globs after real creative + gameplay mission sessions  
- Add worked examples from live PE-019+ asset passes  
- Optionally enable a **minimal** `sessionStart` reminder only if authority order is still skipped  
- Light vs Full PRB tiers (FRAMEWORK-001 recommendation)

## Phase 3 (deferred)

- Broader hooks only if measured value > noise  
- Unreal MCP automation wrappers — never claim Gameplay PASS  

---

## Non-Goals (all phases unless EP expands)

- Redesigning game vision or bibles’ creative content  
- Replacing ContributionGuide / TechnicalDebt as domain canons  
- Enabling noisy always-on hooks that interrupt every edit  
- Committing unrelated `.uasset` dirties with workflow docs  

---

## Success Criteria

### Phase 1

- [x] ProductionPlaybook.md authoritative and linked  
- [x] Modular rules present with frontmatter  
- [x] Five production skills + ten agent briefs  
- [x] AIStudio README + MigrationPlan + Hooks.md  
- [x] Documents README / MasterIndex / Changelog updated  
- [x] No gameplay / production map / Blueprint changes in the Phase 1 commit  

### Phase 2

- [x] Creative Studio docs (overview, pipeline, relationships)  
- [x] Eleven Creative skills with non-overlapping boundaries  
- [x] Flat repository architecture documented and applied  
- [x] Playbook + AI Studio README at v1.2  
- [x] Hooks still disabled  
- [x] No Unreal / Story Canon changes in this framework mission  

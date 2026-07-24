# QA Studio

**Status:** Active — AI Studio **v1.5**  
**Date:** 2026-07-25  
**Scope:** Documentation + Cursor skills only (no Unreal / Blueprints / Story Canon / Hooks / fixes)  
**Parent:** [AI Studio README](../README.md) · [Production Playbook](../../ProductionPlaybook.md)  
**Orchestration:** [Mission Director](../MissionDirector/README.md) — `Review Mission PE-###`  

---

## Purpose

Protect Project Echo quality. QA Studio **evaluates, reviews, challenges, and reports**. It does not create, modify, or implement gameplay.

- QA does not decide — designers / EP decide.  
- QA informs with evidence.  
- Never assume design intent — evaluate the delivered experience objectively.  
- Identify issues before players do.  

---

## Philosophy

Independent department. Report evidence. Classify severity. Recommend review. Preserve objectivity.

**Never:** modify gameplay, redesign mechanics, create Blueprints, edit levels, change Story Canon, generate implementation code, implement fixes.

**Shall:** report evidence, classify severity, explain impact, recommend review.

---

## Skills (flat under `.cursor/skills/`)

| Skill | Evaluates |
|-------|-----------|
| `gameplay-qa-tester` | Progression, objectives, soft locks, sequence breaks |
| `navigation-qa-tester` | Routing, landmarks, orientation, dead ends |
| `horror-experience-tester` | Tension curve, Witness, atmosphere, pacing |
| `puzzle-qa-tester` | Clarity, difficulty, guidance, frustration |
| `environmental-storytelling-qa` | Notes, props, lore delivery, immersion |
| `accessibility-readability-qa` | Prompts, visibility, color dependence, hierarchy |
| `performance-risk-analyzer` | Density / streaming / effect risks (no UE benchmarks) |
| `regression-qa-tester` | Predecessor missions, docs drift, broken mechanics |

Package spec: [QAReviewPackage.md](QAReviewPackage.md)  
Boundaries: [SkillRelationships.md](SkillRelationships.md)

---

## Lifecycle position

```text
… → Implementation → Technical Validation → Human Gameplay Validation
  → QA Studio (Review Mission)
  → Production Review Board
  → Mission Close
```

QA completes **before** PRB final recommendation when EP runs `Review Mission PE-###`.

---

## Repository

```text
Documents/04_Production/AIStudio/QAStudio/
  README.md
  QAReviewPackage.md
  SkillRelationships.md
  Phase5-CompletionReport.md
.cursor/skills/<eight-qa-skills>/
.cursor/rules/qa-studio.mdc
```

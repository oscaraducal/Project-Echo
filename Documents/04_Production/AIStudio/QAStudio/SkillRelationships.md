# QA Studio — Skill Relationships

**Status:** Active  
**Date:** 2026-07-25  

---

## Non-overlap

QA evaluates. Production / Creative / Previs create. Mission Director orchestrates. PRB decides with EP.

| Concern | QA owner | Does not own |
|---------|----------|--------------|
| Progression / soft locks | `gameplay-qa-tester` | Fixing Blueprints |
| Routes / landmarks | `navigation-qa-tester` | Redesigning layout (`environment-designer`) |
| Tension / Witness fairness | `horror-experience-tester` | Authoring Witness beats |
| Puzzle clarity / difficulty | `puzzle-qa-tester` | New puzzle families |
| Notes / env story immersion | `environmental-storytelling-qa` | Rewriting Story Canon |
| Prompts / visibility / a11y | `accessibility-readability-qa` | Implementing UI |
| Lighting density / actor cost risks | `performance-risk-analyzer` | Optimization implementation (`performance-designer` specs remain Creative) |
| Predecessor breakage / doc drift | `regression-qa-tester` | Cleanup missions |

**Note:** Creative `performance-designer` plans budgets; QA `performance-risk-analyzer` reviews delivered/planned risk for the mission package — report only.

---

## Review Mission order

```text
Review Mission PE-###
  → QA Studio (all 8 skills → QA Review Package)
  → production-review-board (uses QA package as input)
  → STOP — EP merge / conditions
```

---

## vs Validate Mission

| Command | Focus |
|---------|--------|
| `Validate Mission` | Technical evidence + human PIE checklist generation |
| `Review Mission` | Full QA Package + PRB |

Do not skip QA by running only PRB.

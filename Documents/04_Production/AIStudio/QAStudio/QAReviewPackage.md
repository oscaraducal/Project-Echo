# QA Review Package

**Status:** Active — permanent AI Studio standard  
**Date:** 2026-07-25  
**Trigger:** Mission Director `Review Mission PE-###` (after Human Gameplay Validation when a player loop exists)  

---

## Rule

Every completed production mission shall generate a **QA Review Package** before the Production Review Board issues a final recommendation.

Suggested path: `Documents/05_Missions/PE-###-QAReviewPackage.md`

---

## Package contents (required)

1. **Executive QA Summary**  
2. **Gameplay QA** (`gameplay-qa-tester`)  
3. **Navigation QA** (`navigation-qa-tester`)  
4. **Horror QA** (`horror-experience-tester`)  
5. **Puzzle QA** (`puzzle-qa-tester`)  
6. **Storytelling QA** (`environmental-storytelling-qa`)  
7. **Accessibility QA** (`accessibility-readability-qa`)  
8. **Performance Risk Report** (`performance-risk-analyzer`)  
9. **Regression Report** (`regression-qa-tester`)  
10. **Consolidated Recommendations**  

---

## Severity levels (every issue)

| Level | Meaning | Examples |
|-------|---------|----------|
| **Critical** | Mission cannot ship | Soft lock, impossible puzzle, broken progression |
| **Major** | Playable; experience significantly degraded | Confusing objective chain, unfair Witness during solve |
| **Minor** | Noticeable; does not block completion | Clutter readability, weak landmark |
| **Observation** | Improvement opportunity; no action required | Optional polish ideas |

---

## Issue template

```markdown
### [CRITICAL|MAJOR|MINOR|OBSERVATION] — short title

- **Evidence:** what was observed (doc / design / known build behavior)
- **Impact:** player effect
- **Recommendation:** what designers should review (not a mandated redesign)
- **Owner suggestion:** Gameplay / Level / Horror / Narrative / Tech Art / EP
```

---

## Executive QA Summary template

```markdown
# QA Review Package — PE-###

**Date:** …
**Basis:** Design Plan / VDP / mission notes / Completion Report / human PIE status
**Ship readiness (QA opinion only):** Block / Conditions / Informational Pass

## Executive QA Summary
- Critical: N
- Major: N
- Minor: N
- Observations: N
- Top risks: …
- Human Gameplay PASS status: PASS / FAIL / PENDING_USER
```

---

## Honesty

- Docs-only / design-plan review: mark evidence as **document-based**, not PIE-verified.  
- Technical ≠ Gameplay. Do not invent PIE results.  
- Performance skill identifies **risks only** — does not claim FPS benchmarks.  
- QA does not implement fixes.  

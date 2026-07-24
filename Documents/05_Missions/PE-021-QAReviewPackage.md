# QA Review Package — PE-021 Security Wing

**Date:** 2026-07-25  
**Branch:** `develop`  
**Map:** `/Game/ProjectEcho/Maps/Production/LV_ARI_SecurityWing`  
**Basis:** Design Plan · VDP · mission notes · Validate Technical PASS (`ef48fe1`) · Playtest checklist · MCP Review inspect (map loaded; loop actors present)  
**Human Gameplay PASS:** **PENDING_USER** — not closed  
**Ship readiness (QA opinion only):** **Conditions** — Technical foundation sound; do not claim Ready For Review YES or Complete without human EI PIE (or EP written waiver)

---

## Executive QA Summary

| Severity | Count |
|----------|------:|
| Critical | 0 |
| Major | 2 |
| Minor | 4 |
| Observations | 4 |

**Top risks**

1. Human Gameplay / manual Replay still open — Technical ≠ Gameplay.  
2. Shared-parent PrintString / stale fuse `objectiveOnAvailable` may confuse first-play clarity until overridden or debt-accepted.  
3. SoftOpenExit stub has no next zone — expected; PE-022 must own destination.

**Honest gate reminder:** Enhanced Input cannot be fully driven by Slate/MCP. This package is **document + Technical/MCP evidence**, not a Gameplay PASS.

---

## 1. Gameplay QA (`gameplay-qa-tester`)

**Verdict:** Conditions — progression design is coherent; human PIE required.

| Check | Result | Evidence basis |
|-------|--------|----------------|
| Objective chain | Document PASS | BeginPlay → Note B ObjectiveOnRead → partial progress → post-solve “Access the next area” |
| Puzzle sequence | Document PASS | Keycard → Lobby gate → CS-BADGE/ZONE ENGAGE + CS-EXIT HOLD → MarkSolved |
| Incomplete fail | Technical PASS | SoftOpenExit locked pre-solve (Validate Simulate) |
| Soft-lock design | No Critical found on paper | SliceReset present; credential + 3 stations max |
| Sequence breaks | Deferred to human | Checklist covers incomplete unlock attempt |
| Anti-scope | Document PASS | No combat / chase / Signal second puzzle / Armory / Restricted dump in plan or notes |

### [MAJOR] — Human Gameplay PASS not executed

- **Evidence:** Mission notes + checklist: Gameplay **PENDING_USER**; Ready For Review **NO**.  
- **Impact:** Cannot certify full loop, Witness timing, or objective readability in real EI.  
- **Recommendation:** EP walk `PE-021-PlaytestChecklist.md` before Close claiming Complete.  
- **Owner suggestion:** EP

### [MINOR] — Stale parent `objectiveOnAvailable` fuse string on AccessClearance

- **Evidence:** Validate caveats — parent default “Find the fuse…” may surface if objective UI reads that field.  
- **Impact:** Momentary genre/family confusion (Electrical vs Security).  
- **Recommendation:** Override on `BP_AccessClearancePuzzle` or SecurityWingReset BeginPlay string in a debt cleanup / Close polish if PIE confirms bleed.  
- **Owner suggestion:** Lead Developer / Gameplay

---

## 2. Navigation QA (`navigation-qa-tester`)

**Verdict:** Pass with Observations (document / PE-018 spine).

| Check | Result |
|-------|--------|
| Room count / hub | 5–6 rooms; Lobby hub + Surveillance / Credential spurs — bible-aligned |
| Landmarks | Glass checkpoint, camera banks, console island, Soft Open silhouette — VDP-specified |
| Backtrack | Surveillance → Console intentional; not maze |
| Dead ends | SoftOpen stub intentional end-of-slice |
| Orientation | +Y North / +X East matches PE-017–020 |

### [OBSERVATION] — Modular security geo still placeholder-leaning

- **Evidence:** Deferred debt — real modular security dressing incomplete.  
- **Impact:** Landmark readability may be weaker than VDP intent in PIE.  
- **Recommendation:** Dressing polish mission / PE-022 prep — not a PE-021 blocker if navigation remains solvable.  
- **Owner suggestion:** Level / Tech Art

---

## 3. Horror QA (`horror-experience-tester`)

**Verdict:** Pass (design) / Conditions (PIE).

| Check | Result |
|-------|--------|
| Curve | Unease → Focus → Relief → Spike → Release — matches Design Plan §6 |
| Witness when/where | Post-solve Exit Approach only — Validate: hidden-until-power print |
| Fairness | Tension-only; does not brick clearance |
| No combat/chase | In scope |

### [MINOR] — Witness silhouette stand-in

- **Evidence:** Debt list — silhouette stand-in mesh.  
- **Impact:** Spike may read weak vs Research / Annex presence bar.  
- **Recommendation:** Accept as tagged debt; do not claim Production Ready art for Witness.  
- **Owner suggestion:** Horror / Tech Art

### [MAJOR] — Witness timing / fairness unconfirmed in EI

- **Evidence:** Technical only proves BeginPlay hide print; human must confirm no mid-solve pressure.  
- **Impact:** If Witness fires early, unfairness vs Bible §8.  
- **Recommendation:** Checklist steps 13–14 mandatory before Gameplay PASS.  
- **Owner suggestion:** EP / Horror

---

## 4. Puzzle QA (`puzzle-qa-tester`)

**Verdict:** Pass (Technical + bible family) / Conditions (human clarity).

| Check | Result |
|-------|--------|
| Family | Security & Access (§5.3) — credential + clearance console |
| Solution shape | Clue-backed CS-BADGE / CS-ZONE / CS-EXIT; not random glyph pad |
| Readable fail | Incomplete → Soft Open stays locked (Technical) |
| Independence | `bNotifyPowerOnSolve=false`; no generator `HasHandledPower` |
| Teaching | Distinct from fuse / fuel / coolant / Research Equipment |

### [OBSERVATION] — Coolant-valve parent UX on console stations

- **Evidence:** Simulate prints `[PE019] Coolant valve ready` on clearance consoles.  
- **Impact:** Debug noise; may break immersion if player sees PrintStrings.  
- **Recommendation:** Tag debt; optional Security-facing print override later.  
- **Owner suggestion:** Lead Developer

---

## 5. Storytelling QA (`environmental-storytelling-qa`)

**Verdict:** Pass (intent) / Conditions (PIE note copy).

| Check | Result |
|-------|--------|
| Notes A–E | Symptoms / residue intent documented |
| Env-first | VDP: tape, monitors, badge trays before mechanics |
| Canon | Checkpoint lockdown unfinished — no Restricted dump |
| Walkthrough risk | Design forbids directions; human must fail-check Note A/B |

### [MINOR] — Note copy not re-audited in this Review against live actors

- **Evidence:** Review used mission tables + VDP; no live note-text dump in MCP this pass.  
- **Impact:** Low if Implement followed symptoms-only brief; residual walkthrough risk until PIE.  
- **Recommendation:** During human PIE, fail if any note gives north/east route or “set CS-EXIT to HOLD” as tutorial.  
- **Owner suggestion:** Narrative / EP

---

## 6. Accessibility / Readability QA (`accessibility-readability-qa`)

**Verdict:** Conditions.

| Check | Result |
|-------|--------|
| Indoor lighting baseline | Directional reduced/hidden per Validate; PointLights present (MCP Gameplay/Lighting) |
| Prompts | Interaction + inventory patterns reused — debt PrintStrings possible |
| Color-only fail | Incomplete clearance should also keep exit locked (not color-only) |
| Hierarchy | Console island + gate as focus — document PASS |

### [MINOR] — Indoor lighting must hold under human flashlight / outdoor bleed check

- **Evidence:** Checklist fail if outdoor sun dominates.  
- **Impact:** Navigation / horror wash-out.  
- **Recommendation:** Confirm in PIE step 2 / pass criteria.  
- **Owner suggestion:** Tech Art / EP

---

## 7. Performance Risk Report (`performance-risk-analyzer`)

**Verdict:** Informational — risks only; no FPS claim.

| Risk | Level | Note |
|------|-------|------|
| PE-018 spine actor density | Low–Moderate | Familiar recipe; Story/Props SM actors present |
| Dynamic lights (PointLight ×4+) | Low–Moderate | Checkpoint mood; watch overlapping unshadowed costs |
| Nanite / modular geo | Observation | Dressing incomplete — future art may raise cost |
| Streaming | N/A | Soft Open Level travel, not multi-wing streaming |

No Critical performance blockers identified from docs/MCP folder inspection.

---

## 8. Regression Report (`regression-qa-tester`)

**Verdict:** Technical Pass / Conditions (manual Soft Open + independence).

| Predecessor | Check | Result |
|-------------|-------|--------|
| PE-020 Research | LabExit Soft Open → Security | Technical PASS (Validate) |
| PE-018 Annex | Generator `HasHandledPower` untouched | Document / Technical independence claim |
| PE-017A | Fuse ownership | Not duplicated |
| PE-019 Coolant | Valve / CoolantLoop as parent only | Thin children; no Coolant map ownership change |
| Soft Open chain | Maint → Annex → Coolant → Research → **Security** | Extended as designed |

### [OBSERVATION] — PE-020 Gameplay also historically PENDING_USER risk

- **Evidence:** Design Plan risk table noted PE-020 foundation honesty.  
- **Impact:** Campaign Soft Open feel may need Research + Security human pass together.  
- **Recommendation:** Optional paired Soft Open regression on Close.  
- **Owner suggestion:** EP / QA

### [OBSERVATION] — SliceReset full reverse is Technical-only until human Replay

- **Evidence:** `BP_SecurityWingReset` present (MCP); parent graphs claimed; manual PENDING_USER.  
- **Impact:** Incomplete reverse would false-claim Replay PASS.  
- **Recommendation:** Checklist steps 16–18 before Replay human PASS.  
- **Owner suggestion:** EP / Lead Developer

---

## 9. Consolidated Recommendations

**Must before Ready For Review YES / Complete Close**

1. EP Human Gameplay PASS (or written waiver) via playtest checklist.  
2. Manual Replay confirm SliceReset full reverse.  
3. Keep Ready For Review **NO** until (1).

**Should (non-blocking for Technical ship honesty)**

1. Override stale fuse `objectiveOnAvailable` on AccessClearance if PIE shows bleed.  
2. Confirm Witness only post-solve on exit path.  
3. Confirm Soft Open Research→Security continuity once in EI.

**Nice**

1. Security-facing PrintString overrides (drop Coolant valve ready noise).  
2. Modular security dressing + real audio.  
3. SoftOpenExit destination for PE-022 Signal / deeper sector.

---

## QA Lead gate honesty

| Gate | Status |
|------|--------|
| Compile | PASS |
| Technical | PASS |
| Gameplay | **PENDING_USER** |
| Replay | Technical PASS / **PENDING_USER** manual |
| Docs | PASS for Review package (this file + Production Review) |
| Ready For Review | **NO** (honest) |

**QA does not approve merge as Complete.** QA recommends: **Approve with Conditions** for documentation / Technical merge honesty; **block Ready For Review YES** until Gameplay closed.

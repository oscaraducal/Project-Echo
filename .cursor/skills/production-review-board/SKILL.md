---
name: production-review-board
description: Run a Project Echo Production Review Board across non-overlapping studio roles before approving a design plan or merging a mission. Use when reviewing PE-### work, Ready for Review gates, or when the user asks for production review / PRB.
---

# Production Review Board

Multi-role review against the Production Playbook and design bibles. Each role has **non-overlapping** duties — see `.cursor/agents/*.md`.

## When to use

- Design Plan approval  
- Mission Ready For Review / pre-merge  
- User asks for production review, PRB, or cross-discipline check  

## Inputs

- Mission brief / design plan / completion report  
- Changelog entry and affected docs  
- Playbook §4–§10  
- Relevant bible sections  

## Process

1. Confirm what is under review (plan vs implementation).  
2. For each role below, answer **only** that role’s questions (use agent briefs).  
3. Collect blockers vs suggestions.  
4. Verdict: **Approve** / **Approve with conditions** / **Reject** — with required fixes.  
5. EP owns final Ready / merge decision.

## Role checklist (no overlap)

| Role | Gate focus |
|------|------------|
| Executive Producer | Priority, scope size, schedule, Ready/merge |
| Creative Director | Tone, pillars, identity fit |
| Lead Developer | Architecture reuse, debt, compile/technical honesty |
| Gameplay Designer | Loop, family teaching, bible anti-patterns |
| Level Designer | Flow, room count, spatial teaching |
| Technical Artist | Lighting, dressing vs geo sink, ThirdParty policy |
| Horror Director | Tension curve, Witness fairness |
| Narrative Director | Symptoms vs exposition; world bible alignment |
| Audio Director | Real cues vs debt tags |
| QA Lead | Gate honesty, checklists, regression |

## Outputs

```text
# Production Review Board Report

Mission / Artifact: …
Verdict: Approve | Approve with conditions | Reject

Blockers:
- …

Conditions:
- …

Suggestions (non-blocking):
- …

EP decision needed: Yes / No
```

## Honesty rules

- Technical PASS does not satisfy Gameplay PASS.  
- Incomplete SliceReset fails Replay claims.  
- Placeholders must be tagged debt.

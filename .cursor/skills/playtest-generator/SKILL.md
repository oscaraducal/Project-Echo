---
name: playtest-generator
description: Generate a manual PIE / Enhanced Input playtest checklist for Project Echo missions. Use when preparing human Gameplay validation, EP QA checklists, or when Technical PASS is done but Gameplay PASS is still PENDING_USER.
---

# Playtest Generator

Produce a **manual PIE checklist** for Oscar (Executive Producer). Do not claim Gameplay PASS from automation.

## When to use

- Mission implementation finished Technical Simulate  
- User asks for playtest / PIE / QA checklist  
- Before Ready For Review when Gameplay is human-gated  

## Inputs

- Mission doc (PE-017 / PE-018 style)  
- Production Playbook §7  
- Map name and objective chain  

## Steps

1. Read mission validation section and loop.  
2. Build ordered steps covering spawn → observe → collect → solve → World Response → Witness (if any) → exit → SliceReset replay.  
3. Call out lighting baseline, symptoms-only notes, and input actions (Move, Interact, Flashlight).  
4. Mark what Technical already proved vs what human must confirm.  
5. Include Fail criteria (soft-lock, Witness during solve, incomplete reset, outdoor sun dominance).  

## Output template

```text
# Manual PIE Checklist — PE-###

Map: …
Estimated time: …

Preconditions: flashlight / IMC / spawn

Steps:
1. …
2. …

Witness (if applicable): …
SliceReset / Replay: …
Pass criteria: …
Fail / defer notes: …

Gameplay PASS owner: Executive Producer (Oscar)
Automation note: Enhanced Input cannot be fully driven by Slate/MCP — human required.
```

## References

- `Documents/05_Missions/PE-017-VerticalSlice01.md` (example checklist)  
- `Documents/05_Missions/PE-018-GeneratorAnnex.md`  
- Production Playbook §7  

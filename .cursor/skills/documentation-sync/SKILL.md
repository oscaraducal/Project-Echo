---
name: documentation-sync
description: Sync Project Echo documentation to match implemented truth after a mission or docs-only pass. Use when updating Changelog, mission notes, MasterIndex, README, systems docs, or when the user asks to align docs with the build.
---

# Documentation Sync

Keep documentation truthful, append-only where required, and aligned with the Production Playbook.

## When to use

- After implementation (with or without `mission-implementer`)  
- Docs-only missions / AI Studio infrastructure  
- User asks to update Changelog, health, roadmap, or indexes  

## Authority

- Playbook documentation standards  
- `.cursor/rules/documentation-standard.mdc`  
- Contribution Guide documentation workflow  

## Steps

1. Identify what actually changed (inspect or trust mission report — do not invent APIs).  
2. Update mission doc status / notes.  
3. **Append** `Documents/04_Production/Changelog.md` — never rewrite history.  
4. Update systems / flow / dependency docs only if ownership or APIs changed.  
5. Update `ProjectHealth.md` / `Roadmap.md` / `SprintHistory.md` when status changes.  
6. Update `Documents/README.md` and `MasterIndex.md` when new authoritative docs appear.  
7. Cross-link Playbook / AI Studio when process docs change.  
8. Verify Canon vs Recommendations remain separated.

## Outputs

- List of files updated  
- Changelog entry text  
- Note any PENDING_USER / debt left explicit  

## Anti-patterns

- Rewriting old Changelog sections  
- Documenting planned-but-unbuilt APIs as implemented  
- Claiming Gameplay PASS in docs without human validation  

# AI Studio — Hooks Policy

**Status:** Phase 1 — documentation only (no enabled project hooks)  
**Date:** 2026-07-25  

---

## Principle

Hooks are high-leverage and high-noise. Phase 1 **does not enable** `.cursor/hooks.json` automation.

Prefer:

1. Always-apply rules (`foundation`, `production-standard`)  
2. Skills invoked for mission workflows  
3. Explicit human PIE checklists  

---

## Recommended Future Hooks (not enabled)

| Hook | Idea | Risk | Recommendation |
|------|------|------|----------------|
| `sessionStart` | Inject short reminder: read Production Playbook + authority order | Low if ≤3 lines | Optional Phase 2 |
| `beforeSubmitPrompt` | Warn if user says “implement” without approved brief path | Medium false positives | Defer |
| `afterFileEdit` | Nudge Changelog on `Documents/**` edits | High noise | Avoid |
| `beforeShell` / git | Block commit of `.uasset` when mission is docs-only | Medium | Consider later with allowlist |
| Stop / completion | Auto-paste Mission Completion Report template | Medium | Prefer `mission-implementer` skill |

---

## If Enabling sessionStart Later

Keep the injected prompt minimal, for example:

```text
Project Echo: prefer ProductionPlaybook.md for process. Authority: Story → Gameplay Bible → Playbook → ADR → Mission Brief. Technical ≠ Gameplay PASS.
```

Do not dump entire bibles into the hook.

---

## Implementation Status

| Item | Status |
|------|--------|
| `.cursor/hooks.json` | **Not created** (intentional) |
| `.cursor/hooks/*` scripts | **Not created** |
| This policy doc | Active |

Revisit after 2–3 missions under the new rules/skills.

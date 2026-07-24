# AI Studio — Hooks Policy

**Status:** Phase 1–5 — documentation only (no enabled project hooks)  
**Date:** 2026-07-25  

---

## Principle

Hooks are high-leverage and high-noise. Phase 1 **does not enable** `.cursor/hooks.json` automation.

**Phases 2–5 (Creative, Previs, Mission Director, QA Studio) also do not enable hooks.** Production orchestration is skill-driven via Mission Director; QA is evaluate-only.

Prefer:

1. Always-apply rules (`foundation`, `mission-director`, `production-standard`)  
2. Mission Director + studio skills for production workflows  
3. Explicit human PIE checklists + QA Review Package on `Review Mission`  

**MCP Auto-accept is not a hook.** Commanded Implement / EP sticky `auto accept` is a docs + prompt-authorization policy ([MissionDirector/MCP-AutoAccept-Policy.md](MissionDirector/MCP-AutoAccept-Policy.md)). Do **not** enable hooks that auto-approve MCP without EP intent; Cursor Auto-run / MCP card Run stay EP UI actions.

---

## Recommended Future Hooks (not enabled)

| Hook | Idea | Risk | Recommendation |
|------|------|------|----------------|
| `sessionStart` | Remind Mission Director command vocabulary | Low if ≤3 lines | Optional Phase 5+ |
| `beforeSubmitPrompt` | Warn if “implement” without VDP | Medium false positives | Defer |
| `afterFileEdit` | Nudge Changelog on `Documents/**` edits | High noise | Avoid |
| `beforeShell` / git | Block commit of `.uasset` when mission is docs-only | Medium | Consider later with allowlist |
| Stop / completion | Auto-paste Mission Completion Report template | Medium | Prefer Director Close |

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

# Mission Director

**Status:** Active — AI Studio **v1.4**  
**Date:** 2026-07-25  
**Scope:** Architecture + Cursor skill / rule only (no Unreal / gameplay / Story Canon / hooks)  
**Parent:** [AI Studio README](../README.md) · [Production Playbook](../../ProductionPlaybook.md)  

---

## Purpose

The Executive Producer issues **high-level production commands**.

The **Mission Director** (orchestration layer) determines:

- which Skills are required  
- execution order  
- dependencies  
- approval gates  
- required deliverables  

EP should never manually orchestrate individual Skills.

---

## What it is / is not

| Is | Is not |
|----|--------|
| Single entry point for production missions | A creative / art skill |
| Command router + gate enforcer | A replacement for Playbook authority |
| Automatic skill selector | Permission to skip VDP or Story Canon |

**Skill:** `.cursor/skills/mission-director/SKILL.md`  
**Commands:** [CommandReference.md](CommandReference.md)  
**MCP Auto-accept:** [MCP-AutoAccept-Policy.md](MCP-AutoAccept-Policy.md)  
**Rule:** `.cursor/rules/mission-director.mdc` (always on for production orchestration default)

---

## Default behavior

Every Project Echo production conversation assumes Mission Director is active.

Preferred EP inputs:

```text
Start Mission PE-020
Continue Mission PE-020
Generate Visual Package PE-020
Implement Mission PE-020
Validate Mission PE-020
Review Mission PE-020
Close Mission PE-020
```

---

## Pipeline (full studio)

```text
EP Command
  → Mission Director
      → Production / Creative / Previs skills (auto)
      → STOP at gate
  → EP decision
  → next command
```

Integrates: Production Playbook · Creative Studio · Previsualization Studio · PRB agents.

---

## Repository

```text
Documents/04_Production/AIStudio/MissionDirector/
  README.md
  CommandReference.md
  MCP-AutoAccept-Policy.md
  Integration-CompletionReport.md
.cursor/skills/mission-director/SKILL.md
.cursor/rules/mission-director.mdc
.cursor/agents/mission-director.md    # Task-tool brief (optional mirror)
```

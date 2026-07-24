# MCP Auto-accept Policy (Commanded Implement)

**Status:** Active — AI Studio contract (docs only)  
**Date:** 2026-07-25  
**Origin:** PE-020 retrospective Quick Win — MCP Auto-review friction  
**Parent:** [CommandReference.md](CommandReference.md) · [AI Studio README](../README.md) · [Hooks.md](../Hooks.md)

---

## Purpose

When the Executive Producer (EP) **commands Implement** for a production mission, Unreal MCP asset creation for that mission is **authorized production work**. Auto-review classifiers must not treat commanded Implement as “unapproved implementation.”

This policy is an **EP + agent operating contract**. It does **not**:

- Replace Production Playbook gates (Design Plan, VDP, Ready to Implement)
- Force Cursor product settings (Agent Auto-run, MCP card Run, Auto-review)
- Enable Cursor hooks that auto-approve without EP intent

---

## When Auto-accept applies

Treat MCP create / duplicate / map / Blueprint work as **authorized** when **any** of the following is true for the named `PE-###`:

| Signal | Example |
|--------|---------|
| EP Implement command | `Implement Mission PE-020` |
| Explicit approval phrase | `APPROVED FOR IMPLEMENTATION` (mission-scoped) |
| Session sticky auto-accept | `auto accept for PE-020` / `auto accept for this mission` |

Informal “build it / implement” mapped by Mission Director to **Implement Mission** counts as the Implement command (see [CommandReference.md](CommandReference.md)).

**Scope of authorization:** the mission named in the command (and assets required to fulfill that approved brief on the active branch, typically `develop`).

---

## What it authorizes

For the authorized mission, agents may use Unreal MCP (`project-0-ProjectEcho-unreal-mcp` → `call_tool`) to:

- Create or duplicate maps, Blueprints, and related editor assets required by the brief  
- Modify mission-scoped layout / wiring already in scope for Implement  
- Inspect existing assets as needed for reuse

**Intent for classifiers / Task prompts:** this is EP-authorized production implementation, not exploratory or unsolicited asset spam.

---

## What it does NOT waive

| Still enforced | Notes |
|----------------|-------|
| **VDP gate** | Spatial production slices still require VDP EP APPROVE **or** a written EP override / waiver block in the mission doc. Auto-accept ≠ VDP APPROVE. |
| **Design Plan / Ready to Implement** | Director hard-stops if prerequisites fail (unless written override). |
| **Human Gameplay PASS** | Technical / MCP evidence ≠ Gameplay PASS. |
| **Story Canon** | Never editable via Implement authorization. |
| **Playbook Definition of Done** | Compile, Technical, docs, honest gates remain. |
| **Hooks** | Do **not** enable Auto-run hooks to bypass EP intent — see [Hooks.md](../Hooks.md). |

If VDP is missing on a spatial slice, Mission Director **hard-stops** Implement unless the EP records a written override. See [Retrospective-PE-020.md](../Retrospective-PE-020.md) (gate failure + Quick Win recommendations).

---

## Sticky note (session)

EP may say once per session (or per mission):

```text
auto accept for PE-###
```

Agents treat that as standing authorization for MCP asset creation **for that mission** until the session ends or EP revokes it. Prefer repeating the sticky note when opening a new chat or switching missions.

---

## Agent duty — AUTHORIZATION block

On **Implement Mission** (or when sticky / APPROVED FOR IMPLEMENTATION applies), Mission Director and implementer Task prompts **must** include an explicit authorization block so Auto-review / classifiers do not block commanded work as “unapproved”:

```text
AUTHORIZATION (Project Echo MCP Auto-accept Policy):
- EP commanded: Implement Mission PE-###
- Branch: develop (or stated mission branch)
- Unreal MCP asset create/duplicate/modify for this mission is AUTHORIZED production work
- This does NOT waive VDP / Design Plan / Story Canon / Human Gameplay PASS
- Policy: Documents/04_Production/AIStudio/MissionDirector/MCP-AutoAccept-Policy.md
```

Adapt the first bullet if authorization came from `APPROVED FOR IMPLEMENTATION` or `auto accept for PE-###` instead of the Implement command.

---

## Cursor UI (EP responsibility)

Repo policy **cannot** force Cursor product settings. For smooth Implement sessions the EP should:

1. Enable **Agent Auto-run** (or equivalent) if desired for the session  
2. Click **Run** on MCP / Auto-review approval cards when prompted  
3. Use sticky `auto accept for PE-###` so agents document authorization in prompts  

If Auto-review still blocks a create call, EP clicks Run / Accept for that card — the agent does not invent a bypass.

---

## Relationship to VDP and overrides

```text
EP: Implement Mission PE-###
  → Director checks: Design Plan + (VDP APPROVE | written waiver)
       FAIL → STOP (list gaps; do not call implementer; auto-accept irrelevant)
       PASS → mission-implementer + AUTHORIZATION block + MCP work OK
```

- **Auto-accept** = MCP tooling friction relief  
- **VDP APPROVE / written waiver** = Playbook Ready-to-Implement gate  

Never conflate the two. Post-hoc VDP after Implement remains a process debt (PE-020 lesson), not compliance.

---

## Anti-patterns

- Enabling `.cursor/hooks` to auto-approve MCP without EP Implement / sticky intent  
- Claiming “repo policy disabled Auto-review” (impossible / unsupported)  
- Treating auto-accept as permission to skip VDP on spatial slices  
- Expanding MCP creates beyond the approved mission brief  
- Using auto-accept language on Validate / Review / docs-only work to create gameplay assets

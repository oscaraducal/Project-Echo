# Gameplay & Puzzle Design Bible

**Status:** Active  
**Version:** 1.0  
**Mission:** PE-016  
**Authority:** Canonical gameplay specification  

---

## Authority Notice

This document is the **canonical gameplay specification** for Project Echo.

Beginning with **PE-017** and all subsequent gameplay missions:

- Mission designs, puzzle implementations, and gameplay features **must** align with this bible.
- Technical implementation truth remains in `Documents/02_Technical/` (especially `PuzzleFramework.md`, `GameplaySystems.md`, `GameplayFlow.md`).
- Narrative / world truth remains in `Documents/03_World/` and supporting design docs under `01_Game_Design/`.
- If a mission conflicts with this bible, resolve via an ADR in `Documents/00_Governance/DecisionLog.md` **before** implementation. Do not silently diverge.

Supporting design docs (`GameDesign.md`, `GameplayLoop.md`, `PuzzleBible.md`) remain valid primers; when detail conflicts, **this bible wins**.

---

## Figure 1 – Gameplay Philosophy Reference

![Figure 1 – Gameplay Philosophy Reference](Concept%20Art/Puzzle%20Design%20Overview.png)

**Figure 1 – Gameplay Philosophy Reference**

This image is the **intended gameplay vision / design reference** for Project Echo’s exploration–horror–puzzle identity.

It is **not**:

- UI or HUD mockup
- Level layout or map plan
- Environment concept art for production asset creation

Use it to communicate tone, pillar balance, and player fantasy when reviewing new missions against this bible.

---

## Cross-References (Do Not Duplicate)

| Domain | Canonical sources |
|--------|-------------------|
| Story / facility tone | `03_World/StoryBible.md`, `FacilityBible.md`, `RoomBible.md`, `NarrativeDesign.md` |
| High-level design primers | `GameDesign.md`, `GameplayLoop.md`, `PuzzleBible.md` |
| Puzzle implementation | `02_Technical/PuzzleFramework.md` (PE-015) |
| Implemented systems / flow | `GameplaySystems.md`, `GameplayFlow.md` |
| Blueprint standards | `BlueprintStandards.md`, `BlueprintArchitecture.md`, `ContributionGuide.md` |
| Health / process | `04_Production/ProjectHealth.md`, `Changelog.md` |

---

# 1. Gameplay Vision

## Identity

**Project Echo** is a first-person psychological horror experience set in the abandoned **Asterion Research Institute**, where the player investigates the aftermath of **Project Echo** while surviving the uncertain presence of **The Witness**.

The game is not an action shooter, stealth combat arena, or RPG. Capability grows through **knowledge, access, and understanding of the facility** — not stats, loot tiers, or skill trees.

## Genre Position

| Axis | Project Echo |
|------|----------------|
| Perspective | First-person |
| Core genres | Psychological horror, exploration, environmental narrative, grounded facility puzzles |
| Threat model | Uncertainty and pressure over constant chase or combat |
| Progression | Spatial access + systems literacy + story revelation |

## Player Fantasy

The player is an investigator inside a real workplace that has failed catastrophically. They should feel:

- **Curious** — every corridor and document might matter
- **Isolated** — help is absent; the facility is the only companion
- **Vulnerable** — light, fuel, keys, and quiet matter
- **Uneasy** — safety is never certain around The Witness
- **Rewarded for attention** — observation unlocks truth and progress

## Exploration Philosophy

Exploration is the primary verb. Rooms exist because Asterion needed them (see `FacilityBible.md`), not because the game needed a “puzzle room.” Layout teaches procedure: Engineering restores power; Security gates access; Research holds answers.

## Horror Philosophy

Horror is atmospheric and psychological first. The environment creates tension before enemies do. The Witness should produce **uncertainty**, not unfair instant failure or relentless pursuit. Survive is a loop stage — not a separate combat game mode.

## Narrative Philosophy

Story is discovered, not delivered in long exposition. Notes, room design, system states, and restricted access reveal what happened. Players are investigators who ask questions before answers arrive (`NarrativeDesign.md`).

## Puzzle Philosophy (Summary)

Puzzles are **facility operations problems** the player inherits: restore power, restore access, interpret research equipment, read procedures. If a challenge would not exist in a real institute, redesign it (expanded in §4–§5).

## Long-Term Vision

As systems expand (Witness AI, save, journal, multi-zone power, campaign levels), every new mechanic must reinforce the core loop in §3 rather than replace it. The bible scales by **families and standards** (§5, §10–§12), not by one-off mission logic.

---

# 2. Gameplay Pillars

Each pillar lists **Purpose**, **Player Experience**, **Design Intent**, and **Examples**.

## 2.1 Exploration

| | |
|--|--|
| **Purpose** | Make spatial discovery the engine of progress and story. |
| **Player Experience** | Freedom to move through believable zones; reward for leaving the obvious path. |
| **Design Intent** | Facility zones (Public, Admin, Medical, Engineering, Security, Research, Restricted) remain legible and purposeful. |
| **Examples** | Finding the Generator Room; discovering a maintenance bypass; noticing a dark wing that becomes reachable after power. |

## 2.2 Observation

| | |
|--|--|
| **Purpose** | Make careful looking and listening a skill, not a cutscene. |
| **Player Experience** | Clues are present in lighting, labels, notes, machinery states, and audio. |
| **Design Intent** | Puzzles and story beats should be solvable/readable via observation; avoid pixel hunting and pure trial-and-error. |
| **Examples** | Reading a maintenance note before fueling the generator; noticing emergency lights fail until power returns; hearing distant activity after World Response. |

## 2.3 Resource Management

| | |
|--|--|
| **Purpose** | Keep vulnerability tangible without inventory busywork. |
| **Player Experience** | Items enable access and systems — flashlight, keys, fuel, fuses — not filler loot. |
| **Design Intent** | Collectibles unlock gameplay (`GameplayLoop.md`). Future batteries/access cards follow the same rule. |
| **Examples** | Facility Key unlocks a door; Fuel Can starts the generator; Fuse completes a panel (`BP_FusePuzzle`). |

## 2.4 Psychological Tension

| | |
|--|--|
| **Purpose** | Sustained unease without cheap deaths or opaque rules. |
| **Player Experience** | Never fully safe; never certain what The Witness will do next. |
| **Design Intent** | Pressure reacts to player progress and noise/attention; it must not erase solvable logic (§8). |
| **Examples** | Horror corridor as pressure space; distant activity hints after power; future Witness presence that interrupts but does not brick puzzles. |

## 2.5 Environmental Storytelling

| | |
|--|--|
| **Purpose** | Deliver narrative through space and residue of work life. |
| **Player Experience** | Rooms feel lived-in then abandoned; documents sound like staff wrote them. |
| **Design Intent** | Every meaningful object serves gameplay or story (`GameDesign.md`). Avoid decorative-only clutter that pretends to be interactive. |
| **Examples** | Note pickup → objective; powered doors and ventilation after generator; research chambers that show procedure, not set dressing alone. |

## 2.6 Meaningful Progression

| | |
|--|--|
| **Purpose** | Make player actions change the world and deepen understanding. |
| **Player Experience** | Solving something opens space, updates objectives, restores systems, reveals story. |
| **Design Intent** | Not an RPG. Progress = knowledge + access + story + environmental change. |
| **Examples** | Generator → PowerManager World Response; fuse solve → objective + tagged light; unlocking Restricted after Security puzzles. |

---

# 3. Core Gameplay Loop

Canonical loop for design (implementation mapping in `GameplayFlow.md`):

```text
Explore → Discover → Understand → Solve → Restore Progress → Reveal Story → Survive → (repeat)
```

Alignment with primer docs: Explore / Observe / Interact / Collect map into **Explore–Discover–Understand**; Solve / Progress map into **Solve–Restore Progress**; then **Reveal Story** and **Survive**.

### Explore

| | |
|--|--|
| **What** | Move through unfamiliar facility space; learn layout. |
| **Why** | Spatial literacy is the player’s primary power. |
| **Emotion** | Curiosity, caution. |
| **Transition** | A new room, locked gate, or anomaly → Discover. |

### Discover

| | |
|--|--|
| **What** | Find objects, notes, machines, routes, threats, or system failures. |
| **Why** | Discovery feeds both puzzle and narrative pipelines. |
| **Emotion** | Recognition, mild dread. |
| **Transition** | Player has a thing or clue → Understand. |

### Understand

| | |
|--|--|
| **What** | Interpret procedures, inventory needs, power/security state, story implications. |
| **Why** | Understanding replaces guessing; matches facility ops fantasy. |
| **Emotion** | Focus, growing competence. |
| **Transition** | Clear next action → Solve. |

### Solve

| | |
|--|--|
| **What** | Apply items, interactions, or multi-step system logic to resolve a facility problem. |
| **Why** | Solving is how the institute becomes traversable again. |
| **Emotion** | Tension → relief / accomplishment. |
| **Transition** | Success hooks fire → Restore Progress. |

### Restore Progress

| | |
|--|--|
| **What** | World response: doors, lights, objectives, power, access, save-worthy state. |
| **Why** | The world must visibly acknowledge the player. |
| **Emotion** | Agency, momentum. |
| **Transition** | New information or space → Reveal Story (and/or next Explore). |

### Reveal Story

| | |
|--|--|
| **What** | Notes, environmental change, audio, character residue, restricted lore. |
| **Why** | Story is the reward for competent investigation. |
| **Emotion** | Unease + fascination. |
| **Transition** | Deeper into danger or mystery → Survive / Explore. |

### Survive

| | |
|--|--|
| **What** | Manage risk: light, noise, resources, Witness pressure, dark routes. |
| **Why** | Survival keeps horror continuous without splitting into a combat game. |
| **Emotion** | Vulnerability, alertness. |
| **Transition** | Safe enough to continue → Explore again. |

**Implemented M1 slice (technical):** Spawn → Move → Interact → Collect → Generator/Power → Objectives → Proceed — plus PE-015 Fuse station. Design loop above is the target for PE-017+ campaign work.

---

# 4. Puzzle Philosophy

## Believable Facility Operations

Every puzzle must answer:

> **Why would this exist in a real research facility?**

Asterion puzzles should feel like interrupted work: incomplete maintenance, security lockout, research equipment left mid-procedure, signal routing, environmental hazards tied to building systems.

## Design Affirmatives

- Clues live in notes, labels, whiteboards, logs, room layout, machine state.
- Difficulty grows via **interconnected systems**, not obscure logic.
- Solutions teach how the facility works (power, security, research networks).
- Player reward includes access, story, and clearer mental model of Asterion.

## Anti-Patterns (Forbidden Without ADR)

| Anti-pattern | Why it fails Project Echo |
|--------------|---------------------------|
| Random symbols / alien glyph pads with no in-world language | Breaks grounded institute tone |
| Arbitrary button sequences with no procedure or label trail | Trial-and-error, not observation |
| Puzzle-for-sake-of-puzzle rooms | Facility stops feeling real |
| Pixel hunting / invisible hotspots | Punishes exploration fairness |
| Logic that The Witness must “solve for” the player | Violates §8 |
| Stat checks / RPG skill gates | Conflicts with progression philosophy |
| Combat as puzzle resolution | Wrong genre fantasy |

If a design needs an anti-pattern for a deliberate story beat, document an ADR and scope the exception tightly.

---

# 5. Puzzle Families

All new puzzles should classify into a family. Implementation extends `BP_PuzzleBase` / `BPI_Puzzle` (PE-015) unless an ADR justifies otherwise.

## 5.1 Electrical

| Field | Content |
|-------|---------|
| **Design goals** | Restore or reroute power as believable engineering work. |
| **Example gameplay** | Insert fuse; flip breakers in labeled order; restore subpanel after reading maintenance log. |
| **Blueprint relationship** | Child of `BP_PuzzleBase`; may use `BPC_Inventory` (e.g. Fuse); on solve use `WorldResponseTargets` / `BPI_PowerReceiver` and optional `BP_PowerManager.NotifyPuzzlePowerResponse` (independent of generator `HasHandledPower`). Example: `BP_FusePuzzle` + `BP_FusePickup`. |
| **Player reward** | Lights, powered doors, new routes, objective update, story of “systems coming back.” |
| **Future expansion** | Multi-zone grids, overload/fail states, sequenced panel puzzles across Engineering. |

## 5.2 Mechanical

| Field | Content |
|-------|---------|
| **Design goals** | Physical facility hardware: valves, vents, lifts, sealed hatches. |
| **Example gameplay** | Align duct dampers; release a mechanical lock after clearing pressure; restore ventilation path. |
| **Blueprint relationship** | `BP_PuzzleBase` child; often `BPI_Interactable` via interactable composition; may call power/objective hooks; may trigger `BP_VentilationUnit`-style receivers or custom world actors. |
| **Player reward** | Alternate routes, safer paths, environmental storytelling (air returns, machines wake). |
| **Future expansion** | Multi-step machine assemblies; timed mechanical sequences that remain fair and clue-backed. |

## 5.3 Security & Access

| Field | Content |
|-------|---------|
| **Design goals** | Believable checkpoints, credentials, and lockouts. |
| **Example gameplay** | Key/card door (`BP_LockedDoor` pattern); security console unlock after finding procedure; camera/lockdown clear. |
| **Blueprint relationship** | May start as interactable + inventory gate; graduate to `BP_PuzzleBase` when multi-state. Use `BPC_Inventory` (`HasItem` / `RemoveItem`), `BPC_Objective`, optional power dependency (`BP_PoweredDoor`). |
| **Player reward** | New zones (Security → Restricted), story densification, rising stakes. |
| **Future expansion** | Access cards, biometric fantasy grounded in institute tech, cascading lockdown clears. |

## 5.4 Research Equipment

| Field | Content |
|-------|---------|
| **Design goals** | Interact with Project Echo apparatus as incomplete science, not arcade minigames. |
| **Example gameplay** | Calibrate observation gear using logged parameters; power a chamber and interpret output; reconstruct a test sequence from notes. |
| **Blueprint relationship** | `BP_PuzzleBase` with rich `PuzzleID` / state; objectives via `BPC_Objective`; story via notes (`BP_NotePickup` / future journal); avoid combat. |
| **Player reward** | Core mystery fragments, character insight, endgame understanding. |
| **Future expansion** | Multi-room research chains; data-center coupling with Signal family. |

## 5.5 Signal & Communication

| Field | Content |
|-------|---------|
| **Design goals** | PA, radios, network terminals, and signal routing as facility ops. |
| **Example gameplay** | Restore PA circuit; align antenna/relay; decrypt only when grounded in found codes/logs (no random crypto). |
| **Blueprint relationship** | `BP_PuzzleBase`; world response may hit `BP_PASpeaker` / future signal actors via `BPI_PowerReceiver` or dedicated interfaces; audio feedback preferred. |
| **Player reward** | Narrative audio, distant activity, coordinated facility “voice,” tension spikes. |
| **Future expansion** | Cross-zone signal graphs; false/misleading broadcasts as horror (still solvable via observation). |

## 5.6 Environmental Observation

| Field | Content |
|-------|---------|
| **Design goals** | Pure observation puzzles — no arbitrary machines. |
| **Example gameplay** | Match room state to a note; follow physical trail; deduce route from damaged signage and lighting. |
| **Blueprint relationship** | May be lightweight: notes + `BPC_Objective` + door unlock without full puzzle actor; when stateful, still prefer `BP_PuzzleBase` for save/`PuzzleID`. |
| **Player reward** | Mastery fantasy (“I read the building”); soft skill pride. |
| **Future expansion** | Journal-assisted clue collation; multi-room observation arcs. |

## 5.7 Resource Integration

| Field | Content |
|-------|---------|
| **Design goals** | Combine inventory, power, access, and observation into one coherent ops problem. |
| **Example gameplay** | Fuel generator (existing loop) then use restored power to complete a fuse/security chain; late-game multi-system restores. |
| **Blueprint relationship** | Orchestrate existing systems: `BPC_Inventory`, `BP_Generator` / `BP_PowerManager`, `BP_PuzzleBase` children, objectives — compose, don’t fork parallel frameworks. |
| **Player reward** | Peak agency; facility feels like one machine. |
| **Future expansion** | Campaign “systems literacy” finales; optional failure states that teach without soft-locking unfairly. |

---

# 6. Puzzle Progression

Difficulty scales by **system interconnection**, not cryptic nonsense.

| Phase | Player skill | Puzzle shape | Example direction |
|-------|--------------|--------------|-------------------|
| **Early** | Learn verbs | Single interaction or one item gate | Flashlight, note, key, simple door, first generator |
| **Mid** | Combine systems | Multi-step objectives across rooms | Fuel → power → proceed; fuse panel; security + inventory |
| **Late** | Facility literacy | Interconnected Electrical + Security + Research | Zone power + access cards + research calibration |
| **Endgame** | Synthesis | Resource Integration across institute systems | Networked restores that unlock final narrative truth / escape motivation |

**Motivation arc** (from `GameplayLoop.md`): Curiosity → Understanding → Escape.

---

# 7. Horror Integration

## Tension Without Unfairness

| Do | Don’t |
|----|-------|
| Use darkness, audio, distant activity, incomplete systems | Soft-lock players with no clue path |
| Interrupt with Witness pressure after clear rules of engagement | Kill/reset progress without telegraph |
| Make restored power feel double-edged (more light, more attention) | Randomize puzzle solutions per death |
| Keep fail states readable (`FailPuzzle` when used) | Hide required items in unfair pixel hunts |

Horror should **raise stakes** around a still-solvable problem. Observation remains viable under stress.

---

# 8. The Witness Design Rules

The Witness is the primary psychological threat (`StoryBible.md`). For gameplay design:

1. **Reacts / pressures** — presence, noise response, path denial, attention tax.
2. **Never replaces solvable logic** — the player must still be able to complete facility ops through observation and correct procedure.
3. **Unpredictable ≠ unfair** — uncertainty of *when*, not *whether rules exist*.
4. **Does not invent puzzle answers** — no possession of UI, no auto-solving, no mandatory chase that skips clue space without alternative.
5. **Integrates into Survive** — Witness beats feed the loop; they are not a separate win condition that voids puzzle families.

Future Witness AI missions must cite this section and PE-016 when specifying encounter rules.

---

# 9. Blueprint Mapping

Technical detail: `PuzzleFramework.md` (PE-015). Design → implementation map:

```text
Puzzle Family (this bible)
  → Child of BP_PuzzleBase (Actor) implementing BPI_Puzzle
  → Optional BPI_Interactable / BP_InteractableBase for interaction
  → BPC_Inventory / BPC_Objective via GetComponentByClass (no Character cast)
  → Power: WorldResponseTargets (BPI_PowerReceiver) + optional NotifyPuzzlePowerResponse
  → Save-ready fields on base (PuzzleID, CurrentState, bSolved, …) — save system later
  → Audio / VFX as feedback layers — never as sole solution channel
```

| Concern | Blueprint / asset | Design rule |
|---------|-------------------|-------------|
| Contract | `BPI_Puzzle` | Activate / Deactivate / IsSolved / ResetPuzzle / GetPuzzleState / GetPuzzleID |
| Lifecycle | `E_PuzzleState`, `BP_PuzzleBase` | Idle→Available→Activated→InProgress→Solved→Completed |
| Example | `BP_FusePuzzle`, `BP_FusePickup`, `BP_PuzzleResetButton` | Electrical family reference implementation |
| Hub (optional) | `BP_PuzzleManager` | Listen / dispatch; do not hardcode family logic |
| Objectives | `BPC_Objective`, `WBP_Objective` | Configure `ObjectiveOnAvailable` / `ObjectiveOnSolved` |
| Power | `BPI_PowerReceiver`, `BP_PowerManager` | Puzzle path ≠ generator `HasHandledPower` once-only path |
| Inventory | `BPC_Inventory`, `ST_InventoryItem` | Items unlock ops; naming per ContributionGuide |
| Interaction | `BPC_Interaction`, `BPI_Interactable` | Prefer interface messaging |
| Save (planned) | `BP_SaveGame`, `BP_GameInstance` | Persist puzzle fields when Save ships |
| Audio / VFX | future `SC_*` / `NS_*` | Feedback and horror; not cryptic required signals without clues |
| Validation | `LV_TestingGround`, `BP_DevSandboxValidator` | Sandbox before campaign |

Naming: `BP_*`, `BPC_*`, `BPI_*`, `ST_*`, `E_*`, `WBP_*` per `ContributionGuide.md` / `BlueprintStandards.md`.

---

# 10. Gameplay Expansion Guide

When adding a puzzle or gameplay feature (PE-017+):

1. **Cite this bible** in the mission brief (family + pillar + loop stage).
2. **Prefer inheritance / composition** from `BP_PuzzleBase` and existing `BPC_*` / `BPI_*` — do not spawn parallel frameworks.
3. **Update docs**: `PuzzleFramework.md` (if contract changes), `GameplaySystems.md` / `GameplayFlow.md` (if implemented behavior changes), Changelog entry.
4. **Validate** on `LV_TestingGround` (or successor sandbox) before campaign placement; include reset/repeat path where appropriate.
5. **Regression**: preserve generator World Response independence from puzzle power hooks; preserve IMC / interaction contracts.
6. **Standards**: BlueprintStandards + ContributionGuide naming; no mission IDs in asset names.
7. **Consistency**: tone matches Asterion / Project Echo; anti-patterns require ADR.
8. **Conflicts**: DecisionLog ADR; then update this bible if the canon intentionally changes.

---

# 11. Future Puzzle Catalogue

Backlog **references only** — not scheduled commitments. Grouped by family for PE-017+ planning.

| Family | Catalogue seeds (design refs) |
|--------|-------------------------------|
| Electrical | Subpanel sequencing; battery bus restore; emergency override that still needs labeled procedure |
| Mechanical | Valve network; elevator/car lift interlock; pressure door after vent clear |
| Security & Access | Tiered keycards; surveillance clear; armory lock (late) |
| Research Equipment | Chamber calibration; sample containment handshake; observation window protocol |
| Signal & Communication | PA zone restore; relay alignment; “echo” signal that is diegetic, clue-backed |
| Environmental Observation | Multi-note triangulation; damage-trail routing; lights-as-language (diegetic only) |
| Resource Integration | Mid-game power+security chain; late-game institute-wide restore sequence |

Campaign placement belongs in Roadmap / mission docs; this table is the design backlog index.

---

# 12. Gameplay Design Rules

Permanent standards — violations need ADR:

1. **This bible is canonical** for gameplay design from PE-017 onward.
2. **Facility realism first** — puzzles are operations problems.
3. **Observation over guessing** — clues exist in-world.
4. **No anti-patterns** from §4 without ADR.
5. **Pillars over novelty** — new mechanics must serve §2.
6. **Loop integrity** — features reinforce §3; they do not replace it.
7. **Witness pressures, never replaces logic** (§8).
8. **Horror stays fair** (§7).
9. **Extend PE-015 framework** — families map to `BP_PuzzleBase` / interfaces / components in §9.
10. **Compose existing systems** — Inventory, Objectives, Power, Interaction, Save hooks.
11. **Progression is knowledge and access**, not RPG stats.
12. **Every interaction matters** — gameplay or story (or both).
13. **Information is a reward** — exploration yields lore and clarity.
14. **Atmosphere before action** — environment leads tension.
15. **Docs track truth** — update technical docs when implementation changes; do not fork silent design canon.
16. **Sandbox before campaign** — prove puzzles on testing maps.
17. **Naming and architecture standards** are mandatory.
18. **Tone** — isolated, scientific, grounded, mysterious; avoid melodrama and horror clichés that break Asterion.

---

## Document Control

| | |
|--|--|
| Created | PE-016 |
| Owners | Design + Technical alignment |
| Review gate | Gameplay missions PE-017+ must reference this file |
| Related image | `Concept Art/Puzzle Design Overview.png` (Figure 1) |

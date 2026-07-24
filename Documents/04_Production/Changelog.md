# Changelog

---

## PE-021 — Implement Security Wing
**Date:** 2026-07-25
**Mission:** PE-021 Security Wing
**Branch:** `develop`

### Added

- Map `/Game/ProjectEcho/Maps/Production/LV_ARI_SecurityWing` (PE-018 recipe from Research Wing)
- `BP_AccessClearancePuzzle` (thin CoolantLoop child) — Security & Access teaching beat
- `BP_ClearanceConsoleStation` (thin CoolantValve child) — CS-BADGE / CS-ZONE / CS-EXIT
- `BP_SecurityWingReset` (CoolantBayReset child) — SliceReset
- Staff Keycard pickup + Lobby `BP_LockedDoor` gate
- SoftOpenExit stub on Security exit approach
- `Documents/05_Missions/PE-021-SecurityWing.md`, `PE-021-PlaytestChecklist.md`

### Changed

- Research Wing `LabExit` → `BP_SoftOpenExit` (`SoftOpenLevelName=LV_ARI_SecurityWing`, `bTravelOnOpen=true`)
- Design Plan → APPROVED & IMPLEMENTED; VDP note implemented; Roadmap Soft Open chain extended
- Indoor DirectionalLight intensity reduced / hidden on Security map

### Validation

- Compile PASS; MapCheck 0/0; Technical Simulate PASS (PuzzleBase ready, consoles ×3, SoftOpen locked, Witness hidden-until-power)
- Gameplay **PENDING_USER** — human EI checklist required
- Replay Technical PASS (SliceReset present); manual reverse PENDING_USER

### Notes

- Cuts honored: no Signal/PA second puzzle, Armory, Restricted, fuse/generator/coolant/research redo, combat/chase
- Next gate: `Validate Mission PE-021` / human PIE

---

## PE-021 — Visual Design Package (Security Wing)
**Date:** 2026-07-25
**Mission:** PE-021 Security Wing
**Branch:** `develop`

### Added

- `Documents/05_Missions/PE-021-VisualDesignPackage.md` — full VDP (8 sections + EP checklist + Approval Block)

### Changed

- `PE-021-DesignPlan.md` — proceeded to Previs; VDP linked; Ready to Implement remains **NO** until EP VDP APPROVE

### Notes

- Docs-only Previs — no Unreal maps / Blueprints / MCP asset creation
- Gate: STOP — waiting for EP VDP APPROVE / RETURN TO DESIGN
- Next: `Implement Mission PE-021` only after APPROVE (MCP Auto-accept applies at Implement)

---

## AI Studio Phase 5 — QA Studio
**Date:** 2026-07-25
**Mission:** AI Studio Phase 4 — QA Studio (brief) / Phase 5 · v1.5
**Branch:** `develop`

### Added

- `Documents/04_Production/AIStudio/QAStudio/` — README, QAReviewPackage, SkillRelationships, Phase5-CompletionReport
- QA Cursor skills (flat): gameplay-qa-tester, navigation-qa-tester, horror-experience-tester, puzzle-qa-tester, environmental-storytelling-qa, accessibility-readability-qa, performance-risk-analyzer, regression-qa-tester
- `.cursor/rules/qa-studio.mdc`

### Changed

- AI Studio → **v1.5**; README QA skills map
- Production Playbook → **v1.5**: lifecycle QA before PRB; §12e
- Mission Director `Review Mission` — QA Review Package then PRB
- `production-review-board` / `qa-lead` — consume QA package
- MigrationPlan / Hooks / indexes / legacy AIStudio.md

### Notes

- Docs + Cursor OS only — no Unreal, Blueprints, Story Canon, Hooks, or fix implementation
- QA evaluates and reports; designers/EP decide
- Brief titled Phase 4; sequenced after Mission Director as Phase 5 / v1.5

---

## PE-020 — Close Mission (Research Wing)
**Date:** 2026-07-25
**Mission:** PE-020 Research Wing
**Branch:** `develop`

### Changed

- `PE-020-ResearchWing.md` — Status **Closed — Technical** (Gameplay **PENDING_USER**); Completion Report; lessons pointer
- Design Plan / VDP / Playtest checklist — archived with Close; status fields consistent
- `ProductionPlaybook.md` §11 — PE-020 durable lessons (VDP before Implement; MCP Auto-accept policy)
- `ProjectHealth.md` / `Roadmap.md` / `SprintHistory.md` — PE-020 Closed with open Gameplay debt
- `Retrospective-PE-020.md` — mission Closed status mirrored

### Notes

- Do **not** claim Human Gameplay PASS — none declared at Close; EP may reopen `Validate Mission PE-020`
- Post-hoc VDP remains process debt (not pre-implement gate compliance)
- Docs-only Close — no Blueprint/map changes

---

## Docs — MCP Auto-accept Policy (PE-020 Quick Win)
**Date:** 2026-07-25
**Mission:** PE-020 retrospective Quick Win (docs)

### Added

- `Documents/04_Production/AIStudio/MissionDirector/MCP-AutoAccept-Policy.md` — EP + agent contract: commanded Implement / sticky auto-accept authorizes Unreal MCP asset creation; does not waive VDP, Story Canon, or Human Gameplay PASS

### Changed

- `.cursor/skills/mission-director/SKILL.md` — Implement Mission MCP authorization + Task AUTHORIZATION block template
- `.cursor/skills/mission-implementer/SKILL.md` — MCP create in-scope under EP Implement / auto accept
- `AIStudio/README.md`, `MissionDirector/CommandReference.md`, `MissionDirector/README.md`, `Hooks.md`, `ProductionPlaybook.md` — pointers (hooks remain disabled)

### Notes

- Policy cannot force Cursor Auto-run / Auto-review product settings; EP still enables Auto-run / clicks Run on MCP cards
- Does **not** enable Cursor hooks that auto-approve without EP intent

---

## PE-020 — AI Studio Production Retrospective
**Date:** 2026-07-25
**Mission:** PE-020 Research Wing (process)

### Added

- `Documents/04_Production/AIStudio/Retrospective-PE-020.md` — recommendations only for AI Studio v1.5 (no rules/skills/Unreal changes)

### Notes

- Gate failures recorded: VDP after Implement; MCP Auto-review friction; Gameplay PENDING_USER
- Do **not** implement from this retrospective until a separate framework/docs mission is commanded

---

## PE-020 — Validate (Technical + Human PIE Checklist)
**Date:** 2026-07-25
**Mission:** PE-020 Research Wing
**Branch:** `develop`

### Added

- Human PIE checklist: `Documents/05_Missions/PE-020-PlaytestChecklist.md`

### Changed

- `PE-020-ResearchWing.md` Validation: MCP technical re-check evidence; gates Compile/Technical PASS; Gameplay **PENDING_USER**; Ready for Review NO until human PIE

### Notes

- Technical re-check PASS (map, GameMode, Soft Open Coolant→Research, ST-* stations, LabExit locked pre-solve, Witness hidden-until-power print, SliceReset present, MapCheck 0/0)
- Do **not** claim Gameplay PASS without EP Enhanced Input walkthrough

---

## PE-020 — Research Wing (Post-Coolant Laboratory)
**Date:** 2026-07-25
**Mission:** PE-020 Research Wing
**Branch:** `develop`

### Added

- Production map `/Game/ProjectEcho/Maps/Production/LV_ARI_ResearchWing`
- Twin assets: `BP_ContainmentCalibrationPuzzle`, `BP_CalibrationStation`, `BP_ResearchWingReset` (Research Equipment family prep)
- Design Plan + mission notes: `PE-020-DesignPlan.md`, `PE-020-ResearchWing.md`
- Soft Open: Coolant Bay `SoftOpenExit_Research` → `LV_ARI_ResearchWing`

### Changed

- Coolant Bay exit Soft Open destination wired to Research Wing (supersedes Security stub for campaign travel)
- Research map narrative/notes/station IDs (ST-TEMP / ST-SEAL / ST-LINK) on reused CoolantLoop/Valve instances

### Notes

- Technical Simulate PASS; Gameplay PASS **PENDING_USER** (Enhanced Input)
- No combat / chase / Security / fuse fork / inventory redesign
- Replay via SliceReset (CoolantBayReset instance); ResearchWingReset twin cutover debt tagged in mission notes

---

## AI Studio Phase 4 — Mission Director Integration
**Date:** 2026-07-25
**Mission:** AI Studio Mission Director Integration
**Branch:** `develop`

### Added

- `Documents/04_Production/AIStudio/MissionDirector/` — README, CommandReference, Integration-CompletionReport
- `.cursor/skills/mission-director/SKILL.md` — permanent production orchestration entry
- `.cursor/rules/mission-director.mdc` — always-on Director default
- `.cursor/agents/mission-director.md` — Task-tool orchestration brief

### Changed

- AI Studio → **v1.4**; README EP commands + orchestration skill map
- Production Playbook → **v1.4**: lifecycle EP→Director; §12d Mission Director
- MigrationPlan / foundation / EP agent — command vocabulary; no manual skill orchestration
- Documents README / MasterIndex / legacy AIStudio.md pointers

### Notes

- Docs + Cursor OS only — no Unreal, gameplay, Story Canon, or Hooks changes
- EP issues high-level commands; Director selects skills and stops at gates

---

## AI Studio Phase 3 — Previsualization Studio
**Date:** 2026-07-25
**Mission:** AI Studio Phase 3 (Previsualization Studio)
**Branch:** `develop`

### Added

- `Documents/04_Production/AIStudio/PrevisualizationStudio/` — README, VisualDesignPackage, SkillRelationships, Phase3-CompletionReport
- Previs Cursor skills (flat): experience-designer, blockout-visualizer, storyboard-designer, concept-artist, lighting-visualizer, asset-placement-designer
- `.cursor/rules/previs-studio.mdc` — VDP gate pointer for mission docs

### Changed

- AI Studio → **v1.3**; README skills map + pipeline
- Production Playbook → **v1.3**: lifecycle 2c/2d + §12c Previs; permanent VDP before implement
- MigrationPlan / Hooks — Phase 3 delivered; hooks remain disabled
- `executive-producer` agent — VDP mental-play checklist
- Documents README / MasterIndex / legacy AIStudio.md pointers
- `mission-planner` / `mission-implementer` — VDP gate awareness

### Notes

- Docs + Cursor workflow only — no maps, Blueprints, gameplay, Story Canon, assets, or image generation
- EP approves player experience (mental play), not text alone
- Applies to future production missions; PE-019 landed before this standard

---

## PE-019 — Coolant Bay (Post-Power Mechanical)
**Date:** 2026-07-25
**Mission:** PE-019
**Branch:** `develop`

### Added

- `LV_ARI_CoolantBay` — production map (PE-018 recipe; ≤5 rooms; Tool Spur cut)
- `BP_CoolantLoopPuzzle` — thin Mechanical `BP_PuzzleBase` child (valve-state `MarkSolved` + World Response)
- `BP_CoolantValve` — labeled valve interactables (V-12 / V-19 / V-27 target states)
- `BP_CoolantBayReset` — full SliceReset twin (hatch / SoftOpen / lights / Witness / ambient / notes / objectives / valves / puzzle)
- `BP_SoftOpenExit` — PoweredDoor child; Soft Open Level on successful open
- Mission notes: `Documents/05_Missions/PE-019-CoolantBay.md`

### Changed

- `LV_ARI_GeneratorAnnex` Powered Exit → Soft Open to `LV_ARI_CoolantBay`
- `LV_ARI_MaintenanceWing` Locked Exit → Soft Open to `LV_ARI_GeneratorAnnex` (PE-018 travel debt)
- PE-019 Design Plan → APPROVED & IMPLEMENTED
- ProjectHealth / Roadmap / SprintHistory / PuzzleFramework updated for Mechanical teaching beat

### Notes

- Technical PASS (PIE); Gameplay PASS **PENDING_USER** (Enhanced Input)
- Audio / Witness mesh / stuck gauges tagged as PrintString / BasicShapes debt
- No Security / fuse fork / generator redo; generator `HasHandledPower` path untouched

---

## AI Studio Phase 2 — Creative Studio
**Date:** 2026-07-25
**Mission:** AI Studio Phase 2 (Creative Studio)
**Branch:** `develop`

### Added

- `Documents/04_Production/AIStudio/CreativeStudio/` — README, AssetCreationPipeline, SkillRelationships, Phase2-CompletionReport
- Creative Cursor skills (flat): asset-creation-planner, ai-asset-coordinator, mesh-designer, environment-designer, facility-designer, prop-designer, lighting-designer, audio-designer, environmental-storytelling-designer, cinematic-designer, performance-designer
- `.cursor/rules/creative-studio.mdc` — scoped Asset Creation Hierarchy pointer

### Changed

- AI Studio → **v1.2**; README skills map + repository architecture (flat skills)
- Production Playbook → **v1.2**: lifecycle step 2b + §12b Creative Studio; permanent asset hierarchy
- MigrationPlan / Hooks — Phase 2 Creative delivered; hooks remain disabled
- Documents README / MasterIndex / legacy AIStudio.md pointers

### Notes

- Docs + Cursor workflow only — no maps, Blueprints, gameplay systems, or Story Canon changes
- Asset hierarchy permanent: Reuse → Fab → Quixel → Meshy → Blender → Custom

---

## FRAMEWORK-001 — AI Studio v1.0 Validation
**Date:** 2026-07-25
**Mission:** FRAMEWORK-001
**Branch:** `develop`

### Added

- `Documents/04_Production/AIStudio/ValidationReport-FRAMEWORK-001.md` — architecture grade B+; YES WITH MINOR CHANGES; upgrade label to AI Studio v1.1

### Changed

- Production Playbook → v1.1: explicit Lessons→Playbook step; PRB vs Human PIE order clarity
- AIStudio README / Documents README / MasterIndex — link Validation Report
- Legacy `AIStudio.md` — Technical Director ↔ Design/Tech guidance naming map
- `DevelopmentBible.md` — workflow points at Playbook as authoritative lifecycle

### Notes

- Docs-only validation; hooks remain disabled; no Blueprints / maps / Story changes
- Final recommendation: YES WITH MINOR CHANGES; keep 10 agents with tiered PRB invocation later

---

## AI Studio Phase 1 — Production Playbook + Cursor Workflow
**Date:** 2026-07-25
**Mission:** AI Studio Phase 1
**Branch:** `develop`

### Added

- `Documents/04_Production/ProductionPlaybook.md` — authoritative production process (PE-017 / PE-017A / PE-018 lessons; DoD; human PIE; PRB; reference recipes)
- `Documents/04_Production/AIStudio/` — README, MigrationPlan, Hooks policy, Phase 1 completion report
- `.cursor/rules/` modular set: foundation, production-standard, blueprint-standards, gameplay-standards, story-canon, documentation-standard, folder-structure
- `.cursor/skills/`: mission-planner, production-review-board, documentation-sync, playtest-generator (+ improved mission-implementer)
- `.cursor/agents/` — 10 non-overlapping role briefs for Task / PRB

### Changed

- Docs: `Documents/README.md`, `MasterIndex.md`, `00_Governance/AIStudio.md` (pointers)
- Reference decision documented: PE-018 = default production map recipe; PE-017A owns Maintenance fuse path

### Notes

- Documentation + `.cursor` workflow only — no Blueprints, maps, or Unreal assets in this change
- Hooks not enabled (policy-only); optional sessionStart deferred to Phase 2
- Unrelated dirty uassets / ThirdParty content excluded from commit

---

## PE-018 — Generator Annex (Maintenance Wing Expansion)
**Date:** 2026-07-25
**Mission:** PE-018
**Branch:** `develop`

### Added

- `/Game/ProjectEcho/Maps/Production/LV_ARI_GeneratorAnnex` — second production map (Service Entry → Fuel Cage → Generator Room → exit-path Witness → Powered Exit)
- `BP_GeneratorAnnexReset` — full SliceReset twin (door / lights / Witness / PowerManager / ambient flags / notes / objectives / Generator state / FuelCan respawn)
- `Documents/05_Missions/PE-018-GeneratorAnnex.md` — mission completion notes
- Design plan approved: `PE-018-DesignPlan.md`

### Changed

- `BP_PowerManager` — generator World Response now includes `BP_WitnessSilhouetteHint`; exit objective text `Access the next area`
- `BP_FuelCan` — sets objective `Fuel and start the generator` on pickup
- Docs: `ProjectHealth.md`, `Roadmap.md`, `SprintHistory.md`, `GameplayFlow.md`

### Notes

- Technical Simulate PASS (boot / generator bind / Witness hidden). Manual Gameplay PASS still required (Enhanced Input).
- Pipe Gallery / Coolant puzzle / Security deferred per approved plan.
- Soft Open Level travel from Maintenance exit not wired this mission (narrative bridge only).
- Audio still PrintString stand-ins — tagged debt.

---

## PE-017A — Experience Hardening & Environment Pass
**Date:** 2026-07-25
**Mission:** PE-017A
**Branch:** `develop`

### Changed

- `BP_MaintenanceWingReset` — complete SliceReset (door lock, emergency lights, Witness once-flag, objectives, notes, fuse respawn via `FuseSpawnMarker`, ambient flags, inventory Fuse clear)
- `BP_NotePickup` — skip `SetObjective` when `ObjectiveOnRead` is empty
- `BP_WitnessSilhouetteHint` — hidden until restore; delayed exit-path presence; `ResetPresence`
- `BP_EmergencyLight` — PointLight standby (dim red) → flicker → fluorescent restore; broken stubs residual
- `BP_PowerAmbientFeedback` — stronger power-restore audio print chain
- `BP_FusePuzzle` — `FUSE BAY EMPTY` interaction prompt; cleared FuelCan leftover ItemData on slice instance
- `LV_ARI_MaintenanceWing` — Witness on exit approach; Note A symptoms-only; outdoor Directional/Sky dimmed; room dressing from existing packs; north silhouette stand-in removed
- Docs: `PE-017-VerticalSlice01.md` (PE-017A notes), `ProjectHealth.md`

### Notes

- Technical PIE PASS (boot / init logs). Manual Gameplay PASS still required (Enhanced Input).
- ThirdParty / vendor pack mass excluded from commit; map refs local Fab/sample packs already in workspace.

---

## Vertical Slice 01 — Maintenance Wing
**Date:** 2026-07-24
**Mission:** PE-017

### Added

- `/Game/ProjectEcho/Maps/Production/LV_ARI_MaintenanceWing` — first production playable slice (L-corridor; Breaker N, Storage E, Electrical S, Exit W/S)
- `BP_WitnessSilhouetteHint` — first Witness presence beat (power-receiver; tension, not chase)
- `BP_MaintenanceWingReset` — slice replay reset (PE-015 reset pattern)
- `Documents/05_Missions/PE-017-VerticalSlice01.md` + design sheet / level blueprint images
- `BP_NotePickup.ObjectiveOnRead` — per-instance objective text on first read (default preserves Facility Key)

### Changed

- Docs: `GameplayFlow.md`, `GameplaySystems.md`, `ProjectHealth.md`, `Roadmap.md`, `SprintHistory.md`
- Composed existing Interaction / Inventory / Objectives / Fuse puzzle / Power frameworks (no PE-015 architecture fork)

### Notes

- Manual PIE Gameplay PASS still required (Enhanced Input)
- ThirdParty mass / unrelated dirties excluded from commit
- Deferred: full door/light/Witness reverse on slice reset without PIE — **addressed in PE-017A**

---

## Gameplay & Puzzle Design Bible
**Date:** 2026-07-24
**Mission:** PE-016

### Added

- `Documents/01_Game_Design/GameplayDesignBible.md` — canonical gameplay & puzzle specification (vision, pillars, loop, families, Witness rules, Blueprint mapping, expansion guide, design rules)
- `Documents/01_Game_Design/Concept Art/Puzzle Design Overview.png` — Figure 1 gameplay philosophy reference (copied design reference; not UI/layout/environment concept)

### Changed

- Docs: `README.md`, `MasterIndex.md`, `GameplaySystems.md`, `GameplayFlow.md`, `ProjectHealth.md`, `PuzzleFramework.md` (cross-refs)
- Authority: beginning PE-017, gameplay missions must reference the bible (or ADR for conflicts)

### Notes

- Documentation + image only; no Blueprints, uassets, or PE-015 puzzle asset changes

---

## Modular Puzzle Framework
**Date:** 2026-07-24
**Mission:** PE-015

### Added

- `BPI_Puzzle`, `E_PuzzleState`, `BP_PuzzleBase` — modular puzzle lifecycle + dispatchers
- `BP_FusePuzzle`, `BP_FusePickup`, `BP_PuzzleResetButton`, `BP_PuzzleManager` — Fuse example + reset
- `BP_PowerManager.NotifyPuzzlePowerResponse` — puzzle power path (tagged `PuzzlePowerResponse`, independent of generator `HasHandledPower`)
- Puzzle Station on `LV_TestingGround` (hub-adjacent): fuse → panel → objective/power → reset/repeat
- `Documents/02_Technical/PuzzleFramework.md`

### Changed

- Docs: `GameplayFlow.md`, `GameplaySystems.md`, `BlueprintDependencyMap.md`, `EventFlow.md`, `ProjectHealth.md`, `MasterIndex.md`, `README.md`

### Notes

- Save fields exposed only (no save implementation)
- ThirdParty / PE-013C dirties excluded from this commit

---

## Gameplay Framework Consolidation & Architecture Documentation
**Date:** 2026-07-24
**Mission:** PE-014

### Added

- `Documents/02_Technical/GameplayFlow.md` — implemented end-to-end loop + Mermaid diagrams (player lifecycle, input, interaction, objectives, generator→power, notes, save/puzzle hooks)
- `Documents/02_Technical/Architecture/BlueprintDependencyMap.md` — major BP relationship tree, coupling concerns, circular-path notes (`BPC_*` names)
- `Documents/02_Technical/Architecture/EventFlow.md` — event chains for Movement, Interaction, Generator, Power, Objectives, Notes, Flashlight
- `Documents/02_Technical/Architecture/TechnicalDebt.md` — Safe / Requires Review / Ignore debt triage from MCP inspection
- `Documents/02_Technical/BlueprintStandards.md` — naming, variables, functions, categories, events, folders, interfaces, components (DOC-002 / ASSET-001 aligned)
- `Documents/04_Production/ProjectHealth.md` — category health grades + recommendations

### Changed

- `Documents/02_Technical/GameplaySystems.md` — full per-system Purpose / Owners / Deps / I/O / Events / Public Functions / Status / Future (MCP-accurate)
- `Documents/02_Technical/BlueprintArchitecture.md` — pointer refresh to PE-014 architecture set; `BPC_*` component tree
- `Documents/README.md` — indexed 00–04 docs with short descriptions

### Notes

- Documentation-only mission; no gameplay feature work
- PE-013C input Blueprint dirties intentionally excluded from this commit
- Validation sandbox remains `LV_TestingGround`

---

## Development Sandbox Environment Refinement
**Date:** 2026-07-24
**Mission:** PE-013D

### Changed

- `LV_TestingGround` final environment refinement for long-term developer UX (not a campaign level)
- Architecture snap pass on modular wall/floor/ceiling pieces; movement obstacles cleared from circulation paths
- Lighting consistency: Hub/Lab bright neutral; Inventory/Control warm white; Generator darker industrial; Horror corridor controlled red; softened sun/skylight to reduce overexposure
- Developer Hub spawn with `HubInfoBoard` / `HubTitleBoard` listing PROJECT ECHO stations and floor-color legend
- Overhead station signage (MOVEMENT, INTERACTION, INVENTORY, POWER, OBJECTIVES, NOTES, PUZZLE, AI, DEVELOPER, GENERATOR)
- Subtle color-coded floor stripes/arrows (`MI_Stripe_*`) for navigation without visual noise
- Room identity dressing (movement barriers/ramp/jump box; lab console/table; inventory shelves/crates; control desk workstation; reserved expansion labels for Save/Dialogue/Networking/Boss/AI)
- Gameplay Blueprints untouched; placed gameplay actors verified present after refinement

---

## Documentation Foundation
**Date:** 2026-07-24

### Added

#### Governance
- DevelopmentBible.md
- AIStudio.md
- DecisionLog.md
- ContributionGuide.md
- MasterIndex.md

#### Game Design
- GameDesign.md
- GameplayLoop.md
- NarrativeDesign.md
- ArtBible.md
- AudioBible.md
- PuzzleBible.md
- AIBible.md

#### Technical
- TechnicalDesign.md
- GameplaySystems.md
- BlueprintArchitecture.md
- CodingStandards.md
- SaveSystem.md
- SystemDependencies.md

#### World
- StoryBible.md
- Timeline.md
- FacilityBible.md
- RoomBible.md
- Characters.md
- Organizations.md
- Glossary.md

### Changed

#### Documentation Standards
- Standardized all project documentation using Markdown.
- Established a unified documentation folder structure.
- Defined the purpose and ownership of each documentation category.
- Added a Master Index for easier navigation.

#### Governance
- Introduced Canon Rules for all future design and story decisions.
- Established the Canon Freeze policy.
- Defined the Documentation Workflow.
- Adopted the Living Documentation philosophy.
- Adopted an Append-Only Changelog policy.
- Separated approved Canon from future Recommendations.

### Notes

This milestone establishes the project's documentation foundation. Future gameplay systems, story content, technical architecture, and production updates will build upon these documents. Historical entries in this changelog should only be appended to and never rewritten.

---

## Documentation
**Date:** 2026-07-24
**Mission:** DOC-001

### Added

- Unreal Engine Naming Standards
- Mission Completion Report
- Prototype Map Purpose
- Documentation Workflow

### Changed

- Standardized Unreal Engine naming conventions.
- Established prototype map workflow.
- Standardized mission completion reporting.
- Reinforced append-only changelog policy.
- Reinforced canon-first documentation philosophy.

---

## World Response System
**Date:** 2026-07-24
**Mission:** PE-012

### Added

- `BP_VentilationUnit` under `Gameplay/Power/` — BPI_PowerReceiver ventilation start feedback (placeholder PrintString / once-only)
- `BP_PASpeaker` under `Gameplay/Power/` — brief PA / electrical static burst (once-only)
- `BP_DistantActivityHint` under `Gameplay/Power/` — distant facility activity hint (once-only, delayed)
- `LV_Prototype_PE012` — generator + fuel flow, emergency lights (including broken), powered door, ambient feedback, and new world-response receivers with `PE012_*` actor labels

### Changed

- Extended `BP_PowerManager` HandlePowerRestored to notify ventilation, PA, and distant-activity receivers after lights, door, and ambient feedback
- Preserved `LV_Prototype_PE011` for regression

### Notes

First post-power living-facility sequence. Grounded uncertainty only — no combat, chase, jump scares, or Witness reveal. Sequence remains once-only via PowerManager `HasHandledPower`.

---

## Asset Naming Standard
**Date:** 2026-07-24
**Mission:** DOC-002

### Added

- Project Echo Asset Naming Standard v1.0 finalized in ContributionGuide
- Component prefix `BPC_[Name]` (replacing `BP_*Component`)
- Map conventions documented: `LV_Prototype_PE###`, `LV_TestingGround`, `LV_ARI_*`
- Descriptive World Outliner labels without `PE###_` prefixes

### Changed

- Renamed components: `BP_InteractionComponent` → `BPC_Interaction`, `BP_ObjectiveComponent` → `BPC_Objective`, `BP_InventoryComponent` → `BPC_Inventory`, `BP_FlashlightComponent` → `BPC_Flashlight`
- Renamed `WBP_Note` → `WBP_NoteReader`
- Renamed `ST_ItemData` → `ST_InventoryItem`
- Updated actor labels on `LV_Prototype_PE011` and `LV_Prototype_PE012` to descriptive names
- Synced CodingStandards component naming with v1.0

### Notes

Reusable assets describe function, not mission number. Mission IDs remain valid only for prototype maps, docs, changelog, commits, and reports.

---

## Project Content Organization Standardization
**Date:** 2026-07-24
**Mission:** ASSET-001

### Added

- Official `Content/ProjectEcho/` hierarchy scaffold (`Gameplay/*`, `Environment/*`, `Maps/*`, `UI/`, `Data/`, `Input/`, `Sequences/`, `Documentation/`, `Developers/`)
- `Content/ThirdParty/` confirmed as policy home for vendor packs
- `Documents/02_Technical/AssetCatalog.md` — catalog of all imported ThirdParty packs
- ContributionGuide sections: Official Content Folder Structure, ThirdParty Policy, ProjectEcho Policy, Folder Naming Standards

### Changed

- Migrated Project Echo originals from `Blueprints/`, `Levels/` into the official hierarchy (asset names preserved)
- Prototype maps moved to `Maps/Prototype/` (`LV_Prototype`, `LV_Prototype_PE011`, `LV_Prototype_PE012`)
- Cleaned redirectors / orphaned old Blueprint path packages after migration

### Notes

Organizational only — no Blueprint graph / gameplay logic changes. ThirdParty vendor packs were not moved or modified.

---

## Asterion Development Testing Facility
**Date:** 2026-07-24
**Mission:** PE-013

### Added

- `LV_TestingGround` under `Maps/Development/` — permanent Asterion Research Institute development sandbox
- Eight labeled zones: Developer Spawn, Interaction Lab, Generator Room, Inventory & Objectives, Puzzle Sandbox, Horror Corridor, Future AI Arena, Developer Control Room
- Integrated PE-011/012 power chain actors into Generator Room with descriptive World Outliner labels
- Interaction Lab and Inventory & Objectives placed with existing gameplay Blueprints (doors, pickups, notes, key item)
- Basic zone lighting, ceiling/floor/wall shells from ThirdParty industrial/lab packs (reference only)

### Changed

- Updated `GameplaySystems.md` with Asterion Development Testing Facility section

### Notes

No Blueprint logic changes. Sandbox is not campaign content. ThirdParty vendor packs were referenced only and not edited.

---

## Asterion Development Testing Facility Environment Polish
**Date:** 2026-07-24
**Mission:** PE-013A

### Changed

- `LV_TestingGround` environmental polish pass (architecture, lighting, dressing, floor marks, room identity, subtle storytelling, corridor navigation cues)
- Sealed interior ceilings across all zones and hub corridors; added beams, pillars, ceiling frames, and elevated access platforms
- Replaced temporary zone PointLights with industrial RectLight fluorescents + lamp meshes (Generator darker; Horror Corridor controlled dim; sun/skylight softened)
- Wall dressing: pipes, vents/ducts, panels, warning signs, cabinets/lockers, cable runs, extinguisher levers (ThirdParty reference only)
- Floor polish: sparse leak decals and circulation markers; human-activity storytelling props (mugs, paper, notices, chairs, monitors) — no horror storytelling

### Notes

No gameplay Blueprint graph or system changes. PE-011/PE-012 prototype maps untouched. Atmosphere relies on existing power-response ambient actors plus visual vent/industrial dressing. ThirdParty vendor packs referenced only and not modified.

---

## Development Sandbox Validation & Gameplay Integration
**Date:** 2026-07-24
**Mission:** PE-013B

### Fixed

- Restored `BP_PlayerController` Enhanced Input registration on `EventOnPossess` (BUG-001 path) after empty EventGraph regression
- Completed `BP_PlayerCharacter` sprint helpers (`CanStartSprint` / `StartSprint` / `StopSprint`)
- Added missing `IA_Interact` / `IA_Flashlight` mappings to `IMC_Player`
- Corrected `DefaultEngine.ini` GameMode / GameInstance / default+startup maps to Project Echo assets (was FirstPerson template)

### Added

- `Station_*` labeled test stations and in-level `DebugBoard_Systems` on `LV_TestingGround`
- `BP_DevSandboxValidator` + placed `DevSandboxValidator` for PIE API validation when Slate keys are unreliable

### Changed

- Updated `GameplaySystems.md` with PE-013B root-cause analysis, fixes, and validation results

### Notes

All implemented validation checklist items PASS in PIE. ThirdParty packs untouched. Prototype maps not modified for this mission.

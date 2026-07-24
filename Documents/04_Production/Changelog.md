# Changelog

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

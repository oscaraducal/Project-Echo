# Changelog

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

# Project Echo Documentation

Welcome to the official documentation for **Project Echo**.

This documentation is the single source of truth for design, technical architecture, world-building, and production planning.

---

## Documentation Structure

### 00_Governance

Project management, development workflow, AI collaboration, and design decisions.

| Document | Description |
|----------|-------------|
| [DevelopmentBible.md](00_Governance/DevelopmentBible.md) | Core development philosophy and process |
| [AIStudio.md](00_Governance/AIStudio.md) | AI collaboration roles (legacy overview; see Production AI Studio) |
| [DecisionLog.md](00_Governance/DecisionLog.md) | Recorded design/technical decisions |
| [ContributionGuide.md](00_Governance/ContributionGuide.md) | Naming, Git, PR, and asset standards (DOC-002 / ASSET-001) |
| [MasterIndex.md](00_Governance/MasterIndex.md) | High-level documentation map |

### 01_Game_Design (Design)

Gameplay vision, mechanics, narrative, art, and audio direction.

| Document | Description |
|----------|-------------|
| [GameplayDesignBible.md](01_Game_Design/GameplayDesignBible.md) | **Canonical** gameplay & puzzle specification (PE-016) — required reference for PE-017+ |
| [GameDesign.md](01_Game_Design/GameDesign.md) | Pillars and high-level design (primer; bible wins on conflict) |
| [GameplayLoop.md](01_Game_Design/GameplayLoop.md) | Explore → interact → progress design loop (primer) |
| [NarrativeDesign.md](01_Game_Design/NarrativeDesign.md) | Story delivery approach |
| [PuzzleBible.md](01_Game_Design/PuzzleBible.md) | Early puzzle design rules (superseded in detail by Gameplay Design Bible) |
| [ArtBible.md](01_Game_Design/ArtBible.md) | Visual direction |
| [AudioBible.md](01_Game_Design/AudioBible.md) | Audio direction |
| [AIBible.md](01_Game_Design/AIBible.md) | Threat / AI design |
| [Concept Art/Puzzle Design Overview.png](01_Game_Design/Concept%20Art/Puzzle%20Design%20Overview.png) | Figure 1 — gameplay philosophy reference (not UI/layout) |

### 02_Technical

Blueprint architecture, gameplay systems, coding standards, and implementation truth.

| Document | Description |
|----------|-------------|
| [TechnicalDesign.md](02_Technical/TechnicalDesign.md) | Technical approach overview |
| [GameplayFlow.md](02_Technical/GameplayFlow.md) | **Implemented** end-to-end flow + Mermaid diagrams (PE-014) |
| [GameplaySystems.md](02_Technical/GameplaySystems.md) | Per-system owners, APIs, status (PE-014) |
| [PuzzleFramework.md](02_Technical/PuzzleFramework.md) | Modular puzzle architecture, lifecycle, Fuse example (PE-015) |
| [BlueprintStandards.md](02_Technical/BlueprintStandards.md) | Authoring standards aligned with DOC-002 (PE-014) |
| [BlueprintArchitecture.md](02_Technical/BlueprintArchitecture.md) | Short architecture philosophy |
| [CodingStandards.md](02_Technical/CodingStandards.md) | Blueprint coding principles |
| [SystemDependencies.md](02_Technical/SystemDependencies.md) | Legacy dependency notes |
| [SaveSystem.md](02_Technical/SaveSystem.md) | Planned save design |
| [AssetCatalog.md](02_Technical/AssetCatalog.md) | Content catalog (ASSET-001) |
| [BugHistory.md](02_Technical/BugHistory.md) | Root-cause bug records (PE-013B/C) |
| [Architecture/BlueprintDependencyMap.md](02_Technical/Architecture/BlueprintDependencyMap.md) | BP relationship tree + coupling concerns |
| [Architecture/EventFlow.md](02_Technical/Architecture/EventFlow.md) | Runtime event chains |
| [Architecture/TechnicalDebt.md](02_Technical/Architecture/TechnicalDebt.md) | Debt triage (Safe / Review / Ignore) |

### 03_World (World / Art context)

Story, lore, facility layouts, timeline, characters, and organizations.

| Document | Description |
|----------|-------------|
| [StoryBible.md](03_World/StoryBible.md) | Canon story |
| [Timeline.md](03_World/Timeline.md) | Chronology |
| [FacilityBible.md](03_World/FacilityBible.md) | Facility overview |
| [RoomBible.md](03_World/RoomBible.md) | Room definitions |
| [Characters.md](03_World/Characters.md) | Characters |
| [Organizations.md](03_World/Organizations.md) | Factions / orgs |
| [Glossary.md](03_World/Glossary.md) | Terms |

### 04_Production

Roadmap, milestones, changelog, sprint history, health, asset tracking, and AI Studio workflow.

| Document | Description |
|----------|-------------|
| [ProductionPlaybook.md](04_Production/ProductionPlaybook.md) | **Authoritative** production process (PE-017 / 017A / 018 lessons) |
| [AIStudio/README.md](04_Production/AIStudio/README.md) | Cursor AI Studio architecture (rules / skills / agents) — **v1.1** |
| [AIStudio/ValidationReport-FRAMEWORK-001.md](04_Production/AIStudio/ValidationReport-FRAMEWORK-001.md) | AI Studio v1.0 validation (FRAMEWORK-001) |
| [AIStudio/MigrationPlan.md](04_Production/AIStudio/MigrationPlan.md) | Phase 1→N migration sequence |
| [AIStudio/Hooks.md](04_Production/AIStudio/Hooks.md) | Hooks policy (Phase 1: docs only — not enabled) |
| [Roadmap.md](04_Production/Roadmap.md) | Forward plan |
| [Milestones.md](04_Production/Milestones.md) | Milestone definitions |
| [Changelog.md](04_Production/Changelog.md) | Append-only change history |
| [SprintHistory.md](04_Production/SprintHistory.md) | Sprint records |
| [AssetMasterList.md](04_Production/AssetMasterList.md) | Production asset tracking |
| [ProjectHealth.md](04_Production/ProjectHealth.md) | Health grades + recommendations (PE-014) |

### 05_Missions

Historical archive of completed development missions (when present).

---

## Current Milestone

**Milestone 1 — The First Encounter**

Status: In Progress

---

## Current Development Branch

`develop`

---

## Latest Design / Architecture Pass

**AI Studio v1.1** — FRAMEWORK-001 validation (docs only) · Phase 1 Playbook + modular Cursor rules/skills/agents

Prior: PE-018 Generator Annex · PE-017A hardening · PE-016 Gameplay Design Bible · PE-015 Puzzle Framework · PE-014 Architecture Documentation

Validation sandbox: `/Game/ProjectEcho/Maps/Development/LV_TestingGround`

Default production map recipe: **PE-018**. Fuse path ownership: **PE-017A**.

---

## Development Workflow

Design Plan → Approval → Cursor Implementation → Compile → Technical Simulate → Human PIE → Docs → Git → Production Review Board → Merge

See [ProductionPlaybook.md](04_Production/ProductionPlaybook.md).

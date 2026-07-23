# Draft for Review — `PROJECT_ECHO_PLAYBOOK.md`

*Not written to disk. Review, revise, then approve before committing to `.cursor/PROJECT_ECHO_PLAYBOOK.md`.*

---

```markdown
# PROJECT ECHO — ENGINEERING PLAYBOOK

**Version:** 0.1 (First Draft — For TD Review)  
**Engine:** Unreal Engine 5.8  
**Language Policy:** Blueprint-first (C++ only when explicitly requested)  
**Status:** Prototype Phase Active  
**Audience:** Gameplay Engineer, AI collaborators (Cursor), Technical Director  

---

## 1. Purpose

This Playbook is the day-to-day operating manual for implementing Project Echo.

It does **not** replace design Bibles, the Technical Design Document, or the Canon Bible.  
It **does** define how engineering work is performed: standards, folders, naming, workflow, and AI collaboration rules.

If this Playbook conflicts with an approved Technical Director decision, the TD decision wins. Update this document afterward.

---

## 2. Development Philosophy

### 2.1 Core Principles

1. **Documentation-driven** — Understand the approved design and architecture before implementing.
2. **Architecture-respecting** — Do not redesign systems. Implement what is approved. If architecture is missing, ask before coding.
3. **Blueprint-first** — Prefer Blueprints for gameplay systems unless C++ is explicitly requested.
4. **Modular by default** — One Blueprint = one purpose. Features live in components. Systems connect through interfaces.
5. **Composition over inheritance** — Prefer Actor Components and interfaces over deep Blueprint class hierarchies.
6. **Production-quality habits early** — Naming, folders, reviews, and commits should look professional even in prototype.
7. **AI-assisted, human-owned** — AI proposes and implements under rules; the developer tests; ChatGPT/TD reviews architecture and quality.

### 2.2 What We Optimize For

| Priority | Meaning |
|----------|---------|
| Clarity | Another engineer (or future you) can read the graph and understand intent |
| Modularity | Systems can grow without rewriting the player or GameMode |
| Safety | No silent renames, deletes, moves, or duplicate systems |
| Traceability | Every feature has purpose, test plan, docs, and a commit message |

### 2.3 What We Explicitly Avoid

- Event Tick for gameplay unless approved
- Unnecessary casts
- Duplicate systems for the same responsibility
- Hard references where interfaces or components are appropriate
- Spaghetti Blueprint graphs
- Inventing gameplay features not present in approved documentation
- Changing architecture without TD approval

---

## 3. Authoritative Documents

| Document | Role |
|----------|------|
| `Documents/00_Governance/` | Development Bible, Decision Log, Master Index |
| `Documents/01_Game_Design/` | GDD, Canon, Narrative, AI, Audio, Art, Level, Puzzle Bibles |
| `Documents/02_Technical/` | Technical Design Document, Gameplay Blueprint, AI Blueprint |
| `Documents/03_World/` | Facility Blueprint, Room Bible, Master Timeline |
| `Documents/04_Production/` | Production Bible, Asset Master List, Puzzle Catalogue |
| `.cursor/project.md` | Project snapshot (genre, status, core systems list) |
| `.cursor/architecture.md` | Runtime ownership rules |
| `.cursor/rules.md` | AI Constitution (hard constraints) |
| `.cursor/standards.md` | Blueprint coding standards |
| `.cursor/workflow.md` | ChatGPT → Cursor → Test → Review → Docs → Git |
| **This Playbook** | Engineering operating procedures |

Design Bibles define *what* the game is.  
This Playbook defines *how* we build it.

---

## 4. Runtime Architecture (Do Not Redesign)

Approved ownership chain:

```
GameMode
  → PlayerController
    → PlayerCharacter
      → Gameplay Components
        → Interaction / Inventory / Save (and other approved feature components)
```

### 4.1 Ownership Rules

| Owner | Responsibility |
|-------|----------------|
| **PlayerController** | Input (Enhanced Input, mapping contexts) |
| **PlayerCharacter** | Movement |
| **Components** | Features (flashlight, interaction, inventory, etc. as approved) |
| **Interfaces** | Connections between systems |
| **GameInstance / SaveGame** | Persistent / save-related concerns as defined by technical docs |

### 4.2 Architecture Rules

- Never use Event Tick for gameplay unless necessary and approved.
- Every system should be modular.
- Avoid hard references when interfaces or components are appropriate.
- Prefer: Blueprint Interfaces, Actor Components, Gameplay Tags, Data Assets, Function Libraries, Enhanced Input.

---

## 5. Folder Organization

### 5.1 Project Root

```
ProjectEcho/
├── Config/
├── Content/
│   └── ProjectEcho/          ← Primary game content root
├── Documents/                ← Design, production, engineering docs
├── .cursor/                  ← AI constitution, playbook, prompts
├── README.md
├── .gitignore
└── ProjectEcho.uproject
```

`Source/` is reserved for future C++ if explicitly required.

### 5.2 Content — `Content/ProjectEcho/`

This is the **canonical** content root for Project Echo gameplay and production assets.

```
Content/ProjectEcho/
├── AI/
├── Animation/
├── Audio/
│   ├── Ambient/
│   ├── Music/
│   ├── SFX/
│   └── Voice/
├── Blueprints/
│   ├── Characters/
│   ├── Components/
│   ├── Cores/              ← GameMode, PlayerController, GameInstance, HUD, SaveGame
│   ├── Gameplay/
│   ├── Interfaces/
│   ├── Systems/
│   └── UI/
├── Characters/             ← Character art / related assets (non-Blueprint)
├── Cinematics/
├── Data/
│   ├── DataAssets/
│   ├── DataTables/
│   ├── Enums/
│   └── Structs/
├── Developer/
├── Environment/
│   ├── Architecture/
│   ├── Decals/
│   ├── Foliage/
│   ├── Materials/
│   ├── Meshes/
│   ├── Props/
│   └── Textures/
├── FX/
│   ├── Niagra/             ← Existing folder name; do not rename without TD approval
│   └── PostProcess/
├── Input/                  ← Project Echo Enhanced Input assets
├── Levels/
│   ├── Persistent/
│   ├── Prototype/
│   ├── Test/
│   └── VerticalSlice/
├── Materials/
└── UI/
```

### 5.3 Blueprint Subfolders (Standards Alignment)

Per Blueprint standards, gameplay Blueprints are organized under themes such as:

- `Characters/`
- `AI/`
- `Environment/`
- `UI/`
- `Systems/`

Cores (framework classes) live under `Blueprints/Cores/`.

### 5.4 Template / Epic Content Policy

Content outside `Content/ProjectEcho/` (for example First Person template, root `Content/Input/`, mannequins, level prototyping kits) is **legacy or reference** unless the Technical Director states otherwise.

**Rules:**

- New Project Echo gameplay assets are created under `Content/ProjectEcho/`.
- Do not silently depend on template GameModes, Controllers, or Input Mapping Contexts when Project Echo equivalents exist.
- Do not delete, rename, or move template folders unless the TD explicitly approves a cleanup mission.

### 5.5 Documents Tree

```
Documents/
├── 00_Governance/
├── 01_Game_Design/
├── 02_Technical/
├── 03_World/
├── 04_Production/
├── 05_Art_References/
├── 06_Meetings/
├── 07_Changelogs/
├── 08_Developer_Journal/
├── 09_Engineering/
├── 10_AI/
├── 11_CodeReviews/
├── 12_TestPlans/
├── 13_Postmortems/
└── Archive/
```

Engineering feature writeups belong in `09_Engineering/` (and/or mission docs as directed).  
Do not park implementation specs only inside chat history.

---

## 6. Naming Conventions

### 6.1 Required Prefixes

| Prefix | Asset Type |
|--------|------------|
| `BP_` | Blueprint |
| `WBP_` | Widget Blueprint |
| `BPI_` | Blueprint Interface |
| `AC_` | Actor Component |
| `IA_` | Input Action |
| `IMC_` | Input Mapping Context |
| `LV_` | Level |
| `SM_` | Static Mesh |
| `SK_` | Skeletal Mesh |
| `M_` | Material |
| `MI_` | Material Instance |
| `T_` | Texture |
| `DA_` | Data Asset |

### 6.2 Naming Rules

- Use clear, purpose-driven names (`BP_PlayerCharacter`, `IA_Interact`, `IMC_Player`).
- Prefer English, PascalCase after the prefix.
- Do not invent alternate prefixes without updating this Playbook and `Documents/readme.md`.
- Do not rename existing assets unless the TD explicitly authorizes a rename mission.

### 6.3 Known Folder Name Debt

- `FX/Niagra/` exists with a spelling inconsistency relative to “Niagara.”  
  **Do not rename** until the TD approves a dedicated cleanup. New assets should follow TD guidance for that folder.

---

## 7. Blueprint Standards

### 7.1 Structure

- Single Responsibility Principle: one Blueprint = one purpose.
- No duplicated logic across Blueprints when a shared function library, component, or interface is appropriate.
- Split logic into functions.
- Maximum **30 nodes per function**.
- Use comments on non-obvious graphs.
- Avoid spaghetti graphs.

### 7.2 Variables

- Private by default.
- Categorized.
- Tooltips added.

### 7.3 Preferred Patterns

- Blueprint Interfaces for cross-system contracts
- Actor Components for features
- Gameplay Tags where appropriate
- Data Assets for tunable data
- Function Libraries for shared pure/utility logic
- Enhanced Input for all player input

### 7.4 Forbidden (Unless Explicitly Approved)

- Event Tick for gameplay
- Unnecessary casts
- Creating a second system that duplicates an existing one
- Renaming, deleting, or moving assets/folders
- Changing architecture

---

## 8. Input Policy

- Player input is owned by **BP_PlayerController**.
- Project Echo input assets live under `Content/ProjectEcho/Input/`.
- Existing Project Echo Input Actions (Move, Look, Interact, Flashlight, Inventory, Journal, Sprint, Crouch, Pause) are part of the approved input surface; wire them only when the corresponding approved feature is being implemented.
- Do not create parallel Input Actions for the same verb without TD approval.

---

## 9. Collision / Trace Channels (Existing)

The project already defines custom channels in config, including:

- `Interactable`
- `EchoTrigger`
- `Witness`
- `PlayerNoise`

Treat these as approved plumbing. Do not redefine equivalent channels under new names. Use them according to technical documentation when implementing related systems.

---

## 10. Workflow

### 10.1 Standard Pipeline

```
1. ChatGPT designs / confirms architecture
2. Cursor implements (under AI Constitution + this Playbook)
3. Developer tests in-editor
4. ChatGPT / reviewer reviews
5. Documentation updated
6. Git commit
7. Merge (per branch policy)
```

### 10.2 Branch Strategy

| Branch | Purpose |
|--------|---------|
| `main` | Stable production branch |
| `develop` | Active development |
| `feature/*` | Individual feature development |

Do not treat `main` as a daily scratch branch once `develop` is active.

### 10.3 Commit Message Style

Follow Conventional Commit style used by the project README:

```
feat: implement flashlight system
fix: correct interaction trace
refactor: simplify inventory component
docs: update Facility Blueprint
```

Every implementation should be prepared with a proposed commit message even when the developer makes the final commit.

### 10.4 Mission Discipline

Before implementation missions:

1. Read `.cursor/rules.md`, `architecture.md`, `standards.md`, and this Playbook.
2. Confirm the feature exists in approved documentation / TD decisions.
3. If architecture is missing → **ask**, do not invent.
4. After implementation → document, test, then commit when requested.

---

## 11. AI Collaboration Rules

### 11.1 Role

Cursor / AI acts as **Gameplay Engineer** for Project Echo.

### 11.2 AI Must

- Follow the AI Constitution (`.cursor/rules.md`)
- Follow approved architecture
- Implement systems, refactor when asked, generate documentation, suggest improvements, explain implementation
- Ask clarifying questions when architecture or requirements are incomplete
- Prefer Unreal patterns listed in the Constitution

### 11.3 AI Must Not

- Redesign the project
- Rename assets
- Delete assets
- Move folders
- Change architecture
- Use Event Tick unless approved
- Cast unnecessarily
- Create duplicate systems
- Invent gameplay features not present in approved docs / TD decisions

### 11.4 Every Implementation Deliverable Must Include

1. Purpose  
2. Architecture  
3. Variables  
4. Functions  
5. Events  
6. Testing  
7. Future Expansion  
8. Known Limitations  
9. Documentation  
10. Git Commit Message  

### 11.5 Prompt Library (`.cursor/prompts/`)

| Prompt | Use |
|--------|-----|
| `feature.md` | New gameplay feature implementation |
| `refactor.md` | Reduce complexity; preserve behavior |
| `debug.md` | Root cause, solutions, prevention |
| `review.md` | Architecture, performance, naming, maintainability |
| `test.md` | QA cases with preconditions, steps, expected results |
| `documentation.md` | Engineering documentation package |

Use the matching prompt style for the mission type.

### 11.6 Read-Only Missions

When a mission is marked READ-ONLY:

- Do not modify, create, rename, or delete files
- Produce analysis / drafts for review only
- Present documents in chat unless the TD explicitly requests a write

---

## 12. Documentation Standards

### 12.1 Feature Documentation Minimum

Every feature requires documentation covering:

- Purpose  
- Architecture  
- Blueprints involved  
- Variables  
- Functions  
- Events  
- Testing  
- Future Improvements  
- Known Issues  

### 12.2 Developer Journal

Use `Documents/08_Developer_Journal/` for sprint learnings, problems, and solutions (as already begun).

### 12.3 Decision Log

Architectural or production decisions that change how work is done must be recorded in the Governance Decision Log and reflected here if they affect daily engineering practice.

---

## 13. Testing Expectations

For each implemented feature, provide test coverage that includes:

- Preconditions  
- Steps  
- Expected Result  
- Pass Criteria  
- Regression Tests  

Prototype work still requires a clear in-editor test path. “It compiles / it opens” is not sufficient for gameplay systems.

---

## 14. Review Criteria

When reviewing an implementation, check:

1. Architecture compliance  
2. Performance (especially Tick, ticks-in-disguise, expensive ticks/timers)  
3. Naming  
4. Scalability  
5. Maintainability  
6. Blueprint cleanliness  
7. Professional Unreal practices  

Suggest improvements; do not silently redesign.

---

## 15. Git & Repository Hygiene (Engineering Policy)

- Keep `Binaries/`, `DerivedDataCache/`, `Intermediate/`, `Saved/` out of version control (per `.gitignore`).
- Prefer small, reviewable commits scoped to one feature or fix.
- Do not commit secrets or machine-local paths.
- Binary assets (`.uasset`, `.umap`, large docs) must follow the repository’s approved binary strategy as defined by the TD (LFS or equivalent). Until that policy is finalized, ask before large content drops.
- Do not force-push protected branches.

---

## 16. Prototype Phase Focus (Non-Feature Inventory)

Per project status, Prototype Phase is active and the following **system areas** are listed as core to the project. This Playbook does **not** define their design — only that implementation must wait for approved architecture per system:

- Player  
- Interaction  
- Inventory  
- Flashlight  
- AI  
- Puzzle  
- Save  
- Audio  
- UI  

Future milestones (Vertical Slice → Alpha → Beta → Release) remain roadmap items in `README.md` / production docs.

---

## 17. Change Control

| Change Type | Who Approves |
|-------------|--------------|
| Gameplay feature design | Design docs + TD |
| Architecture change | TD |
| Asset rename / move / delete | TD (explicit mission) |
| Naming prefix additions | TD + Playbook update |
| Folder structure changes | TD |
| Playbook updates | TD review |

---

## 18. Quick Reference — Do / Don’t

### Do

- Implement approved architecture  
- Keep Controller = Input, Character = Movement, Components = Features  
- Use interfaces and components  
- Document and test every feature  
- Ask when unsure  

### Don’t

- Invent systems or redesign architecture  
- Rename / delete / move without approval  
- Use Event Tick casually  
- Duplicate existing systems  
- Bypass the workflow (implement → skip test/docs/commit discipline)  

---

## 19. Document History

| Version | Date | Notes |
|---------|------|-------|
| 0.1 | 2026-07-23 | First draft compiled from existing project docs, architecture, standards, rules, workflow, and README. For TD review. No architecture changes. No new gameplay features invented. |

---

*"The building remembers."*
```

---

## Review notes for the TD

- Draft stays within existing docs; core systems are listed as scope areas only, not designed.
- Preserves current folder names (`Cores`, `FX/Niagra`) and flags rename debt instead of “fixing” it.
- Marks Epic/template content as non-canonical without mandating deletion.
- Git LFS is framed as “ask TD,” not prescribed as a new architecture decision.
- Ready to drop into `.cursor/PROJECT_ECHO_PLAYBOOK.md` after your edits.
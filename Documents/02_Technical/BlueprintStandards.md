# Blueprint Standards

Status: Active  
Version: 1.0  
Mission: PE-014  

Aligned with ContributionGuide (DOC-002 / ASSET-001) and CodingStandards.md.

---

# Purpose

Authoring rules for Project Echo Blueprints so new systems plug into the consolidated architecture without renaming churn.

---

# Naming

| Type | Format | Examples |
|------|--------|----------|
| Actor / Object BP | `BP_[Name]` | `BP_Generator`, `BP_Door` |
| Component BP | `BPC_[Name]` | `BPC_Interaction`, `BPC_Inventory` |
| Interface | `BPI_[Name]` | `BPI_Interactable`, `BPI_PowerReceiver` |
| Widget | `WBP_[Name]` | `WBP_Objective`, `WBP_NoteReader` |
| Struct | `ST_[Name]` | `ST_InventoryItem` |
| Enum | `E_[Name]` | `E_GeneratorState` |
| Data Asset | `DA_[Name]` | — |
| Function Library | `BFL_[Name]` | — |
| Input Action | `IA_[Name]` | `IA_Interact` |
| Input Mapping Context | `IMC_[Name]` | `IMC_Player` |
| Level | `LV_[Name]` or `LV_Prototype_PE###` | `LV_TestingGround` |

**Forbidden:** `BP_*Component` (use `BPC_*`). Mission IDs on reusable assets or Outliner labels (`PE014_Generator`).

---

# Variables

- Boolean: `b` prefix (`bHasFlashlight`, `bCollected`).
- Prefer clear names over abbreviations (`TraceDistance` not `TD`).
- Expose instance-editable only when designers must tune per-instance.
- Always assign a **Category** (see below).
- Tooltips for designer-facing properties.
- Avoid duplicate `_0` suffixes from failed renames (`HasHandledPower_0`).

---

# Functions

- Verb phrases: `TryInteract`, `SetObjective`, `GiveFlashlight`, `FinishGeneratorStart`.
- Pure getters when side-effect free: `GetCurrentObjective`, `HasItem`.
- One responsibility per function; extract helpers rather than mega-EventGraph blobs.
- Mark BlueprintPure only when truly pure.
- Prefer calling component public functions over duplicating logic in actors.

---

# Categories

Suggested Categories for consistency:

| Category | Use |
|----------|-----|
| `Config` | Tunables (trace distance, speeds, intensity) |
| `State` | Runtime flags (`IsSprinting`, `PowerRestored`) |
| `References` | Soft/hard object refs |
| `Debug` | Print toggles, validator hooks |
| `Input` | IMC / sensitivity |
| `UI` | Widget class refs, display duration |

---

# Events & Dispatchers

- Prefer **Event Dispatchers** for one-to-many (`BP_Generator.OnPowerRestored`).
- Prefer **Interfaces** for many actor types (`BPI_Interactable`, `BPI_PowerReceiver`).
- Do not leave empty custom events / empty Tick / empty BeginOverlap in shipping graphs — remove or comment why reserved.
- Name dispatchers `On[PastEvent]` (`OnPowerRestored`).
- Avoid stacking numbered duplicates (`OnPowerRestored_Event_13`).

---

# Comments & Graph Organization

- Comment boxes around systems (Input, Interact, Power bind).
- Execution left → right; data pins tidy.
- Delete unused nodes after experiments (disconnected ApplySprintSpeed leftovers, orphan customs).
- PrintString messages may include short mission tags during validation (`[PE012]`, `[PE013C]`); remove temporary debug prints before declaring Gameplay PASS.
- Do not rely solely on Blueprint DSL reads for Enhanced Input verification (BUG-002) — confirm pins / PIE.

---

# Folders

Primary content root: `Content/ProjectEcho/`

| Folder | Contents |
|--------|----------|
| `Gameplay/Characters/` | Pawn, Controller |
| `Gameplay/Interaction/` | BPC_Interaction, BPI_Interactable, doors, notes |
| `Gameplay/Inventory/` | BPC_Inventory, pickups |
| `Gameplay/Objectives/` | BPC_Objective |
| `Gameplay/Power/` | Generator, PowerManager, receivers, BPI_PowerReceiver |
| `Gameplay/Systems/` | GameMode, GameInstance, Flashlight component, validators |
| `Gameplay/Save/` | SaveGame stubs |
| `Gameplay/Puzzle/` / `AI/` / `Audio/` | Reserved |
| `UI/` | WBP_*, BP_HUD |
| `Data/` / `Data/Enums/` | ST_*, E_* |
| `Input/` | IMC_*, IA_* |
| `Maps/Development/` | `LV_TestingGround` |
| `Maps/Prototype/` | `LV_Prototype_PE###` |

Do not place new gameplay under legacy empty `Content/ProjectEcho/Blueprints/` or FirstPerson template paths.

---

# Interfaces

- World interaction **must** implement `BPI_Interactable` (`CanInteract`, `Interact`, `GetInteractionText`).
- Prefer parenting `BP_InteractableBase` for shared defaults.
- Power consumers **should** implement `BPI_PowerReceiver.OnPowerRestored`.
- New systems: define `BPI_*` before casting to concrete player/component classes when multiple callers exist.

---

# Components

- Player-owned gameplay systems live as **`BPC_*` components** on `BP_PlayerCharacter`.
- Actors call `GetComponentByClass` only when the Interactor is known to be the player; document assumptions.
- Components must not hard-reference specific level actors.
- One component = one system (Interaction ≠ Inventory ≠ Objectives ≠ Flashlight).

---

# Communication Preference

1. Components (local player systems)  
2. Blueprint Interfaces (world polymorphism)  
3. Event Dispatchers (broadcast)  
4. Soft object references  
5. Hard `Cast To` / `GetAllActorsOfClass` (last resort; document if used)

---

# Compile & Validation

- Every edited Blueprint must compile clean.
- Regression in `LV_TestingGround` (+ prototypes when touching power).
- Technical Validation (validator / ObjectTools) ≠ Gameplay Validation (real PIE input). See BugHistory BUG-007.
- After renames: Fix Up Redirectors (ASSET-001).

---

# Related

- `00_Governance/ContributionGuide.md`  
- `CodingStandards.md`  
- `Architecture/TechnicalDebt.md`  

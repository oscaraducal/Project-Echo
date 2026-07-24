# Contribution Guide

Status: Active

---

# Purpose

This guide defines development standards for anyone contributing to Project Echo.

Currently, contributors include:

- Oscar
- ChatGPT
- Cursor AI

Future contributors should follow the same workflow and standards.

---

# Coding Standards

- Prefer reusable Blueprints.
- Avoid duplicate logic.
- Keep Blueprints focused on a single responsibility.
- Favor Components over inheritance where appropriate.
- Use Blueprint Interfaces for communication.
- Use Event Dispatchers for global events.

---

# Folder Organization

Organize gameplay assets by feature.

Example:

Gameplay/

Doors/

Generator/

Items/

Lighting/

Notes/

---

# Naming Convention

Status: Project Echo Asset Naming Standard v1.0

| Type | Format |
|------|--------|
| Blueprints | BP_[Name] |
| Components | BPC_[Name] |
| Interfaces | BPI_[Name] |
| Widgets | WBP_[Name] |
| Enums | E_[Name] |
| Structs | ST_[Name] |
| Data Assets | DA_[Name] |
| Function Libraries | BFL_[Name] |
| Static Meshes | SM_[Name] |
| Skeletal Meshes | SK_[Name] |
| Materials | M_[Name] |
| Material Instances | MI_[Name] |
| Textures | T_[Name] |
| Sound Waves / Cues | SW_[Name] / SC_[Name] |
| Niagara Systems | NS_[Name] |
| Anim Blueprints | ABP_[Name] |
| Animations / Montages | A_[Name] / AM_[Name] |

Reusable assets describe function, not mission number. Mission IDs belong only in documentation, changelog, commits, mission reports, and prototype map names.

---

# Git Workflow

Active Development

develop

Stable Releases

main

Never push failing code.

---

# Commit Messages

Examples:

feat: implement generator system

fix: resolve interaction regression

refactor: simplify inventory component

docs: update technical design

---

# Pull Request Checklist

- Compile passes
- PIE passes
- Regression verified
- Documentation updated
- Commit message follows convention

---

# Development Philosophy

Every feature should:

- Improve gameplay.
- Support the project vision.
- Be maintainable.
- Be testable.
- Be reusable.

Avoid unnecessary complexity.

---

# Documentation Workflow

Documentation is considered a living record.

Rules:

- Never rewrite historical changelog entries.
- Always append new entries.
- Preserve chronological history.
- Record gameplay systems, documentation updates, technical improvements, and bug fixes.
- Separate Canon from Recommendations.
- Documentation reflects approved decisions only.

---

# Unreal Engine Naming Standards

Version: 1.0 (DOC-002)

## General Principles

- Asset names should clearly describe their purpose.
- Avoid ambiguous or temporary names.
- Blueprint assets remain generic and reusable.
- Mission identifiers belong only to prototype map names (`LV_Prototype_PE###`), documentation, changelog, commits, and mission reports — not reusable assets or World Outliner labels.

---

## Blueprint Assets

Format: `BP_[Name]`

Examples

✓ BP_Generator

✓ BP_FuelCan

✓ BP_EmergencyLight

✓ BP_PoweredDoor

✓ BP_VentilationUnit

✓ BP_PASpeaker

✓ BP_DistantActivityHint

✗ BP_PE011_Generator

---

## Blueprint Components

Format: `BPC_[Name]`

Do not use `BP_*Component`.

Examples

✓ BPC_Interaction

✓ BPC_Objective

✓ BPC_Inventory

✓ BPC_Flashlight

✓ BPC_PowerReceiver

✗ BP_InteractionComponent

---

## Blueprint Interfaces

Format: `BPI_[Name]`

Examples

✓ BPI_Interactable

✓ BPI_PowerReceiver

---

## Widgets

Format: `WBP_[Name]`

Examples

✓ WBP_Objective

✓ WBP_NoteReader

---

## Enums

Format: `E_[Name]`

Examples

✓ E_GeneratorState

✓ E_DoorState

---

## Structs

Format: `ST_[Name]`

Examples

✓ ST_InventoryItem

✓ ST_ObjectiveData

---

## Maps

Prototype maps (mission IDs allowed):

`LV_Prototype_PE###`

Examples: `LV_Prototype_PE011`, `LV_Prototype_PE012`

Other map conventions (docs / future use):

- `LV_TestingGround` — general sandbox / systems testing
- `LV_ARI_*` — art / environment iteration maps

Rules

- Do not overwrite previous prototype maps.
- Preserve historical prototype levels.
- Prototype maps are used for regression testing and historical snapshots.

---

## Placed Actor Labels

Use descriptive World Outliner labels. Do not prefix actors with `PE###_`.

Examples

✓ Generator

✓ FuelCan

✓ PowerManager

✓ EmergencyLight_01

✓ EmergencyLight_02

✓ BrokenEmergencyLight

✓ AmbientFeedback

✓ PoweredDoor

✓ VentilationUnit

✓ PASpeaker

✓ DistantActivityHint

✗ PE012_Generator

✗ PE011_Light_A

---

## Avoid Generic Labels

Avoid

Light_A

Light_B

Broken

Ambient

Actor

Test

Cube

Sphere

Use descriptive labels instead.

---

## Numbering

Multiple actors of the same type should use two-digit numbering.

Example

EmergencyLight_01

EmergencyLight_02

EmergencyLight_03

---

## Folder Organization

Gameplay assets should remain organized by gameplay system under `Content/ProjectEcho`.

Example

Gameplay/

Doors/

Generator/

Lighting/

Items/

Notes/

Objectives/

Power/

Future gameplay systems should follow the same structure.

---

## Validation Checklist

Before completing every gameplay mission verify:

- Blueprint / component / widget / struct names follow Asset Naming Standard v1.0.
- Prototype map follows `LV_Prototype_PE###`.
- Actor labels are descriptive (no `PE###_` prefix).
- Generic labels removed.
- Assets remain reusable.
- Folder organization remains consistent.
- Redirectors fixed up after any rename.

---

# Mission Completion Report

Future gameplay missions must conclude with the following report.

---

Mission

PE-###

Status

Complete

Branch

<Branch Name>

Commit

<Commit Hash>

Blueprints Created

Blueprints Modified

Maps Created

Maps Modified

Documentation Updated

Compile

PASS / FAIL

Runtime Test

PASS / FAIL

Regression Test

PASS / FAIL

Git Commit

PASS / FAIL

Git Push

PASS / FAIL

Ready For Review

YES / NO

Notes

Implementation notes, limitations, or important observations.

---

# Prototype Map Purpose

Prototype maps exist to:

- Demonstrate newly implemented gameplay systems.
- Preserve historical development snapshots.
- Support regression testing.
- Provide isolated testing environments.

Prototype maps are development maps.

They are not production levels.

Production maps should be created separately and must not depend on prototype maps.

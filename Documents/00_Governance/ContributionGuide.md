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

Blueprints:

BP_

Widgets:

WBP_

Interfaces:

BPI_

Enums:

E_

Structs:

ST_

Components:

BP_[System]Component

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

## General Principles

- Asset names should clearly describe their purpose.
- Avoid ambiguous or temporary names.
- Blueprint assets remain generic and reusable.
- Mission identifiers belong only to prototype maps, placed actor labels, documentation, and mission reports.

---

## Blueprint Assets

Blueprint names must remain reusable.

Examples

✓ BP_Generator

✓ BP_FuelCan

✓ BP_EmergencyLight

✓ BP_PoweredDoor

✗ BP_PE011_Generator

---

## Prototype Maps

Every gameplay mission receives its own prototype level.

Naming

LV_Prototype_PE###

Examples

LV_Prototype_PE008

LV_Prototype_PE009

LV_Prototype_PE010

LV_Prototype_PE011

Rules

- Do not overwrite previous prototype maps.
- Preserve historical prototype levels.
- Prototype maps are used for regression testing and historical snapshots.

---

## Placed Actor Labels

Format

PE###_[ActorType]_[Number]

Examples

PE011_Generator

PE011_FuelCan

PE011_PowerManager

PE011_EmergencyLight_01

PE011_EmergencyLight_02

PE011_PoweredDoor

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

Examples

EmergencyLight

BrokenEmergencyLight

AmbientFeedback

PowerManager

Generator

---

## Numbering

Multiple actors should use two-digit numbering.

Example

PE011_EmergencyLight_01

PE011_EmergencyLight_02

PE011_EmergencyLight_03

---

## Folder Organization

Gameplay assets should remain organized by gameplay system.

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

- Blueprint names follow standards.
- Prototype map follows LV_Prototype_PE###.
- Actor labels are descriptive.
- Generic labels removed.
- Assets remain reusable.
- Folder organization remains consistent.

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

# Gameplay Systems

Status: Active

Version: 0.1

---

# Purpose

This document provides an overview of every gameplay system in Project Echo.

Each system is designed to be modular, reusable, and independently testable.

---

# Current Systems

## Movement

Status

Complete

Responsibilities

- Player movement
- Looking
- Sprinting (Future)
- Crouching (Future)

Dependencies

- Enhanced Input

---

## Interaction

Status

Complete

Responsibilities

- Detect interactable actors
- Display interaction prompts
- Execute Blueprint Interface calls

Dependencies

- BPI_Interactable

Used By

- Doors
- Notes
- Flashlight Pickup
- Fuel Can
- Generator

---

## Flashlight

Status

Complete

Responsibilities

- Equip flashlight
- Toggle light
- Future battery management

Dependencies

- Interaction System

---

## Inventory

Status

Complete

Responsibilities

- Store gameplay items
- Query required items
- Consume items

Current Items

- Facility Key
- Fuel Can

Future

- Batteries
- Access Cards
- Fuses

---

## Objectives

Status

Complete

Responsibilities

- Set objectives
- Complete objectives
- Update objective UI

Future

- Optional objectives
- Chapter objectives

---

## Generator

Status

Complete

Responsibilities

- Track generator state
- Consume fuel
- Broadcast power restoration

Dependencies

- Inventory
- Objectives

---

## Power System

Status

Complete (PE-011 / PE-012)

Responsibilities

- React to restored power
- Activate world systems
- Notify powered actors

Dependencies

- Generator

Receivers

- Emergency Lights
- Powered Door
- Power Ambient Feedback
- Ventilation Unit
- PA Speaker
- Distant Activity Hint

---

## World Response

Status

Complete (PE-012)

Responsibilities

- Play a once-only environmental response after power restoration
- Imply facility reactivation without revealing threat or story spoilers
- Encourage exploration through unlocked access and distant activity hints

Dependencies

- Power Manager
- BPI_PowerReceiver

---

## Asterion Development Testing Facility

Status

Complete (PE-013)

Map

`/Game/ProjectEcho/Maps/Development/LV_TestingGround`

Purpose

Permanent development sandbox (not campaign content) for validating and demonstrating gameplay systems in a believable Asterion Research Institute industrial/research layout.

Zones

1. Developer Spawn — safe start (`PlayerStart_DeveloperSpawn`), hub paths to all zones
2. Interaction Lab — doors, locked door, flashlight pickup, lab props
3. Generator Room — PE-011/012 power chain (`Generator`, `FuelCan`, `PowerManager`, `PoweredDoor`, emergency lights, `VentilationUnit`, `PASpeaker`, `DistantActivityHint`, ambient feedback)
4. Inventory & Objectives — notes, key item pickup, objective progression hooks
5. Puzzle Sandbox — reserved empty labeled area
6. Horror Corridor — dim lighting / ambience test (pipes + sparse red lights)
7. Future AI Arena — open space, no AI placed
8. Developer Control Room — reserved for future debug UI

Notes

- Actor labels are descriptive (DOC-002); no `PE013_*` mission prefixes
- Environment meshes referenced from ThirdParty packs (AbandonedPowerPlant, Laboratory, IndustryPropsPack6, IndustrialPipesM); vendor assets are not modified
- Prototype maps `LV_Prototype_PE011` / `LV_Prototype_PE012` remain for regression

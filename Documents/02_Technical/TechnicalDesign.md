# Technical Design

## Architecture

Project Echo uses a modular Blueprint architecture built around reusable components and interfaces.

---

## Core Components

PlayerCharacter

├── InteractionComponent

├── FlashlightComponent

├── InventoryComponent

├── ObjectiveComponent

---

## Communication

Preferred communication methods:

- Blueprint Interfaces
- Event Dispatchers

Avoid direct Blueprint references whenever possible.

---

## Gameplay Systems

Current:

- Interaction
- Flashlight
- Inventory
- Objectives
- Generator

Future:

- Power Manager
- Save System
- Witness AI
- Journal
- Audio Manager

---

## Folder Philosophy

Gameplay systems should remain modular and reusable.

Avoid monolithic Blueprints.
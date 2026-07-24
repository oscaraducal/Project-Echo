# Blueprint Architecture

Status: Active

Version: 0.1

---

# Philosophy

Project Echo follows a modular Blueprint architecture.

Every Blueprint should have a clear responsibility.

Avoid large, monolithic Blueprints.

---

# Core Architecture

PlayerCharacter

├── InteractionComponent

├── FlashlightComponent

├── InventoryComponent

├── ObjectiveComponent

---

# Communication

Preferred

Blueprint Interfaces

↓

Event Dispatchers

↓

Components

Avoid direct Blueprint references whenever possible.

---

# Gameplay Flow

Player

↓

Interaction Component

↓

Interactable Interface

↓

Gameplay Actor

↓

Gameplay Logic

---

# Power Architecture

Generator

↓

Event Dispatcher

↓

Power Manager

↓

Power Interface

↓

Lights

↓

Doors

↓

Ventilation / PA / Distant Activity

↓

Future Systems

---

# UI Architecture

Gameplay System

↓

Component

↓

Widget

↓

Player HUD

Widgets should never contain gameplay logic.

---

# Future Expansion

Future systems should plug into existing architecture instead of replacing it.
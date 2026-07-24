# Blueprint Architecture

Status: Active  
Version: 0.2  
Mission: PE-014 (pointer refresh)

---

# Philosophy

Project Echo follows a modular Blueprint architecture.

Every Blueprint should have a clear responsibility.

Avoid large, monolithic Blueprints.

For full implementation truth see:

- `GameplayFlow.md`
- `GameplaySystems.md`
- `Architecture/BlueprintDependencyMap.md`
- `Architecture/EventFlow.md`
- `BlueprintStandards.md`

---

# Core Architecture

```text
BP_PlayerCharacter
├── BPC_Interaction
├── BPC_Flashlight
├── BPC_Inventory
└── BPC_Objective
```

---

# Communication

Preferred

```text
Blueprint Interfaces
  → Event Dispatchers
  → Components
```

Avoid direct Blueprint references whenever possible.

---

# Gameplay Flow

```text
Player
  → BPC_Interaction
  → BPI_Interactable
  → Gameplay Actor
  → Gameplay Logic
```

---

# Power Architecture

```text
BP_Generator
  → OnPowerRestored (dispatcher)
  → BP_PowerManager
  → BPI_PowerReceiver / concrete receivers
  → Lights / Doors / Ventilation / PA / Distant Activity
  → Future Systems
```

---

# UI Architecture

```text
Gameplay System
  → Component
  → Widget (WBP_*)
  → Player HUD
```

Widgets should never contain gameplay logic.

---

# Future Expansion

Future systems should plug into existing architecture instead of replacing it.

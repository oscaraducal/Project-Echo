# ARCHITECTURE

GameMode

↓

PlayerController

↓

PlayerCharacter

↓

Gameplay Components

↓

Interaction

↓

Inventory

↓

Save System

Rules

PlayerController owns Input.

Character owns Movement.

Components own Features.

Interfaces connect systems.

Never use Event Tick for gameplay unless necessary.

Every system should be modular.

Avoid hard references when interfaces or components are appropriate.
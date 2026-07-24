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

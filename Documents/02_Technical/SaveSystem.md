# Save System

Status: Planning

Version: 0.1

---

# Purpose

This document outlines the future save system for Project Echo.

The save system has not yet been implemented.

---

# Design Goals

- Reliable
- Lightweight
- Expandable
- Easy to debug

---

# Save Philosophy

Saving should preserve tension.

The player should not be able to save at any moment.

Preferred save locations include:

- Safe Rooms
- Checkpoints
- Story Milestones

---

# Planned Data

Player

- Position
- Rotation

Inventory

- Keys
- Fuel
- Future Items

Objectives

- Current Objective
- Completed Objectives

World

- Open Doors
- Restored Power
- Puzzle States

Future

- Witness State
- Chapter Progress

---

# Technical Approach

Likely implementation:

SaveGame Object

↓

Game Instance

↓

Gameplay Systems

Detailed implementation will be designed closer to development.
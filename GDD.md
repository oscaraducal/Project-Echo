# PROJECT ECHO
Game Design Document (GDD)

Version: 0.1
Status: Living Document
Project Lead: Oscar
Technical Director: ChatGPT
Gameplay Engineer: Cursor AI

---

# 1. Vision

Project Echo is a first-person psychological horror game set inside the abandoned Asterion Research Institute.

Players uncover the truth behind a failed experiment known as Project Echo while surviving encounters with an unknown entity called The Witness.

The game focuses on atmosphere, exploration, environmental storytelling, and tension rather than combat.

---

# 2. Genre

Primary:
- First-Person Horror

Secondary:
- Puzzle
- Exploration
- Psychological Horror
- Narrative Adventure

---

# 3. Target Experience

The player should constantly feel:

- Curious
- Isolated
- Vulnerable
- Uneasy
- Rewarded for exploration

Fear should come from uncertainty instead of constant jump scares.

---

# 4. Core Gameplay Loop

Explore

↓

Observe

↓

Interact

↓

Collect

↓

Solve

↓

Progress

↓

Reveal Story

↓

Survive

↓

Repeat

---

# 5. Design Pillars

## Atmosphere Before Action

The environment creates tension before enemies do.

Lighting, sound, and pacing are more important than combat.

---

## Every Interaction Matters

Every object should have a purpose.

Examples:

- Door
- Note
- Generator
- Battery
- Key
- Terminal

No meaningless collectibles.

---

## Information Is Reward

Exploration reveals story.

The player should never feel forced to read lore, but those who do should better understand the mystery.

---

## The Witness Is Unpredictable

The Witness should not behave like a scripted monster.

Players should never be completely certain where or when it will appear.

---

# 6. Gameplay Systems

Current

✓ Movement

✓ Interaction

✓ Flashlight

✓ Inventory

Future

- Notes
- Locked Doors
- Generator
- Power Grid
- Save System
- Objectives
- Witness AI
- Audio Triggers
- Environmental Events

---

# 7. Player Goals

Immediate Goal

Escape the current area.

Short-Term Goal

Restore power.

Mid-Term Goal

Discover what happened.

Long-Term Goal

Escape the Asterion Research Institute.

---

# 8. Failure State

Player is caught by The Witness.

Future systems may include additional consequences based on game mechanics.

---

# 9. Player Progression

Progress is measured through:

- Knowledge
- Access to new areas
- Story discoveries
- Environmental changes

NOT by leveling or combat upgrades.

---

# 10. Save Philosophy

Players should feel tension.

Saving should be deliberate.

(Provisional until save system is designed.)

---

# 11. Technical Philosophy

- Blueprint-first development
- Component-based architecture
- Blueprint Interfaces
- Modular gameplay systems
- Git after every completed feature
- Every feature must compile cleanly
- Manual playtest required before merge

---

# 12. Definition of Done

A feature is complete when:

- Blueprint compile passes
- Runtime works
- Manual playtest passes
- No regressions
- Git commit completed
- Technical review approved

Only then is the feature considered merged.
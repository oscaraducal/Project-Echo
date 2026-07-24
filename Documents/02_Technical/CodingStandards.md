# Coding Standards

Status: Active

Version: 0.1

---

# Purpose

This document defines Blueprint development standards for Project Echo.

Consistency is more important than personal preference.

---

# Naming Conventions

Aligned with Project Echo Asset Naming Standard v1.0 (see ContributionGuide).

Blueprint

BP_

Component

BPC_

Widget

WBP_

Interface

BPI_

Enum

E_

Struct

ST_

Data Asset

DA_

Function Library

BFL_

---

# Blueprint Principles

One Blueprint

One Responsibility

Avoid duplicate logic.

Prefer Components over inheritance.

---

# Communication

Preferred order

1. Components
2. Blueprint Interfaces
3. Event Dispatchers

Avoid Cast To whenever practical.

---

# Graph Organization

- Use Comment Boxes
- Keep execution flow left to right
- Group related logic
- Remove unused nodes

---

# Variables

Expose variables only when necessary.

Use Categories.

Provide Tooltips where helpful.

---

# Performance

Avoid Tick unless required.

Prefer Events.

Reuse existing systems.

---

# Testing

Every Blueprint should compile without errors.

Every gameplay feature should be tested in PIE.

Regression testing is required before merge.
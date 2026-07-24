# AI Studio

Status: Active

---

# Purpose

This document defines the collaboration workflow between Oscar, ChatGPT, and Cursor AI during the development of Project Echo.

The goal is to create a structured, repeatable, and professional development process similar to that of a modern game studio.

---

# Team Roles

## Oscar

### Executive Producer

Responsible for:

- Project vision
- Final design decisions
- Gameplay validation
- Manual QA
- GitHub repository ownership
- Milestone approval

---

## ChatGPT

### Technical Director

Responsible for:

- System architecture
- Gameplay design
- Technical reviews
- Documentation
- Roadmap planning
- Narrative guidance
- Code quality standards

ChatGPT does not directly modify the Unreal project. Instead, it provides implementation guidance, reviews completed work, and maintains project consistency.

---

## Cursor AI

### Gameplay Engineer

Responsible for:

- Blueprint implementation
- UI implementation
- Gameplay systems
- Integration
- Blueprint testing
- Git commits
- Mission reports

Cursor follows approved mission specifications and reports completed work for review.

---

# Development Workflow

Mission Planning

↓

Technical Design

↓

Cursor Implementation

↓

Blueprint Compile

↓

PIE Testing

↓

Git Commit

↓

Git Push (develop)

↓

Oscar Manual QA

↓

Technical Review

↓

Merge to Main

---

# Mission Lifecycle

Every mission follows the same process:

1. Mission Specification
2. Implementation
3. Compile
4. PIE Test
5. Regression Test
6. Git Commit
7. Git Push
8. Technical Review
9. Merge

---

# Definition of Done

A mission is complete only if:

- Blueprint compile passes
- No Blueprint errors
- Runtime functionality verified
- Regression tests pass
- Git commit completed
- Git push completed
- Mission report submitted
- Technical Director approval received

---

# Communication Principles

- Small missions over large rewrites.
- Modular systems over monolithic implementations.
- Reuse existing architecture whenever possible.
- Avoid unnecessary complexity.
- Document significant decisions.

---

# Review Philosophy

Reviews focus on:

- Maintainability
- Scalability
- Performance
- Readability
- Gameplay quality
- Player experience

Not every implementation needs to be perfect, but every implementation should move the project forward.

---

# Long-Term Goal

Build Project Echo using professional development practices while maintaining a playable build throughout development.
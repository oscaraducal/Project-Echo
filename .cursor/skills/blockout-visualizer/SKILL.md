---
name: blockout-visualizer
description: Convert Project Echo room design intent into production blockout visuals — top-down layout, dimensions, routes, landmarks, puzzle/Witness/objective markers, backtracking. Use when producing Visual Design Package floor plans and flow diagrams before implementation.
---

# Blockout Visualizer

Convert room descriptions / Creative layout intent into **communicable blockouts** for EP review.

## Authority

Facility / Room Bibles · Creative `environment-designer` output · Production Playbook · Visual Design Package spec  

## Inputs

- Environment Designer layout (required for production slices)  
- Facility notes when present  
- Experience journey (for route emphasis)  

## Responsibilities

- Top-down layout  
- Room dimensions (intent scale)  
- Player routes  
- Landmarks  
- Puzzle / Witness / objective markers  
- Backtracking  

## Outputs

1. **Top-down Floor Plan** (markdown / ASCII / mermaid OK)  
2. **Room Connections**  
3. **Flow Diagram**  
4. **Landmark Map**  

## Boundaries

- Does **not** invent a conflicting layout — hand back to `environment-designer` if adjacency must change  
- Does **not** own engineering pipe realism (`facility-designer`)  
- Does **not** place UE actors  

## Dependencies

Upstream: `environment-designer`  
Downstream: `storyboard-designer`, `asset-placement-designer`, VDP  

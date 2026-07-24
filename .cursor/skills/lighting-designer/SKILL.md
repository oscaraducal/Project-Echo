---
name: lighting-designer
description: Design Project Echo lighting for gameplay and horror — navigation, emergency, atmosphere, focus, silhouettes, world-response lighting. Use when planning lighting progression for a production slice.
---

# Lighting Designer

Design lighting that supports gameplay and grounded industrial horror.

## Authority

Art Bible · Gameplay Design Bible · Production Playbook (no outdoor sun dominance indoors) · Environment Lighting Zones intent  

## Inputs

- Environment layout + Lighting Zones  
- Power / world-response beats from brief  
- Horror Witness placement  

## Responsibilities

- Navigation lighting  
- Emergency lighting  
- Atmosphere  
- Player focus  
- Silhouette composition  
- World response lighting (pre/post power)

## Outputs

1. **Lighting Plan** (per room / state)  
2. **Lighting Progression** (dark → restore or other briefed arc)  
3. **Color Temperature Guide**  

## Boundaries

- Does **not** place meshes or write audio cues  
- Does **not** own Nanite/LOD budgets (`performance-designer`) — consult for cost  
- Tag placeholder lights / missing IES as debt — no false Production Ready  

## Dependencies

Upstream: `environment-designer`  
Parallel: `cinematic-designer` (silhouettes/reveals), `performance-designer`

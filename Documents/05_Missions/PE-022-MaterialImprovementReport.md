# PE-022 — Material Improvement Report

**Mission:** PE-022 Medical Wing — AAA Environmental Art Pass  
**Map:** `/Game/ProjectEcho/Maps/Production/LV_ARI_MedicalWing`  
**Date:** 2026-07-25  

---

## Goals

- Replace repetitive default white-box read on floors/walls/ceilings
- Room-function material literacy (clinical tiles vs humidity dirt vs isolation wear)
- Prefer existing Office / APP material instances — no ripped game materials

---

## Overrides applied (StaticMeshComponent `OverrideMaterials`)

| Surface set | Material | Path | Rooms / use |
|-------------|----------|------|-------------|
| Floors (primary) | `M_Tiles_1` | `/Game/ThirdParty/Office_Pack_Vol_1/Materials/M_Tiles_1` | Transfer, Triage, Process, Nurse, OH, Records, Sec Check |
| Floors (clinical wet) | `M_Tiles_2` | `.../M_Tiles_2` | Exam, Pharmacy |
| Floors (contamination) | `M_Dirt_1` | `.../M_Dirt_1` | Observation, Quarantine Closet |
| Floors (service) | `MI_FactoryFloor` / concrete | APP Floor MIs | Isolation, Vent Access |
| Walls (clinical) | `M_Plaster_1` | Office Pack | Triage / Transfer / Process / Exam / OH / Records / Nurse / Pharm (re-affirmed after bad APP clad) |
| Walls (isolation) | `MI_Wall_Painted_Bottom_01` | APP Walls | Isolation geo |
| Walls (service/QC) | `MI_Wall_Bare_01` | APP Walls | Vent / Quarantine geo |
| Walls (obs humidity) | `M_Dirt_1` | Office | Observation geo |
| Ceilings (clinical) | `M_Plaster_1` | Office | Most rooms |
| Ceilings (humidity) | `M_Dirt_1` | Office | Isolation, Observation, Vent |
| Ceilings (service) | `M_Metal_1` | Office | Quarantine Closet |
| Stripe | `MI_Stripe_Green` | Project Echo | Retained teal literacy |

**Count:** ~95 geo actors re-materialized this pass.

---

## Decals (surface storytelling)

APP decal MIs on `DecalActor` instances (`Dressing/Decals`):

- `MI_Leak_01` / `MI_Leak_02` — Triage, Isolation, Process, Exam floor leaks
- `MI_Moss_01` / `MI_Moss_Wall_01` — Observation / QC / Vent humidity stains

---

## Rejected / removed material reads

- Abandoned Power Plant **wall cladding overlays** on Triage/Process — rusty/gold industrial read fought Medical fantasy; removed
- Laboratory `SM_wall` overlays — hazard striping; removed

---

## Remaining debt

- Procedural wear masks / unique cracked-tile MIs (need Quixel or custom)
- Readable painted MED-## door codes (texture work)
- Consistent UV scale on scaled BasicShape cubes (still cube-tiling artifacts at extreme scales)

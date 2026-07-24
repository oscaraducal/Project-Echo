# PE-022 — Asset Acquisition Report

**Mission:** PE-022 Medical Wing — World Polish  
**Date:** 2026-07-25  
**Policy:** Reuse → Starter/Engine → Fab free/licensed → Quixel → other legal only · never ripped commercial game assets

---

## Summary

**No new marketplace imports this pass.** All dressing used assets already present under `Content/` from prior project acquisition / Engine basics. Placement-only for PE-022 polish.

---

## Sources used (placement)

| Source | Content path | Usage in PE-022 | License / provenance note |
|--------|--------------|-----------------|---------------------------|
| Project Echo | `/Game/ProjectEcho/Environment/Materials/MI_Stripe_*` | Clinical teal stripe | First-party |
| Project Echo | `/Game/ProjectEcho/Gameplay/Interaction/BP_NotePickup` | Notes F–I instances | First-party |
| Unreal Engine | `/Engine/BasicShapes/Cube` | Floors, walls, ceilings, stripes (geo) | Epic Engine |
| Laboratory pack (existing in project) | `/Game/Laboratory/StaticMeshes/*` | Beds, IV, curtain, carts, fridge, racks, boards, lamps, medical props | Pre-existing project Content; Fab/marketplace provenance assumed from prior import — **no new download this mission** |
| Office Pack Vol 1 (existing) | `/Game/Office_Pack_Vol_1/Models/*`, `Materials/M_*` | Counters, chairs, cabinets, monitors, tables, sink, trash; plaster/tile/dirt mats | Pre-existing project Content — **no new download this mission** |
| Industry Props Pack 6 (existing) | `/Game/IndustryPropsPack6/Meshes/SM_Tarp01`, `SM_Hose01` | Quarantine tarp barricade; vent hose | Pre-existing — **no new download** |
| Industrial Pipes M (existing) | `/Game/IndustrialPipesM/models/pipe_m_l300_00` | Ceiling pipe runs | Pre-existing — **no new download** |

---

## Explicitly not used

- No ripped commercial game assets (Outlast / RE / Isolation / etc.).
- Abandoned Power Plant rubble / industrial barrels **removed** from Medical Wing this pass (wrong department fantasy).
- No Quixel pull this pass (debt: future clinical modular kit if EP prioritizes).

---

## Recommendation

If EP wants next fidelity jump: acquire **one** Fab clinical modular interior kit (walls/ceilings/doors matching teal stripe) under project license, document author + invoice in a follow-up Asset Acquisition append — do not mix five competing hospital kits.

---

## AAA Environmental Art Pass append (2026-07-25)

**Still no new marketplace downloads this pass.** Placement expanded to additional **already-in-repo** ThirdParty packs.

| Source | Content path | Usage this pass | License / provenance | NEW import? |
|--------|--------------|-----------------|----------------------|-------------|
| Abandoned Power Plant | `/Game/ThirdParty/AbandonedPowerPlant/Assets/Ceiling/*` | Ceiling frames + tiles | Pre-existing ThirdParty (Fab/marketplace prior) | **No** |
| Abandoned Power Plant | `.../Walls/SM_Pillar*`, `SM_Corner*`, window walls | Isolation structure / observation windows | Pre-existing | **No** |
| Abandoned Power Plant | `.../Doors/SM_Door_Single_01` | Isolation door visual framing | Pre-existing | **No** |
| Abandoned Power Plant | `.../Decals/MI_Leak_*`, `MI_Moss_*` | Floor/wall leak & humidity decals | Pre-existing | **No** |
| Abandoned Power Plant | `.../Floor/MI_FactoryFloor`, wall MIs | Isolation/Vent floor & accent mats | Pre-existing | **No** |
| Laboratory | `/Game/ThirdParty/Laboratory/StaticMeshes/*` | Carts, IV, beds, vents, wires, frames, signs, lockers | Pre-existing | **No** |
| Office Pack Vol 1 | `/Game/ThirdParty/Office_Pack_Vol_1/Models/*`, `Materials/*` | Cabinets, chairs, benches, `SM_Wall_Full_1`, plaster/tile/dirt | Pre-existing | **No** |
| Industrial Pipes M | `/Game/ThirdParty/IndustrialPipesM/models/pipe_m_l300_00` | Expanded ceiling pipe runs | Pre-existing | **No** |
| Industry Props Pack 6 | `/Game/IndustryPropsPack6/Meshes/SM_Tarp*`, boxes | Barricades / debris | Pre-existing | **No** |
| Construction VOL2 | `/Game/ThirdParty/Construction_VOL2/Meshes/SM_Plywood*`, `SM_Canister` | Barricade boards / decon canisters | Pre-existing | **No** |

### Explicitly not used

- No ripped RE7 / Alien Isolation / Callisto / Dead Space / Outlast meshes
- APP **industrial wall cladding** on Triage briefly placed then **removed** (wrong department fantasy)
- Laboratory `SM_wall` hazard overlays briefly placed then **removed**

### Recommendation (unchanged, higher urgency)

Acquire **one** Fab free/licensed **clinical modular interior** kit for walls/ceilings/doors — document creator, store listing, license, invoice in next Asset Acquisition append.

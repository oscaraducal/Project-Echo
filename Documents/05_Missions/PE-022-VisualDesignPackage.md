# PE-022 — Visual Design Package: Medical Wing (Unique Light VDP)

**Status:** Ready to Implement — Light VDP · **EP uniqueness correction applied**  
**Mission:** PE-022 Medical Wing  
**Map:** `/Game/ProjectEcho/Maps/Production/LV_ARI_MedicalWing`  
**Date:** 2026-07-25  
**Design Plan:** [`PE-022-DesignPlan.md`](PE-022-DesignPlan.md)  
**WORLD-001:** Inspiration only — [`WORLD-001/EnvironmentDesign.md`](WORLD-001/EnvironmentDesign.md) themes (teal, privacy, amber Isolation, paperwork). **Do not clone WORLD-001 blockout as playable L-hub.**  

---

> ### Gate
>
> WORLD-001 APPROVE + Implementation start = VDP proceed.  
> **EP correction:** Player must feel a **different building** than Generator / Coolant / Research / Security — not new paint on the same L-hub + triad puzzle.

---

## Creative intent — unique identity

| Intent | Spec |
|--------|------|
| **Massing** | Long **Triage Corridor** process spine (E–W), not center lobby hub |
| **Pinch** | **Isolation Anteroom** seals Observation until OH filing completes |
| **Solve landmark** | Glazed **OH Console bay** mid-corridor (south), facing triage — paperwork authority |
| **Human scale** | Exam Cubicle privacy curtain; Observation two-bed quiet |
| **Color temp** | Clinical cool white + desaturated teal stripe; amber **only** at Isolation |
| **Dressing density** | Clinical low–medium (Exam/Obs); paper-high (Records); avoid industrial junkpile |
| **Cut** | Never Armory/Restricted; never 3-station clearance clone |

---

## 1. Overview

| Field | Content |
|-------|---------|
| Fantasy | Occupational Health abandoned mid-Isolation filing — Protocol Card never reached the console |
| Length | ~15–20 min |
| Spaces | Transfer Vestibule · Triage Corridor · Exam Cubicle · OH Console Bay · Records Niche · Isolation Anteroom · Observation Bay + Soft Open egress |
| Ops | Protocol Card → OH Console file → Isolation opens |
| Horror | Witness on Observation egress after Isolation |
| Cuts | Combat · chase · triad stations · Security keycard redo · layout clone of PE-018–021 |

**Emotional curve:** Quiet vestibule → triage curiosity → paper focus → relief at Isolation open → Witness spike in Observation → Soft Open release.

---

## 2. Player journey

1. Soft Open into **Transfer Vestibule** (narrow). Note A.  
2. Enter **Triage Corridor** — teal stripe, askew chair, sightline toward Isolation amber (door sealed).  
3. **Exam Cubicle** — curtain / lamp / Note C.  
4. **Records Niche** — Protocol Card + Note B.  
5. **OH Console Bay** — file card → MarkSolved. Note D warning.  
6. **Isolation Anteroom** unlocks → **Observation Bay**.  
7. Witness on path to **Soft Open egress**. Stub next zone.

---

## 3. Top-down (unique — not L-hub)

```text
                    N
                    │
              ┌─────┴ Exam Cubicle ─────┐
 W  Transfer══╪════ Triage Corridor ════╪══ Isolation ══ Observation ══ SoftOpen (E)
              │         │               │   Anteroom        Bay
              │    OH Console (S)       │
              │         │               │
              └──── Records Niche ──────┘
```

Contrast PE-021: West entry → Center Lobby → N/E/S spurs → Far-S exit.  
Medical: **West→East process** with mid-spine solve and **east Isolation pinch** before egress.

---

## 4. Lighting mood

| Zone | Temp / intent |
|------|----------------|
| Vestibule / Triage | Cool clinical dim; flashlight-valuable corners |
| Exam | Soft pool on empty table (guidance without marker) |
| OH Console | Cool monitor glow — bureaucratic heart |
| Isolation | Single amber beacon silhouette |
| Observation egress / Witness | Colder spill; lower fill |
| Global | Kill outdoor Directional/Sky dominance |

---

## 5. Placement

**Interactive:** Notes A–D · ProtocolCard pickup · ObservationProtocolPuzzle (OH Console) · Isolation door · SoftOpenExit · WitnessPresence · SliceResetButton  

**Static:** Curtain/exam table intent · waiting chairs · chart rails · PPE cart at Isolation · Observation beds · teal stripe/decal intent via available materials  

**Density:** Avoid Security camera banks / badge trays as primary language.

---

## 6. Soft Open

| Link | Spec |
|------|------|
| Security SoftOpenExit_Stub → Medical | `SoftOpenLevelName=LV_ARI_MedicalWing`, `bTravelOnOpen=true` |
| Medical SoftOpenExit egress | Locked until WR; stub destination |

---

## 7. EP mental-play checklist

- [x] Topology is process spine + Isolation pinch (not L-hub clone)  
- [x] Ops is Protocol Card → OH file (not 3-station triad)  
- [x] Notes authored for Medical spaces  
- [x] Witness only post-solve on Observation egress  
- [x] Clinical cool lighting language  

**Ready to Implement:** **YES**

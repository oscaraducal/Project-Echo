# PE-022 — Lighting Improvement Report

**Mission:** PE-022 Medical Wing — World Polish  
**Map:** `/Game/ProjectEcho/Maps/Production/LV_ARI_MedicalWing`  
**Date:** 2026-07-25  

---

## Goals

- Clinical cool path guidance (cool white / soft teal)
- Amber landmark only at Isolation Anteroom
- Avoid map-wide red bloom
- Localized dark in Observation / Vent / Quarantine
- Soft fog for depth without milky whiteout

---

## Palette

| Role | Approx RGB | Use |
|------|------------|-----|
| Clinical cool | (0.78, 0.88, 0.95) | Transfer, Triage, Nurse, Pharmacy, OH, corridor |
| Teal accent | (0.35, 0.72, 0.78) | `Light_Triage_TealAccent` |
| Isolation amber | (1.0, 0.67, 0.24) | Isolation + small flicker cue |
| Dim clinical | (0.65, 0.72, 0.8) | Records, Observation, QC, Vent |
| Standby red (localized) | (0.85, 0.25, 0.2) | Transfer standby only — low intensity |

---

## Light inventory (Clinical folder)

**Retuned existing:** Transfer, Triage W/E, Teal accent, Exam, OH, Records, Corridor W/E, Isolation Amber, Observation W/E, Standby Red Transfer.

**Added:** Nurse Station, Pharmacy, Quarantine Closet, Security Med Check, Vent Access, Triage Mid, Corridor Mid, Exam Practical, Obs Bedside Dim, Iso Flicker Cue.

---

## Atmosphere

| Setting | Value / action |
|---------|----------------|
| Exponential Height Fog | Density ~0.03 · HeightFalloff ~0.2 · MaxOpacity ~0.55 |
| SkyAtmosphere / VolumetricCloud | Hidden (indoor clinical) |
| Path hierarchy | Brighter triage mid → cooler corridor → amber Isolation → dimmer Observation pools |

---

## Known editor warning

Viewport may show: *Cached lighting in Lumen and real-time sky capture lighting is going to be clipped* / `r.EyeAdaptation.CachedLightingPreExposure`.

**Status:** Documented debt — project-level CVar / PostProcess volume pass recommended; not changed globally this mission to avoid cross-map regressions.

---

## Validation

| Check | Result |
|-------|--------|
| Cool clinical dominant | **PASS** |
| Amber only at Isolation landmark | **PASS** |
| No map-wide red wash | **PASS** |
| Gameplay light receivers / WR lights | Untouched (ExitApproachAccent retained) |
| Human mood PIE | **PENDING_USER** |

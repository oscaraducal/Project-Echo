# PE-022 — Medical Wing (Occupational Health & Clinical Observation)

**Status:** Implemented — Technical + World Polish (Gameplay **PENDING_USER**)  
**Branch:** `develop`  
**Priority:** High  
**Map:** `/Game/ProjectEcho/Maps/Production/LV_ARI_MedicalWing`  
**Design authority:** Gameplay Design Bible · WORLD-001 inspiration only  
**Design plan:** [`PE-022-DesignPlan.md`](PE-022-DesignPlan.md)  
**Visual Design Package:** [`PE-022-VisualDesignPackage.md`](PE-022-VisualDesignPackage.md)  
**Playtest checklist:** [`PE-022-PlaytestChecklist.md`](PE-022-PlaytestChecklist.md)  
**World Polish:** [`PE-022-WorldPolishReport.md`](PE-022-WorldPolishReport.md) · [`PE-022-ReferenceAnalysis.md`](PE-022-ReferenceAnalysis.md) · [`PE-022-EnvironmentalStorytellingReport.md`](PE-022-EnvironmentalStorytellingReport.md) · [`PE-022-LightingImprovementReport.md`](PE-022-LightingImprovementReport.md) · [`PE-022-AssetAcquisitionReport.md`](PE-022-AssetAcquisitionReport.md)  
**Predecessor:** `LV_ARI_SecurityWing` SoftOpenExit_Stub → Medical Wing  
**Ready For Review:** **NO** (Gameplay PENDING_USER)

---

## Uniqueness vs PE-018–021 (required)

| Axis | Prior wings | PE-022 Medical |
|------|-------------|----------------|
| Topology | L-hub / center lobby + side rooms + south exit | **E–W Triage Corridor process spine** → Isolation Anteroom pinch → Observation → Soft Open east |
| Ops fantasy | Fuel / valves / 3 stations / keycard + 3 consoles | **Protocol Card → OH Console filing** (single clinical handshake) |
| Puzzle beat | Multi-station HOLD/ENGAGE triad | **Item-gated Fuse-family file** — zero CS/ST triad in map |
| Landmarks | Generator / hatch / cameras / lab glass | Teal corridor, Exam cubicle, glazed OH bay, Isolation amber cue, Observation beds |
| Exit | Hub south Soft Open | **Clinical egress beyond Observation** (Witness on Observation path) |
| Notes | Security/Research clearance language | Authored Medical transfer / IP-3 sleeve / interrupted exam / OH sticky / bedside scrap |

---

## Player Experience Goal

15–20 minute Medical beat after Security: explore a clinic process corridor, recover Protocol Card IP-3, file it at the OH Console, pass Isolation into Observation, Witness on Soft Open egress — no combat, chase, Armory, Restricted, or triad-station clone.

---

## Layout (+Y = North, +X = East) — World Polish scale (~95×54 m)

| Space | Approx | Role |
|-------|--------|------|
| Clinical Transfer Vestibule | x≈0 | Soft Open arrival; PlayerStart; Note A |
| Security Med Check | x≈−200, y≈1100 | Clearance medicals residue; Note H |
| Nurse Station | x≈900, y≈1400 | Roster / care coordination; Note I |
| Pharmacy | x≈900, y≈−1400 | Controlled stock; Note G |
| Triage Corridor | x≈2400 spine | Primary process hall (widened) |
| Exam Clinic | x≈1800, y≈2000 | Interrupted care; Note C |
| OH Console Bay | x≈2400, y≈−2000 | Filing puzzle solve; Note D |
| Records Office | x≈3800, y≈1800 | Protocol Card + Note B |
| Process Corridor | x≈4800 | Widened clinical hall |
| Quarantine Closet | x≈4800, y≈1400 | PPE staging; Note F |
| Vent Access | x≈4800, y≈−1400 | Engineering bleed into Medical |
| Isolation Anteroom | x≈6200 | Pinch + amber cue landmark |
| Observation Ward + Soft Open egress | x≈7800 | Note E; Witness; SoftOpenExit_ClinicalEgress |

---

## Objective Chain

| Trigger | Objective text |
|---------|----------------|
| Note B Protocol Sleeve `ObjectiveOnRead` | File the Protocol Card at the OH Console |
| OH Console `MarkSolved` | Access the clinical egress |

---

## Systems Reused / Created

- Notes: `BP_NotePickup` (authored Medical prose)
- Key item: `BP_KeyItemPickup` Protocol Card (`itemId=ProtocolCard`)
- Ops: `BP_OHConsoleFilingPuzzle` (thin FusePuzzle child) — **not** AccessClearance triad
- WR: SoftOpenExit_ClinicalEgress, Witness, EmergencyLights, Vent/PA/ambient/DistantActivity
- Horror: `BP_WitnessSilhouetteHint` (Observation egress; post-solve)
- Soft Open in: Security SoftOpenExit_Stub → `LV_ARI_MedicalWing`
- Reset: `BP_MedicalWingReset`
- Indoor Directional/Sky hidden

---

## Soft Open Level

| From | To | Actor |
|------|-----|--------|
| Security SoftOpenExit_Stub | `LV_ARI_MedicalWing` | `SoftOpenLevelName=LV_ARI_MedicalWing`, `bTravelOnOpen=true` |
| SoftOpenExit_ClinicalEgress | Stub next zone | Locked until WR; travel false / level None |

---

## Validation

| Gate | Status | Evidence |
|------|--------|----------|
| Compile | **PASS** | OHConsoleFilingPuzzle + MedicalWingReset compile via MCP |
| Technical | **PASS** | Map loads; unique spine actors present; triad/keycard absent; Protocol Card + OH filing configured; Soft Open Security→Medical wired; Simulate start/stop |
| Gameplay | **PENDING_USER** | Walk [`PE-022-PlaytestChecklist.md`](PE-022-PlaytestChecklist.md) |
| Replay | **PASS** (Technical) / **PENDING_USER** (manual) | SliceResetButton (`BP_MedicalWingReset`) present |

### Technical caveats

- Fuse-family PrintString debt may still say fuse language until overridden in graphs.
- IsolationAnteroomDoor is spatial pinch / landmark; Soft Open egress is the WR-unlocked exit.
- World Polish 2026-07-25: industrial leftover props removed; side rooms (Nurse / Pharmacy / Quarantine / Security Med Check / Vent) enclosed; clinical materials + cool/amber lighting; notes F–I placed — **no gameplay graph edits**.
- Editor may still warn on Lumen `CachedLightingPreExposure` (project-level debt).

---

## Debt

- True Fab/Quixel clinical modular kit (beyond plastered cubes + stripe MI)  
- Readable MED-## signage texture decals  
- Fuse PrintString / objective string parent debt on OHConsoleFiling  
- Human Gameplay + Replay  
- SoftOpenExit clinical egress destination TBD (Signal / deeper)  
- Lumen exposure CVar / PostProcess project pass  

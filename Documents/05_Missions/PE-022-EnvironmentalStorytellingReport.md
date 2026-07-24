# PE-022 — Environmental Storytelling Report

**Mission:** PE-022 Medical Wing — World Polish  
**Date:** 2026-07-25  
**Studio:** Content (+ Implementation placement)  
**Canon posture:** Symptoms-only · WORLD-001 inspiration · no Story Canon silent edits · no gameplay redesign

---

## Theme

Asterion **Occupational Health & Clinical Observation** after catastrophic containment / isolation protocol failure: interrupted exams, incomplete IP-3 filing, pharmacy seal breach, fitness-for-duty HOLDs tying Research exposure culture to Security clearance culture. Psychological contamination and abandoned procedure — not gore set dressing.

---

## Note placements (`BP_NotePickup` instance overrides only)

| Actor | Room | Title | Role |
|-------|------|-------|------|
| `Note_A_Transfer` | Clinical Transfer | Transfer Vestibule Scrap | Arrival bridge from Security |
| `Note_B_ProtocolSleeve` | Records | IP-3 Sleeve — Empty | **ObjectiveOnRead** → file Protocol Card (unchanged) |
| `Note_C_ExamInterrupted` | Exam Clinic | Exam Note — Interrupted | Care abandoned mid-session |
| `Note_D_OHWarning` | OH Console Bay | OH Console Sticky | Filing authority |
| `Note_E_ObservationScrap` | Observation | Bedside Scrap | Patient apprehension / Witness adjacency |
| `Note_F_QuarantineNotice` | Quarantine Closet | Quarantine Staging Notice | PPE / amber protocol literacy |
| `Note_G_PharmacySeal` | Pharmacy | Controlled Stock Exception | Seal breach; Security non-reply |
| `Note_H_FFDHold` | Security Med Check | Fitness-for-Duty HOLD — Cover Sheet | Research → Medical → Security chain |
| `Note_I_NurseRoster` | Nurse Station | Shift Roster Fragment | Understaffed night; incomplete Isolation log |

All new notes: `objectiveOnRead` empty — do not alter objective chain.

---

## Prop storytelling clusters (read without text)

| Cluster | Props | Reads as |
|---------|-------|----------|
| Care interrupted | Exam bed, curtain, lamp, IV, wash | Mid-exam evacuation |
| Filing authority | OH desk, monitor, board | Protocol Card destination |
| Quarantine staging | QC racks, PPE cart, quarantine sign | Containment prep abandoned |
| Pharmacy breach | Cabs, fridge ajar story, sharps proxy | Controlled stock failure |
| Security medicals | Check desk, clearance board, panel | Clearance medicals residue |
| Observation residue | Dual beds, curtains, IV, dim bedside | Clinical egress pressure |
| Vent bleed | Conditioner unit, hose, ladder, tools | Engineering humidity into Medical |
| Panic barricade | Tarp, abandoned gurney proxy | Institutional panic archaeology |

---

## Diegetic signage / boards (mesh stand-ins)

- Wayfinding board (triage entry)
- Isolation protocol sign (anteroom approach)
- Quarantine staging sign (closet)
- Nurse roster board / Security clearance board

True typography decals remain debt if mesh boards lack readable text at distance.

---

## Soft Open / Witness honesty

- Soft Open egress storytelling unchanged (Observation path).
- Witness silhouette placement untouched.
- Storytelling supports Isolation / filing fantasy without new mechanics.

---

## Debt

- Readable institutional font decals (MED-## room codes) not authored as textures this pass.
- Audio log scripts specified in WORLD-001 Content Package remain unvoiced (PrintString / no Wwise this mission).
- Morgue omitted — not a strong WORLD-001 / Story Bible fit for Occupational Health; quarantine closet covers containment residue.

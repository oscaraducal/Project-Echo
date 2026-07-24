# WORLD-001 — Visual Design Package (World-Building Previs)

**Status:** Ready for EP review (world-building VDP — **not** Ready to Implement gate)  
**Mission:** WORLD-001 — Medical Wing expansion  
**Type:** Adapted VDP for documentation / future PE handoff  
**Ready to Implement:** **N/A**  
**Linked Design Plan:** [`../WORLD-001-DesignPlan.md`](../WORLD-001-DesignPlan.md)  
**Environment intent:** [`EnvironmentDesign.md`](EnvironmentDesign.md)

---

> ### Gate note
>
> For PE gameplay slices, VDP EP APPROVE unlocks Implement.  
> For WORLD-001, this package lets the EP **mentally walk the department** and approve world cohesion.  
> A future Medical PE-### must produce its own gameplay VDP (loop, Witness beat, puzzle markers) before Unreal work.

---

## 1. Overview

| Field | Content |
|-------|---------|
| Fantasy | A quiet clinic that kept Asterion’s workforce “fit” — abandoned mid-care |
| Duration (mental walk) | ~8–12 minutes imagining exploration only |
| Rooms | 7 (M1–M7) |
| Systems reused (future) | Interaction, Notes, Terminals, Audio logs — **no new frameworks** |
| Cut list | Puzzles, combat, keycard solve, Witness chase scripting, Soft Open wiring |
| Horror register | Absence, HOLD bureaucracy, isolation amber, unfinished charts |

---

## 2. Player journey (exploratory — no solve)

```text
Clinical Transfer approach
  → Threshold triage residue
    → Exam Suite interrupted care
      → Observation protocol without patients
        → Records misfile / HOLD paper
          → Pharmacy seal breach
            → OH Console bureaucratic heart
              → Exit imagination toward Research or Security paper trail
```

Beginning: clinical stripe + transfer signage.  
Middle: human-scale rooms, paperwork density.  
Ending: OH Console as institutional “mind” of the wing — still not explaining Echo.

---

## 3. Top-down blockout

```text
                    [Research clinical link]
                              |
                    M7 Transfer Corridor
                              |
              +---------------M1 Threshold---------------+
              | waiting | desk | OH glass (M6) behind desk|
              +-----+------+------+------+---------------+
                    |      |      |      |
                  M2 Exam  |   M4 Rec  M5 Pharm
                           |
                        M3 Observation
```

| Room | Connections | Landmark | Env story marker | Puzzle/Witness markers |
|------|-------------|----------|------------------|------------------------|
| M7 Transfer | → M1 | Clinical Transfer sign | Dropped glove | None (WB) |
| M1 Threshold | → M2/M3/M4/M5/M6 | Intake desk | Clipboard mid-sentence | None |
| M2 Exam A | ← M1 | Exam lamp | Curtain drawn | None |
| M3 Observation | ← M1 | Amber beacon | Half-made bed | None |
| M4 Records | ← M1 | Open cabinet | Research tab misfile | None |
| M5 Pharmacy | ← M1 | Broken seal | Short count sheet | None |
| M6 OH Bay | ← M1 / visible from desk | Terminal | HOLD list on screen | None |

Routes: single primary loop from Threshold; dead-end suites force return through desk sightline (orientation).

---

## 4. Storyboard (ordered scenes)

| # | Scene | Player notices | Emotional beat |
|---|-------|----------------|----------------|
| 1 | Transfer | Teal stripe; AUTHORIZED STAFF | Threshold into care culture |
| 2 | Triage | Empty chairs; unfinished clipboard | Shift died mid-intake |
| 3 | Exam | Lamp on empty table | Care without patient |
| 4 | Observation | Amber + PPE cart | Protocol > people |
| 5 | Records | HOLD sheet; Research tab | Bureaucracy of fear |
| 6 | Pharmacy | Broken seal | Scarcity / breach |
| 7 | OH Console | HOLD queue on CRT/LCD | Fitness as control |
| 8 | Leave (imagined) | Paper trail toward Security / Research | Cohesion without quest arrow |

---

## 5. Hero concept prompts (prompts only)

### Hero — Clinical Threshold

> Dim abandoned occupational health triage desk in a classified research institute, seafoam wainscot, vinyl floor scuffs, three waiting chairs one askew, clipboard on floor, teal department stripe on wall, cold fluorescent flicker, no people, psychological horror atmosphere, grounded industrial medical, Unreal Engine cinematic still, desaturated teal and gray

### Hero — Observation Bay

> Two clinical observation beds one stripped one half-made, amber isolation beacon above door, PPE cart, stained acoustic ceiling tile, privacy curtain track, emergency-adjacent soft red exit sign distant, empty, tense quiet, photoreal environment concept

### Hero — OH Console Bay

> Small glazed occupational health office, dual monitors showing redacted employee HOLD queue, badge printer jam, shift roster half-erased, desk phone crooked, teal UI glow on face of empty chair, bureaucratic dread

### Supporting — Exam Suite / Pharmacy / Records

> (Exam) Gooseneck lamp illuminating empty exam table paper roll, curtain 70% drawn, stainless sink, abandoned vitals cuff  
> (Pharmacy) Glass cabinet with broken paper seal tag, sharps container overfull, medical fridge door ajar dark interior  
> (Records) Lateral files one drawer open, color-tab binders, stamp set FIT HOLD REFER TO SECURITY, overflowing shred bin

---

## 6. Lighting concepts

World-building lighting states (not power-puzzle beats):

| State | Intent |
|-------|--------|
| **Abandoned baseline** | 30–40% fluorescents; several dead tubes; flashlight-valuable corners in Records / Pharmacy |
| **Clinical pools** | Soft pools on desk, exam lamp, OH screens — guidance without quest markers |
| **Amber Isolation** | Single warm amber at Observation door — readable silhouette cue |
| **Emergency bleed** | Distant exit red only; do not wash Medical in Engineering orange |
| **Optional future “partial restore”** | If a later PE restores branch power: more even clinical white — still cold |

Shadow priorities: under beds, inside open cabinets, pharmacy depth.

---

## 7. Asset placement (readability)

### Interactive (future PE)

- Notes / clipboards (Threshold, Exam, Records, Pharmacy)  
- OH Console + Records terminal  
- Audio log devices (1–2)  
- Optional clearance wall reader (display only)

### Static hero

- Exam table, curtains, beds, file cabinets, pharmacy shelving, waiting chairs, OH desk

### Decals

- Floor scuffs, water stain under Observation ceiling, seal tape residue, wayfinding vinyl discs (one missing)

### Storytelling clusters

See Narrative ES-01…ES-07 — place for silhouette readability from Threshold sightlines where possible (Exam lamp glow visible from desk).

### Density

- Threshold: medium clutter  
- Exam / Obs: low–medium (clinical)  
- Records: high paper density  
- Pharmacy: medium shelving rhythm  
Avoid junkpile horror.

---

## 8. Rhythm (exploration analogue)

```text
Approach → Observe → Read residue → Cross-check departments → Leave with questions
```

Maps to Gameplay Design Bible loop **without** Operate / World Response / Witness scripted beats in WORLD-001.

---

## 9. Env story map (summary)

```text
Transfer (adjacency)
    ↓
Threshold (evacuation intake)
    ↓
Exam (interrupted care) ←→ Observation (protocol without patients)
    ↓
Records (HOLD + Research bleed) ←→ Pharmacy (breach)
    ↓
OH Console (institutional mind)
```

---

## 10. Room purposes (Room Bible compliance)

| Room | Used for? | Happened? | Why player later? |
|------|-----------|-----------|-------------------|
| Threshold | Intake / waiting | Mid-shift abandon | Orient + first notes |
| Exam A | Occupational exams | Session interrupted | Human voice note |
| Observation | Short-stay / isolation | Patients gone; protocol staged | Atmosphere + WO note |
| Records | Charts / FFD covers | Misfile + HOLD | Lore + Security link |
| Pharmacy | Controlled supply | Seal breach | Scarcity subplot |
| OH Console | Fitness determinations | Session open | Terminal heart |
| Transfer | Clinical link | Staff flight | Research cohesion |

---

## 11. EP mental-play checklist (world package)

- [ ] I understand Medical’s workplace function  
- [ ] I can picture walking M1→M7 without a puzzle  
- [ ] Research and Security cohesion is clear on paper  
- [ ] Horror is bureaucratic / absent-care, not gore  
- [ ] I accept Ready to Implement = N/A  

**EP VDP decision (world-building):** ☐ APPROVE ☐ RETURN

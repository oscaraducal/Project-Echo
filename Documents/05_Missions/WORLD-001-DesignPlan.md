# WORLD-001 — Design Plan: Expand the World – Asterion Research Institute

**Status:** Approved — awaiting Implementation Studio handoff (N/A until future PE mission builds Medical Wing)  
**Mission ID:** WORLD-001  
**Type:** World-building / AI Studio Content validation — **NOT** a PE gameplay slice  
**Branch:** `develop`  
**Date:** 2026-07-25  
**Ready to Implement:** **N/A** — no Unreal implementation in this mission  
**Package folder:** [`Documents/05_Missions/WORLD-001/`](WORLD-001/README.md)  
**Expansion mirror:** [`Documents/03_World/Expansions/WORLD-001/`](../03_World/Expansions/WORLD-001/README.md)

---

> ### EP Gate
>
> **EP decision:** **APPROVE**  
> **Status:** Approved — awaiting Implementation Studio handoff (N/A until future PE mission builds Medical Wing)  
> **Date:** 2026-07-25  
>
> WORLD-001 is world-building authority for Medical Wing documentation.  
> Does **not** set Ready to Implement on any map. Does **not** authorize Blueprint / map / asset changes.  
> Does **not** auto-start a Medical Wing PE gameplay mission.

---

## Mission Brief

| Field | Content |
|-------|---------|
| **Mission** | WORLD-001 — Expand the World (Asterion Research Institute) |
| **Goal** | Enrich one under-documented facility department so existing production wings feel like parts of a real institute, not isolated demos. |
| **Selected expansion** | **Medical Wing — Occupational Health & Clinical Observation** |
| **Why this (not Admin / Electrical / Restricted)** | Facility Bible lists Medical (Examination Rooms, Laboratories) but production maps never dress it. Medical is the believable **human residue bridge** between Research Wing (PE-020 — exposure / observation culture) and Security Wing (PE-021 — clearance / fitness-for-duty). Administration is thinner atmospherically; Electrical Control retreads PE-017A; Restricted / Project Echo Wing is too early and would force canon spoilers. |
| **Cohesion target** | Soft adjacency to Research Wing clinical transfer language + Security medical-fitness clearance paperwork — symptoms and paperwork trails, not quest routes. |
| **Player experience (future)** | When a later PE-### implements Medical, the player should already have a coherent workplace grammar from this package. WORLD-001 itself has **no playable loop**. |
| **Out of scope** | Puzzles, combat, enemy encounters, mission scripting, Witness encounter design as gameplay, Unreal assets, Soft Open wiring, SliceReset, Gameplay PASS claims |

---

## Selection rationale (candidates)

| Candidate | Verdict |
|-----------|---------|
| **Medical Wing (Occupational Health & Clinical Observation)** | **Selected.** Under-documented Facility Bible zone. Strengthens Research ↔ Security cohesion via fitness-for-duty, incident intake, isolation observation, and records culture. High environmental storytelling density without inventing Project Echo purpose. |
| Administration / Offices | Strong institutional voice, but weaker visual horror residue and less adjacency to current production chain (Eng → Research → Security). Defer. |
| Engineering Electrical Control | Adjacent to Maintenance / Generator / Coolant, but fuse literacy owned by PE-017A; risk of retread. Defer. |
| Public Reception | Valuable later for tutorial / arrival; not the cohesion gap after PE-020/021. Defer. |
| Restricted / Project Echo Wing | Far too early; would pressure Canon spoilers. Forbidden for WORLD-001. |

---

## Scope of world update

### In scope (documentation)

1. **Facility / department expansion** — Medical Wing purpose, sub-rooms, adjacency to Research & Security, naming conventions.  
2. **Creative identity** — architecture, materials, signage, props, furniture, themes (`EnvironmentDesign.md`).  
3. **Narrative content** — in-world documents, emails, security notices, lab/clinic notes, audio log scripts, terminal prose, env storytelling beats, collectible recommendations (`ContentPackage-Narrative.md`).  
4. **World Building** — department structure, org hierarchy proposals, timeline enrichment proposals, technologies / programs naming (`ContentPackage-WorldBuilding.md`) — **Canon Proposals**, not silent bible rewrites.  
5. **UX specs** — clinic terminal layouts, security-adjacent medical clearance panels, keypad / notification examples (`ContentPackage-UX.md`) — specs only.  
6. **Previs VDP** — adapted for world-building (layout, mood, lighting, env story map, asset placement, room purposes) — not a gameplay loop approval (`WORLD-001-VisualDesignPackage.md`).  
7. **Canon Validation** — pass/fail vs Story / Facility / Room bibles (`WORLD-001-CanonValidationReport.md`).  
8. **Executive assembly** — package index + EP decision block (`WORLD-001-ExecutiveSummary.md`).

### Explicit cuts

- No PE-### map creation (`LV_ARI_MedicalWing` name reserved as **proposal only**).  
- No puzzle family assignment (Security & Access / Research Equipment / Mechanical remain owned by prior missions).  
- No Witness chase / combat ADR.  
- No Glossary / Story Bible silent edits — flagged Recommendations only.  
- No gameplay validation, Technical Simulate, or Human PIE.

---

## Authority & compliance

| Authority | Application |
|-----------|-------------|
| Story Bible | Setting, Witness uncertainty, environmental storytelling style — preserved |
| Facility Bible | Medical zone exists; WORLD-001 **enriches** Examination / Laboratories without replacing Engineering / Security / Research ownership |
| Room Bible | Every proposed room answers function / what happened / why player might later be there |
| Gameplay Design Bible | Zones remain legible; no new mechanics; Medical Keys primer language respected as future item family only |
| Production Playbook | Docs-only mission; no Implement; git commit as EP-requested for this package |
| ADRs | No new ADR required unless EP APPROVE elevates specific Canon Proposals into bible edits |

---

## Proposed room set (world-building; ≤7 spaces)

| ID | Room | Function | Story residue |
|----|------|----------|---------------|
| M1 | Clinical Threshold / Triage Desk | Intake, badge check, waiting chairs | Evacuation mid-shift; clipboard unfinished |
| M2 | Examination Suite A | Routine occupational exams | Half-drawn curtain; vitals cuff abandoned |
| M3 | Observation Bay (Isolation-capable) | Short-stay clinical observation | Beds stripped; isolation light still armed |
| M4 | Records Alcove | Charts, clearance binders, redacted folders | Cabinet ajar; one folder misfiled toward Research |
| M5 | Pharmacy / Clinical Supply | Controlled meds, PPE, sharps | Inventory partial; lockdown seal broken once |
| M6 | Occupational Health Console Bay | Fitness-for-duty / clearance workstation | Terminal mid-login; Security CC chain |
| M7 | Transfer Corridor (Research Clinical Link) | Soft adjacency language to Research Wing | Signage: CLINICAL TRANSFER — AUTHORIZED STAFF |

Future PE map may cut rooms; WORLD-001 documents the full coherent department.

---

## Narrative rules (hard)

- Symptoms, not walkthroughs.  
- Do not explain The Witness.  
- Do not disclose Project Echo true purpose.  
- Medical content = workplace medicine + occupational health under classified research pressure — not body-horror spectacle for its own sake.  
- Prefer paperwork, protocols, unfinished care over gore.

---

## Deliverables checklist

| Deliverable | Path | Status |
|-------------|------|--------|
| Design Plan (this doc) | `Documents/05_Missions/WORLD-001-DesignPlan.md` | **APPROVED** (2026-07-25) |
| Package README | `Documents/05_Missions/WORLD-001/README.md` | Complete |
| Environment Design | `Documents/05_Missions/WORLD-001/EnvironmentDesign.md` | Complete |
| Content — Narrative | `Documents/05_Missions/WORLD-001/ContentPackage-Narrative.md` | Complete |
| Content — World Building | `Documents/05_Missions/WORLD-001/ContentPackage-WorldBuilding.md` | Complete |
| Content — UX | `Documents/05_Missions/WORLD-001/ContentPackage-UX.md` | Complete |
| Visual Design Package | `Documents/05_Missions/WORLD-001/WORLD-001-VisualDesignPackage.md` | Complete |
| Canon Validation | `Documents/05_Missions/WORLD-001/WORLD-001-CanonValidationReport.md` | Complete |
| Executive Summary | `Documents/05_Missions/WORLD-001/WORLD-001-ExecutiveSummary.md` | Complete |
| Expansion index mirror | `Documents/03_World/Expansions/WORLD-001/README.md` | Complete |

---

## Risks

| Risk | Mitigation |
|------|------------|
| Medical content invents Subject / Echo spoilers | Canon Validation + lore rules; keep Incident details withheld |
| Future PE implementers treat WORLD-001 as Ready to Implement | Explicit N/A Ready to Implement; VDP labeled world-building previs |
| Named characters silently become Canon | All names tagged **Canon Proposal** until EP/ADR |
| Scope creep into Admin + Medical + Signal | Single department lock; cuts listed |

---

## Approval Block

| Field | Value |
|-------|-------|
| Ready for EP Review | **YES** (complete) |
| Ready to Implement | **N/A** |
| EP decision | **APPROVE** |
| Status | Approved — awaiting Implementation Studio handoff (N/A until future PE mission builds Medical Wing) |
| Date | 2026-07-25 |
| Follow-up | Optional: elevate selected Canon Proposals (R1–R6) via ADR; schedule future PE-### Medical spatial slice only when EP starts that mission |

**EP decision:** ☑ APPROVE ☐ RETURN  

**EP notes:** Package approved as Medical Wing world-building authority. No Unreal / no auto-start Medical Wing PE mission.

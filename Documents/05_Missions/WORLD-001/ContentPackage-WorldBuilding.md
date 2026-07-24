# WORLD-001 — Content Package: World Building Division

**Status:** Ready for EP review  
**Mission:** WORLD-001 — Medical Wing world expansion  
**Division:** Content Studio — World Building  
**Canon posture:** **Canon Proposals** and enrichment guides — **do not** silently rewrite Story / Facility / Room bibles  
**Validation:** See `WORLD-001-CanonValidationReport.md`

---

## 1. Expansion thesis

Asterion’s Medical department existed to keep a classified workforce **fit for duty**, not to be a public hospital. Under Project Echo pressure it became the institute’s quiet ledger of **symptoms without diagnoses** — the paperwork bridge between Research exposure culture and Security access control.

This strengthens cohesion with:

- **Research Wing (PE-020)** — observation / containment culture; personnel rotate through clinical checks.  
- **Security Wing (PE-021)** — clearance renewals depend on Fitness-for-Duty.  
- **Engineering chain (PE-017A / 018 / 019)** — facility humidity / power / coolant irregularities appear as Medical work orders, not as Medical puzzles.

---

## 2. Facility history enrichment (Proposal)

| Phase | Medical role (proposal) |
|-------|-------------------------|
| Phase 1 — Construction | Medical sized as **Occupational Health + short-stay Observation** for a research campus (not trauma center). |
| Phase 2 — Project Echo begins | Medical gains **Clearance Medical** mandate for Restricted-adjacent zones; staffing increases; Records digitization starts. |
| Phase 3 — Anomalies | SYM clusters appear in FFD queues; Isolation amber used more; Pharmacy shrinkage; Engineering humidity tickets rise. |
| Phase 4 — Incident | Mid-shift abandonment; HOLD lists uncleared; seals broken; Director elevation locks Incident charts. |
| Phase 5 — Present | Player may later traverse residue; truth still hidden. |

**Canon note:** Timeline phases preserved; Medical detail is additive proposal only.

---

## 3. Department structure (Proposal)

```text
Medical Director
├── Clinical Services
│   ├── Examination Suite(s)
│   └── Observation / Isolation Bay
├── Occupational Health (OH)
│   ├── Fitness-for-Duty Desk
│   └── Clearance Medical Liaison (→ Security)
├── Clinical Supply / Pharmacy
└── Medical Records
```

**Out of scope for Asterion Medical (proposal):** public ER, surgery theater as hero space, maternity, long-term psych ward branding. Isolation is short-stay clinical observation only.

---

## 4. Organizational hierarchy (Proposal)

| Role | Reports to | Interfaces |
|------|------------|------------|
| Medical Director | Administration (Executive chain unspecified) | Security Chief (clearance), Research leads (exposure events) |
| Clinicians | Medical Director | OH Desk, Records |
| OH Technician | Medical Director / OH Desk | Security Clearance Desk |
| Pharmacy Tech | Medical Director | Facilities / Engineering for cold chain |
| Records Clerk | Medical Director | All depts (chart custody) |

Characters.md lists **Medical Director** as future character — WORLD-001 proposes **Dr. Elena Voss** as candidate fill (EP/ADR required to promote).

---

## 5. Scientific / clinical programs (Proposal naming)

| Program ID | Name | Purpose (diegetic) | Spoiler control |
|------------|------|--------------------|-----------------|
| OH-FFD | Fitness-for-Duty Program | Periodic exams + symptom holds | No Echo purpose |
| OH-CM | Clearance Medicals | Medical gate for Zone C+ | Aligns Security literacy |
| CLIN-OBS | Clinical Observation Protocol | Short-stay monitoring | Not containment science (Research owns containment) |
| SYM-04 | Symptom Cluster Code | Sleep / apprehension / “watched” language | Track symptoms only |
| IP-3 | Isolation Protocol 3 | Amber-lit entry control | Clinical, not Security detention |

**Boundary:** Research owns experiment chambers / containment handshake (PE-020). Medical owns **human clinical observation** and **occupational fitness**. Do not merge into a second Research Wing.

---

## 6. Technologies & equipment naming (Proposal)

| Term | Definition |
|------|------------|
| Amber Isolation Indicator | Door beacon tied to IP-3 |
| OH Console | Occupational Health workstation (audited) |
| FFD Determination | FIT / HOLD / REFER TO SECURITY |
| Clinical Transfer | Authorized movement path Medical ↔ Research clinical link |
| Controlled Cabinet B | Pharmacy sealed stock |
| Zone C | Security clearance tier requiring current FFD (ties PE-021 without defining all zones) |

Glossary additions recommended only after EP APPROVE (see Canon Validation Recommendations).

---

## 7. Timeline update proposals

| ID | Proposal | Action if APPROVE |
|----|----------|-------------------|
| TL-P-01 | Add under Phase 2: “Occupational Health clearance medicals mandated for Restricted-adjacent access.” | Append Timeline.md subsection |
| TL-P-02 | Add under Phase 3: “Medical FFD HOLD volume rises; Isolation protocol exercised.” | Append Timeline.md |
| TL-P-03 | Add under Phase 4: “Medical mid-shift abandonment; Director-sealed incident charts.” | Append Timeline.md |

Until APPROVE: remain proposals in this package only.

---

## 8. Naming conventions

| Element | Convention | Example |
|---------|------------|---------|
| Room codes | `MED-##` | MED-03 Observation Bay |
| Bulletins | `OHB-##` | OHB-12 |
| Work orders | `WO-MED-###` | WO-MED-441 |
| Isolation | `IP-#` | IP-3 |
| Email domain | `@asterion.internal` | proposal only |
| Map name (future) | `LV_ARI_MedicalWing` | reserved proposal — not created |

Align existing: Asterion, Project Echo, The Incident, The Witness, Generator Room / Restricted Wing glossary terms unchanged.

---

## 9. Culture & documentation standards (Medical voice)

From Culture Designer posture (guidance for writers):

- Clinical, clipped, liability-aware.  
- Prefer codes (SYM-04, HOLD) over sensational adjectives.  
- Never write patient entertainment horror monologues.  
- Redact PHI aggressively in player-facing props.  
- Conflict with Security tone: Medical says “clinical”; Security says “clearance.”

---

## 10. Facility Bible enrichment (Proposal text block)

If EP elevates via ADR, suggested Facility Bible Medical expansion:

```markdown
## Medical

- Clinical Threshold / Triage
- Examination Suites
- Observation Bay (Isolation-capable)
- Occupational Health Console
- Medical Records
- Pharmacy / Clinical Supply
- Clinical Transfer link toward Research

Purpose: Occupational health, fitness-for-duty, short-stay clinical observation.
Does not replace Research containment or Security detention.
```

Until ADR: Facility Bible remains Version 0.1 as-is; this block is proposal only.

---

## 11. Adjacency map (world cohesion)

```text
[Research Wing] --Clinical Transfer--> [Medical Wing] --FFD / Clearance paper--> [Security Wing]
        ^                                      |
        |                                      v
   containment / obs                     Engineering WOs
   (PE-020 literacy)                    (humidity / power residue)
```

Engineering zones remain physically upstream in campaign order; Medical paperwork may reference them without requiring Medical to sit between Coolant and Research in Soft Open chain.

**Campaign note (non-binding):** Future PE Medical slice may Soft Open from Research clinical exit **or** Security reverse-discovery — EP chooses later. WORLD-001 does not lock Soft Open order.

---

## 12. World Building checklist

- [x] Department structure  
- [x] Org hierarchy proposals  
- [x] Programs / technologies naming  
- [x] Timeline proposals (flagged)  
- [x] Naming conventions  
- [x] Canon vs Proposal separation  
- [x] Cohesion with PE-020 / PE-021 / Engineering

# PE-022 — Design Plan: Medical Wing (Occupational Health & Clinical Observation)

**Status:** APPROVED & Ready to Implement — EP Implementation start 2026-07-25 · **EP uniqueness correction applied**  
**Branch:** `develop`  
**Priority:** High (campaign beat after PE-021 Security Wing)  
**Map:** `/Game/ProjectEcho/Maps/Production/LV_ARI_MedicalWing`  
**Wing name:** **Medical Wing** (Occupational Health & Clinical Observation)  
**Design authority:** `Documents/01_Game_Design/GameplayDesignBible.md` (PE-016)  
**World authority:** WORLD-001 package = **inspiration / recommendation only** — not a template to clone  
**Puzzle framework:** PE-015 systems reuse — **unique player fantasy & spatial beat** (no PE-019/020/021 find-replace)  
**Map recipe:** PE-018 = **production process recipe** (GameMode, Soft Open, SliceReset, indoor light kill) — **not** geometry clone of Annex/Coolant/Research/Security  
**Fuse path:** Owned by **PE-017A** — do not duplicate  
**Predecessor:** `LV_ARI_SecurityWing` SoftOpenExit_Stub → Medical Wing  
**Mission notes:** [`PE-022-MedicalWing.md`](PE-022-MedicalWing.md)  
**VDP:** [`PE-022-VisualDesignPackage.md`](PE-022-VisualDesignPackage.md)  

---

> ### Gate
>
> **Design Plan:** Accepted via EP Implementation start.  
> **VDP proceed:** WORLD-001 APPROVE + Implementation start (Light VDP).  
> **EP correction (2026-07-25):** Medical Wing must be **spatially and mechanically unique** — WORLD-001 inspires themes; PE-018–021 supply systems, not layouts or puzzle carbon-copies.  
> Does **not** waive Story Canon or Human Gameplay PASS.

---

## Uniqueness contract (vs PE-018–021)

| Axis | PE-018–021 pattern (do **not** clone) | PE-022 Medical (required) |
|------|--------------------------------------|---------------------------|
| **Topology** | L-hub / center lobby + 3 side rooms + south exit corridor | **Linear clinical process spine** → **Isolation Anteroom pinch** → Observation egress |
| **Landmark language** | Generator / hatch / cameras / lab glass | Teal clinical stripe, privacy curtain, amber Isolation beacon, chart rails, glazed OH bay |
| **Ops fantasy** | Fuel / valves / 3 calibration stations / keycard + 3 clearance consoles | **Recover Protocol Card → file at OH Console → Isolation releases** (one clinical handshake) |
| **Puzzle beat** | Multi-station HOLD/ENGAGE triad | **Item + single console procedure** — no open-three/close-one station set |
| **Lighting** | Industrial amber / plant / checkpoint dim | **Clinical cool** (cool white / desaturated teal spill); amber only on Isolation |
| **Exit path** | Hub → south Soft Open | **Through Isolation Anteroom into Observation → Soft Open clinical egress** |
| **Notes** | Find-replace Security/Research IDs | **Authored Medical prose** (WORLD-001 ideas rewritten for this topology) |

**Allowed reuse:** Interaction, Inventory KeyItem, Notes, Objectives, thin `BP_PuzzleBase` child, LockedDoor / SoftOpenExit / Power receivers, Witness silhouette, SliceReset twin, Soft Open Level travel, GameMode/player — **systems, not layout.**

---

## Connection from Security Wing

| From | To | How |
|------|-----|-----|
| Security SoftOpenExit_Stub | Medical **Clinical Transfer Vestibule** | Soft Open Level after PE-021 clearance |

**Narrative bridge:** Clearance is live enough that Occupational Health residue matters — incomplete Isolation paperwork still holds the clinical egress. Symptoms only; no quest dump.

---

# Mission Brief

| Field | Content |
|-------|---------|
| **Mission** | PE-022 Medical Wing |
| **Player experience goal** | 15–20 min: walk a **clinic process corridor** (not another checkpoint lobby), read interrupted care, recover a **Protocol Card**, file it at the **OH Console**, pass the **Isolation Anteroom** into Observation, meet Witness on clinical egress Soft Open — no combat/chase/Armory/Restricted. |
| **Teaching beat** | Fitness / observation paperwork as progression (care-as-procedure) — distinct from Engineering resources, Research calibration stations, and Security clearance consoles. |
| **End state** | OH Console handshake complete → Isolation unlock + Soft Open unlock → Witness on Observation egress → stub Soft Open next zone. |
| **Target length** | ~15–20 minutes. ≤6 spaces. Cut Records niche before adding mechanics. |

---

# Gameplay Loop

```text
Spawn (Transfer Vestibule)
  → Explore Triage Corridor + Exam + Records
    → Observe (authored notes + env)
      → Recover Protocol Card
        → File at OH Console (MarkSolved)
          → World Response (Isolation + Soft Open unlock)
            → Pass Isolation Anteroom → Observation
              → Witness on egress → Soft Open stub
```

---

# Level Layout — unique topology

**Map:** `LV_ARI_MedicalWing`  
**Compass:** +Y North, +X East.

### Spatial idea: process spine + isolation pinch

```text
 WEST                                                         EAST
[Transfer Vestibule]═══[Triage Corridor]═══════════════[Isolation Anteroom]═══[Observation Bay]
       Soft Open in              │                              ▲ locked until WR      │
                                 ├── N: Exam Cubicle            │                      └── Soft Open egress
                                 ├── S: OH Console bay (solve)                         └── Witness here
                                 └── N/E: Records niche (card)
```

| Space | Role | Why unique vs prior wings |
|-------|------|---------------------------|
| **Clinical Transfer Vestibule** | Soft Open arrival; narrow double-threshold; Note A | Not a wide checkpoint lobby |
| **Triage Corridor** | Primary spine; teal stripe landmark; waiting residue | Linear process hall, not hub |
| **Exam Cubicle** | Privacy curtain + interrupted exam; Note C | Human-scale alcove, not locker bay |
| **OH Console Bay** | Glazed bay facing corridor; Protocol Card file; puzzle | Solve sits mid-spine facing care, not south ops room |
| **Records Niche** | Chart rails / open drawer; Protocol Card pickup; Note B/D | Paper culture landmark |
| **Isolation Anteroom** | Pinch door locked until WR; PPE cart; amber cue | **Required pass-through** after solve — unique traversal |
| **Observation Bay + Soft Open egress** | Two-bed observation; Witness; Soft Open stub | Exit beyond care space, not hub south door |

**Cut order:** Records niche density → Exam depth → never Armory/Restricted → never second puzzle family → never 3-station triad.

---

# Environmental Storytelling

Authored for this topology (WORLD-001 themes as inspiration only — rewrite voice/placement):

| ID | Placement | Intent |
|----|-----------|--------|
| Note A | Transfer Vestibule | Clearance live / clinical transfer open / Isolation still holding egress — no directions |
| Note B | Records Niche | Protocol Card missing from IP-3 sleeve; HOLD residue — ObjectiveOnRead toward OH filing |
| Note C | Exam Cubicle | Interrupted exam voice (pressure behind eyes / curtain left drawn) — symptoms |
| Note D | OH Console shelf | Do not release Isolation under incomplete protocol filing |
| Note E | Observation egress (optional) | Quiet apprehension after amber settles |

Env-only: teal stripe, empty waiting chair askew, exam lamp on empty table, PPE at Isolation, half-made Observation bed, HOLD stamp set.

**Rules:** Symptoms only. No walkthrough. No Witness explanation. No silent Canon promotion of WORLD-001 name proposals.

---

# Puzzle Design — unique ops problem

## Fantasy

Staff abandoned an **Isolation Protocol filing**. The Protocol Card never reached the OH Console. Isolation Anteroom stays sealed; Soft Open clinical egress beyond Observation stays locked. Player completes the interrupted clinical handshake.

## Steps (ONE ops problem)

1. Explore → find **Protocol Card** (`BP_KeyItemPickup`, `itemId=ProtocolCard`) in Records Niche.  
2. At **OH Console**, interact thin `BP_ObservationProtocolPuzzle` with required `ProtocolCard` → consume / `MarkSolved`.  
3. **No** multi-station HOLD/ENGAGE triad. Optional single diegetic “FILE” feedback PrintString is debt-ok.

## World Response

`WorldResponseTargets`: Isolation Anteroom door unlock, Soft Open egress unlock, clinical cool lights / ambient / PA prints, Witness arm on Observation egress.

## Failure

Missing card / incomplete file → Isolation stays locked; readable feedback; no timer; no Witness soft-lock.

## Explicit non-builds

- No CS-BADGE / CS-ZONE / CS-EXIT clone  
- No ST-TEMP / ST-SEAL / ST-LINK clone  
- No Staff Keycard / Lobby clearance redo  
- No fuse / fuel / coolant redo  
- No combat / chase / Armory / Restricted  

---

# Horror

```text
Quiet clinic → paper focus → relief (Isolation opens) → pressure (Witness in Observation egress) → Soft Open release
```

Witness **only** after solve, on Observation → Soft Open path (inside/after Isolation), clinical-cold silhouette — not during Exam/Records search.

---

# Technical Plan

| Asset | Role |
|-------|------|
| `LV_ARI_MedicalWing` | **Rebuilt** E–W clinical process spine + Isolation pinch (not Security L-hub rename) |
| `BP_OHConsoleFilingPuzzle` | Thin **FusePuzzle** child — Protocol Card file at OH Console (**no** station triad) |
| `BP_ObservationProtocolPuzzle` / `BP_ObservationStation` | Early AccessClearance duplicates — **unused** in map (do not wire triad) |
| `BP_MedicalWingReset` | Full SliceReset twin |
| Protocol Card KeyItem | Records Niche (`itemId=ProtocolCard`) |
| Isolation AnteroomDoor | Spatial pinch landmark mid-spine |
| SoftOpenExit_ClinicalEgress | Locked until WR; east Observation egress stub |
| Soft Open Security→Medical | Security SoftOpenExit_Stub → `LV_ARI_MedicalWing` |

**Lighting:** Kill outdoor Directional/Sky dominance. Clinical cool interior; amber Isolation only.

**Dressing:** Laboratory / Office / ThirdParty clinical-adjacent props; teal stripe intent; tag stand-in debt.

---

# Risks

| Risk | Mitigation |
|------|------------|
| Accidental Security clone | Uniqueness contract + rebuild gate before Validate |
| WORLD-001 treated as template | Inspiration-only note on every package pointer |
| Puzzle drifts into 3-station | Design forbids triad; Implement checklist verifies one console + card |

---

# Approval Block

| Field | Value |
|-------|-------|
| Ready for Approval | YES |
| Ready to Implement | YES |
| EP uniqueness correction | Binding — layout + puzzle + story must differ from PE-018–021 |

**Next:** Implement unique `LV_ARI_MedicalWing` per this plan + VDP.

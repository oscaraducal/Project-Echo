# Manual PIE Checklist — PE-022 Medical Wing

**Map:** `/Game/ProjectEcho/Maps/Production/LV_ARI_MedicalWing`  
**Estimated time:** 15–25 minutes  
**Gameplay PASS owner:** Executive Producer (Oscar)  
**Automation note:** Enhanced Input cannot be fully driven by Slate/MCP — human required.

---

## Preconditions

- Flashlight / IMC / Project Echo GameMode  
- Prefer Soft Open from Security SoftOpenExit_Stub after clearance, **or** PIE direct into MedicalWing  
- Confirm indoor clinical-dim (no outdoor sun dominance)

---

## Technical already proved (do not re-claim as Gameplay)

| Check | Status |
|-------|--------|
| Unique E–W clinic spine floors/walls labeled | Technical |
| No CS-BADGE/ZONE/EXIT / AccessClearance / StaffKeycard in map | Technical |
| ProtocolCardPickup + OHConsoleFilingPuzzle present | Technical |
| Soft Open Security→Medical wired | Technical |
| SoftOpenExit_ClinicalEgress locked pre-solve | Technical |
| SliceResetButton (`BP_MedicalWingReset`) present | Technical |
| Simulate start/stop | Technical |

---

## Steps (human)

1. Spawn at **Clinical Transfer Vestibule** (west). Read **Note_A_Transfer** — symptoms only; no directions.  
2. Walk **Triage Corridor** east — confirm process-spine read (not Security lobby hub).  
3. Enter **Exam Cubicle** — **Note_C_ExamInterrupted**.  
4. Enter **Records Niche** — **Note_B_ProtocolSleeve** (objective); pick up **Protocol Card IP-3**.  
5. Go to **OH Console Bay** — **Note_D_OHWarning**; interact **OHConsoleFilingPuzzle** with Protocol Card.  
6. Confirm **World Response**: SoftOpenExit_ClinicalEgress unlocks; lights/ambient respond; Witness arms.  
7. Pass **Isolation Anteroom** into **Observation Bay**; read optional **Note_E_ObservationScrap**.  
8. Confirm **Witness** only on Observation→egress path (not during Exam/Records search).  
9. Interact **SoftOpenExit_ClinicalEgress** (stub next zone OK).  
10. Press **SliceResetButton** — full reverse; second run without UE restart.

---

## Uniqueness fail criteria (EP)

- Map reads as Security/Research L-hub with medical paint → **FAIL uniqueness**  
- Puzzle requires 3-station CS/ST triad → **FAIL uniqueness**  
- Staff Keycard / Access Clearance redo → **FAIL scope**

## Other fail criteria

- Soft Open opens before Protocol Card filing  
- Witness pressure during Exam/Records/OH filing  
- Outdoor Directional/Sky dominates indoor  
- Incomplete SliceReset (exit stays open, card gone, Witness stuck)  
- Walkthrough notes  

## Pass criteria

- Soft Open Security→Medical feels continuous  
- Clinic spine + Isolation pinch + Observation egress readable  
- Protocol Card → OH file is the sole ops problem  
- Witness post-solve on egress only  
- SliceReset replay without UE restart  

**Gameplay PASS:** PENDING_USER until Oscar walks this checklist (or written waiver).

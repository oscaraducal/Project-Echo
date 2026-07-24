# WORLD-001 — Content Package: UX Division

**Status:** Ready for EP review  
**Mission:** WORLD-001 — Medical Wing world expansion  
**Division:** Content Studio — UX  
**Scope:** Specifications and flows only — **no** UMG / Blueprint implementation

---

## 1. UX goals

| Goal | Spec |
|------|------|
| Legibility | Medical interfaces feel quieter and more form-like than Security threat UI |
| Diegesis | Terminals and panels look like workplace tools |
| Continuity | Clearance Medical status mirrors Security literacy (PE-021) without duplicating keycard puzzles |
| Honesty | Specs ≠ shipped widgets |

---

## 2. Terminal experience — OH Console (`TERM-MED-OH`)

### Flow map

```text
Boot splash
  → Login (user / pass)
    → Home menu
      → Fitness-for-Duty Queue
      → Observation Occupancy
      → Clearance Medical Status (read-only)
      → Mail
      → Lock / Log out
    → Access Denied (Director elev) — dead end with return
```

### Screen specs

#### Boot

- Full-bleed dark teal clinical field  
- Wordmark: `ASTERION MEDICAL`  
- Sub: `OCCUPATIONAL HEALTH`  
- Tiny footer: `Session auditing enabled`

#### Login

- Fields: Username, Password  
- Error: `Invalid credentials` (generic)  
- Hint none (no quest text)

#### Home menu

- Vertical list, monospaced institutional  
- Selected row: desaturated teal highlight  
- Esc / Exit interaction: returns control to world (future `BPC_Interaction` pattern)

#### FFD Queue

| Column | Width intent | Notes |
|--------|--------------|-------|
| ID | Redacted glyphs | Never show full employee names on shared console |
| DEPT | Research / Security / … | |
| CODE | SYM-04 / SLEEP / NONE | |
| STATUS | FIT / HOLD | HOLD in warning amber text |

Interaction: select row → Cover Sheet preview (print disabled / printer jam message optional).

#### Observation Occupancy

- Bed cards: VACANT / OCCUPIED  
- Amber: ON / OFF indicator  
- No mini-game; read-only atmosphere

#### Clearance Medical Status

- Read-only table for Security liaison  
- Banner: `MIRROR VIEW — CHANGES MUST BE MADE FROM FFD QUEUE`  
- Reinforces Medical ownership of determinations

#### Mail

- List + reader panes  
- Preload MAIL-MED-01 / 02 as readable entries  
- No compose required for world-building package

#### Access Denied

- Hard stop for Director account  
- Copy: `ACCESS DENIED — DIRECTOR ELEVATION REQUIRED`  
- Soft tone — bureaucratic, not horror jump

---

## 3. Records terminal (`TERM-MED-REC`)

```text
Login (optional shared `records`) → Chart Index → Cover Sheet Preview → Logout
```

- Dense list UI; most entries `[REDACTED]`  
- One readable misfile line for env storytelling  
- Print action: `Printer offline` (optional)

---

## 4. Security panel concept — Medical Clearance Reader (wall)

**Not a puzzle in WORLD-001.** Spec for future Security/Medical adjacency dressing.

| Element | Spec |
|---------|------|
| Form factor | Wall plate beside Clinical Transfer or Threshold |
| Display | `FFD: CURRENT` / `FFD: HOLD` / `FFD: UNKNOWN` |
| Input | Badge tap silhouette (no new input device family) |
| Fail state | Soft buzz + `REPORT TO OH CONSOLE` |
| Success | Quiet click + status LED teal |

Pairs with SEC-MED-01 notice. Implementation may reuse Security panel visual language with Medical stripe color.

---

## 5. Lab / clinic interface concepts

### Exam suite wall panel (non-interactive preferred)

- Static vitals silhouette / dark screen  
- Optional interact: short read-only last session timestamp  

### Isolation amber control (future)

- Physical key-switch or covered button — **not** designed as WORLD-001 puzzle  
- If ever interactive: binary ON/OFF with heavy narrative cost; prefer env-only

### Pharmacy fridge display

- Temperature readout dead / `ERR`  
- Supports MAIL-MED-03 cold chain beat

---

## 6. Keypad UX (Medical)

Medical uses **few** keypads. Prefer badge + OH Console over digit codes.

If a pharmacy cabinet keypad appears later:

| State | Feedback |
|-------|----------|
| Idle | Dim red LEDs |
| OK | Teal flash + solenoid |
| Fail | Red flash + soft reject chirp |
| Lockout | `SEE OH DESK` after N fails |

Do not invent glyph pads. No arbitrary sequences without diegetic chart reference.

---

## 7. HUD / notification examples (copy library)

World-building examples for future HUD designer reuse — Medical-flavored, diegetic-optional.

| ID | Context | Copy |
|----|---------|------|
| N-MED-01 | Enter Threshold | `Occupational Health` |
| N-MED-02 | Read OHB-12 | (none — note handles it) |
| N-MED-03 | Terminal login success | (prefer no HUD; diegetic only) |
| N-MED-04 | Future FFD item pickup | `Fitness record` |
| N-MED-05 | Amber visible | (prefer world audio/light; avoid objective spoiler) |

**Anti-pattern:** `Go to Observation and flip the amber light` as objective text.

Objective examples (future PE only):

- `Investigate the clinic`  
- `Check occupational health records`  

Still symptoms-oriented; no multi-step walkthrough objectives.

---

## 8. Interaction flow specs (docs)

### Interactable: OH Console

```text
Approach → Prompt "Use console" → Focus UI → Browse → Exit → Prompt clears
```

### Interactable: Note / clipboard

```text
Approach → Prompt "Read" → Note widget / fullscreen text → Close
```

### Interactable: Audio log device

```text
Approach → Prompt "Play" → Audio + optional subtitle → End
```

### Non-interactable preferred

- Amber beacon (env)  
- Broken pharmacy seal (env + note)  
- Waiting chairs  

Reuse existing `BPC_Interaction` patterns when a future PE implements — no new interaction framework.

---

## 9. GUI wireframe notes (textual)

**OH Home**

```text
┌─────────────────────────────────────┐
│ ASTERION MEDICAL — OH          [x]  │
├─────────────────────────────────────┤
│ > Fitness-for-Duty Queue            │
│   Observation Occupancy             │
│   Clearance Medical Status          │
│   Mail                              │
│   Lock / Log out                    │
└─────────────────────────────────────┘
```

**FFD Queue**

```text
┌─────────────────────────────────────┐
│ FFD QUEUE                    HOLD:3 │
├──────┬──────────┬───────┬───────────┤
│ ID   │ DEPT     │ CODE  │ STATUS    │
├──────┼──────────┼───────┼───────────┤
│████  │ Research │ SYM-04│ HOLD      │
│████  │ Research │ SYM-04│ HOLD      │
│████  │ Security │ NONE  │ FIT       │
└──────┴──────────┴───────┴───────────┘
│ [Cover Sheet]  [Back]               │
└─────────────────────────────────────┘
```

---

## 10. Accessibility / readability (spec intent)

- Avoid red/green-only status — pair HOLD with amber text + icon  
- Terminal contrast: light text on near-black clinical field  
- Note text: short paragraphs; high contrast paper texture  
- Do not rely on color alone for Isolation amber — use shape + label

---

## 11. UX checklist

- [x] Terminal flows  
- [x] Security-adjacent panel concept  
- [x] Clinic interface concepts  
- [x] Keypad policy  
- [x] Notification / objective copy examples  
- [x] Interaction flows reuse existing systems  
- [x] No widget implementation claimed

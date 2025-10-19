# TFU-T1

**Series:** Tactical (T-Series) — compact duty light built for single-hand discipline, high candela, and zero bullshit.

---

## TL;DR

Small, brutal, and reliable. Forward-clicky control, three-mode UI, and a throwy SFT40 for ID and signaling at distance.  
Built to be used — not admired on a shelf.

---

## Prototype Spec (current baseline)

- **Host:** Convoy M2  
- **Emitter:** Luminus SFT40, 6500 K  
- **Driver:** 8 A buck driver (regulated)  
- **Optics:** Smooth reflector (stock M2)  
- **Switch:** Forward clicky (momentary + latch)  
- **Mode Group:** Group 5 — **1 % / 20 % / 100 %** (no strobe)  
- **Cells:** Samsung 25R (recommended for duty) or Samsung 30Q (runtime tradeoff)

---

## Purpose & Identity

TFU-T1 is a compact duty/tactical tool focused on one thing: **controlled, high-candela output** when you need to identify or signal at range.  
No gimmicks. No ramps. Muscle-memory UI and a head designed to throw.

**Key traits:**
- **Throw-first:** SFT40 produces a tight hotspot for distance ID.  
- **Simple UI:** Three predictable states — immediate, repeatable behavior under stress.  
- **Momentary discipline:** Forward clicky gives instant momentary without accidental changes.  
- **Serviceable:** Built to be repairable and hardened (MX-4, Loctite, spring bypass options).

---

## Thermal & Performance Notes

- At **100 % (8 A)** expect high junction temps; verify with logged runs. Use proper copper star/pill and thermal paste.  
- **20 %** is the default carry level — usable for navigation and short tasks with manageable thermal rise.  
- Recommend thermal telemetry during validation: MCPCB thermocouple + body surface probe. Record until steady-state or driver step-down.

---

## Cell Guidance

| Role | Cell | Why |
|------|------|-----|
| **Duty / Punch** | Samsung 25R | Best punch with low sag for repeated high-candela bursts. Standard issue. |
| **Extended Runtime** | Samsung 30Q | More capacity, slightly more sag at full tilt — good for runtime-heavy roles. |
| **User Supplied** | Any 18650 | Supported. Mark compatibility clearly on packaging if no cell shipped. |

**Runtime estimates:** ~18–25 min @100 % (depends on cell & cooling), 80–110 min @20 %.

---

## Test & Evaluation Plan

1. **Driver verification:** Confirm mode steps and memory on bench with dummy load.  
2. **Current check:** Measure amps at 1 %, 20 %, and 100 % with fresh cell.  
3. **Thermal run:** 100 % for 45 s; record temps every 10 s. Repeat 5 cycles of 45 s on / 90 s off.  
4. **Long run:** 20 % continuous for 60+ min to validate regulation curve.  
5. **Beam & candela:** Indoor/outdoor beamshots, lux readings, candela calc.  
6. **Stress UI:** One-hand drills, rapid click sequences, confirm no mode skip under stress.

Log all data to CSV in `/data/TFU-T1/`.

---

## Build & Hardening Notes

- **Thermal path:** Copper star (and copper pill if available). Thin MX-4 layer, no air gaps.  
- **Bypass:** 22 AWG spring bypass recommended on production units.  
- **Retention:** Loctite 242 on retaining rings, torque verified.  
- **Switch:** Shaved or ported boot improves feel and dust resistance.  
- **QC Label:** Inside box lid — “TFU QC PASS – BUILT IN U.S.”  
- **User Card:** “Default: 20 % / Burst: 100 % (limit 45 s)” included in packaging.

---

## User Copy

> **TFU-T1** — Compact tactical duty light. Forward-click discipline, SFT40 throw, three-mode simplicity.  
> Built to be carried. Built to work.

---

## Status

**Prototype.** Pending runtime graphs, beamshot validation, and final hardening checklist.  
Planned production: single 6500 K variant.  
User options: forward clicky (standard), reverse clicky (optional, by request).

---

## Design Decisions (pre-release)

- Keep 8 A full-drive for duty spec or cap to 6 A for longer sustained use?  
- Standardize forward clicky; offer reverse as alternate SKU only.  
- Default cell recommendation: Samsung 25R for duty carry.

---

*TFU-T1 — first in the Tactical Series. Field-grade, simple, and brutally effective.*

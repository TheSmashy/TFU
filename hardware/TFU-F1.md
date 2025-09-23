# TFU-F1 (Field) — S21G Platform

**Series:** F (Field / Work)

**Host:** Convoy S21G (21700)

**Colorway:** Black

**Status:** **Release: v1 (Aug 2025)** — field-verified build.  
_This page is the authoritative tech spec / build guide for TFU-F1 on the S21G platform._

![TFU-F1 hero shot placeholder](../Assets/TFU-F1-Hero.jpg)

---

## Mission & Philosophy of Use
TFU-F1 is a **mission-grade field/inspection light** tuned for **stable regulated output, high-CRI fidelity, and hard-use reliability**. It favors **usable beam** and **predictable behavior** over peak spec sheet lumens.

- **Role:** field tasks, patrol, inspection, close-to-mid range work
- **Beam intent:** neutral, color-accurate, soft-edged hotspot; minimal artifacts
- **Operator focus:** simple UI, clean LVP behavior, serviceable hardening

---

## Core Specifications (v1)
- **Cell size:** 21700  
- **Recommended cell:** **Molicel P45B** (performance)  
  _Alternatives:_ P42A (cooler), P50B (runtime bias)  
- **Driver:** **5 A buck** (12-group UI) — regulated  
- **Emitter:** **Nichia 519A 4500K** (high CRI)  
- **Optic:** **15° bead TIR** (inspection / patrol)  
- **User interface:** **Group 10** (1% → 10% → 35% → 100%), **memory off**  
- **Electrical path:** **20 AWG** LED leads; **22 AWG** tail spring bypass  
- **Hardening:** MX-4 TIM under MCPCB; **CS109** driver perimeter glue; **Loctite 242** on retaining rings & clip screws  
- **Water protection:** IPX8 expected (post-build seal check)  
- **Impact resistance:** 1 m drop tested  
- **Dimensions / weight:** 124mm x 26mm, 78g (dry)

> **Field-Verified** — LVP gating at ~3.2 V (under load); 10% “finish-the-task” stability toward ~3.0 V.

---

## Bill of Materials (BOM)
- Convoy S21G host (21700)  
- Nichia 519A 4500K on 20 mm MCPCB  
- 5 A buck driver (12-group UI)  
- 15° bead TIR optic (S21G format)  
- Silicone wire: **20 AWG** (LED), **22 AWG** (tail bypass)  
- Thermal interface: **MX-4**  
- Adhesive: **CS109** (driver edge bond)  
- Threadlocker: **Loctite 242**  
- O-ring lube: **Super Lube**  

---

## Assembly & Hardening Procedure
1. **Disassemble** bezel → optic → MCPCB; remove tail and cell.  
2. **Driver swap**: desolder leads; remove driver ring; install **5 A buck**; **CS109** micro-bead at perimeter; reinstall **ring w/ 242**.  
3. **Rewire**: fit **20 AWG** LED leads (short runs, proper strain relief).  
4. **Tail bypass**: **22 AWG** silicone from spring base to contact; ensure full travel.  
5. **Thermal seat**: alcohol clean; **thin MX-4** under MCPCB; clamp even; confirm centering.  
6. **Optic**: install **15° bead TIR**; check for debris; verify gasket fit.  
7. **Threads & seals**: O-rings lightly lubed; torque rings; **clip screws 242**.  
8. **UI program**: **Group 10**, memory **off**.  
9. **QC**: continuity check, beam artifact check (1 m wall), switch feel.

---

## Electrical & UI Notes
- **Buck vs linear:** Buck regulation maintains target LED current longer, lowers waste heat, and pairs well with high-drain 21700 cells (P45B).  
- **Tailcap current at 100%:** expect **~4–5 A from the cell** (not equal to LED current due to conversion).  
- **Short measurements only** at 100% to avoid unnecessary stress.

---

## Runtime & Thermal Characterization (Planned Graphs)
![TFU-F1 runtime graph placeholder](../Assets/TFU-F1-Runtime-Graph.jpg)

**Test rig:** TEST-O-MATIC-PI (DS18B20 temp, lux @ fixed distance)  
**Cells:** P45B primary; P42A/P50B comparison  
**Modes:** 100% sustained to step; 35% 15-min hold  
**Ambient:** *TBD* °C; fan-off  
**Logging interval:** *TBD* s

**Record template**
| Mode | Start V (load) | V @1m | V @5m | Step/cut time | End V (load) | Recovered OCV (10m) | Notes |
|---|---:|---:|---:|---:|---:|---:|---|
| 100% | | | | | | | |
| 35% | | | | | | | |
| 10% | | | | | | | |

---

## Acceptance Checklist (5-Minute)
- **UI**: Group 10, memory off; half-press cycle clean  
- **100% (90 s)**: no flicker/whine; smooth thermal step  
- **35% (5 min)**: flat output; beam clean; body temp reasonable  
- **LVP gate**: with ~3.2 V (load) cell, 100% → blink → 35%  
- **Tail current @100%**: ~4–5 A (brief measurement)  
- **Mechanical**: rings snug (242), driver edge bonded (CS109), O-rings lubed

---

## Maintenance
- **O-rings**: light re-lube every 3–6 months  
- **Lens/contacts**: IPA/DeoxIT wipe; avoid residue pools  
- **Cell care**: store at 3.7–3.8 V; avoid resting <3.0 V  
- **Thread check**: verify ring torque after heavy vibration

---

## Operator Notes
- **35% = work mode**; **100% = burst**  
- Treat first **blink → 35%** as **SWAP SOON**  
- **10%** is the most stable “finish-the-task” mode near empty  
- Do not bypass LVP or defeat protections

---

## Revisions & Serialization
- **TFU-F1 v1 (Aug 2025)** — S21G platform, 5 A buck, 519A 4500K, 15° bead, hardening as above  
- Unit label format: **TFU-F1-S21G-v1-###** (sticker inside tube + QR to repo page)

**Changelog**  
- v1: Initial release with documented LVP and acceptance tests

---

## Commit Message (suggested)

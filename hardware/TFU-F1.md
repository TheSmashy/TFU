# TFU-F1 (Field)

**Series:** F (Field / Work)  
**Host:** Convoy S21G (21700)  
**Colorway:** Black  

**Status:** **Release v1 (Aug 2025)** — Field-verified build  
_This page is the authoritative tech spec and build guide for TFU-F1 on the S21G platform._

![TFU-F1 hero shot placeholder](../Assets/TFU-F1-Hero.jpg)

---

## Mission & Philosophy of Use
The **TFU-F1** is a **mission-grade field/inspection light** tuned for **stable regulated output, high-CRI fidelity, and hard-use reliability**. It prioritizes a **usable beam** and **predictable behavior** over peak spec-sheet lumens.

- **Role:** Field tasks, patrol, inspection, close-to-mid range work  
- **Beam Intent:** Neutral, color-accurate, soft-edged hotspot; minimal artifacts  
- **Operator Focus:** Simple UI, clean LVP behavior, serviceable hardening  

---

## Core Specifications (v1)

| Component        | Spec / Notes |
|-----------------|--------------|
| **Cell Size**    | 21700 |
| **Recommended Cell** | **Molicel P45B** (performance) <br> _Alternatives:_ P42A (cooler), P50B (runtime bias) |
| **Driver**       | **5 A buck** (12-group UI) — regulated |
| **Emitter**      | **Nichia 519A 4500K** (high CRI) |
| **Optic**        | **15° bead TIR** (inspection / patrol) |
| **User Interface** | **Group 10**: 1% → 10% → 35% → 100% (memory off) |
| **Electrical Path** | 20 AWG LED leads; 22 AWG tail spring bypass |
| **Hardening**    | MX-4 TIM under MCPCB; **CS109** driver perimeter glue; **Loctite 242** on retaining rings & clip screws |
| **LVP Behavior** | **Three steady blinks at 3.0 V under load**, then step to lower mode |
| **Protection**   | IPX8 expected (post-build seal check); 1 m drop tested |
| **Dimensions / Weight** | 124 mm × 26 mm; 78 g (dry) |

### Estimated Output & Runtime (P45B 4500 mAh)

| Mode  | % Output | Lumens (est.) | Runtime (est.) | Notes / Use Case |
|-------|----------|---------------|----------------|------------------|
| Low   | 1%       | ~20 lm         | 150–180 h      | Map reading / extended runtime |
| Med1  | 10%      | ~200 lm        | 18–20 h        | General work / navigation |
| Med2  | 35%      | ~700 lm        | 5–6 h          | Primary work mode |
| High  | 100%     | ~1900–2000 lm  | 1.2–1.5 h (step down as needed) | Maximum output – monitor heat |

*Estimates vary by cell condition, temperature, and cycling.*

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
2. **Driver Swap:** Desolder leads, remove driver ring, install **5 A buck**, apply **CS109** micro-bead at perimeter, reinstall ring with **Loctite 242**.  
3. **Rewire:** Fit **20 AWG** LED leads (short runs, proper strain relief).  
4. **Tail Bypass:** **22 AWG** silicone from spring base to contact; ensure full travel.  
5. **Thermal Seat:** Alcohol clean; thin layer of **MX-4** under MCPCB; clamp even; confirm centering.  
6. **Optic:** Install **15° bead TIR**; check for debris; verify gasket fit.  
7. **Threads & Seals:** O-rings lightly lubed; torque rings; **clip screws with 242**.  
8. **UI Program:** Set **Group 10**, memory **off**.  
9. **QC:** Continuity check, beam artifact check (1 m wall), switch feel.  

---

## Electrical & UI Notes

- **Buck vs. Linear:** Buck regulation maintains target LED current longer, lowers waste heat, and pairs well with high-drain 21700 cells.  
- **Tailcap Current at 100%:** Expect ~4–5 A from the cell (not equal to LED current due to conversion).  
- **LVP:** At ~3.0 V under load the driver issues **three steady blinks**, then steps to a lower mode. Treat this as a “swap soon” indicator.  
- Only take **short measurements** at 100% to avoid unnecessary stress.  

---

## Runtime & Thermal Characterization (Planned Graphs)

![TFU-F1 runtime graph placeholder](../Assets/TFU-F1-Runtime-Graph.jpg)

**Test Rig:** TEST-O-MATIC-PI (DS18B20 temp, lux @ fixed distance)  
**Cells:** P45B primary; P42A/P50B comparison  
**Modes:** 100% sustained to step; 35% 15-min hold  
**Ambient:** *TBD* °C; fan-off  
**Logging Interval:** *TBD* s  

**Record Template:**

| Mode | Start V (load) | V @1 m | V @5 m | Step/Cut Time | End V (load) | Recovered OCV (10 m) | Notes |
|---|---:|---:|---:|---:|---:|---:|---|
| 100% | | | | | | | |
| 35% | | | | | | | |
| 10% | | | | | | | |

---

## Acceptance Checklist (5-Minute)

- **UI:** Group 10, memory off; half-press cycles clean  
- **100% (90 s):** No flicker/whine; smooth thermal step  
- **35% (5 min):** Flat output; beam clean; body temp reasonable  
- **LVP Gate:** At ~3.0 V (load), three blinks then step-down  
- **Tail Current @100%:** ~4–5 A (brief measurement)  
- **Mechanical:** Rings snug (242), driver edge bonded (CS109), O-rings lubed  

---

## Maintenance

- **O-rings:** Light re-lube every 3–6 months  
- **Lens/Contacts:** IPA/DeoxIT wipe; avoid residue pools  
- **Cell Care:** Store at 3.7–3.8 V; avoid resting <3.0 V  
- **Thread Check:** Verify ring torque after heavy vibration  

---

## Operator Notes

- **35% = Work Mode**; **100% = Burst**  
- **Three steady blinks at ~3.0 V = SWAP SOON**  
- **10%** is the most stable “finish-the-task” mode near empty  
- Do not bypass LVP or defeat protections  

---

## Revisions & Serialization

- **TFU-F1 v1 (Aug 2025)** — S21G platform, 5 A buck, 519A 4500K, 15° bead, hardening as above  
- Unit Label Format: **TFU-F1-###** (sticker inside tube + QR to repo page)

**Changelog**  
- v1: Initial release with documented LVP and acceptance tests


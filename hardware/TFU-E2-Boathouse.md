# **TFU-E2 Classic+ — *Flagship Spec (Personal / Halo Build)***

**Serial:** **TFU-E2-WM-01+**  
**Owner:** WM (personal flagship carry)  
**Purpose:** High-output, high-CRI **519A triple** tuned for **maximum punch**, **copper-heavy thermal mass**, and **zero compromises.**  
This is the *halo variant* of the E2 line — built to show what an S2-geometry triple can really do.

---

## **Summary (at a glance)**
- **Host:** Black **Convoy S2**  
- **Engine:** **Triple Nichia 519A 4500K (CRI90)** on 20 mm MCPCB  
- **Optic:** **Carclo 10508**  
- **Driver/UI:** **17 mm 8 A buck** (regulated), **Group 10** (1/10/35/100%), **memory OFF**  
- **Cell:** **Samsung 30Q** or **Molicel P28A**  
- **Thermal Core:** Full **S2 copper triple spacer**, resurfaced and leveled  
- **Hardening:** Spring bypasses, MX-4, CS109, Loctite 242, black lens o-ring  
- **Style:** Murder-out aesthetic, premium beam quality, ultra-tight hotspot

---

## **Bill of Materials (Classic+ Variant)**
- **Host:** Convoy **S2** (black), AR lens  
- **MCPCB:** Triple Nichia **519A 4500K**, 20 mm (Kai)  
- **Optic:** Carclo **10508**  
- **Spacer:** **S2 copper triple spacer**, flattened + prepped  
- **Driver:** **8 A buck**, regulated, 17 mm  
- **Wiring:** 22 AWG silicone, **bypasses both springs**  
- **Consumables:**  
  - MX-4 under MCPCB  
  - CS109 (driver thermal potting & stack contact)  
  - Loctite 242 (retaining rings + clip screws)  
- **Cells:**  
  - **Samsung 30Q** (ideal)  
  - **Molicel P28A**  
  - M35A acceptable but not ideal for 8 A discharge

---

## **Performance (realistic OTF behavior)**

| Mode | Output | Tail Current | Runtime (30Q) | Notes |
|---|---:|---:|---:|---|
| **100%** | **1600–2000 lm** | ~7.5–8.1 A | short bursts, ~3–5 min to 60–65 °C | flagship punch |
| **35%** | 550–700 lm | ~2.4–2.8 A | 1.3–1.6 h | sustainable work mode |
| **10%** | 150–180 lm | ~0.6 A | 6–7 h | task level |
| **1%** | 10–15 lm | ~0.05 A | ~70 h | admin use |

**Beam:**  
519A + 10508 + clear o-ring = **smooth, cohesive hotspot**, zero “holey” artifacts, creamy edges, perfect indoor/outdoor beam.

**Thermals:**  
The S2 copper core stabilizes early; expect predictable ~60–65 °C head temps on 100%.

---

## **UI & Power**
- **UI Group:** **10** → 1% / 10% / 35% / 100%  
- **Memory:** **OFF**  
- **LVP:** Warn ~3.0 V / cutoff ~2.8 V  
- **Cell Guidance:**  
  - Use **30Q**/**P28A** for full 8 A behavior  
  - Store spares @ **3.7–3.8 V**  
  - Rotate quarterly  

---

## **Assembly Notes (Classic+ stack)**
1. **Spacer Prep:** Copper spacer resurfaced flat; deburred; cleaned.  
2. **MCPCB Seat:** MX-4 thin layer; torque even; verify no tilt under optic.  
3. **Driver Install:**  
   - Program Group 10 + test LVP  
   - Confirm ground-ring continuity  
   - Add **CS109** between driver + pill  
4. **Springs:** 22 AWG bypass (head + tail)  
5. **Optic Fit:** 10508 should lightly touch the lens; clear ring improves beam quality.  
6. **Thread-Lock:** Loctite 242 on rings and clip screws.  
7. **Stack Tightness:** No optic pinch, no MCPCB float, no spacer rock.

---

## **QA Checklist (Classic+ Acceptance)**
- Tail current confirmed on all modes with 30Q  
- Thermal run:  
  - 100% for 10–15 min  
  - DS18B20 temp + lux logged  
  - Expect ~60–65 °C max  
- Beamshot verification:  
  - White wall + 10–20 m outdoor  
  - Look for Classic+ signature beam  
- LVP warn + cutoff verified  
- Rattle test: light taps onto concrete  
- UI sanity: always starts at 1% (memory off)

---

## **Maintenance**
- Re-lube o-rings + threads every few months  
- Keep spare 10508 optic + gasket  
- Quarterly:  
  - Current check  
  - Ring torque  
  - MCPCB seat re-check  

---

## **Marking**
- **Internal label:**  
  `TFU-E2-WM-01+ (519A/4500K • 8A Buck • 30Q)`  
- **External:**  
  *Classic+ — Flagship Spec* (logbook only)

---

## **Change Log**
- **2025-11-xx** — Classic+ spec drafted (8 A version).  
- **2025-11-xx** — Optic finalized (10508).  
- **2025-11-xx** — Build pending driver arrival.

---

*Classic+ is the E2 at full send — proof-of-concept, halo-tier execution.*  

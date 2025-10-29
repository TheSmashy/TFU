# TFU-F1 (Field)

**Series:** F (Field / Work)  
**Host:** Convoy S21G (21700)  
**Colorway:** Black — Boathouse Spec  

**Status:** **Release v1 R2 (Oct 2025)** — Field-verified build  
_Authoritative technical record for the TFU-F1 configuration on the S21G platform._

![TFU-F1 hero shot placeholder](../Assets/TFU-F1-Hero.jpg)

---

## Mission & Philosophy of Use
The **TFU-F1** is a **mission-grade field and inspection light** built for **endurance, CRI fidelity, and predictable regulation**.  
Every design choice—optic, driver, and mass bias—serves one goal: **sustained utility under pressure**.

- **Role:** Field / worklight / inspection / patrol  
- **Beam Intent:** Neutral tone, high color accuracy, controlled spill for close-range visibility  
- **Operator Focus:** Minimal UI friction, hardened electronics, field-serviceable design  

---

## Core Specifications (v1 R2)

| Component | Specification / Notes |
|------------|------------------------|
| **Cell Type** | 21700 |
| **Recommended Cell** | **Molicel P45B** — standard and only approved cell |
| **Driver** | **5 A buck** (12-group UI) — regulated, low-loss |
| **Emitter** | **Nichia 519A 4500 K** (CRI ≥ 90, sweet bin) |
| **Optic** | **15° bead TIR** — tight core, tamed spill |
| **User Interface** | **Group 10:** 1 / 10 / 35 / 100 % · Memory off |
| **Electrical Path** | 20 AWG LED leads · 22 AWG tail bypass |
| **Hardening** | MX-4 TIM · CS109 driver edge bond · Loctite 242 on rings & clip |
| **LVP Behavior** | 3 blinks @ ≈ 3.0 V → auto step-down |
| **Ingress / Impact** | IPX8 expected · 1 m drop verified |
| **Dimensions / Weight** | 124 mm × 26 mm · ≈ 78 g dry |

---

## Emitter Configuration

- **Standard Production:** Nichia 519A 5000 K  
- **Legacy / Reference:** Nichia 519A 4500 K (“good-vibe bin,” 1 unit retained)  
- **Driver:** 5 A buck · Full bypass · Regulated current  

> The 4500 K variant represents the original TFU color intent — a warmer neutral with natural rendering and soft contrast. Later runs use 5000 K for fleet uniformity.

---

## Estimated Output & Runtime (P45B 4500 mAh)

| Mode | Output % | Lumens (est.) | Runtime (est.) | Field Use |
|------|-----------|---------------|----------------|-----------|
| Low | 1 % | ~20 lm | 150 – 180 h | map / admin / dark adapt |
| Med 1 | 10 % | ~200 lm | 18 – 20 h | general work / nav |
| Med 2 | 35 % | ~700 lm | 5 – 6 h | primary task mode |
| High | 100 % | ~1900 lm | 1.2 – 1.5 h (thermal step) | burst illumination |

---

## Bill of Materials (BOM)

- Convoy S21G host (21700)  
- Nichia 519A 4500 K on 20 mm DTP MCPCB  
- 5 A buck driver (12-group UI)  
- 15° bead TIR optic  
- 20 AWG silicone LED leads  
- 22 AWG tail spring bypass  
- MX-4 thermal compound  
- CS109 adhesive (driver edge bond)  
- Loctite 242 threadlocker  
- Super Lube for threads / O-rings  

---

## Assembly & Hardening Procedure

1. **Disassemble** bezel → optic → MCPCB · remove tail and cell.  
2. **Driver install:** Fit 5 A buck; apply CS109 micro-bead around edge; Loctite 242 driver ring.  
3. **Wire-in:** 20 AWG LED runs (short and clean).  
4. **Bypass:** 22 AWG tail spring wire · confirm travel & switch return.  
5. **Thermal seat:** Alcohol clean · thin MX-4 layer · center MCPCB · torque evenly.  
6. **Optic:** Install 15° bead TIR + gasket; verify seal and alignment.  
7. **Threads / Seals:** Lube O-rings · Loctite clip screws · snug rings.  
8. **Program UI:** Group 10 · memory off.  
9. **QC:** Continuity · beam inspection · switch feel · LVP test.  

---

## Electrical / UI Notes
- Buck regulation keeps LED current flat for longer and reduces heat.  
- Expect ≈ 4 – 5 A tail draw on High.  
- LVP = 3 steady blinks then mode drop; treat as swap signal.  
- Keep High tests short during bench setup.  

---

## Field Runtime / Thermal (Planned Data)

![Runtime graph placeholder](../Assets/TFU-F1-Runtime-Graph.jpg)

**Rig:** Pi Logger · DS18B20 temp · fixed lux sensor  
**Cell:** P45B (primary)  
**Modes:** 100 % → step · 35 % sustain  
**Ambient:** TBD °C · fan off  
**Interval:** TBD s  

| Mode | Start V | 1 m V | 5 m V | Step / Cut | End V | OCV (10 m) | Notes |
|------|:--:|:--:|:--:|:--:|:--:|:--:|:--|
| 100 % |  |  |  |  |  |  |  |
| 35 % |  |  |  |  |  |  |  |
| 10 % |  |  |  |  |  |  |  |

---

## Acceptance Checklist (5 min)

- **UI:** Group 10 · memory off · clean cycle  
- **100 % (90 s):** no flicker / whine · smooth step  
- **35 % (5 min):** flat output · temp stable  
- **LVP:** 3 blinks @ ≈ 3.0 V then step-down  
- **Tail current:** ≈ 4–5 A (brief measurement)  
- **Mechanical:** rings snug · CS109 bond · lubed O-rings  

---

## Maintenance

- Re-lube O-rings every 3–6 months  
- Clean lens / contacts with IPA or DeoxIT  
- Store cells @ 3.7–3.8 V  
- Verify ring torque after heavy vibration or impact  

---

## Operator Notes

- **35 % = Primary Work Mode** · **100 % = Burst / Signal**  
- **3 blinks ≈ swap cell soon**  
- **10 % mode** is the “finish the job” setting on a low pack.  
- Never bypass LVP or defeat thermal logic.  

---

## Revisions  

| Version | Date | Key Changes |
|----------|------|-------------|
| v1 (Aug 2025) | Initial release · 5 A buck · 519A 4500 K · bead TIR · hardening defined |
| v1 R2 (Oct 2025) | Rebuild with sweet-bin 4500 K · verified 5 A buck performance · improved clip hardware · formalized Boathouse Spec |

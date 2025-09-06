# TFU-T1 (In Development)

## Series: Tactical (T Series)

Mission-focused lights designed for controlled output, momentary activation, and high-candela throw.

---

## Prototype Configuration

- **Host:** Convoy M2  
- **Emitter:** Luminus SFT40, 6500K  
- **Driver:** 8A Buck Driver  
- **Optics:** Smooth Reflector (M2 stock)  
- **Switch:** Forward Clicky (momentary capable)  
- **Mode Group:** 5 (1% – 20% – 100%)  
- **Cells:** Samsung 25R (duty) / Samsung 30Q (extended runtime)  

---

## Tactical Identity

- **Throw Priority:** SFT40 delivers a tight, high-candela beam for distance ID and signaling.  
- **Direct UI:** 3 modes only, no strobe/disco. Built for muscle memory.  
- **Momentary Discipline:** Forward clicky enables light discipline and controlled activation.  
- **Rugged Host:** M2 with crenulated bezel, compact size fits pistol mag pouches for discreet or rapid carry.  

---

## Test & Evaluation Notes

- **Thermal / Regulation:** Log output curves at 8A with Pi rig.  
- **Beam Profile:** Compare throw vs. flood against TFU-F2 (M1/B35AM) to clarify tactical role.  
- **User Drills:** One-hand operation, momentary press discipline, confirm no mode-skip under stress.  
- **Cells:** 25R for max punch; 30Q as alternate for missions needing longer runtime.  

---

## Cell Options

**Assumptions:** 8A draw on 100%, ~1.6A at 20%; buck ~90% efficient; nominal 3.6V; derated for sag/thermal.

| Role                | Cell        | Capacity | Cont. Discharge | Runtime @ 100% (8A) | Runtime @ 20% (1.6A) | Notes                                              |
|---------------------|-------------|----------|-----------------|---------------------|----------------------|---------------------------------------------------|
| **Duty / Hardcore** | Samsung 25R | 2500 mAh | 20A             | ~18–20 min          | ~85–95 min           | Strong regulation, minimal sag. Tactical choice.  |
| **Heavy EDC**       | Samsung 30Q | 3000 mAh | 15A             | ~22–24 min          | ~105–115 min         | Longer runtime, slight sag at sustained max.      |
| **No Cell**         | N/A         | N/A      | N/A             | User-supplied       | User-supplied        | For buyers with existing compatible cells.        |

---

## Status

**Development Prototype.** Pending:  

- Runtime graphs  
- Beamshots and candela measurement  
- Hardening notes (Loctite, CS109, MX-4, bypasses)  

---

## Planned Designation

**TFU-T1** — First tactical model in the TFU lineup.  
Planned disposition: single variant in **6500K**.

**Objective:** Build a compact duty light with forward clicky control, simplified modes, and SFT40 candela — hardened to survive real-world carry and deployment.

> Tactical, compact, SureFire-grade ruggedness — TFU’s first purpose-built duty light.

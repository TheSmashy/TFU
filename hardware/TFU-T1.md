# TFU-T1 (In Development)

## Series: Tactical (T Series)

Mission‑focused lights designed for controlled output, momentary activation, and high candela throw.

---

## Prototype Configuration

- **Host:** Convoy M2
- **Emitter:** Luminus SFT40, 6500K
- **Driver:** 8A Buck Driver
- **Optics:** Smooth Reflector (stock M2)
- **Switch:** Forward Clicky (momentary capable)
- **Mode Group:** 5 (1% – 20% – 100%)
- **Cell:** Samsung 25R (high‑drain) or Samsung 30Q (extended runtime)

---

## Tactical Identity

- **High Candela Throw:** SFT40 produces a tight beam ideal for distance ID and signaling.
- **Simple, Direct UI:** Limited modes, no strobe/disco functions. Easy muscle memory.
- **Momentary Activation:** Forward clicky enables light discipline and tactical use cases.
- **Durability:** M2 host with crenulated bezel and robust construction.

---

## Test & Evaluation Notes

- **Runtime/Regulation:** Log thermal and output curve at 8A with Pi sensor rig.
- **Beam Profile:** Compare throw vs. flood against TFU-F2 (M1/B35AM) for role distinction.
- **Usability Drills:** One‑hand activation, momentary control, confirm no accidental mode cycling.
- **Cells:** 25R for high-drain reliability; 30Q as viable option for longer missions.

---

## Cell Options for TFU-T1

**Assumptions:** 8A on “100%”, ~1.6A on “20%”; buck ~90% efficient; nominal 3.6V; conservative real-world derates for sag/thermal.

| Option               | Cell        | Capacity | Cont. Discharge | Est. Runtime @ 100% (8A) | Est. Runtime @ 20% (~1.6A) | Runtime Profile                                   | Best For                      |
|----------------------|-------------|----------|------------------|--------------------------|----------------------------|---------------------------------------------------|-------------------------------|
| **Duty / Hardcore**  | Samsung 25R | 2500 mAh | 20A              | ~18–20 min               | ~85–95 min                 | Shorter runtime, very strong regulation, minimal sag | Tactical / duty (max punch)   |
| **Heavy EDC**        | Samsung 30Q | 3000 mAh | 15A              | ~22–24 min               | ~105–115 min               | Longer runtime, slight sag at sustained high draw | EDC with extra runtime        |
| **No Cell (-$10)**   | N/A         | N/A      | N/A              | User-supplied            | User-supplied              | Flexible for buyers with existing cells           | BYO cell                      |

---
## Status

Currently in development (prototype stage). Pending:

- Runtime graphs
- Beamshots and candela measurements
- Hardening notes

---

## Planned Designation

**TFU-T1** — First tactical model in the TFU lineup.

> Current planned disposition: single model offering in **6500K**.
```

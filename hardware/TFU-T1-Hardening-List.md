# TFU-T1 (M2 / SFT40) — Harden & Validation Checklist

**Goal:** Take a stock M2 SFT40 6500 K (8 A) and harden it into a field-ready TFU-T1: reliable contacts, improved thermal path, durable mechanicals, clean UI, and validated short-burst 8 A behavior with Samsung 25R.

> Safety first: wear eye protection and gloves when working on cells; work on an insulated surface; never test unattended. Use a proper Li-ion charger, a fire-safe bag for tests, and a bench power supply or meter-rated holder for current measurements.

---

## Parts & Tools
- Stock M2 SFT40 6500 K (from Simon)  
- Samsung 25R (fresh, tested cell)  
- MX-4 thermal paste  
- Copper star (20 mm or matching MCPCB) and copper pill (if M2 accepts)  
- Thermal adhesive (CS109 style or equivalent) — small amount for driver potting  
- Loctite 242 (thread locker)  
- Super Lube (or equivalent silicone o-ring grease)  
- Spring bypass kit (copper braid / solder wick, flux, solder)  
- Shaving tools for switch boot (razor, Dremel with small file, or sanding stick)  
- Black tail clip (replacement)  
- Heat-shrink, flux, soldering iron, 22–26 AWG wire for bypass if needed  
- K-type thermocouple or DS18B20 probe, small thermal tape, IR thermometer (secondary)  
- Multimeter, true RMS clamp or inline ammeter for current checks  
- Torque driver for retaining rings (or consistent hand torque technique)  
- Heat-resistant bench surface and Li-ion safe containment bag

---

## Disassembly
1. Remove tailcap and battery. Power down driver by removing cell.  
2. Unscrew head/retaining ring; carefully extract reflector/MCPCB assembly. Note any factory paste and stack order (reflector, spring, pill, glass).  
3. Remove stock thermal paste and clean surfaces (isopropyl alcohol, lint-free). Inspect MCPCB for flatness and solder joints.

---

## Thermal & Mechanical Hardening
1. **Copper star & pill:** mount 519A on copper star (if not already). If M2 accepts, use a copper pill. Ensure flatness and full seating.  
2. **MX-4:** apply a thin, even smear of MX-4 to star underside and mating surface of pill/shelf (no blobs).  
3. **Seat MCPCB/pill:** re-seat board/pill; verify full contact and no gaps.  
4. **Driver thermal adhesive:** place a small bead of thermal adhesive on the driver body where it contacts pill or head shelf (only if driver design allows and it won’t short pads). Allow cure per adhesive spec.  
5. **Spring bypass:** install copper-braid spring bypass — solder to tail spring and tailcap contact. Verify low-ohm continuity (<0.2 Ω preferable). Cover solder with heat-shrink.  
6. **Switch boot shave:** shave or port the forward clicky boot for smoother action and dust relief. Verify tactile feel and momentary action after shaving.  
7. **Replace clip:** remove stainless clip, install black tail clip if desired. Check for clearance and no thread interference.  
8. **Retention ring:** reassemble head; apply Loctite 242 to retaining ring threads (thin coat). Torque to spec (or consistent firm hand torque). Wipe excess.  
9. **O-rings & lubrication:** degrease and re-grease all tube and head O-rings with Super Lube. Replace o-rings if nicks are present.

---

## Electrical sanity & UI
1. Inspect all solder joints and wires. Confirm polarity.  
2. Verify switch continuity and momentary behavior with multimeter (no bounce or intermittent).  
3. Confirm driver programming: Group 5 (1 % / 20 % / 100 %) or your chosen group. Verify memory behavior.  
4. Verify low-ohm path from cell + to LED via bypass (multimeter).

---

## Bench Test — Low-Risk Checks
1. **No-load checks:** Insert a dummy load or current-limited bench supply. Verify driver powers and modes without cell.  
2. **Initial cell test:** Insert fresh, tested Samsung 25R. Measure resting voltage and initial current at 20 % mode (should be ~1.6 A if your driver low step set there). Record values.
3. **Short functional test:** Cycle modes, check for abnormal noises, smells, or loose parts.

---

## Thermal Validation (critical)
**Ambient**: ~20–24 °C recommended for test timing. Record ambient.

1. **20 % long run:** Run at 20 % continuously for 60 minutes. Log:
   - timestamp, battery voltage, current (A), MCPCB temp (°C), head surface temp (°C).
   - Acceptable: steady-state body surface ≤ ~45 °C and MCPCB junction reasonable (driver not stepping down). If temps drift high, re-evaluate thermal path.

2. **8 A burst test (primary acceptance test):**  
   - With fresh 25R, run **100 % (8 A)** for **30 seconds**. Monitor MCPCB (thermocouple) and body surface (probe or IR).  
   - Repeat **3 cycles** of 30 s on / 90 s off. Log temps every 10 s during bursts and every 30 s during cooldown.  
   - **Pass criteria (baseline):**
     - No driver hard step-down before 30 s on (unless driver protects).  
     - Body surface temp after 30 s ≤ **65 °C** (hand-holdable briefly; uncomfortable above).  
     - MCPCB probe safely below junction limit (driver should maintain regulation).  
     - No mechanical loosening, no solder joint creep, no smell of overheating.
   - If body > 70 °C or driver steps down early, fail: re-evaluate star/pill contact, rework thermal paste, increase contact pressure, or reduce max drive.

3. **Extended 100 % sanity (optional):** run 45 s once to confirm burst limit behavior — you already plan to label 45 s max. If unit survives 45 s with controlled temps and step-down handled, log it for marketing/test proof.

---

## Final Checks & Documentation
1. Re-torque retaining ring if necessary (once cooled).  
2. Confirm switch feel after thermal cycles.  
3. Apply QC label inside box and the Burst sticker on the packaging / body.  
4. Save logs (CSV) to `data/TFU-T1/<serial>_thermal.csv` and a short summary `data/TFU-T1/<serial>_test-summary.md`.  
5. Add build notes: parts used, paste brand (MX-4), adhesive brand, spring braid method, driver PN/settings, cell SN used for test.

---

## Acceptance Criteria (ship)
- Pass all bench and thermal tests.  
- 20 % run stable for 60 min with acceptable temps.  
- 3× 30 s 8 A bursts with body temp ≤ 65 °C and no failures.  
- Switch action solid, continuity low, no mechanical or electrical faults.  
- QC label and user card included.

---

## Fail & fallback guidance
- If fails thermal tests: re-check copper contact, re-seat MCPCB, reapply MX-4, verify pill flatness, improve spring contact, consider capping production drive to 6 A.  
- If driver steps down early and you can’t rework path, consider swapping to lower-drive or add temp-controlled soft step.

---

## Notes / Rationale (short)
This hardening sequence focuses on **reducing thermal resistance** (copper star/pill, MX-4, driver adhesive), **improving conduction** (spring bypass, pill contact), and **mechanical reliability** (Loctite, shaved boot, clip swap). The goal: a compact, high-candela tool that survives repeated short bursts without becoming an oven in your hand.


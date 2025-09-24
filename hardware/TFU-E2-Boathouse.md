# TFU-E2 — *Boathouse Spec* (Personal Build)

**Serial:** **TFU-E2-WM-01**  
**Owner:** Yours truely  
**Purpose:** Personal EDC/field light tuned for **high-CRI utility** and **calm thermals**. Keep it bombproof, not brochure.

---

## Summary (at a glance)
- **Host:** Sterile Grey **S2+** (Kai)  
- **Engine:** **Triple Nichia 519A 4500K (R9080)** on 20 mm MCPCB  
- **Optic:** **Carclo 10511**  
- **Driver/UI:** **17 mm 5 A buck**, Group 10 = **1 / 10 / 35 / 100%**, **memory OFF**  
- **Cell:** **Molicel M35A** (3.5 Ah)  
- **Build hardening:** S2+ **triple copper spacer**, **spring bypasses (head & tail)**, MX-4 under MCPCB, Loctite 242 on rings, CS109 on driver, thermal stack   
- **LVP:** Warn ≈ **3.0 V** (3 flashes), cutoff ≈ **2.8 V**

---

## Bill of Materials
- **Host:** S2+ sterile (Kai) w/ AR glass & retaining rings  
- **LED/MCPCB:** Nichia **519A 4500K** (R9080), triple on **20 mm** (Kai)  
- **Optic:** Carclo **10511** (alt: 10508/10509 for softer edges)  
- **Spacer:** **S2+ triple copper spacer**   
- **Driver:** **5 A regulated buck, 17 mm** (Convoy)  
- **Wiring:** 20–22 AWG silicone leads; head & tail **spring bypass** (22 AWG)  
- **Consumables:** MX-4 (MCPCB), **Loctite 242** (rings/clip screws), **CS109** (driver potting, thermal stack), fresh o-rings  
- **Cell:** **Molicel M35A** (primary); Samsung 30Q acceptable

---

## Performance (realistic, OTF estimates)
| Mode | Output | Tail Current | Est. Runtime (M35A) | Notes |
|---|---:|---:|---:|---|
| **100%** | ~1100–1400 lm (burst) | ~4–5 A | ~20–30 min at top (≈42 min theoretical) | Will heat-soak; expect step/settle |
| **35%** | ~400–500 lm | ~1.5–1.8 A | ~2 h | Practical “do work” level |
| **10%** | ~120–150 lm | ~0.4–0.6 A | ~7 h | Walk/indoor tasking |
| **1%** | ~10–15 lm | ~0.05 A | ~70 h | Admin/dark-adapted use |

**Thermals:** Still air, 100% reaches ~**55–65 °C** head in ~3–5 min on S2+ mass. Copper spacer and buck regulation keep behavior sane.

**Tint/CRI:** 519A 4500K = **creamy neutral-warm**, excellent R9. May show slight green at very low currents; a thin **DC-Fix** disk can smooth artifacts without killing output.

---

## UI & Power
- **Mode Group:** **10** → **1% / 10% / 35% / 100%**  
- **Memory:** **OFF** by default (always starts low).  
- **LVP:** ~**3.0 V** warn (3 blinks) / **2.8 V** cutoff.  
- **Cell policy:** Run **M35A** for endurance/thermal composure. Store spares ~**3.7–3.8 V**; quarterly check.

---

## Assembly Notes (S2+ stack)
1. **Dry-fit**: Spacer → MCPCB → optic → lens. Optic should **lightly kiss** the glass (no rattle/bowing). Removing the lens is fine too if the geometry lines up.  
2. **Thermal seat**: MX-4 under MCPCB; torque even so the board is truly flat.  
3. **Driver**: Set Group 10 on bench, verify LVP blink. Ensure **full ground-ring contact**; retaining ring snug. Dot of CS109 if you want it permanent and improve thermal transfer.  
4. **Bypasses**: Tail and head spring bypass (22 AWG).  
5. **Thread-lock**: Blue **242** on retaining rings (and clip screws). Fresh o-rings; lens clean.

---

## QA / Sanity Checklist (10–20 min)
- **Mode order & memory** verified.  
- **Tail current** measured at 1/10/35/100.  
- **Thermal run**: 100% for 15 min; log DS18B20 head temp + lux (Pi rig). Note time-to-settle and steady-state temp.  
- **Beam check**: White-wall @ all modes; confirm no tilt or optic pinch. Add **DC-Fix** if edges need taming.  
- **LVP**: Warn & cutoff confirmed.  
- **Rattle test**: Light tap/drop onto mat; re-check mode stability and stack compression.
- **1 Meter**:  Just drop your new light on the concrete.  It'll be okay, but prove you did it right.    

---

## Maintenance
- **Threads**: Periodic clean/re-lube; check ring torque.  
- **Optic/Lens**: Keep a spare 10511 and DC-Fix disk in the kit.  
- **Cell care**: M35A primary; rotate and storage-charge as per policy.  
- **Quarterly**: Quick current check and o-ring condition.

---

## Marking
- **Internal tube label:** `TFU-E2-WM-01 (519A/4500K • 5A Buck • M35A)`  
- **External:** *Boathouse Spec* note in log only. (We know what color it is.)

---

## Change Log
- **2025-09-24** — Initial build spec drafted; designated **Boathouse Spec** personal E2. Components confirmed on hand (519A triple, S2+ sterile host, 5 A buck, M35A). Group 10, memory OFF, LVP 3.0/2.8 V.

*Personal build. Not for sale. Tune for reliability over max lumens.*

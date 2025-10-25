# TFU-F3

**Series:** F (Field)  
**Host:** Convoy S16  
**Colorway:** Black and grey  

The TFU-F3 is a high-output field/work light built on the robust Convoy S16 platform and configured as a mule for maximum flood and situational awareness. Designed for sustained high-CRI output in open or enclosed work areas where beam discipline is not a priority. Built and tested in the U.S., the F3 is the first Field series model to reach production — F1 and F2 remain in development.

## Product Shot

![TFU-F3 Hero](../Assets/TFU-F3-hero.jpg)  
*TFU-F3 shown on field kit. Quad 519A mule, built for maximum flood and situational awareness.*

## Kit Context

![TFU-F3 Kit Dump](../Assets/TFU-F3-kitdump.jpg)  
*TFU-F3 alongside everyday field tools. Not a desk toy—this mule rides with real gear.*

## Internals / Build Detail

![TFU-F3 Internals](../Assets/TFU-F3-internals.jpg)  
*Quad 519A MCPCB, hardened driver install, and Molicel P45B cell. No shims, no shortcuts—TFU creed applied.*

## Beamshot (Wall of Light)

![TFU-F3 Beam](../Assets/TFU-F3-beam.jpg)  
*Full mule flood: situational awareness over distance. A wall of light, not a hotspot.*

## Specifications

* **Cell size:** 21700  
* **Recommended cell:** Molicel P45B  
* **Driver:** 6 V 8 A Buck  
* **Emitter (Standard):** Nichia 519A Quad (5000 K, 90 CRI)  
* **Emitter (Alternate):** Nichia 219B 2S2P (4500 K, 95+ CRI) — smoother tint, slightly longer runtime, warmer tone.  
* **User interface:** Mode group 10 (1 % → 10 % → 35 % → 100 %), memory off  
* **Runtime:** Sustained high output without aggressive thermal throttling (see runtime charts)  
* **Optic:** Carclo quad mule (no optic) for maximum flood  
* **Weight:** 120 g (dry)  
* **Dimensions:** 126 mm length × 33 mm head diameter  
* **Clip:** Black steel deep-carry  
* **Hardening:** Loctite 242, CS109 thermal adhesive, MX-4 thermal paste  
* **Water protection:** IPX8 tested  
* **Impact resistance:** 1 m drop tested  
* **Electrical mod:** Tail spring bypass (22 AWG)  

## Low Voltage Protection (LVP) Behavior — TFU-F3

The TFU-F3 driver includes built-in **Low Voltage Protection (LVP)** to prevent cell over-discharge and keep the light usable in the field.

* **Trigger:** ~**3.2 V under load** (cell may read higher at rest).  
* **Behavior:**
  * Attempting **High (100 %)** causes **one blink → automatic return to Med2 (35 %)**.  
    *Not a fault; the driver is gating turbo due to low voltage.*  
  * As voltage continues to fall, **35 % will no longer sustain** and will step/refuse.  
  * **10 % remains stable** down toward ~**3.0 V under load**.  
  * When the light **drops out of 10 %**, the cell is effectively **~3.0 V** → **discontinue use**.  

### Sub-Threshold Operation (3.2 V → ~3.0 V)

* **3.2 V (approx):** **Blink → hold at 35 %** (LVP gate on 100 %).  
* **< 3.2 V and falling:** **35 % becomes unstable**; **10 % = finish-the-task mode**.  
* **~3.0 V under load:** **10 % drops out** (or becomes unreliable). **Stop and swap/recharge.**

**Operator Guidance**

* Treat the first **blink → 35 %** as **SWAP SOON**.  
* To stretch the last slice, **drop to 10 %**; use **1 %** only for map/egress.  
* **Do not deep-discharge**: remove the cell if **10 % drops out** or if recovered open-circuit voltage settles near **~3.0 V** after 10 minutes rest.  

**Status:** Field-verified behavior (3.2 V gate; ~3.0 V 10 % dropout) to protect the cell and maintain safe operation.  

### Voltage Bands (under load) — Quick Reference

| Cell V (load) | Expected Behavior | Operator Action |
| ------------: | ------------------------------------------------------------------- | ------------------------------------ |
|  **≥ 3.6 V** | All modes available; 100 % generally sustained (thermal permitting). | Run as needed. |
| **3.2–3.6 V** | **100 % gated** (blink → 35 %); **35 % stable**; 10 % very stable. | Treat as **SWAP SOON**; use 35 %/10 %. |
| **3.0–3.2 V** | **35 % may step/refuse**; **10 % stable**; 1 % extended. | **Finish at 10 %**; monitor closely. |
|  **< 3.0 V** | **10 % drops out / unreliable**; protection near cutoff. | **Discontinue use**; swap/recharge. |

*Note:* “Under load” voltage will read lower than open-circuit. Re-check OCV ~10 minutes after removal; if it settles near **~3.0 V**, consider the cell field-dead for that cycle.  

## Role & Deployment

The TFU-F3 is intended for **field tasks, workspace lighting, and inspection** where maximum area coverage and color accuracy are more important than throw or beam discipline. The 5000 K quad mule configuration renders colors accurately and reduces eye strain, making it ideal for prolonged use in dynamic environments. Not intended for low-signature or tactical operations.  

### F3 Variants

* **TFU-F3 (519A, 5000 K):** Core field light — neutral daylight output with high lumen ceiling.  
* **TFU-F3B (219B, 4500 K):** Warm-tint variant — smoother tint, superior color accuracy, slightly extended runtime; ideal for indoor, inspection, or enclosed-field use.  

## Runtime & Thermal Performance

![TFU-F3 runtime graph placeholder](../Assets/TFU-F3-Runtime-Graph.jpg)  
*Placeholder — replace with runtime and thermal curve once baseline test is completed.*

**Test parameters:**

* Cell: Molicel P45B, fully charged at 4.20 V  
* Mode: 100 % (Mode Group 10)  
* Ambient: *TBD* °C  
* Distance to lux sensor: *TBD* m  
* Logging interval: *TBD* seconds  

## Tuning and Options

Each TFU-F3 is hand-built and tuned for reliable sustained output. Optics, emitter CCT, and firmware options can be customized to suit your operational needs. Contact TFU for special orders or kit integration.

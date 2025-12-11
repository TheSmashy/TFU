# Welcome to Your TFU-F3

![TFU Logo](../TFU-LOGO.png)

**Welcome to TFU – Real Gear for Hard Use**

---

**Model:** TFU-F3 (Field / Flood Utility)  

**Contact Support:** [TFU-Lights@wmode.anonaddy.com](mailto:TFU-Lights@wmode.anonaddy.com) | Reddit DM: u/thesmashy  
**Warranty:** Lifetime—details [here](https://github.com/TheSmashy/TFU/blob/main/ops/WARRANTY.md)

---

## Overview

Quad-emitter mule configuration for maximum flood and situational awareness. Designed for sustained high-CRI output in work areas. Not for covert/tactical—this is a wall-of-light tool!

>Want to carry an S2+ full of washers? Cool, bro. Want to jump out of a helo with a mule? Grab a TFU-F3 — good to go.

## At a Glance

- **Emitter:** Nichia 519A Quad, 4500K, high CRI
- **Driver:** 6V 8A buck, Mode Group 10
- **Cell:** 21700 (recommend Molicel P45B)
- **Optic:** Mule/no optic—maximum wall-of-light

| Mode  | % Output | Lumens | Runtime (est., P45B) |
|-------|----------|--------|----------------------|
| Low   | 1%       | ~40    | 150–170h             |
| Med1  | 10%      | ~400   | 15–17h               |
| Med2  | 35%      | ~1400  | 4.5–5.5h             |
| High  | 100%     | ~4000  | 35–45min             |

*Estimates vary by cell condition and use.*  
*Heat regulation is going to be an issue on 100%*  

## Quick Start
- Open tailcap, remove DC Fix disk blocking battery and spring
- From OFF, full press = ON (starts at 1%)
- Tap to cycle modes: 1% → 10% → 35% → 100%
- Full click OFF to shut down (always starts at 1%)
- Lockout: unscrew tailcap 1/4 turn

## Low Voltage Protection (LVP) Behavior — TFU-F3

The TFU-F3 driver includes built-in **Low Voltage Protection (LVP)** to prevent cell over-discharge and keep the light usable in the field.

- **Trigger:** ~**3.2 V under load** (cell may read higher at rest).
- **Behavior:**
  - Attempting **High (100%)** causes **one blink → automatic return to Med2 (35%)**.  
    *Not a fault; the driver is gating turbo due to low voltage.*
  - As voltage continues to fall, **35% will no longer sustain** and will step/refuse.
  - **10% remains stable** down toward ~**3.0 V under load**.
  - When the light **drops out of 10%**, the cell is effectively **~3.0 V** → **discontinue use**.

### Sub-Threshold Operation (3.2 V → ~3.0 V)
- **3.2 V (approx):** **Blink → hold at 35%** (LVP gate on 100%).  
- **<3.2 V and falling:** **35% becomes unstable**; **10% = finish-the-task** mode.  
- **~3.0 V under load:** **10% drops out** (or becomes unreliable). **Stop and swap/recharge.**

**Operator Guidance**
- Treat the first **blink → 35%** as **SWAP SOON**.
- To stretch the last slice, **drop to 10%**; use **1%** only for map/egress.
- **Do not deep-discharge**: remove the cell if **10% drops out** or if recovered open-circuit voltage settles near **~3.0 V** after 10 minutes rest.

**Status:** Field-verified behavior (3.2 V gate; ~3.0 V 10% dropout) to protect the cell and maintain safe operation.


### Field Notes
- If you encounter blink + fallback, **swap or recharge the cell**.  
- Behavior is most often observed during extended patrols or after leaving a cell in the light down to storage voltage.  
- Do not bypass LVP. It is integral to safe operation and preserves both the driver and 21700 cells.

## Build Quality

- Tail spring bypass, max current, instant ON
- Loctite 242 on all hardware, MX-4 and CS109 on MCPCB/driver
- Waterproof and drop-tested
- Hand-assembled and tuned in the U.S.A.
---
### Configuration & Mode Guide  
Full documentation is available here:  
**[Config Guide](docs/config_guide.md)**  

---

[Full Documentation](https://github.com/TheSmashy/TFU) | [Warranty](https://github.com/TheSmashy/TFU/blob/main/WARRANTY.md)

---
Built by hand in the U.S.A. | Last updated: 2025-12-11  

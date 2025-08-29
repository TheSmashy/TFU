# Welcome to Your TFU-F3

![TFU Logo](../TFU-LOGO.png)

**Welcome to TFU – Real Gear for Hard Use**

---

**Model:** TFU-F3 (Field / Flood Utility)  

**Contact Support:** [TFU-Lights@wmode.anonaddy.com](mailto:TFU-Lights@wmode.anonaddy.com) | Reddit DM: u/thesmashy  
**Warranty:** Lifetime—details [here](https://github.com/TheSmashy/TFU/blob/main/WARRANTY.md)

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

## Low Voltage Protection (LVP) Behavior – TFU-F3

The TFU-F3 driver includes built-in **Low Voltage Protection (LVP)**.  
This prevents cell over-discharge and ensures continued safe operation in the field.

- **Trigger point:** ~3.2V cell voltage  
- **Behavior:**  
  - When attempting to engage **High (100%)**, the light will blink once, then automatically step back to **Med2 (35%)**.  
  - This is not a fault condition. It is the driver signaling that the cell voltage is below the threshold for sustained maximum output.  
- **Result:** The light remains operational at reduced levels rather than cutting off completely, extending usable runtime while protecting the cell.  

### Field Notes
- If you encounter blink + fallback, **swap or recharge the cell**.  
- Behavior is most often observed during extended patrols or after leaving a cell in the light down to storage voltage.  
- Do not bypass LVP. It is integral to safe operation and preserves both the driver and 18650 cells.

### Below-Threshold Operation (3.2 V → ~3.0 V)

Once the cell sags to ~3.2 V, **LVP prevents 100%** and the light will **blink then hold at 35%**. From **~3.2 V down toward ~3.0 V**, the light generally remains usable at **1% / 10% / 35%**, but **runtime is limited** and voltage recovery will vary with cell health and temperature.

**Operator guidance**
- Treat **blink → 35%** as **“swap soon”**.
- You may continue at **1–10–35%** to finish a task, but **don’t expect sustained output**.
- **Do not run the cell flat.** Swap or recharge before the cell rests below ~3.0 V. Deep discharge accelerates wear.

> Note: Exact cutoff/step behavior below ~3.0 V depends on this driver’s firmware and cell sag. Field testing pending.

## Build Quality

- Tail spring bypass, max current, instant ON
- Loctite 242 on all hardware, MX-4 and CS109 on MCPCB/driver
- Waterproof and drop-tested
- Hand-assembled and tuned in the U.S.A.

---

[Full Documentation](https://github.com/TheSmashy/TFU) | [Warranty](https://github.com/TheSmashy/TFU/blob/main/WARRANTY.md)

---
Built by hand in the U.S.A. | Last updated: 2025-08-13

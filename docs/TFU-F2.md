# Welcome to Your TFU-F2

![TFU Logo](../TFU-LOGO.png)

**Welcome to TFU – Real Gear for Hard Use**

---

**Model:** TFU-F2 (Field / Utility Light)  

**Contact Support:** [TFU-Lights@wmode.anonaddy.com](mailto:TFU-Lights@wmode.anonaddy.com) | Reddit DM: u/thesmashy  
**Warranty:** Lifetime—details [here](https://github.com/TheSmashy/TFU/blob/main/WARRANTY.md)

---

## Overview

Single-emitter B35AM build optimized for high-CRI, neutral-white utility. Balanced between throw and flood using an OP reflector — tuned for field tasks, work benches, and real-world runtime.

> When you need a light that isn’t a stunt, but still flexes on Brice — the TFU-F2 is the tool.

## At a Glance

- **Emitter:** Nichia B35AM, 5000K, high CRI  
- **Driver:** 6V 2A boost, Mode Group 10  
- **Cell:** 18650 (recommend Molicel M35A)  
- **Optic:** OP reflector, glass lens  

| Mode  | % Output | Lumens | Runtime (est., M35A) |
|-------|----------|--------|----------------------|
| Low   | 1%       | ~12    | 75–90h               |
| Med1  | 10%      | ~150   | 8–10h                |
| Med2  | 35%      | ~500   | 2.5–3h               |
| High  | 100%     | ~1000  | 45–55min             |

*Estimates vary by cell condition and use.*  
*Turbo (100%) is best used in bursts; ~35% is the real sustained work mode.*

## Quick Start
- Open tailcap, remove DC Fix disk blocking battery and spring  
- From OFF, full press = ON (starts at 1%)  
- Tap to cycle modes: 1% → 10% → 35% → 100%  
- Full click OFF to shut down (always starts at 1%)  
- Lockout: unscrew tailcap 1/4 turn  

## Low Voltage Protection (LVP) Behavior — TFU-F2

The TFU-F2 driver includes built-in **Low Voltage Protection (LVP)** to prevent cell over-discharge and keep the light usable in the field.

- **Trigger:** ~**3.2 V under load** (cell may read higher at rest).  
- **Behavior:**  
  - Attempting **100%** causes **one blink → automatic return to 35%**.  
  - As voltage continues to fall, **35% becomes unstable**.  
  - **10% remains stable** toward ~**3.0 V under load**.  
  - When **10% drops out**, the cell is effectively **~3.0 V** → **discontinue use**.

### Operator Guidance
- First **blink + fallback to 35%** = **swap soon**.  
- To stretch runtime, drop to **10%**; use **1%** for maps/egress only.  
- Do not deep-discharge: pull the cell if **10% drops out** or if rested voltage is ~**3.0 V**.

**Status:** Field-verified behavior (3.2 V gate; ~3.0 V dropout) for safe, repeatable operation.

---

## Build Quality

- Tail spring bypass for max current  
- Loctite 242 on hardware; MX-4 and CS109 thermal management on MCPCB/driver  
- Waterproof and drop-tested  
- Hand-assembled and tuned in the U.S.A.

---

[Full Documentation](https://github.com/TheSmashy/TFU) | [Warranty](https://github.com/TheSmashy/TFU/blob/main/WARRANTY.md)

---

Built by hand in the U.S.A. | Last updated: 2025-09-18

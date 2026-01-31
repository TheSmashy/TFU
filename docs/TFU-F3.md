# Welcome to Your TFU-F3

![TFU Logo](../TFU-LOGO.png)

**Welcome to TFU – Real Gear for Hard Use**

---

**Model:** **TFU-F3** (Field / Flood Utility)  

> ✅ Current Production Model  
> This document reflects the current TFU-F3 configuration and specifications.   
> Updated: 2026-01-30   

**Contact Support:**  
[TFU-Lights@wmode.anonaddy.com](mailto:TFU-Lights@wmode.anonaddy.com) | Reddit DM: u/thesmashy  

**Warranty:** Lifetime — details [here](https://github.com/TheSmashy/TFU/blob/main/ops/WARRANTY.md)

---

## Overview

Quad-emitter **mule** configuration for maximum flood and situational awareness.  
Designed for sustained, high-CRI output in work areas where spill and uniformity matter more than throw.

This is **not** a covert or tactical light.  
It is a **wall-of-light** tool built to illuminate everything in front of you—cleanly and honestly.

> Want to carry an S2+ full of washers? Cool, bro.  
> Want to jump out of a helo with a mule? Grab a TFU-F3 — good to go.

---

## At a Glance

- **Emitter:** Nichia **519A Quad**, **5000K**, high CRI  
- **Driver:** **22 mm 6 V 5 A boost** (Convoy XHP70 family), **Mode Group 10**  
- **Cell:** **21700** (recommended **Molicel P45B**)  
- **Optic:** Mule / no optic — maximum flood  
- **Switch:** Reverse clicky  
- **Mode Memory:** OFF (always starts at Low)

---

## Output & Runtime (Molicel P45B)

| Mode  | % Output | Lumens (est.) | Runtime (est.) |
|------:|---------:|--------------:|---------------:|
| Low   | 1%       | ~40 lm        | 150–180 h      |
| Med1  | 10%      | ~400 lm       | 15–18 h        |
| Med2  | 35%      | ~1400 lm      | 4.5–6 h        |
| High  | 100%     | ~3800–4200 lm | 35–45 min      |

*Estimates assume a healthy P45B at room temperature.*  
*High mode is thermally limited — step-down is normal and expected.*

---

## Quick Start

- Open tailcap and remove **DC-Fix disk** (battery blocker), if installed.
- From **OFF**: full click = **ON** (starts at **1%**)
- Tap to cycle modes: **1% → 10% → 35% → 100%**
- Full click **OFF** to shut down
- **Lockout:** unscrew tailcap ~1/4 turn for transport or storage

---

## Low Voltage Protection (LVP) — TFU-F3

This TFU-F3 uses a **true MCU-managed Low Voltage Protection system** built into the 6 V boost driver.  
Behavior is **progressive and intentional**, not a fault.

### Verified LVP Behavior

- **~3.2 V under load**
  - Attempting **100%** causes **one blink → automatic fallback to 35%**
  - Turbo is gated to protect the cell

- **Below ~3.2 V**
  - **35%** becomes unstable or refuses
  - **10%** remains usable

- **~3.0 V under load**
  - **10%** drops out or becomes unreliable  
  - **Discontinue use and recharge**

*Cell voltage may rebound higher at rest. Use under-load behavior as your guide.*

### Operator Guidance

- **Blink → fallback to 35% = SWAP SOON**
- Drop to **10%** to finish the task safely
- Use **1%** for map work or egress only
- Do **not** deep-discharge — remove the cell once **10% drops out**

**Status:** Field-verified Convoy boost LVP (3.2 V gate, ~3.0 V dropout)

---

## Build Quality

- Tail spring bypass for maximum current delivery
- MX-4 on MCPCB, CS109 on driver for thermal transfer
- Loctite 242 on all threaded hardware
- Hand-assembled, tuned, and tested in the U.S.A.
- Waterproof and drop-resistant (field use expected)

---

### Configuration & Mode Guide

Full configuration documentation:  
**[Config Guide](../docs/config_guide.md)**

---

[Full Documentation](https://github.com/TheSmashy/TFU) |  
[Warranty](https://github.com/TheSmashy/TFU/blob/main/ops/WARRANTY.md)   

---

Built by hand in the U.S.A.  
Last updated: **2026-01-30**

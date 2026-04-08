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
| Low   | 1%       | ~40 lm        | ~45–55 h       |
| Med1  | 10%      | ~400 lm       | ~4–6 h         |
| Med2  | 35%      | ~1400 lm      | ~1.1–1.7 h     |
| High  | 100%     | ~3800–4200 lm | 35–45 min      |

*Estimates assume a healthy P45B at room temperature.*  
*Engineering note: 100% is a ~30W class load; expect heat stepdown and aggressive battery draw (~8–10A class from the cell).*  

---

## Quick Start

- Open tailcap and remove **DC-Fix disk** (battery blocker), if installed.
- From **OFF**: full click = **ON** (starts at **1%**)
- Tap to cycle modes: **1% → 10% → 35% → 100%**
- Full click **OFF** to shut down
- **Lockout:** unscrew tailcap ~1/4 turn for transport or storage

---

## Low Voltage Protection (LVP) — TFU-F3

MCU-managed LVP is built into the 6V boost driver.  
Behavior is **intentional** and **progressive**.

---

### Behavior (Under Load)

**~3.2 V**
- 100% → *blink* → returns to 35%  
- Turbo is locked out

**Below ~3.2 V**
- 35% becomes unstable or unavailable  
- 10% remains usable

**~3.0 V**
- 10% drops out or becomes unreliable  
- **Stop use and recharge**

*Cell voltage will read higher at rest. Trust behavior under load.*

---

### Operator Guidance

- Blink → 35% = **SWAP SOON**  
- Use 10% to finish the task  
- Use 1% for minimal light only  
- If 10% fails → **STOP and recharge**  
- Do not repeatedly force 100% after stepdown  

> **If it steps you down, it’s time.**

---

### Status

Field-verified LVP  
(~3.2 V turbo gate, ~3.0 V dropout)  

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

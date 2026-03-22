# TFU / Convoy 5 A 14500 Driver Programming Guide  
> **Applies only to flashlights using the 5 A 14500 driver.**  
> ⚠️ Not for 18650, 21700, or other higher-current cells or drivers.

---

## Entering Configuration Mode

1. **Turn on the flashlight.**  
2. **Tap the switch 20 times quickly** to enter configuration mode.

> 💡 This driver has no visual interface — it uses flash sequences to indicate options.  
> When an option is flashing, **tap the switch during the flash** to select it.

---

## Option 1 — Select Mode Group  
**Flash pattern:** 1 × normal flash + 1 × buzz flash  

If selected, the light will step through **sub-options (1.1 – 1.12)**, each representing a mode group.  
If no action is taken, the flashlight will automatically proceed to **Option 2**.

<details>
<summary>📘 View Mode Groups (click to expand)</summary>

| Sub-Option | Flash Pattern | Mode Group | Modes |
|:-----------:|:--------------|:-----------|:-------|
| **1.1** | 1 flash | Group 1 | 1 % → 10 % → 30 % → 100 % |
| **1.2** | 2 flashes | Group 2 | 1 % → 10 % → 35 % → 100 % → Strobe → Biking → Battery Check |
| **1.3** | 3 flashes | Group 3 | 100 % → 35 % → 10 % → 1 % |
| **1.4** | 4 flashes | Group 4 | 1 % → 20 % → 100 % → Strobe → Biking → Battery Check |
| **1.5** | **5 flashes** | **Group 5** | **1 % → 20 % → 100 %** |
| **1.6** | 6 flashes | Group 6 | 100 % → 20 % → 1 % |
| **1.7** | 7 flashes | Group 7 | 1 % → 10 % → 50 % → Strobe → Biking → Battery Check |
| **1.8** | **8 flashes** | **Group 8** | **1 % → 10 % → 50 %** |
| **1.9** | 9 flashes | Group 9 | 50 % → 10 % → 1 % |
| **1.10** | 10 flashes | Group 10 | 20 % → 100 % |
| **1.11** | 11 flashes | Group 11 | 100 % → 20 % → Strobe |
| **1.12** | 12 flashes | Group 12 | 100 % only |

</details>

---

## Option 2 — Toggle Mode Memory  
**Flash pattern:** 2 × normal flashes + 1 × buzz flash  

Tap the switch to **enable or disable mode memory.**  
If no action is taken, the flashlight will **return to the last used mode.**

---

### Notes

- This configuration system is for the **5 A 14500 driver only.**  
- Do **not** use these instructions for larger-cell drivers (18650, 21700, etc.) — timing and flash patterns differ.  
- Mode groups are stored in driver memory and retained after power loss.  
- *“Buzz-flash”* = a short, rapid flicker indicating the end of a flash sequence.

---

*Document version 1.0 — For TFU and compatible Convoy 5 A 14500 driver builds.*

# TFU / Convoy Multi-Cell Driver Programming Guide  
> **Applies to flashlights using larger-cell drivers (e.g., 18650 / 21700).**  
> ⚠️ Not for 5 A 14500 drivers — timing and mode tables differ.

---

## Basic Operation

- **Power On / Off:** Click the switch  
- **Mode Selection:** Tap (half-press) the switch to cycle through modes  

---

## Entering Configuration Mode

1. Turn on the flashlight.  
2. Quickly **tap (half-press) the switch 20 times or more**.  
3. The light will enter configuration mode.

> 💡 The driver provides **visual feedback through flash sequences** (no screen).  
> When an option flashes, **tap the switch during the flash** to select it.

---

## Option 1 — Select Mode Group  
**Flash pattern:** 1 × normal flash + 1 × buzz flash  

Tap during this sequence to access the **mode-group sub-options**.  
If no action is taken, the light automatically proceeds to **Option 2**.

| Sub-Option | Flash Pattern | Mode Group | Modes |
|:-----------:|:--------------|:-----------|:-------|
| **1.1** | 1 flash | Group 1 | 0.1 % → 1 % → 10 % → 35 % → 100 % → Strobe → Biking → Battery Check |
| **1.2** | 2 flashes | Group 2 | 0.1 % → 1 % → 10 % → 35 % → 100 % |
| **1.3** | 3 flashes | Group 3 | 100 % → 35 % → 10 % → 1 % → 0.1 % |
| **1.4** | 4 flashes | Group 4 | 1 % → 20 % → 100 % → Strobe → Biking → Battery Check → SOS |
| **1.5** | 5 flashes | Group 5 | 1 % → 20 % → 100 % |
| **1.6** | 6 flashes | Group 6 | 100 % → 20 % → 1 % |
| **1.7** | 7 flashes | Group 7 | 0.1 % → 1 % → 10 % → 50 % → Strobe → Biking → Battery Check → SOS |
| **1.8** | 8 flashes | Group 8 | 0.1 % → 1 % → 10 % → 50 % |
| **1.9** | 9 flashes | Group 9 | 50 % → 10 % → 1 % → 0.1 % |
| **1.10** | 10 flashes | Group 10 | 1 % → 10 % → 35 % → 100 % |
| **1.11** | 11 flashes | Group 11 | 100 % → 20 % → Strobe |
| **1.12** | 12 flashes | Group 12 | 100 % only |

</details>

---

## Option 2 — Toggle Mode Memory  
**Flash pattern:** 2 × normal flashes + 1 × buzz flash  

Tap the switch to **enable or disable** mode memory.  
If no action is taken, the flashlight will **return to the last used mode**.

---

### Notes

- This configuration applies to **high-current or multi-cell drivers** (18650, 21700, etc.).  
- For the 5 A 14500 driver, see: [`config_guide_14500.md`](./config_guide_14500.md).  
- *“Buzz flash”* = a short, rapid flicker marking the end of a flash sequence.  
- All selected settings are stored in driver memory and persist after power loss.

---

*Document Version 1.0 — For TFU and compatible Convoy multi-cell drivers.*

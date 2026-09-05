# TFU Lights – User Documentation

Welcome to the **TFU Lights Documentation Hub**.

This directory contains operation, configuration, maintenance, and usage guides for TFU production and development models.

These guides are written for **end users**. No soldering, programming, or engineering knowledge is required.

---

## Product Guides

| File | Model | Description |
|:-----|:------|:------------|
| [`TFU-E0.md`](./TFU-E0.md) | **E0** | Compact, regulated 14500 instrument light designed for precision tasks and light EDC use. |
| [`TFU-E1.md`](./TFU-E1.md) | **E1** | Compact EDC light designed for everyday reliability. Includes operation, runtime, and care instructions. |
| [`TFU-E2.md`](./TFU-E2.md) | **E2** | Compact, high-output, high-CRI EDC platform built around a triple Nichia emitter array and 5 A regulated buck driver. |
| [`TFU-E3.md`](./TFU-E3.md) | **E3** | High-output 14500 EDC platform using triple Nichia 519A emitters and advanced driver tuning. |
| [`TFU-E4.md`](./TFU-E4.md) | **E4** | Compact, high-output, high-CRI EDC light using a single Nichia 519A 5000K emitter and 5 A regulated buck driver. |
| [`TFU-T2B.md`](./TFU-T2B.md) | **T2B** | Compact brass 14500 EDC light using a single Nichia 519A 4000K high-CRI emitter. |
| [`TFU-F1.md`](./TFU-F1.md) | **F1** | Field light built for task work and general-purpose use. Includes runtime data and configuration information. |
| [`TFU-F2.md`](./TFU-F2.md) | **F2** | Extended-runtime field light optimized for a balanced beam, high-CRI output, and durability. |
| [`TFU-F3-Legacy.md`](./TFU-F3-Legacy.md) | **F3 Legacy** | Retired performance-tuned mule configuration retained for reference. |
| [`TFU-F3.md`](./TFU-F3.md) | **F3** | Performance-tuned mule with standard driver configuration and 5000K CCT. Includes advanced mode details. |
| [`TFU-F4.md`](./TFU-F4.md) | **F4** | High-CRI, ultralight field light with a smooth, usable beam for everyday work and spotting. |
| [`TFU-T1.md`](./TFU-T1.md) | **T1** | Hardened tactical light designed for longer-range positive identification (PID) and dependable field use. |
| [`TFU-T2.md`](./TFU-T2.md) | **T2** | Compact 14500 high-CRI tactical light using a Nichia 519A 5000K emitter and 5 A regulated buck driver. |
| [`TFU-T3.md`](./TFU-T3.md) | **T3** | Compact tactical thrower using an SFT40 6500K emitter, 8 A buck driver, throw reflector, and forward-clicky switch. |

---

## Configuration & Interface Guides

| File | Applies To | Description |
|:-----|:-----------|:------------|
| [`Anduril.md`](./Anduril.md) | Andúril UI | User guide and interface map for lights running the Andúril firmware. Covers basic operation, ramping, auxiliary LEDs, configuration, and advanced functions. |
| [`config_guide_14500.md`](./config_guide_14500.md) | 5 A 14500 Driver | Configuration instructions for 14500-based lights, including T-series and select E-series models. |
| [`config_guide.md`](./config_guide.md) | 18650 / 21700 Drivers | Configuration guide for larger-cell lights, including supported E-series and F-series models. Covers mode groups and memory options. |
| [`Ramping.md`](./Ramping.md) | Ramping Driver | Operation and configuration instructions for TFU side-switch ramping drivers. |

Configuration and interface guides cover functions such as mode selection, programming, ramping behavior, mode memory, and advanced user-interface features. Refer to the individual product guide to determine which configuration guide applies to a specific light.

---

## Maintenance & Hardening

| File | Description |
|:-----|:------------|
| [`HardeningService.md`](./HardeningService.md) | TFU Hardening Service information for lights serviced and upgraded at the boathouse. |

---

## Approved Cells

| File | Description |
|:-----|:------------|
| [`approved_cells.md`](./approved_cells.md) | Tested and approved lithium-ion cells, including model-specific cell recommendations and compatibility. |

---

## Warranty

| File | Description |
|:-----|:------------|
| [`WARRANTY.md`](../ops/WARRANTY.md) | TFU Lights warranty and guarantee information. |

---

## About TFU Lights

**TFU (Tactical Field Use)** flashlights are hand-built, tested, and field-verified for reliability and performance.

Each model is designed around three principles:

1. **Thermal efficiency** – Solid heat paths and effective thermal management.
2. **Mechanical integrity** – Secure assemblies, durable components, and no shortcuts.
3. **Electrical reliability** – Regulated drivers, quality components, and clean assembly.

### Battery and Configuration Notes

- Use only the lithium-ion cells specified or approved for your TFU light.
- Follow the battery recommendations in the individual product guide and [`approved_cells.md`](./approved_cells.md).
- Driver behavior and configuration procedures vary by model.
- Do not assume configuration instructions for one driver family apply to another.
- Some models use specialized interfaces such as Andúril; consult the applicable interface guide before changing advanced settings.

---

*Documentation maintained by TheSmashy*  
*© 2025–2026 TFU Lights – Tactical Field Use Series*

# TFU-F2 – Field Utility Light

**Series:** TFU-F (Field)  
**Model:** TFU-F2  
**Status:** Development Reference / Production Ready  
**Mission Profile:**  
Rugged field/duty flashlight with balanced flood output, excellent CRI, and sustained regulation. Designed for extended runtime, reliability, and performance under stress.

---

## Build Evolution

The initial TFU-F2 prototype was constructed on a Convoy **M1** host with a Nichia B35AM emitter and 6 V 2 A boost driver. While electrically solid and highly usable, testing showed the M1’s 18650 form factor lacked the thermal mass, runtime, and ergonomics required for the TFU “Field” series.  

The platform has since transitioned to the **Convoy M21B (21700)** host, which delivers the proper size, mass, and endurance expected of a field-grade light. The M21B build now defines the baseline specification for all future F2 production lights.

---

## Build Specifications

| Component | Detail |
|------------|---------|
| **Host** | Convoy M21B (Black) – enhanced thermal path, deep fins |
| **Emitter** | Nichia B35AM (5000 K) – high CRI, smooth flood, true-color rendering |
| **Driver** | 6 V 2 A Boost Driver – efficient, regulated, optimized for B35AM |
| **Switch** | Forward clicky – optimized for gloved use |
| **Clip** | Black steel M21B clip – deep carry, durable |
| **Bypass** | 22 AWG silicone wire tail spring bypass |
| **Thermal** | MX-4 under MCPCB; CS109 thermal bond on driver |
| **Securing** | Loctite 242 on driver and switch retaining rings |

---

## Power Source

| Cell | Notes |
|-------|--------|
| **Molicel P45B** | 4500 mAh – high-drain 21700 cell, excellent sustainability |
| **Samsung 40T** | 4000 mAh – slightly more punch, less runtime |

---

## Output & User Interface

| Parameter | Value |
|------------|--------|
| **Mode Group** | Group 10: 1 % → 10 % → 35 % → 100 % |
| **Memory** | ON (forward clicky optimized) |
| **UI Type** | Stepped modes, simple layout |
| **Beam Profile** | Wide hotspot, smooth spill – balanced throw and flood |

---

## Use Case

- Utility and duty carry  
- Task and maintenance lighting  
- Indoor / outdoor field use  
- Sustained runtime in adverse conditions  
- Reliable one-hand operation with gloves  

---

## Testing Notes

- Thermal curve logging via Pi test rig at 100 % output  
- Runtime comparison between P45B and 40T cells  
- Beamshot profiling (3 m / 10 m / 30 m distances)  
- Drop and water tests for IPX8 validation  
- Ergonomic evaluation in field kit and gloved operation  

---

> **TFU – Real Gear for Hard Use**  
> Designed, built, and field-tested by TFU Labs.

---

**Version:** v1.2  
**Last Updated:** 2025-10-16  
**[← Back to README](../README.md)**  

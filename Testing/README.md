# TFU Testing Methodology

This folder documents the TFU flashlight testing rig and procedures.  
Goal: generate repeatable, comparable data for builds and driver swaps.

---

## Rig Overview
- **Lux Sensor:** TSL2591 (Adafruit breakout, I²C)  
- **Temp Probe:** DS18B20 with thermal pad, mounted to flashlight surface  
- **Logger:** Raspberry Pi Zero W running Python logger → InfluxDB + Grafana  
- **Mount:** GorillaPod tripod with fixed clamp, ~1m from sensor  
- **Environment:** Indoor, controlled (ambient 20–22 °C, no airflow)

---

## Protocols
1. **Baseline run** → 15 minutes at 100%  
2. **Step test** → 25% → 50% → 100% cycling, 1 min each  
3. **Sustained bursts** → 5 × 3 min at 100% with 2 min rest  
4. **Cell recording** → start/end voltage, IR noted  

Details in `/protocols/`.

---

## Data
All runs export to CSV + Grafana dashboards. Each `/runs/` folder contains:
- Raw logs (`.csv`)  
- Charts (`.png`)  
- Notes (`.md`) with observations

---

## Why It Matters
By locking the rig geometry and protocol, we ensure:
- **Repeatability** → same setup, different builds = clean comparisons  
- **Transparency** → anyone can see how data was collected  
- **Validation** → A/B driver swaps (linear vs. buck) are backed with evidence


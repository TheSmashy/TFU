# Sensor Stack Overview

This document summarizes the sensors used in the TFU thermal/lux test rig.  
Each sensor has its own dedicated documentation file for wiring and details.

---

## Sensors in Use

- **Lux Measurement**  
  - **TSL2591** → High dynamic range I²C lux sensor  
  - Role: Captures output over time (lux vs. seconds)  
  - Details: [TSL2591.md](./TSL2591.md)

- **Surface Temperature**  
  - **DS18B20** → 1-Wire digital probe  
  - Role: Logs flashlight body temperature during sustained runs  
  - Details: [ds18b20.md](./ds18b20.md)

- **Ambient Conditions**  
  - **BME280** → I²C environmental sensor  
  - Role: Tracks room temperature, humidity, and barometric pressure  
  - Details: [bme280.md](./bme280.md)

---

## Integration

- All sensors connect to a **Raspberry Pi logger**.  
- Data streams into **InfluxDB** → visualized via **Grafana dashboards**.  
- Sampling intervals:  
  - Lux & surface temp: ~2s  
  - Ambient (BME280): ~10s  

---

## Notes

- Keeping sensor placement consistent is critical for repeatability.  
- Rig photos for reference: [Thermal-Test-Rig-01.jpg](./Thermal-Test-Rig-01.jpg)  
- Each test run should note:  
  - Ambient conditions (BME280)  
  - Probe placement (DS18B20)  
  - Lux sensor distance/orientation (TSL2591)  

---

## Next Steps

- Add diagrams of wiring for quick reference.  
- Add calibration notes (lux baseline, temp verification).  

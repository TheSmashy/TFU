# **TFU Approved Cells**
Reliable power sources for field-grade lights.

TFU lights are engineered around specific load profiles, thermal envelopes, and cell behavior under sag.  
Using the correct cell ensures predictable regulation, safe operation, and the performance each light was built to deliver.

This guide lists all **TFU-approved cells** by model and battery class.

---

## **What “TFU Approved” Means**

A cell qualifies as TFU-approved if it demonstrates:

- Safe discharge characteristics under the driver load  
- Predictable voltage sag  
- Thermal compatibility with the host and driver  
- Adequate runtime for the intended mission profile  
- Manufacturer consistency (no junk chemistry, no rewrap roulette)

TFU lights are tested using the recommended cells below.

---

# **1. 21700 Class — F-Series (F1, F2, F3…)**

### **TFU Standard Cell — Molicel P42A**
- 4200 mAh, ~35A CDR  
- Best voltage stability at 5–8A  
- Industry-leading thermal behavior  
- **Primary F-series cell**

### **Alternates**
**Molicel P45B** — fully approved, higher capacity and CDR

### **Allowed (Not Preferred)**
**Samsung 40T** — acceptable, but heavier sag

### **Not Approved**
- Samsung 50E  
- Molicel M50  
- Lishen LR2170L  
(High capacity, poor sag characteristics)

---

# **2. 18650 Class — E2, T1 (M2), Legacy Builds**

## **Primary Recommended Cell — Samsung 30Q**
- 3000 mAh, 15A  
- Ideal for 5A buck drivers  
- Clean regulation curve  
- **TFU standard for all 18650 E-series lights**

---

## **High-Discharge Special Use**
### **Molicel P30B**
- 3000 mAh  
- Very high discharge  
- **TFU-Approved only for:**  
  - **T1 (M2 host, 8A buck)**  
  - **T3 (S6 host, 8A buck)**

Also acceptable, but older chemistry:  
### **Samsung 25R**  
-2500 mAh  
-Very high discharge  

---

## **Runtime Option**
### **Molicel M35A**
- 3500 mAh  
- Best for low-medium tasks  
- Not for high-drain (greater than 5A) use

---

# **3. 18350 Class — E1, E2 Shorty, Compact Builds**

## **E1 — 6V 2A Boost Driver**
### **TFU Standard — Vapcell H16**
- 1600 mAh  
- Handles boost driver startup load  
- E1 is tuned around this cell

### **Alternate — Vapcell M11v2**
- Higher discharge (10A CDR)  
- Lower runtime - 1100 mAh

---

## **E2 Shorty, E4 — 5A Buck**
### **TFU Standard — Vapcell M11v2**
- Best 18350 for 5A continuous

### **Alternate — Vapcell H16**
- Higher capacity  
- Lower performance ceiling

---

# **4. 14500 Class — E3 and T2**

---

## **E3 — Triple 14500 (5A Buck, 519A emitters)**

### **TFU Standard — Vapcell H10 → K10 (new)**
- High discharge needed for triple emitters  
- Supports Group 1 (1–10-30–100%)   

**Thermal Warning:**  
- 100% output = **120 seconds max**  
- Stepdown expected

### **Balanced Operation — Vapcell F12 → F15**
- Cooler runtime  
- Ideal for everyday customers  
- Best with **Group 8 (1–10–50%)**

---

## **T2 — 14500, Group 8 Default**

### **TFU Standard — Vapcell F12 / F15**
- Perfect for 1–10–50% daily-use  
- Cool running, reliable

### **Optional High Output — H10 / K10**
- Allowed only with **Group 5 (1–20–100%)**  
- 100% mode must be limited to **45 seconds**  

---

# **5. Quick Reference Table**

| Model | Driver | Battery | Approved Cells | Notes |
|-------|--------|---------|----------------|-------|
| **F-Series** | 5A / 8A | 21700 | P42A (Std), P45B | TFU primary platform |
| **T1 (M2)** | 8A Buck | 18650 | 30Q, P30B, 25R | P30B only recommended here |
| **E2 (18650)** | 5A Buck | 18650 | 30Q (Std), M35A | M35A for runtime builds |
| **E2 Shorty (18350)** | 5A Buck | 18350 | M11v2 (Std), H16 | M11v2 = output |
| **E1 (18350)** | 6V Boost | 18350 | H16 (Std), M11v2 | E1 tuned for H16 |
| **E3 (14500)** | 5A Buck | 14500 | H10/K10 (Std), F12/F15 | Triple emitter limits |
| **T2 (14500)** | 3-mode | 14500 | F12/F15 (Std), H10/K10 | H10/K10 w/ Group 5 |

---

# **6. Mode Guide Links**

➡️ **18650 / 18350 / 21700 Mode Guide**  
[config_guide.md](../docs/config_guide.md)

➡️ **14500 Mode Guide**  
[config_guide_14500.md](../docs/config_guide_14500.md)  

---

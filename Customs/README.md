# TFU Custom Lights

This folder holds documentation for **one-off or serialized TFU Custom builds** — lights built as gifts, prototypes, or limited runs outside the main TFU-E / F / M series.

Each light has a Markdown page with its own specs, photos, and provenance record.

---

## 🔢 Serial Format
`TFU-CUST-###`

- Sequential numbering across all customs.  
- Optionally append a suffix for host or material, e.g.:
  - `TFU-CUST-002-S2` — S2+ host
  - `TFU-CUST-003-Ti` — titanium tube
- Example label on packaging:
  > **TFU-CUST-001** — PE1 Prototype  
  > *Built by TFU / ItascaSec Works*

---

## 🧭 Index

| Serial | Name / Tagline | Host | Emitter(s) | Driver | Status | Link |
|--------|----------------|------|-------------|---------|---------|------|
| TFU-CUST-001 | PE1 Prototype — *Gets the job done* | S2+ Ti-18350 | 3× 519A 4500 K | 3 V 5 A Buck | Retained | [PE1 Prototype](TFU-CUST-001.md) |
| TFU-CUST-002 | S6 Shorty | S6 Cu 18350 | SFT40 6500 K | 3 V 8 A Buck | For Sale | [S6 Shorty](TFU-CUST-002.md) |
| TFU-CUST-003 | M1 Shelf Queen | M1 Tan 18650 | SFT25R 5000 K | 4-Mode Driver | For Sale | [M1 Shelf Queen](TFU-CUST-003.md) |

_Add new builds to this table and create a matching `.md` file in this folder._

---

## 🧾 Individual Build Template

Copy the snippet below into a new file named `/Customs/TFU-CUST-###.md`.

```markdown
# TFU-CUST-### — [Build Name or Tagline]

**Status:** [Retained / Sold / Gifted / For Sale]  
**Date built:** YYYY-MM-DD  
**Host:** [e.g., Convoy S2+ Black]  
**Tube:** [e.g., Titanium 18350 Tube]  
**Emitter(s):** [e.g., 3× 519A 4500 K]  
**Driver:** [e.g., 3 V 5 A Buck Driver]  
**Optic / Window:** [e.g., AR Glass No Optic]  
**Switch:** [Metal / Black / Forward Clicky]  
**Clip:** [ReyLight DLC / Stonewashed Ti / Convoy Long]  
**Cell Recommendation:** [e.g., Vapcell H16]  
**Glue / Fasteners:** [CS109 / Loctite 242 / MX-4 etc.]  

## Notes
- [Thermal / runtime behavior, CCT feel, tint notes, etc.]
- [Any special features, quirks, or story line]

## Photos
![Hero](../Assets/CUST-###-hero.jpg)  
![Beam](../Assets/CUST-###-beam.jpg)

> *Tagline or quote here*

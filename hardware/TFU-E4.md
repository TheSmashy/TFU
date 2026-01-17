# TFU-E4

**Series:** E (Everyday / EDC)  
**Model:** TFU-E4  
**Role:** Compact EDC / task light (high-CRI, practical beam)  
**Status:** In development (first build scheduled: 2026-01-18)

---

## Overview

The **TFU-E4** is a compact, no-nonsense EDC light tuned for real-world use: clean UI, high CRI, and a beam profile that’s useful indoors, on a map, and at arm’s length—without feeling like a toy.

This page is the canonical reference for **specs, build method, QC checks, and revisions**.

---

## Specifications

| Category | Spec |
|---|---|
| Host | Convoy S3 |
| Emitter | 519A 5000K |
| Driver | 5 A Buck |
| Reflector | OP reflector |
| Lens | AR glass |
| Cell | 18350 |
| UI | mode group 10, memory off, 1-10-35-100% |
| Switch | reverse clicky, rubber boot |
| Body / Finish | black colorway, stonewash clip, silver bezel |

---

## Beam Profile

**Target behavior**
- **Low:** usable for maps / bedside / reading without blasting
- **Mid:** practical household / inspection
- **High:** short bursts for outdoor/task use

**Notes**
- Describe hotspot/spill behavior and any diffusion choices (TIR bead vs matte, DC-Fix, etc.)
- If this is an “Urban” type beam, say so explicitly.

---

## Default Mode Configuration

- **Mode set:** 1% → 10% → 35% → 100%
- **Memory:** of)
- **Strobe/SOS:** disabled

---

## Build Notes

### Assembly choices
- **Lead management:** (e.g., driver leads tied in a knot before seating to control slack)
- **Thermal interface:** `TBD` (MX-4 / etc.)
- **Thread treatment:** `TBD` (light lube / none)
- **Retention:** `TBD` (Loctite/CS109 on rings if used)

### Known “gotchas”
- Negative lead routing in pill builds can cause intermittent switch behavior if pinched or stressed.
- Note any tight-fit steps (gasket alignment, optic seating, reflector centering, etc.)

---

## QC Checklist (per unit)

**Electrical**
- [ ] Tailcap current sanity check (optional)
- [ ] No flicker when tapping body/head
- [ ] No switch weirdness after full assembly
- [ ] All modes cycle correctly
- [ ] Memory behavior matches spec

**Mechanical**
- [ ] Driver retaining ring torqued / seated
- [ ] MCPCB seated flat
- [ ] Optic/reflector centered; no emitter shadowing
- [ ] Lens clean (inside/out)
- [ ] Clip torqued; no spin
- [ ] Threads smooth; no grit

**Thermal**
- [ ] Run on high for `TBD` minutes: stable, no stepdown oddities beyond driver behavior
- [ ] Body warms predictably; no sudden thermal spikes

---

## Testing

### Smoke test
- Cell: `TBD` (known-good)
- Duration: `TBD`
- Result: `TBD`

### Runtime / thermal (optional)
- Ambient: `TBD`
- Notes: `TBD` (regulation behavior, comfort, stepdown)

---

## Bill of Materials (BOM)

| Part | Spec | Source | Cost |
|---|---|---:|---:|
| Host |  |  |  |
| Driver |  |  |  |
| Emitter + MCPCB |  |  |  |
| Optic/Reflector |  |  |  |
| Lens |  |  |  |
| Gasket/spacer |  |  |  |
| Clip |  |  |  |
| Switch parts |  |  |  |
| Misc | solder, paste, etc. |  |  |

**Total (parts):** `$TBD`  
**Notes:** cells optional / sold separately

---

## Revisions

### Rev A — Initial build (planned)
- First production-intent spec
- Record any deviations here

### Rev B — `TBD`
- Change log: driver/optic/UI/assembly improvements

---

## Photos / Media

- Add hero photo(s)
- Add beam video link(s)
- Add “mode progression” clip

---

## Serial / Labeling

- Model: **TFU-E4**
- Serial format: TFU-E4-### 

---

## Field Notes

Short bullets after real carry/use:
- What surprised you
- What you’d change
- What you’d keep forever

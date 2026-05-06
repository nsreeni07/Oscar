# Oscar
Autonomous UAV system that performs precision crop monitoring using aerial imaging and vegetation index mapping. The drone executes pre-programmed waypoint missions, captures geotagged imagery, and processes data on a ground station to generate field health maps.
# Project OSCAR — Bill of Materials

> Custom 850mm endurance agricultural mapping quadcopter

---

## Frame

| Item | Qty | Cost | Purpose |
|------|:---:|-----:|---------|
| Custom 850mm frame (self-designed + 3D printed parts) | 1 | $50.00 | Core structure — round-tube CF frame with internal wire routing and clamp motor mounts |
| Round CF tubes — 16mm OD × 2mm wall × 500mm | 4 | $13.99 | Arms — 2mm wall critical at 325mm arm length to prevent flex oscillation |
| M3 Screw Assortment (motor mounts) | 1 | $9.99 | Frame assembly — motor mount fasteners |
| M3 Screw Assortment (FC/ESC stack) | 1 | $8.99 | Frame assembly — flight controller and ESC retention |
| Heat-set inserts M3 × OD4.5 | 1 | $3.03 | Motor mount clamp inserts |


---

## Propulsion

| Item | Qty | Cost | Purpose |
|------|:---:|-----:|---------|
| 4114 320KV brushless motors | 4 | $43.02 | Low-KV motors for 17″ props on 6S — ~3,500g max thrust each, 25mm bolt pattern |
| 1755 carbon fiber props (2× CW, 2× CCW) | 2 pairs | $11.85 | CF over plastic — at 850mm tip speeds plastic props flex and reduce efficiency |

---

## Power

| Item | Qty | Cost | Purpose |
|------|:---:|-----:|---------|
| 6S 5000mAh LiPo 45C XT90 | 1 | $54.99 | Main power — 22.2V nominal, 111Wh total |
| XT90 Female → XT60 Male adapter | 1 | $1.14 | Battery and power lead interface |
| UBEC 5V 3A (2-pack) | 1 pk | $2.23 | Two dedicated 5V rails — one for FC, one for Pi |
| 12 AWG silicone wire — red + black, 1m each | 1 | $0.99 | Main battery leads — rated for 6S current draw |
| 18 AWG silicone wire | 1 | $3.14 | Motor phase extensions through arm tubes |
| Heat shrink assortment 2–12mm | 1 | $2.52 | Insulate all solder joints |

---

## Flight Control

| Item | Qty | Cost | Purpose |
|------|:---:|-----:|---------|
| Matek H743 Slim V3 flight controller | 1 | $74.51 | Main flight computer |
| Holybro PM06 V2 power module | 1 | $20.99 | Power distribution |
| M8N GPS module with compass | 1 | $31.24 | Position hold, RTL, waypoint navigation — external compass on mast |
| SiK 915MHz telemetry pair | 1 | $58.99 | Live MAVLink to laptop — mission monitoring over-air |
| FlySky FS-i6 TX + FS-iA6B RX bundle | 1 | $49.99 | RC control — 6 channels, iBus, receiver included |

---

## Compute / Payload

| Item | Qty | Cost | Purpose |
|------|:---:|-----:|---------|
| Raspberry Pi Zero 2W | 1 | $18.00 | Companion computer — MAVLink listener, distance trigger, camera capture, geotagging |
| Raspberry Pi Camera v2 NoIR 8MP | 1 | $15.00 | NIR-capable sensor for NDVI — IR-cut filter removed |
| 22-pin → 15-pin CSI ribbon cable 15cm | 1 | $2.50 | Required adapter for Pi Zero 2W 22-pin CSI port |
| 680nm bandpass filter 12mm round | 1 | $3.23 | Blocks visible blue/green, transmits red + NIR for NDVI channel separation |
| Single-axis passive gimbal (custom) | 1 | ~$8.00 | Self-designed pendulum camera stabilizer — period calculated to avoid pitch resonance |
| 32GB microSD card Class 10 A1 | 1 | ~$8.00 | Pi OS and survey image storage |

---

## Hardware & Consumables

| Item | Qty | Cost | Purpose |
|------|:---:|-----:|---------|
| Anti-vibration FC damper grommets | 1 pk | $0.99 | Isolate FC IMU from motor vibration |
| Blue Loctite 243 threadlocker | 1 | $9.99 | Motor mount bolts and prop adapters |
| Zip ties 2.5mm × 100 | 1 pk | $0.99 | Wire management inside hub |
| Kapton tape (polyimide) | 1 roll | $0.99 | Insulate FC and ESC contacts |

---

## Cost Summary

| Category | Subtotal |
|----------|:--------:|
| Frame | ~$99 |
| Propulsion | ~$55 |
| Power | ~$65 |
| Flight Control | ~$239 |
| Compute / Payload | ~$55 |
| Hardware & Consumables | ~$13 |
| **Total (estimated)** | **~$526** |

# Oscar
Autonomous UAV system that performs precision crop monitoring through systematic aerial imaging and vegetation index mapping across agricultural fields. The drone executes pre-programmed waypoint missions via INAV autopilot, with an onboard Raspberry Pi Zero 2W capturing geotagged near-infrared imagery using a NoIR camera and 680nm bandpass filter at each waypoint. Upon mission completion, imagery is transferred to a ground station running WebODM, which stitches frames into orthomosaic maps and calculated NDVI values to produce color-coded field health maps highlighting crop health, irrigation stress, and potential disease pressure. 



<img width="960" height="786" alt="Screenshot 2026-05-12 180331" src="https://github.com/user-attachments/assets/5cb71a60-cdf0-4a29-b372-2b2cad4f5c3e" />

<img width="1345" height="641" alt="Screenshot 2026-05-06 182000" src="https://github.com/user-attachments/assets/735606a8-7236-477b-a397-c1ffcca2f356" />


<img width="1110" height="785" alt="Screenshot 2026-05-12 113512" src="https://github.com/user-attachments/assets/066d5c06-10ed-4771-af28-48e4128f38d5" />


# Project OSCAR — Bill of Materials

> Custom 850mm endurance agricultural mapping quadcopter

---

## Frame

| Item | Qty | Cost | Purpose |
|------|:---:|-----:|---------|
| Custom 850mm frame (self-designed + 3D printed parts) | 1 | $0 | Core structure — round-tube CF frame with internal wire routing and clamp motor mounts |
| Round CF tubes — 16mm OD × 2mm wall × 500mm | 4 | $0| Arms — 2mm wall critical at 325mm arm length to prevent flex oscillation |
| M3 Screw Assortment (motor mounts) | 1 | $0 | Frame assembly — motor mount fasteners |
| M3 Screw Assortment (FC/ESC stack) | 1 | $0 | Frame assembly — flight controller and ESC retention |
| Heat-set inserts M3 × OD4.5 | 1 | $0 | Motor mount clamp inserts |


---

## Propulsion

| Item | Qty | Cost | Purpose |
|------|:---:|-----:|---------|
| 4114 320KV brushless motors | 4 | $0 | Low-KV motors for 17″ props on 6S — ~3,500g max thrust each, 25mm bolt pattern |
| 1755 carbon fiber props (2× CW, 2× CCW) | 2 pairs | $0 | CF over plastic — at 850mm tip speeds plastic props flex and reduce efficiency |

---

## Power

| Item | Qty | Cost | Purpose |
|------|:---:|-----:|---------|
| 6S 5000mAh LiPo 45C XT90 | 1 | $0 | Main power — 22.2V nominal, 111Wh total |
| XT60 Male | 1 | $1.38 | Battery and power lead interface | [https://tinyurl.com/2z8uudk9](url)
| UBEC 5V 3A (2-pack) | 1 pk | $0 | Two dedicated 5V rails — one for FC, one for Pi |
| 12 AWG silicone wire — red + black, 1m each | 1 | $0 | Main battery leads — rated for 6S current draw |
| 18 AWG silicone wire | 1 | $0 | Motor phase extensions through arm tubes |
| Heat shrink assortment 2–12mm | 1 | $0 | Insulate all solder joints |

---

## Flight Control

| Item | Qty | Cost | Purpose |
|------|:---:|-----:|---------|
| Matek H743 Slim V3 flight controller | 1 | $74.51 | Main flight computer |[https://www.amazon.com/HeEHQA-Controller-Compatible-STM32H743VIT6-Barometer/dp/B0DZWXG12P](url)
| Holybro PM06 V2 power module | 1 | $20.99 | Power distribution |[https://holybro.com/products/micro-power-module-pm06-v2?srsltid=AfmBOopocQf-cEABsOn1cCE1-NMtm74523a-JO5FzjXD4KCYBg8PD4NU](url)
| M8N GPS module with compass | 1 | $0 | Position hold, RTL, waypoint navigation — external compass on mast |
| SiK 915MHz telemetry pair | 1 | $58.99 | Live MAVLink to laptop — mission monitoring over-air |[https://holybro.com/products/sik-telemetry-radio-v3?variant=41562952302781](url)
| FlySky FS-i6 TX + FS-iA6B RX bundle | 1 | $0 | RC control — 6 channels, iBus, receiver included |

---

## Compute / Payload

| Item | Qty | Cost | Purpose |
|------|:---:|-----:|---------|
| Raspberry Pi Zero 2W | 1 | $17.99 | Companion computer — MAVLink listener, distance trigger, camera capture, geotagging |[https://www.microcenter.com/product/683270/raspberry-pi-raspberry-pi-zero-w-2-with-headers?](url)bvstate=pg%3A2%2Fct%3Ar&osfs=true&storeid=075
| Raspberry Pi Camera v2 NoIR 8MP | 1 | $15.00 | NIR-capable sensor for NDVI — IR-cut filter removed |[https://www.digikey.com/en/products/detail/raspberry-pi/SC0024/6152811](url)
| 22-pin → 15-pin CSI ribbon cable 15cm | 1 | $0 | Required adapter for Pi Zero 2W 22-pin CSI port |
| 680nm bandpass filter 12mm round | 1 | $0 | Blocks visible blue/green, transmits red + NIR for NDVI channel separation |
| Single-axis passive gimbal (custom) | 1 | $0 | Self-designed pendulum camera stabilizer — period calculated to avoid pitch resonance |
| 32GB microSD card Class 10 A1 | 1 | $0 | Pi OS and survey image storage |

---

## Hardware & Consumables

| Item | Qty | Cost | Purpose |
|------|:---:|-----:|---------|
| Anti-vibration FC damper grommets | 1 pk | $0 | Isolate FC IMU from motor vibration |
| Blue Loctite 243 threadlocker | 1 | $0 | Motor mount bolts and prop adapters |
| Zip ties 2.5mm × 100 | 1 pk | $0 | Wire management inside hub |
| Kapton tape (polyimide) | 1 roll | $0 | Insulate FC and ESC contacts |
| Solder | 1 roll | $2.55 | Insulate FC and ESC contacts | [https://tinyurl.com/3x5hzd6u](url)
| Desolder | 1 roll | $1.99 | Insulate FC and ESC contacts | https://tinyurl.com/2yraufwr
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
| Shipping | ~$35 |
| Grant Total( Estimated Requesting Amount) | $227.02 |

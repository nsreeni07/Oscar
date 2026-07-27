OSCAR

Autonomous UAV system for precision agricultural crop monitoring

OSCAR is a custom-built 850mm quadcopter designed to fly automated survey missions over farmland and produce NDVI (Normalized Difference Vegetation Index) health maps of crops. It flies pre-programmed waypoint missions on INAV, captures geotagged near-infrared imagery at each waypoint using a modified Raspberry Pi camera, and hands that imagery off to a ground station for orthomosaic stitching and vegetation analysis. The end result is a color-coded map of a field showing where crops are healthy, where they're under irrigation stress, and where disease pressure might be building, all without a human piloting the aircraft or walking the field.

Onshape CAD: https://cad.onshape.com/documents/19523291b70a9c787e4fbec5/w/8af018b0ace6f9250dc6f3df/e/06f56f02d452d38e7c73aa30 
Full BOM: https://docs.google.com/spreadsheets/d/1ItluG4JZ7m0poAZtw0F7x5zs6U-Jy8w3EoTn_GnxS2I

How it works

OSCAR flies a field, takes pictures, and turns those pictures into a crop health map. Three steps:

Plan — a survey area is broken into a grid of GPS waypoints with enough overlap for the images to stitch together later. This mission gets loaded onto the flight controller in INAV Configurator.
Fly and capture — the drone flies the waypoints on its own. At each one, the flight controller tells the Pi Zero 2W over MAVLink that it's arrived. The Pi triggers the NIR camera (fitted with a 680nm bandpass filter, so it only sees red and near-infrared light) and geotags the image with the GPS position.
Process — after landing, the images go from the Pi's SD card to a ground station laptop running WebODM. WebODM stitches them into one map of the field and runs NDVI, which compares red vs. near-infrared reflectance to score plant health. Healthy plants reflect a lot of NIR, stressed or dying plants reflect more red. WebODM turns that into a color map, red for poor health, green for good, so problem spots in the field are obvious at a glance.
System architecture

Keeping them separate means the flight stack can be tuned and flown with no payload attached, and the imaging pipeline can be bench-tested with a fake waypoint signal without ever leaving the ground.

<img width="960" height="786" alt="Screenshot 2026-05-12 180331" src="https://github.com/user-attachments/assets/5cb71a60-cdf0-4a29-b372-2b2cad4f5c3e" />

<img width="1345" height="641" alt="Screenshot 2026-05-06 182000" src="https://github.com/user-attachments/assets/735606a8-7236-477b-a397-c1ffcca2f356" />


<img width="1110" height="785" alt="Screenshot 2026-05-12 113512" src="https://github.com/user-attachments/assets/066d5c06-10ed-4771-af28-48e4128f38d5" />


# Project OSCAR — Bill of Materials
|OSCAR — Updated Bill of Materials|FIELD2                                             |FIELD3|FIELD4        |FIELD5        |FIELD6                                               |FIELD7                                                                           |
|---------------------------------|---------------------------------------------------|------|--------------|--------------|-----------------------------------------------------|---------------------------------------------------------------------------------|
|                                 |                                                   |      |              |              |                                                     |                                                                                 |
|Category                         |Item                                               |Qty   |Unit Price ($)|Line Total ($)|Notes                                                |Link                                                                             |
|Flight Controller / ESC          |SpeedyBee F405 V4 BLS 60A 30x30 FC + 60A 4-in-1 ESC|1     |$70.31        |$70.31        |FC + ESC stack, replaces F722 + separate PDB/PM06    |https://tinyurl.com/2nz8ucyx                                                     |
|Companion Computer               |Raspberry Pi Zero 2W                               |1     |$20.00        |$20.00        |Runs NDVI pipeline + MAVLink telemetry               |https://www.adafruit.com/piz2w?src=raspberrypi                                   |
|Camera                           |Pi Camera v2 NoIR                                  |1     |$15.00        |$15.00        |Paired with 680nm bandpass filter for NDVI           |https://www.pishop.us/product/raspberry-pi-noir-camera-module-v2/?src=raspberrypi|
|Power                            |XT90 Male-Female Pairs                             |1     |$3.00         |$3.00         |Battery-to-frame power connectors                    |https://tinyurl.com/m3hn7ykb                                                     |
|Power Protection                 |50V 2200µF Low-ESR Electrolytic Capacitor          |1     |$3.00         |$3.00         |Across ESC battery pads — 6S voltage spike protection|https://tinyurl.com/yksjk3cu                                                     |
|Logistics                        |Shipping                                           |1     |$35.00        |$35.00        |Combined shipping across vendors                     |                                                                                 |
|                                 |                                                   |      |Total         |$146.31       |                                                     | 


Assembly

Build order, roughly in this sequence:

Frame — Cut the four CF tubes to 500mm. Press heat-set inserts into the 3D printed motor mount clamps, bolt clamps onto the tube ends. Assemble the central hub, routing motor and GPS/telemetry wiring through it before closing it up. Leave the FC/ESC deck plate off for now.
Propulsion — Bolt on the motors with threadlocker on every screw. Hold off on props until after ESC calibration. Two props are CW, two are CCW, check rotation direction against the SpeedyBee's motor order before mounting.

Power wiring — Solder the XT60 to the main 12 AWG battery leads, then wire the 4-in-1 ESC to the same leads. Solder the 2200uF capacitor across the ESC's battery pads for spike protection. Run 18 AWG phase wire from each motor through the arm tubes to its ESC output. Wire the two UBECs off the main power lead, one to the FC, one to the Pi, kept separate.
Flight controller — Mount the SpeedyBee F405 V4 stack on its vibration grommets near the frame's center of mass. Mount the GPS/compass on a mast, away from the ESC. Wire the SiK telemetry radio to a UART. Bind and wire the FlySky receiver to iBus.

Flash and configure INAV — Flash INAV to the SpeedyBee. Set the mixer to quad X, calibrate accelerometer and compass, confirm GPS lock, run ESC calibration with props off, set RC failsafe to RTL. Only mount props after confirming motor direction and throttle response in the motor test tab.

Payload — Confirm the IR-cut filter is removed from the NoIR camera, then thread on the 680nm bandpass filter. Connect the camera to the Pi Zero 2W via the CSI adapter. Mount the Pi and camera on the passive gimbal, mount the gimbal to the frame's underside. Power the Pi off its own UBEC rail.

Telemetry link and trigger logic — Wire a UART from the flight controller to the Pi so it can read the MAVLink stream. Run the waypoint-reached listener script from UAV Code/ on the Pi, which fires the camera and geotags on trigger. Bench-test this indoors before flying.

Balance and pre-flight check — Confirm the aircraft balances near center with the battery installed, arms are square, and motors spin freely. Run a full pre-flight (GPS lock, compass, RC link, telemetry link) and a hover test before attempting a waypoint mission.

Ground station — Install WebODM (Docker install is easiest). After a flight, pull images off the Pi's SD card, load them into a WebODM project, and run the orthomosaic and NDVI task. Output is viewable in WebODM or exportable as a GeoTIFF.|


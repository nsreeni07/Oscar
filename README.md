# Oscar
Autonomous UAV system that performs precision crop monitoring through systematic aerial imaging and vegetation index mapping across agricultural fields. The drone executes pre-programmed waypoint missions via INAV autopilot, with an onboard Raspberry Pi Zero 2W capturing geotagged near-infrared imagery using a NoIR camera and 680nm bandpass filter at each waypoint. After the mission is completed, images are transferred to a ground station running WebODM, which stitches frames into orthomosaic maps and calculated NDVI values to produce color-coded field health maps showing crop health, irrigation stress, and potential disease pressure. 

Onshape Link:https://cad.onshape.com/documents/19523291b70a9c787e4fbec5/w/8af018b0ace6f9250dc6f3df/e/06f56f02d452d38e7c73aa30?renderMode=0&uiState=6a4018b7d9e7363edd5feb0e

<img width="960" height="786" alt="Screenshot 2026-05-12 180331" src="https://github.com/user-attachments/assets/5cb71a60-cdf0-4a29-b372-2b2cad4f5c3e" />

<img width="1345" height="641" alt="Screenshot 2026-05-06 182000" src="https://github.com/user-attachments/assets/735606a8-7236-477b-a397-c1ffcca2f356" />


<img width="1110" height="785" alt="Screenshot 2026-05-12 113512" src="https://github.com/user-attachments/assets/066d5c06-10ed-4771-af28-48e4128f38d5" />


# Project OSCAR — Bill of Materials

> Custom 850mm endurance agricultural mapping quadcopter
|                                 |FIELD2                                             |FIELD3|FIELD4        |FIELD5        |FIELD6                                               |FIELD7                                                                           |
|---------------------------------|---------------------------------------------------|------|--------------|--------------|-----------------------------------------------------|---------------------------------------------------------------------------------|
|                                 |                                                   |      |              |              |                                                     |                                                                                 |
|Category                         |Item                                               |Qty   |Unit Price ($)|Line Total ($)|Notes                                                |Link                                                                             |
|Flight Controller / ESC          |SpeedyBee F405 V4 BLS 60A 30x30 FC + 60A 4-in-1 ESC|1     |$70.31        |$70.31        |FC + ESC stack, replaces F722 + separate PDB/PM06    |https://tinyurl.com/2nz8ucyx                                                     |
|Companion Computer               |Raspberry Pi Zero 2W                               |1     |$20.00        |$20.00        |Runs NDVI pipeline + MAVLink telemetry               |https://www.adafruit.com/piz2w?src=raspberrypi                                   |
|Camera                           |Pi Camera v2 NoIR                                  |1     |$15.00        |$15.00        |Paired with 680nm bandpass filter for NDVI           |https://www.pishop.us/product/raspberry-pi-noir-camera-module-v2/?src=raspberrypi|
|Power                            |XT90 Male-Female Pairs                             |1     |$3.00         |$3.00         |Battery-to-frame power connectors                    |https://tinyurl.com/m3hn7ykb                                                     |
|Power Protection                 |50V 2200µF Low-ESR Electrolytic Capacitor          |1     |$3.00         |$3.00         |Across ESC battery pads — 6S voltage spike protection|https://tinyurl.com/yksjk3cu                                                     |
|Logistics                        |Shipping                                           |1     |$35.00        |$35.00        |Combined shipping across vendors                     |                                                                                 |
|                                 |                                                   |      |Total         |$146.31       |                                                     |                                                                                 |

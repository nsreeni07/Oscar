---
title: "OSCAR - Autonomous NDVI Agricultural Mapping Drone"
author: "nsreeni07"
description: "An 850mm quadcopter designed for autonomous NDVI agricultural mapping using a Raspberry Pi Zero 2W imaging payload and custom carbon fiber frame."
created_at: "2026-04-05"
---

# April 5: Project Research and Initial BOM

Started the project by reviewing my original UAV plan and identifying gaps. I then researched alternative flight controllers to replace the Pixhawk (too expensive), explored GPS module options, and settled on the battery and power system i will be using. I also learned about the importance of correct wire gauges for safety, Started building the BOM, though there is still a lot left to finalize.

![Initial BOM Draft](https://github.com/user-attachments/assets/d4b93ad4-46d0-4e08-bc00-0bdf3df08ad6)

**Total time spent: 2 hours**

---

# April 6: System Architecture and Component Research

Researched components through forums and videos to finalize what I need to buy. Defined the core concept: use an onboard IR camera to map large areas of land (primary focus: crops) and generate NDVI maps that identify vegetation health, drought, and stress. I then created a system architecture diagram showing how all components connect. Built out initial BOM using AliExpress for lowest cost; current estimate around $200.

![System Architecture Diagram](https://github.com/user-attachments/assets/a303c29b-844c-457d-b84b-d02380fd948a)

**Total time spent: 2 hours**

---

# April 7: NDVI Processing Algorithm

So today I developed the NDVI vegetation index processing algorithm using RGB image data. Since hardware hasn't arrived yet, used sample stock images to simulate drone-captured data. Implemented an NDVI approximation formula (since the NoIR camera mixes IR and red channels rather than isolating them), tested different normalization methods, and debugged division errors and inconsistent results from lighting variation. Ran stock images through the pipeline and got solid outputs. Also started planning a batch processing pipeline for when the drone captures hundreds of images.

![NDVI Algorithm Output 1](https://github.com/user-attachments/assets/79d60ad9-ce0d-47ef-8f27-6c86d2082e5a)
![NDVI Algorithm Output 2](https://github.com/user-attachments/assets/95bf73d7-a267-418b-ab90-0520952bf940)

**Total time spent: 3 hours**

---

# April 8: Waypoint-Based Photo Capture Code and MAVLink Integration

Scrapped the original time-based photo capture approach (every 2 seconds), which was too unreliable because of speed variation, crosswind, and GPS drift that would happen irl. Replaced it with a waypoint-based capture system using the Haversine Formula to calculate distance between GPS coordinates. The system stores the last capture position and triggers a new photo once the drone has traveled past a set threshold (EX: 5 meters). Wrote the MAVLink communication layer to wait for a heartbeat signal and continuously read GPS data from the M8N module. Next step is integrating the actual camera module and finishing the image stitching pipeline.

![Waypoint Capture Code](https://github.com/user-attachments/assets/f7b2ef0f-a559-4ca8-b185-fcaea7e3d3bb)

**Total time spent: 2 hours**

---

# April 10: Wiring Diagram, BOM Update, and Camera Mount Design

Created a full wiring diagram in draw.io. Switched flight controller from the F722 to the Speedybee F405 V4 stack, which includes a PDB and 4-in-1 ESC, saving money and simplifying the build. Updated the BOM to reflect the new FC and adjusted prices. Added female bullet sockets and heat shrink for soldering motor wires to the FC. Also started thinking through the camera mount; considered a stabilizing gimbal with ball bearings for keeping the camera level during flight but holding off due to cost.

![Wiring Diagram](https://github.com/user-attachments/assets/2a9a5807-04a3-43b5-9779-68fb527b2e9d)

**Total time spent: 3 hours**

---

# April 11: MAVLink Integration and Camera Mount CAD

Worked through the MAVLink integration between the Raspberry Pi and flight controller in VS Code. This is the communication layer that lets the Pi read GPS coordinates, battery voltage, and flight mode in real time, enabling geotagging and distance-based photo capture. When the Pi arrives, will need to configure hardware UART at 115200 baud and set up pymavlink for message parsing.

Also completed the camera mount CAD. Simplified the design from a full gimbal to a fixed camera holder to cut costs. Added M3 screw holders and plan to mount it to the frame with foam padding to dampen motor vibrations. 

![Camera Mount CAD](https://github.com/user-attachments/assets/c3a6ab61-be63-43b8-b35f-f9648f0ea21a)

**Total time spent: 2 hours**

---

# April 13: Project Feedback and Redesign

Received feedback and identified major issues with the current plan: tier was too high and most of the project was just purchasing parts with little original engineering. Decided to do a full refresh:
1. Design a custom frame from scratch
2. Explore building a custom flight computer (TBD)
3. Find more ways to reduce cost

Ran new thrust calculations and created an updated project doc outlining the new direction: [Updated Project Doc](https://docs.google.com/document/d/19ZpP3lER7y1khA4oXiPfYRFo_DdoW_JR/edit)

![OSCAR Project Dossier](https://github.com/user-attachments/assets/c5a4f012-6ee1-46ba-878b-94f3364b50e4)

**Total time spent: 1 hour**

---

# April 20: Custom Frame Design and Sponsorship Outreach

Started designing the custom 850mm drone frame. Researched existing frames for reference, drew a sketch, then modeled the bottom plate in Onshape. Top plate design coming next but progress is slow due to exams. I also decided to use clamps with M3 nylon bolts to secure the motor arms.

On the funding side: total build cost at this scale is high. Plan is to cover ~$100 out of pocket and pursue ~$200 from Stasis and ~$200 from outside sponsors. Created a sponsor outreach list and will start emailing.

![Frame Bottom Plate CAD](https://github.com/user-attachments/assets/139ad086-0a11-44e1-8b2a-872981db6df5)

**Total time spent: 4 hours**

---

# April 26: CAD Model Revamp and Updated Dossier

Completed the final CAD revamp, almost done with the full drone model(hopefully?). Still need to merge the motor mounts from a separate file into the main assembly. Also created an updated project dossier with revised thrust calculations and cleaner formatting. Planning to run frame simulations in Fusion soon.

![Full CAD Model](https://github.com/user-attachments/assets/28d806ec-79f9-47fb-9391-9f5ed72f6bb4)

**Total time spent: 2 hours**

---

# May 5: Final CAD and Budget Finalized

Finalized the complete CAD model, adding motor mounts and double-checking the full assembly. Total project cost came in at approximately $650. Paying $550 out of pocket; hoping Stasis contributes $100.

![Final CAD Assembly](https://github.com/user-attachments/assets/45a92108-5968-4068-9fa5-442831c34047)

**Total time spent: 2 hours**

---

# May 7: CAD Fixes and Pitch Refresh

Did some small but important updates today, I went back into the CAD and edited the holes to 4.85mm to get a better fit for the hardware. I also refreshed my pitch and cleaned it up a bit, feels a lot more solid now. Nothing too crazy today just tying up loose ends.

![CAD Holes Update](https://github.com/user-attachments/assets/fb9de81c-1055-4581-8474-67c4b4913022)

**Total time spent: 0.4 hour**

---

# June 6: Flight Controller Switch and Capacitor

Did some BOM updates today, I switched the flight controller from the F722 to the Speedybee F405 V4 stack, it comes with a PDB and 4-in-1 ESC built in which saves me some money and I can cut the PMO6 V2 Power module and makes the build cleaner. I also added a capacitor to the BOM to help with voltage spikes from the motors, pretty important for protecting the ESC long term.

![Speedybee F405 V4](https://github.com/user-attachments/assets/69a6a3ad-3552-4748-913d-b0f2b7915441)

**Total time spent: 1 hour**

---
title: "OSCAR - Autonomous NDVI Agricultural Mapping Drone"
author: "nsreeni07"
description: "An 850mm quadcopter designed for autonomous NDVI agricultural mapping using a Raspberry Pi Zero 2W imaging payload and custom carbon fiber frame."
created_at: "2026-04-05"
---

# April 5: Project Research and Initial BOM

The Pixhawk I originally planned to use would have taken up most of my budget, so I started looking into other options. I also realized I hadn't put much thought into the power system yet. I spent a few hours reading RCGroups forums and build logs while comparing F4, F7, and H7 flight controllers. The biggest things I looked at were processing power, price, and how well they worked with INAV. Since my drone needs autonomous waypoint navigation for mapping, INAV compatibility was a requirement. I narrowed my choices down to the F4 and F405 controllers after comparing features like the number of UARTs, built-in barometers, and current sensing.

For the power system, I decided to use a 4S LiPo battery because it's the standard choice for this type of drone and offers a good balance between voltage, weight, and capacity. I also researched the correct wire gauge for the main power connections between the battery, ESC, and motors. Based on several reference tables, I confirmed that 14 AWG wire is the minimum I should use for the main power leads. Using wire that's too small can cause it to overheat, which is a serious safety concern during flight.

I also started putting together a bill of materials in a spreadsheet using prices from AliExpress. The list isn't complete yet since I still need to choose a GPS module, frame, and camera, but having everything organized makes it much easier to keep track of my budget. Right now, the biggest expenses are the flight controller and power system, so I'm planning to use an F4-based controller and a 4S LiPo battery to keep the project affordable while still meeting the performance requirements.

![Initial BOM Draft](https://github.com/user-attachments/assets/d4b93ad4-46d0-4e08-bc00-0bdf3df08ad6)

**Total time spent: 2 hours**

---

# April 6: System Architecture and Component Research
The main goal of OSCAR is to fly pre-programmed waypoint missions over farmland while capturing geotagged images at regular intervals. After the flight, those images will be stitched together into orthomosaics and processed into NDVI heat maps that highlight crop health, drought stress, and other problem areas. For the imaging system, I'm using a Raspberry Pi Zero 2W with a NoIR camera and a 680nm bandpass filter. The filter blocks most visible light while allowing the wavelengths needed for NDVI imaging to pass through. Since the NoIR camera is sensitive to near-infrared light, this setup gives me a much lower-cost alternative to an actual multispectral camera.

I also put together a complete system architecture diagram to better understand how everything connects. I split the project into four main subsystems. The first is the flight platform, which includes the frame, motors, ESCs, flight controller, GPS, and battery. The second is the imaging payload, made up of the Raspberry Pi Zero 2W, NoIR camera, bandpass filter, and onboard SD card storage. The third is the communication layer, where MAVLink runs over UART between the Pi and the flight controller so the Pi can access GPS coordinates, flight mode, and battery data in real time. The last subsystem is the ground station, where INAV Configurator is used for mission planning and WebODM processes the images after the flight. While putting the diagram together, I realized the Raspberry Pi has to wait for a MAVLink heartbeat from the flight controller before it can start reading GPS data. That means the startup sequence will be an important part of the software.

I also kept working on my bill of materials using AliExpress prices. Right now the estimated cost is about $200, not including the frame and a few smaller hardware items. I'll need to find ways to reduce costs in other parts of the project so I can stay within my budget.

![System Architecture Diagram](https://github.com/user-attachments/assets/a303c29b-844c-457d-b84b-d02380fd948a)

**Total time spent: 2 hours**

---

# April 7: NDVI Processing Algorithm
Since the hardware still hasn't arrived, I decided to focus on the software side of the project. My goal was to have the entire NDVI image processing pipeline working before I started collecting actual drone images, so I could begin testing as soon as the hardware was ready.

The standard NDVI formula is (NIR - Red) / (NIR + Red), which produces values between -1 and 1. Healthy vegetation usually falls somewhere between 0.2 and 0.8. Because I'm using a NoIR camera with a 680nm bandpass filter, I can't capture perfectly separate NIR and red channels like a true multispectral camera. Instead, I developed an approximation that uses the camera's red and blue channels as substitutes for the red and NIR values. It won't be as accurate as professional equipment, but it should still provide useful NDVI maps while keeping the overall project cost much lower.

The first few test results were inconsistent. Some images produced good NDVI maps, while others looked completely washed out or had inverted colors. After debugging the code, I found two main problems. The first was division-by-zero errors when both channels had values close to zero in dark or shadowed areas, which I fixed by adding a small epsilon value to the denominator. The second issue was that changing lighting conditions affected the channel ratios, so I added per-image normalization to make the results more consistent. I also started planning the batch processing pipeline for handling hundreds of images after each flight: load the image, extract the color channels, calculate NDVI, normalize the output, save the colorized image, and then send it to the geotagging stage. I tested the pipeline using stock aerial crop images, and the results were encouraging. Healthy vegetation appeared green while stressed areas showed up in the expected yellow and red regions.

![NDVI Algorithm Output 1](https://github.com/user-attachments/assets/79d60ad9-ce0d-47ef-8f27-6c86d2082e5a)
![NDVI Algorithm Output 2](https://github.com/user-attachments/assets/95bf73d7-a267-418b-ab90-0520952bf940)

**Total time spent: 3 hours**

---

# April 8: Waypoint-Based Photo Capture Code and MAVLink Integration

I made a major change today to how the drone captures photos, and I think it'll make a big difference in the quality of the final NDVI maps.

My original plan was to take a picture every two seconds, but after thinking it through I realized that wasn't the best approach. During a real flight, the drone's speed can easily vary by around 30% because of wind and throttle changes. That would make the image overlap inconsistent, which would make stitching the images together much harder. Instead, I switched to a distance-based capture system using the Haversine formula, which calculates the distance between two GPS coordinates while accounting for the Earth's curvature. Every time the drone takes a photo, it saves that GPS location as the last capture point. As new GPS data comes in, the software continuously calculates the distance from that point. Once the drone has traveled more than the set threshold, currently 5 meters, it captures another image and updates the last capture position. This should keep the image spacing consistent regardless of how fast the drone is flying.

I also finished writing the MAVLink communication module using pymavlink. When the Raspberry Pi starts up, it first waits for a heartbeat from the flight controller before doing anything else. This makes sure the flight controller is fully initialized and has a GPS lock before the Pi begins reading flight data. Once the heartbeat is received, the program continuously reads GLOBAL_POSITION_INT messages and feeds the GPS coordinates directly into the distance-based photo capture system.


![Waypoint Capture Code](https://github.com/user-attachments/assets/f7b2ef0f-a559-4ca8-b185-fcaea7e3d3bb)
![Waypoint Capture Code](https://github.com/user-attachments/assets/f7b2ef0f-a559-4ca8-b185-fcaea7e3d3bb)

**Total time spent: 2 hours**

---

# April 10: Wiring Diagram, BOM Update, and Camera Mount Design

Today I completed a full wiring diagram in draw.io showing how every major component connects. This includes the battery to the PDB, the PDB to each ESC with the correct motor directions for an X configuration, the ESCs to the motors, the flight controller to the GPS and receiver, and the UART connection between the flight controller and the Raspberry Pi. I also marked where female bullet connectors and heat shrink tubing will be used throughout the build. Having everything planned out ahead of time should make assembly much smoother and help me avoid mistakes once I start soldering.

I also spent some time designing the camera mount. At first I wanted to build a two-axis stabilized gimbal with ball bearings to keep the camera level during turns and reduce motion blur. After looking into the parts and cost, though, I realized it would push the project well over my budget. Instead, I decided on a fixed 3D-printed mount that securely holds the Raspberry Pi and camera while attaching to the frame with foam padding to reduce vibrations from the motors. Since this drone will be flying relatively slowly with only shallow bank angles during mapping missions, I think the fixed mount will provide good enough image quality. I still plan to model a gimbal later in case I decide to upgrade the design in the future.


![Wiring Diagram](https://github.com/user-attachments/assets/2a9a5807-04a3-43b5-9779-68fb527b2e9d)

**Total time spent: 3 hours**

---

# April 11: MAVLink Integration and Camera Mount CAD

I continued working on the MAVLink communication code in VS Code. At this point, the communication layer can detect heartbeats with timeout protection so the Raspberry Pi doesn't get stuck waiting if the flight controller is powered off. It also continuously reads GLOBAL_POSITION_INT messages to get the drone's latitude, longitude, and altitude, monitors battery voltage using SYS_STATUS messages, and logs raw MAVLink messages for debugging. I also wrote down the full hardware setup process as a checklist, including enabling UART, setting the baud rate to 115200, and configuring pymavlink to use /dev/ttyAMA0. Having everything documented now should save time when I start integrating the hardware later.

I also finished the camera mount CAD model in Onshape. The final design is a two-piece enclosure with a base plate that bolts directly to the bottom of the drone frame and a top cover that securely holds the Raspberry Pi Zero 2W and NoIR camera module in place. I added integrated M3 standoffs for mounting the PCB, and the camera opening includes a small retaining lip to hold the 680 nm bandpass filter above the lens. The entire assembly attaches to the frame using four M3 bolts with vibration-damping foam grommets. It's a much cheaper alternative to a stabilized gimbal and should work well for the slow, steady flight paths OSCAR will use during agricultural mapping.


![Camera Mount CAD](https://github.com/user-attachments/assets/c3a6ab61-be63-43b8-b35f-f9648f0ea21a)

**Total time spent: 2 hours**

---

# April 13: Project Feedback and Redesign

I received some important feedback today that made me rethink the direction of the project. The main concern was that the engineering challenge wasn't as strong as it could be since most of the work involved selecting and assembling commercially available parts rather than designing original components.

After thinking about it, I agreed with the feedback and decided to redesign the project while keeping the main goal the same. OSCAR will still be an autonomous drone for NDVI agricultural mapping, but I'll be doing much more of the engineering myself. Instead of buying a pre-made frame, I'm going to design a custom 850 mm carbon fiber frame from scratch. I'm also considering designing a custom flight computer in the future if time allows, while continuing to look for ways to reduce the overall cost of the build.

I also reran my thrust calculations to make sure my motor and propeller combination can safely lift the fully assembled drone. I compared the expected thrust against the estimated all-up weight, including the frame, motors, flight controller stack, battery, imaging payload, and all of the hardware. I used a minimum thrust-to-weight ratio of 2:1, while aiming for closer to 3:1 to provide enough performance and stability for reliable flight.

[Updated Project Doc](https://docs.google.com/document/d/19ZpP3lER7y1khA4oXiPfYRFo_DdoW_JR/edit)

![OSCAR Project Dossier](https://github.com/user-attachments/assets/c5a4f012-6ee1-46ba-878b-94f3364b50e4)

**Total time spent: 1 hour**

---

# April 20: Custom Frame Design and Sponsorship Outreach

I started designing the custom 850 mm drone frame today. Before creating any CAD models, I spent some time studying existing 800 to 900 mm quadcopter frames to understand common design practices, including motor-to-motor spacing, plate thickness, and different ways of attaching the arms. I noticed that most commercial frames use a clamped arm design where the arms slide between two center plates and are secured with bolts. This makes damaged arms easy to replace without rebuilding the entire frame.

After doing that research, I began modeling the bottom plate in Onshape. I positioned the mounting holes to match the F722 flight controller's standard 30 × 30 mm M3 mounting pattern and added slots for the battery straps. Progress has been a little slower than I expected since exams have limited me to working in short 30-minute sessions, but I'm still making steady progress whenever I have time.

I also took another look at my project budget and realized the total cost will be much higher than I can afford on my own. Right now, my plan is to contribute about $100 myself, apply for around $200 in funding from Stasis, and try to raise another $200 through outside sponsors. To get started, I created a list of potential sponsors and began drafting outreach emails to companies in the drone and precision agriculture industries.

![Frame Bottom Plate CAD](https://github.com/user-attachments/assets/139ad086-0a11-44e1-8b2a-872981db6df5)

**Total time spent: 4 hours**

---

# April 26: CAD Model Revamp and Updated Dossier

I spent some time today cleaning up my Onshape assembly because the older versions had parts spread across multiple files, and everything felt kind of disconnected. My main goal was to make sure the assembly itself was organized and that the mate relationships between the plates, arms, and other components all worked correctly. I still need to bring the motor mount over from a different file and merge it into the main assembly, but other than that, the overall geometry is pretty much where I want it to be.

Right now, the frame uses a 4 mm bottom plate, which is a little thicker than normal since I'm using 3D-printed PETG instead of stronger carbon fiber. It also has a 3 mm top plate and 15 × 15 mm square arm tubes. The motor mounts are 3D-printed PETG brackets with heat-set M3 inserts, so when the motors are bolted on, the screws thread into metal instead of plastic, which makes the mounting much more durable.


![Full CAD Model](https://github.com/user-attachments/assets/28d806ec-79f9-47fb-9391-9f5ed72f6bb4)

**Total time spent: 2 hours**

---

# May 5: Final CAD and Budget Finalized

Today I finished the full CAD model by adding the motor mounts and doing a final assembly check. I made sure the motor bolt patterns lined up with the mounts, the FC stack had enough clearance under the top plate, the camera mount had a clear downward view, the battery was centered over the center of gravity, and all of the wire routing paths were accessible. There are still a few areas where I'll have to rely on careful cable management to keep the wiring neat since the frame doesn't include dedicated wire channels. That's definitely something I'd like to improve in a future revision.

The total cost of the project ended up being about $650. I'm paying around $550 myself and hoping Stasis can help cover the remaining $100. The biggest expenses were the motors, props, and ESC stack at about $80, the FC stack at $45, the battery at $40, the imaging payload at $35, the GPS at $12, the frame materials and hardware at around $60, 3D printing filament and fabrication at about $30, and another $20 for wire, connectors, and fasteners. The final cost was higher than I originally expected, mostly because the custom frame and the full imaging payload added more to the budget than I had planned.


![Final CAD Assembly](https://github.com/user-attachments/assets/45a92108-5968-4068-9fa5-442831c34047)

**Total time spent: 2 hours**

---

# May 7: CAD Fixes and Pitch Refresh

Today I updated the motor mount design by changing the hole size for the heat-set inserts. The standard approach with PETG is to make the hole slightly undersized so the insert melts its way into the plastic under heat and pressure. As the plastic cools, it hardens around the knurled insert and creates a much stronger fit. Based on recommendations from the Prusa forums, I'm using about a 0.15 mm undersized hole. That means changing the hole diameter to 4.85 mm instead of the 5.0 mm version I had before, which would have been too loose and wouldn't have held the inserts as securely.

I also spent some time revising my project pitch. I tightened up the overall wording and made the main problem statement more focused by emphasizing the price gap between professional NDVI drones and what a small farm or a high school student can realistically afford. I think the revised version does a better job of explaining why this project matters.


![CAD Holes Update](https://github.com/user-attachments/assets/fb9de81c-1055-4581-8474-67c4b4913022)

**Total time spent: 0.4 hour**

---

# June 6: Flight Controller Switch and Capacitor

Today I finalized my decision to switch from the F722 flight controller to the SpeedyBee F405 V4 stack, which includes both the flight controller and a 4-in-1 60A BLS ESC. I decided to go with this setup because it's more affordable than buying an F722 and a separate ESC. Another advantage is that the flight controller and ESC connect internally, so there isn't any soldering required between them. The stack also has built-in current sensing, which means I no longer need the PM06 V2 power module. On top of that, it's fully compatible with my existing FlySky i6 transmitter and FS-iA6B receiver using the iBUS protocol, so I don't have to spend money on a new radio system. The ESC is rated for 60A per motor, which gives me plenty of headroom since my motors are only expected to draw about 25 to 30A at full throttle.

I also added a 50V 2200 µF low-ESR electrolytic capacitor to the bill of materials. When the motors speed up or slow down quickly, they can create voltage spikes on the power rail because of the sudden change in current. Without a capacitor to absorb those spikes, the voltage could exceed what the ESC can safely handle, potentially causing brownouts or even permanent damage. The capacitor will be mounted as close as possible to the ESC power input so it can do its job effectively. I chose a Panasonic FR or FC series capacitor because their low ESR makes them much better at reducing high-frequency voltage spikes than standard capacitors. The 50V rating also provides plenty of safety margin above the maximum voltage of my 4S battery, which is about 16.8V.

![Speedybee F405 V4](https://github.com/user-attachments/assets/69a6a3ad-3552-4748-913d-b0f2b7915441)

**Total time spent: 1 hour**

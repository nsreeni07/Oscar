---
title: "OSCAR - Autonomous NDVI Agricultural Mapping Drone"
author: "nsreeni07"
description: "An 850mm quadcopter designed for autonomous NDVI agricultural mapping using a Raspberry Pi Zero 2W imaging payload and custom carbon fiber frame."
created_at: "2026-04-05"
---

# April 5: Project Research and Initial BOM

Initially, I was planning to use the Pixhawk flight controller, however, its cost was very high, hence I had to start comparing flight controllers F4, F7, and H7 with respect to performance, cost and INAV compatibility. Autonomous waypoint navigation being an important part of this project, I further reduced the choices of controllers to F4 and F405 through comparison of characteristics such as UARTs, internal barometers and current sensors. The chosen batteries will be 4S LiPo and 14 AWG will be the minimum wire size required for power lines. In order to keep track of my budget, I started making a bill of materials, where the cost of each item is from AliExpress, thus the most expensive items have been identified to be flight controller and power system.

![Initial BOM Draft](https://github.com/user-attachments/assets/d4b93ad4-46d0-4e08-bc00-0bdf3df08ad6)

**Total time spent: 2 hours**

---

# April 6: System Architecture and Component Research

Today I was busy with system architecture design of OSCAR. The drone will fly according to predefined waypoints, capturing geotagged images that can be later stitched into orthomosaics and turned into NDVI maps for identifying crop health and stress. I decided to use Raspberry Pi Zero 2W with NoIR camera and 680 nm bandpass filter as a cheaper replacement for the multispectral camera. Also, I made a diagram of the system architecture, where the project is divided into four major parts – flight platform, imaging payload, communications and ground station. In the course of my work, I discovered that Raspberry Pi has to wait for the MAVLink heartbeat before it starts receiving data from GPS module, which will become an essential part of the software initialization process. Besides, I have updated my bill of materials; the total cost is currently about $200 without the frame and a few other elements.

![System Architecture Diagram](https://github.com/user-attachments/assets/a303c29b-844c-457d-b84b-d02380fd948a)

**Total time spent: 2 hours**

---

# April 7: NDVI Processing Algorithm

As the hardware had not yet arrived, my attention was paid to software pipeline development for NDVI image processing to have everything ready before flight testing. As no multispectral data could be gathered from a NoIR camera with a 680 nm bandpass filter, an approximate NDVI algorithm using red and blue channels as substitutes for the red and near-infrared bands was created. In order to avoid a division by zero error, I added epsilon to the denominator and adjusted for the variable lighting conditions using per-image normalization. Additionally, a batch-processing workflow was developed in order to automate calculations of NDVI, normalization, coloring, and geotagging preparation of hundreds of images per flight. The initial testing with aerial images of crops gave promising results with healthy vegetation depicted in green and stressed areas marked in yellow and red colors.

![NDVI Algorithm Output 1](https://github.com/user-attachments/assets/79d60ad9-ce0d-47ef-8f27-6c86d2082e5a)
![NDVI Algorithm Output 2](https://github.com/user-attachments/assets/95bf73d7-a267-418b-ab90-0520952bf940)

**Total time spent: 3 hours**

---

# April 8: Waypoint-Based Photo Capture Code and MAVLink Integration

This is where I have been able to make a huge upgrade to the image capture system of the drone because instead of the previous time-based system, I used the distance-based system that employs the use of the Haversine formula. While the time-based system was capturing photos every two seconds, the new system calculates the distance moved since the last capture point based on the GPS coordinate and captures an image every 5 meters. This is irrespective of the change in the speed of the flight. I have been able to develop the MAVLink communication system using pymavlink that captures GLOBAL_POSITION_INT message when a heart beat from the flight controller is obtained.

![Waypoint Capture Code](https://github.com/user-attachments/assets/f7b2ef0f-a559-4ca8-b185-fcaea7e3d3bb)
![Waypoint Capture Code](https://github.com/user-attachments/assets/f7b2ef0f-a559-4ca8-b185-fcaea7e3d3bb)

**Total time spent: 2 hours**

---

# April 10: Wiring Diagram, BOM Update, and Camera Mount Design
I have finished drawing up the wiring diagram which demonstrates connections between each of the main components such as the battery, power distribution board, ESCs, motors, flight controller, GPS, receiver and Raspberry Pi, and I noted the points where the bullet connectors and heat shrink tubing will be placed in order to make it easier to assemble the components without errors in wiring. Also, I have finished designing the camera mount, and decided to use a stationary one instead of the gimbal due to its extra cost and difficulty of assembly.


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

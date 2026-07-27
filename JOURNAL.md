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

The next step in my MAVLink communication system within VS Code was to add the ability to detect heartbeats along with a timeout mechanism, read GPS information constantly from `GLOBAL_POSITION_INT`, read battery voltage from `SYS_STATUS`, and log raw messages for troubleshooting purposes. In addition, I created documentation for the whole hardware set-up, including UART configuration, baud rate setting at 115200, and `pymavlink` connection parameters. Furthermore, I finished the design for the Onshape CAD model for the camera mount, which includes a two-piece housing that features M3 stand-offs for mounting, 680 nm filter retaining lips, and vibration damping foam mounts. The fixed mount is a cheaper solution than the gimbal but sufficient enough for slow agricultural mapping flights by OSCAR.


![Camera Mount CAD](https://github.com/user-attachments/assets/c3a6ab61-be63-43b8-b35f-f9648f0ea21a)

**Total time spent: 2 hours**

---

# April 13: Project Feedback and Redesign

From the feedback I got, the project should be made to have a more engineering approach since most of the work in the original design had been based on buying and assembling commercially available parts. Having considered the comments, I have resolved to modify my design of OSCAR such that the target will still remain autonomous NDVI agricultural mapping. In the revised design, there will be need to design an 850 mm carbon fiber drone chassis from scratch and maybe develop a custom flight controller at some point in the future. The design of the propulsion system will entail recomputation of the thrust to weight ratio for the full drone weight, which will include chassis, motors, electronics, batteries, and the imaging payload.

[Updated Project Doc](https://docs.google.com/document/d/19ZpP3lER7y1khA4oXiPfYRFo_DdoW_JR/edit)

![OSCAR Project Dossier](https://github.com/user-attachments/assets/c5a4f012-6ee1-46ba-878b-94f3364b50e4)

**Total time spent: 1 hour**

---

# April 20: Custom Frame Design and Sponsorship Outreach

I began designing the custom 850 mm drone frame by researching existing large quadcopter designs to understand common structural approaches, including motor spacing, plate thickness, and replaceable arm configurations. Based on this research, I started modeling the bottom plate in Onshape with a 30 × 30 mm M3 mounting pattern for the F722 flight controller and integrated battery strap slots. Progress has been slower due to limited time during exams, but I have continued making steady improvements. I also reevaluated the project budget and created a funding plan involving $100 of personal contribution, approximately $200 from Stasis funding, and another $200 through external sponsors. To support this, I began compiling a list of potential sponsors and drafting outreach emails to companies in the drone and precision agriculture industries.


![Frame Bottom Plate CAD](https://github.com/user-attachments/assets/139ad086-0a11-44e1-8b2a-872981db6df5)

**Total time spent: 4 hours**

---

# April 26: CAD Model Revamp and Updated Dossier

My primary concern was to make the organization of my Onshape assembly by bringing together all the previous files, which had been separated and also correcting all the mates of the plates, arms, and all other components. The basic geometry of the whole frame is almost done except for the motor mount, which I need to bring in from another file. In my current design, I have used a 4 mm bottom plate, a 3 mm top plate, and 15 × 15 mm square arm tubes. As I am going to use 3D printed PETG in place of carbon fiber in my prototype, I have made the plate thicker for extra support.

![Full CAD Model](https://github.com/user-attachments/assets/28d806ec-79f9-47fb-9391-9f5ed72f6bb4)

**Total time spent: 2 hours**

---

# May 5: Final CAD and Budget Finalized

The model design is now complete and involves assembling the model and checking the fitment of all parts including the mounting of the motors. It is now verified that all the bolt arrangements in the motors fit well, the flight controller stack has enough space, the camera mount provides a clear view downwards, the battery position is close to the CG point and the wire routing is still possible. Although the design works well, there is room for future improvement through the provision of dedicated cable routing space inside the frame. The cost of this project is around $650 where most of the money will be spent on the motors, propellers, and ESC stack, flight controller stack, battery, imaging payload, GPS, frame, 3D printing and other miscellaneous hardware. The main reason for high cost is the special frame design and added components for the imaging payload.

![Final CAD Assembly](https://github.com/user-attachments/assets/45a92108-5968-4068-9fa5-442831c34047)

**Total time spent: 2 hours**

---

# May 7: CAD Fixes and Pitch Refresh
In today's session, I worked on designing the motor mounts where I modified the size of heat set insert holes to allow for a better fit into PETG material. To do this, I reduced the hole size from 5.0 mm to 4.85 mm which is 0.15 mm undersized. This allows the heat set insert to embed itself into the plastic when it melts. In addition to this, I also worked on modifying my project pitch to make the problem more apparent. In particular, I worked on the cost aspect of having professional NDVI mapping drones for small farms and students.

![CAD Holes Update](https://github.com/user-attachments/assets/fb9de81c-1055-4581-8474-67c4b4913022)

**Total time spent: 0.4 hour**

---

# June 6: Flight Controller Switch and Capacitor
Nowadays, I have successfully replaced the F722 flight controller with the SpeedyBee F405 V4 stack, which consists of the flight controller and 60A 4-in-1 BLS ESC in one more compact and less expensive package. It lowers costs, gets rid of soldering needed between the FC and ESC, and makes it possible to forget about purchasing the Power Module 06 V2 because of the current measurement implemented in the stack. The stack still works with my old FlySky i6 transmitter and FS-iA6B receiver via iBUS, and the 60A ESC is quite enough for my motors, which are estimated to consume 25-30A at full throttle. Moreover, I decided to add a 50V 2200 µF low-ESR electrolytic capacitor to the system in order to save the power system from any possible voltage spikes related to the fast change of the current used by the motors.

![Speedybee F405 V4](https://github.com/user-attachments/assets/69a6a3ad-3552-4748-913d-b0f2b7915441)

**Total time spent: 1 hour**

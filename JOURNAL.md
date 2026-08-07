---
title: "OSCAR - Autonomous NDVI Agricultural Mapping Drone"
author: "nsreeni07"
description: "An 850mm quadcopter designed for autonomous NDVI agricultural mapping using a Raspberry Pi Zero 2W imaging payload and custom carbon fiber frame."
created_at: "2026-04-05"
---

# April 5: Project Research and Initial BOM

Initially, I was planning to use the Pixhawk flight controller, however, its cost was very high, hence I had to start comparing flight controllers F4, F7, and H7 with respect to performance, cost and INAV compatibility. Autonomous waypoint navigation being an important part of this project, I further reduced the choices of controllers to F4 and F405 through comparison of characteristics such as UARTs, internal barometers and current sensors. The chosen batteries will be 4S LiPo and 14 AWG wire size. In order to keep track of my budget.
![Initial BOM Draft](https://github.com/user-attachments/assets/d4b93ad4-46d0-4e08-bc00-0bdf3df08ad6)

**Total time spent: 2 hours**

---

# April 6: System Architecture and Component Research

Today I was busy with system architecture design of OSCAR. The drone will fly according to predefined waypoints, capturing geotagged images that can be later stitched into orthomosaics and turned into NDVI maps for identifying crop health and stress. I decided to use Raspberry Pi Zero 2W with NoIR camera and 680 nm bandpass filter. In the course of my work, I discovered that Raspberry Pi has to wait for the MAVLink heartbeat before it starts receiving data from GPS module, which will be a useful part of the software initialization process. Besides, I have updated my bill of materials the total cost is currently about $200 without the frame and a few other elements.

![System Architecture Diagram](https://github.com/user-attachments/assets/a303c29b-844c-457d-b84b-d02380fd948a)

**Total time spent: 2 hours**

---

# April 7: NDVI Processing Algorithm

As the hardware had not yet arrived, my attention was paid to software pipeline development for NDVI image processing to have everything ready before flight testing. because there is no multispectral data could be gathered from a NoIR camera with a 680 nm bandpass filter, an approximate NDVI algorithm using red and blue channels as substitutes for the red and near-infrared bands. Also in order to avoid a division by zero error, I added epsilon to the denominator and adjusted for the variable lighting conditions using per-image normalization.  The initial testing with "aerial images" of crops gave very good results

![NDVI Algorithm Output 1](https://github.com/user-attachments/assets/79d60ad9-ce0d-47ef-8f27-6c86d2082e5a)
![NDVI Algorithm Output 2](https://github.com/user-attachments/assets/95bf73d7-a267-418b-ab90-0520952bf940)

**Total time spent: 3 hours**

---

# April 8: Waypoint-Based Photo Capture Code and MAVLink Integration

This is where I have been able to make a huge upgrade to the image capture system of the drone because instead of the previous time-based system, I used the distance-based system that uses the Haversine formula. While the time-based system was capturing photos every two seconds, the new system calculates the distance moved since the last capture point based on the GPS coordinate and captures an image every 5 meters. This is irrespective of the change in the speed of the flight. I have been able to develop the MAVLink communication system using pymavlink that captures GLOBAL_POSITION_INT message when a heart beat from the flight controller is obtained.

![Waypoint Capture Code](https://github.com/user-attachments/assets/f7b2ef0f-a559-4ca8-b185-fcaea7e3d3bb)
![Waypoint Capture Code](https://github.com/user-attachments/assets/f7b2ef0f-a559-4ca8-b185-fcaea7e3d3bb)

**Total time spent: 2 hours**

---

# April 10: Wiring Diagram, BOM Update, and Camera Mount Design
I finished drawing up the wiring diagram which demonstrates connections between each of the main components such as the battery, power distribution board, ESCs, motors, flight controller, GPS, receiver and Raspberry Pi, and I noted the points where the bullet connectors and heat shrink tubing will be placed in order to make it easier to assemble the components without errors. Also, I finished designing the camera mount, and decided to use a stationary one instead of the gimbal due to extra cost.

![Wiring Diagram](https://github.com/user-attachments/assets/2a9a5807-04a3-43b5-9779-68fb527b2e9d)

**Total time spent: 3 hours**

---

# April 11: MAVLink Integration and Camera Mount CAD

The next step in my MAVLink communication system within VS Code was to add the ability to detect heartbeats along with a timeout mechanism, read GPS information constantly from `GLOBAL_POSITION_INT`, read battery voltage from `SYS_STATUS`, and log raw messages for troubleshooting purposes. In addition, I created documentation for the whole hardware set-up, including UART configuration, baud rate setting at 115200, and `pymavlink` connection parameters. I finished the design for the Onshape CAD model for the camera mount, which includes a two-piece housing that features M3 stand-offs for mounting, 680 nm filter retaining lips, and vibration damping foam mounts. The fixed mount is a cheaper solution than the gimbal but works for slow agricultural mapping flights.


![Camera Mount CAD](https://github.com/user-attachments/assets/c3a6ab61-be63-43b8-b35f-f9648f0ea21a)

**Total time spent: 2 hours**

---

# April 13: Project Feedback and Redesign

From the feedback I got, the project should be made to have a more engineering approach since most of the work in the original design had been based on buying and assembling. I modified my design of OSCAR so that the target will still remain autonomous NDVI agricultural mapping. In the new design, there will be a 850 mm carbon fiber drone frame from scratch and maybe develop a custom flight controller. 

[Updated Project Doc](https://docs.google.com/document/d/19ZpP3lER7y1khA4oXiPfYRFo_DdoW_JR/edit)

![OSCAR Project Dossier](https://github.com/user-attachments/assets/c5a4f012-6ee1-46ba-878b-94f3364b50e4)

**Total time spent: 1 hour**

---

# April 20: Custom Frame Design and Sponsorship Outreach

I began designing the custom 850 mm drone frame by researching existing large drone designs to understand common structural approaches, including motor spacing, plate thickness, and arm configurations. I then started modeling the bottom plate in Onshape with a 30 × 30 mm M3 mounting pattern for the F722 flight controller and integrated battery strap slots. I also rethought the project budget and created a funding plan where a $100 of personal contribution, and $200 from Stasis funding, and another $200 through external sponsors. I alsp began making a list of potential sponsors and drafting outreach emails to companies in the drone and precision agriculture industries.


![Frame Bottom Plate CAD](https://github.com/user-attachments/assets/139ad086-0a11-44e1-8b2a-872981db6df5)

**Total time spent: 4 hours**

---

# April 26: CAD Model Revamp and Updated Dossier

My main concern was to make the organization of my Onshape assembly by bringing together all the previous files, which had been separated and also correcting all the mates of the plates, arms, and all other components. The basic geometry of the whole frame is almost done except for the motor mount, which I need to bring in from another file. In my current design, I used a 4 mm bottom plate, a 3 mm top plate, and 15 × 15 mm square arm tubes. As I am going to use 3D printed PETG in place of carbon fiber in my prototype, I made the plate thicker for extra support.

![Full CAD Model](https://github.com/user-attachments/assets/28d806ec-79f9-47fb-9391-9f5ed72f6bb4)

**Total time spent: 2 hours**

---

# May 5: Final CAD and Budget Finalized

The design is all set, and the test fit looks great. Motor bolts line up, the flight controller stack fits fine, the camera has a clear view straight down, and the battery sits right on the center of gravity. Wiring works as-is, but adding dedicated internal cable channels in the future would definitely clean things up.

Total cost landed right around $650, mostly driven by the motors, props, stack, battery, and camera setup.

![Final CAD Assembly](https://github.com/user-attachments/assets/45a92108-5968-4068-9fa5-442831c34047)

**Total time spent: 2 hours**

---

# May 7: CAD Fixes and Pitch Refresh
I worked on designing the motor mounts where I modified the size of heat set insert holes to allow for a better fit into PETG material. I reduced the hole size from 5.0 mm to 4.85 mm which is 0.15 mm undersized. This allows the heat set insert to embed itself into the plastic when it melts. I also worked on modifying my project pitch to make the problem more apparent. I also worked on the cost aspect of having professional NDVI mapping drones for small farms and students.

![CAD Holes Update](https://github.com/user-attachments/assets/fb9de81c-1055-4581-8474-67c4b4913022)

**Total time spent: 0.4 hour**

---

# June 6: Flight Controller Switch and Capacitor
I replaced the F722 flight controller with the SpeedyBee F405 V4 stack, which has the flight controller and 60A 4-in-1 BLS ESC in one more compact and less expensive set. It lowers costs, gets rid of soldering needed between the FC and ESC. The stack still works with my old FlySky i6 transmitter and FS-iA6B receiver via iBUS, and the 60A ESC is quite enough for my motors, which are estimated to consume 25-30A at full throttle. I decided to add a 50V 2200 µF low-ESR electrolytic capacitor to the system in order to save the power system from any possible voltage spikes related to the fast change of the current used by the motors.

![Speedybee F405 V4](https://github.com/user-attachments/assets/69a6a3ad-3552-4748-913d-b0f2b7915441)

**Total time spent: 1 hour**

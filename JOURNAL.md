---
title: "OSCAR - Autonomous NDVI Agricultural Mapping Drone"
author: "nsreeni07"
description: "An 850mm quadcopter designed for autonomous NDVI agricultural mapping using a Raspberry Pi Zero 2W imaging payload and custom carbon fiber frame."
created_at: "2026-04-05"
---

# April 5: Project Research and Initial BOMStarted my project by reviewing my UAV idea and finding gaps in the plan.

The Pixhawk I had chosen would have cost most of my budget. I hadn't thought about the power system properly.I spent time looking into F4, F7 and H7 flight controllers on RCGroups and build logs.The main things to consider were processing power, cost and compatibility with INAV.INAV support was a must-have since I need to navigate through waypoints for mapping.I chse between F4 and F405 options. Compared how many UARTs they had, barometer integration and current sensing.
For the power system I decided on a LiPo battery.It's standard for this type of motor. Provides a good balance of voltage and capacity.I also checked the wire gauge requirements for the current connections between the battery, ESC and motors.I found some reference tables. Confirmed that I need at least 14AWG wire for the main power leads.If the wire is too small it can. Cause a fire during flight so this is a real safety concern.I started a list of parts in a spreadsheet. Pulled prices from AliExpress.It's not final yet. I still need to decide on a GPS, frame and camera.Having the list in place helps me track the cost and see where my budget is going.The Pixhawk and power system are parts of the cost and INAV compatibility is crucial, for my project I'm using F4-based options and a 4S LiPo battery to balance cost and performance.
![Initial BOM Draft](https://github.com/user-attachments/assets/d4b93ad4-46d0-4e08-bc00-0bdf3df08ad6)

**Total time spent: 2 hours**

---

# April 6: System Architecture and Component Research
The main idea is that OSCAR flies pre-programmed waypoint grids over farmland. It captures geotagged images at regular intervals and processes these images into orthomosaics and NDVI heat maps. These maps show crop stress, drought areas, and plant health. The imaging setup uses a Raspberry Pi Zero 2W with a NoIR camera and a 680nm bandpass filter. This filter blocks visible light except for red. The NoIR sensor’s sensitivity to near-infrared light allows me to get the NIR and red channels needed for NDVI at a much lower cost than a real multispectral camera.

I created a complete diagram of the system architecture, showing every component across four subsystems: (1) the flight platform made up of the frame, motors, ESCs, flight controller, GPS, and battery; (2) the imaging payload, which includes the Pi Zero 2W, NoIR camera, bandpass filter, and SD storage; (3) the communication layer, which uses MAVLink over UART to connect the Pi and the flight controller, giving the Pi access to real-time GPS coordinates, flight mode, and battery voltage; (4) the ground station, which uses INAV Configurator for mission planning and WebODM for processing images after the flight. Drawing this out showed me something important: the Pi needs a MAVLink heartbeat from the flight controller before it can read GPS data. This means that the startup sequence is crucial and must be handled in software.

I continued to build the bill of materials using AliExpress. The current estimate is around $200, not including the frame and some hardware. I will need to cut costs in other areas to stick to my budget.
![System Architecture Diagram](https://github.com/user-attachments/assets/a303c29b-844c-457d-b84b-d02380fd948a)

**Total time spent: 2 hours**

---

# April 7: NDVI Processing Algorithm
Hardware’s still on its way, so in the meantime I shifted over to getting the image processing pipeline working in software — I wanted my NDVI algorithm to be ready to drop right in the second I actually had some real drone images to feed it.

Standard NDVI is (NIR – Red) / (NIR + Red), yielding a value somewhere between -1 and +1, with healthy vegetation generally falling into the 0.2–0.8 range. Complicating the matter with our NoIR + 680nm filter setup is that it won’t give us clean NIR and Red channels because we capture a blend of the two — I used a rough approximation formula based on the camera’s red and blue channels as proxies for Red and NIR respectively. It’s nowhere near as accurate as a dedicated multispectral camera but should produce usable NDVI estimates at a fraction of the price.

Early outputs were hit or miss — some images came out just fine, while others produced blown-out or inverted NDVI maps. After debugging I traced it to two issues: (1) division-by-zero errors caused by both channels reading near zero in shadowed or black regions (fixed by adding a tiny epsilon term to the denominator); (2) lighting variation between images shifting the channel ratios (partially addressed with per-image normalization). Started sketching the batch processing pipeline for dealing with hundreds of post-flight images: load image → extract channels → compute NDVI → normalize → save colorized output → move to geotagger queue. Took stock aerial crop images through the pipeline and came out with great results, stressed areas showing up in the expected red/yellow range, healthy veggie in green.

![NDVI Algorithm Output 1](https://github.com/user-attachments/assets/79d60ad9-ce0d-47ef-8f27-6c86d2082e5a)
![NDVI Algorithm Output 2](https://github.com/user-attachments/assets/95bf73d7-a267-418b-ab90-0520952bf940)

**Total time spent: 3 hours**

---

# April 8: Waypoint-Based Photo Capture Code and MAVLink Integration

Made a fundamental change today to how photo capture is triggered that’ll have a huge impact on the quality of my final NDVI maps.

My original plan was a photo every 2 seconds but realised there’s some serious problems with that idea: speed variation in real flight conditions can be +/- 30% from planned, meaning image overlap would be all over the place depending on wind and throttle. Replaced it with a distance based system using the Haversine formula (calculates great-circle distance between two GPS coords accounting for Earth’s curvature). When a photo is taken, those coords are stored as the “last capture position”. On each GPS update it computes distance from that stored point to the current one. Once the threshold is exceeded (default: 5m) a new photo fires and the last capture position updates. Guarantees consistent ground sampling distance regardless of speed variation.

Also wrote the MAVLink communication module using pymavlink. The startup sequence waits for a heartbeat from the FC before doing anything (ensures the FC is fully booted and GPS has a lock before the Pi starts reading position data). After the heartbeat it enters a loop reading GLOBAL_POSITION_INT messages at high frequency, feeding directly into the Haversine capture logic.

![Waypoint Capture Code](https://github.com/user-attachments/assets/f7b2ef0f-a559-4ca8-b185-fcaea7e3d3bb)
![Waypoint Capture Code](https://github.com/user-attachments/assets/f7b2ef0f-a559-4ca8-b185-fcaea7e3d3bb)

**Total time spent: 2 hours**

---

# April 10: Wiring Diagram, BOM Update, and Camera Mount Design

Built a full wiring diagram in draw.io of everything  battery to PDB, PDB to ESCs (with correct spin directions for X configuration), ESCs to motors, FC to GPS, FC to receiver, UART from FC to RPi. Also mapped where I need female bullet connectors on motor wires and where heat shrink goes. Having that done means I can sell efficiently without second guessing things mid build.

Started thinking through the camera mount. My first instinct was a 2-axis stabilizing gimbal with ball bearings to keep the camera level during banked turns and reduce motion blur, after priceing out the hardware it was way too expensive given my budget. Settled on a fixed mount instead, a 3d printed enclosure holding the Pi and camera rigidly, mounted to the frame with foam padding to absorb motor vibration. At the low speeds/shallow bank angles this drone will fly for agricultural mapping, the fixed mount should be good enough But I'll model that just in case I change my mind.

![Wiring Diagram](https://github.com/user-attachments/assets/2a9a5807-04a3-43b5-9779-68fb527b2e9d)

**Total time spent: 3 hours**

---

# April 11: MAVLink Integration and Camera Mount CAD

Continued the MAVLink work in VS Code. My comm layer can now handle: heartbeat detection (with timeout logic so the Pi doesn’t hang if the FC is off), continuous polling of GLOBAL_POSITION_INT for lat/lon/alt, SYS_STATUS reads for battery voltage monitoring, and raw MAVLink message logging for debugging. Documented the full hardware setup as a checklist  enable UART, set 115200 baud, configure pymavlink to /dev/ttyAMA0 so I don’t have to re-derive it at integration time.

Also, completed the camera mount CAD in Onshape. Final design is a two-piece enclosure: a base plate that bolts to the bottom of the drone frame, and a top cover that sandwiches the Pi Zero 2W and camera module. M3 screw posts are integrated for PCB standoffs. The lens aperture is sized for the NoIR camera with a small retaining ledge to hold the 680nm bandpass filter in place above the lens. The assembly mounts to the frame via four M3 bolts through vibration-damping foam grommets — the budget alternative to a gimbal, appropriate for the slow, stable flight profiles OSCAR will fly.

![Camera Mount CAD](https://github.com/user-attachments/assets/c3a6ab61-be63-43b8-b35f-f9648f0ea21a)

**Total time spent: 2 hours**

---

# April 13: Project Feedback and Redesign
Received feedback today that forced a significant rethink of the project. The main critique was that the project tier was too high compared to the actual original engineering involved (most of the work was purchasing/assembling commercial parts, with limited custom design)

Agreed with the feedback and decided to do a full refresh. The core NDVI mapping mission stays the same but the engineering approach changes: design a custom 850mm carbon fiber frame from scratch vs. buying off-the-shelf, maybe even explore building a custom flight computer, and find additional cost savings. Ran new thrust calculations to validate that my motor + propeller selection can actually lift the drone with full payload (used 2:1 thrust-to-weight min, 3:1 preferred) against calculated all-up weight including frame, motors, FC stack, battery, payload, and fasteners
[Updated Project Doc](https://docs.google.com/document/d/19ZpP3lER7y1khA4oXiPfYRFo_DdoW_JR/edit)

![OSCAR Project Dossier](https://github.com/user-attachments/assets/c5a4f012-6ee1-46ba-878b-94f3364b50e4)

**Total time spent: 1 hour**

---

# April 20: Custom Frame Design and Sponsorship Outreach
Started designing the custom 850mm frame. Before modeling anything I studied existing 800-900mm quad frames to get a sense of standard geometry (motor-to-motor diagonal), plate thickness conventions, and arm attachment methods. Most commercial frames use a “clamped” arm design where arms slide into center plates and are compressed by bolts – simple/replaceable if an arm breaks mid flight. I then started modeling the bottom plate in Onshape, positioning FC stack mounting holes to match the F722’s 30x30mm M3 pattern, adding battery strap slots. Progress is a bit slower than I’d like due to exams getting me maybe 30minutes at a time.

Total build cost is going to be way more than I could hope to cover alone. Plan is to pay ~$100 out of pocket, pursue ~$200 from Stasis, and ~$200 from outside sponsors. I created a sponsor outreach list and started drafting emails to companies in the drone and precision agriculture space.
![Frame Bottom Plate CAD](https://github.com/user-attachments/assets/139ad086-0a11-44e1-8b2a-872981db6df5)

**Total time spent: 4 hours**

---

# April 26: CAD Model Revamp and Updated Dossier

Did a big revamp of my Onshape assembly. Earlier versions had parts scattered across different files and they just didn’t really go together as well today I was mostly trying to make sure the main assembly itself made sense with good mate relationships between the plates, arms, etc. I still have to merge the motor mount  from another file into the main assembly, but otherwise the geometry is pretty much correct at this point. My frame uses a 4mm bottom plate (thicker than normal to compensate for having 3D-printer PETG instead of nice strong carbon fiber) 3mm top plate and 15x15mm square arm tubes. The motor mounts are 3D-printed PETG brackets with heat-set M3 inserts so when you bolt the motors down, your screws thread into metal and not plastic.

Also finally got around to rewriting the whole project dossier in a much nicer format and fixing up my thrust estimates now that I know the all-up weight.

![Full CAD Model](https://github.com/user-attachments/assets/28d806ec-79f9-47fb-9391-9f5ed72f6bb4)

**Total time spent: 2 hours**

---

# May 5: Final CAD and Budget Finalized

Finalized the complete CAD model adding motor mounts and running a full assembly check: motor bolt patterns match mount geometry, FC stack clears the top plate, camera mount has unobstructed downward view, battery sits centered over CG, and all wire routing paths are accessible. There are a few spots where I’m relying on cable management during the build to route wires cleanly — the frame doesn’t have dedicated wire channels, something I’d add in a revision.

Total project cost came in at about $650. Paying $550 out of pocket; hoping Stasis chips in $100. Cost breakdown roughly: motors + props + ESC stack (~$80), FC stack ($45), battery ($40), imaging payload ($35), GPS ($12), frame materials/hardware (~$60), 3D printing filament/fabrication (~$30), misc. wire, connectors, and fasteners (~$20). Higher than early estimates largely because the custom frame and full imaging payload add up faster than expected.

![Final CAD Assembly](https://github.com/user-attachments/assets/45a92108-5968-4068-9fa5-442831c34047)

**Total time spent: 2 hours**

---

# May 7: CAD Fixes and Pitch Refresh
Went back into the CAD and updated the M3 heat-set insert holes to 4.85mm diameter.

Standard practice for heat-set inserts in PETG is to size the hole slightly undersized the insert melts its way in under heat and pressure, creating a tight interference fit as plastic resolidifies around the knurling. I’m targeting ~0.15mm undersize based on Prusa forum guidance. The 4.85mm spec replaces an earlier 5.0mm hole that would’ve been too loose and produced a weak pull-out strength.

Also refreshed and tightened the project pitch. Main changes: sharpened the problem statement around the cost gap between professional NDVI drones and what a small farm or high school student can actually afford.

![CAD Holes Update](https://github.com/user-attachments/assets/fb9de81c-1055-4581-8474-67c4b4913022)

**Total time spent: 0.4 hour**

---

# June 6: Flight Controller Switch and Capacitor

Confirmed the switch from the F722 to the SpeedyBee F405 V4 stack (FC + 4-in-1 60A BLS ESC). Key reasons: it’s cheaper than a standalone F722 + separate ESC, the stack handles FC-to-ESC power/signal connections internally with no soldering between them, the built-in current sensing eliminates the PM06 V2 power module, and my existing FlySky i6 transmitter + FS-iA6B receiver over iBUS are directly compatible so I don’t need to buy a new radio system. The 60A per-motor rating has comfortable headroom my motors draw around 25-30A at full throttle.

Also added a 50V 2200µF low-ESR electrolytic capacitor to the BOM. When motors throttle up/down quickly, the sudden current change creates voltage spikes on the power rail. Without a bulk capacitor to absorb these, spikes can exceed the ESC’s voltage tolerance and cause brownouts/permanent damage. The cap sits as close to the ESC power input as possible—specced a Panasonic FR or FC series part specifically for their low ESR, higher ESR caps are less effective at damping high-frequency transients. At 50V rating it has comfortable headroom above the 4S battery’s max of ~16.8V.

![Speedybee F405 V4](https://github.com/user-attachments/assets/69a6a3ad-3552-4748-913d-b0f2b7915441)

**Total time spent: 1 hour**

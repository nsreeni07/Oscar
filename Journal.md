4/11
MAVLink Communication
The main work was getting the MAVLink figured out between the rasberry pi and the flight controller. MAVLink is what lets the pi talk to the computer. It's how the Pi will read GPS coordinates, battery voltage, and flight mode in real time during a survey. This is what enable geotagging and distance vases capture. I worked through the full integration in VS code. When I get the Pi I will have configure the hardware UART, on of the UART port need to be configured to output MAVLink at 115200 baud. Then pymavlink handles the message parsing in python. There is a lot more to do with the Pi but that will be when it arrives.

The second thing I worked on today was the CAD model for the camera mount. I decided to change the design up to just a camera holder because the codt is really high for the barings and everything so I decided to make it just a camera holder.

<img width="1204" height="676" alt="Screenshot 2026-04-11 210928" src="https://github.com/user-attachments/assets/c3a6ab61-be63-43b8-b35f-f9648f0ea21a" />

I added some M3 screw holders, and I'm planning to atttach the screw to the frame with foam in the middle to remove vibrations from the motor. 

4/10
Wiring diagram,Cad Model, Code Revision
So today I worked on this wiring diagram, I used draw.io, to create my wiring diagram it was a simple diagram adn didnt take too long I also updated my BOM, I previously was planning pn running a F722 flight controller but after some reasearch and asking friend who had experience in drones they said that the Speedybee F405 V4 would be abetter choice the stack version I'm buying comes with a PDB and it has a 4 in 1 esc which means I can save some money. But because of this I ahd to add some female bullet sockets to solder the motor wires to the flight computer. I also hadded some heat shrink for this and fixed up some of my BOM prices which had changed.
<img width="938" height="619" alt="Screenshot 2026-04-11 210911" src="https://github.com/user-attachments/assets/2a9a5807-04a3-43b5-9779-68fb527b2e9d" />



I also worked on my camera holder, for the NVDI I need the photo to be taken level with the ground with around 5-10 degreed allowed so I thought about making a stabilizing camera mount with ball bearings but I'm still thinking about wheter or not because its kinda expensive to buy everything, I might scratch it but we will have to see.


4/8
Waypoint Photo Capture Code
So today I worked on the code for the photo capture system, to accurately create a big map of farmland i need to take multiple smaller photos, my orignal plan was to create a time-based code that takes photos every 2 seconds, i quickly realized that this doesnt accoutn for many real world diffrences such as diffrence speed, crosswind, and slight deviation. These added up could give an glitchy or messed up final picture so I decided on a diffrent approach. Instead of time Im going to use a waypoint based capture code, Which takes photo based on GPS coordinates. I used the Haversine Formula to calculate the distance between 2 points, I then worked on the camera capture logic, the program stored the last gps position and compares it to the current position if the calcualted distance is greater than a set distance(Ex:5 Meters), the system takes a photo, Im later going to replace this with the camera but this is just the basic logic.


<img width="1530" height="1041" alt="Screenshot 2026-04-08 184641" src="https://github.com/user-attachments/assets/f7b2ef0f-a559-4ca8-b185-fcaea7e3d3bb" />

I then wrote the actual Mavlink communication into the code that is going to be used on the drone, I wrote a code that waits for the "heartbeat" signal for communication, and constantly reads the gps data from the M8N module, It then uses the same logic and formulas to take photos. I'm going to keep working today and maybe finish the code for image stiching pipeline that creates the full image

4/7
NDVI
I worked on developing the NDVI (vegetation index) processing algorithm using RGB image data. Since I don’t have any of the hardware yet, I used sample images from online to simulate drone-captured data. I added the NDVI approximation formula and tested different normalization methods to improve visibility. A lot of time went into debugging issues like random division errors and inconsistent results due to lighting differences. This helped a lot in understanding how image processing will work once the drone is operational and how this is probably going to be the longest part of this entire project

<img width="1098" height="923" alt="Screenshot 2026-04-08 192909" src="https://github.com/user-attachments/assets/0ffbac3f-6835-4856-a7c0-ed64fa7035b4" />

I then took some stock images from the web and ran it through this code and got some pretty decent outputs, im also working on a pipleline for when I get 100s of images from the drone in real life. How this entire thing works is the NoIR camera captures infrared but cannot isolate it from the red channel(the red light and infared are mixed together kinda), so I implemented an NDVI approximation instead of true NDVI and with this the forumula((NIR - Red) / (NIR + Red)) is applied to every pixel in the image to generate a new dataset representing vegetation health. So for the first part of the project its going to be just a basic proof of concept and I'm plannign to buy my own cheap real Infared camera to actually see this work in the future even though infared is CRAZY expensive (cheapest is $400)

<img width="673" height="388" alt="Screenshot 2026-04-07 192434" src="https://github.com/user-attachments/assets/79d60ad9-ce0d-47ef-8f27-6c86d2082e5a" />

<img width="1282" height="708" alt="Screenshot 2026-04-07 192440" src="https://github.com/user-attachments/assets/95bf73d7-a267-418b-ab90-0520952bf940" />

4/6
So I looked through a bunch of forums and watched some videos to get an idea of what I need to buy, I also planned out the structure for my drone The whole idea for my drone is to use the onboard IR camera to map huge amounts of land ideally crops, but can also be used for Pastures(Tracking animals), or flying over highways and monitoring car speeds, but for now the agricultural side is what I am focusing on. With that data I can create a Normalized Diffrence vegetation index (NDVI). These maps help identify healthy vegetation, stress, drought, or barren areas, with NDVI. I also made a system architecture diagram that shows how everything will be.

<img width="679" height="734" alt="Screenshot 2026-04-06 140014" src="https://github.com/user-attachments/assets/a303c29b-844c-457d-b84b-d02380fd948a" />

All of my part in my current BOM are from aliexpress because its the cheapest, there are other parts that I have to buy myself, are mostly from amazon, my final is coming out to $200, My future plan for this project is to create my own custom frame and make my own custom software but for now I gotta finish this. I'm going to keep coding today and finish off the code and then journal that.

4/5
Today was mostly just reasearching and figuring out my UAV project. I started by going though my orignal plan I previously had and saw a lot of gaps and decided to do some reasearch to fix those haps, I spen time looking into diffrent components and one big change I made was to with a cheaper flight controller instaead of the pixhawk I orignally intended on using because its a little to expensive. I als reasearched GPS modules and found more ways i could optimize costs. I also figured out my battery adn power system. I learned battery choice is a big part and I also realized that using the wrong wire gauges can be pretty dangerous. I started working on my BOM but I still got a lot to finish.

<img width="341" height="280" alt="Screenshot 2026-04-05 222717" src="https://github.com/user-attachments/assets/d4b93ad4-46d0-4e08-bc00-0bdf3df08ad6" />

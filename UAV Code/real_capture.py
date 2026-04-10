from pymavlink import mavutil
import math
import time

# Distance calculation (meters)
def get_distance(lat1, lon1, lat2, lon2):
    R = 6371000

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)

    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    return R * c

# Connect to flight controller
print("Connecting to flight controller...")
master = mavutil.mavlink_connection('COM3', baud=115200)

# Wait for heartbeat
master.wait_heartbeat()
print("Connected!")

last_position = None
capture_distance = 5  # meters

while True:
    msg = master.recv_match(type='GLOBAL_POSITION_INT', blocking=True)

    if msg is not None:
        lat = msg.lat / 1e7
        lon = msg.lon / 1e7
        alt = msg.alt / 1000

        print(f"GPS: {lat}, {lon}, Alt: {alt}")

        if last_position is not None:
            dist = get_distance(last_position[0], last_position[1], lat, lon)
            print(f"Moved: {dist:.2f} meters")

            if dist > capture_distance:
                print(" TAKE PHOTO")

                # TODO: Replace with real camera trigger
                # Example:
                # capture_image()

                last_position = (lat, lon)
        else:
            last_position = (lat, lon)

     last_position = (lat, lon)

    time.sleep(0.1)

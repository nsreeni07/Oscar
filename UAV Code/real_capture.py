from pymavlink import mavutil
import math
import time

# -----------------------------
# SETTINGS
# -----------------------------
CAPTURE_DISTANCE = 5        # meters
MIN_CAPTURE_INTERVAL = 0.8  # seconds (GPS jitter guard)

# -----------------------------
# DISTANCE FUNCTION (Haversine)
# -----------------------------
def get_distance(lat1, lon1, lat2, lon2):
    R = 6371000
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

# -----------------------------
# CONNECT
# -----------------------------
print("Connecting to flight controller...")
master = mavutil.mavlink_connection('COM3', baud=115200)
master.wait_heartbeat()
print("Connected!")

last_position = None
last_capture_time = 0

# -----------------------------
# MAIN LOOP
# -----------------------------
while True:
    msg = master.recv_match(type='GLOBAL_POSITION_INT', blocking=True)

    if msg is not None:
        lat = msg.lat / 1e7
        lon = msg.lon / 1e7
        alt = msg.alt / 1000.0

        print(f"GPS: {lat:.6f}, {lon:.6f}  Alt: {alt:.1f}m")

        if last_position is not None:
            dist = get_distance(last_position[0], last_position[1], lat, lon)
            now = time.time()
            print(f"Moved: {dist:.2f}m")

            if dist >= CAPTURE_DISTANCE and (now - last_capture_time) >= MIN_CAPTURE_INTERVAL:
                print("TAKE PHOTO")
                # TODO: Replace with real camera trigger
                # capture_image()
                last_capture_time = now

        # Always update — not just on capture
        last_position = (lat, lon)

    time.sleep(0.1)

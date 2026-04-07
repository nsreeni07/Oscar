"""
config.py — All UAV companion settings in one place.
Edit this file to tune behaviour without touching core logic.
"""

import os
from dataclasses import dataclass, field
from pathlib import Path

BASE_DIR = Path(__file__).parent


@dataclass
class Config:
    # ── MAVLink / Serial ─────────────────────────────────────────────────────
    # Pi Zero 2W hardware UART after disabling Bluetooth
    MAVLINK_PORT: str        = "/dev/serial0"
    MAVLINK_BAUD: int        = 115200
    MAVLINK_TIMEOUT: float   = 3.0          # Seconds before connection error
    HEARTBEAT_INTERVAL: float = 1.0         # How often Pi sends heartbeat to FC
    FC_SYSTEM_ID: int        = 1            # ArduPilot default system ID
    FC_COMPONENT_ID: int     = 1

    # ── Camera ───────────────────────────────────────────────────────────────
    CAMERA_RESOLUTION: tuple = (3280, 2464)  # Full Pi Camera v2 NoIR resolution
    CAMERA_FRAMERATE: int    = 15            # fps during survey (lower = better quality)
    IMAGE_FORMAT: str        = "jpeg"        # "jpeg" or "png"
    JPEG_QUALITY: int        = 95            # 1–100
    IMAGE_DIR: Path          = Path("/home/pi/survey_images")

    # Trigger mode
    TRIGGER_MODE: str        = "mavlink"     # "mavlink" | "distance" | "time"
    TRIGGER_DISTANCE_M: float = 10.0         # Capture every N meters (distance mode)
    TRIGGER_INTERVAL_S: float = 2.0          # Capture every N seconds (time mode)

    # ── GPS / Geotagging ─────────────────────────────────────────────────────
    GEOTAG_EXIF: bool        = True          # Write GPS EXIF to JPEG files
    GPS_LOG_FILE: Path       = Path("/home/pi/survey_images/gps_log.csv")
    MIN_GPS_SATS: int        = 8             # Minimum satellites for valid geotag
    GPS_HDOP_MAX: float      = 2.0           # Max HDOP (lower = better accuracy)

    # ── Health monitoring ─────────────────────────────────────────────────────
    BATTERY_WARN_VOLTAGE: float = 14.4       # 3.6V/cell on 4S — log warning
    BATTERY_CRIT_VOLTAGE: float = 14.0       # 3.5V/cell — log critical
    DISK_WARN_PERCENT: int   = 85            # Warn when disk >85% full
    TEMP_WARN_C: float       = 75.0          # Pi Zero 2W throttles at ~80°C

    # ── Paths ────────────────────────────────────────────────────────────────
    LOG_DIR: Path            = Path("/var/log/uav")

    def __post_init__(self):
        self.IMAGE_DIR.mkdir(parents=True, exist_ok=True)
        self.LOG_DIR.mkdir(parents=True, exist_ok=True)

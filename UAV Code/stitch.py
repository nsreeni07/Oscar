import cv2
import os
import sys
import math

# -----------------------------
# SETTINGS
# -----------------------------
IMAGE_FOLDER = "captured_images"   # Folder of drone images
OUTPUT_FILE  = "stitched_output.jpg"
MAX_IMAGES   = 50                  # Cap per stitch pass (RAM safety)
RESIZE_WIDTH = 1920                # Downscale before stitching (faster, less RAM)

# -----------------------------
# LOAD IMAGES
# Sorted by filename = sorted by capture order (our filenames include count + timestamp)
# -----------------------------
def load_images(folder, max_count=MAX_IMAGES):
    supported = (".jpg", ".jpeg", ".png")
    files = sorted([
        f for f in os.listdir(folder)
        if f.lower().endswith(supported)
    ])

    if not files:
        print(f"No images found in '{folder}'")
        sys.exit(1)

    if len(files) > max_count:
        print(f"Found {len(files)} images — capping at {max_count} for RAM safety.")
        print(f"For full mosaics, run in batches or use WebODM.")
        files = files[:max_count]

    images = []
    for fname in files:
        path = os.path.join(folder, fname)
        img = cv2.imread(path)
        if img is None:
            print(f"  Warning: could not read {fname}, skipping")
            continue

        # Downscale to RESIZE_WIDTH to keep RAM usage reasonable
        h, w = img.shape[:2]
        if w > RESIZE_WIDTH:
            scale = RESIZE_WIDTH / w
            img = cv2.resize(img, (RESIZE_WIDTH, int(h * scale)))

        images.append(img)
        print(f"  Loaded: {fname} ({img.shape[1]}x{img.shape[0]})")

    return images

# -----------------------------
# STITCH
# -----------------------------
def stitch_images(images):
    print(f"\nAttempting to stitch {len(images)} images...")

    # SCANS mode is more robust for aerial/overlapping imagery than PANORAMA
    stitcher = cv2.Stitcher_create(cv2.Stitcher_SCANS)

    status, stitched = stitcher.stitch(images)

    if status == cv2.Stitcher_OK:
        cv2.imwrite(OUTPUT_FILE, stitched, [cv2.IMWRITE_JPEG_QUALITY, 95])
        h, w = stitched.shape[:2]
        size_mb = os.path.getsize(OUTPUT_FILE) / (1024 * 1024)
        print(f"\nStitching successful!")
        print(f"  Output: {OUTPUT_FILE}")
        print(f"  Size:   {w}x{h} pixels  ({size_mb:.1f} MB)")
        return True

    # Descriptive error codes
    errors = {
        cv2.Stitcher_ERR_NEED_MORE_IMGS:    "Not enough matching features between images. Try more overlap (fly slower / closer spacing).",
        cv2.Stitcher_ERR_HOMOGRAPHY_EST_FAIL: "Homography failed. Images may be too similar (low texture) or too far apart.",
        cv2.Stitcher_ERR_CAMERA_PARAMS_ADJUST_FAIL: "Camera parameter adjustment failed. Try fewer images or more overlap.",
    }
    reason = errors.get(status, f"Unknown error code {status}")
    print(f"\nStitching failed. {reason}")
    print("Stitching failed Brochacho lock in :(")
    return False

# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":
    # Optional: pass folder as argument
    if len(sys.argv) > 1:
        IMAGE_FOLDER = sys.argv[1]

    print(f"Loading images from: {IMAGE_FOLDER}")
    images = load_images(IMAGE_FOLDER)
    print(f"\nLoaded {len(images)} images successfully")

    success = stitch_images(images)

    if not success:
        print("\nTip: For 100+ drone images, use WebODM (free) for better results:")
        print("     https://webodm.net")

import cv2
import os

image_folder = "."
images = []

for filename in os.listdir(image_folder):
   if filename.endswith((".jpg", ".png")):
        img = cv2.imread(os.path.join(image_folder, filename))
        images.append(img)

print(f"Loaded {len(images)} images")

# Create stitcher
stitcher = cv2.Stitcher_create()

status, stitched = stitcher.stitch(images)

if status == cv2.Stitcher_OK:
    cv2.imwrite("stitched_output.jpg", stitched)
    print(" Stitching successful! Saved as stitched_output.jpg")
    cv2.imshow("Stitched Image", stitched)
    cv2.waitKey(0)
else:
    print(" Stitching failed Brochacho lock in :(")
    
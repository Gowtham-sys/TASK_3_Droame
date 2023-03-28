import cv2
import numpy as np

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 30, (512, 512))

# Draw a circle on the image and write each frame to the video
for i in range(900):  # 30 frames per second for 30 seconds
    cv2.circle(img,(256,256), 100, (0,0,255), -1)
    out.write(img)

# Release everything if job is finished
out.release()

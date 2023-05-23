#appeler les package:
import numpy as np
import cv2
import imutils
import os

folder_path = r"D:\dataset\Predict_Ground-truths"
output_folder = r"D:\dataset\Mask_processing"

# Iterate over all files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an image
    if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
        # Construct the full file path
        file_path = os.path.join(folder_path, filename)

        # Read the image using OpenCV
        img = cv2.imread(file_path)

        # Perform image processing steps
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.erode(thresh, None, iterations=2)
        thresh = cv2.dilate(thresh, None, iterations=2)

        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        # Check if any contours were found
        if cnts:
            # Find the contour with the maximum area
            c = max(cnts, key=cv2.contourArea)

            extLeft = tuple(c[c[:, :, 0].argmin()][0])
            extRight = tuple(c[c[:, :, 0].argmax()][0])
            extTop = tuple(c[c[:, :, 1].argmin()][0])
            extBot = tuple(c[c[:, :, 1].argmax()][0])

            ADD_PIXELS = 0

            new_img = img[extTop[1] - ADD_PIXELS:extBot[1] + ADD_PIXELS,
                      extLeft[0] - ADD_PIXELS:extRight[0] + ADD_PIXELS].copy()

            # Save the processed image to the output folder
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, new_img)
        else:
            print(f"No contours found in image: {filename}")
#
# # Folder path where the images are located
# folder_path = r"D:\dataset\Predict_crop_images2"
#
# # Output folder path
# output_folder = r"D:\dataset\image_proccecing"
#
# # Iterate over all files in the folder
# for filename in os.listdir(folder_path):
#     # Check if the file is a PNG image
#     if filename.endswith('.png'):
#         # Construct the full file path
#         file_path = os.path.join(folder_path, filename)
#
#         # Read the PNG image
#         img = cv2.imread(file_path)
#
#         # Convert the image to grayscale
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#         # Apply image thresholding to isolate the black background
#         _, thresh = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY_INV)
#
#         # Find contours of the foreground object
#         contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
#         # Find the largest contour
#         largest_contour = max(contours, key=cv2.contourArea)
#
#         # Get the bounding rectangle of the largest contour
#         x, y, w, h = cv2.boundingRect(largest_contour)
#
#         # Crop the image based on the bounding rectangle
#         cropped_img = img[y:y+h, x:x+w]
#
#         # Save the resulting cropped image with the black background removed
#         output_path = os.path.join(output_folder, filename)
#         cv2.imwrite(output_path, cropped_img)

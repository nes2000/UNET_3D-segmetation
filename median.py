import cv2
import numpy as np
import os

kernel1 = np.ones((3, 3), np.float32) / 9

for image in os.listdir("images"):
    try:
        #         result = cv2.filter2D(src=cv2.imread("images/"+image), ddepth=-1, kernel=kernel1)
        #         cv2.imwrite("new_moyenneur/"+image, result)
        result = cv2.medianBlur(src=cv2.imread("images/"+image), ksize=3)
        cv2.imwrite("new_median/"+image, result)
    except:
        pass

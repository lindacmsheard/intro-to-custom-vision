"""
Brief implementation of edge detection for image foreground extraction.

References:
- https://answers.opencv.org/question/30459/what-is-kernel/
- https://stackoverflow.com/questions/67275165/image-foreground-extraction-techniques-using-python

GrabCut article:
- https://python.engineering/python-foreground-extraction-in-an-image-using-grabcut-algorithm/
"""

import cv2
import numpy as np

def edge_detect(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Converts image to greyscale.
    img_canny = cv2.Canny(img_gray, 200, 215) #Finds edges in the input image and marks them in the output map edges using the Canny algorithm.
    kernel = np.ones((3, 3)) #Create a 3x3 array of 1s for the kernel.
    img_dilate = cv2.dilate(img_canny, kernel, iterations=20) #Dilates the source image using the specified structuring element that determines the shape of a pixel neighborhood.
    img_erode = cv2.erode(img_dilate, kernel, iterations=16) #Erodes the source image using the specified structuring element that determines the shape of a pixel neighborhood.
    return img_erode

img = cv2.imread("<path_to_image_here>")
contours, _ = cv2.findContours(edge_detect(img), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
imS = cv2.resize(img, (960, 540)) # Resize image
cv2.imshow("Image", imS) #Display the image
cv2.waitKey(0)
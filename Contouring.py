# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 15:29:46 2024

@author: Tipperary
"""

import cv2
import numpy as np
from Opening_images import image

def contour(img): 
    """
    Detects and draws contours on an image.

    Args:
        img (numpy.ndarray): Input image.

    Returns:
        tuple: A tuple containing the image with drawn contours and a list of detected contours.

    This function converts the input image to a binary image if necessary,
    finds contours using OpenCV's `cv2.findContours`, and draws the contours
    on the image. It returns both the image with contours and the detected contours.
    """
    if img.dtype == bool:
        img = img.astype(np.uint8) * 255
    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    if len(img.shape) == 2:  
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR) 
    img = cv2.drawContours(img, contours, -1, (0, 0, 255), 1)
    print('no. contours', len(contours))
    return img, contours

if __name__ == "__main__":
    #path =
    img = image(path)
    cv2.imshow('Original', img)
    
    img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) # The upper and lower intensity bounds should be adjusted accordingly.
    img, contours = contour(img)
    cv2.imshow('Contoured', img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()



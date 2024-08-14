# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 11:52:20 2024

@author: Tiffany
"""
import cv2
import numpy as np
from Opening_images import image 

def denoise(path, image_inserted = False, only_thresh = False, plot = True):
    """
    Denoises an image using adaptive thresholding and noise reduction.

    Args:
        path (str): Path to the image file or an image.
        image_inserted (bool, optional): Whether the input is a pre-loaded image. Defaults to False.
        only_thresh (bool, optional): If True, applies only thresholding. Defaults to False.

    Returns:
        numpy.ndarray: The denoised image as a NumPy array.
    """
    if image_inserted == False:
        img = image(path)
    else:
        img = path
        
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 6);
    if only_thresh == False:
        img = cv2.fastNlMeansDenoising(img, h = 40, templateWindowSize = 20, searchWindowSize = 21)
    
    img = img.astype(np.uint8) # May need this for the contouring function

    if plot == True:
        cv2.imshow('Denoised', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return img

if __name__ == "__main__":
    img = denoise(r"C:\Users\Tiffany\Downloads\COMPOS\Bubble Chamber Digital\bubble films (low res)\C1_7_web.png")

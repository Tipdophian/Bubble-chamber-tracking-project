# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 16:30:42 2024

@author: Tiffany
"""

import cv2
import numpy as np

def image(path, w = 1500, h = 800): 
    """
    Loads and preprocesses an image.

    Args:
        path (str): Path to the image file.
        w (int, optional): Maximum width for resizing. Defaults to 1500.
        h (int, optional): Maximum height for resizing. Defaults to 800.

    Returns:
        numpy.ndarray: Preprocessed image as a NumPy array.

    This function loads an image from the specified path, converts it to grayscale,
    and resizes it while maintaining aspect ratio. 
    """
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    height, width = img.shape
    max_width = w
    max_height = h
    if width > height:
      new_width = max_width
      new_height = int(height * (max_width / width))
    else:
      new_height = max_height
      new_width = int(width * (max_height / height))
    img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)
    img = img.astype(np.uint8)  

    if img is None:
        print(f"Could not read the image: {path}")
    return img

if __name__ == "__main__":
    path = r"C:\Users\Tiffany\Downloads\COMPOS\Bubble Chamber Digital\bubble films (low res)\C1_1_web.png"
    img = image(path)
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 16:30:42 2024

@author: Tiffany
"""

import cv2
import os
import numpy as np

def image(path): 
    """
    Loads and preprocesses an image.

    Args:
        path (str): Path to the image file.

    Returns:
        numpy.ndarray: Preprocessed image as a NumPy array.

    This function loads an image from the specified path, converts it to grayscale,
    and resizes it while maintaining aspect ratio. 
    """
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    height, width = img.shape
    max_width = 1500
    max_height = 800
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
    # View images in a folder of images
    img_folder = r"C:\Users\Tiffany\Downloads\COMPOS\Bubble Chamber Digital\bubble films (low res)"  
    img = os.listdir(img_folder)
    while True:
        try:
            choice = int(input(f"Enter the number of the image to open. There are {len(img)} images.(or 0 to quit): "))
            if 0 <= choice <= len(img):
                break
            else:
                print("Invalid choice. Please enter a number between 0 and", len(img))
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    if choice == 0:
        print("Exiting...")
    else:
        chosen_image_path = os.path.join(img_folder, img[choice - 1])
        img = image(chosen_image_path)
    
    cv2.imshow(f"Number {choice}", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


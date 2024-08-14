# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 15:41:05 2024

@author: Tiffany
"""
import cv2
import numpy as np
from Opening_images import image

def detect_crosses(image_path, template_path, w=15, h=15, threshold=0.69, margin=2, plot=False):
    """
    Detects fiducial marks (crosses) in an image using template matching.

    Args:
        image_path (str): Path to the input image.
        template_path (str): Path to the template image of a fiducial mark.
        w (int, optional): Width of the template. Defaults to 15.
        h (int, optional): Height of the template. Defaults to 15.
        threshold (float, optional): Matching threshold for template matching. Defaults to 0.69.
        margin (int, optional): Maximum distance between detected crosses to consider them duplicates. Defaults to 2.
        plot (bool, optional): If True, displays the image with detected crosses. Defaults to False.

    Returns:
        list: A list of detected cross coordinates (x, y).
    """
    img = image(image_path)
    temp = image(template_path, w, h)
    res = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    coord = []
    for i in range(len(loc[0])):
        y = loc[0][i]
        x = loc[1][i]
        coord.append([x, y])

    # Remove duplicate detections
    deleted_entries = 0
    for i in range(len(coord)):
        for j in range(i + 1, len(coord)):
            if abs(coord[i][0] - coord[j][0]) <= margin and abs(coord[i][1] - coord[j][1]) <= margin:
                coord[j] = (0, 0)
                deleted_entries += 1
    coord = [i for i in coord if i != (0, 0)]
    if plot:
        for pt in coord:
            cv2.rectangle(img, (pt[0], pt[1]), (pt[0] + w, pt[1] + h), (0, 0, 255), 1)
        cv2.imshow("Detected Crosses", img)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    return coord

if __name__ == "__main__":
    image_path = r"C:\Users\Tiffany\Downloads\COMPOS\Bubble Chamber Digital\bubble films (low res)\C1_8_web.png"
    template_path = r"C:\Users\Tiffany\Downloads\COMPOS\Bubble Chamber Digital\Crosses\Cross.png"
    w, h = 15, 15
    coords = detect_crosses(image_path, template_path, w, h, plot=True)


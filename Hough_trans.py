# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 12:26:35 2024

@author: Tiffany
"""
import cv2
import numpy as np
from Opening_images import image

def detect_lines(image_path, threshold_value=150, rho=1, theta=np.pi/180, threshold_line=50, min_line_length=100, max_line_gap=10):
    """
    Detects lines in an image using Hough Line Transform.

    Args:
        image_path (str): Path to the input image.
        threshold_value (int, optional): Threshold value for the binary threshold. Defaults to 150.
        rho (float, optional): Distance resolution in pixels. Defaults to 1.
        theta (float, optional): Angle resolution in radians. Defaults to np.pi/180.
        threshold_line (int, optional): Minimum number of votes (intersections in Hough space) to detect a line. Defaults to 50.
        min_line_length (int, optional): Minimum length of the detected line segments. Defaults to 100.
        max_line_gap (int, optional): Maximum allowed gap between line segments to be connected. Defaults to 10.

    Returns:
        numpy.ndarray: Image with detected lines.
    """

    img = image(image_path)
    _, img = cv2.threshold(img, threshold_value, 200, cv2.THRESH_TOZERO)

    lines = cv2.HoughLinesP(img, rho, theta, threshold_line, None, min_line_length, max_line_gap)

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 1, cv2.LINE_AA)

    return img, lines

if __name__ == "__main__":
    image_path = r"C:\Users\Tiffany\Downloads\COMPOS\Bubble Chamber Digital\bubble films (low res)\C1_5_web.png"
    img, lines = detect_lines(image_path)

    cv2.imshow('Lined Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

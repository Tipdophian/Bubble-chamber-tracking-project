# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:44:09 2024

@author: Tiffany
"""
import cv2
import numpy as np
from Opening_images import image
from Denoising import denoise
from Contouring import contour

path = r"C:\Users\Tiffany\Downloads\COMPOS\Bubble Chamber Digital\bubble films (low res)\C1_8_web.png"


# only threshold
imgde = denoise(path, False, True, plot = False) # Only adaptive threshold
# imgde = denoise(path, plot = False) # Adaptive threshold and denoised

# sobelX (detecting vertical edges using the thresholded image)

scale = 5
delta = 0
ksize = 1
ddepth = cv2.CV_8U
imgx = cv2.Sobel(imgde, ddepth, 1, 0, ksize=ksize, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
imgx = cv2.bitwise_not(imgx)
cv2.imshow('sobelX', imgx)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Subtract vertical from threshold
subtracted = cv2.bitwise_not(cv2.subtract(imgx, imgde)) # subtract the images 
subtracted = cv2.bitwise_not(cv2.subtract(imgx, subtracted))
cv2.imshow('subtracted', subtracted) 
cv2.waitKey(0)
cv2.destroyAllWindows()

# sobelY ( horizontal), add horizontal and subtracted
scale = 5
delta = 10
ksize = 1
imgy = cv2.Sobel(imgde, ddepth, 0, 1, ksize=ksize, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
imgy = cv2.bitwise_not(imgy)
cv2.imshow('sobelY', imgy)
cv2.waitKey(0)
cv2.destroyAllWindows()

# denoising added
added = cv2.add(subtracted, imgy)
cv2.imshow('added', added)
cv2.waitKey(0)
cv2.destroyAllWindows()


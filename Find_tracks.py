# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 17:39:06 2024

@author: Tiffany
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from Opening_images import image

def track_detect(filepath, col_range, intensity_dist = False):
    """
  Finding track coordinates by detecting peaks in pixel intensity within specified columns of an image.

  Args:
      filepath (str): Path to the image file.
      col_range (list): List of column indices to analyse.
      intensity_dist (bool, optional): Flag to show intensity distribution plots for each column index. Defaults to False.

  Returns:
      tuple: A tuple containing three elements:
          - pk (dict): A dictionary where keys are column indices and values are lists of peak coordinates (x, y).
    """
    img = image(filepath)
    margin = 30
    diff = 6 # Sensitivity to intensity difference
    peaks = []
    
    for col_i in col_range:
        col = 225 - img[margin : img.shape[0] - margin, col_i] # Make darker pixels peaks instead of troughs for easier spotting.
        
        # Detecting peaks in pixel intensity
        for i, n in enumerate(col):
            if i < len(col) - 1 and i != 0:
                if col[i] > col[i-1] and col[i] > col[i+1] and col[i] - col[i-1] > diff and col[i] - col[i+1] > diff and n != 0: 
                    peaks.append([col_i, i])
            elif i == len(col) - 1 and i !=0 :
                if col[i] > col[i-1] and col[i] - col[i-1] > diff and n != 0: 
                    peaks.append([col_i, i]) 
        x_axis = np.arange(margin, img.shape[0] - margin)  
        pk = {}
        for x, y in peaks:
          if x not in pk:
            pk[x] = []
          pk[x].append([x, y])
          
        # Show the (inverted) intensity distribution of pixels for each column (peaks represent darker pixels)
        if intensity_dist == True:
            plt.bar(x_axis, col, width = 1)
            plt.xlabel("Column index (y coordinate)")
            plt.ylabel("255 - intensity")
            plt.ylim(0, 225)
            for i in peaks: # For visualization of location of peaks.
                plt.axvline(i[1]+margin, color=(1, 0, 0)) 
            plt.title(f"Inverted pixel intensity of column {col_i}")
            plt.show()
    return pk
   
def track_fit(path, col, spread = 1, show_detected = False, show_fit = False):
    """
    Groups detected coordinates with similar y-coordinates into tracks and fits a polynomial model to them.
      
    Args:
        path (str): Path to the image file.
        col (list): List of column indices to analyze (reccomended to be within 260 - 1459, in the current scale). 
        spread (int, optional): Y-coordinate difference for considering peaks within a track. Defaults to 1.
        show_detected (bool, optional): Flag to display detected tracks on the image. Defaults to False.
        show_fit (bool, optional): Flag to display fitted tracks on the image. Defaults to False.
      
    Returns:
        list: A list of fitted track, each of which is a list of coordinates (x, y).
    """
    pk = track_detect(path, col)
    spread = 1
    first_col = list(pk.items())[0][1:][0]
    if first_col[-1][1] == 0:
        first_col = list(pk.items())[1][1:][0]
    if type(col) != list:
        col = list(col)
        
    # Convert column indices to indices in the list of detected columns
    detect_ind = []
    dec_i = np.arange(0, len(pk))
    col_map = {}
    for i in dec_i:
        if i < len(pk): 
            col_map[list(pk.items())[i][0]] = i
    
    for true_ind in col:
        if true_ind in col_map:
            detected_col_ind = col_map[true_ind]
            detect_ind.append(detected_col_ind)
        else:
            print('column with index', true_ind, 'is not among the detected columns')
            
    # Group pixels into tracks by select pixels in the each column that has minimal y-coordinate difference.
    tracks = []
    for pt in first_col:
        track_list = [pt]
        for i in detect_ind:
            next_col = list(pk.items())[i][1:][0]
            for next_pt in next_col:
                accept_pt = None
                min_diff = spread + 1
                diff = abs(next_pt[1] - pt[1])
                
                if diff <= spread and diff < min_diff: 
                    accept_pt = next_pt
                    min_diff = diff # The minimum difference found so far.
                elif accept_pt is not None and diff == min_diff and pt[1] < accept_pt[1]: # For pixels with equal difference, pick the higher pixel.
                    accept_pt = next_pt
                    
                if accept_pt: 
                    track_list.append(accept_pt)
                    pt = accept_pt
                
        if len(track_list) > 1:
            tracks.append(track_list)
    
    # Fitting a polynomial model to the track points
    fit_tracks = []
    for track in tracks:
        xlist = [] 
        ylist = []
        for i in track:
            xlist.append(i[0])
            ylist.append(i[1])
            
        degree = 2 # Fit with quadratic model.
        polyfit = np.polyfit(xlist, ylist, degree) 
        
        yfit = []  
        xfit = np.arange(min(xlist), max(xlist)+1) 
        for x in xfit:
            terms = []
            for index, coeff in enumerate(polyfit):
                terms.append(coeff * x**(degree - index))
            yfit.append(sum(terms))
        fit_tracks.append(list(zip(xfit, yfit)))
    
    # Plots tracks detected using intensity
    if show_detected == True:
        img = image(path)
        for track in tracks:
            for co in track:
                cv.circle(img, (co[0], co[1] + 30), radius=1, color=(0, 255, 0), thickness=-1)  
        
        cv.imshow(f"Columns {col[0]}-{col[-1]}, {len(tracks)} tracks detected", img)
        cv.waitKey(0)
        cv.destroyAllWindows()
        
    # Plots tracks fitted with polynomial model (using fit_images)
    if show_fit == True:
        img2 = image(path)  # Load image once outside the loop
        for fit_track in fit_tracks:
            xfit, yfit = zip(*fit_track)  # Unpack x and y coordinates
            for index in np.arange(0, len(xfit)):
                cv.circle(img2, (xfit[index], int(yfit[index]) + 30), radius=1, color=(0, 255, 0), thickness=-1)
    
        cv.imshow(f"Columns {col[0]}-{col[-1]}, {len(fit_tracks)} tracks fitted", img2)
        cv.waitKey(0)
        cv.destroyAllWindows()

if __name__ == "__main__":
    path = r"C:\Users\Tiffany\Downloads\COMPOS\Bubble Chamber Digital\bubble films (high res)\img_004.tif"
    fit_tracks = track_fit(path, range(260, 1459), show_fit = True) 
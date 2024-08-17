**Required packages**
1. Python 3.8.8
2. OpenCV 4.10.0
3. matplotlib 3.3.4
4. 'Opening_images'

**Algorithms and aims**
1. 'Opening_images' (required for other algorithms)
  - Takes an image file path and outputs a resized image.
    
2. 'Find_tracks'
  - Finds coordinates of points on tracks, groups them into tracks based on similar y-coordinates and applies a polynomial model to the tracks.
    
3. 'Temp_match'
  - Provides coordinates of the fiducial marks by matching them with a template image of the cross.
  - Template image is 'Cross.png'

4. 'Denoising'
  - Applies adaptive thresholding on the image to smooth out the background and make the tracks stand out visually.

5. 'Contouring'
  - Applies the cv2.contour function on an image to detect contours and provide their coordinates.

**Additional files**
1. Cross.png
  - The template image of fiducial marks used in 'Temp_match'.
2. Sample.png
  - A sample bubble chamber film image that is used as the input image for all algorithms.

**Usage**
1. Download 'Sample.png' and 'Cross.png'.
2. Replace the placeholder file paths in the code with the actual paths to the downloaded images.
3. Run the main script.

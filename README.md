Programs and aims:
1. 'Opening_images' (required for other algorithms)
- Takes an image file path and outputs a resized image.
- It is used in ALL subsequent algorithms.

2. 'Find_tracks'
- Finds coordinates of points on tracks, groups them into tracks based on similar y-coordinates and applies a polynomial model to the tracks.

3. 'Temp_match'
- Provides coordinates of the fiducial marks by matching them with a template image of the cross.

4. 'Denoising'
- Applies adaptive thresholding on the image to smooth out the background and make the tracks stand out visually.

5. 'Contouring'
- Applies the cv2.contour function on an image to detect contours and provide their coordinates.

Additional files:
1. template

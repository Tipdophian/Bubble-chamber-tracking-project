Aims: 
1. To detect particle tracks and obtain their coordinates from a bubble chamber film image.
2. To detect coordinates of the fiducial marks on the images.

Successful programs:
1. 'Opening_images' opens images from a file and resizes it. It is used in all subsequent algorithms.
2. 'Find_tracks' coordinates points on tracks, groups them into tracks based on similar y-coordinates and applies a polynomial model to the tracks. It fulfils aim 1.
3. 'Temp_match' provides coordinates of crosses by mthemching it with a template image of the cross. It fulfils aim 2.
4. 'Denoising' applies adaptive thresholding on the image and denoises it, smoothing out the background and making the tracks visually clearer.
5. 'Contouring' applies the cv2.contour function on an image to detect contours., Ideally the image has minimal background noise.

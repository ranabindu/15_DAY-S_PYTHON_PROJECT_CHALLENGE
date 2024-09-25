import numpy as np
import imageio.v2 as imageio  # Use v2 as per the warning
import scipy.ndimage
import cv2

img = "E:/sadow/python projects/IMG to SKCH Convater/gg.jpg"  # the image file

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])  # Convert image to grayscale

def dodge(front, back):
    final_sketch = front * 255 / (255 - back)
    # If any pixel value is greater than 255, cap it at 255
    final_sketch[final_sketch > 255] = 255
    final_sketch[back == 255] = 255
    return final_sketch.astype('uint8')  # Convert to 8-bit unsigned integer

ss = imageio.imread(img)  # Read the image
gray = rgb2gray(ss)  # Convert image to grayscale

i = 255 - gray  # Invert grayscale image

# Apply Gaussian blur using the correct module
blur = scipy.ndimage.gaussian_filter(i, sigma=15)

r = dodge(blur, gray)  # Create the sketch effect by blending the blurred image with the grayscale

cv2.imwrite('GG-sketch.jpg',r)
from PIL import Image, ImageChops, ImageEnhance
import os

# Define the file paths
file_path1 = r"E:/sadow/python projects/IMAGE DIFFERENCE DITECTION/1-1521.jpg"
file_path2 = r"E:/sadow/python projects/IMAGE DIFFERENCE DITECTION/1-152.jpg"

# Check if files exist
if not os.path.exists(file_path1):
    print(f"File not found: {file_path1}")
    exit(1)
if not os.path.exists(file_path2):
    print(f"File not found: {file_path2}")
    exit(1)

try:
    # Load the images
    img1 = Image.open(file_path1)
    img2 = Image.open(file_path2)

    # Convert images to grayscale
    img1_gray = img1.convert('L')
    img2_gray = img2.convert('L')

    # Compute the difference
    diff = ImageChops.difference(img1_gray, img2_gray)

    # Enhance the difference image to make differences more visible
    enhancer = ImageEnhance.Contrast(diff)
    diff_enhanced = enhancer.enhance(2.0)  # Increase contrast

    # Apply a threshold to highlight significant differences
    threshold = 30
    diff_thresholded = diff_enhanced.point(lambda p: p > threshold and 255)

    # Show the difference image if there are any differences
    if diff_thresholded.getbbox():
        diff_thresholded.show()

except Exception as e:
    print(f"An error occurred: {e}")

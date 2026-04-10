# Grayscale Image Quantization Using Python (PIL & NumPy)

# Background
# A small imaging startup is working on reducing the storage size of grayscale images used in low-bandwidth applications such as remote
# sensing dashboards and embedded systems. The goal is not to compress images using standard formats, but to reduce the number of intensity 
# levels while preserving the overall structure of the image.

# An intern is asked to prototype a manual grayscale quantization algorithm using Python so that the logic is transparent and easy to reason 
# about for learning and analysis.

# Problem Statement

# Given an 8-bit grayscale image (pixel values ranging from 0 to 255), reduce the image to 8 discrete gray levels by mapping ranges of pixel 
# intensities to a smaller set of values.

# Each new pixel value should represent a bucket of intensities rather than the original fine-grained value.

# Tools Used
# PIL (Python Imaging Library): for loading, converting, and saving images
# NumPy: for converting the processed image into an array for further analysis

# Step-by-Step Explanation of the Approach
# Step 1: Load and Prepare the Image
# The image is loaded from disk.
# It is explicitly converted into grayscale mode ('L'), ensuring each pixel has a single intensity value between 0 and 255.
# A pixel access object (pixelMap) is created to read pixel values.

# Step 2: Create a New Output Image
# A new grayscale image with the same dimensions as the original is created.
# Another pixel access object (pixelNew) is used to write the quantized pixel values.

# Step 3: Quantization Logic
# Two nested loops traverse every pixel (i, j) in the image.
# Each pixel value is checked against predefined intensity ranges.
# Based on the range it falls into, the pixel is assigned a new value from 0 to 7.
# Original Intensity Range New Value

from PIL import Image # In-built module - Python Imaging Library
import numpy as np

# Step 1: Load the image in Grayscale mode
old_im = Image.open("images.jpg").convert("L") # Ensure Grayscale
pixelMap = old_im.load()

# Step 2: Create a new Grayscale image
new_im = Image.new("L", old_im.size)
pixelNew = new_im.load()

# Step 3: Qunatize
for i in range(new_im.size[0]):
    for j in range(new_im.size[1]):
        if 0<=pixelMap[1,j]<=31:
            pixelNew[i,j] = 0
        elif 32<=pixelMap[1,j]<=63:
            pixelNew[i,j] = 1
        elif 64<=pixelMap[1,j]<=95:
            pixelNew[i,j] = 2
        elif 96<=pixelMap[1,j]<=127:
            pixelNew[i,j] = 3
        elif 128<=pixelMap[1,j]<=159:
            pixelNew[i,j] = 4
        elif 160<=pixelMap[1,j]<=191:
            pixelNew[i,j] = 5
        elif 192<=pixelMap[1,j]<=223:
            pixelNew[i,j] = 6
        elif 224<=pixelMap[1,j]<=255:
            pixelNew[i,j] = 7
		
new_im.save("lena_2.jpg")
J = np.asarray(Image.open("lena_2.jpg"))        

# Assume a pixel at position (10, 20) in the original image has a grayscale value of 31.
# What will be the value stored at the same position in pixelNew?
#  0   (Right Answer)
#  1
#  2
#  7


# What will be the quantized value for a pixel whose original grayscale intensity is 223?
#  6      (Right Answer)
#  5
#  7
#  4


# Assuming the input is an RGB image, what happens without grayscale conversion?
#  The output image would still be correct
#  The image would automatically convert to grayscale
#  The quantization ranges would adjust dynamically
#  The code would fail because pixelMap would return tuples instead of single values   (Right Answer)


# Which change would reduce execution time significantly while keeping the output logically equivalent?
#  Add more conditional checks
#  Increase the number of intensity ranges
#  Save the image in PNG instead of JPG
#  Replace nested loops with NumPy vectorized operations   (Right Answer)


# A Python program processes a grayscale image by examining each pixel value (ranging from 0 to 255). Based on fixed intensity intervals, 
# the program assigns one of a small set of integer values to a new image. The transformed image is then saved and viewed using a standard 
# image viewer with no contrast stretching or enhancement applied.
# Which option best describes the visual appearance of the output image and the mathematical operation being performed on each pixel?

#  The image appears nearly black with very low contrast.
# Formula:
# Pixel_new = Pixel_old / 255

# The image preserves smooth gradients but with reduced brightness.
# Formula:
# Pixel_new = Pixel_old − 32

# The image shows random speckle noise due to heavy quantization.
# Formula:
# Pixel_new = Pixel_old XOR 32

# The image appears nearly black.
# Formula:
# Pixel_new = floor(Pixel_old / 32)   (Right Answer)


# Optimised Version
from PIL import Image # In-built module - Python Imaging Library
import numpy as np

old_im = Image.open("images.jpg").convert("L") # Ensure Grayscale
arr = np.array(old_im)
quantized = arr//32 # Converts Pixel intensities 0-255 to 0-7 quantized buckets 
new_im = Image.fromarray(quantized.astype(np.uint8)) # Converts the array’s data type to 8-bit unsigned integers (0–255)
		
new_im.save("lena_2.jpg")
J = np.asarray(Image.open("lena_2.jpg"))  
# # Problem 1 : Edge Detection
from skimage import io
from skimage import measure

from skimage.color import rgb2gray
from skimage.filters import sobel
from skimage.filters import roberts
from skimage import feature
import numpy as np
img = io.imread('yale.png')
io.imshow(img)
io.show()

# Take the color image and convert it to a grayscale image:
grey_img = rgb2gray(img)
io.imshow(grey_img)
io.show()

# Sobel operator
sobel_edge = sobel(grey_img)
io.imshow(sobel_edge)
io.show()

# Robot’s Cross
robert_cross_edge = roberts(grey_img)
io.imshow(robert_cross_edge)
io.show()

# The Canny Edge Detector
canny_edge = feature.canny(grey_img)
io.imshow(canny_edge.astype(np.float64))
io.show()

# # 1. Low threshold
canny_edge_1 = feature.canny(grey_img, low_threshold = 0.1, high_threshold = 0.5)
io.imshow(canny_edge_1.astype(np.float64))
io.show()

canny_edge_2 = feature.canny(grey_img, low_threshold = 0.2, high_threshold = 0.5)
io.imshow(canny_edge_2.astype(np.float64))
io.show()

canny_edge_3 = feature.canny(grey_img, low_threshold = 0.3, high_threshold = 0.5)
io.imshow(canny_edge_3.astype(np.float64))
io.show()

canny_edge_4 = feature.canny(grey_img, low_threshold = 0.4, high_threshold = 0.6)
io.imshow(canny_edge_4.astype(np.float64))
io.show()

# # 2. High threshold
canny_edge_1 = feature.canny(grey_img, low_threshold = 0.1, high_threshold = 0.3)
io.imshow(canny_edge_1.astype(np.float64))
io.show()

canny_edge_2 = feature.canny(grey_img, low_threshold = 0.1, high_threshold = 0.5)
io.imshow(canny_edge_2.astype(np.float64))
io.show()

canny_edge_3 = feature.canny(grey_img, low_threshold = 0.1, high_threshold = 0.7)
io.imshow(canny_edge_3.astype(np.float64))
io.show()

canny_edge_4 = feature.canny(grey_img, low_threshold = 0.1, high_threshold = 0.9)
io.imshow(canny_edge_4.astype(np.float64))
io.show()
#
# # 3. sigma
canny_edge_1 = feature.canny(grey_img, sigma = 0.3)
io.imshow(canny_edge_1.astype(np.float64))
io.show()

canny_edge_2 = feature.canny(grey_img, sigma = 0.5)
io.imshow(canny_edge_2.astype(np.float64))
io.show()

canny_edge_3 = feature.canny(grey_img, sigma = 0.7)
io.imshow(canny_edge_3.astype(np.float64))
io.show()

canny_edge_4 = feature.canny(grey_img, sigma = 0.9)
io.imshow(canny_edge_4.astype(np.float64))
io.show()

# # Problem 2: Finding Color Blobs
img = io.imread('object.jpg')
io.imshow(img)
io.show()

# 1. Divide the color image into three separate color-channel images
redImage = img[:, :, 0]
greenImage = img[:, :, 1]
blueImage = img[:, :, 2]

# 2. Binarize the images by applying a threshold
redBinary = np.logical_and(redImage > 125, greenImage < 64, blueImage < 64)
yellowBinary = np.logical_and(redImage > 125, greenImage > 125)
blueBinary = blueImage > 143
greenBinary = np.logical_and(np.logical_and(greenImage > 130, redImage < 90), blueImage < 110)

# io.imshow(redBinary.astype(np.float64))
# io.show()
# io.imshow(yellowBinary.astype(np.float64))
# io.show()
# io.imshow(blueBinary.astype(np.float64))
# io.show()
# io.imshow(greenBinary.astype(np.float64))
# io.show()

# 3. Label connected components in the binary images using region growing
# e.g. redTagged - 0: background 1: first region 2: second region
redTagged, redN = measure.label(redBinary, connectivity = 2, return_num = True)
yellowTagged, yellowN = measure.label(yellowBinary, connectivity = 2, return_num = True)
blueTagged, blueN = measure.label(blueBinary, connectivity = 2, return_num = True)
greenTagged, greenN = measure.label(greenBinary, connectivity = 2, return_num = True)

# print(redN)
# print(yellowN)
# print(blueN)
# print(greenN)

# 4. Extract a binary image showing the location of each tagged region
# yellow1 = yellowTagged == 1 # return a T/F array
# yellow2 = yellowTagged == 2
# green1 = greenTagged == 1
# green2 = greenTagged == 2
# blue1 = blueTagged == 1
# blue2 = blueTagged == 2
# red1 = redTagged == 1
# red2 = redTagged == 2

# 5. Compute the boundary and the centroid
# boundary: the maximum and minimum row and column for the tagged region
# centroid: the average row and column position of each pixel in the tagged region

def get_regions_rows_cols(tagged_img, region_idx):
    binary = tagged_img == region_idx
    row_vec = binary.max(0) # the row vec corresponds to the max element in each column
    cols = np.flatnonzero(row_vec)

    col_vec = binary.max(1)  # the col vec corresponds to the max element in each row
    rows = np.flatnonzero(col_vec)

    col_min = cols.min()
    col_max = cols.max()
    row_min = rows.min()
    row_max = rows.max()
    col_centroid = cols.mean()
    row_centroid = rows.mean()
    print(row_centroid, col_centroid, row_max, col_max, row_min, col_min)
    return row_centroid, col_centroid, row_max, col_max, row_min, col_min


get_regions_rows_cols(yellowTagged, 1)
get_regions_rows_cols(yellowTagged, 2)
get_regions_rows_cols(greenTagged, 1)
get_regions_rows_cols(greenTagged, 2)
get_regions_rows_cols(blueTagged, 1)
get_regions_rows_cols(blueTagged, 2)
get_regions_rows_cols(redTagged, 1)
get_regions_rows_cols(redTagged, 2)


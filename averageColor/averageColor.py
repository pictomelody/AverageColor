import numpy
import cv2

def average_color(pixelbox):
    """
    Finds the average bgr color of a list of pixels
    """
    blue_sum = 0
    green_sum = 0
    red_sum = 0

    for row in pixelbox:
        for pixel in row:
            blue_sum += pixel[0]
            green_sum += pixel[1]
            red_sum += pixel[2]

    #average of: blue, green, red
    average_colors = [blue_sum/len(pixelgrid), green_sum/len(pixelgrid), red_sum/len(pixelgrid)]

    return (average_colors)

cv2.imread("Cat-With-Glasses1.jpg", CatPic1)

#Image dimension variables
img_size = CatPic1.shape
xsize = img_size[0]
ysize = img_size[1]
n_roi = 5
xrem = xsize%n_roi
yrem = ysize%n_roi
xsize_roi = xsize/n_roi
ysize_roi = ysize/n_roi


roi_matrix = []
#xcoordinate_temp = 0
#ycoordinate_temp = 0

#turns image into grid. there should be 25 2-D boxes
for i in xrange(n_roi):

    y1 = i*ysize_roi
    y2 = y1+ysize_roi
    if i+1 == n_roi:    #is it on the bottom of the grid? if so, then add the y padding
        y2 += yrem

    for j in xrange(n_roi):
        x1 = j*xsize_roi
        x2 = x1+xsize_roi
        if j+1 == n_roi:    #is it on the right of the grid? if so, then add the x padding
            x2 += xrem
        #each element of roi_matrix is a 2D box
        roi_matrix[i*n_roi+j] = CatPic1[x1:x2, y1:y2]

average_roi = []    #average_roi is a 25-element list of the average colors of the image

for i in xrange(len(roi_matrix)):
    average_roi[i] = average_color(roi_matrix[i])

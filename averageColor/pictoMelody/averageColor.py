import sys

sys.path.append('C\Annie\Python2.7\Lib\site-packages')

import numpy as np
import cv2

def averageColorBox(pixelbox):
    """
    Finds the average bgr color of a box of pixels
    """
    blue_sum = 0
    green_sum = 0
    red_sum = 0
    x = len(pixelbox)
    y = len(pixelbox[0])

    for i in xrange(x):
        for j in xrange(y):
            blue_sum += pixelbox[i][j][0]
            green_sum += pixelbox[i][j][1]
            red_sum += pixelbox[i][j][2]

    #average of: blue, green, red
    average_colors = [blue_sum/(x*y), green_sum/(x*y), red_sum/(x*y)]

    return (average_colors)

def averageColorGrid(image):

    img = cv2.imread(image)

    #Image dimension variables
    img_size = img.shape
    width = img_size[0] #xsize
    height = img_size[1] #ysize
    n_box = 5 #number of boxes in one dimension (so total number of boxes = 5x5)
    xrem = width%n_box #when image can't be evenly split into 5x5
    yrem = height%n_box #there will be a x and y remainder
    width_box = width/n_box #width of each box
    height_box = height/n_box #height of each box
    avgcolor = [] #avgcolor is a 25-element list of the average colors of the image

    box_matrix = [] #each element of box_matrix is a box of pixels

    #turns image into grid. there should be 25 2-D boxes
    for i in xrange(n_box):

        y1 = i*height_box #upper limit of box height
        y2 = y1+height_box #lower limit of box height
        #is it on the bottom of the grid? if so, then add the y padding
        if i+1 == n_box:
            y2 += yrem

        for j in xrange(n_box):
            x1 = j*width_box
            x2 = x1+width_box
            #is it on the right of the grid? if so, then add the x padding
            if j+1 == n_box:
                x2 += xrem
            box_matrix.append(img[x1:x2, y1:y2]) #each element of box_matrix is a 2D box

    box_matrix = np.array(box_matrix)

    for i in xrange(len(box_matrix)):
        avgcolor.append(averageColorBox(box_matrix[i]))

    return avgcolor

print(averageColorGrid("Cat-With-Glasses1.jpg"))

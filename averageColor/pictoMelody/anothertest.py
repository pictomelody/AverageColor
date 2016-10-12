import sys

sys.path.append('C\Annie\Python2.7\Lib\site-packages')

import numpy as np
import cv2

def averageColor(pixelbox):
    """
    Finds the average bgr color of a box of pixels
    """
    blue_sum = 0
    green_sum = 0
    red_sum = 0
    n = len(pixelbox)

    for row in pixelbox:
        for pixel in row:
            blue_sum += pixel[0]
            green_sum += pixel[1]
            red_sum += pixel[2]

    #average of: blue, green, red
    average_colors = [blue_sum/(n**n), green_sum/(n**n), red_sum/(n**n)]

    return (average_colors)

matrix3D = [[[0,0,0],[1,1,1],[2,2,2],[3,3,3],[4,4,4]],
            [[0,0,0],[1,1,1],[2,2,2],[3,3,3],[4,4,4]],
            [[0,0,0],[1,1,1],[2,2,2],[3,3,3],[4,4,4]],
            [[0,0,0],[1,1,1],[2,2,2],[3,3,3],[4,4,4]],
            [[0,0,0],[1,1,1],[2,2,2],[3,3,3],[4,4,4]]]

matrixArray = np.asarray(matrix3D)

cv2.imwrite("test.png", matrixArray)
PicTest = cv2.imread("test.png")

#Image dimension variables
img_size = PicTest.shape
width = img_size[0] #xsize
height = img_size[1] #ysize
n_box = 5 #number of boxes in one dimension (so total number of boxes = 5x5)
xrem = width%n_box #when image can't be evenly split into 5x5
yrem = height%n_box #there will be a x and y remainder
width_box = width/n_box #width of each box
height_box = height/n_box #height of each box

box_matrix = [] #each element of box_matrix is a box of pixels. there is 1 box/row, and 25 rows
print(box_matrix)
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
        print(PicTest[x1:x2, y1:y2])
        box_matrix.append(PicTest[x1:x2, y1:y2]) #each element of box_matrix is a 2D box

#flatten
arr = np.array(box_matrix)
print(arr)
print("STOP")

avgcolor_grid = []
for i in xrange(len(arr)):
    avgcolor_grid.append(averageColor(arr[i]))

arr = np.array(avgcolor_grid)
print(arr.tolist())

#for row in arr:
    #print(row.tolist())

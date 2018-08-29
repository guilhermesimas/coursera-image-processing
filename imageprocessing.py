import copy
import math

def width(image):
  return len(image)

def height(image):
  return len(image[0])

def adjustGreyscale(img, factor):
    if  1 > factor > 7:
        print("Invalid factor. Use between 1 and 8 please.")

    mask = (2**factor) - 1;

    w = width(img)
    h = height(img)

    imgcpy = copy.deepcopy(img)

    for x in range(0,w):
        for y in range(0,h):
            imgcpy[x][y] &= ~mask
            if imgcpy[x][y] != 0:
                imgcpy[x][y] |= mask

    return imgcpy

def spatialAverage(img, factor):
    if  factor < 1:
        print("Invalid factor. Use larger than 1 please.")

    w = width(img)
    h = height(img)

    processed_img = copy.deepcopy(img) 

    for x in range(0,w):
        for y in range(0,h):
            spatial_sum = 0
            n = (1+(factor*2))**2
            for i in range(x-factor,x+factor+1):
                # print("i is now " + str(i))
                if not 0 <= i < w:
                    n -= 1+(factor*2)
                    # print("n is now " + str(n))
                    continue
                for j in range(y-factor,y+factor+1):
                    # print("j is now " + str(j))
                    if not 0 <= j < h:
                        n -= 1
                        continue
                    spatial_sum += img[i][j]
            processed_img[x][y] = int(spatial_sum / n)

    return processed_img

def rotate(img,degree):

    w = width(img)
    h = height(img)

    processed_img = [[0]*h]*w 

    for x in range(0,w):
        for y in range(0,h):
            new_x = int(x*math.cos(degree) - y*math.sin(degree))
            new_y = int(x*math.sin(degree) + y*math.cos(degree))
            if 0 <= new_x < w and 0 <= new_y < h:
                processed_img[new_x][new_y] = img[x][y]
    return processed_img

    

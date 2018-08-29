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

    for x in range(0,w):
        for y in range(0,h):
            img[x][y] &= ~mask
            if img[x][y] != 0:
                img[x][y] |= mask

    return img

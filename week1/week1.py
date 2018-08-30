import pgm
import imageprocessing as ip
import math

print("Coursera Image Processing Week 1")

image = pgm.loadPGM("casablanca.ascii.pgm")

image_greyscale = ip.adjustGreyscale(image,4)
pgm.writeImage(image_greyscale,"image_greyscale.pgm")

image_spatial_avg = ip.spatialAverage(image,3)
pgm.writeImage(image_spatial_avg,"image_spatial_avg.pgm")

image_rotated = ip.rotate(image,math.pi / 6)
pgm.writeImage(image_rotated,"image_rotate.pgm")

image_rotated_no_aliasing = ip.rotateNoAliasing(image,math.pi / 6)
pgm.writeImage(image_rotated_no_aliasing,"image_rotated_no_aliasing.pgm")

image_reduced_res = ip.reduceResolution(image,4)
pgm.writeImage(image_reduced_res,"image_reduced_red.pgm")

exit()

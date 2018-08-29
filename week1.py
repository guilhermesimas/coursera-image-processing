import pgm
import imageprocessing as ip

print("Coursera Image Processing Week 1")

image = pgm.loadPGM("fractal_tree.ascii.pgm")

image = ip.adjustGreyscale(image,7)

pgm.writeImage(image,"image_copy.pgm")

exit()

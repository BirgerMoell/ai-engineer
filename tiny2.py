# Write a function that creates a random image that is 100x100 pixels.
# The image should be in rgb and have random colors and be with pretty patterns
import random
from PIL import Image
#
def create_random_image():
     # create a new image
    img = Image.new('RGB', (100, 100))
    # get the pixels of the image
    pixels = img.load()
    # loop over the pixels
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            # set the pixel to a random color
            pixels[i,j] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    # save the image
    img.save('random_image.png')
    # show the image
    img.show()
#
create_random_image()
# write a function that plots a mandelbrot set and saves the image to a file
# the function should take the following arguments:
#   - the name of the file to save the image to
#   - the width of the image in pixels
#   - the height of the image in pixels
#   - the number of iterations to use when computing the mandelbrot set
#   - the real part of the center of the image
#   - the imaginary part of the center of the image
#   - the width of the image in the complex plane
#   - the height of the image in the complex plane
#   - the color palette to use when coloring the image

# import the necessary modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors

# define the function
def mandelbrot(filename, width, height, iterations, real_center, imag_center, real_width, imag_height, color_palette):
    # create a 2D array of complex numbers
    real = np.linspace(real_center - real_width/2, real_center + real_width/2, width)
    imag = np.linspace(imag_center - imag_height/2, imag_center + imag_height/2, height)
    c = real[:, np.newaxis] + 1j*imag[np.newaxis, :]
    # create a 2D array of zeros
    z = np.zeros((height, width), dtype=complex)
    # create a 2D array of zeros to store the number of iterations
    n = np.zeros((height, width), dtype=int)
    # create a 2D array of zeros to store the number of iterations
    m = np.zeros((height, width), dtype=int)
    # create a 2D array of zeros to store the number of iterations
    p = np.zeros((height, width), dtype=int)
    # create a 2D array of zeros to store the number of iterations
    q = np.zeros((height, width), dtype=int)
    # create a 2D array of zeros to store the number of iterations
    r = np.zeros((height, width), dtype=int)

    # compute the mandelbrot set
    for i in range(iterations):
        z = z**2 + c
        mask = np.abs(z) < 2
        n[mask] = i
        m[mask] = i
        p[mask] = i
        q[mask] = i
        r[mask] = i
    
    # create a figure
    fig = plt.figure(figsize=(width/100, height/100), dpi=100)
    # plot the mandelbrot set
    plt.imshow(n, cmap=color_palette, norm=colors.PowerNorm(0.3))
    # remove the axes
    plt.axis('off')
    # save the figure
    plt.savefig(filename, bbox_inches='tight', pad_inches=0)
    # close the figure
    plt.close(fig)


# call the function
mandelbrot('mandelbrot.png', 1000, 1000, 100, 0, 0, 4, 4, 'magma')
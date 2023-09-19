# write a function that calculate the area of a circle
import numpy as np

def area_of_circle(radius :int):
    area = np.pi * radius**2
    return area

# write a function that calculate the area of a triangle

def area_of_triangle(base: int, height: int):
    area = 0.5 * base * height
    return area

# write a function that calculate the area of a rectangle

def area_of_rectangle(width: int, height: int):
    area = width * height
    return area

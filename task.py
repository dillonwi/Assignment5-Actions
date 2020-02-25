import math


def firstrun():
    return "success"


def getArea(radius):
    # Initialize the area variable.
    area = 0

    # Mulitply the radius by itself and pi to get the area
    area = radius * radius * math.pi

    # return the area
    return area

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


def firstLast(list):
    # Python allows for returning multiple values. We do this here by returning the first and last value.
    return list[0], list[-1]


def dateDiff(sDate, eDate):
    # Calculate the difference between the dates and return the diff.
    return (eDate - sDate).days
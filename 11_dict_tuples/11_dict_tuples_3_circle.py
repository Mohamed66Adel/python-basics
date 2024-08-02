# todo: Write circle_calc() function that takes radius of a circle as an input from user and
#  then it calculates and returns area, circumference and diameter.
#  You should get these values in your main program by calling circle_calc function and then print them.
from math import pi


def circle_calc(r):
    d = 2 * r
    area = pi * r**2
    circumference = d * pi
    return area, circumference, d


if __name__ == "__main__":
    r = float(input("Enter the radius of the circle: "))
    area, circumference, d = circle_calc(r)
    print(f"Area: {area:.2f}")
    print(f"Circumference: {circumference:.2f}")
    print(f"Diameter: {d:.2f}")

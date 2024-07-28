from utils import print_separator


# todo:1 Write a function called calculate_area that takes base and height as an input and returns and area of a triangle.
#  Equation of an area of a triangle is, [area = (1/2)*base*height]
def calculate_area(base, height):
    return 0.5 * base * height


# todo:2 Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle".
#  Based on shape type it will calculate area.
#  Equation of rectangle's area is, [rectangle area=length*width]
#  If no shape is supplied then it should take triangle as a default shape
def calculate_area2(base, height, shape="triangle"):
    if shape == "rectangle":
        return base * height
    return 0.5 * base * height


# todo:3 Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
#  *
#  **
#  ***
#  if input is 4 then it should print
#  *
#  **
#  ***
#  ****
#  Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)
def print_pattern(n, **kwargs):
    for i in range(1, n + 1):
        print("*" * i)
    print('\n')


if __name__ == "__main__":
    print_separator(1)
    print(calculate_area(10, 20))
    print_separator(2)
    print(calculate_area2(10, 20))
    print(calculate_area2(10, 20, "rectangle"))
    print_separator(3)
    print_pattern(3)
    print_pattern(4)

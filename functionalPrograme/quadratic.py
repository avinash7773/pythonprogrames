"""
@Author : Avinash Jadhav
@Date : 2021-11-12
@Last Modify by : Avinash Jadhav
@Title : print quadratic equation
"""


import math


def find_roots(a, b, c):
    """
        @Description : find roots of quadratic equation
        @Parameter   : parameter is value of equation
        @return      : -
    """
    if a == 0:
        print("Invalid")
        return -1
    delta = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(delta))

    if delta > 0:
        print("Roots are real and different ")
        print((-b + sqrt_val) / (2 * a))
        print((-b - sqrt_val) / (2 * a))
    elif delta == 0:
        print("Roots are real and same")
        print(-b / (2 * a))
    else:
        print("Roots are complex")
        print(- b / (2 * a), " + i", sqrt_val)
        print(- b / (2 * a), " - i", sqrt_val)


a = 1
b = -7
c = 12

# Function call
find_roots(a, b, c)
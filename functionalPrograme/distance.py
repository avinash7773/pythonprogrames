
""""
@Author : Avinash Jadhav
@Date : 2021-11-12
@Last Modify by : Avinash Jadhav
@Title : calculate distance
"""

import math
import sys


def calculate_distance(x1, x2, y1, y2):
    """
       @Description : find distance by using math module
       @Parameter   : parameter is coordinate values
       @return      : distance
    """
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
d = int(sys.argv[4])

distance = calculate_distance(a, b, c, d)
print("Distance = ", distance)

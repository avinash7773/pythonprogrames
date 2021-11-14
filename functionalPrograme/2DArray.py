'''
@Author : Avinash Jadhav
@Date : 2021-11-11
@Last Modify by : Avinash Jadhav
@Title : print 2D array
'''

from numpy import *
def printArray(array):
    '''
    @Description : take number of rows and colunm from user and print 2D array
    @Parameter   : parameter is only one that is array
    @return      : - '''
    for i in range(number_of_rows):
        for j in range(number_of_colunm):
            print(array[i][j], end=" ")
        print()


array = []
try:
    number_of_rows = int(input("Enter number of rows:"))
    number_of_colunm = int(input("Enter number of colunm:"))
    for i in range(number_of_rows):
        temp_array = []
        for j in range(number_of_colunm):
            temp_array.append(int(input("Enter next element:")))
        array.append(temp_array)
    printArray(array)
except ValueError as e:
    print("Number of rows and colunm should be integer", e)
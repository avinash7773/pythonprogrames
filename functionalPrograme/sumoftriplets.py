"""
@Author : Avinash Jadhav
@Date : 2021-11-11
@Last Modify by : Avinash Jadhav
@Title : print three integer number
"""


def find_triplets(arr, n):
    """
        @Description : find triplets which sum equal to zero
        @Parameter   : parameter is only one that is array
        @return      : -
        """
    found = False
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if(arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])
                    found = True
    if found == False:
        print(" not exist ")


arr = [0, -1, 2, -3, 1]
n = len(arr)
find_triplets(arr, n)
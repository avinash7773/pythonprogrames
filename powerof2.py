''' 
@Author : Avinash Jadhav
@Date : 2021-11-09
@Last Modify by : Avinash Jadhav
@Title : find the power of N, take N value from argument
'''
import sys
N = int(sys.argv[1])
if(N>0 and N<=31):
    for i in range(1,N):
        print(2**i)
else:
    print("argument should be gretter than 0 and less than 31")

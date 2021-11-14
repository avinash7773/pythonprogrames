''' 
@Author : Avinash Jadhav
@Date : 2021-11-09
@Last Modify by : Avinash Jadhav
@Title : print prime number of given number
'''

'''
@Description : prime_factors function is finding prime factors of given number
@Parameter   : parameter is only one that is number
@return      : - '''
import math
def prime_factors(num):    
    while num % 2 == 0:  
        print(2,)  
        num = num / 2  
    for i in range(3, int(math.sqrt(num)) + 1, 2):  
        while num % i == 0:  
            print(i,)  
            num = num / i  
    if num > 2:  
        print(num)  
  
num = int(input("Enter number:"))  
prime_factors(num)
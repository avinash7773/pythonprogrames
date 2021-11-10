''' 
@Author : Avinash Jadhav
@Date : 2021-11-08
@Last Modify by : Avinash Jadhav
@Title : find head and tail percentage by using random() function
'''

import random

'''
@Description : flipcoin method will print percentage of tail and head
@Parameter   : parameter is only one that is number of time coin flip
@return      : return tail percentage and head percentage '''
def flipCoin(number_of_times_flip_coin):
   if(number_of_times_flip_coin <= 0):
        print("number_of_times_flip_coin should be positive")
   else:
         tail_count = 0;
         head_count = 0;
         i = 0
         while(i < number_of_times_flip_coin ):
            random_number = random.random()
            if(random_number <= 0.5) :
                tail_count = tail_count + 1
            else:
                head_count = head_count + 1
            i = i + 1
         tail_percentage = (tail_count / number_of_times_flip_coin) * 100
         head_percentage = (head_count / number_of_times_flip_coin) * 100
         return tail_percentage, head_percentage
          
try:
    number_of_times_flip_coin = int(input("Enter any number:"))
    tail_percentage,head_percentage = flipCoin(number_of_times_flip_coin)
    print("Tail Percentage=",tail_percentage,"%")
    print("head percentage=",head_percentage,"%")
except Exception as e:
    print("input should be integer",e)

   



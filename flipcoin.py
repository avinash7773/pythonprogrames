''' 
@Author : Avinash Jadhav
@Date : 2021-11-08
@Last Modify by : Avinash Jadhav
@Title : find head and tail percentage by using random() function
'''

tail_count = 0;
head_count = 0;
import random 

number_of_times_flip_coin = int(input("Enter any number:"))

if(number_of_times_flip_coin <= 10):
    print("number_of_times_flip_coin should be positive")
else:
    i = 0
    while(i < number_of_times_flip_coin ):
        random_number = random.random()
        if(random_number < 0.5) :
            tail_count = tail_count + 1
        else:
            head_count = head_count + 1
        i = i + 1
    tail_percentage = (tail_count / number_of_times_flip_coin) * 100
    head_percentage = (head_count / number_of_times_flip_coin) * 100
    print("Tail Percentage=",tail_percentage,"%")
    print("head percentage=",head_percentage,"%")


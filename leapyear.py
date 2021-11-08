''' 
@Author : Avinash Jadhav
@Date : 2021-11-08
@Last Modify by : Avinash Jadhav
@Title : check year is leap or not
'''

def isLeap(year) :
    if((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
        return True
    else:
        return False
    

year = int(input("Enter year:"))

if(isLeap(year)):
    print(year," is Leap Year")
else:
    print(year," is not Leap Year")


    

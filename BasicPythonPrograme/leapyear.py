''' 
@Author : Avinash Jadhav
@Date : 2021-11-08
@Last Modify by : Avinash Jadhav
@Title : check year is leap or not
'''

'''
@Description : isLeap function will check given year is leap or not
@Parameter   : parameter is only one that is year
@return      : return boolean  '''
def isLeap(year) :
    if((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
        return True
    else:
        return False

try:
    year = int(input("Enter year:"))
    if(isLeap(year)):
        print(year," is Leap Year")
    else:
        print(year," is not Leap Year")
except ValueError as e:
    print("year should be integer",e)




    

''' 
@Author : Avinash Jadhav
@Date : 2021-11-09
@Last Modify by : Avinash Jadhav
@Title : print Nth harmonic number
'''


'''
@Description : sringTemplates function will check username is in given condition or not,
                if yes than it will replace string templates with username
@Parameter   : parameter is only one that is username
@return      : it will return string according to input'''

def harmonicNumber(N):
    harmonic_number = 0;
    for i in range(1,N+1):
        harmonic_number = harmonic_number + (1/i)
        
    return harmonic_number
       
         
        
N = int(input("Enter any number:"))
print(harmonicNumber(N))

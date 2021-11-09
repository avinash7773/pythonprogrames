''' 
@Author : Avinash Jadhav
@Date : 2021-11-08
@Last Modify by : Avinash Jadhav
@Title : print string templates
'''


'''
@Description : sringTemplates function will check username is in given condition or not,
                if yes than it will replace string templates with username
@Parameter   : parameter is only one that is username
@return      : it will return string according to input'''
def stringTemplates(username): 
    if(len(username) < 3) :
        return "username should min 3 character:"
    else:
        return "Hello "+username+" How are you"
    
    
username = input("Enter username:")
output_message = stringTemplates(username)
print(output_message)



'''
AT THIS PROGRAM WE ARE GOING TO USE THE REGEX (REGULAR EXPRESSIONS)
we will check the given inputs has the needed characters it should have or not (using REGEX)
____________________________
the INPUTS are :
--name
--moblie number
--E_mail id
--password
_____________________________
'''
import re
check = False
while check != True :
    name = input("Enter your name(without any special characters) : ")
    if re.search('[\w\s]*', name) != None:
        check = True
    else:
        print("the name should not have any special charters (-,:;'\"<>?/+= ) ")
check = False
while check == False :
    number = input("Enter your Number(please add pin code at start) : ")
    if re.search('[\+91][\d]{10}',number) != None:
        check = True
    else:
        print("This Number is not from India!!! please Enter an Indian Number ")
check = False
while check == False :
    E_mail = input("Enter the E_mail id :")
    if re.search('[\w]*[@][Gg][mail.com]',E_mail) != None:
        check = True
    else:
        print("these E_mail id is worng ")
check = False
while check == False :
    password = input("Enter the password :")
    c_password = input ("confrom password(re-enter the password) : ")
    if re.search('\w\W\s]+{6,}',password) != None and password ==c_password :
        check = True
    elif(password !=c_password) :
        print("please make shoull that you Enter same password")
    else :
        print('''the password has to have atlest 6 characters
               --Upper case letter
               --Lower case letter
               --special character ''')
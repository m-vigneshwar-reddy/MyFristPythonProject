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
    if re.search(r'[A-Z||a-z||\s||\_]*', name) != None:
        check = True
    else:
        print("the name should not have any special charters (-,:;'\"<>?/+= ) ")
check = False
while check == False :
    number = input("Enter your Number(please add pin code at start) : ")
    if re.search('[\+91][0-9]{10}',number) != None:
        check = True
    else:
        print("This Number is not from India!!! please Enter an Indian Number ")
check = False
while check == False :
    E_mail = input("Enter the E_mail id :")
    if re.search('[a-zA-Z0-9\_]*[@][G||g][mail.com]',E_mail) != None:
        check = True
    else:
        print("these E_mail id is worng ")
check = False
while check == False :
    password = input("Enter the password :")
    c_password = input ("confrom password(re-enter the password) : ")
    if re.search('[a-zA-z0-9[^a-zA-z0-9]]+{6,}[\s]*',password) != None and password ==c_password :
        check = True
    elif(password !=c_password) :
        print("please make shoull that you Enter same password")
    else :
        print('''the password has to have atlest 6 characters
               --Upper case letter
               --Lower case letter
               --special character ''')
s = 'y'
while s == 'y':
    ch = int(input("which pattern do you want to print on \n 1. Right Half pyramid\n2. Left Half pyramid\n"
               "3.inverted Right Half pyramid\n4.inverted left Half pyramid\n  :  "))
    inp = int(input("\nEnter The number of lines you want to print : "))
    if ch == 1 :
        for i in range(1,inp+1):
            print('*'*i)
    elif ch ==2 :
        for i in range(1,inp+1):
            print(' '*(inp-i),'*'*(i))
    elif ch == 3:
        for i in range(inp+1,0,-1):
            print('*'*i)
    elif ch == 4:
        for i in range(inp,0,-1):
            print(' '*(inp-i),'*'*(i))
    else :
        print("sorry! wrong option!!try again")
    s =  input("Do you want to continue ?(y/n) : ")
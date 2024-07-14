ch =1
di = {'Name':input("Enter your name :"),'number': []}
while ch == 1:
    di['number'] = di['number'] +[int(input("enter the number :"))]
    ch = int(input("do you want to add another number(1 or 0) : "))
di['top_number']=max(di['number'])
di.pop('number')
print(di)
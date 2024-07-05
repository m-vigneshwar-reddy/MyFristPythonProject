a=int(input('enter the number'))
i=1
if a >0 :
 print(a,'!=')
 while a>=1 :
    print(a,'*')
    i*=a
    a-=1
 print('=',i)
else:
    print('the value is none')

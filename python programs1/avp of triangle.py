#doing all about the triangle
#1.confirming the sides of triangle
import math

print('enter the sides of the triangle')
a=float(input())
b=float(input())
c=float(input())
if a+b>c and b+c>a and c+a>b :
    ch=int(input(print(''''what do you want to find out?
    1.volume
    2.area
    3.paremeter of the triangle
    ''')))
    while ch in (1,2,3,4):
        s=(a+b+c)/2
        A=math.sqrt((s*(s-a)*(s-b)*(s-c)))
        h=2*A%a
        V=a*h
        if ch==2:
            print('the area of the triangle is',A)
        if ch==1:
            print('the volume of the triangle is ',V)
        if ch==3:
            print('the paremeter of the triangle is',a+b+c)

        ch=int(input('ehter your chooise'))

else:
    print('worng sides!!!!!!!')
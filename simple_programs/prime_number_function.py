def prime(num):
    prim=[]
    for i in range(1,num+1):
        count = 0
        for j in range(1,i+1):
            if i%j == 0:
                count+=1
        if count == 2:
            prim.append(i) 
    return prim
limt = int(input("Enter the limit : "))               
print("the list of prime numbers below ",limt,' is : ',prime(limt))
size = int(input("Enter the size of the array : "))
print("Enter the elements of the array (",size,") : ")
array = list(int(input())for i in range(size))
for i in range(size):
    if array[i]<= array[i+1]:
        continue
    else:
        for j in range(i,size):
            if array[j]> array[j+1]:
                array[j+1],array[j]=array[j],array[j+1]
print("the sorted array is ",array)

i_string=input("Enter the string: ")
n_string=""
for i in range(len(i_string)-1,-1,-1):
    n_string += i_string[i]
print(n_string)    
i_string=input("Enter the string: ")
n_string=""
c=""
for i in range(len(i_string)):
    if i_string[i] in {'a','e','i','o','u','A','E','I','O','U'}:
        n_string += i_string[i]
    else:
        c += i_string[i]
print("split(",i_string,") is ",n_string+c)
# This is a script for lab 2 excercise 1a

x = input("Please provide an 8-bit binary number: \n")

missing = 8 - len(x)

if len(x) < 8:
    print("your number was less than 8-bits!")
    x = "0" * missing + x
    print("It has been augmented to: ", x)
if len(x) > 8:
    print("your number was larger than 8-bits!")
    exit()

bit_lst = list(x) # store string x as a list
bit_lst.reverse() # reverse that list
as_int = 0 # store the integer value in here
i = 0 # exponent
for j in bit_lst:
    as_int+= int(j) * 2**i
    i += 1 
print(x, " -> ", as_int)

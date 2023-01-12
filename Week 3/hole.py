# This is the script solution for lab 2 excercise 3

length = 12
L = range(length)

# Distance method
method = "euclidean" # "euclidean" "manhattan"

# Origin of hole
ox = length/2 
oy = length/2 
r = (length/2) - 1
if(r < 1):
    r = 1

for i in L:
    for j in L:
        # Calculate distance
        if method == "manhattan":
            distance = abs(j - ox) + abs(i - oy)
        else:
            distance = ((j-ox)**2 + (i-oy)**2)**0.5
            
        # Create hole
        if distance <= r:
            print(' ', end = "") 
        else:
            print('#', end = "")
    print("")
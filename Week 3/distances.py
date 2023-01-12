import sys

a = sys.argv
if(len(a) < 2):
    print("\nUSAGE: Please input x1 y1 x2 y2 on the command line")
    print("E.G. <python3 Excercise-2.py 0 0 1 1> mac")
    print("E.G. <py Excercise-2.py 0 0 1 1> win")
else:
    x1 = int(a[1])
    y1 = int(a[2])

    x2 = int(a[3])
    y2 = int(a[4])

    print("Distances between point (" + a[1] + ", " + a[2] + ") and ("  + a[1] + ", " + a[2] + ")")
    # Lets find the Euclidean distance 
    Euclidean = ((x2-x1)**2 + (y2-y1)**2)**0.5 
    print("Euclidean -> ", Euclidean)

    # Lets find the Manhattan distance
    Manhattan = abs(x2 - x1) + abs(y2 - y1)
    print("Manhattan -> ", Manhattan)
# ---
# SCRIPT NAME: 
#   <data_prompter_2.py>
#
# DESCRIPTION: 
#   1) Demonstrate input prompting in python 3. Prompted inputs
#      are srored in a list until the list has N 'rows'.
#   2) The rows of data are then printed to the screen.
#   3) Then, until the user decides not to, they can 'query' a chosen row, then
#      a chosen column (or crash the program if they don't keep inside the 
#      appropriate row/col index ranges...no error handling here!).
#   4) Finally, the data is used to derive calculated values and print
#      a formatted string to the console, per row of data.

# Ask the user for the inputs until N is reached
my_list = []
N = 2
while len(my_list) < N:
    fname = input("Please enter your forename, and press enter:\n> ")
    sname = input("Please enter your surname, and then press enter:\n> ")
    height = input("Please enter your height in <ft> <inches>, and then press enter:\n> ")
    weight = float(input("Please enter your weight in stone, and then press enter:\n> "))
    age = int(input("Please enter your age, and then press Enter:\n> "))

    my_list.append([fname, sname, height, weight, age])

# Print the rows of data
print("Here is the raw data:")
for r in my_list:
    print(r)

# User-prompted indices to access subsets of data
label = ""
while label != 'q':
 
    # User-defined row-wise index, then print the row
    max_row_index = N - 1
    msg = f"\nEnter a row index in [0, {max_row_index}]:\n> "
    row = int(input(msg))
    print(my_list[int(row)])

    # User-defined col-wise index, then print the row
    max_col_index = len(my_list[0]) - 1
    msg = f"\nEnter a column index in [0, {max_col_index}]:\n> "
    col_index = int(input(msg))
    column = [c[col_index] for c in my_list]
    for c in column:
        print(c)
    label = input("Enter q to quit or just enter to get some more data:\n> ")
 
# Some output similar to previous exercises, but now list-wise
for r in my_list:
    print("~ ~ ~ ~ ~")
    feet, inches = r[2].split()
    weightkg = r[3] * 6.35
    dob = 2022 - r[4]
    output = f"{r[0]} {r[1]} is {r[4]} years old, {feet} ft {inches} inches, {weightkg:.2f} kg and was born in {dob}."
    print(output)
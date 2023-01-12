# ---
# SCRIPT NAME: 
#   <data_prompter_2.py>
#
# DESCRIPTION: 
#   Simple script to demonstrate input prompting in python 3, simple 
#   data calculations on input data and storing formatted string output, 
#   all inside a while loop until N 'rows' of formatted data are stored.
# ---

# Ask the user for the inputs until N is reached
my_list = []
N = 2
while len(myList) < N:
    fname = input("Please enter your forename, and press enter:\n> ")
    sname = input("Please enter your surname, and then press enter:\n> ")
    height = input("Please enter your height in <ft> <inches>, and then press enter:\n> ")
    weight = float(input("Please enter your weight in stone, and then press enter:\n> "))
    age = int(input("Please enter your age, and then press Enter:\n> "))

    feet, inches = str.split(height)
    weightkg = weight * 6.35
    dob = 2022 - age

    row = f"Dear {fname} {sname}, you are {age}, {feet} ft {inches} inches, {weightkg:.2f} kg and you were born in {dob}."

    my_list.append(row)

# Print the rows of data
for i in my_list:
    print(i)
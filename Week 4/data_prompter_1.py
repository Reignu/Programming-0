# ---
# SCRIPT NAME: 
#   <data_prompter_1.py>
#
# DESCRIPTION: 
#   Simple script to demonstrate input prompting in python 3, simple 
#   data calculations on input data and formatted string output 
#   wrapped in the print.
# ---

fname = input("Please enter your forename, and press enter:\n> ")
sname = input("Please enter your surname, and then press enter:\n> ")
height = input("Please enter your height in <ft> <inches>, and then press enter:\n> ")
weight = float(input("Please enter your weight in stone, and then press enter:\n> "))
age = int(input("Please enter your age, and then press Enter:\n> "))

feet, inches = str.split(height)
weightkg = weight * 6.35
dob = 2022 - age

print(f"Dear {fname} {sname}, you are {age}, {feet} ft {inches} inches, {weightkg:.2f} kg and you were born in {dob}.")
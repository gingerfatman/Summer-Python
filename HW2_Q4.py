# Author: Athar Abdullah
# Assignment / Part: HW2 - Q4
# Date due: 2022-06-07
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

string = input("Please enter a string: ")
lw_string = string.lower()
lw_string = lw_string.replace("'", "")
lw_string = lw_string.replace(" ", "")
lw_string = lw_string.replace(".", "")
lw_string = lw_string.replace(",", "")
alpha = "abcdefghijklmnopqrstuvwxyz"
print(lw_string)
print(alpha)
missing = ""
for letter in alpha:
    if missing == "":
        print("True")
    else:
        missing += letter + " "
        print(missing)

    #if letter not in lw_string:      
      #  missing += letter + " "
#print("True")

    #if ord("a") <= ord(letter) <= ord("z"):
    #    print("True")
    #else:
       # missing += letter + " "
      #  print(missing)

#if ord(letter) != range(ord("a"),ord("z")+1):

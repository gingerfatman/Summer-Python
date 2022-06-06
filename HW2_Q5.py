# Author: Athar Abdullah
# Assignment / Part: HW2 - Q5
# Date due: 2022-06-07
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

max_value = int(input("Please enter a positive integer: "))
even_digits = ""
for num in range(1, max_value):
    rem = num % 10
    lastdigit = num // 10
    if rem % 2 == 0 and lastdigit % 2 == 0:
        even_digits += str(num) + " "

print(even_digits)
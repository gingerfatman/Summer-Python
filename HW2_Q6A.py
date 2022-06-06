# Author: Athar Abdullah
# Assignment / Part: HW2 - Q6A
# Date due: 2022-06-07
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.
import math
length = int(input("Please enter the length of the sequence: "))
count = 0
product = 1
print("Please enter your sequence:")
while count < length:
    seq = (input())
    count += 1
    product *= int(seq)

geomean = math.pow(product,1/length)
rgeomean = round(geomean,4)
print("The geometric mean is:",rgeomean)


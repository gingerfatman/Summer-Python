# Author: Athar Abdullah
# Assignment / Part: HW2 - Q6B
# Date due: 2022-06-07
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.
import math
count = 0
product = 1
print(("Please enter your sequence:"))
while True:
    seq = (input())
    count += 1
    product *= int(seq)
    if seq =="done":
        break
geomean = math.pow(product,1/count)
rgeomean = round(geomean,4)     

#geomean = math.pow(product,1/count)
#rgeomean = round(geomean,4)
print("The geometric mean is:",rgeomean)
#if seq == "done":
       # break
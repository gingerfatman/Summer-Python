# Author: Athar Abdullah
# Assignment / Part: HW2 - Q3
# Date due: 2022-06-07
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.
import math
first = float(input("Please enter lengths of a triangle's sides \nLength of the first side (float): "))
sec = float(input("Length of the second side (float): "))
third = float(input("Length of the third side (float): "))

if math.fabs(first - sec) < .00001 and math.fabs(first - third) < .00001: 
    print(first,",",sec,",",third,"form an equilateral triangle")
elif math.fabs(first - sec) > .00001 and math.fabs(first - third) > .00001 and math.fabs(sec - third) > .00001:
    print(first,",",sec,",",third,"form an scalene triangle")
elif math.fabs(first - sec) > .00001 and math.fabs(first - third) < .00001 or math.fabs(first - sec) < .00001 and math.fabs(sec - third) > .00001 or math.fabs(first - third) > .00001 and math.fabs(sec - third) < .00001:
    if math.fabs(sec - first * math.sqrt(2)) < .00001 and math.fabs(first - third) < .00001 or math.fabs(third - first * math.sqrt(2)) < .00001 and math.fabs(first - sec) < .00001  or math.fabs(first - sec * math.sqrt(2)) < .00001 and math.fabs(sec - third) < .00001:
        print(first,",",sec,",",third,"form an isosceles right triangle")
    else:
        print(first,",",sec,",",third,"form an isosceles triangle")


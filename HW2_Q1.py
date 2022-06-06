# Author: Athar Abdullah
# Assignment / Part: HW2 - Q1 
# Date due: 2022-06-07
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.
weight = float(input("Please enter weight in kilograms:"))
height = float(input("Please enter height in meters:"))
bmi = weight/height**2

if bmi < 18.5:
    status = "Underweight"
elif 18.5 <= bmi <= 24.9:
    status = "Normal"
elif 25.0 <= bmi <= 29.9:
    status = "Overweight"
else:
    status = "Obese"

print("Your BMI is",bmi,"and your weight status is:\"",status,"\"")
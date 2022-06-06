# Author: Athar Abdullah
# Assignment / Part: HW2 - Q2
# Date due: 2022-06-07
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

sentence = input("Enter a string to modify: ")
char = input("Enter an index value and a character: ")
search = char[0]
repl = char[2]

newsent = ""
for letter in sentence:
    newsent = newsent + letter
    if letter == search:
        #finde = sentence.find(search)  #Search for position of desired character
        letter = ""
        newsent = newsent + repl

print(newsent)
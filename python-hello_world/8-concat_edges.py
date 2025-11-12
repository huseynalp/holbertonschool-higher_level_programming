#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[str.find("object-oriented"):str.find("programming")+11] + " with Python"
print(str) # do not change this line

#!/usr/bin/python3
str = ("Python is an interpreted, interactive, object-oriented programming "
       "language that combines remarkable power with very clear syntax")
str = str[str.find("object-oriented"):str.find("programming") + 11]
print(str + " with Python")  # do not change this line Pycodestyle validation

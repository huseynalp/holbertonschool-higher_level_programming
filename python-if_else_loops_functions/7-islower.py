#!/usr/bin/python3
def islower(c):
    if len(c)!=1:
	raise ValueError("Input must be a single character")

    char_code=ord(c)
    return 97<= char_code <= 122


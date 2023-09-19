# create a function that calculates the lenght of s string

def length_of_string(s: str):
    if s == '':
        return 0
    else:
        return 1 + length_of_string(s[1:])
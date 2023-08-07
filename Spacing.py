#Defines solution function and takes one argument
def solution(s):
    #Creates an empty string
    space = ""
    #Loops through the given argument
    for char in s:
        #Checks if a character is an Upper Case
        if char.isupper():
            #Adds the space behind the Upper Case
            space += " "
        #Keeps the characters has they are
        space += char
    #Returns the spaced string
    return space

#Defines count method and takes one argument
def count(s):
    #Creates an empty dictionary
    char = {}
    #Loops through the given argument
    for i in s:
        #Checks the number of character occurence
        if i in char:
            char[i] += 1
        else:
            char[i] = 1
    #Returns the number of characters
    return char

#Defines count method and takes one argument
def count(s):
    #Checks if the argument is empty
    if not s:
        return {}
    #Creates an empty dictionary
    char = {}
    #Loops through the given argument
    for i in s:
        #Check the number of character occurence
        if i in char:
            char[i] += 1
        else:
            char[i] = 1
    #Returns the number of characters
    return char

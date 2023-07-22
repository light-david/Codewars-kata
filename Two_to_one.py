#Defines longest method
def longest(a1, a2):
    #Concatenates two strings
    string = a1 + a2
    #Removes duplicates
    sorted_string = set(string)
    #Sort the string in increasing order
    character = sorted(sorted_string)
    #Returns the sorted string
    return ''.join(character)

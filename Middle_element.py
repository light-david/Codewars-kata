#Defines get_middle function and takes one argument
def get_middle(s):
    #Assigns the middle element to length
    length = len(s) // 2
    #Checks if length of the argument is even
    if len(s) % 2 == 0:
        #Returns the two middle elements of the given argument
        return s[length - 1: length + 1]
    #Returns the middle element
    return s[length]

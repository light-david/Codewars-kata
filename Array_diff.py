#Defines the array_diff method and takes two arguments
def array_diff(a, b):
    #Creates an empty list
    empty_list = []
    #Loops through each elements of a
    for i in a:
        #Checks if each elements of a is in b
        if i not in b:
            #Adds the elements that are not in a to the empty list
            empty_list.append(i)
    #Returns the list
    return empty_list

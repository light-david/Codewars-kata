#Defines the function friend and accepts one argument
def friend(x):
    #Creates an empty list
    name = []
    #Iterates over the list
    for i in x:
        #Checks if the length of an element in the list is 4
        if len(i) == 4:
            #Adds the element to the empty list
            name.append(i)
    #Returns the list with the element
    return name

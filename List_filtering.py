#Defines filter_list method and takes one argument
def filter_list(l):
    #Creates an empty list
    digit = []
    #Loops through the taken argument
    for i in l:
        #Checks if i is an integer
        if type(i) == int:
            #Appends it to the empty list
            digit.append(i)
    #Returns the appended list
    return digit

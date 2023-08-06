#Defines double_char function and takes one argument
def double_char(s):
    #Creates an empty function
    duplicate = ""
    #Loops through the taken argument
    for i in s:
        #Iterates through each element in the argument
        duplicate += i + i 
    #Returns the duplicated argument
    return duplicate

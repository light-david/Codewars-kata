#Defines maps function and takes one argument
def maps(a):
    #Empty list created
    multiple_two = []
    #Loops through the argument
    for i in a:
        #Iterates through the argument
        i = i * 2
        #Inserts argument into the list
        multiple_two.append(i)
    #Output the appended list
    return multiple_two

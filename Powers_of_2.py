#Defines a function and takes one parameter
def powers_of_two(n):
    #Creates an empty list
    powers = []
    #Iterates through the given argument
    for i in range(n + 1):
        #Inputs it into the list
        powers.append(2 ** i)
    #Returns list
    return powers

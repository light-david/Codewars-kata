#Defines get_sum fucntion and takes two arguments
def get_sum(a,b):
    #Checks if the two arguments are equals
    if a == b:
        return a
    #Checks if the first argument is less than the second argument
    elif a < b:
        first, second = a, b
    else:
        first, second = b, a
    #Crreates a parameter
    add_sum = 0
    #Loops through given argument
    for num in range(first, second + 1):
        #Iterates through the given arrgument
        add_sum += num
    #Returns the sum
    return add_sum

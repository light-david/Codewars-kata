#Defines opposite function and takes one argument
def opposite(number):
    #Checks if the given argument is 0
    if number == 0:
        return 0
    #Checks if the given argument is less than 0
    elif number < 0:
        return abs(number)
    #Returns negativevalue of the given argument
    return number * -1

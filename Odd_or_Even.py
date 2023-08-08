#Defines odd_or_even function and takes an argument
def odd_or_even(arr):
    num = 0
    #Loops through the taken argument
    for i in arr:
        #Iterates through the argument
        num += i
    #Checks if num is divisble by 2
    if num % 2 == 0:
        return "even"
    #Returns odd if num is not divisble by 2
    return "odd"

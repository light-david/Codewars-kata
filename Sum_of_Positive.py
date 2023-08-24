#Defines positive_sum function and takes one argument
def positive_sum(arr):
    digit, sum_arr = 0, 0
    #Loops through the given argument
    for digit in arr:
        #Checks if any element is less than 0
        if digit < 0:
            digit = 0
        #Iterates through the the given argument
        sum_arr += digit
    return sum_arr

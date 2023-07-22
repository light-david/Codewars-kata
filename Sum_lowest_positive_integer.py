#Defines sum_two_numbers function
def sum_two_smallest_numbers(numbers):
    #Sorts numbers in increasing order
    num = sorted(numbers)
    #Adds the first two digits in numbers
    summation = num[0] + num[1]
    #Returns summation
    return summation

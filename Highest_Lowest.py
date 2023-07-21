#Defines high_and_low function which takes one argument
def high_and_low(numbers):
    #Spilts the string into substring
    str_numbers = [int(num) for num in numbers.split()]
    #Finds the minimum and maximum string
    x, y = min(str_numbers), max(str_numbers)
    number = f"{y} {x}"
    #Returns the maximum and minimum string
    return number

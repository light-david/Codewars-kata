#Defines the simple_multiplication function
def simple_multiplication(number) :
    #Checks if number is even or odd
    if number // 2 == number / 2:
        num = number * 8
    else:
        num = number * 9
    #Returns num
    return num

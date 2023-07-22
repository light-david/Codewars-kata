#Defines square_digits method
def square_digits(num):
    #Converts integer to string
    string_num = str(num)
    output = ''
    for digit in string_num:
        #Converts and squares the num 
        squared_string = int(digit) ** 2
        #Concatenates and converts the integer
        output += str(squared_string)
    #Converts and returns num
    return int(output)

#Defines fake_bin function and takes one argument
def fake_bin(x):
    #Converts digits greater than 5 to 1 and less than 5 to 0
    binary_string = ''.join(['1' if int(digit) >= 5 else '0' for digit in str(x)])
    #Return the converted value
    return binary_string
    pass

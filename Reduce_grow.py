#Defines grow method
def grow(arr):
    #Assigns output to 1
    output = 1
    for digit in arr:
        #Multiplies the elements of arr
        output *= digit
    #Returns output
    return output

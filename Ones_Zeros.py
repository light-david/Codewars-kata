#Defines binary_array_to_number method
def binary_array_to_number(arr):
        #Declares result
        result = 0
        #Iterates through the array
        for digit in arr:
            result = result * 2 + digit
        #Returns the result
        return result

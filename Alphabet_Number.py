#Defines alphabet_position and takes an argument
def alphabet_position(text):
    result = ""
    #Loops over the argument
    for letter in text.lower():
        #Checks if it is an alphabet
        if letter.isalpha():
            result += str(ord(letter) - 96) + " "
    #Returns result
    return result[:-1]

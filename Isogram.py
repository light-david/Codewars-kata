#Defines is_isogram function and takes one argument
def is_isogram(string):
    #Converts the argument into lowercase
    string = string.lower()
    #Store the unique characters in the string
    char = set(string)
    #Returns True or False
    return len(char) == len(string)

#Using a for loop
#Defines is_isogram function and takes one argument
def is_isogram(string):
    #Converts the argument into lowercase
    string = string.lower()
    #Creates a dictionary to store the occurence of each characters
    store_character = {}
    #Loops through the converted argument
    for char in string:
        #Checks if a character is repeated
        if char in store_character:
            #Returns false
            return False
        else:
            #Sets the character count to 1
            store_character[char] = 1
    #Returns True
    return True

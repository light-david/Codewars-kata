#Defines get_count function and takes one argument
def get_count(sentence):
    #Creates a list with all the vowels 
    vowels = ['a','e','i','o','u']
    count = 0
    #Loops through the taken argument
    for char in sentence:
        #Checks if char is in vowels
        if char in vowels:
            #Increases the value of count
            count += 1
    #Returns count
    return count

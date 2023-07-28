#Defines duplicate_encode method and accepts one argument
def duplicate_encode(word):
    #Converts word to lowercase
    word = word.lower()
    #Creates an ampty string
    result = ''
    #Iterates through the wprd
    for char in word:
        #Checks if the word appears more than once
        if word.count(char) == 1:
            #Appends ( if the word appears once
            result += '('
        else:
            #Appends ) if the word appears once more than once
            result += ')'
    #Returns the string
    return result

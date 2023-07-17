#Defines the function string_to_array and take one argument
def string_to_array(s):
  #Creates and empty list
    words = []
  #Checks if s is an empty string and appends s
    if s == '':
        words.append(s)
  #Splits the string into an array
    else:
        words = s.split()
  #returns words
    return words

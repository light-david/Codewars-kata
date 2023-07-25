#Defines the find_needle method
def find_needle(haystack):
    #Finds the position of needle in the list
    index = haystack.index('needle')
    #Returns the position of the needle
    return f'found the needle at position {index}'

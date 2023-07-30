#Defines solution method and takes two argument
def solution(text, ending):
    #Returns True if ending is in text
    return text.endswith(ending)

##""""""""Alternative function to solution""""""""

#Defines solution method and takes two arguments
def solution(text, ending):
    #Checks if the last elements of text is ending
    if text[-len(ending):] == ending:
        return True
    return False

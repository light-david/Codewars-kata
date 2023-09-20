#defines reverse_words function and takes one parameter
def reverse_words(s):
    #Splits the strings in the sentence
    words = s.split()
    #Reverses the splited words
    reversed_words = words[::-1]
    #Joins the reversed strings together
    reversed_string = ' '.join(reversed_words)
    #Returns the reversed sentence
    return reversed_string

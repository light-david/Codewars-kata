#Defines variance method and takes one argument
def variance(words):
    #Finds the length of each word and stores it in a list
    lengths = [len(word) for word in words]
    #Mean of the list of word length
    mean = sum(lengths) / len(lengths)
    #Sum of the suqare of the difference between each word length and mean
    square_diffs = [(length - mean) ** 2 for length in lengths]
    #Divides the sum of the total sum of words
    variance = sum(square_diffs) / len(words)
    #Returns variance
    return round(variance, 4)

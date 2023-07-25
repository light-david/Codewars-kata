#Defines pattern method and accepts an argument
def pattern(n):
    #Checks if n is lower than 1
    if n < 1:
        #Returns empty string
        return ""
    #Declares patterns as empty string
    patterns = ""
    #Loops through the given value
    for i in range(1, n + 1):
        #Iterates the argument
        patterns += str(i) * i + "\n"
    #Return the pattern
    return patterns[:-1]

#Defines number function and takes one argument
def number(lines):
    #Creates an empty list
    numbered_lines = []
    #Loops through the given argument
    for i, line in enumerate(lines):
        #Appends the given argument
        numbered_lines.append(f"{i+1}: {line}")
    #Returns the list
    return numbered_lines

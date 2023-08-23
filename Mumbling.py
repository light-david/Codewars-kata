def accum(s):
    #Iterates each character of the string with the index
    #Concatenate the uppercase version of c with i copies of lowercase version of c
    #Put them together using the join function and - as the separator
    result = '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
    return result

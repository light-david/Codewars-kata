def parse_float(input):
    try:
        #Checks if input is list
        if isinstance(input, list):
            #Joins the elements
            input = ''.join(input)        
        #Returns the parse as a float
        return float(input)
    except ValueError:
        #Returns None if parsed is not float
        return None
    #Returns None
    return None

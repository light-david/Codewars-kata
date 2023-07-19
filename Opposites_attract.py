#Defines lovefunc method and takes in two argument
def lovefunc( flower1, flower2 ):
    #Checks if flower1 is equal to flower 2 
    if flower1 % 2 == 0 and flower2 % 2 != 0:
        return True
    elif flower1 % 2 != 0 and flower2 % 2 == 0:
        return True
    #Returns False
    return False

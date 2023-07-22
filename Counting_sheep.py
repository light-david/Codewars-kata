#Defines count_sheep function
def count_sheeps(sheep):
    #Declares i
    i = 0
    for present in sheep:
        if present:
            i += 1
    return i

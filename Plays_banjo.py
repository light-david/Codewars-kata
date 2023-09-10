#Defines a function and takes a parameter
def are_you_playing_banjo(name):
    #Checks if the argument starts with r
    if name[0].lower() == 'r':
        return name + " plays banjo"
    return name + " does not play banjo"

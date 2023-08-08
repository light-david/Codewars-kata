#Defines set_alarm method and takes two argument
def set_alarm(employed, vacation):
    #Checks if employed is True and vacation is False
    if employed and not vacation:
        return True
    #Else returns False
    return False

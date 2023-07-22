#Defines desceding method
def descending_order(num):
    #Converts num to a string, sorts and reverse num
    new = ''.join(sorted(str(num), reverse = True))
    #Convert num to integer
    new = int(new)
    #Returns new
    return new

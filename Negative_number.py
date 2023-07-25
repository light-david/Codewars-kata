#Defines make_negative method and takes one argument
def make_negative( number ):
    #Concatenates the taken argument
    negative_number = "-" + str(number)
    #Checks if the argument is negative
    if number == -abs(number):
        return number
    #Returns negative_number as an integer
    return int(negative_number)

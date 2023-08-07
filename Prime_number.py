#Define is_prime function and takes one argument
def is_prime(num):
    #Checks if num is less than or equals to 1
    if num <= 1:
        #Returns False
        return False
    #Loops through all possible integers from 2 to the suqare root of num
    for i in range(2, int(num ** 0.5) + 1):
        #Checks if there is a remainder when num is divided by the iterator
        if num % i == 0:
            #Returns False
            return False
    #Returns True
    return True

#Defines a function and takes one parameter
def count_positives_sum_negatives(arr):
    #Checks if the given argument is empty
    if arr is None or len(arr) == 0:
        return []
    
    count_positives = 0
    sum_negatives = 0
    
    #Iterates through the given argument
    for num in arr:
        #Checks if the iterator is positive
        if num > 0:
            count_positives += 1
        #Checks if the iterator is negative
        elif num < 0:
            sum_negatives += num
    
    #Returns the length of the positive number and the sum of the negative number
    return [count_positives, sum_negatives]

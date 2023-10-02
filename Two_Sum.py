def two_sum(numbers, target):
	# Create a dictionary to store the complement of each number
    complements = {}

    for i, num in enumerate(numbers):
        complement = target - num
        # If the complement is in the dictionary, return the indices
        if complement in complements:
            return (complements[complement], i)
        # Store the index of the current number as the value in the dictionary
        complements[num] = i

    # Return an empty list if no solution is found
    return []
    #n = len(numbers)
    #for i in range(n):
        #for j in range(i+1, n):
            #if numbers[i] + numbers[j] == target:
                #return [i,j]
    #return None

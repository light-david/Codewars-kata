#Defines the find_smallest_int function which takes one argument
def find_smallest_int(arr):
    for i in range (len(arr)):
        #Assigns the smallest element in the array to i
        i = min(arr)
        #Returns i
        return i

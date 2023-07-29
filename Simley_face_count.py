#Defines count_smileys function and takes one argument
def count_smileys(arr):
    #A list containing simley faces
    check1 = [':)', ':-)', ':~)', ':D', ':-D', ':~D']
    check2 = [';)', ';-)', ';~)', ';D', ';-D', ';~D']
    count = 0
    #Loops through arr
    for i in arr:
        #Checks if arr is in check1 or check2
        if i in check1 or i in check2:
            #Iterates through the loop
            count += 1
    #Returns number of simley faces
    return count

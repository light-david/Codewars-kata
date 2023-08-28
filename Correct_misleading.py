#Defines correct function and takes one parameter
def correct(s):
    #Uses the replace function
    s = s.replace('5','S')
    s = s.replace('0','O')
    s = s.replace('1','I')
    return s

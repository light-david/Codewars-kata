#Defines a function and takes one parameter
def human_cat_dog_years(human_years):
    #Checks if the taken argument is 1
    if human_years == 1:
        cat_years = 15
        dog_years = 15
    #Checks if the taken argument is 2
    elif human_years == 2:
        cat_years = 24
        dog_years = 24
    #Checks if the taken argument is greater than 2 
    else:
        cat_years = 24 + 4 * (human_years - 2)
        dog_years = 24 + 5 * (human_years - 2)
    return [human_years, cat_years, dog_years]

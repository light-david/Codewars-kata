#Defines the function zero_fuel which takes three argument
def zero_fuel(distance_to_pump, mpg, fuel_left):
    #Calculates the mileage left
    miles_left = mpg * fuel_left
    #Calculates the possiblity of reaching the pump
    drive_possible = distance_to_pump - miles_left
    #Checks if drive to pump is possible
    if drive_possible <= 0:
        return True
    return False

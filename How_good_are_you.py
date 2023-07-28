#Defines better_than_average method and takes two argument
def better_than_average(class_points, your_points):
    #Calculates the class average
    class_ave = sum(class_points) / len(class_points)
    #Returns False if your_points is less than class_ave
    return False if your_points < class_ave else True

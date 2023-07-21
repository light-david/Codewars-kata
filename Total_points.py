#Defines points method and takes one argument
def points(games):
    total_points = 0
    for results in games:
        x, y = results.split(':')
        if int(x) > int(y):
            total_points += 3
        elif int(x) == int(y):
            total_points += 1
    return total_points
    pass

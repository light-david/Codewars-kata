def twice_as_old(dad_years_old, son_years_old):
    #Subtracte dad age from son age
    age_diff = dad_years_old - son_years_old
    #Subtracte age difference from son age
    years_ago_twice = abs(age_diff - son_years_old)
    #Returns years_ago_twice
    return years_ago_twice

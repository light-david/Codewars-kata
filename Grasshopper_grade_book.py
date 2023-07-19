#Defines the get_grade function and takes three arguments
def get_grade(s1, s2, s3):
    # Code here
    ave_score = (s1 + s2 + s3) / 3
    if 90 <= ave_score <= 100:
        return "A"
    elif 80 <= ave_score < 90:
        return "B"
    elif 70 <= ave_score < 80:
        return "C"
    elif 60 <= ave_score < 70:
            return "D"
    return "F"

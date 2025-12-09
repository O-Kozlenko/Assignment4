def get_grade(score):
    if score>=90:
        return("A")
    elif score>=80:
        return("B")
    elif score>=70:
        return("C")
    elif score>=60:
        return("D")
    elif score<60:
        return("F")
    else:
        return("Error")
scores = [95, 45, 78, 82, 60]
for i in range(len(scores)):
    print(get_grade(scores[i]),end=' ')
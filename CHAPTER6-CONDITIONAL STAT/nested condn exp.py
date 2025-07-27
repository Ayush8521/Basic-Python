# Nested conditional statement to determine the grade based on the score

score = int(input("Enter your score: "))
if score >= 90:
    grade = "A"
else:
    if score >= 80:
        grade = "B"
    else:
        if score >= 70:
            grade = "C"
        else:
            if score >= 60:
                grade = "D"
            else:                                                
                grade = "F"
print("Your grade is", grade)
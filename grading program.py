student_scores={
    "harry":81,
    "tom":75,
    "jerry":65,
}
student_grades={}
for student in student_scores:
    score=student_scores[student]
    if score>90:
        student_grades[student]="outstanding"
    elif score>80:
        student_grades[student]="exceeds exception"
    elif score>70:
        student_grades[student]="acceptable"
    else:
        student_grades[student]="fail"
print(student_grades)

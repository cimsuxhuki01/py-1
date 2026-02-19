grades = {
    ("Amar","Math"): 2,
    ("Filan", "Physics"): 3.5,
    ("Hasan","Biology"): 5,
    ("Remzi","English"): 4
}

amar_math = grades[("Amar", "Math")]
print("Amari's grade in math is", amar_math)

grades[("Filan","Physics")] = 3
print(grades)

keys = list(grades.keys())

student, subject = keys[0]
print(student,"'s grade in", subject, " is ", amar_math)
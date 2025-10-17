def find_student_grades(students, grades, target_student):
    if target_student in students:
        index = students.index(target_student)
        return grades[index]
    else:
        return "Студент не найден"

students = ("Анна", "Борис", "Виктория", "Григорий")
grades = [85, 92, 78, 96]

print(find_student_grades(students, grades, "Виктория"))
print(find_student_grades(students, grades, "Борис"))
print(find_student_grades(students, grades, "Дмитрий"))
print(find_student_grades(students, grades, "Анна"))
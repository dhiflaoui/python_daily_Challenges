grades = {
    "Alice": 78,
    "Bob": 42,
    "Charlie": 65,
    "Diana": 49,
    "Eve": 90
}
def categorize_students(grades):
    print("student categorization:")
    for student, grade in grades.items():
        if grade >= 50:
            print(f"{student} passed with a grade of {grade}")
        else:
            print(f"{student} failed with a grade of {grade}")

categorize_students(grades)
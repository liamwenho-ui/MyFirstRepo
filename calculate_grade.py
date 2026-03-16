def calculate_grade(marks):
    total = 0
    for m in marks:
        total += m

    average = total / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    elif average >= 50:
        grade = "E"
    else:
        grade = "F"

    return average, grade


def print_report(name, marks):
    average, grade = calculate_grade(marks)
    print(f"\n--- Report for {name} ---")
    print(f"Marks: {marks}")
    print(f"Average: {average}")
    print(f"Grade: {grade}")
    print("-------------------------")


students = ["Liam", "Sarah"]

for student in students:
    print(f"Enter marks for ({student}):")
    marks = []

  
    for _ in range(3):
        while True:
            try:
                mark = float(input())
                marks.append(mark)
                break
            except ValueError:
                print("Please enter a number!")

    print_report(student, marks)



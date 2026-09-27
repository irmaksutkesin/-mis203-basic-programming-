total_scores = 0
student_count = 0 

while True:
    name = input("Enter student name (or q to quit): ")

    if name.lower() == 'q':
        break

    try:
        score = float(input("Enter score: "))
    except ValueError:
        print("Invalid score. Please enter a number between 0 and 100.")
        continue

    if score < 0 or score > 100:
        print("Invalid score. Please enter a number between 0 and 100.")
        continue

    if score >= 90:
        letter_grade = 'A'
    elif score >= 80:
        letter_grade = 'B'
    elif score >= 70:
        letter_grade = 'C'
    elif score >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'


    display_score = int(score) if score.is_integer() else score
    print(f"{name}: {display_score} -> {letter_grade}")

    total_scores += score 
    student_count += 1

if student_count > 0:
    average = total_scores / student_count
    print(f"Total students: {student_count}")
    print(f"Average score: {average:.2f}")
else:
    print("No students entered.")

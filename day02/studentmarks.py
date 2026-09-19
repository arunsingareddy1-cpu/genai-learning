# student marks.py
Marks = [{"Arun": 85}, {"Kumar": 90}, {"Reddy": 78}, {"Anji": 92}, {"Reddy": 88}]

def get_student_highest_marks(marks):
    highest_marks = 0
    student_name = ""
    
    for student in marks:
        for name, mark in student.items():
            if mark > highest_marks:
                highest_marks = mark
                student_name = name
                
    return student_name, highest_marks
student, marks = get_student_highest_marks(Marks)
print(f"The student with the highest marks is {student} with a score of {marks}.")

def get_student_lowest_marks(marks):
    lowest_marks = float('inf')
    student_name = ""
    
    for student in marks:
        for name, mark in student.items():
            if mark < lowest_marks:
                lowest_marks = mark
                student_name = name
                
    return student_name, lowest_marks
student, marks = get_student_lowest_marks(Marks)
print(f"The student with the lowest marks is {student} with a score of {marks}.")

def get_average_marks(marks):
    total_marks = 0
    num_students = len(marks)
    
    for student in marks:
        for mark in student.values():
            total_marks += mark
            
    average_marks = total_marks / num_students
    return average_marks
average = get_average_marks(Marks)
print(f"The average marks of the students is {average:.2f}.")

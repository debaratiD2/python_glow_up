student_records = {}

def add_student(name, age, courses):
    if name in student_records.keys():
        print(f"Student '{name}' already exists.")
    else:
        student_records[name] = {
            #"name" : name,
            "age" : age,
            "grades" : set(),
            "courses" : set(courses)
        }
        print(f"Student '{name}' added successfully.")

def add_grade(name, grade):
    if name not in student_records.keys():
        print(f"Student '{name}' not found.")
    else:
        student_records[name]["grades"].add(grade)
             
        print(f"Grade {grade} added for student '{name}'.")

def is_enrolled(name, course):
    if name not in student_records.keys():
        print(f"Student '{name}' not found.")
        return False
        
    if course in student_records[name]["courses"]:
        return True
    else:
        return False

def calculate_average_grade(name):
    if name not in student_records.keys():
        print(f"Student '{name}' not found.")
        return None
    else:
        grades = student_records[name]["grades"]
        if not grades:
            return 0
        else:
            avg = sum(grades) / len(grades)
            return avg

def list_students_by_course(course):
    enrolled_student = []
    for key,value in student_records.items():
        if course in value["courses"]:
            enrolled_student.append(key)
    return enrolled_student

def filter_top_students(threshold):
    top_students = []
    for key,value in student_records.items():
        avg_grade = calculate_average_grade(key)
        if avg_grade is not None and avg_grade >= threshold:
            top_students.append(key)
    return top_students


add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Diana", 95)
print(filter_top_students(80))  # Should return ["Alice", "Diana"]
print(filter_top_students(90))  # Should return ["Diana"]
print(filter_top_students(100))  # Should return an empty list
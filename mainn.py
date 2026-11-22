import json

next_roll_no = 101
students = []

pname = "STUDENT ANALYZER"

print(f"\nWelcome! To the {pname}\n")


def add_student():

    global next_roll_no

    name = input("Enter Student name : ").strip().title()
    while True:
        try:
            age = int(input("Enter age : "))
            if age > 0:
                break
            else:
                print("Age must ne greater than 0")
        except ValueError:
            print("Please enter valid number")
    course = input("Enter course : ").strip().upper()

    while True:
        try:
            semester = int(input("\nEnter semester : "))
            if semester >=1 and semester <=6:
                break
            else:
                print("Semester must be between 1 and 6")
        except ValueError:
            print("Please enter valid number.")

    print("\n------- Student Details -------\n")
    print("Roll number :",next_roll_no)
    print("Name       :", name)
    print("Age        :", age)
    print("Course     :", course)
    print("Semester   :", semester)

    while True:
        try:
            python = int(input("\nEnter PYTHON marks :"))
            if python >= 0 and python <= 100:
                break
            else:
                print("marks must be 0 between 100")
        except ValueError:
            print("Please enter valid number")

    while True:
        try:
            dbms = int(input("\nEnter DBMS marks :"))
            if dbms >= 0 and dbms <= 100:
                break
            else:
                print("marks must be 0 between 100")
        except ValueError:
            print("Please enter valid number")
    while True:
        try:
            computer = int(input("\nEnter Computer marks :"))
            if computer >= 0 and computer <= 100:
                break
            else:
                print("marks must be 0 between 100")
        except ValueError:
            print("Please enter valid number")


    total = python + dbms + computer
    percentage = total / 3

    if python < 35 or dbms < 35 or computer < 35:
        result = "Fail"
    elif percentage >= 75:
        result = "Excellent"
    elif percentage >= 60:
        result = "Very Good"
    elif percentage >= 50:
        result = "Good"
    else:
        result = "Pass"

    print("\n------- Student Marks -------\n")
    print("PYTHON     :", python)
    print("DBMS       :", dbms)
    print("Computer   :", computer)
    print("\nTotal      :", total)
    print("Percentage :", percentage)
    print("Result     :", result)

    student_record = {
        "roll_number":next_roll_no,
        "name":name,
        "age":age,
        "course":course,
        "semester":semester,
        "python":python,
        "dbms":dbms,
        "computer":computer,
        "total":total,
        "percentage":percentage,
        "result":result        
}

    students.append(student_record)

    print("\nStudent added successfully!")
    print("Total number of students :", len(students))
    next_roll_no += 1
    save_student()

def display_student():
    if len(students) == 0:
        print("No students data available")
    else:
        for student in students:
            print("\n-------------------------------")
            print("Roll number :",student["roll_number"])
            print("Name        :", student["name"])
            print("Age         :", student["age"])
            print("Course      :", student["course"])
            print("Python      :", student["python"])
            print("DBMS        :", student["dbms"])
            print("Computer    :", student["computer"])
            print("Total       :", student["total"])
            print("Percentage  :", student["percentage"])
            print("Result      :", student["result"])

def search_student():
    roll = input("Enter roll number :")

    for student in students:
        if student["roll_number"] == int(roll):
            print("\nStudent found")
            print("Roll Number:", student["roll_number"])
            print("Name:", student["name"])
            print("Course:", student["course"])
            print("Percentage:", student["percentage"])
            print("Result:", student["result"])
            return
    print("Student not found")

def delete_student():
    roll = int(input("Enter roll number for delete :"))

    for student in students:
        if student["roll_number"] == roll:
            students.remove(student)
            print("Student remove successfully")
            save_student()
            return
    print("Student not found")

def update_student():
    roll = int(input("Enter roll number to update: "))

    for student in students:
        if student["roll_number"] == roll:

            print("\nStudent found!")

            while True:
                try:
                    new_age = int(input("Enter new age: "))
                    if new_age > 0:
                        break
                    else:
                        print("Age must be greater than 0.")

                except ValueError:
                    print("Please enter a valid number.")

            new_course = input("Enter new course: ").strip().upper()
            while True:
                try:
                    new_semester = int(input("\nEnter semester : "))
                    if new_semester >=1 and new_semester <=6:
                        break
                    else:
                        print("Semester must be between 1 and 6")
                except ValueError:
                        print("Please enter valid number.")
            

            while True:
                try:
                    new_python = int(input("\nEnter PYTHON marks"))
                    if new_python >= 0 and new_python <= 100:
                        break
                    else:
                        print("marks must be 0 between 100")
                except ValueError:
                    print("Please enter valid number")

            while True:
                try:
                    new_dbms = int(input("\nEnter DBMS marks"))
                    if new_dbms >= 0 and new_dbms <= 100:
                        break
                    else:
                        print("marks must be 0 between 100")
                except ValueError:
                    print("Please enter valid number")
            while True:
                try:
                    new_computer = int(input("\nEnter Computer marks"))
                    if new_computer >= 0 and new_computer <= 100:
                        break
                    else:
                        print("marks must be 0 between 100")
                except ValueError:
                    print("Please enter valid number")

            total = new_python + new_dbms + new_computer
            percentage = total / 3

            if new_python < 35 or new_dbms < 35 or new_computer < 35:
                result = "Fail"
            elif percentage >= 75:
                result = "Excellent"
            elif percentage >= 60:
                result = "Very Good"
            elif percentage >= 50:
                result = "Good"
            else:
                result = "Pass"

            student["age"] = new_age
            student["course"] = new_course
            student["semester"] = new_semester
            student["python"] = new_python
            student["dbms"] = new_dbms
            student["computer"] = new_computer
            student["total"] = total
            student["percentage"] = percentage
            student["result"] = result

            print("Student updated successfully!")
            save_student()
            return

    print("Student not found.")

def student_analytics():

    if len(students) == 0:
        print("No student data available.")
        return

    total_percentage = 0
    python_total = 0
    dbms_total = 0
    computer_total = 0

    for student in students:
        total_percentage += student["percentage"]
        dbms_total += student['dbms']
        python_total += student['python']
        computer_total += student['computer']

    average = total_percentage / len(students)
    python_average = python_total / len(students)
    dbms_average = dbms_total / len(students)
    computer_average = computer_total / len(students)

    highest = max(students, key=lambda s: s["percentage"])
    lowest = min(students, key=lambda s: s["percentage"])
    python_topper = max(students,key=lambda s:s['python'])
    dbms_topper = max(students,key=lambda s:s['dbms'])
    computer_topper = max(students,key=lambda s:s['computer'])

    pass_count = 0
    fail_count = 0
    excellent_count = 0
    very_good_count = 0
    good_count = 0
    pass_grade_count = 0
    fail_grade_count = 0

    for student in students:
        if student["result"] == "Fail":
            fail_count += 1
        else:
            pass_count += 1

        pass_percentage = pass_count / len(students) * 100

        if student['percentage'] >= 75:
            excellent_count += 1
        elif student['percentage'] >= 60:
            very_good_count += 1
        elif student['percentage'] >= 50:
            good_count += 1
        elif student['percentage'] >= 35:
            pass_grade_count += 1
        else:
            fail_grade_count += 1

    print("\n------- Student Analytics -------")
    print("Total Students      :", len(students))
    print("Average Percentage  :", round(average, 2))
    print("Python Average      :",round(python_average,2))
    print("DBMS Average        :",round(dbms_average,2))
    print("Computer Average    :",round(computer_average,2))
    print(f"Python Topper name : {python_topper['name']} marks :{python_topper['python']}")
    print(f"DBMS Topper name : {dbms_topper['name']} marks :{dbms_topper['dbms']}")
    print(f"Computer Topper name : {computer_topper['name']} marks :{computer_topper['computer']}")
    print("Highest Percentage  :", highest["percentage"])
    print("Topper              :", highest["name"])
    print("Lowest Percentage   :", lowest["percentage"])
    print("Lowest Student      :", lowest["name"])
    print("Passed Students     :", pass_count)
    print("Pass Percentage     :",round(pass_percentage,2))
    print("Failed Students     :", fail_count)
    print("Excellent grade students :",excellent_count)
    print("Very good grade students :",very_good_count)
    print("Good count students :",good_count)
    print("Pass grade count students :",pass_grade_count)
    print("Fail grade count students :",fail_grade_count)

def save_student():
    try:
        with open("students.json",'w') as file:
            json.dump(students,file,indent=4)
        print("student data save successfully")
    except OSError:
        print("Unable to save check permissions or storage.")


def load_students():
    global students,next_roll_no

    try:
        with open("students.json",'r') as file:
            students = json.load(file)
        
        if len(students) > 0:
            next_roll_no = max(student["roll_number"] for student in students)+1

        print("student data load successfully")
    except FileNotFoundError:
        print("No previous student data found")

    except json.JSONDecodeError:
        print("Student data file is corrupted.")

def main_menu():
    while True:
        print("\n1. Add student")
        print("2. Display All student")
        print("3. Search student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Student Analytics")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_student()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            student_analytics()

        elif choice == "7":
            print("Thank you")
            break

        else:
            print("you choose wrong")

load_students()
main_menu()
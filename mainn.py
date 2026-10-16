students = []

pname = "STUDENT ANALYZER"

print("\n================================")
print(f"\t{pname}")
print("================================")
print(f"\nWelcome! To the {pname}\n")


def student_detail():

    name = input("Enter Student name : ").strip().title()
    age = int(input("Enter age : "))
    course = input("Enter course : ").strip().upper()
    semester = int(input("Enter semester : "))

    print("\n------- Student Details -------\n")
    print("Name       :", name)
    print("Age        :", age)
    print("Course     :", course)
    print("Semester   :", semester)

    python = int(input("\nEnter PYTHON marks : "))
    dbms = int(input("Enter DBMS marks : "))
    computer = int(input("Enter Computer marks : "))

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

    students.append([
        name, age, course, semester,
        python, dbms, computer,
        total, percentage, result
    ])

    print("\nStudent added successfully!")
    print("Total number of students :", len(students))


# Add students
student_detail()

another = input("\nDo you want to add another student? (yes/no) : ").lower()

while another == "yes":
    student_detail()
    another = input(
        "\nDo you want to add another student? (yes/no) : "
    ).lower()


# Average
if len(students) > 0:

    total_percentage = 0

    for student in students:
        total_percentage += student[8]

    average = total_percentage / len(students)

    print("\n================================")
    print("Average Percentage :", average)


    # Highest
    highest = students[0][8]
    highest_name = students[0][0]

    for student in students:
        if student[8] > highest:
            highest = student[8]
            highest_name = student[0]

    print("Highest Percentage :", highest)
    print("Highest Student    :", highest_name)


    # Lowest
    lowest = students[0][8]
    lowest_name = students[0][0]

    for student in students:
        if student[8] < lowest:
            lowest = student[8]
            lowest_name = student[0]

    print("Lowest Percentage  :", lowest)
    print("Lowest Student     :", lowest_name)


    # Pass / Fail Count
    pass_count = 0
    fail_count = 0

    for student in students:

        if student[9] == "Fail":
            fail_count += 1
        else:
            pass_count += 1

    print("Passed Students    :", pass_count)
    print("Failed Students    :", fail_count)


    # Search
    found = False

    search_std = input(
        "\nEnter student name for search : "
    ).strip().lower()

    for student in students:

        if search_std == student[0].lower():

            found = True

            print("\n------- Student Found -------")
            print("Name        :", student[0])
            print("Age         :", student[1])
            print("Course      :", student[2])
            print("Semester    :", student[3])
            print("Python      :", student[4])
            print("DBMS        :", student[5])
            print("Computer    :", student[6])
            print("Total       :", student[7])
            print("Percentage  :", student[8])
            print("Result      :", student[9])

            break

    if not found:
        print("No student found.")


    # Delete
    found = False

    delete_name = input(
        "\nEnter student name to delete : "
    ).strip().lower()

    for student in students:

        if delete_name == student[0].lower():

            found = True
            students.remove(student)

            print("Student deleted successfully.")
            break

    if not found:
        print("No student found.")


    # Update
    found = False

    update_name = input(
        "\nEnter student name to update : "
    ).strip().lower()

    for student in students:

        if update_name == student[0].lower():

            found = True

            new_age = int(input("Enter new age : "))
            student[1] = new_age

            new_course = input("Enter new course : ")
            student[2] = new_course

            new_semester = int(input("Enter new semester : "))
            student[3] = new_semester

            new_python = int(input("Enter new Python marks : "))
            student[4] = new_python

            new_dbms = int(input("Enter new DBMS marks : "))
            student[5] = new_dbms

            new_computer = int(input("Enter new Computer marks : "))
            student[6] = new_computer

            new_total = new_python + new_dbms + new_computer
            new_percentage = new_total / 3

            student[7] = new_total
            student[8] = new_percentage

            if (
                new_python < 35
                or new_dbms < 35
                or new_computer < 35
            ):
                new_result = "Fail"

            elif new_percentage >= 75:
                new_result = "Excellent"

            elif new_percentage >= 60:
                new_result = "Very Good"

            elif new_percentage >= 50:
                new_result = "Good"

            else:
                new_result = "Pass"

            student[9] = new_result

            print("Student updated successfully.")

            break

    if not found:
        print("No student found.")

else:
    print("No student data available.")

print("\n================================")
print("       PROGRAM FINISHED")
print("================================")
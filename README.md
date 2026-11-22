# Student Analyzer 2.0

## Project Overview

Student Analyzer 2.0 is a console-based student management and academic performance analysis application developed using Python.

It allows users to manage student records, calculate academic results, track student performance, and generate useful academic insights.

The application also supports automatic roll number generation and permanent data storage using JSON.

## Technologies Used

- Python 3
- JSON
- Visual Studio Code

## Key Features

### 1. Student Management
- Add new student records.
- Automatically generate unique roll numbers.
- Display all student records.
- Search students by roll number.
- Update student details and marks.
- Delete student records.

### 2. Marks Calculation
- Calculate total marks.
- Calculate percentage.
- Determine Pass or Fail status.
- Assign performance grades automatically.

### 3. Advanced Student Analytics
- Calculate overall average percentage.
- Calculate subject-wise average marks.
- Identify the overall topper.
- Find the student with the lowest percentage.
- Identify subject-wise toppers.
- Calculate pass and fail counts.
- Calculate overall pass percentage.
- Generate grade distribution.

### 4. Data Validation
- Validate student age.
- Validate semester.
- Validate subject marks (0–100).
- Handle invalid user inputs using exception handling.

### 5. Data Persistence
- Save student records in a JSON file.
- Automatically load previously saved records when the application starts.
- Maintain automatic roll number generation using existing records.
- Handle missing or corrupted JSON files.

### 6. Menu-Driven Interface
The application provides a menu to perform different student management and analytics operations.

## Grading Criteria

| Percentage | Grade |
|---|---|
| 75% and above | Excellent |
| 60% – below 75% | Very Good |
| 50% – below 60% | Good |
| 35% – below 50% | Pass |
| Any subject below 35 marks | Fail |

## Python Concepts Used

- Variables and Data Types
- Conditional Statements
- For and While Loops
- Functions
- Lists and Dictionaries
- String Methods
- List and Dictionary Operations
- Lambda Functions
- Built-in Functions (`len`, `max`, `min`, `round`)
- Exception Handling (`try-except`)
- JSON File Handling
- Modules and Imports
- Input Validation

## How to Run

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Make sure Python 3 is installed.
4. Open the terminal.
5. Run the following command:

```bash
python main.py
```

The application will automatically load previously saved student records from `students.json`, if available.

## Project Structure

```text
Student-analyzer/
│
├── main.py
├── students.json
└── README.md
```

Note: `students.json` is created when student data is saved for the first time.

## Future Improvements

- Export student reports to CSV or Excel.
- Add graphical charts for student performance.
- Develop a graphical user interface (GUI).
- Integrate a database for managing larger student records.

## Conclusion

This project helped me apply Core Python concepts in a practical application.

By developing Student Analyzer 2.0, I gained hands-on experience in student record management, data validation, file handling, exception handling, and academic performance analysis.
# 🎓 Student Grading System

A beginner-level Python command-line project that calculates a student's total marks, percentage, grade, and final pass/fail result based on marks in five subjects.

## 📌 Features

- Accepts the student's name.
- Takes marks in five subjects.
- Validates marks within the range of 0–100.
- Calculates total marks and percentage.
- Assigns grades based on percentage.
- Checks individual subject passing criteria.
- Displays a formatted result report.

## 🛠️ Technologies Used

- Python 3
- Command Line Interface (CLI)
- Variables and Data Types
- User Input (`input()`)
- Type Conversion (`float()`)
- Arithmetic Operators
- Conditional Statements (`if`, `elif`, `else`)
- String Formatting and Methods

## 📂 Project Structure

```text
02_student_grading_system/
│
├── main.py
└── README.md
```

## 📊 Grading Criteria

| Percentage | Grade |
|---|---|
| 90–100% | A+ |
| 80–below 90% | A |
| 70–below 80% | B |
| 60–below 70% | C |
| 50–below 60% | D |
| 40–below 50% | E |
| Below 40% | F |

**Passing Criteria:** A student must score at least 40 marks in every subject to pass. Failing even one subject results in an overall FAIL.

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Open a terminal in the project directory.
3. Run:

```bash
python main.py
```

## 🖥️ Subjects

The program accepts marks in these five subjects:

1. English
2. Mathematics
3. Physics
4. Chemistry
5. Computer Science

**Maximum Marks:** 500

## ⚠️ Input Validation

- Marks below 0 are rejected.
- Marks above 100 are rejected
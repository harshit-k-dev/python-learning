print("=" * 76)
print("STUDENT GRADING SYSTEM".center(76))
print("=" * 76)

student_name = input("\nEnter the student's name: ").strip()

print("\nEnter marks-")
english_marks = float(input("Enter English marks: ").strip())
maths_marks = float(input("Enter Maths marks: ").strip())
physics_marks = float(input("Enter Physics marks: ").strip())
chemistry_marks = float(input("Enter Chemistry marks: ").strip())
cs_marks = float(input("Enter Computer Science marks: ").strip())

# Validate marks between 0 and 100
if (english_marks < 0 or english_marks > 100) or \
   (maths_marks < 0 or maths_marks > 100) or \
   (physics_marks < 0 or physics_marks > 100) or \
   (chemistry_marks < 0 or chemistry_marks > 100) or \
   (cs_marks < 0 or cs_marks > 100):

    print("\nInvalid marks entered. Please enter marks between 0 and 100.")

else:
    # Total marks calculation
    total_marks = english_marks + maths_marks + physics_marks + chemistry_marks + cs_marks

    # Percentage calculation
    percentage = (total_marks / 500) * 100

    # Check pass/fail condition
    if english_marks >= 40 and maths_marks >= 40 and physics_marks >= 40 and chemistry_marks >= 40 and cs_marks >= 40:
        result = "PASS"

        # Grade calculation
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        elif percentage >= 40:
            grade = "E"
        else:
            grade = "F"

    else:
        result = "FAIL"
        grade = "F"

    # Display result
    print("\n" + "=" * 76)
    print("RESULT".center(76))
    print("=" * 76)

    print("\nStudent Name:", student_name)
    print("Total Marks:", total_marks, "/ 500")
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)
    print("Result:", result)

    print("=" * 76)
    
print("\n" + "=" * 76)
print("Thank you for using STUDENT GRADING SYSTEM!")
print("A Python CLI Project")
print("Developed by Harshit Pal | Python Learning Project")
print("Version: 1.0.0")
print("=" * 76)
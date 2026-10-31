# Level 1 (if statement)
# exer1
numcheck = int(input("Enter a Number: "))
if (numcheck > 0):
    print("Positive Number")

# exer2
userAge = int(input("Enter your age to check voting eligibility: "))
if (userAge >=18):
    print("Eligible to Vote")
    
# exer3
number = int(input("Enter a Number: "))
if (number %5 == 0):
    print("Divisible by 5")

# exer4
password = (input("Enter your Password: ")).lower().strip()
if (len(password) >= 8) and password.isalnum():
    print("Password Accepted")
    
# exer5
string = input("Enter a word or sentence: ")
if (string.isupper()):
    print("All Uppercase")
    
# level2 (if-else statements)
# exer6
number = int(input("Enter a Number: "))
if(number %2 == 0):
    print("Entered Number is Even.")
else:
    print("Entered Number is Odd.")
    
# exer7
number1 = int(input("Enter your Number: "))
if number1 >0:
    print("Number is Positive.")
else:
    print("Number is Zero or Negative.")
 
# exer8
age = int(input("Enter your Age: "))
if (age >=18):
    print("You can Vote.")
else:
    print("You can not Vote.")

# exer9
userName = input("Enter your USERNAME").strip()
if (userName.isalnum()):
    print("Valid Username.")
else:
    print("Invalid Username.")
    
# exer10
numdivide = int(input("Enter Number: "))
if(numdivide %3 == 0):
    print("Divisible by 3.")
else:
    print("Not divisible by 3.")

# level3 (if-elif-else statement)
# exer11
number = int(input("Enter a Number: "))
if (number >0):
    print("Number is Positive.")
elif (number == 0):
    print("Number is Zero.")
else:
    print("Number is Negative.")
    
# exer12
print("========================\nSTUDENT GRADING SYSTEM\n========================")
marks = int(input("Enter your Marks: "))
if (marks >=90 and marks <=100):
    print("Congratulations. You Obtained Grade A.")
elif (marks>=75 and marks<=89):
    print("Not bad. You obtained Grade B.")
elif (marks >= 50 and marks <= 74):
    print("Study Hard. You obtained Grade C.")
elif (marks >= 33 and marks <=49):
    print("Too Bad. You obtained Grade D.")
elif (marks >=0 and marks <=32):
    print("Failed.")
else:
    print("Invalid Marks")
    
# exer13
print("======================\nTEMPERATURE CLASSIFIER\n======================")
temperature = float(input("Enter Temperature: ").strip())
if (temperature <10):
    print("Weather: Cold")
elif (temperature >= 10 and temperature <=24):
    print("Weather: Moderate")
elif (temperature >= 25 and temperature <=34):
    print("Weather: Warm")
else:
    print("Weather: Hot")
    
# exer14
print("================\nSIMPLE CALCULATOR\n================")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1, 2, 3, 4): ").strip()

num1 = float(input("Enter first Number: "))
num2 = float(input("Enter Second Number: "))

if (choice == '4' or choice.lower() == 'divide') and num2 == 0:
    print("Error: Division by zero is undefined and not allowed.")
elif (choice == '1' or choice.lower()== "add"):
    print(f"Result: {num1} + {num2} = {num1 +num2}")
elif (choice == '2' or choice.lower()== "subtract"):
    print(f"Result: {num1} - {num2} = {num1 - num2}")
elif (choice == '3' or choice.lower()== "multiply"):
    print(f"Result: {num1} * {num2} = {num1 *num2}")
elif (choice == '4' or choice.lower()== "divide"):
    print(f"Result: {num1} / {num2} = {num1 /num2}")
    
else:
    print("Invalid Choice.")
    
# exer15
print("================\nDAY FINDER\n================")
weekDay = (input("Enter DAY number (1-7): ")).strip()
if (weekDay == '1'):
    print("Day: Monday")
elif (weekDay == '2'):
    print("Day: Tuesday")
elif (weekDay == '3'):
    print("Day: Wednesday")
elif (weekDay == '4'):
    print("Day: Thursday")
elif (weekDay == '5'):
    print("Day: Friday")
elif (weekDay == '6'):
    print("Day: Saturday")
elif (weekDay == '7'):
    print("Day: Sunday")
else:
    print("Invalid Day")
    
# exer16
print("================\nCHARACTER CLASSIFIER\n================")
character = input("Enter a single Character: ").strip()
if len(character) != 1:
    print("Error: Please enter exactly one character.")
else:
    if (character.isupper()):
        print("UpperCase")
    elif(character.islower()):
        print("Lowercase")
    elif(character.isdigit()):
        print("Digit")
    else:
        print("Special Character")

# Level 4 (Nested if-else)
# exer17
print("===============\nLOGIN AUTHENTICATION\n===============")
correct_username = "admin123"
correct_password = "SecurePassword7"

username_input = input("Enter username: ").strip()
if (username_input == correct_username):
    password_input = input("Enter password: ")
    
    if (password_input == correct_password):
        print("Login Successful!")
    else:
        print("Error: Incorrect Password.")
        
else:
    print("Error: Username not found.")

# exer18
print("===============\nSCHOLAR ELIGIBILITY CHECKER\n===============")

user_marks = float(input("Enter Student Marks: ").strip())
if user_marks >= 85:
    income = float(input("Enter annual family income (in Rs.): ").strip())
    if income <=300000:
        print("Status: Scholarship Eligible.")
    else:
        print("Status: Not Eligible (Income exceeds Rs. 300000.)")
else:
    print("Status: Not Eligible (Marks must be at least 85)")
    
    
# exer19
print("========================\nLARGEST OF THREE NUMBERS\n========================")

# Take three numbers as input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Use nested if-else to find the largest
if num1 >= num2:
    # If num1 is greater than or equal to num2, compare num1 with num3
    if num1 >= num3:
        largest = num1
    else:
        largest = num3
else:
    # If num1 is less than num2, compare num2 with num3
    if num2 >= num3:
        largest = num2
    else:
        largest = num3

print(f"The largest number is: {largest}")

# exer20
print("================\nLEAP YEAR CHECKER\n================")

user_input = int(input("Enter a Year (e.g. 2026: )"))
if (user_input % 100==0):
    if (user_input %400==0):
        print(user_input, "is a LEAP YEAR.")
    else:
        print(user_input, "is not a LEAP YEAR.")
else:
    if(user_input %4==0):
        print(user_input, "is a LEAP YEAR.")
    else:
        print(user_input, "is not a LEAP YEAR.")

# exer21
print("================\nATM WITHDRAWAL SYSTEM\n================")
account_balance = 10000.0
print("Current Balance: ",account_balance)

withdraw_amount = float(input("Enter amount to withdraw: "))

if withdraw_amount >0:
    
    if withdraw_amount %100 == 0:
        
     if withdraw_amount <= account_balance:
        remaining_balance = account_balance-withdraw_amount
        print("\nTRANSACTION SUCCESSFUL!")
        print("Please collect your cash: Rs.",withdraw_amount)
        print("Remaining Balance: ", remaining_balance)
     else:
        print("\nTRANSACTION DENIED: Insufficien Balance")
        
    else:
        print("TRANSACTION DENIED: Amount must be a multiple of 100 (e.g., 100, 200, 500, 1000)")
else:
    print("TRANSACTION DENIED: Please enter a valid amount greater than 0.")
    
# exer22
print("================\nCOLLEGE ADMISSION CHECKER\n================")
physics_marks = float(input("Enter Physics Marks: "))
chemistry_marks = float(input("Enter Chemistry Marks: "))
maths_marks = float(input("Enter Maths Marks: "))

if (physics_marks >= 40 and chemistry_marks >= 40 and maths_marks >= 40):
    
    total_marks = physics_marks + chemistry_marks + maths_marks
    print("Individual Subject Quakified! Total Marks:", total_marks)
    
    if total_marks >= 180:
        print("Admission Status: Provisionaly Accepted.")
    else:
        print("Admission Status: Rejected (Total Marks Must be Atleast 180.)")
else:
    print("Admission Status: Rejected (Score atleast 40 marks in each subject.)")
    print("Failed Criteria.")
    
# exer23
print("================\nTICKET PRICING SYSTEM\n================")

age = int(input("Enter Your Age: ").strip())

if age < 5:
    ticket_price = 0
    print("Ticket Price:", ticket_price)
    
elif age >= 5 and age <=17:
    ticket_price = 100
    print("Ticket Price:", ticket_price)

elif age >=18 and age <= 59:
    
    is_student = input("are you a Student? (yes/no)").strip().lower()
    
    if is_student == "yes":
        ticket_price = 150
        print("Ticket Price: Student Discount applied: NEW TICKET PRICE =", ticket_price)
    else:
        ticket_price = 200
        print("Ticket Price:", ticket_price)
else:
    ticket_price = 120
    print("Ticket Price:", ticket_price)
        
# exer24
print("================\nMULTI-LEVEL SECURITY SYSTEM\n================")

CORRECT_USERNAME = "harshit_M"
CORRECT_PASSWORD = "harshit@123"
CORRECT_OTP = "4465"

userName_input = input("Enter Username: ").strip()
if userName_input == CORRECT_USERNAME:
    print("USERNAME Verified\n")
    
    passWord_input = (input("Enter Password: ")).strip()
    if passWord_input == CORRECT_PASSWORD:
        print("Password Verified\n")
        otp_input = input("Enter 4-digit OTP: ").strip()
        if otp_input == CORRECT_OTP:
            print("================")
            print("ACCESS GRANTED")
            print("================")
        else:
            print(" Security Error: Invalid OTP verification failed. Access Denied.")
    else:
        print(" Security Error: Incorrect Password. Access Denied.")
else:
    print(" Security Error: Username not recognized. Access Denied.")
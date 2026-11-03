import sys
print("============================================================================")
str1 = ("SMART CALCULATOR")
print(str1.center(75))
print("============================================================================\n")

print("Available Operations:\n")
print(" + : Addition")
print(" - : Subtraction")
print(" * : Multiplication")
print(" / : Division")
print(" % : Modulus (Remainder)")
print(" ^ : Power")
print("============================================================================\n")

operation = input("Select an operation (+, -, *, /, %, ^): ").strip()

if operation not in ['+', '-', '*', '/', '%', '^']:
    print("Error: Invalid operation selected. Program terminated.")
    sys.exit()
    
# input and validation for numbers
num1_input = input("Enter the first number: ").strip()
if not num1_input.replace('.', '', 1).isdigit() and not (num1_input.startswith('-') and num1_input[1:].replace('.', '', 1).isdigit()):
    print("Error: Invalid input for the first number. Program terminated.")
    sys.exit()
num1 = float(num1_input)

num2_input = input("Enter the second number: ").strip()
if not num2_input.replace('.', '', 1).isdigit() and not (num2_input.startswith('-') and num2_input[1:].replace('.', '', 1).isdigit()):
    print("Error: Invalid input for the second number. Program terminated.")
    sys.exit()
num2 = float(num2_input)

print("============================================================================\n")

# perform calculation and error handling
if operation == '+':
    result = num1 + num2
    print("Result:", num1, "+", num2, "=", result)
elif operation == '-':
    result = num1 - num2
    print("Result:", num1, "-", num2, "=", result)
elif operation == '*':
    result = num1 * num2
    print("Result:", num1, "*", num2, "=", result)
elif operation == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed. Program terminated.")
        sys.exit()
    result = num1 / num2
    print("Result:", num1, "/", num2, "=", result)
elif operation == '%':
    if num2 == 0:
        print("Error: Modulus by zero is not allowed. Program terminated.")
        sys.exit()
    result = num1 % num2
    print("Result:", num1, "%", num2, "=", result)
elif operation == '^':
    result = num1 ** num2
    print("Result:", num1, "^", num2, "=", result)
print("\n============================================================================\n")
print("\n" + "=" * 76)
print("Thank you for using SMART CALCULATOR!")
print("A Python CLI Project")
print("Developed by Harshit Pal | Python Learning Project")
print("Version: 1.0.0")
print("=" * 76)
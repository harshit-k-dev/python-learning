# python exercise
# level 1 basic input
# exer 1
name = input("Enter your name: ")
print("Hello, ",name,"!")

# exer 2
age = int(input("Enter your age: "))
print("You are ",age," years old.")

# exer 3
city= input("Enter your city: ")
print("You live in ",city,".")

# exer4
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("Your full name is ",first_name," ",last_name,".")

# exer5
language = input("Enter your favorite programming language: ")
print("Your favorite programming language is ",language,".")

# level2 Input and Variables
# exer 6
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city name: ")
print("Your name is ",name,". You are ",age," years old and you live in ",city,".")

# exer7
a = int(float(input("Enter first number: ")))
b = int(float(input("Enter second number: ")))
print(a,b)

# exer8
num1 = int(float(input("Enter first number: ")))
num2 = int(float(input("Enter second number: ")))
print("Sum: ",num1+num2)


# exer9
num1 = int(float(input("Enter first number: ")))
num2 = int(float(input("Enter second number: ")))
print("Sum: ",num1+num2)
print("Difference: ",num1-num2)
print("Product: ",num1*num2)
print("Quotient: ",num1/num2)

# exer10
c = int(float(input("Enter length: ")))
d = int(float(input("Enter width: ")))
print("Area: ",c*d,"square units")

# level 3 input and data types
# exer 11
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(name)
print("Data Type: ",type(name))
print(age)
print("Data Type: ", type(age))

# exer 12
age = input("Enter your age: ")
age = int(age)
print(int(age), "Data Type: ", type(age))

# exer13
height = float(input("Enter your height in meters: "))
print(float(height), type(height))

# exer14
num2 = 9.7
num3 = 0.0002
print(float(num2+num3))

# exer15
temp = int(float(input("Enter temperature in celsius: ")))
temp1 = 9/5*temp+32
print("temperature in fahrenheit: ",temp1)

# level4 
# exer 16
a = input("Enter first number: ")
b = input("Enter second number: ")
print(a+b)
# it will not add instead it will print combining of both number as example
# 10 and 20 it will print 1020, instead of 30


# exer 17
a = int(float(input("Enter first number: ")))
b = int(float(input("Enter second number: ")))
print(a+b)

# exer 18
a = int(float(input("Enter first number: ")))
b = int(float(input("Enter second number: ")))
print("Sum: ", a+b)
print("Difference: ",a-b)
print("Product: ", a*b)
print("Quotient: ", a/b)

# exer19
a = input("Enter your name: ")
b = input("Enter Your City: ")

a, b = b, a
print(b)
print(a)


# exer20
name = input("Tell your name: ")
age = int(input("Tell your age: "))
city = input("Tell your city name: ")
height = float(input("Tell your height in meters: "))
language = input("Tell your favorite programming language: ")

print("======= STUDENT PROFILE =======")
print("Name: ",name)
print("Age: ",age)
print("City: ", city)
print("Height: ",height)
print("Learning: ", language)

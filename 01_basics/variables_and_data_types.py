# exercise for variables and data types
#  level 1-- Variables

# exer1-- create a variable named name and assigned name to it
name = "Harshit"
print(name)

# exer2--- create multiple variables named name, age, and city
name = "Harshit"
age = 16
city = "Orai"
print(name, age, city)

# exer3--- variable reassignment
name = "Harsh"
name = "Harshit" # answer is Harshit because the variable name was reassigned to "Harshit" 
print(name)


# exer4--- two variables 
first_name = "Harshit"
last_name = "Pal"
print(first_name)
print(last_name)

# exer5--- swap variables
a = 10
b = 20
a, b = b, a
print(a, b)

# level 2-- Basic Data types
# exer6--- identify the data type
name = "Harshit"
age = 16
height = 5.3
whether_you_like_python = True

print(type(name))
print(type(age))
print(type(height))
print(type(whether_you_like_python))

# exer7--- check the data type of the variable
name = "Harshit"
age = 16
weight = 47.6
am_i_a_student = True

print(name, "type is", type(name))
print(age, "type is", type(age))
print(weight, "type is", type(weight))
print(am_i_a_student, "type is", type(am_i_a_student))  

# exer8--- integer vs str
age = 18
age_text = "18"
print(age, "type is", type(age), age_text, "type is", type(age_text))

# because age is an integer and age_text is a string, they are of different data types.

# exer 9--- float
height = 1.75
print(height, "type is", type(height))

# exer 10--- boolean
is_student = True
print(is_student, "type is", type(is_student))

# false printed here because to understand both true and false values are boolean data types.
is_student = False
print(is_student, "type is", type(is_student))

# level 3-- Variables + Operations
# exer 11--- addition of two variables
a = 15
b = 25
print("Addition of a and b is:", a + b)

# exer 12--- Basic Calculator
a = 9997 
b = 6709
print("addition of a and b is-:" , a+b) #add
print("subtraction of a and b is-:" , a-b) #sub
print("multiplication of a and b is-:" , a*b) #mul              
print("division of a and b is-:" , a/b) #div

#  exer 13--- age calculation
birth_year = 2008
current_year = 2026
print("Your age is-:", current_year-birth_year) #age calculation

# exer 14--- String concatenation
first_name = "Harshit"
last_name = "Pal"
print("Full name is-:", first_name + " " + last_name) #string concatenation

# exer 15--- Different data types
name = "Harshit"
age = 18
height = 1.75
is_student = True

print("name=", name, ", age=", age, ", height=", height, ", is_student=", is_student) #different data types

print("type of name is", type(name))
print("type of age is", type(age))
print("type of height is", type(height))
print("type of is_student is", type(is_student))   

# level 4
# exer 16--- 
x = 10
x = 20
x = 30 

print(x)
# ans-30-expl- because the variable x was reassigned multiple times, and the last assignment was x = 30, so the final value of x is 30.

# exer 17--- same variable, different types
x = 10
x = "10"
x = 10.0
x = True

print(x)
print("type of x is", type(x))
# ans-True-expl- because the variable x was reassigned multiple times, and the last assignment was x = True, so the final value of x is True, and its data type is bool.

# exer 18--- variable refrences

a = 10
b = a
a = 20
print(a)
print(b)
# b does not become 20 because when we assign b = a, b gets the value of a at that moment, which is 10. Later, when we change a to 20, it does not affect b, so b remains 10.

# exer 19--- fixedcode
age = ("18")
age = int(age)

print(age + 2) 
print(type(age))


# exer20 --- mini profile

Name = "Harshit"
Age = 18
City = "Orai"
Height = 1.75
Student_status = True
Programming_language = "Python"

print("===== MY PROFILE =====")
print("Name:", Name)
print("Age:", Age)
print("City:", City)
print("Height:", Height, "m")
print("Student:", Student_status)
print("Learning:", Programming_language)
print("======================")
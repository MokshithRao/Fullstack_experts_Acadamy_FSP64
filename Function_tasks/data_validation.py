# Part 1 - Clean a User's Name
name = input("Enter your name: ")
print("Is valid name:", name.isalpha())

"""
Output:
Enter your name: john123
Is valid name: False

Enter your name: John
Is valid name: True

Enter your name: John Doe
Is valid name: False

Enter your name: John_Doe
Is valid name: False

Enter your name: JohnDoe
Is valid name: True
"""

# Part 2 - Phone Number Validator
phone = input("phone number: ")
print("Valid:",phone.isdigit())

"""
Output:
phone number: 9876543210
Valid: True

phone number: 98765abc10
Valid: False

phone number: 98765 43210
Valid: False

phone number: +919876543210
Valid: False

Explain why "9876543210" returns True but "+919876543210" returns False?
- Because "+919876543210" has "+" which is not a digit.
"""


# Part 3 - Student ID Validator
student_id = input("Enter student_id: ")
print("student_id: ", student_id.isalnum())


"""
Output:
Enter student_id: PYTHON2026
student_id:  True

Enter student_id: PYTHON_2026
student_id:  False

Enter student_id: PYTHON-2026
student_id:  False

Enter student_id: PYTHON 2026
student_id:  False

Why does isalnum() reject _, -, and spaces?
They are punctuations and isalnum only accepts alphanumeric characters means standard letters and decimal digits.
"""





# Part 4 - Password Validation
password = input("Enter password: ")
print("Password :", password)
print("All uppercase :", password.isupper())
print("All lowercase :", password.islower())
print("Alphanumeric :", password.isalnum())


"""
Output:
Password : Python123
All uppercase : False
All lowercase : False
Alphanumeric : True

Password : PYTHON
All uppercase : True
All lowercase : False
Alphanumeric : True

Password : python
All uppercase : False
All lowercase : True
Alphanumeric : True

Password : Python
All uppercase : False
All lowercase : False
Alphanumeric : True

Password : Python@123
All uppercase : False
All lowercase : False
Alphanumeric : False

Why does "Python".isupper() return False?
- Because "Python" contains both uppercase and lowercase letters.
- isupper() returns True only when all the letters are uppercase.

Why does "Python123".isalnum() return True?
- Because "Python123" contains only letters and numbers.
- isalnum() accepts alphabetic characters and numbers.
- It does not accept spaces or special characters like @, _, or -.
"""


# # Part 5 - Username Case Checker
username = input("Enter username: ")
print("Username :", username)
print("Lowercase :", username.islower())


"""
Output:
Enter username: john_doe
Username : john_doe
Lowercase : True

Enter username: JOHN_DOE
Username : JOHN_DOE
Lowercase : False

Enter username: John_Doe
Username : John_Doe
Lowercase : False

Enter username: john123
Username : john123
Lowercase : True
"""


# Part 6 - Student Name Format Checker
student_name = input("Enter student name: ")
print("Student Name :", student_name)
print("Correct Format :", student_name.istitle())

if student_name.istitle() == False:
    print("Corrected Name :", student_name.title())


"""
Output:
Enter student name: John Doe
Student Name : John Doe
Correct Format : True

Enter student name: john doe
Student Name : john doe
Correct Format : False
Corrected Name : John Doe

Enter student name: JOHN DOE
Student Name : JOHN DOE
Correct Format : False
Corrected Name : John Doe

Enter student name: John doe
Student Name : John doe
Correct Format : False
Corrected Name : John Doe

Enter student name: John123
Student Name : John123
Correct Format : True
"""


# Part 7 - Numeric Data Detector
value1 = "12345"
value2 = "12.50"
value3 = "-500"
value4 = "123abc"
value5 = "■"

print("12345 :", value1.isnumeric())
print("12.50 :", value2.isnumeric())
print("-500 :", value3.isnumeric())
print("123abc :", value4.isnumeric())
print("■ : ", value5.isnumeric())

"""
Output:
12345 : True
12.50 : False
-500 : False
123abc : False
■ :  False

Compare isdigit() and isnumeric():

"123".isdigit() : True
"123".isnumeric() : True

"■".isdigit() : False
"■".isnumeric() : False
"""


# Part 8 - Empty Input Detector
address = input("Enter address: ")
print('Address received : "' + address + '"')
print("Contains only spaces :", address.isspace())


"""
Output:
Enter address:  
Address received : " "
Contains only spaces : True

Enter address: hello
Address received : "hello"
Contains only spaces : False

Enter address:  hello 
Address received : " hello "
Contains only spaces : False

Enter address:
Address received : ""
Contains only spaces : False


Why does "".isspace() return False?
- Because an empty string does not contain any whitespace characters.
- isspace() returns True only when the string contains at least one whitespace character
"""



# Part 9 - Process an Address
address = input("Enter address: ")
result = address.partition(":")
print("Address parts :", result)


"""
Output:
Enter address: Hyderabad:Telangana:India
Address parts : ('Hyderabad', ':', 'Telangana:India')

Enter address: Hyderabad:Telangana
Address parts : ('Hyderabad', ':', 'Telangana')

Enter address: Hyderabad
Address parts : ('Hyderabad', '', '')
"""



# Part 10 - Parse API Data
data = "name:John Doe,email:john@gmail.com,city:Hyderabad"

first_part = data.partition(",")
name_data = first_part[0]
remaining_data = first_part[2]

name = name_data.partition(":")
print("Key :", name[0])
print("Value :", name[2])


second_part = remaining_data.partition(",")
email_data = second_part[0]
remaining_data = second_part[2]

email = email_data.partition(":")
print("Key :", email[0])
print("Value :", email[2])


city = remaining_data.partition(":")
print("Key :", city[0])
print("Value :", city[2])


"""
Output:
Key : name
Value : John Doe
Key : email
Value : john@gmail.com
Key : city
Value : Hyderabad
"""


# Part 11 - Clean Imported Data Using replace()

phone = input("Enter phone number: ")
clean_phone = phone.replace("-", "")
print("Original phone :", phone)
print("Clean phone :", clean_phone)

phone_number =  "987 654 3210"
clean_phone = phone.replace(" ", "")
print("Original phone :", phone_number)
print("Clean phone :", clean_phone)

"""
Output:
Enter phone number: 987-654-3210
Original phone : 987-654-3210
Clean phone : 9876543210

phone number: 987 654 3210
Original phone : 987 654 3210
Clean phone : 9876543210
"""


# Part 12 - Clean User Input
name = input("Enter name: ")
clean_name = name.replace("@", " ")
print("Original name :", name)
print("Clean name :", clean_name)


"""
Output:
Enter name: John@Doe
Original name : John@Doe
Clean name : John Doe


Now try "Python#Full#Stack" and convert it to Python Full Stack.
"""

name = input("Enter name: ")
clean_name = name.replace("#", " ")
print("Original name :", name)
print("Clean name :", clean_name)

"""
Output:
Enter name: Python#Full#Stack
Original name : Python#Full#Stack
Clean name : Python Full Stack
"""


# Part 13 - Generate a URL Slug
course = input("Enter course name: ")
url = course.lower()
url = url.replace(" ", "-")

print("Course Name :", course)
print("URL Slug :", url)


"""
Output:
Enter course name: Python Full Stack Development
Course Name : Python Full Stack Development
URL Slug : python-full-stack-development
"""


# Part 14 - Process Multi-Line Data
students = """John Doe
Alice Smith
Rahul Kumar
Sneha Reddy"""

records = students.splitlines()
print("Student Records:")

for record in records:
    print(record)


"""
Output:
Student Records:
John Doe
Alice Smith
Rahul Kumar
Sneha Reddy
"""

students = """John Doe
Alice Smith
Rahul Kumar
Sneha Reddy"""

records = students.splitlines()
result = " | ".join(records)
print("Joined Data :", result)

"""
Output:
Joined Data : John Doe | Alice Smith | Rahul Kumar | Sneha Reddy
"""


# Part 15 - Course Description Processor
description = """Python
Django
React
MySQL
AWS"""

modules = description.splitlines()
result = " -> ".join(modules)
print("Course Modules :", result)

"""
Output:
Course Modules : Python -> Django -> React -> MySQL -> AWS
"""


# Part 16 - Student Registration Number
number = input("Enter registration number: ")
registration_number = number.zfill(5)
print("Registration Number :", registration_number)


"""
Output:
Enter registration number: 1
Registration Number : 00001

Enter registration number: 42
Registration Number : 00042

Enter registration number: 123
Registration Number : 00123

Enter registration number: 9999
Registration Number : 09999

Enter registration number: 12345
Registration Number : 12345
"""


# Part 17 - Generate Employee ID
employee_number = input("Enter employee number: ")
employee_id = "EMP" + employee_number.zfill(5)
print("Employee ID :", employee_id)


"""
Output:
Enter employee number: 42
Employee ID : EMP00042
"""


# Part 18 - Build a Terminal Dashboard
print("CODEHUB DASHBOARD".center(30, "*"))

"""
Output:
*******CODEHUB DASHBOARD*******
"""


# Part 19 - Create a Student Table
print("Name".ljust(20), "City".ljust(15), "Course")
print("-" * 50)

print("John Doe".ljust(20), "Hyderabad".ljust(15), "Python")
print("Alice Smith".ljust(20), "Chennai".ljust(15), "React")
print("Rahul Kumar".ljust(20), "Delhi".ljust(15), "Django")


"""
Output:
Name                 City            Course
--------------------------------------------------
John Doe             Hyderabad       Python
Alice Smith          Chennai         React
Rahul Kumar          Delhi           Django
"""


# Part 20 - Student Score Display
score1 = "5"
score2 = "42"
score3 = "87"
score4 = "100"

print("Student Score")
print("-------------")

print(score1.zfill(3))
print(score2.zfill(3))
print(score3.zfill(3))
print(score4.zfill(3))


"""
Output:
Student Score
-------------
005
042
087
100
"""



# Final Challenge - CodeHub Data Processing System
name = input("Enter name: ")
email = input("Enter email: ")
phone = input("Enter phone: ")
student_id = input("Enter student ID: ")
course = input("Enter course: ")
address = input("Enter address: ")
password = input("Enter password: ")
registration_number = input("Enter registration number: ")


# 1. Name Validation
name_without_space = name.replace(" ", "")
name_valid = name_without_space.isalpha()
name_title = name.istitle()

# 2. Phone Validation
clean_phone = phone.replace("-", "")
clean_phone = clean_phone.replace(" ", "")
phone_valid = clean_phone.isdigit()


# 3. Student ID Validation
student_id_valid = student_id.isalnum()


# 4. Password Analysis
password_upper = password.isupper()
password_lower = password.islower()
password_alphanumeric = password.isalnum()


# 5. Address Processing
address_parts = address.partition(":")
address_city = address_parts[0]
address_separator = address_parts[1]
address_remaining = address_parts[2]


# 6. Data Cleaning
clean_name = name.replace("@", " ")
clean_email = email.replace(" ", "")


# 7. Course Processing
course_modules = course.splitlines()
course_result = " -> ".join(course_modules)


# 8. Registration Number
registration_id = registration_number.zfill(5)
student_registration = "STU" + registration_id


# 9. Dashboard
print()
print("*" * 50)
print("CODEHUB DASHBOARD".center(50))
print("*" * 50)

print("STUDENT INFORMATION".center(50))
print("-" * 50)

print("Name :".ljust(20), clean_name)
print("Email :".ljust(20), clean_email)
print("Phone :".ljust(20), clean_phone)
print("Student ID :".ljust(20), student_id)
print("Course :".ljust(20), course_result)
print("Registration No. :".ljust(20), student_registration)

print("-" * 50)

print("VALIDATION".center(50))
print("-" * 50)

print("Name Valid :".ljust(20), name_valid)
print("Phone Valid :".ljust(20), phone_valid)
print("Student ID Valid :".ljust(20), student_id_valid)
print("Password AlphaNum :".ljust(20), password_alphanumeric)
print("Name Title Case :".ljust(20), name_title)

print("-" * 50)

print("PROFILE STATUS".center(50))
print("-" * 50)

print("REGISTRATION SUCCESSFUL".center(50))

print("*" * 50)


"""
Sample Input:

Enter name: John Doe
Enter email: john.doe@gmail.com
Enter phone: 987-654-3210
Enter student ID: PYTHON2026
Enter course:  Python Full Stack
Enter address: Hyderabad:Telangana:India
Enter password: Python123
Enter registration number: 42


Output:

**************************************************
                 CODEHUB DASHBOARD
**************************************************
              STUDENT INFORMATION
--------------------------------------------------
Name :               John Doe
Email :              john.doe@gmail.com
Phone :              9876543210
Student ID :         PYTHON2026
Course :             Python Full Stack
Registration No. :   STU00042
--------------------------------------------------
                  VALIDATION
--------------------------------------------------
Name Valid :         True
Phone Valid :        True
Student ID Valid :   True
Password AlphaNum :  True
Name Title Case :    True
--------------------------------------------------
                PROFILE STATUS
--------------------------------------------------
             REGISTRATION SUCCESSFUL
**************************************************
"""
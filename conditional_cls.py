Sanjeev-Python-8:Am
Weekdays
30-07-2020 Class Recordings & Files
Sanjeev Classes March
•
10:08 AM (Edited 1:37 PM)

conditional_cls.py
Text

Verify to Continue
https://vimeo.com/442960759/5c375f0c4d
Class comments



# Conditional Statements-- Those statements that will be executed based on certain conditions...


# a = 34

# print(a,"is greaterthan 50")


# if statement
# if - else statements
# if-elif-else statements
# nested statements



# if statements -- 

# block of code

"""
if condition:
    statements
"""

# if condition{
#     print("hello")
#     print(4+5)
# }


# a = 56

# print(a,"is greaterthan 50")

# input() - it will help you to take user input...
# input() - what ever type of values you have passed by default it will take it ass string only....
# a = input("Enter a values:")
# eval -- it will convert your string into respective data type
# a = eval(input("Enter a values:"))
# print(type(a))
# type -- will return the type of value...
# if a>50:
#     print(a,"is greaterthan 50")
#     print("hello")

# print("python")

# commenting -- if any line starts with #...
# """ """ -- wil be used for multiple line commenting..

"""
Comments
Comments
"""


# if-else statements
"""
if condition:
    satements
else:
    satements
"""
# a = eval(input("Enter a values:"))
# if a>50:
#     print(a,"is greaterthan 50")
#     print("hello")
# else:
#     print(a,"is lessthan 50")


# username = input("Enter username:-")
# password = input("Enter Password:-")


# nested conditionals-- writing if conditions inside other conditionals... 

# if statement should be declared mandatory before declaring else statements...
# if username=="rajesh":
#     print("Username Matched")
#     print()
#     password = input("Enter Password:-")
#     if password == "123456":
#         print("Userlogged In")
#     else:
#         print("Not Logged In! Password Mismatch")
# else:
#     print("Username doesnot matched")


# ATM Transactions -- Task



# if - elif -else statements

# this is used for check mutliple conditions and execute respective statements...
# we can declare n numer of elif... But before elif if should be declared mandatory...
"""
if condition:
    statements
elif condition:
    statements
elif condition:
    statements
else:
    statements
"""


percentage = eval(input("Enter your percentage:-"))

# print(percentage)


# a = eval(input("Enter Your Value:-"))

if percentage>=70:
    print("Distinction")
elif percentage>=60 and percentage<70:
    print("First class")
elif percentage>=50 and percentage<60:
    print("Second Class")
elif percentage>=35 and percentage < 50:
    print("Just Pass")
else:
    print("Failed")
conditional_cls.py
Displaying conditional_cls.py.
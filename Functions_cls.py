# # Function - Set of Statements which perform a specific task...
#     # Which can be executed n number of times...
#     # code reusuability.....

# a=4
# b=7

# # print(a+b)
# # print(a-b)
# # print(a*b)
# # print(a/b)

# a=87
# b=23

# # print(a+b)
# # print(a-b)
# # print(a*b)
# # print(a/b)

# a=23
# b=2

# # print(a+b)
# # print(a-b)
# # print(a*b)
# # print(a/b)


# # def -- it is the keyword for defining the function...

# """
# def function-name():
#     statements
# """

# a=4
# b=7
# # print("Hi")

# # Defining or Declaring the functions
# def arithmetic():
#     print(a)
#     print(b)
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)

# # print("Bye")

# # Calling a function
# arithmetic()

# print(a)
# print(b)

# a=87
# b=23

# arithmetic()
# a=23
# b=2

# arithmetic()

# Passing Arguments to the functions:--
    # 1) Positional Arguments
    # 2) Default Arguments
    # 3) Keyword Arguments
    # 4) Arbitrary Positional Arguments
    # 5) Arbitrary Keywprd Arguments.

# 1) Positional Arguments:- Assigning the value to the arguments based on position...

# def arithmetic(a,b):
#     print("a value:",a)
#     print("b value:",b)
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)

# arithmetic(7,4)

# arithmetic(23,2)

# arithmetic(12,5)

# print(a)
# print(b)

# def user_data(name,location):
#     print("{} is located at {} city".format(name,location))

# user_data("Suresh","Hyderabad")

# # user_data("Ramesh","Bangalore")

# # user_data("Bangalore","Ramesh")
# user_data("Venkatesh","vizag")

# Positional arguments will check no.of value we are passing to the function.It has to be same as no.of arguemts..

# 2) Default Arguments: - Passing a default value to a argument at the function declaration.
#   if the value is passed to that argument at the function call, that value will  be taken in consideration..
#   if the value is not passed to that argument at the function call, default valur we have provided will be taken it conserdation..
#   


# def user_data(name,location="delhi"):
#     print("{} is located at {} city".format(name,location))

# user_data("subash","hyderabad")

# user_data("venkat")


# Function Default Argument syntax is once a default argument is declared after that all should be declard as default arguments only....
# def user_data(name,location="delhi",state="Delhi"):
#     print("{} is located at {} city in {} state".format(name,location,state))

# user_data("rajesh","hyderabad","Telangana")


# user_data("Suresh","Ranchi")
# user_data("krishna")

# user_data("mahesh")


# 3)Keyword Arguments: - Delaring the value to the arguments at the function-call based on the name of argument..

# Function Keyword Argument syntax is once a keyword argument is declared after that all should be declard as keyword arguments only at function call.......

# def user_data(name,location,state):
#     print("{} is located at {} city in {} state".format(name,location,state))
#     print(location)

# user_data("Hyderabad","Ramesh","Telanagana")

# location = input("Enter the Location:-")
# user_data(location=input("Enter the Location:-"),name="Ramesh",state="Telanagana")

# print(location)
# user_data(location="Hyderabad",name="Ramesh",state="Telanagana")

# user_data("Suresh",state="delhi",location="Delhi")

# user_data("suresh",name="rajesh",state="Maharastra",location="Mumbai")

# 4) Arbitrary Positional Arguments:- Passing n number of arguments to the function..

# * -- used for representing the arbirary arguments..

# def month_trans(*trans):
#     print(trans) # tuple
#     amount = sum(trans)
#     # amount = 0
#     # print(type(trans))
#     # for j in trans:
#     #     amount = amount+j
#     print("You have done {} transaction and {} is debited from your account".format(len(trans),amount))

# month_trans(4500,5500,3500)

# month_trans(250,1500,2500,8500)

# month_trans(5000,8000,12000,1500,2300)


# 5) Arbitrary Keyword Arguments:- 

# ** -- for arbitrary keyword arguments...

# def month_trans(account_number,**trans):
#     print(trans)
#     amount = 0
#     for j in trans:
#         amount = amount + trans[j]
#     # print(amount)
#     print("You have done transactions in {} months and {} is debited from the account. with {} account number".format(len(trans),amount,account_number))

# month_trans(account_number=737383837388,jan = 24500,sep=23600,mar=56700)

# month_trans(apr=12700,nov=23600,dec=4375,aug=14670)

# month_trans(feb=32560,may=8765,june=8279,july=7876,oct=9875)


# return -- it will store the output and send that output to function call.

# return should be the last statement inside the function..
# def add(a,b):
#     # print(a+b)
#     return a+b
#     # print("hello")


# # print(add(3,4))
# def sub(c):
#     return add(3,4)-c

# print(sub(5))

# global and local varibales

# global - Those which can be accessed any where thorugh out the program..
# local - Those which can be accesed only inside that particular function...

a=45 # global varibale
# name = "rajesh"
def add(b,a): # local variales..
    global name # to make a local varibale into global variable..
    name = "venkatesh"
    print((b)) 
    print(a)

add(5,6)
print(a)
# print(b)

print(name)
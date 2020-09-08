atm_name = input("Enter the Bank Name:-")
account = input("Enter Account Type:-")
pin  = eval(input("Enter ATM PIN:-"))

if atm_name=="HDFC":
    print("\nBank Name Matched")
    print()
 
    if account == "Current":
        print("Account Type Matched \n")
        print()
    else:
            print("Incorrect Account Type")
    
    else:
    print("Incorrect PIN Entered")

atm_name = input("Enter Name of the Bank ATM:-")
password = input("Enter ATM PIN:-")
withdraw = eval(input("Enter Amount:-"))

if atm_name=="SBH":
    print("ATM Bank Name Matched\n")
    print()
    
    if password == "12345":
        print("Account Accessed Successfully\n")
        if withdraw <= 15000:
            print("Collect the Amount")
        else:
            print("Entered Denominations not available")
    else:
        print("Access Denied! Incorrect PIN")

else:
    print("ATM Bank Name Doesnot matched")
Sanjeev-Python-8:Am
Weekdays
30-07-2020 Class Recordings & Files
Sanjeev Classes March
�
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
username = input("Enter username:-")
password = input("Enter Password:-")

if username=="rajesh":
    print("Username Matched")
    print()
    password = input("Enter Password:-")
    if password == "123456":
        print("Userlogged In")
    else:
        print("Not Logged In! Password Mismatch")
else:
    print("Username doesnot matched")"""
a = eval(input("Enter a Value:"))
if a>100:
    print(a, "is greather than 100")
    print("good")
else:
    print(a, "is lessthan 100")
    """
"""
if username=="sbh":
    print("Bank Name Matched")
    pin = input("Enter PIN:-")
    if pin == "12345"
        print("PIN is Correct")
    else:
        print("Not Entered PIN! PIN Mismatched")
else:
    print("PIN doesnot matched")
    """

#if username=="rajesh":
 #   print("Username Matched")
 #   password = input("Enter Password")
 #   if password == "12345":
 #      print("Userlogged in")
 #   else: 
 #      print("Not Logged In! Password Mismatch")
#else:
#    print("Username doesnot matched")

# if statement should be declared mandatory before declaring else statements...
if username=="rajesh":
    print("Username Matched")
    print()
    password = input("Enter Password:-")
    if password == "123456":
        print("Userlogged In")
    else:
        print("Not Logged In! Password Mismatch")
else:
    print("Username doesnot matched")
"""
attendance = eval(input("Days of Present:-"))
if attendance>30:
    print("Full Present")
elif attendance>=25 and attendance<27:
    print("Partial Present")
elif attendance>=15:
    print("Average Present")
else:
    print("Detained!! lesstan 50 persantage days present")
"""
Grade = int(input("Enter percentage of Marks:-"))

if
a=45
b=45
lists_cls.py
11-08-2020 Recording & Files
# Lists -- Sequence of multiple values seperated with comma(,) declared inside [ ]...
    # Ex:- a = [23,45.67,'python'] 

a = [23,45.67,'python',34,"django"] 

# print(type(a))


# Accessing elments inside the list  -- Indexing.

# indexing will start from zero..
# Indexing is represented in [ ]..

# print(a[0])

# print(a[4])

# print(a[6])


a = [23,45.67,'python',34,"django"]

# print(a[1:5])

# print(a[2:10])

# negative indexing:- Accessing the elements in negative order... 

# negative indexing will start from -1...

# print(a[-3])
# # print(a[-5])

# print(a[-1:-4])

# print(a[-1:-4:-1])

# Mutuable --- We can make changes inside the list...

a = [23,45.67,'python',34,"django"]

# print(a)
# a[1] = 76

# print(a)

# a[1:4] = [78,"datascience",67.43]
# a[1:5] = [78,"datascience",67.43,"devops"]

# print(a)

# del a[2]

# print(a)


# Basic Operations : -
    # Concatenation(+):- Adding of 2 or more list and making it as single list..
    # Repetition(*):- Adding same list elments multiple number of times inside the list..


# print([1,2,3]+[7,8,9])

# print([1,2,3]*4)

# Lists Methods:-
# print(dir(list))

# adding methods
    # append
    # extend
    # insert

# removing elments
    # remove
    # pop
    # clear

# accessing
    # index,count,
# alterating
    # sort,reverese
# Loop -- Iteration  --- Executing same line of code multiple numbers of times..

a=[4,19,45,36]

# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])


# while loop
# for loop


# while loop:- While check the condition and will execute the statements n number of times. till condition becomes false...

"""
while condition:
    satements
"""

# a=eval(input("Enter a value:-"))

# username = input("Enter username:")

# while a==50:
#     print(a,"is greaterthan 50")
#     a = a-1

# while username=="ramesh":
#     print(username,"is the username")
# print("Python")



# for loop -- It will based on a sequence....


"""
for element in sequence:
    statements
"""

# a="python programming"
# a=[34,"python","56","django"]
# for j in a:
#     print(j)


# nested loopign --  looping inside other loopings...
# a=["python",56,"django"]
# for j in a:
#     print(j)
#     if type(j)==int:
#         print("not satisfied")
#     else:
#         for i in j:
#             print(i)


# range -- 

# print(list(range(2,20)))

# for j in range(2,30):
#     print(j)

# a = eval(input("Enter a value:"))
# b = eval(input("Enter b value:"))
# for j in range(a,b):
#     print(j)


# print(help(str))

# for j in range(2,20):
#     print(j,end="-")


# for j in range(20):
#     print(j,end=" ")

# for j in range(2,20,3):
#     print(j,end=" ")


# for j in range(20,2,-1):
#     print(j,end=" ")


# controlflow statements:-
    # break -- Will stop all the next iteration and will go outside of the loop..
    # continue -- will pause current iteration and will directly go to next iteration...
    # pass -- Its is just for synatx purpose...


#print(list(range(4,50)))

# a=eval(input("Enter a value:-"))

#username = input("Enter username:")

#while a==50:
 #   print(a,"is greaterthan 50")
  #  a = a-1

#while username=="ramesh":
 #   print(username,"is the username")
#print("Python")

#a=["6472267282","4787428787","6536521","77646271","6732773787"]

# len -- will return the length of the value..
#for j in a:
 #   if len(j) != 10:
  #      break
   #     print(j,"not satisfied")
   
   # else:
   #     print(j)

#print("hello")

#print(list(range(4,50)))

#a=("6472267282","4787428787","6536521","77646271","6732773787")

# len -- will return the length of the value..
#for j in a:
 #   if len(j) != 10:
        #break
  #      print(j,"not satisfied")
   
   # else:
    
    #    print(j)

#print("hello")

a=("12333535","1233353512333535","1233353512333535","123335351233353512333535","12333535")

for k in a:
    if len(k) != 15:
        print(k,"Invalid Numbers")
    else:
        print(k)

print("Success")# # Loop -- Iteration  --- Executing same line of code multiple numbers of times..

# a=[4,19,45,36]

# # print(a[0])
# # print(a[1])
# # print(a[2])
# # print(a[3])


# # while loop
# # for loop


# # while loop:- While check the condition and will execute the statements n number of times. till condition becomes false...

# """
# while condition:
#     satements
# """

# # a=eval(input("Enter a value:-"))

# # username = input("Enter username:")

# # while a==50:
# #     print(a,"is greaterthan 50")
# #     a = a-1

# # while username=="ramesh":
# #     print(username,"is the username")
# # print("Python")



# # for loop -- It will based on a sequence....


# """
# for element in sequence:
#     statements
# """

# # a="python programming"
# # a=[34,"python","56","django"]
# # for j in a:
# #     print(j)


# # nested loopign --  looping inside other loopings...
# # a=["python",56,"django"]
# # for j in a:
# #     print(j)
# #     if type(j)==int:
# #         print("not satisfied")
# #     else:
# #         for i in j:
# #             print(i)


# # range -- 

# # print(list(range(2,20)))

# # for j in range(2,30):
# #     print(j)

# # a = eval(input("Enter a value:"))
# # b = eval(input("Enter b value:"))
# # for j in range(a,b):
# #     print(j)


# # print(help(str))

# # for j in range(2,20):
# #     print(j,end="-")


# # for j in range(20):
# #     print(j,end=" ")

# # for j in range(2,20,3):
# #     print(j,end=" ")


# # for j in range(20,2,-1):
# #     print(j,end=" ")


# # controlflow statements:-
#     # break -- Will stop all the next iteration and will go outside of the loop..
#     # continue -- will pause current iteration and will directly go to next iteration...
#     # pass -- Its is just for synatx purpose...


# a=["6472267282","4787428787","6536521","77646271","6732773787"]

# # len -- will return the length of the value..
# for j in a:
#     if len(j) != 10:
#         break
#     else:
#         print(j)
#     print("hello")

# print("outside")

a=["6472267282","4787428787","6536521","77646271","6732773787"]

# for j in a:
#     if len(j) != 10:
#         continue
#     else:
#         print(j)
#     print("hello")
#     b=["1"]
#     print(a+b)

# print("outside")

# for j in a:
#     if len(j) != 10:
#         pass
#     else:
#         print(j)
#     print("hello")
#     b=["1"]
#     print(a+b)

# print("outside")

# a = 1
# while a < 4:
#     pin = input("Enter pin number:-")
#     if pin == '1234':
#         account_type = input("Enter your account type:")
#         if account_type == "saving":
#             amount = int(input("enter amount:-"))
#             print("{} is debited from your account".format(amount))
#             break
#         else:
#             print("account type not matched,Try Again!")
#             a=a+1
#     else:
#         a=a+1
#         if a != 4:
#             print("Pin not matched,Try Again!")
# else:
#     print("Tried More no.of time Account Blocked for 24 hours!")
Sanjeev-Python-8:Am
Weekdays
24-07-2020 Class Recordings & Files
Sanjeev Classes March
•
10:00 AM

operators_cls.py
Text
Class comments


24-07-2020 Class Recordings & Files
# Operators -- Its a symbol which perform an operation between 2 or more operands....

# 3+5+6

# List of Operators:-
    # 1) Arithemtic Operators(+,-,*,/,//,%,**)
    # 2) Relational Operators(==,!=,>,<,>=,<=)
    # 3) Logical Operators(and,or,not)
    # 4) Assignment Operators(=,+=,-=,*=,/=)
    # 5) Bitwise Operators(Bitwise And(&),Bitwise OR(|),Bitwise XOR(^),Left Shift(<<),Right Shift(>>),Bitwise NOT(~))
    # 6) Membership Operators(in,not in)
    # 7) Identity Operators(is,is not)


# 1) Arithmetic Operators

# print(34+67)
# print(45-35)
# print(12*12)


# print(17/3)

# print(17//3)

# print(16/3) = 5.6667

# print(16//3) = 5

# print(17%3)  =2


# 3) 17 (5
#    15
# ---------
#     2

# 158%3 - 2
# 3) 158 (52
#    15
# --------
#     08
#      6
# ---------
#      2

# 3*5
# 3**5 == 3*3*3*3*3 -- 343


# 2)Relational Operators -- Output for relational operators will be True or False only..

a=45
b=78

# print(a==b) # False
# print(a != b) # False

# print(a>b) # False
# print(a<b) # True
# print(a>=b) # False
# print(a<=b) # True

# 3) Logical Operators(and,or,not):-


# A            B          A and B          A or B        not(A)        not(A and B)
# ------------------------------------------------------------------------------------
# T            F             F               T             F              T 
# F            T             F               T             T              T 
# T            T             T               T             F              F 
# F            F             F               F             T              T 




a=45
b=67


# print(a>50 and b<100)
# #      F   and  T    - F


# print(a>50 or b<100)

# #     F    or  T    -  T 


# print(not(a>50 and b<100))



# username = "gsanjeev"
# password = "123456"


# print('gsaneev'==username and '123456'==password)

# print('gsaneev'==username or '123456'==password)


# 4) Assignment Operators(=,+=,-=,*=)

# a=45
# # a=a+15
# print(a)
# print(id(a))
# a+=15 # a=a+15
# print(a)
# print(id(a))
# a-=15
# print(a)
# print(id(a))
# a*=5

# print(a)

# a/=5

# print(a)

# 45

# Python datatypes:-
    # 1) Numbers --- Numeric values or decimal values...(int,floating)
        # a=45, b=6.7
    # 2) Strings --- Sequennce of charcaters which are declared inside " "....
        # a = "hyderabad123"
    # 3) Lists ---  Sequence of multiple values which are declared inside [ ] seperated with comma(,)..
        # a = [4,"python",5.6,"hyderabad"]
    # 4) Tuples --- Sequence of multiple values which are declared inside ( ) seperated with comma(,)..
        # a = (4,"python",5.6,"hyderabad")
    # 5) Dictionaries  -- Sequence of key:value pairs which are declared inside { } seperated with comma(,)..
        # a = {'email' : 'gsanjeev@gmail.com','password':'123456'}  
    # 6) Sets -- Frozensets.. -- Sequence of multiple values which are declared inside { } seperated with comma(,)..
        # a = {4,5.6,'python','django',4}


# a = {4,5.6,'python','django',4}

# a = (4,5.6,'python','django',4)
# # print(a)

# # Lists,Dictionaries,Sets --- Mutuable
# # Tuples,Strings,Numbers --- Immutuable

# a= [4,5.6,'python','django',4]

# 6) Membership Operators(in, not in):- These are  used just for checking whether the value or elments in present in thee varibales..

# a="Python is a programming langauge"


# print("Python" in a)

# print("Python" not in a)


# a=[56,"python","django","csv",65]

# print(56 in a)

# print("csv" not in a)

# 7) Identity Operators(is,is not):- These are used to check the identity(memory allocation) if the values...


# a=45
# b=45

# print(a is b)
# print(a == b)


# a="python"
# b="python"

# print(a is b)
# print(a == b)

# a=(1,2,3)
# b=(1,2,3)

# print(a is b)
# print(a == b)

# a=[1,2,3]
# b=[1,2,3]

# print(id(a))
# print(id(b))
# print(a == b)
# print(a is b)

# print(a is not b)


# 5) Bitwise Operators:- Binary Level Operations

# A     B     A & B      A | B        A ^ B(XOR)    
# -----------------------------------------------
# 0     1       0         1            1
# 1     0       0         1            1
# 1     1       1         1            0
# 0     0       0         0            0


a = 17

b = 19


# print(a&b)

# print(a|b)
# print(a^b)

# 17  -  10001
# 19  -  10011
# -------------
    #  10001 - 17
    #  10011 - 19
    #  00010 - 2
        
# 17 -- 10001
# 2)17(
#   2)8 - 1
#     2)4 - 0
#       2)2 - 0
#         1 - 0

# 73 -- 
# 19 - 10011
# 2)19(
#    2)9 - 1
#      2)4 - 1
#        2)2 - 0
#          1 - 0


#            512 256 128  64  32 16  8 4 2 1
#                          1   0  0  1 0 1 0
                                # 0  0 0 1 0 --- 2

                        # 1   0  0   1 0 0 1 --- 73

# 1001010 - 74

# 2)74(
#   2)37 - 0
#      2)18 - 1
#        2)9  - 0
#          2)4 - 1
#            2)2 - 0
#              1 - 0

# print(bin(74))

# print(int('1001010',2))

# Bitwise NOT(~)


Sanjeev-Python-8:Am
Weekdays
08-08-2020
Sanjeev Classes March
•
Aug 10

strings_cls.py
Text
Class comments



# Strings - Sequence of charcaters or numbers or special symbols declared inside ' ' or " " or """ """..

# a="python programming"
# b='python programming'
# c="""python programming"""

# print(a)
# print(b)
# print(c)

# print(type(a))
# print(type(b))
# print(type(c))

a="python is a programming langauge python is used for web development" # single line string.

b='python is a programming langauge python is used for web development' # single line string

c="""python is a programming langauge   
python is used for web development""" # multiline string

# print(a)
# print(b)
# print(c)

# " " or '' -- Used for declaring single line string only...
# """ """ -- used for declaring multiple line string


# python' programming
# a= "python' programming"
# a= 'python" programming'
# print(a)


a="python programming language"


# Accessing values inside the string -- Indexing...

# Indexing will start from 0...
# indexing is represented in [ ]..

# print(a[10])

# print(a[17])

# print(a[30]) # will through an error.(because index value giving is more than the length of string...)

# a="python programming language"

# print(a[7:14])

# print(a[4:12])

# a=['python','django',"datascience"]

# b=0
# for j in a:
#     if j=="django":
#         print("django is present at ",b)
#         break
#     else:
#         b=b+1

# print(a[b])


# negative indexing:- Access elments inside the string in reverse order..

# negative indexing will be starting from -1..

# a="python programming language"

# print(a[-3])

# print(a[-25])

# print(a[-14:-25:-1])


# Basic Operations:
    # Concatenation(+): Adding of multiple strings and giving it as a single string...
    # Repetition(*): Repeating the same element specified no.of times...

# print(3+4)

# print("Python"+" Django")

# print("Django"+"Framewwork"+"webdevelopment")

# print(4*3)

# print("Python"*5)

# print("Python"+" Django"+3)

# Concatenation will be performed on similar datatypes values only....

# a="Python"


# Datatypes are devided into 2 types..
    # Immutable datatypes -- Those we cannot make chnages once declared...(number,strings,tuples)
    # Mutuable datatypes -- Those Datatypes we can make changes..(Lists,Dictionaries,Sets..)


# String is an immutable datatypes. So, i cannot make the chnages once delcared...

# a="Python"

# print(id(a))
# # print(a[0])

# # a[0] = 'p'

# del a[0]
# a="python"

# print(id(a))

# String Methods:-
# a="Python"
# print(dir(a))

# startswith(),endswith(),isalpha(),isalnum(),isdigit(),isspace(),isupper(),islower(),lower()
# upper(),title(),capitalize(),swapcase(),count,index,find,rindex,rfind,split(),rsplit()
# strip(),rstrip(),lstrip(),zfill,join, format()


# startswith() -- Will check Whether the string is starting with what we specified..(True/False)


# a="Django is a framework"

# print(a.startswith('D'))

# # print(a.startswith("Djng")) # False

# print(a.startswith("d"))

# endswith() -- Will check Whether the string is ending with what we specified..(True/False)

# a="rajesh@gmail.com"

# print(a.endswith("gmail.com"))

# print(a.endswith("M"))


# isalpha() -- It is used to check whether all the values inside the string are alphabets only...

# a="PythonProgramming"

# print(a.isalpha())

# isalnum() -- It is used to check whether all the values inside the string are alphanumeric(alpabets or numbers) only...

# a="Python 123"

# print(a.isalnum())

# isdigit() -- It is used to check whether all the values inside the string are numbers only...

# a="518 502"

# print(a.isdigit())


# isspace() -- Will check whther complete string is a space itself...

# a=" "

# print(a.isspace())

# islower() -- It will check all the alphabets inside the string are in lower case or not... 

# a="Python is a langauge456"

# print(a.islower())


# isupper() -- It will check all the alphabets inside the string are in upper case or not...

# a="Python is a langauge456"

# a="PYTHON 123"
# print(a.isupper())

# lower() -- It will convert all the upper alphabets into lower case inside the string..

# a="PYTHON is a Language"

# print(a.lower())


# upper() -- It will convert all the lower alphabets into upper case inside the string..

# a="PYTHON is a Language"

# print(a.upper())

# title() -- Will convert Each word starting charcater into uppercase inside the string..


# a="Python is a programming language"

# print(a.title())

# capitalize() -- Will convert only starting charcater of string into uppercase and remaining into lowercase inside the string..
# a="python is a proGRamming Language"

# print(a.capitalize())


# swapcase() -- Will convert alphabest upper into lower and vice versa inside the string..

# a="python is a proGRamming Language"

# print(a.swapcase())

# count -- Will return how many times a substring is repeated inside the string..

# a="Python is a programming languange"

# print(a.count('a'))

# print(a.count('Python'))

# print(a.count('python'))

# index -- Will return the index value of the specified element inside the string..

# if the element occured multiple times. it will defaultly considr the first occurence of element itself..

# if the element we are trying is not present inside the string index method will through an error..


a="Python is a programming language"

# print(a.index('g'))

# print(a.index('g',16))

# print(a.index('g',23))


# steps
# a="Python is a programming language"
# input() -- to which elment has to search...

# Which occurence index values:-

# index_value = 0
# for -- on string:
# if condition


# print(a.index('z'))

# # print(a.find('g'))

# if a.find('z') == -1:
#     print("no elments present")
# print("Hello")


# find() -- Same as index method...
# only when elments is not present index will  give an error but find will give -1..

# # print(a.find('g'))

# if a.find('z') == -1:
#     print("no elments present")



# rindex() -- Same like indexing, but will do it from right side to leftside..

# a="Python is a programming language"

# # print(a.rindex('g',0,26))

# print(a.rindex('z',0,26))

# # print(a.rfind('g',0,26))

# print(a.rfind('z'))

# split(),rsplit()
# strip(),rstrip(),lstrip(),zfill,join, format()


# split() -- It will split your string into multiple string based on space by default.. if you specify the 
# the argument it will split based on the arguments...
# a="python is a programing language"

# print(a.split())

# print(a.split('a',2))


# rsplit() -- same as split() but will perform from right to left...
# print(a.rsplit('a',2))
# print(a.rsplit('a'))



# strip() -- it will remove the escape sequences at the starting and ending of the string...

# \n - newline
# \t - tabspace
# a="\n\tpython\n\tprogramming\n"

# # print(a)

# # print(a.strip())

# # print(a.lstrip())

# print(a.rstrip())


# zfill() -- filling up with zeros....

# a="776772376426772829"

# print(a.zfill(15))


# join() --  It is used for joining any special things to each and every elments inside the string..except the first element..

a="python"


# print("-".join(a))

# print("@".join(a))

# a=["python", "is","a","programming","language"]

# print("$".join(a))

# format() -- Dynamic way of creating a format based on valuess..

# print("Hi Ramesh,Your order with order Id 6722672 is successfully palced and will be delivered by 13-08-2022")

# print("Hi Ramesh,Your order with order Id 6427772789 is successfully palced and will be delivered by 23-08-2022")

# {} -- 

# name = input("Enter your name:-")
# order_id = input("Enter your Order Id:-")
# delivery_by = input("Enter Delivery date:-")
# print("Hi {},Your order with order Id {} is successfully palced and will be delivered by {}".format(name,order_id,delivery_by))

# print("Hi {},Your order with order Id {} is successfully palced and will be delivered by {}".format(order_id,delivery_by,name))

# print("Hi {2},Your order with order Id {0} is successfully palced and will be delivered by {1}".format(order_id,delivery_by,name))


strings_cls.py
Displaying strings_cls.py.atm_name = input("Enter the Bank Name:-")
account = input("Enter Account Type:-")
pin  = eval(input("Enter ATM PIN:-"))

if atm_name=="HDFC":
    print("\nBank Name Matched")
    print()
 
    if account == "Current":
        print("Account Type Matched \n")
        print()
    else:
            print("Incorrect Account Type")
    
    else:
    print("Incorrect PIN Entered")

atm_name = input("Enter Name of the Bank ATM:-")
password = input("Enter ATM PIN:-")
withdraw = eval(input("Enter Amount:-"))

if atm_name=="SBH":
    print("ATM Bank Name Matched\n")
    print()
    
    if password == "12345":
        print("Account Accessed Successfully\n")
        if withdraw <= 15000:
            print("Collect the Amount")
        else:
            print("Entered Denominations not available")
    else:
        print("Access Denied! Incorrect PIN")

else:
    print("ATM Bank Name Doesnot matched")
Sanjeev-Python-8:Am
Weekdays
30-07-2020 Class Recordings & Files
Sanjeev Classes March
�
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
username = input("Enter username:-")
password = input("Enter Password:-")

if username=="rajesh":
    print("Username Matched")
    print()
    password = input("Enter Password:-")
    if password == "123456":
        print("Userlogged In")
    else:
        print("Not Logged In! Password Mismatch")
else:
    print("Username doesnot matched")"""
a = eval(input("Enter a Value:"))
if a>100:
    print(a, "is greather than 100")
    print("good")
else:
    print(a, "is lessthan 100")
    """
"""
if username=="sbh":
    print("Bank Name Matched")
    pin = input("Enter PIN:-")
    if pin == "12345"
        print("PIN is Correct")
    else:
        print("Not Entered PIN! PIN Mismatched")
else:
    print("PIN doesnot matched")
    """

#if username=="rajesh":
 #   print("Username Matched")
 #   password = input("Enter Password")
 #   if password == "12345":
 #      print("Userlogged in")
 #   else: 
 #      print("Not Logged In! Password Mismatch")
#else:
#    print("Username doesnot matched")

# if statement should be declared mandatory before declaring else statements...
if username=="rajesh":
    print("Username Matched")
    print()
    password = input("Enter Password:-")
    if password == "123456":
        print("Userlogged In")
    else:
        print("Not Logged In! Password Mismatch")
else:
    print("Username doesnot matched")
"""
attendance = eval(input("Days of Present:-"))
if attendance>30:
    print("Full Present")
elif attendance>=25 and attendance<27:
    print("Partial Present")
elif attendance>=15:
    print("Average Present")
else:
    print("Detained!! lesstan 50 persantage days present")
"""
Grade = int(input("Enter percentage of Marks:-"))

if
a=45
b=45
lists_cls.py
11-08-2020 Recording & Files
# Lists -- Sequence of multiple values seperated with comma(,) declared inside [ ]...
    # Ex:- a = [23,45.67,'python'] 

a = [23,45.67,'python',34,"django"] 

# print(type(a))


# Accessing elments inside the list  -- Indexing.

# indexing will start from zero..
# Indexing is represented in [ ]..

# print(a[0])

# print(a[4])

# print(a[6])


a = [23,45.67,'python',34,"django"]

# print(a[1:5])

# print(a[2:10])

# negative indexing:- Accessing the elements in negative order... 

# negative indexing will start from -1...

# print(a[-3])
# # print(a[-5])

# print(a[-1:-4])

# print(a[-1:-4:-1])

# Mutuable --- We can make changes inside the list...

a = [23,45.67,'python',34,"django"]

# print(a)
# a[1] = 76

# print(a)

# a[1:4] = [78,"datascience",67.43]
# a[1:5] = [78,"datascience",67.43,"devops"]

# print(a)

# del a[2]

# print(a)


# Basic Operations : -
    # Concatenation(+):- Adding of 2 or more list and making it as single list..
    # Repetition(*):- Adding same list elments multiple number of times inside the list..


# print([1,2,3]+[7,8,9])

# print([1,2,3]*4)

# Lists Methods:-
# print(dir(list))

# adding methods
    # append
    # extend
    # insert

# removing elments
    # remove
    # pop
    # clear

# accessing
    # index,count,
# alterating
    # sort,reverese
# Loop -- Iteration  --- Executing same line of code multiple numbers of times..

a=[4,19,45,36]

# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])


# while loop
# for loop


# while loop:- While check the condition and will execute the statements n number of times. till condition becomes false...

"""
while condition:
    satements
"""

# a=eval(input("Enter a value:-"))

# username = input("Enter username:")

# while a==50:
#     print(a,"is greaterthan 50")
#     a = a-1

# while username=="ramesh":
#     print(username,"is the username")
# print("Python")



# for loop -- It will based on a sequence....


"""
for element in sequence:
    statements
"""

# a="python programming"
# a=[34,"python","56","django"]
# for j in a:
#     print(j)


# nested loopign --  looping inside other loopings...
# a=["python",56,"django"]
# for j in a:
#     print(j)
#     if type(j)==int:
#         print("not satisfied")
#     else:
#         for i in j:
#             print(i)


# range -- 

# print(list(range(2,20)))

# for j in range(2,30):
#     print(j)

# a = eval(input("Enter a value:"))
# b = eval(input("Enter b value:"))
# for j in range(a,b):
#     print(j)


# print(help(str))

# for j in range(2,20):
#     print(j,end="-")


# for j in range(20):
#     print(j,end=" ")

# for j in range(2,20,3):
#     print(j,end=" ")


# for j in range(20,2,-1):
#     print(j,end=" ")


# controlflow statements:-
    # break -- Will stop all the next iteration and will go outside of the loop..
    # continue -- will pause current iteration and will directly go to next iteration...
    # pass -- Its is just for synatx purpose...


#print(list(range(4,50)))

# a=eval(input("Enter a value:-"))

#username = input("Enter username:")

#while a==50:
 #   print(a,"is greaterthan 50")
  #  a = a-1

#while username=="ramesh":
 #   print(username,"is the username")
#print("Python")

#a=["6472267282","4787428787","6536521","77646271","6732773787"]

# len -- will return the length of the value..
#for j in a:
 #   if len(j) != 10:
  #      break
   #     print(j,"not satisfied")
   
   # else:
   #     print(j)

#print("hello")

#print(list(range(4,50)))

#a=("6472267282","4787428787","6536521","77646271","6732773787")

# len -- will return the length of the value..
#for j in a:
 #   if len(j) != 10:
        #break
  #      print(j,"not satisfied")
   
   # else:
    
    #    print(j)

#print("hello")

a=("12333535","1233353512333535","1233353512333535","123335351233353512333535","12333535")

for k in a:
    if len(k) != 15:
        print(k,"Invalid Numbers")
    else:
        print(k)

print("Success")# # Loop -- Iteration  --- Executing same line of code multiple numbers of times..

# a=[4,19,45,36]

# # print(a[0])
# # print(a[1])
# # print(a[2])
# # print(a[3])


# # while loop
# # for loop


# # while loop:- While check the condition and will execute the statements n number of times. till condition becomes false...

# """
# while condition:
#     satements
# """

# # a=eval(input("Enter a value:-"))

# # username = input("Enter username:")

# # while a==50:
# #     print(a,"is greaterthan 50")
# #     a = a-1

# # while username=="ramesh":
# #     print(username,"is the username")
# # print("Python")



# # for loop -- It will based on a sequence....


# """
# for element in sequence:
#     statements
# """

# # a="python programming"
# # a=[34,"python","56","django"]
# # for j in a:
# #     print(j)


# # nested loopign --  looping inside other loopings...
# # a=["python",56,"django"]
# # for j in a:
# #     print(j)
# #     if type(j)==int:
# #         print("not satisfied")
# #     else:
# #         for i in j:
# #             print(i)


# # range -- 

# # print(list(range(2,20)))

# # for j in range(2,30):
# #     print(j)

# # a = eval(input("Enter a value:"))
# # b = eval(input("Enter b value:"))
# # for j in range(a,b):
# #     print(j)


# # print(help(str))

# # for j in range(2,20):
# #     print(j,end="-")


# # for j in range(20):
# #     print(j,end=" ")

# # for j in range(2,20,3):
# #     print(j,end=" ")


# # for j in range(20,2,-1):
# #     print(j,end=" ")


# # controlflow statements:-
#     # break -- Will stop all the next iteration and will go outside of the loop..
#     # continue -- will pause current iteration and will directly go to next iteration...
#     # pass -- Its is just for synatx purpose...


# a=["6472267282","4787428787","6536521","77646271","6732773787"]

# # len -- will return the length of the value..
# for j in a:
#     if len(j) != 10:
#         break
#     else:
#         print(j)
#     print("hello")

# print("outside")

a=["6472267282","4787428787","6536521","77646271","6732773787"]

# for j in a:
#     if len(j) != 10:
#         continue
#     else:
#         print(j)
#     print("hello")
#     b=["1"]
#     print(a+b)

# print("outside")

# for j in a:
#     if len(j) != 10:
#         pass
#     else:
#         print(j)
#     print("hello")
#     b=["1"]
#     print(a+b)

# print("outside")

# a = 1
# while a < 4:
#     pin = input("Enter pin number:-")
#     if pin == '1234':
#         account_type = input("Enter your account type:")
#         if account_type == "saving":
#             amount = int(input("enter amount:-"))
#             print("{} is debited from your account".format(amount))
#             break
#         else:
#             print("account type not matched,Try Again!")
#             a=a+1
#     else:
#         a=a+1
#         if a != 4:
#             print("Pin not matched,Try Again!")
# else:
#     print("Tried More no.of time Account Blocked for 24 hours!")
Sanjeev-Python-8:Am
Weekdays
24-07-2020 Class Recordings & Files
Sanjeev Classes March
•
10:00 AM

operators_cls.py
Text
Class comments


24-07-2020 Class Recordings & Files
# Operators -- Its a symbol which perform an operation between 2 or more operands....

# 3+5+6

# List of Operators:-
    # 1) Arithemtic Operators(+,-,*,/,//,%,**)
    # 2) Relational Operators(==,!=,>,<,>=,<=)
    # 3) Logical Operators(and,or,not)
    # 4) Assignment Operators(=,+=,-=,*=,/=)
    # 5) Bitwise Operators(Bitwise And(&),Bitwise OR(|),Bitwise XOR(^),Left Shift(<<),Right Shift(>>),Bitwise NOT(~))
    # 6) Membership Operators(in,not in)
    # 7) Identity Operators(is,is not)


# 1) Arithmetic Operators

# print(34+67)
# print(45-35)
# print(12*12)


# print(17/3)

# print(17//3)

# print(16/3) = 5.6667

# print(16//3) = 5

# print(17%3)  =2


# 3) 17 (5
#    15
# ---------
#     2

# 158%3 - 2
# 3) 158 (52
#    15
# --------
#     08
#      6
# ---------
#      2

# 3*5
# 3**5 == 3*3*3*3*3 -- 343


# 2)Relational Operators -- Output for relational operators will be True or False only..

a=45
b=78

# print(a==b) # False
# print(a != b) # False

# print(a>b) # False
# print(a<b) # True
# print(a>=b) # False
# print(a<=b) # True

# 3) Logical Operators(and,or,not):-


# A            B          A and B          A or B        not(A)        not(A and B)
# ------------------------------------------------------------------------------------
# T            F             F               T             F              T 
# F            T             F               T             T              T 
# T            T             T               T             F              F 
# F            F             F               F             T              T 




a=45
b=67


# print(a>50 and b<100)
# #      F   and  T    - F


# print(a>50 or b<100)

# #     F    or  T    -  T 


# print(not(a>50 and b<100))



# username = "gsanjeev"
# password = "123456"


# print('gsaneev'==username and '123456'==password)

# print('gsaneev'==username or '123456'==password)


# 4) Assignment Operators(=,+=,-=,*=)

# a=45
# # a=a+15
# print(a)
# print(id(a))
# a+=15 # a=a+15
# print(a)
# print(id(a))
# a-=15
# print(a)
# print(id(a))
# a*=5

# print(a)

# a/=5

# print(a)

# 45

# Python datatypes:-
    # 1) Numbers --- Numeric values or decimal values...(int,floating)
        # a=45, b=6.7
    # 2) Strings --- Sequennce of charcaters which are declared inside " "....
        # a = "hyderabad123"
    # 3) Lists ---  Sequence of multiple values which are declared inside [ ] seperated with comma(,)..
        # a = [4,"python",5.6,"hyderabad"]
    # 4) Tuples --- Sequence of multiple values which are declared inside ( ) seperated with comma(,)..
        # a = (4,"python",5.6,"hyderabad")
    # 5) Dictionaries  -- Sequence of key:value pairs which are declared inside { } seperated with comma(,)..
        # a = {'email' : 'gsanjeev@gmail.com','password':'123456'}  
    # 6) Sets -- Frozensets.. -- Sequence of multiple values which are declared inside { } seperated with comma(,)..
        # a = {4,5.6,'python','django',4}


# a = {4,5.6,'python','django',4}

# a = (4,5.6,'python','django',4)
# # print(a)

# # Lists,Dictionaries,Sets --- Mutuable
# # Tuples,Strings,Numbers --- Immutuable

# a= [4,5.6,'python','django',4]

# 6) Membership Operators(in, not in):- These are  used just for checking whether the value or elments in present in thee varibales..

# a="Python is a programming langauge"


# print("Python" in a)

# print("Python" not in a)


# a=[56,"python","django","csv",65]

# print(56 in a)

# print("csv" not in a)

# 7) Identity Operators(is,is not):- These are used to check the identity(memory allocation) if the values...


# a=45
# b=45

# print(a is b)
# print(a == b)


# a="python"
# b="python"

# print(a is b)
# print(a == b)

# a=(1,2,3)
# b=(1,2,3)

# print(a is b)
# print(a == b)

# a=[1,2,3]
# b=[1,2,3]

# print(id(a))
# print(id(b))
# print(a == b)
# print(a is b)

# print(a is not b)


# 5) Bitwise Operators:- Binary Level Operations

# A     B     A & B      A | B        A ^ B(XOR)    
# -----------------------------------------------
# 0     1       0         1            1
# 1     0       0         1            1
# 1     1       1         1            0
# 0     0       0         0            0


a = 17

b = 19


# print(a&b)

# print(a|b)
# print(a^b)

# 17  -  10001
# 19  -  10011
# -------------
    #  10001 - 17
    #  10011 - 19
    #  00010 - 2
        
# 17 -- 10001
# 2)17(
#   2)8 - 1
#     2)4 - 0
#       2)2 - 0
#         1 - 0

# 73 -- 
# 19 - 10011
# 2)19(
#    2)9 - 1
#      2)4 - 1
#        2)2 - 0
#          1 - 0


#            512 256 128  64  32 16  8 4 2 1
#                          1   0  0  1 0 1 0
                                # 0  0 0 1 0 --- 2

                        # 1   0  0   1 0 0 1 --- 73

# 1001010 - 74

# 2)74(
#   2)37 - 0
#      2)18 - 1
#        2)9  - 0
#          2)4 - 1
#            2)2 - 0
#              1 - 0

# print(bin(74))

# print(int('1001010',2))

# Bitwise NOT(~)
a=45
b=45
print(a+b)



Sanjeev-Python-8:Am
Weekdays
08-08-2020
Sanjeev Classes March
•
Aug 10

strings_cls.py
Text
Class comments



# Strings - Sequence of charcaters or numbers or special symbols declared inside ' ' or " " or """ """..

# a="python programming"
# b='python programming'
# c="""python programming"""

# print(a)
# print(b)
# print(c)

# print(type(a))
# print(type(b))
# print(type(c))

a="python is a programming langauge python is used for web development" # single line string.

b='python is a programming langauge python is used for web development' # single line string

c="""python is a programming langauge   
python is used for web development""" # multiline string

# print(a)
# print(b)
# print(c)

# " " or '' -- Used for declaring single line string only...
# """ """ -- used for declaring multiple line string


# python' programming
# a= "python' programming"
# a= 'python" programming'
# print(a)


a="python programming language"


# Accessing values inside the string -- Indexing...

# Indexing will start from 0...
# indexing is represented in [ ]..

# print(a[10])

# print(a[17])

# print(a[30]) # will through an error.(because index value giving is more than the length of string...)

# a="python programming language"

# print(a[7:14])

# print(a[4:12])

# a=['python','django',"datascience"]

# b=0
# for j in a:
#     if j=="django":
#         print("django is present at ",b)
#         break
#     else:
#         b=b+1

# print(a[b])


# negative indexing:- Access elments inside the string in reverse order..

# negative indexing will be starting from -1..

# a="python programming language"

# print(a[-3])

# print(a[-25])

# print(a[-14:-25:-1])


# Basic Operations:
    # Concatenation(+): Adding of multiple strings and giving it as a single string...
    # Repetition(*): Repeating the same element specified no.of times...

# print(3+4)

# print("Python"+" Django")

# print("Django"+"Framewwork"+"webdevelopment")

# print(4*3)

# print("Python"*5)

# print("Python"+" Django"+3)

# Concatenation will be performed on similar datatypes values only....

# a="Python"


# Datatypes are devided into 2 types..
    # Immutable datatypes -- Those we cannot make chnages once declared...(number,strings,tuples)
    # Mutuable datatypes -- Those Datatypes we can make changes..(Lists,Dictionaries,Sets..)


# String is an immutable datatypes. So, i cannot make the chnages once delcared...

# a="Python"

# print(id(a))
# # print(a[0])

# # a[0] = 'p'

# del a[0]
# a="python"

# print(id(a))

# String Methods:-
# a="Python"
# print(dir(a))

# startswith(),endswith(),isalpha(),isalnum(),isdigit(),isspace(),isupper(),islower(),lower()
# upper(),title(),capitalize(),swapcase(),count,index,find,rindex,rfind,split(),rsplit()
# strip(),rstrip(),lstrip(),zfill,join, format()


# startswith() -- Will check Whether the string is starting with what we specified..(True/False)


# a="Django is a framework"

# print(a.startswith('D'))

# # print(a.startswith("Djng")) # False

# print(a.startswith("d"))

# endswith() -- Will check Whether the string is ending with what we specified..(True/False)

# a="rajesh@gmail.com"

# print(a.endswith("gmail.com"))

# print(a.endswith("M"))


# isalpha() -- It is used to check whether all the values inside the string are alphabets only...

# a="PythonProgramming"

# print(a.isalpha())

# isalnum() -- It is used to check whether all the values inside the string are alphanumeric(alpabets or numbers) only...

# a="Python 123"

# print(a.isalnum())

# isdigit() -- It is used to check whether all the values inside the string are numbers only...

# a="518 502"

# print(a.isdigit())


# isspace() -- Will check whther complete string is a space itself...

# a=" "

# print(a.isspace())

# islower() -- It will check all the alphabets inside the string are in lower case or not... 

# a="Python is a langauge456"

# print(a.islower())


# isupper() -- It will check all the alphabets inside the string are in upper case or not...

# a="Python is a langauge456"

# a="PYTHON 123"
# print(a.isupper())

# lower() -- It will convert all the upper alphabets into lower case inside the string..

# a="PYTHON is a Language"

# print(a.lower())


# upper() -- It will convert all the lower alphabets into upper case inside the string..

# a="PYTHON is a Language"

# print(a.upper())

# title() -- Will convert Each word starting charcater into uppercase inside the string..


# a="Python is a programming language"

# print(a.title())

# capitalize() -- Will convert only starting charcater of string into uppercase and remaining into lowercase inside the string..
# a="python is a proGRamming Language"

# print(a.capitalize())


# swapcase() -- Will convert alphabest upper into lower and vice versa inside the string..

# a="python is a proGRamming Language"

# print(a.swapcase())

# count -- Will return how many times a substring is repeated inside the string..

# a="Python is a programming languange"

# print(a.count('a'))

# print(a.count('Python'))

# print(a.count('python'))

# index -- Will return the index value of the specified element inside the string..

# if the element occured multiple times. it will defaultly considr the first occurence of element itself..

# if the element we are trying is not present inside the string index method will through an error..


a="Python is a programming language"

# print(a.index('g'))

# print(a.index('g',16))

# print(a.index('g',23))


# steps
# a="Python is a programming language"
# input() -- to which elment has to search...

# Which occurence index values:-

# index_value = 0
# for -- on string:
# if condition


# print(a.index('z'))

# # print(a.find('g'))

# if a.find('z') == -1:
#     print("no elments present")
# print("Hello")


# find() -- Same as index method...
# only when elments is not present index will  give an error but find will give -1..

# # print(a.find('g'))

# if a.find('z') == -1:
#     print("no elments present")



# rindex() -- Same like indexing, but will do it from right side to leftside..

# a="Python is a programming language"

# # print(a.rindex('g',0,26))

# print(a.rindex('z',0,26))

# # print(a.rfind('g',0,26))

# print(a.rfind('z'))

# split(),rsplit()
# strip(),rstrip(),lstrip(),zfill,join, format()


# split() -- It will split your string into multiple string based on space by default.. if you specify the 
# the argument it will split based on the arguments...
# a="python is a programing language"

# print(a.split())

# print(a.split('a',2))


# rsplit() -- same as split() but will perform from right to left...
# print(a.rsplit('a',2))
# print(a.rsplit('a'))



# strip() -- it will remove the escape sequences at the starting and ending of the string...

# \n - newline
# \t - tabspace
# a="\n\tpython\n\tprogramming\n"

# # print(a)

# # print(a.strip())

# # print(a.lstrip())

# print(a.rstrip())


# zfill() -- filling up with zeros....

# a="776772376426772829"

# print(a.zfill(15))


# join() --  It is used for joining any special things to each and every elments inside the string..except the first element..

a="python"


# print("-".join(a))

# print("@".join(a))

# a=["python", "is","a","programming","language"]

# print("$".join(a))

# format() -- Dynamic way of creating a format based on valuess..

# print("Hi Ramesh,Your order with order Id 6722672 is successfully palced and will be delivered by 13-08-2022")

# print("Hi Ramesh,Your order with order Id 6427772789 is successfully palced and will be delivered by 23-08-2022")

# {} -- 

# name = input("Enter your name:-")
# order_id = input("Enter your Order Id:-")
# delivery_by = input("Enter Delivery date:-")
# print("Hi {},Your order with order Id {} is successfully palced and will be delivered by {}".format(name,order_id,delivery_by))

# print("Hi {},Your order with order Id {} is successfully palced and will be delivered by {}".format(order_id,delivery_by,name))

# print("Hi {2},Your order with order Id {0} is successfully palced and will be delivered by {1}".format(order_id,delivery_by,name))


strings_cls.py
Displaying strings_cls.py.<!DOCTYPE html>
<!-- saved from url=(0078)https://classroom.google.com/u/0/c/MTE3MzM0OTI3NDE3/p/MTI5NzEzNDQ3MjY0/details -->
<html lang="en" dir="ltr" class="QTigq We03Jb"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><script src="./Variable_cls_files/cb=gapi.loaded_2" nonce="" async=""></script><script src="./Variable_cls_files/cb=gapi.loaded_1" nonce="" async=""></script><script src="./Variable_cls_files/cb=gapi(2).loaded_0" nonce="" async=""></script><meta name="viewport" content="initial-scale=1.0,minimum-scale=1.0,width=device-width"><title>Recording Link Of 22-July-20</title><link href="./Variable_cls_files/css" rel="stylesheet"><link href="./Variable_cls_files/css(1)" rel="stylesheet"><link rel="manifest" href="https://classroom.google.com/manifest.json"><meta name="apple-itunes-app" content="app-id=924620788"><script nonce="">;this.gbar_={CONFIG:[[[0,"www.gstatic.com","og.qtm.en_US.RRvjrq5nyko.O","co.in","en","265",0,[4,2,".40.40.40.40.40.40.","","1300102,3700316,3700816","321478870","0"],null,"oFQaX6XrC6O8tgXb4ZIY",null,0,"og.qtm.1j3riysh03am7.L.W.O","AA2YrTt_OJqbWnkMjMONweMkFGu-2q-ILg","AA2YrTszUE1lFZmFXVA54XWasIZ1sOlgkA","",2,1,200,"IND",null,null,"265","265",1],null,[1,0.1000000014901161,2,1],[1,0.001000000047497451,1],[1,0,0,null,"0","sanath1975@gmail.com","","AOEwXKruQi_CHrZ0eCJWyc7-j7gnWcTVbzVwgEEQa7_cxFNmnS2UdhZKXY9kZMyDjLfxUy75tAsQWEnRJMvFbMHYrZ0ZI4tvJQ"],[0,0,"",1,0,0,0,0,0,1,0,0,0,null,0,0,null,null,0,0,0,"","","","","","",null,0,0,0,0,0,null,null,null,"rgba(32,33,36,1)","transparent",0,0,1,1],["%1$s (default)","Brand account",1,"%1$s (delegated)",1,null,83,"https://classroom.google.com/?authuser=$authuser",null,null,null,1,"https://accounts.google.com/ListAccounts?listPages=0\u0026authuser=0\u0026pid=265\u0026gpsia=1\u0026source=ogb\u0026mo=1\u0026mn=1\u0026hl=en",0,"dashboard",null,null,null,null,"Profile","",1,null,"Signed out","https://accounts.google.com/AccountChooser?source=ogb\u0026continue=$continue\u0026Email=$email","https://accounts.google.com/RemoveLocalAccount?source=ogb","Remove","Sign in",0,0,1,0,1,0,0,"000770F2036036614D3F3C96DF6A2E66C6A7ECEFA651AB56F4::1595561120197",null,102,"Session expired",null,null,"https://docs.google.com/picker","Visitor",null,"Default","Delegated","Sign out of all accounts",1,0,0,0,0],null,["1","gci_91f30755d6a6b787dcc2a4062e6e9824.js","googleapis.client:plusone:gapi.iframes","0","en"],null,null,null,null,["m;/_/scs/abc-static/_/js/k=gapi.gapi.en.ZR5MgddWeJU.O/am=AAY/d=1/ct=zgms/rs=AHpOoo-4Z3ZFsIV5SfJ3ya7-4n9QA-0-og/m=__features__","https://apis.google.com","","","1","",null,1,"es_plusone_gc_20200706.0_p0","en",null,0,0],[0.009999999776482582,"co.in","265",[null,"","0",null,1,5184000,null,null,"",0,1,"",0,0,0,0,0,0,1,0,0,0,0,0,0,0],null,[["","","0",0,0,-1]],null,0,null,null,["5061451","google\\.(com|ru|ca|by|kz|com\\.mx|com\\.tr)$",1]],[1,1,null,40400,265,"IND","en","321478870.0",8,0.009999999776482582,1,0,null,null,1,0,"3700816",null,null,null,"oFQaX6XrC6O8tgXb4ZIY",0],[[null,null,null,"https://www.gstatic.com/og/_/js/k=og.qtm.en_US.RRvjrq5nyko.O/rt=j/m=qabr,qgl,q_d,qdid,qcwid,qmutsd,qbg,qbd,qapid/exm=qaaw,qadd,qaid,qein,qhaw,qhbr,qhch,qhga,qhid,qhin,qhpr/d=1/ed=1/rs=AA2YrTt_OJqbWnkMjMONweMkFGu-2q-ILg"],[null,null,null,"https://www.gstatic.com/og/_/ss/k=og.qtm.1j3riysh03am7.L.W.O/m=qdid,qcwid/excm=qaaw,qadd,qaid,qein,qhaw,qhbr,qhch,qhga,qhid,qhin,qhpr/d=1/ed=1/ct=zgms/rs=AA2YrTszUE1lFZmFXVA54XWasIZ1sOlgkA"]],null,null,[""],[[[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/app"],0,448,328,57,4,1,0,0,63,64,8000,"https://www.google.co.in/intl/en/about/products",67,1,69,null,1,70,"Can't seem to load the app launcher right now. Try again or go to the %1$sGoogle Products%2$s page.",3,0,0,74,4000,null,null,null,null,null,null,1]],0,[null,null,null,"https://www.gstatic.com/og/_/js/k=og.qtm.en_US.RRvjrq5nyko.O/rt=j/m=qdsh/d=1/ed=1/rs=AA2YrTt_OJqbWnkMjMONweMkFGu-2q-ILg"],"265","265",1,0,null,"en",0],[300000,"/u/0","/u/0/_/bgogb/program/get","AOEwXKruQi_CHrZ0eCJWyc7-j7gnWcTVbzVwgEEQa7_cxFNmnS2UdhZKXY9kZMyDjLfxUy75tAsQWEnRJMvFbMHYrZ0ZI4tvJQ","https",0,"aa.google.com","rt=j\u0026sourceid=265","","oyOmiKk88xagdqe4yDstyw","",0,0,null,0,0],[["mousedown","touchstart","touchmove","wheel","keydown"],300000]]],};this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
var aa,ba,ca,da,ea,ha,ja,ka,oa,pa,Ca,Da,Fa;aa=function(a){var b=0;return function(){return b<a.length?{done:!1,value:a[b++]}:{done:!0}}};ba="function"==typeof Object.defineProperties?Object.defineProperty:function(a,b,c){if(a==Array.prototype||a==Object.prototype)return a;a[b]=c.value;return a};
ca=function(a){a=["object"==typeof globalThis&&globalThis,a,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var b=0;b<a.length;++b){var c=a[b];if(c&&c.Math==Math)return c}throw Error("a");};da=ca(this);ea=function(a,b){if(b)a:{var c=da;a=a.split(".");for(var d=0;d<a.length-1;d++){var e=a[d];if(!(e in c))break a;c=c[e]}a=a[a.length-1];d=c[a];b=b(d);b!=d&&null!=b&&ba(c,a,{configurable:!0,writable:!0,value:b})}};
ea("Symbol",function(a){if(a)return a;var b=function(e,f){this.j=e;ba(this,"description",{configurable:!0,writable:!0,value:f})};b.prototype.toString=function(){return this.j};var c=0,d=function(e){if(this instanceof d)throw new TypeError("b");return new b("jscomp_symbol_"+(e||"")+"_"+c++,e)};return d});
ea("Symbol.iterator",function(a){if(a)return a;a=Symbol("c");for(var b="Array Int8Array Uint8Array Uint8ClampedArray Int16Array Uint16Array Int32Array Uint32Array Float32Array Float64Array".split(" "),c=0;c<b.length;c++){var d=da[b[c]];"function"===typeof d&&"function"!=typeof d.prototype[a]&&ba(d.prototype,a,{configurable:!0,writable:!0,value:function(){return ha(aa(this))}})}return a});ha=function(a){a={next:a};a[Symbol.iterator]=function(){return this};return a};
_.ia=function(a){var b="undefined"!=typeof Symbol&&Symbol.iterator&&a[Symbol.iterator];return b?b.call(a):{next:aa(a)}};ja="function"==typeof Object.create?Object.create:function(a){var b=function(){};b.prototype=a;return new b};if("function"==typeof Object.setPrototypeOf)ka=Object.setPrototypeOf;else{var la;a:{var ma={a:!0},na={};try{na.__proto__=ma;la=na.a;break a}catch(a){}la=!1}ka=la?function(a,b){a.__proto__=b;if(a.__proto__!==b)throw new TypeError("d`"+a);return a}:null}oa=ka;
_.n=function(a,b){a.prototype=ja(b.prototype);a.prototype.constructor=a;if(oa)oa(a,b);else for(var c in b)if("prototype"!=c)if(Object.defineProperties){var d=Object.getOwnPropertyDescriptor(b,c);d&&Object.defineProperty(a,c,d)}else a[c]=b[c];a.P=b.prototype};pa=function(a,b,c){if(null==a)throw new TypeError("e`"+c);if(b instanceof RegExp)throw new TypeError("f`"+c);return a+""};
ea("String.prototype.startsWith",function(a){return a?a:function(b,c){var d=pa(this,b,"startsWith"),e=d.length,f=b.length;c=Math.max(0,Math.min(c|0,d.length));for(var g=0;g<f&&c<e;)if(d[c++]!=b[g++])return!1;return g>=f}});ea("Number.MAX_SAFE_INTEGER",function(){return 9007199254740991});
var qa=function(a,b){a instanceof String&&(a+="");var c=0,d={next:function(){if(c<a.length){var e=c++;return{value:b(e,a[e]),done:!1}}d.next=function(){return{done:!0,value:void 0}};return d.next()}};d[Symbol.iterator]=function(){return d};return d};ea("Array.prototype.keys",function(a){return a?a:function(){return qa(this,function(b){return b})}});ea("Array.prototype.values",function(a){return a?a:function(){return qa(this,function(b,c){return c})}});
var ra=function(a,b){return Object.prototype.hasOwnProperty.call(a,b)};
ea("WeakMap",function(a){function b(){}function c(l){var m=typeof l;return"object"===m&&null!==l||"function"===m}function d(l){if(!ra(l,f)){var m=new b;ba(l,f,{value:m})}}function e(l){var m=Object[l];m&&(Object[l]=function(r){if(r instanceof b)return r;Object.isExtensible(r)&&d(r);return m(r)})}if(function(){if(!a||!Object.seal)return!1;try{var l=Object.seal({}),m=Object.seal({}),r=new a([[l,2],[m,3]]);if(2!=r.get(l)||3!=r.get(m))return!1;r.delete(l);r.set(m,4);return!r.has(l)&&4==r.get(m)}catch(t){return!1}}())return a;
var f="$jscomp_hidden_"+Math.random();e("freeze");e("preventExtensions");e("seal");var g=0,k=function(l){this.j=(g+=Math.random()+1).toString();if(l){l=_.ia(l);for(var m;!(m=l.next()).done;)m=m.value,this.set(m[0],m[1])}};k.prototype.set=function(l,m){if(!c(l))throw Error("g");d(l);if(!ra(l,f))throw Error("h`"+l);l[f][this.j]=m;return this};k.prototype.get=function(l){return c(l)&&ra(l,f)?l[f][this.j]:void 0};k.prototype.has=function(l){return c(l)&&ra(l,f)&&ra(l[f],this.j)};k.prototype.delete=function(l){return c(l)&&
ra(l,f)&&ra(l[f],this.j)?delete l[f][this.j]:!1};return k});var sa="function"==typeof Object.assign?Object.assign:function(a,b){for(var c=1;c<arguments.length;c++){var d=arguments[c];if(d)for(var e in d)ra(d,e)&&(a[e]=d[e])}return a};ea("Object.assign",function(a){return a||sa});
ea("Array.from",function(a){return a?a:function(b,c,d){c=null!=c?c:function(k){return k};var e=[],f="undefined"!=typeof Symbol&&Symbol.iterator&&b[Symbol.iterator];if("function"==typeof f){b=f.call(b);for(var g=0;!(f=b.next()).done;)e.push(c.call(d,f.value,g++))}else for(f=b.length,g=0;g<f;g++)e.push(c.call(d,b[g],g));return e}});
ea("Map",function(a){if(function(){if(!a||"function"!=typeof a||!a.prototype.entries||"function"!=typeof Object.seal)return!1;try{var k=Object.seal({x:4}),l=new a(_.ia([[k,"s"]]));if("s"!=l.get(k)||1!=l.size||l.get({x:4})||l.set({x:4},"t")!=l||2!=l.size)return!1;var m=l.entries(),r=m.next();if(r.done||r.value[0]!=k||"s"!=r.value[1])return!1;r=m.next();return r.done||4!=r.value[0].x||"t"!=r.value[1]||!m.next().done?!1:!0}catch(t){return!1}}())return a;var b=new WeakMap,c=function(k){this.o={};this.j=
f();this.size=0;if(k){k=_.ia(k);for(var l;!(l=k.next()).done;)l=l.value,this.set(l[0],l[1])}};c.prototype.set=function(k,l){k=0===k?0:k;var m=d(this,k);m.list||(m.list=this.o[m.id]=[]);m.Za?m.Za.value=l:(m.Za={next:this.j,bc:this.j.bc,head:this.j,key:k,value:l},m.list.push(m.Za),this.j.bc.next=m.Za,this.j.bc=m.Za,this.size++);return this};c.prototype.delete=function(k){k=d(this,k);return k.Za&&k.list?(k.list.splice(k.index,1),k.list.length||delete this.o[k.id],k.Za.bc.next=k.Za.next,k.Za.next.bc=
k.Za.bc,k.Za.head=null,this.size--,!0):!1};c.prototype.clear=function(){this.o={};this.j=this.j.bc=f();this.size=0};c.prototype.has=function(k){return!!d(this,k).Za};c.prototype.get=function(k){return(k=d(this,k).Za)&&k.value};c.prototype.entries=function(){return e(this,function(k){return[k.key,k.value]})};c.prototype.keys=function(){return e(this,function(k){return k.key})};c.prototype.values=function(){return e(this,function(k){return k.value})};c.prototype.forEach=function(k,l){for(var m=this.entries(),
r;!(r=m.next()).done;)r=r.value,k.call(l,r[1],r[0],this)};c.prototype[Symbol.iterator]=c.prototype.entries;var d=function(k,l){var m=l&&typeof l;"object"==m||"function"==m?b.has(l)?m=b.get(l):(m=""+ ++g,b.set(l,m)):m="p_"+l;var r=k.o[m];if(r&&ra(k.o,m))for(k=0;k<r.length;k++){var t=r[k];if(l!==l&&t.key!==t.key||l===t.key)return{id:m,list:r,index:k,Za:t}}return{id:m,list:r,index:-1,Za:void 0}},e=function(k,l){var m=k.j;return ha(function(){if(m){for(;m.head!=k.j;)m=m.bc;for(;m.next!=m.head;)return m=
m.next,{done:!1,value:l(m)};m=null}return{done:!0,value:void 0}})},f=function(){var k={};return k.bc=k.next=k.head=k},g=0;return c});
ea("Set",function(a){if(function(){if(!a||"function"!=typeof a||!a.prototype.entries||"function"!=typeof Object.seal)return!1;try{var c=Object.seal({x:4}),d=new a(_.ia([c]));if(!d.has(c)||1!=d.size||d.add(c)!=d||1!=d.size||d.add({x:4})!=d||2!=d.size)return!1;var e=d.entries(),f=e.next();if(f.done||f.value[0]!=c||f.value[1]!=c)return!1;f=e.next();return f.done||f.value[0]==c||4!=f.value[0].x||f.value[1]!=f.value[0]?!1:e.next().done}catch(g){return!1}}())return a;var b=function(c){this.j=new Map;if(c){c=
_.ia(c);for(var d;!(d=c.next()).done;)this.add(d.value)}this.size=this.j.size};b.prototype.add=function(c){c=0===c?0:c;this.j.set(c,c);this.size=this.j.size;return this};b.prototype.delete=function(c){c=this.j.delete(c);this.size=this.j.size;return c};b.prototype.clear=function(){this.j.clear();this.size=0};b.prototype.has=function(c){return this.j.has(c)};b.prototype.entries=function(){return this.j.entries()};b.prototype.values=function(){return this.j.values()};b.prototype.keys=b.prototype.values;
b.prototype[Symbol.iterator]=b.prototype.values;b.prototype.forEach=function(c,d){var e=this;this.j.forEach(function(f){return c.call(d,f,f,e)})};return b});ea("Object.entries",function(a){return a?a:function(b){var c=[],d;for(d in b)ra(b,d)&&c.push([d,b[d]]);return c}});ea("Object.is",function(a){return a?a:function(b,c){return b===c?0!==b||1/b===1/c:b!==b&&c!==c}});
ea("Array.prototype.includes",function(a){return a?a:function(b,c){var d=this;d instanceof String&&(d=String(d));var e=d.length;c=c||0;for(0>c&&(c=Math.max(c+e,0));c<e;c++){var f=d[c];if(f===b||Object.is(f,b))return!0}return!1}});ea("String.prototype.includes",function(a){return a?a:function(b,c){return-1!==pa(this,b,"includes").indexOf(b,c||0)}});
ea("Array.prototype.fill",function(a){return a?a:function(b,c,d){var e=this.length||0;0>c&&(c=Math.max(0,e+c));if(null==d||d>e)d=e;d=Number(d);0>d&&(d=Math.max(0,e+d));for(c=Number(c||0);c<d;c++)this[c]=b;return this}});var ta=function(a){return a?a:Array.prototype.fill};ea("Int8Array.prototype.fill",ta);ea("Uint8Array.prototype.fill",ta);ea("Uint8ClampedArray.prototype.fill",ta);ea("Int16Array.prototype.fill",ta);ea("Uint16Array.prototype.fill",ta);ea("Int32Array.prototype.fill",ta);
ea("Uint32Array.prototype.fill",ta);ea("Float32Array.prototype.fill",ta);ea("Float64Array.prototype.fill",ta);_.ua=_.ua||{};_.p=this||self;_.va=function(){};_.wa=function(a){a.We=void 0;a.va=function(){return a.We?a.We:a.We=new a}};_.ya=function(a){var b=typeof a;return"object"!=b?b:a?Array.isArray(a)?"array":b:"null"};_.za=function(a){return"function"==_.ya(a)};_.Aa=function(a){var b=typeof a;return"object"==b&&null!=a||"function"==b};_.Ba="closure_uid_"+(1E9*Math.random()>>>0);
Ca=function(a,b,c){return a.call.apply(a.bind,arguments)};Da=function(a,b,c){if(!a)throw Error();if(2<arguments.length){var d=Array.prototype.slice.call(arguments,2);return function(){var e=Array.prototype.slice.call(arguments);Array.prototype.unshift.apply(e,d);return a.apply(b,e)}}return function(){return a.apply(b,arguments)}};_.q=function(a,b,c){Function.prototype.bind&&-1!=Function.prototype.bind.toString().indexOf("native code")?_.q=Ca:_.q=Da;return _.q.apply(null,arguments)};_.Ea=Date.now;
_.u=function(a,b){a=a.split(".");var c=_.p;a[0]in c||"undefined"==typeof c.execScript||c.execScript("var "+a[0]);for(var d;a.length&&(d=a.shift());)a.length||void 0===b?c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}:c[d]=b};_.v=function(a,b){function c(){}c.prototype=b.prototype;a.P=b.prototype;a.prototype=new c;a.prototype.constructor=a};Fa=function(a){return a};
_.Ga=function(a){var b=null,c=_.p.trustedTypes;if(!c||!c.createPolicy)return b;try{b=c.createPolicy(a,{createHTML:Fa,createScript:Fa,createScriptURL:Fa})}catch(d){_.p.console&&_.p.console.error(d.message)}return b};
_.Ha=function(a){if(Error.captureStackTrace)Error.captureStackTrace(this,_.Ha);else{var b=Error().stack;b&&(this.stack=b)}a&&(this.message=String(a))};_.v(_.Ha,Error);_.Ha.prototype.name="CustomError";
_.Ia=Array.prototype.indexOf?function(a,b){return Array.prototype.indexOf.call(a,b,void 0)}:function(a,b){if("string"===typeof a)return"string"!==typeof b||1!=b.length?-1:a.indexOf(b,0);for(var c=0;c<a.length;c++)if(c in a&&a[c]===b)return c;return-1};_.Ja=Array.prototype.forEach?function(a,b,c){Array.prototype.forEach.call(a,b,c)}:function(a,b,c){for(var d=a.length,e="string"===typeof a?a.split(""):a,f=0;f<d;f++)f in e&&b.call(c,e[f],f,a)};
_.Ka=Array.prototype.filter?function(a,b,c){return Array.prototype.filter.call(a,b,c)}:function(a,b,c){for(var d=a.length,e=[],f=0,g="string"===typeof a?a.split(""):a,k=0;k<d;k++)if(k in g){var l=g[k];b.call(c,l,k,a)&&(e[f++]=l)}return e};_.La=Array.prototype.map?function(a,b,c){return Array.prototype.map.call(a,b,c)}:function(a,b,c){for(var d=a.length,e=Array(d),f="string"===typeof a?a.split(""):a,g=0;g<d;g++)g in f&&(e[g]=b.call(c,f[g],g,a));return e};
_.Ma=Array.prototype.some?function(a,b){return Array.prototype.some.call(a,b,void 0)}:function(a,b){for(var c=a.length,d="string"===typeof a?a.split(""):a,e=0;e<c;e++)if(e in d&&b.call(void 0,d[e],e,a))return!0;return!1};_.Na=function(a,b){return 0<=(0,_.Ia)(a,b)};
var Pa;_.Oa=function(a,b,c){for(var d in a)b.call(c,a[d],d,a)};Pa="constructor hasOwnProperty isPrototypeOf propertyIsEnumerable toLocaleString toString valueOf".split(" ");_.Qa=function(a,b){for(var c,d,e=1;e<arguments.length;e++){d=arguments[e];for(c in d)a[c]=d[c];for(var f=0;f<Pa.length;f++)c=Pa[f],Object.prototype.hasOwnProperty.call(d,c)&&(a[c]=d[c])}};
var Ra;_.Sa=function(){void 0===Ra&&(Ra=_.Ga("ogb-qtm#html"));return Ra};
var Ua;_.Va=function(a,b){this.j=a===_.Ta&&b||"";this.o=Ua};_.Va.prototype.Qb=!0;_.Va.prototype.Gb=function(){return this.j};_.Wa=function(a){return a instanceof _.Va&&a.constructor===_.Va&&a.o===Ua?a.j:"type_error:Const"};Ua={};_.Ta={};
var Ya,Xa;_.Za=function(a,b){this.o=a===Xa&&b||"";this.A=Ya};_.Za.prototype.Qb=!0;_.Za.prototype.Gb=function(){return this.o.toString()};_.Za.prototype.Ue=!0;_.Za.prototype.j=function(){return 1};_.ab=function(a){return _.$a(a).toString()};_.$a=function(a){return a instanceof _.Za&&a.constructor===_.Za&&a.A===Ya?a.o:"type_error:TrustedResourceUrl"};Ya={};_.bb=function(a){var b=_.Sa();a=b?b.createScriptURL(a):a;return new _.Za(Xa,a)};Xa={};
var db;_.cb=String.prototype.trim?function(a){return a.trim()}:function(a){return/^[\s\xa0]*([\s\S]*?)[\s\xa0]*$/.exec(a)[1]};
_.eb=function(a,b){var c=0;a=(0,_.cb)(String(a)).split(".");b=(0,_.cb)(String(b)).split(".");for(var d=Math.max(a.length,b.length),e=0;0==c&&e<d;e++){var f=a[e]||"",g=b[e]||"";do{f=/(\d*)(\D*)(.*)/.exec(f)||["","","",""];g=/(\d*)(\D*)(.*)/.exec(g)||["","","",""];if(0==f[0].length&&0==g[0].length)break;c=db(0==f[1].length?0:parseInt(f[1],10),0==g[1].length?0:parseInt(g[1],10))||db(0==f[2].length,0==g[2].length)||db(f[2],g[2]);f=f[3];g=g[3]}while(0==c)}return c};
db=function(a,b){return a<b?-1:a>b?1:0};
var jb,gb;_.hb=function(a,b){this.o=a===_.fb&&b||"";this.A=gb};_.hb.prototype.Qb=!0;_.hb.prototype.Gb=function(){return this.o.toString()};_.hb.prototype.Ue=!0;_.hb.prototype.j=function(){return 1};_.ib=function(a){return a instanceof _.hb&&a.constructor===_.hb&&a.A===gb?a.o:"type_error:SafeUrl"};jb=/^(?:(?:https?|mailto|ftp):|[^:/?#]*(?:[/?#]|$))/i;_.kb=function(a){if(a instanceof _.hb)return a;a="object"==typeof a&&a.Qb?a.Gb():String(a);return jb.test(a)?new _.hb(_.fb,a):null};
_.lb=function(a){if(a instanceof _.hb)return a;a="object"==typeof a&&a.Qb?a.Gb():String(a);jb.test(a)||(a="about:invalid#zClosurez");return new _.hb(_.fb,a)};gb={};_.mb=new _.hb(_.fb,"about:invalid#zClosurez");_.fb={};
_.ob=function(){this.j="";this.o=_.nb};_.ob.prototype.Qb=!0;_.nb={};_.ob.prototype.Gb=function(){return this.j};_.pb=function(a){var b=new _.ob;b.j=a;return b};_.qb=_.pb("");
a:{var sb=_.p.navigator;if(sb){var tb=sb.userAgent;if(tb){_.rb=tb;break a}}_.rb=""}_.w=function(a){return-1!=_.rb.indexOf(a)};
var wb;_.ub=function(){return _.w("Trident")||_.w("MSIE")};_.vb=function(){return _.w("Firefox")||_.w("FxiOS")};_.xb=function(){return _.w("Safari")&&!(wb()||_.w("Coast")||_.w("Opera")||_.w("Edge")||_.w("Edg/")||_.w("OPR")||_.vb()||_.w("Silk")||_.w("Android"))};wb=function(){return(_.w("Chrome")||_.w("CriOS"))&&!_.w("Edge")};_.yb=function(){return _.w("Android")&&!(wb()||_.vb()||_.w("Opera")||_.w("Silk"))};
var zb;_.Ab=function(){this.o="";this.B=zb;this.A=null};_.Ab.prototype.Ue=!0;_.Ab.prototype.j=function(){return this.A};_.Ab.prototype.Qb=!0;_.Ab.prototype.Gb=function(){return this.o.toString()};_.Bb=function(a){return a instanceof _.Ab&&a.constructor===_.Ab&&a.B===zb?a.o:"type_error:SafeHtml"};zb={};_.Cb=function(a,b){var c=new _.Ab,d=_.Sa();c.o=d?d.createHTML(a):a;c.A=b;return c};_.Db=new _.Ab;_.Db.o=_.p.trustedTypes&&_.p.trustedTypes.emptyHTML?_.p.trustedTypes.emptyHTML:"";_.Db.A=0;
_.Eb=_.Cb("<br>",0);
_.Fb=function(a){var b=!1,c;return function(){b||(c=a(),b=!0);return c}}(function(){var a=document.createElement("div"),b=document.createElement("div");b.appendChild(document.createElement("div"));a.appendChild(b);b=a.firstChild.firstChild;a.innerHTML=_.Bb(_.Db);return!b.parentElement});
var Gb;Gb=function(){return _.w("iPhone")&&!_.w("iPod")&&!_.w("iPad")};_.Hb=function(){return Gb()||_.w("iPad")||_.w("iPod")};
_.Ib=function(a){_.Ib[" "](a);return a};_.Ib[" "]=_.va;var Kb=function(a,b){var c=Jb;return Object.prototype.hasOwnProperty.call(c,a)?c[a]:c[a]=b(a)};
var Yb,Zb,Jb,gc;_.Lb=_.w("Opera");_.x=_.ub();_.Mb=_.w("Edge");_.Nb=_.Mb||_.x;_.Ob=_.w("Gecko")&&!(-1!=_.rb.toLowerCase().indexOf("webkit")&&!_.w("Edge"))&&!(_.w("Trident")||_.w("MSIE"))&&!_.w("Edge");_.Pb=-1!=_.rb.toLowerCase().indexOf("webkit")&&!_.w("Edge");_.Qb=_.w("Macintosh");_.Rb=_.w("Windows");_.Sb=_.w("Linux")||_.w("CrOS");_.Tb=_.w("Android");_.Ub=Gb();_.Vb=_.w("iPad");_.Wb=_.w("iPod");_.Xb=_.Hb();Yb=function(){var a=_.p.document;return a?a.documentMode:void 0};
a:{var $b="",ac=function(){var a=_.rb;if(_.Ob)return/rv:([^\);]+)(\)|;)/.exec(a);if(_.Mb)return/Edge\/([\d\.]+)/.exec(a);if(_.x)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a);if(_.Pb)return/WebKit\/(\S+)/.exec(a);if(_.Lb)return/(?:Version)[ \/]?(\S+)/.exec(a)}();ac&&($b=ac?ac[1]:"");if(_.x){var bc=Yb();if(null!=bc&&bc>parseFloat($b)){Zb=String(bc);break a}}Zb=$b}_.cc=Zb;Jb={};_.dc=function(a){return Kb(a,function(){return 0<=_.eb(_.cc,a)})};_.fc=function(a){return Number(ec)>=a};
if(_.p.document&&_.x){var hc=Yb();gc=hc?hc:parseInt(_.cc,10)||void 0}else gc=void 0;var ec=gc;
_.ic=_.vb();_.jc=Gb()||_.w("iPod");_.kc=_.w("iPad");_.lc=_.yb();_.mc=wb();_.nc=_.xb()&&!_.Hb();
var oc={},pc=null;
_.qc=function(a){this.j=0;this.o=a};_.qc.prototype.next=function(){return this.j<this.o.length?{done:!1,value:this.o[this.j++]}:{done:!0,value:void 0}};"undefined"!=typeof Symbol&&"undefined"!=typeof Symbol.iterator&&(_.qc.prototype[Symbol.iterator]=function(){return this});
var xc;_.y=function(){};_.rc="function"==typeof Uint8Array;
_.z=function(a,b,c,d,e,f){a.j=null;b||(b=c?[c]:[]);a.J=c?String(c):void 0;a.C=0===c?-1:0;a.A=b;a:{c=a.A.length;b=-1;if(c&&(b=c-1,c=a.A[b],!(null===c||"object"!=typeof c||Array.isArray(c)||_.rc&&c instanceof Uint8Array))){a.D=b-a.C;a.B=c;break a}-1<d?(a.D=Math.max(d,b+1-a.C),a.B=null):a.D=Number.MAX_VALUE}a.K={};if(e)for(d=0;d<e.length;d++)b=e[d],b<a.D?(b+=a.C,a.A[b]=a.A[b]||_.sc):(_.tc(a),a.B[b]=a.B[b]||_.sc);if(f&&f.length)for(d=0;d<f.length;d++)_.uc(a,f[d])};_.sc=[];
_.tc=function(a){var b=a.D+a.C;a.A[b]||(a.B=a.A[b]={})};_.A=function(a,b){if(b<a.D){b+=a.C;var c=a.A[b];return c===_.sc?a.A[b]=[]:c}if(a.B)return c=a.B[b],c===_.sc?a.B[b]=[]:c};_.B=function(a,b){a=_.A(a,b);return null==a?a:!!a};_.C=function(a,b,c){a=_.A(a,b);return null==a?c:a};_.vc=function(a,b,c){a=_.B(a,b);return null==a?c:a};_.wc=function(a,b,c){a=_.A(a,b);a=null==a?a:+a;return null==a?c:a};_.D=function(a,b,c){b<a.D?a.A[b+a.C]=c:(_.tc(a),a.B[b]=c);return a};
_.uc=function(a,b){for(var c,d,e=0;e<b.length;e++){var f=b[e],g=_.A(a,f);null!=g&&(c=f,d=g,_.D(a,f,void 0))}return c?(_.D(a,c,d),c):0};_.G=function(a,b,c){a.j||(a.j={});if(!a.j[c]){var d=_.A(a,c);d&&(a.j[c]=new b(d))}return a.j[c]};_.H=function(a,b,c){a.j||(a.j={});var d=c?c.ub():c;a.j[b]=c;return _.D(a,b,d)};xc=function(a){if(a.j)for(var b in a.j){var c=a.j[b];if(Array.isArray(c))for(var d=0;d<c.length;d++)c[d]&&c[d].ub();else c&&c.ub()}};_.y.prototype.ub=function(){xc(this);return this.A};
_.y.prototype.o=_.rc?function(){var a=Uint8Array.prototype.toJSON;Uint8Array.prototype.toJSON=function(){var b;void 0===b&&(b=0);if(!pc){pc={};for(var c="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789".split(""),d=["+/=","+/","-_=","-_.","-_"],e=0;5>e;e++){var f=c.concat(d[e].split(""));oc[e]=f;for(var g=0;g<f.length;g++){var k=f[g];void 0===pc[k]&&(pc[k]=g)}}}b=oc[b];c=[];for(d=0;d<this.length;d+=3){var l=this[d],m=(e=d+1<this.length)?this[d+1]:0;k=(f=d+2<this.length)?this[d+2]:0;
g=l>>2;l=(l&3)<<4|m>>4;m=(m&15)<<2|k>>6;k&=63;f||(k=64,e||(m=64));c.push(b[g],b[l],b[m]||"",b[k]||"")}return c.join("")};try{return JSON.stringify(this.A&&this.ub(),yc)}finally{Uint8Array.prototype.toJSON=a}}:function(){return JSON.stringify(this.A&&this.ub(),yc)};var yc=function(a,b){return"number"!==typeof b||!isNaN(b)&&Infinity!==b&&-Infinity!==b?b:String(b)};_.y.prototype.toString=function(){xc(this);return this.A.toString()};
_.I=function(){this.Ya=this.Ya;this.Pb=this.Pb};_.I.prototype.Ya=!1;_.I.prototype.ua=function(){this.Ya||(this.Ya=!0,this.S())};_.I.prototype.S=function(){if(this.Pb)for(;this.Pb.length;)this.Pb.shift()()};
var zc=function(a){_.z(this,a,0,-1,null,null)};_.v(zc,_.y);
_.Ac=function(a){_.z(this,a,0,-1,null,null)};_.v(_.Ac,_.y);
var Bc=function(a){_.z(this,a,0,-1,null,null)};_.v(Bc,_.y);
_.Cc=function(a){_.z(this,a,0,-1,null,null)};_.v(_.Cc,_.y);
_.Dc=function(a){_.z(this,a,0,-1,null,null)};_.v(_.Dc,_.y);
var Ec=function(a){_.I.call(this);this.A=a;this.j=[];this.o={}};_.v(Ec,_.I);Ec.prototype.vd=function(){for(var a=this.j.length,b=this.j,c=[],d=0;d<a;++d){var e=b[d].j();a:{var f=this.A;for(var g=e.split("."),k=g.length,l=0;l<k;++l)if(f[g[l]])f=f[g[l]];else{f=null;break a}f=f instanceof Function?f:null}if(f&&f!=this.o[e])try{b[d].vd(f)}catch(m){}else c.push(b[d])}this.j=c.concat(b.slice(a))};
var Lc;_.Fc=function(){this.j={};this.o={}};_.wa(_.Fc);_.Hc=function(a){return _.Gc(_.Fc.va(),a)};_.Jc=function(a,b){var c=_.Fc.va();if(a in c.j){if(c.j[a]!=b)throw new Ic(a);}else{c.j[a]=b;if(b=c.o[a])for(var d=0,e=b.length;d<e;d++)b[d].j(c.j,a);delete c.o[a]}};_.Gc=function(a,b){if(b in a.j)return a.j[b];throw new Kc(b);};Lc=function(){_.Ha.call(this)};_.v(Lc,_.Ha);var Ic=function(){_.Ha.call(this)};_.v(Ic,Lc);var Kc=function(){_.Ha.call(this)};_.v(Kc,Lc);
var Mc=function(a){_.I.call(this);this.C=a;this.A=this.j=null;this.D=0;this.B={};this.o=!1;a=window.navigator.userAgent;0<=a.indexOf("MSIE")&&0<=a.indexOf("Trident")&&(a=/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a))&&a[1]&&9>parseFloat(a[1])&&(this.o=!0)};_.n(Mc,_.I);Mc.prototype.F=function(a,b){this.j=b;this.A=a;b.preventDefault?b.preventDefault():b.returnValue=!1};
_.Nc=function(a){_.z(this,a,0,-1,null,null)};_.v(_.Nc,_.y);
_.Qc=function(a){_.z(this,a,0,-1,null,null)};_.v(_.Qc,_.y);
_.J=function(a,b){return null!=a?!!a:!!b};_.L=function(a,b){void 0==b&&(b="");return null!=a?a:b};_.Rc=function(a,b){void 0==b&&(b=0);return null!=a?a:b};
_.Sc=function(){this.data={}};_.Sc.prototype.j=function(){window.console&&window.console.log&&window.console.log("Log data: ",this.data)};_.Sc.prototype.o=function(a){var b=[],c;for(c in this.data)b.push(encodeURIComponent(c)+"="+encodeURIComponent(String(this.data[c])));return("atyp=i&zx="+(new Date).getTime()+"&"+b.join("&")).substr(0,a)};
var Tc=function(a,b){this.data={};var c=_.G(a,Bc,8)||new Bc;window.google&&window.google.kEI&&(this.data.ei=window.google.kEI);this.data.sei=_.L(_.A(a,10));this.data.ogf=_.L(_.A(c,3));var d=window.google&&window.google.sn?/.*hp$/.test(window.google.sn)?!1:!0:_.J(_.B(a,7));this.data.ogrp=d?"1":"";this.data.ogv=_.L(_.A(c,6))+"."+_.L(_.A(c,7));this.data.ogd=_.L(_.A(a,21));this.data.ogc=_.L(_.A(a,20));this.data.ogl=_.L(_.A(a,5));b&&(this.data.oggv=b)};_.v(Tc,_.Sc);
var Uc=[1,2,3,4,5,6,9,10,11,13,14,28,29,30,34,35,37,38,39,40,42,43,48,49,50,51,52,53,62,500],Xc=function(a,b,c,d,e,f){Tc.call(this,a,b);_.Qa(this.data,{oge:d,ogex:_.L(_.A(a,9)),ogp:_.L(_.A(a,6)),ogsr:Math.round(1/(Vc(d)?_.Rc(_.wc(c,3,1)):_.Rc(_.wc(c,2,1E-4)))),ogus:e});if(f){"ogw"in f&&(this.data.ogw=f.ogw,delete f.ogw);"ved"in f&&(this.data.ved=f.ved,delete f.ved);a=[];for(var g in f)0!=a.length&&a.push(","),a.push(Wc(g)),a.push("."),a.push(Wc(f[g]));f=a.join("");""!=f&&(this.data.ogad=f)}};
_.v(Xc,Tc);var Wc=function(a){a=String(a);return a.replace(".","%2E").replace(",","%2C")},Yc=null,Vc=function(a){if(!Yc){Yc={};for(var b=0;b<Uc.length;b++)Yc[Uc[b]]=!0}return!!Yc[a]};
var Zc,bd,ad;_.$c=function(a){var b=window.google&&window.google.logUrl?"":"https://www.google.com";b+="/gen_204?";b+=a.o(2040-b.length);Zc(_.kb(b)||_.mb)};Zc=function(a){var b=new Image;b.onerror=b.onload=b.onabort=function(){ad in bd&&delete bd[ad]};bd[ad++]=b;b.src=_.ib(a)};bd=[];ad=0;
var fd=function(){var a=cd,b=dd,c=ed;this.D=a;this.C=b;this.B=_.Rc(_.wc(a,2,1E-4),1E-4);this.o=_.Rc(_.wc(a,3,1),1);b=Math.random();this.A=_.J(_.B(a,1))&&b<this.B;this.j=_.J(_.B(a,1))&&b<this.o;a=0;_.J(_.B(c,1))&&(a|=1);_.J(_.B(c,2))&&(a|=2);_.J(_.B(c,3))&&(a|=4);this.F=a};fd.prototype.log=function(a,b){try{if(Vc(a)?this.j:this.A){var c=new Xc(this.C,"quantum:gapiBuildLabel",this.D,a,this.F,b);_.$c(c)}}catch(d){}};
_.gd=function(a,b,c,d,e){Tc.call(this,a,b);_.Qa(this.data,{jexpid:_.L(_.A(a,9)),srcpg:"prop="+_.L(_.A(a,6)),jsr:Math.round(1/d),emsg:c.name+":"+c.message});if(e){e._sn&&(e._sn="og."+e._sn);for(var f in e)this.data[encodeURIComponent(f)]=e[f]}};_.v(_.gd,Tc);
_.hd=function(a){_.z(this,a,0,-1,null,null)};_.v(_.hd,_.y);
var kd=function(){var a=id;this.F=jd;this.B=_.Rc(_.wc(a,2,.001),.001);this.D=_.J(_.B(a,1))&&Math.random()<this.B;this.C=_.Rc(_.C(a,3,1),1);this.A=0;this.j=this.o=null;_.vc(a,4,!0)};kd.prototype.log=function(a,b){if(this.j){var c=new zc;_.D(c,1,a.message);_.D(c,2,a.stack);_.D(c,3,a.lineNumber);_.D(c,5,1);var d=new _.Ac;_.H(d,40,c);this.j.log(98,d)}try{if(this.D&&this.A<this.C){try{var e=(this.o||_.Gc(_.Fc.va(),"lm")).j(a,b)}catch(f){e=new _.gd(this.F,"quantum:gapiBuildLabel",a,this.B,b)}_.$c(e);this.A++}}catch(f){}};
var ld=function(a){_.z(this,a,0,-1,null,null)};_.v(ld,_.y);
var md=function(a){this.j=a;this.o=void 0;this.A=[]};md.prototype.then=function(a,b,c){this.A.push(new nd(a,b,c));_.od(this)};_.pd=function(a,b){if(void 0!==a.j||void 0!==a.o)throw Error("o");a.j=b;_.od(a)};_.od=function(a){if(0<a.A.length){var b=void 0!==a.j,c=void 0!==a.o;if(b||c){b=b?a.B:a.C;c=a.A;a.A=[];try{(0,_.Ja)(c,b,a)}catch(d){console.error(d)}}}};md.prototype.B=function(a){a.o&&a.o.call(a.j,this.j)};md.prototype.C=function(a){a.A&&a.A.call(a.j,this.o)};
var nd=function(a,b,c){this.o=a;this.A=b;this.j=c};
_.qd=function(){this.B=new md;this.o=new md;this.F=new md;this.C=new md;this.D=new md;this.H=new md;this.K=new md;this.j=new md;this.A=new md};_.h=_.qd.prototype;_.h.Gh=function(){return this.B};_.h.Oh=function(){return this.o};_.h.Uh=function(){return this.F};_.h.Nh=function(){return this.C};_.h.Sh=function(){return this.D};_.h.Vh=function(){return this.H};_.h.Kh=function(){return this.K};_.h.Lh=function(){return this.j};_.h.zh=function(){return this.A};_.wa(_.qd);
var rd=function(a){_.z(this,a,0,-1,null,null)};_.v(rd,_.y);_.td=function(){return _.G(_.sd,_.Cc,1)};_.ud=function(){return _.G(_.sd,_.Dc,5)};
var vd;window.gbar_&&window.gbar_.CONFIG?vd=window.gbar_.CONFIG[0]||{}:vd=[];_.sd=new rd(vd);
var id,jd,dd,ed,cd;id=_.G(_.sd,_.hd,3)||new _.hd;jd=_.td()||new _.Cc;_.M=new kd;dd=_.td()||new _.Cc;ed=_.ud()||new _.Dc;cd=_.G(_.sd,ld,4)||new ld;_.wd=new fd;
_.u("gbar_._DumpException",function(a){_.M?_.M.log(a):console.error(a)});
_.xd=new Mc(_.M);
_.wd.log(8,{m:"BackCompat"==document.compatMode?"q":"s"});_.u("gbar.A",md);md.prototype.aa=md.prototype.then;_.u("gbar.B",_.qd);_.qd.prototype.ba=_.qd.prototype.Oh;_.qd.prototype.bb=_.qd.prototype.Uh;_.qd.prototype.bd=_.qd.prototype.Sh;_.qd.prototype.be=_.qd.prototype.Vh;_.qd.prototype.bf=_.qd.prototype.Gh;_.qd.prototype.bg=_.qd.prototype.Nh;_.qd.prototype.bh=_.qd.prototype.Kh;_.qd.prototype.bi=_.qd.prototype.Lh;_.qd.prototype.bj=_.qd.prototype.zh;_.u("gbar.a",_.qd.va());var yd=new Ec(window);
_.Jc("api",yd);var zd=_.ud()||new _.Dc,Ad=_.L(_.A(zd,8));window.__PVT=Ad;_.Jc("eq",_.xd);

}catch(e){_._DumpException(e)}
try{
var Bd=function(a){_.z(this,a,0,-1,null,null)};_.v(Bd,_.y);
var Cd=function(){_.I.call(this);this.o=[];this.j=[]};_.n(Cd,_.I);Cd.prototype.A=function(a,b){this.o.push({Vd:a,options:b})};Cd.prototype.init=function(a,b,c){window.gapi={};var d=window.___jsl={};d.h=_.L(_.A(a,1));null!=_.A(a,12)&&(d.dpo=_.J(_.B(a,12)));d.ms=_.L(_.A(a,2));d.m=_.L(_.A(a,3));d.l=[];_.A(b,1)&&(a=_.A(b,3))&&this.j.push(a);_.A(c,1)&&(c=_.A(c,2))&&this.j.push(c);_.u("gapi.load",(0,_.q)(this.A,this));return this};
var Dd=_.G(_.sd,_.Nc,14)||new _.Nc,Ed=_.G(_.sd,_.Qc,9)||new _.Qc,Fd=new Bd,Gd=new Cd;Gd.init(Dd,Ed,Fd);_.Jc("gs",Gd);

}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><style nonce="">.gb_4a:not(.gb_0d){font:13px/27px Roboto,RobotoDraft,Arial,sans-serif;z-index:986}@-webkit-keyframes gb__a{0%{opacity:0}50%{opacity:1}}@keyframes gb__a{0%{opacity:0}50%{opacity:1}}a.gb_0{border:none;color:#4285f4;cursor:default;font-weight:bold;outline:none;position:relative;text-align:center;text-decoration:none;text-transform:uppercase;white-space:nowrap;-webkit-user-select:none}a.gb_0:hover:after,a.gb_0:focus:after{background-color:rgba(0,0,0,.12);content:'';height:100%;left:0;position:absolute;top:0;width:100%}a.gb_0:hover,a.gb_0:focus{text-decoration:none}a.gb_0:active{background-color:rgba(153,153,153,.4);text-decoration:none}a.gb_1{background-color:#4285f4;color:#fff}a.gb_1:active{background-color:#0043b2}.gb_2{-webkit-box-shadow:0 1px 1px rgba(0,0,0,.16);box-shadow:0 1px 1px rgba(0,0,0,.16)}.gb_0,.gb_1,.gb_3,.gb_4{display:inline-block;line-height:28px;padding:0 12px;-webkit-border-radius:2px;border-radius:2px}.gb_3{background:#f8f8f8;border:1px solid #c6c6c6}.gb_4{background:#f8f8f8}.gb_3,#gb a.gb_3.gb_3,.gb_4{color:#666;cursor:default;text-decoration:none}#gb a.gb_4.gb_4{cursor:default;text-decoration:none}.gb_4{border:1px solid #4285f4;font-weight:bold;outline:none;background:#4285f4;background:-webkit-linear-gradient(top,#4387fd,#4683ea);background:linear-gradient(top,#4387fd,#4683ea);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#4387fd,endColorstr=#4683ea,GradientType=0)}#gb a.gb_4.gb_4{color:#fff}.gb_4:hover{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15);box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_4:active{-webkit-box-shadow:inset 0 2px 0 rgba(0,0,0,.15);box-shadow:inset 0 2px 0 rgba(0,0,0,.15);background:#3c78dc;background:-webkit-linear-gradient(top,#3c7ae4,#3f76d3);background:linear-gradient(top,#3c7ae4,#3f76d3);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#3c7ae4,endColorstr=#3f76d3,GradientType=0)}.gb_Ia{display:none!important}.gb_Ja{visibility:hidden}.gb_nd{display:inline-block;vertical-align:middle}.gb_0f{position:relative}.gb_D{display:inline-block;outline:none;vertical-align:middle;-webkit-border-radius:2px;border-radius:2px;-webkit-box-sizing:border-box;box-sizing:border-box;height:40px;width:40px;color:#000;cursor:pointer;text-decoration:none}#gb#gb a.gb_D{color:#000;cursor:pointer;text-decoration:none}.gb_6a{border-color:transparent;border-bottom-color:#fff;border-style:dashed dashed solid;border-width:0 8.5px 8.5px;display:none;position:absolute;left:11.5px;top:43px;z-index:1;height:0;width:0;-webkit-animation:gb__a .2s;animation:gb__a .2s}.gb_7a{border-color:transparent;border-style:dashed dashed solid;border-width:0 8.5px 8.5px;display:none;position:absolute;left:11.5px;z-index:1;height:0;width:0;-webkit-animation:gb__a .2s;animation:gb__a .2s;border-bottom-color:#ccc;border-bottom-color:rgba(0,0,0,.2);top:42px}x:-o-prefocus,div.gb_7a{border-bottom-color:#ccc}.gb_F{background:#fff;border:1px solid #ccc;border-color:rgba(0,0,0,.2);color:#000;-webkit-box-shadow:0 2px 10px rgba(0,0,0,.2);box-shadow:0 2px 10px rgba(0,0,0,.2);display:none;outline:none;overflow:hidden;position:absolute;right:8px;top:62px;-webkit-animation:gb__a .2s;animation:gb__a .2s;-webkit-border-radius:2px;border-radius:2px;-webkit-user-select:text}.gb_nd.gb_na .gb_6a,.gb_nd.gb_na .gb_7a,.gb_nd.gb_na .gb_F,.gb_na.gb_F{display:block}.gb_nd.gb_na.gb_1f .gb_6a,.gb_nd.gb_na.gb_1f .gb_7a{display:none}.gb_2f{position:absolute;right:8px;top:62px;z-index:-1}.gb_Qa .gb_6a,.gb_Qa .gb_7a,.gb_Qa .gb_F{margin-top:-10px}.gb_nd:first-child,#gbsfw:first-child+.gb_nd{padding-left:4px}.gb_sa.gb_9e .gb_nd:first-child{padding-left:0}.gb_4c{position:relative}.gb_Tc .gb_4c,.gb_he .gb_4c{float:right}.gb_D{padding:8px;cursor:pointer}.gb_sa .gb_6c:not(.gb_0):focus img{background-color:rgba(0,0,0,0.20);outline:none;-webkit-border-radius:50%;border-radius:50%}.gb_af button:focus svg,.gb_af button:hover svg,.gb_af button:active svg,.gb_D:focus,.gb_D:hover,.gb_D:active,.gb_D[aria-expanded=true]{outline:none;-webkit-border-radius:50%;border-radius:50%}.gb_Cc .gb_af.gb_bf button:focus svg,.gb_Cc .gb_af.gb_bf button:focus:hover svg,.gb_af button:focus svg,.gb_af button:focus:hover svg,.gb_D:focus,.gb_D:focus:hover{background-color:rgba(60,64,67,0.1)}.gb_Cc .gb_af.gb_bf button:active svg,.gb_af button:active svg,.gb_D:active{background-color:rgba(60,64,67,0.12)}.gb_Cc .gb_af.gb_bf button:hover svg,.gb_af button:hover svg,.gb_D:hover{background-color:rgba(60,64,67,0.08)}.gb_ia .gb_D.gb_Ta:hover{background-color:transparent}.gb_D[aria-expanded=true],.gb_D:hover[aria-expanded=true]{background-color:rgba(95,99,104,0.24)}.gb_D[aria-expanded=true] .gb_cf,.gb_D[aria-expanded=true] .gb_df{fill:#5f6368;opacity:1}.gb_Cc .gb_af button:hover svg,.gb_Cc .gb_D:hover{background-color:rgba(232,234,237,0.08)}.gb_Cc .gb_af button:focus svg,.gb_Cc .gb_af button:focus:hover svg,.gb_Cc .gb_D:focus,.gb_Cc .gb_D:focus:hover{background-color:rgba(232,234,237,0.10)}.gb_Cc .gb_af button:active svg,.gb_Cc .gb_D:active{background-color:rgba(232,234,237,0.12)}.gb_Cc .gb_D[aria-expanded=true],.gb_Cc .gb_D:hover[aria-expanded=true]{background-color:rgba(255,255,255,0.12)}.gb_Cc .gb_D[aria-expanded=true] .gb_cf,.gb_Cc .gb_D[aria-expanded=true] .gb_df{fill:#ffffff;opacity:1}.gb_nd{padding:4px}.gb_sa.gb_9e .gb_nd{padding:4px 2px}.gb_sa.gb_9e .gb_Ua.gb_nd{padding-left:6px}.gb_F{z-index:991;line-height:normal}.gb_F.gb_ef{left:8px;right:auto}@media (max-width:350px){.gb_F.gb_ef{left:0}}.gb_ff .gb_F{top:56px}.gb_C .gb_D,.gb_E .gb_C .gb_D{background-position:-64px -29px}.gb_j .gb_C .gb_D{background-position:-29px -29px;opacity:1}.gb_C .gb_D,.gb_C .gb_D:hover,.gb_C .gb_D:focus{opacity:1}.gb_1d{display:none}.gb_7c{font-family:Google Sans,Roboto,RobotoDraft,Helvetica,Arial,sans-serif;font-size:20px;font-weight:400;letter-spacing:.25px;line-height:48px;margin-bottom:2px;opacity:1;overflow:hidden;padding-left:16px;position:relative;text-overflow:ellipsis;vertical-align:middle;top:2px;white-space:nowrap;-webkit-flex:1 1 auto;flex:1 1 auto}.gb_7c.gb_8c{color:#3c4043}.gb_sa.gb_ta .gb_7c{margin-bottom:0}.gb_9c.gb_ad .gb_7c{padding-left:4px}.gb_sa.gb_ta .gb_bd{position:relative;top:-2px}.gb_sa{color:black;min-width:320px;position:relative;-webkit-transition:box-shadow 250ms;transition:box-shadow 250ms}.gb_sa.gb_Lc{min-width:240px}.gb_sa.gb_2d .gb_2c{display:none}.gb_sa.gb_2d .gb_3d{height:56px}header.gb_sa{display:block}.gb_sa svg{fill:currentColor}.gb_4d{position:fixed;top:0;width:100%}.gb_5d{-webkit-box-shadow:0 4px 5px 0 rgba(0,0,0,0.14),0 1px 10px 0 rgba(0,0,0,0.12),0 2px 4px -1px rgba(0,0,0,0.2);box-shadow:0 4px 5px 0 rgba(0,0,0,0.14),0 1px 10px 0 rgba(0,0,0,0.12),0 2px 4px -1px rgba(0,0,0,0.2)}.gb_6d{height:64px}.gb_sa:not(.gb_Oc) .gb_dd.gb_ed:not(.gb_7d):not(.gb_8d),.gb_sa:not(.gb_Oc) .gb_Wd:not(.gb_7d):not(.gb_8d),.gb_sa.gb_9d .gb_dd.gb_ed.gb_7d,.gb_sa.gb_9d .gb_Wd.gb_7d,.gb_sa.gb_9d .gb_dd.gb_ed.gb_8d,.gb_sa.gb_9d .gb_Wd.gb_8d{display:none!important}.gb_3d{-webkit-box-sizing:border-box;box-sizing:border-box;position:relative;width:100%;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:space-between;-webkit-justify-content:space-between;justify-content:space-between;min-width:-webkit-min-content;min-width:min-content}.gb_sa:not(.gb_ta) .gb_3d{padding:8px}.gb_sa.gb_ae .gb_3d{-webkit-flex:1 0 auto;flex:1 0 auto}.gb_sa .gb_3d.gb_be.gb_ce{min-width:0}.gb_sa.gb_ta .gb_3d{padding:4px;padding-left:8px;min-width:0}.gb_2c{height:48px;vertical-align:middle;white-space:nowrap;-webkit-box-align:center;-webkit-align-items:center;align-items:center;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-user-select:none}.gb_ee>.gb_2c{display:table-cell;width:100%}.gb_9c{padding-right:30px;-webkit-box-sizing:border-box;box-sizing:border-box;-webkit-flex:1 0 auto;flex:1 0 auto}.gb_sa.gb_ta .gb_9c{padding-right:14px}.gb_fe{-webkit-flex:1 1 100%;flex:1 1 100%}.gb_fe>:only-child{display:inline-block}.gb_3c.gb_Uc{padding-left:4px}.gb_3c.gb_ge,.gb_sa.gb_ae .gb_3c,.gb_sa.gb_ta:not(.gb_he) .gb_3c{padding-left:0}.gb_sa.gb_ta .gb_3c.gb_ge{padding-right:0}.gb_sa.gb_ta .gb_3c.gb_ge .gb_ia{margin-left:10px}.gb_Uc{display:inline}.gb_sa.gb_Oc .gb_3c.gb_ie,.gb_sa.gb_he .gb_3c.gb_ie{padding-left:2px}.gb_7c{display:inline-block}.gb_3c{-webkit-box-sizing:border-box;box-sizing:border-box;height:48px;line-height:normal;padding:0 4px;padding-left:30px;-webkit-flex:0 0 auto;flex:0 0 auto;-webkit-box-pack:flex-end;-webkit-justify-content:flex-end;justify-content:flex-end}.gb_he{height:48px}.gb_sa.gb_he{min-width:initial;min-width:auto}.gb_he .gb_3c{float:right;padding-left:32px}.gb_he .gb_3c.gb_je{padding-left:0}.gb_ke{font-size:14px;max-width:200px;overflow:hidden;padding:0 12px;text-overflow:ellipsis;white-space:nowrap;-webkit-user-select:text}.gb_le{-webkit-transition:background-color .4s;transition:background-color .4s}.gb_me{color:black}.gb_Cc{color:white}.gb_sa a,.gb_Ic a{color:inherit}.gb_t{color:rgba(0,0,0,0.87)}.gb_sa svg,.gb_Ic svg,.gb_9c .gb_ne,.gb_Tc .gb_ne{color:#5f6368;opacity:1}.gb_Cc svg,.gb_Ic.gb_Mc svg,.gb_Cc .gb_9c .gb_ne,.gb_Cc .gb_9c .gb_Bc,.gb_Cc .gb_9c .gb_bd,.gb_Ic.gb_Mc .gb_ne{color:rgba(255,255,255, .87 )}.gb_Cc .gb_9c .gb_ua:not(.gb_oe){opacity:.87}.gb_8c{color:inherit;opacity:1;text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased}.gb_Cc .gb_8c,.gb_me .gb_8c{opacity:1}.gb_pe{position:relative}.gb_qe{font-family:arial,sans-serif;line-height:normal;padding-right:15px}a.gb_g,span.gb_g{color:rgba(0,0,0,0.87);text-decoration:none}.gb_Cc a.gb_g,.gb_Cc span.gb_g{color:white}a.gb_g:hover,a.gb_g:focus{opacity:.85;text-decoration:underline}.gb_h{display:inline-block;padding-left:15px}.gb_h .gb_g{display:inline-block;line-height:24px;outline:none;vertical-align:middle}.gb_re{font-family:Google Sans,Roboto,RobotoDraft,Helvetica,Arial,sans-serif;font-weight:500;font-size:14px;letter-spacing:.25px;line-height:16px;margin-left:10px;margin-right:8px;min-width:96px;padding:9px 23px;text-align:center;vertical-align:middle;-webkit-border-radius:4px;border-radius:4px;-webkit-box-sizing:border-box;box-sizing:border-box}.gb_sa.gb_he .gb_re{margin-left:8px}#gb a.gb_4.gb_4.gb_re,#gb a.gb_3.gb_3.gb_re{cursor:pointer}.gb_4.gb_re:hover{background:#2b7de9;-webkit-box-shadow:0 1px 2px 0 rgba(66,133,244,0.3),0 1px 3px 1px rgba(66,133,244,0.15);box-shadow:0 1px 2px 0 rgba(66,133,244,0.3),0 1px 3px 1px rgba(66,133,244,0.15)}.gb_4.gb_re:focus,.gb_4.gb_re:hover:focus{background:#5094ed;-webkit-box-shadow:0 1px 2px 0 rgba(66,133,244,0.3),0 1px 3px 1px rgba(66,133,244,0.15);box-shadow:0 1px 2px 0 rgba(66,133,244,0.3),0 1px 3px 1px rgba(66,133,244,0.15)}.gb_4.gb_re:active{background:#63a0ef;-webkit-box-shadow:0 1px 2px 0 rgba(66,133,244,0.3),0 1px 3px 1px rgba(66,133,244,0.15);box-shadow:0 1px 2px 0 rgba(66,133,244,0.3),0 1px 3px 1px rgba(66,133,244,0.15)}.gb_re:not(.gb_3){background:#1a73e8;border:1px solid transparent}.gb_sa.gb_ta .gb_re{padding:9px 15px;min-width:80px}.gb_se{text-align:left}#gb a.gb_4.gb_ja.gb_re,#gb a.gb_re.gb_3{background:#ffffff;border-color:#dadce0;-webkit-box-shadow:none;box-shadow:none;color:#1a73e8}#gb a.gb_4.gb_ja.gb_re:hover,#gb a.gb_re.gb_3:hover{background:#f8fbff;border-color:#cce0fc}#gb a.gb_4.gb_ja.gb_re:focus,#gb a.gb_4.gb_ja.gb_re:focus:hover,#gb a.gb_re.gb_3:focus,#gb a.gb_re.gb_3:focus:hover{background:#f4f8ff;border-color:#c9ddfc}#gb a.gb_4.gb_ja.gb_re:active,#gb a.gb_re.gb_3:active{background:#ecf3fe}#gb a.gb_4.gb_ja.gb_re:active{-webkit-box-shadow:0 1px 2px 0 rgba(0,0,0,0.3),0 2px 6px 2px rgba(0,0,0,0.15);box-shadow:0 1px 2px 0 rgba(0,0,0,0.3),0 2px 6px 2px rgba(0,0,0,0.15)}#gb a.gb_re.gb_3:not(.gb_ja):active{-webkit-box-shadow:0 1px 2px 0 rgba(60,64,67,0.3),0 2px 6px 2px rgba(60,64,67,0.15);box-shadow:0 1px 2px 0 rgba(60,64,67,0.3),0 2px 6px 2px rgba(60,64,67,0.15)}.gb_ia{background-color:rgba(255,255,255,0.88);border:1px solid #dadce0;-webkit-box-sizing:border-box;box-sizing:border-box;cursor:pointer;display:inline-block;max-height:48px;overflow:hidden;outline:none;padding:0;vertical-align:middle;width:134px;-webkit-border-radius:8px;border-radius:8px}.gb_ia.gb_ja{background-color:transparent;border:1px solid #5f6368}.gb_ka{width:115px}.gb_la{display:inherit}.gb_la.gb_ja{background:#ffffff;-webkit-border-radius:4px;border-radius:4px;display:inline-block;left:8px;margin-right:5px;position:relative;padding:3px;top:-1px}.gb_la.gb_ma.gb_ja{left:6px;margin-right:2px}.gb_ia:hover{border:1px solid #d2e3fc;background-color:rgba(248,250,255,0.88)}.gb_ia.gb_ja:hover{border:1px solid #5f6368;background-color:rgba(232,234,237,0.08)}.gb_ia:focus{border:1px solid #fff;background-color:rgba(255,255,255);-webkit-box-shadow:0 1px 2px 0 rgba(60,64,67,0.3),0 1px 3px 1px rgba(60,64,67,0.15);box-shadow:0 1px 2px 0 rgba(60,64,67,0.3),0 1px 3px 1px rgba(60,64,67,0.15)}.gb_ia.gb_ja:focus{border:1px solid #e8eaed;background-color:#38383b}.gb_ia.gb_ja:active,.gb_ia.gb_na.gb_ja:focus{border:1px solid #5f6368;background-color:#333438}.gb_oa{display:inline-block;padding-left:7px;padding-bottom:2px;text-align:center;vertical-align:middle;line-height:32px;width:78px}.gb_oa.gb_ja{line-height:26px;width:72px}.gb_oa.gb_pa.gb_ja{line-height:30px;width:57px}.gb_oa.gb_pa{line-height:40px;width:59px}.gb_oa.gb_ja{padding-left:0;padding-bottom:0}.gb_oa.gb_qa{background-color:#f1f3f4;-webkit-border-radius:4px;border-radius:4px;margin-left:8px;padding-left:0}.gb_oa.gb_qa .gb_ra{vertical-align:middle}.gb_sa:not(.gb_ta) .gb_ia{margin-left:10px;margin-right:4px}.gb_ia .gb_ra.gb_ua{min-width:0}.gb_va{max-height:32px;width:78px}.gb_pa>.gb_va{max-height:40px;width:96px}.gb_va.gb_ja{max-height:26px;width:72px}.gb_pa>.gb_va.gb_ja{max-height:30px;width:88px}.gb_Ka{-webkit-background-size:32px 32px;background-size:32px 32px;border:0;-webkit-border-radius:50%;border-radius:50%;display:block;margin:0;position:relative;height:32px;width:32px;z-index:0}.gb_La{background-color:#e8f0fe;border:1px solid rgba(32,33,36,.08);position:relative}.gb_La.gb_Ka{height:30px;width:30px}.gb_La.gb_Ka:hover,.gb_La.gb_Ka:active{-webkit-box-shadow:none;box-shadow:none}.gb_Ma{background:#fff;border:none;-webkit-border-radius:50%;border-radius:50%;bottom:2px;-webkit-box-shadow:0 1px 2px 0 rgba(60,64,67,.30),0 1px 3px 1px rgba(60,64,67,.15);box-shadow:0 1px 2px 0 rgba(60,64,67,.30),0 1px 3px 1px rgba(60,64,67,.15);height:14px;margin:2px;position:absolute;right:0;width:14px}.gb_Na{color:#1f71e7;font:400 22px/32px Google Sans,Roboto,RobotoDraft,Helvetica,Arial,sans-serif;text-align:center;text-transform:uppercase}@media (min-resolution:1.25dppx),(-o-min-device-pixel-ratio:5/4),(-webkit-min-device-pixel-ratio:1.25),(min-device-pixel-ratio:1.25){.gb_Ka::before{display:inline-block;-webkit-transform:scale(.5);transform:scale(.5);-webkit-transform-origin:left 0;transform-origin:left 0}.gb_Oa::before{display:inline-block;-webkit-transform:scale(.5);transform:scale(.5);-webkit-transform-origin:left 0;transform-origin:left 0}.gb_l .gb_Oa::before{-webkit-transform:scale(0.416666667);transform:scale(0.416666667)}}.gb_Ka:hover,.gb_Ka:focus{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15);box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_Ka:active{-webkit-box-shadow:inset 0 2px 0 rgba(0,0,0,.15);box-shadow:inset 0 2px 0 rgba(0,0,0,.15)}.gb_Ka:active::after{background:rgba(0,0,0,.1);-webkit-border-radius:50%;border-radius:50%;content:'';display:block;height:100%}.gb_Pa{cursor:pointer;line-height:40px;min-width:30px;opacity:.75;overflow:hidden;vertical-align:middle;text-overflow:ellipsis}.gb_D.gb_Pa{width:auto}.gb_Pa:hover,.gb_Pa:focus{opacity:.85}.gb_Qa .gb_Pa,.gb_Qa .gb_Ra{line-height:26px}#gb#gb.gb_Qa a.gb_Pa,.gb_Qa .gb_Ra{font-size:11px;height:auto}.gb_Sa{border-top:4px solid #000;border-left:4px dashed transparent;border-right:4px dashed transparent;display:inline-block;margin-left:6px;opacity:.75;vertical-align:middle}.gb_Ta:hover .gb_Sa{opacity:.85}.gb_ia>.gb_Ua{padding:3px 3px 3px 4px}.gb_Va.gb_Ja{color:#fff}.gb_j .gb_Pa,.gb_j .gb_Sa{opacity:1}#gb#gb.gb_j.gb_j a.gb_Pa,#gb#gb .gb_j.gb_j a.gb_Pa{color:#fff}.gb_j.gb_j .gb_Sa{border-top-color:#fff;opacity:1}.gb_E .gb_Ka:hover,.gb_j .gb_Ka:hover,.gb_E .gb_Ka:focus,.gb_j .gb_Ka:focus{-webkit-box-shadow: 0 1px 0 rgba(0,0,0,.15) , 0 1px 2px rgba(0,0,0,.2) ;box-shadow: 0 1px 0 rgba(0,0,0,.15) , 0 1px 2px rgba(0,0,0,.2) }.gb_Wa .gb_Ua,.gb_Xa .gb_Ua{position:absolute;right:1px}.gb_Ua.gb_i,.gb_Za.gb_i,.gb_Ta.gb_i{-webkit-flex:0 1 auto;flex:0 1 auto;-webkit-flex:0 1 main-size;flex:0 1 main-size}.gb_0a.gb_1a .gb_Pa{width:30px!important}.gb_2a.gb_Ja{display:none}.gb_3a{height:40px;position:absolute;right:-5px;top:-5px;width:40px}.gb_4a .gb_3a,.gb_5a .gb_3a{right:0;top:0}.gb_Ua .gb_D{padding:4px}.gb_ue{display:none}.gb_cd{display:none}.gb_cd.gb_na{display:block}.gb_dd{background-color:#fff;-webkit-box-shadow:0 1px 0 rgba(0,0,0,0.08);box-shadow:0 1px 0 rgba(0,0,0,0.08);color:#000;position:relative;z-index:986}.gb_ed{height:40px;padding:16px 24px;white-space:nowrap}.gb_fd{position:fixed;bottom:16px;padding:16px;right:16px;white-space:normal;width:328px;-webkit-transition:width .2s,bottom .2s,right .2s;transition:width .2s,bottom .2s,right .2s;-webkit-border-radius:2px;border-radius:2px;-webkit-box-shadow:0 5px 5px -3px rgba(0,0,0,0.2),0 8px 10px 1px rgba(0,0,0,0.14),0 3px 14px 2px rgba(0,0,0,0.12);box-shadow:0 5px 5px -3px rgba(0,0,0,0.2),0 8px 10px 1px rgba(0,0,0,0.14),0 3px 14px 2px rgba(0,0,0,0.12)}@media (max-width:400px){.gb_dd.gb_fd{max-width:368px;width:auto;bottom:0;right:0}}.gb_dd .gb_6c{border:0;font-weight:500;font-size:14px;line-height:36px;min-width:32px;padding:0 16px;vertical-align:middle}.gb_dd .gb_6c:before{content:'';height:6px;left:0;position:absolute;top:-6px;width:100%}.gb_dd .gb_6c:after{bottom:-6px;content:'';height:6px;left:0;position:absolute;width:100%}.gb_dd .gb_6c+.gb_6c{margin-left:8px}.gb_gd{height:48px;padding:4px;margin:-8px 0 0 -8px}.gb_fd .gb_gd{float:left;margin:-4px}.gb_hd{font-family:Roboto,RobotoDraft,Helvetica,Arial,sans-serif;overflow:hidden;vertical-align:top}.gb_ed .gb_hd{display:inline-block;padding-left:8px;width:640px}.gb_fd .gb_hd{display:block;margin-left:56px;padding-bottom:16px}.gb_id{background-color:inherit}.gb_ed .gb_id{display:inline-block;position:absolute;top:18px;right:24px}.gb_fd .gb_id{text-align:right;padding-right:24px;padding-top:6px}.gb_id .gb_jd{height:1.5em;margin:-.25em 10px -.25em 0;vertical-align:text-top;width:1.5em}.gb_kd{line-height:20px;font-size:16px;font-weight:700;color:rgba(0,0,0,.87)}.gb_fd .gb_kd{color:rgba(0,0,0,.87);font-size:16px;line-height:20px;padding-top:8px}.gb_ed .gb_kd,.gb_ed .gb_ld{width:640px}.gb_ld .gb_md,.gb_ld{line-height:20px;font-size:13px;font-weight:400;color:rgba(0,0,0,.54)}.gb_fd .gb_ld .gb_md{font-size:14px}.gb_fd .gb_ld{padding-top:12px}.gb_fd .gb_ld a{color:rgba(66,133,244,1)}.gb_nd.gb_od{padding:0}.gb_od .gb_F{background:#ffffff;border:solid 1px transparent;-webkit-border-radius:8px;border-radius:8px;-webkit-box-sizing:border-box;box-sizing:border-box;padding:16px;right:16px;top:72px;-webkit-box-shadow:0 1px 2px 0 rgba(65,69,73,0.3),0 3px 6px 2px rgba(65,69,73,0.15);box-shadow:0 1px 2px 0 rgba(65,69,73,0.3),0 3px 6px 2px rgba(65,69,73,0.15)}.gb_od .gb_F.gb_pd{right:60px;top:48px}.gb_od .gb_F.gb_qd{top:62px}a.gb_rd{color:#5f6368!important;font-size:22px;height:24px;opacity:1;padding:8px;position:absolute;right:8px;top:8px;text-decoration:none!important;width:24px}a.gb_rd:focus,a.gb_rd:active,a.gb_rd:focus:hover{background-color:#e8eaed;-webkit-border-radius:50%;border-radius:50%;outline:none}a.gb_rd:hover{background-color:#f1f3f4;-webkit-border-radius:50%;border-radius:50%;outline:none}svg.gb_sd{fill:#5f6368;opacity:1}.gb_td{padding:0;white-space:normal;display:table}.gb_ud{line-height:normal;font-family:Roboto,RobotoDraft,Helvetica,Arial,sans-serif}.gb_od .gb_4:active{outline:none;-webkit-box-shadow:0 4px 5px rgba(0,0,0,.16);box-shadow:0 4px 5px rgba(0,0,0,.16)}.gb_0.gb_vd.gb_wd{-webkit-border-radius:4px;border-radius:4px;-webkit-box-sizing:border-box;box-sizing:border-box;cursor:pointer;height:36px;font-family:Google Sans,Roboto,RobotoDraft,Helvetica,Arial,sans-serif;font-size:14px;font-weight:500;letter-spacing:.25px;line-height:16px;min-width:70px;outline:none;text-transform:none;-webkit-font-smoothing:antialiased}.gb_0.gb_xd.gb_wd{-webkit-border-radius:4px;border-radius:4px;-webkit-box-sizing:border-box;box-sizing:border-box;cursor:pointer;height:36px;color:#5f6368;font-family:Google Sans,Roboto,RobotoDraft,Helvetica,Arial,sans-serif;font-size:14px;font-weight:500;letter-spacing:.25px;line-height:16px;min-width:70px;outline:none;padding:8px 6px;text-transform:none;-webkit-font-smoothing:antialiased}.gb_0.gb_vd.gb_wd{background:white;border:1px solid #dadce0;color:#1a73e8;margin-top:21px;padding:9px 7px}.gb_0.gb_vd.gb_wd:hover{background-color:rgba(26,115,232,0.04)}.gb_0.gb_vd.gb_wd:focus,.gb_0.gb_vd.gb_wd:focus:hover{background-color:rgba(26,115,232,0.12);border:solid 1px #1a73e8}.gb_0.gb_vd.gb_wd:active{background-color:rgba(26,115,232,0.1);border-color:transparent}.gb_0.gb_xd:hover{background-color:#f8f9fa}.gb_0.gb_xd:focus,.gb_0.gb_xd:hover:focus{background-color:#f1f3f4;border-color:transparent}.gb_0.gb_xd:active{background-color:#f1f3f4;-webkit-box-shadow:0 1px 2px 0 rgba(60,64,67,0.3),0 1px 3px 1px rgba(60,64,67,0.15);box-shadow:0 1px 2px 0 rgba(60,64,67,0.3),0 1px 3px 1px rgba(60,64,67,0.15)}.gb_md{color:#5f6368;font-family:Roboto,RobotoDraft,Helvetica,Arial,sans-serif;font-size:14px;letter-spacing:.25px;line-height:20px;margin:0;margin-bottom:5px}.gb_yd{text-align:right;font-size:14px;padding-bottom:0;white-space:nowrap}.gb_yd .gb_zd,.gb_yd .gb_Ad{margin-left:12px;text-transform:none}a.gb_4.gb_zd:hover{background-color:#2b7de9;border-color:transparent;-webkit-box-shadow:0 1px 2px 0 rgba(66,133,244,0.3),0 1px 3px 1px rgba(66,133,244,0.15);box-shadow:0 1px 2px 0 rgba(66,133,244,0.3),0 1px 3px 1px rgba(66,133,244,0.15)}a.gb_4.gb_zd:focus,a.gb_4.gb_zd:hover:focus{background-color:#5094ed;border-color:transparent;-webkit-box-shadow:0 1px 2px 0 rgba(66,133,244,0.3),0 1px 3px 1px rgba(66,133,244,0.15);box-shadow:0 1px 2px 0 rgba(66,133,244,0.3),0 1px 3px 1px rgba(66,133,244,0.15)}a.gb_4.gb_zd:active{background-color:#63a0ef;-webkit-box-shadow:0 1px 2px 0 rgba(66,133,244,0.3),0 1px 3px 1px rgba(66,133,244,0.15);box-shadow:0 1px 2px 0 rgba(66,133,244,0.3),0 1px 3px 1px rgba(66,133,244,0.15)}.gb_yd .gb_zd.gb_Bd{padding-left:6px;padding-right:14px}.gb_yd .gb_wd.gb_zd img{background-color:inherit;-webkit-border-radius:initial;border-radius:initial;height:18px;margin:0 8px 0 4px;vertical-align:text-top;width:18px}.gb_Cd .gb_td .gb_Dd .gb_wd{border:2px solid transparent}.gb_td .gb_Dd .gb_wd:focus:after,.gb_td .gb_Dd .gb_wd:hover:after{background-color:transparent}.gb_ud{background-color:#404040;color:#fff;padding:16px;position:absolute;top:62px;min-width:328px;max-width:650px;right:8px;-webkit-border-radius:2px;border-radius:2px;-webkit-box-shadow:4px 4px 12px rgba(0,0,0,0.4);box-shadow:4px 4px 12px rgba(0,0,0,0.4)}.gb_ud a,.gb_ud a:visited{color:#5e97f6;text-decoration:none}.gb_Ed{text-transform:uppercase}.gb_Fd{padding-left:50px}.gb_Hd{color:#3c4043;font-family:Google Sans,Roboto,RobotoDraft,Helvetica,Arial,sans-serif;font-size:16px;font-weight:500;letter-spacing:.1px;line-height:20px;margin:0;margin-bottom:12px}.gb_md a.gb_Jd{text-decoration:none;color:#5e97f6}.gb_md a.gb_Jd:visited{color:#5e97f6}.gb_md a.gb_Jd:hover,.gb_md a.gb_Jd:active{text-decoration:underline}.gb_Kd{position:absolute;background:transparent;top:-999px;z-index:-1;visibility:hidden;margin-top:1px;margin-left:1px}#gb .gb_od{margin:0}.gb_od .gb_6c{background:#4d90fe;border:2px solid transparent;-webkit-box-sizing:border-box;box-sizing:border-box;font-weight:500;margin-top:21px;min-width:70px;text-align:center;-webkit-font-smoothing:antialiased}.gb_od a.gb_4{background:#1a73e8;-webkit-border-radius:4px;border-radius:4px;color:#ffffff;font-family:Google Sans,Roboto,RobotoDraft,Helvetica,Arial,sans-serif;font-size:14px;font-weight:500;letter-spacing:.25px;line-height:16px;padding:8px 22px;-webkit-font-smoothing:antialiased}.gb_od a.gb_4.gb_Ld{background:#d93025}.gb_od a.gb_4.gb_Ld:hover{background-color:#cc3127;-webkit-box-shadow:0 -1px 5px rgba(128,134,139,0.09),0 3px 5px rgba(128,134,139,0.06),0 1px 2px rgba(60,64,67,0.3),0 1px 3px rgba(60,64,67,0.15);box-shadow:0 -1px 5px rgba(128,134,139,0.09),0 3px 5px rgba(128,134,139,0.06),0 1px 2px rgba(60,64,67,0.3),0 1px 3px rgba(60,64,67,0.15)}.gb_od a.gb_4.gb_Ld:focus,.gb_od a.gb_4.gb_Ld:focus:hover{background-color:#b3332c;-webkit-box-shadow:none;box-shadow:none}.gb_od a.gb_4.gb_Ld:active,.gb_od a.gb_4.gb_Ld:focus:active{background-color:#a6342e;-webkit-box-shadow:0 -2px 8px rgba(128,134,139,0.09),0 4px 8px rgba(128,134,139,0.06),0 1px 2px rgba(60,64,67,0.3),0 2px 6px rgba(60,64,67,0.15);box-shadow:0 -2px 8px rgba(128,134,139,0.09),0 4px 8px rgba(128,134,139,0.06),0 1px 2px rgba(60,64,67,0.3),0 2px 6px rgba(60,64,67,0.15)}.gb_od.gb_Md a.gb_4{float:right}#gb .gb_od a.gb_6c.gb_6c{color:#ffffff;cursor:pointer}.gb_od .gb_6c:hover{background:#357ae8;border-color:#2f5bb7}.gb_Nd,.gb_Dd{display:table-cell}.gb_Nd{vertical-align:middle}.gb_Nd img{height:48px;padding-left:4px;padding-right:20px;width:48px}.gb_Dd{padding-left:13px;width:100%}.gb_od .gb_Dd{padding-top:4px;min-width:326px;padding-left:0;width:326px}.gb_od.gb_Od .gb_Dd{min-width:254px;width:254px}.gb_od.gb_Md .gb_Dd{padding-top:32px}.gb_Pd{display:block;display:inline-block;padding:1em 0 0 0;position:relative;width:100%}.gb_Qd{color:#ff0000;font-style:italic;margin:0;padding-left:46px}.gb_Pd .gb_Rd{float:right;margin:-20px 0;width:-webkit-calc(100% - 46px);width:calc(100% - 46px)}.gb_Sd svg{fill:grey}.gb_Sd.gb_Td svg{fill:#4285f4}.gb_Pd .gb_Rd label:after{background-color:#4285f4}.gb_Sd{display:inline;float:right;margin-right:22px;position:relative;top:2px}.gb_Wd{color:#ffffff;font-size:13px;font-weight:bold;height:25px;line-height:19px;padding-top:5px;padding-left:12px;position:relative;background-color:#4d90fe}.gb_Wd .gb_Xd{color:#ffffff;cursor:default;font-size:22px;font-weight:normal;position:absolute;right:12px;top:5px}.gb_Wd .gb_zd,.gb_Wd .gb_xd{color:#ffffff;display:inline-block;font-size:11px;margin-left:16px;padding:0 8px;white-space:nowrap}.gb_Zd{background:none;background-image:-webkit-gradient(linear,left top,left bottom,from(rgba(0,0,0,0.16)),to(rgba(0,0,0,0.2)));background-image:-webkit-linear-gradient(top,rgba(0,0,0,0.16),rgba(0,0,0,0.2));background-image:linear-gradient(top,rgba(0,0,0,0.16),rgba(0,0,0,0.2));background-image:-webkit-linear-gradient(top,rgba(0,0,0,0.16),rgba(0,0,0,0.2));border-radius:2px;border:1px solid #dcdcdc;border:1px solid rgba(0,0,0,0.1);cursor:default!important;filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#160000ff,endColorstr=#220000ff);text-decoration:none!important;-webkit-border-radius:2px}.gb_Zd:hover{background:none;background-image:-webkit-gradient(linear,left top,left bottom,from(rgba(0,0,0,0.14)),to(rgba(0,0,0,0.2)));background-image:-webkit-linear-gradient(top,rgba(0,0,0,0.14),rgba(0,0,0,0.2));background-image:linear-gradient(top,rgba(0,0,0,0.14),rgba(0,0,0,0.2));background-image:-webkit-linear-gradient(top,rgba(0,0,0,0.14),rgba(0,0,0,0.2));border:1px solid rgba(0,0,0,0.2);box-shadow:0 1px 1px rgba(0,0,0,0.1);-webkit-box-shadow:0 1px 1px rgba(0,0,0,0.1);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#14000000,endColorstr=#22000000)}.gb_Zd:active{box-shadow:inset 0 1px 2px rgba(0,0,0,0.3);-webkit-box-shadow:inset 0 1px 2px rgba(0,0,0,0.3)}.gb_sa .gb_0{color:#4285f4}.gb_sa .gb_1{color:#fff}.gb_sa .gb_6c:not(.gb_7e):focus{outline:none}sentinel{}</style><script data-id="_gd" nonce="">window.WIZ_global_data = {"MBtTuc":false,"h1uG0e":false,"nQyAE":{"wvFeYd":"https://people-pa.googleapis.com/$discovery/rest?version\u003dv2","duuZ1c":"true"},"u9xrGb":"%.@.\"https://drive.google.com/picker\",null,null,null,null,null,null,null,\"ABFGqemASJywJBUqo1Dcmh_459_gLVZP1g:1595561120173\",null,null,\"100248592662097646947\",[\"AB_Ypsnu1dRj4b4r1HB5Z5xOqqcGt0eza4IIq2t2QL3LlxrzaNF5UNT5WZzseqPmpbVEPS-dP8Ie\",0,\"CPiXpK745OoCFUdwyQodWxUDjQ\",1595561120173000,[14500005,14500011,14500062,14500078,14500079,14500085,14500126,14500159,14500195,14500223,14500224,14500226,14500247,14500281,14500296,14500298,14500305,14500317,14500346,14500381,14500394,14500408,14500424,14500450,14500454,14500473,14500475,14500501,14500534,14500539,14500548,14500550,14500581,14500582,14500583,14500584,14500588,14500590,14500594,14500618,14500626,14500628,14500630,14500631,14500645,14500648,14500649,14500650,14500651,14500652,14500656,14500664,14500671,14500674,14500681,14500687,14500689,14500690,14500692,14500693,14500694,14500695,14500696,14500697,14500724,14500916,14500922,14500928,14500930,14500932,14500936,14500938,14500952,14500958,14500960,14500966,14500980,14500986,14500988,14500990,14500996,14501000,14501002,14501016,14501026,14501030,14501032,44480047,44480477,44480622,44481147,44481165,44481207,44481209,44481826,44482107,44482721,44482755,44483104,44484100,44484324,44485150,44486094,44487335]\n]\n,null,null,100,\"homeroom_20200718_15_RC01\",null,null,[\"https://client-channel.google.com/client-channel/client\",\"https://clients4.google.com/invalidation/lcs/client\",\"p\",1800000,null,null,null,10000,39000,120000,2,null,100,3100,false]\n,null,null,null,null,null,null,[\"classroom.photos.gallery@gmail.com\",\"6115088410112085761\",\"https://gstatic.com/classroom/themes/img_backtoschool.jpg\",\"6109883882206140961\",[[\"6628644630507485729\",\"General\"]\n,[\"6628632272968684913\",\"English \\u0026 History\"]\n,[\"6628629996243734465\",\"Math \\u0026 Science\"]\n,[\"6628626803683231425\",\"Arts\"]\n,[\"6628641822806554225\",\"Sports\"]\n,[\"6628656847355659073\",\"Other\"]\n]\n]\n,null,\"r\",null,null,null,\"/u/0\",0,null,null,null,null,null,null,null,10,1,null,5,null,null,null,null,null,null,null,null,null,null,null,true,null,null,null,null,10,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,true,null,null,null,null,null,null,null,null,null,null,20,null,null,null,null,null,null,null,null,1000,null,null,\"{size}\",20,null,true,\"ngz3v77yrkaqffo7trsloqixwq\",null,null,null,null,null,null,null,null,null,null,null,null,null,\"https://calendar.google.com\",null,null,null,[100,604800000,2.0,0.5]\n,null,null,null,null,null,null,null,null,null,null,null,null,null,20,null,null,null,\"AIzaSyAsci9BIornX30lNLDWDIHpeClo7G8DX6k\",\"https://www.googleapis.com/drive/v2internal\",null,[]\n,null,null,null,false,null,null,null,true,true,null,null,null,null,null,null,null,null,null,null,null,null,\"https://docs.google.com\",\"https://drive.google.com\",null,100,null,null,null,null,true,null,null,\"^video/|^application/(x-flash-video|vnd\\\\.google-apps\\\\.video|video)$|^application/vnd\\\\.google-apps\\\\.drive-sdk\\\\.\",null,null,null,null,\"https://lh3.googleusercontent.com/-XdUIqdMkCWA/AAAAAAAAAAI/AAAAAAAAAAA/4252rscbv5M/s72-fbw\\u003d1/photo.jpg\",null,null,false,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,15,null,false,false,null,null,null,null,false,null,false,null,null,null,null,null,null,null,null,null,null,null,null,null,300000,null,null,null,null,null,null,null,10,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,false,null,null,null,null,null,null,null,null,\"//ssl.gstatic.com/classroom/favicon.png\",null,\"117347317482\",\"http://classroom.google.com/\",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,\"000770F2030CDE23E1C24C0749395E027D11C1A4CBAE111C95::1595561120186\",null,null,null,null,null,null,null,null,null,false,null,null,null,4000,1.3,null,null,false,null,[3]\n,null,false,true,null,false,null,null,null,null,null,null,false,null,null,null,null,true,false,true,null,false,false,null,true,null,null,null,null,null,[true,\"96485\",\"AIzaSyBqt2sx2fvfwP502G4u_Mu_kRmei_3A2OU\",null,false]\n,null,false,null,null,true,false,true,false,false,false,true,false,null,false,true,null,null,100,true,true,false,false,false,true,false,true,true,false,null,false,false,false,false,false,false]\n","w2btAe":"%.@.\"100248592662097646947\",\"100248592662097646947\",\"0\",false,null,null,true,false]\n"};</script><style nonce="">.DShyMc-AaTFfe.bFjUmb-Ysl7Fe, .DShyMc-AaTFfe .bFjUmb-Ysl7Fe {background-color: #E8F0FE;}.DShyMc-AaTFfe.bFjUmb-Wvd9Cc, .DShyMc-AaTFfe .bFjUmb-Wvd9Cc, .DShyMc-AaTFfe.CNpREd.bFjUmb-Wvd9Cc, .DShyMc-AaTFfe.CNpREd .bFjUmb-Wvd9Cc {background-color: #1A73E8;}.DShyMc-AaTFfe.bFjUmb-Tvm9db, .DShyMc-AaTFfe .bFjUmb-Tvm9db, .DShyMc-AaTFfe.CNpREd.bFjUmb-Tvm9db, .DShyMc-AaTFfe.CNpREd .bFjUmb-Tvm9db {background-color: #185ABC;}.DShyMc-AaTFfe.yxp05b-Wvd9Cc, .DShyMc-AaTFfe.CNpREd.yxp05b-Wvd9Cc, .DShyMc-AaTFfe .yxp05b-Wvd9Cc {border-color: #1A73E8;}.DShyMc-AaTFfe.VnOHwf-Ysl7Fe, .DShyMc-AaTFfe .VnOHwf-Ysl7Fe, .DShyMc-AaTFfe.CNpREd .VnOHwf-Ysl7Fe {color: #E8F0FE;}.DShyMc-AaTFfe.VnOHwf-Wvd9Cc, .DShyMc-AaTFfe .VnOHwf-Wvd9Cc, .DShyMc-AaTFfe.CNpREd .VnOHwf-Wvd9Cc {color: #1A73E8;}.DShyMc-AaTFfe.VnOHwf-Tvm9db, .DShyMc-AaTFfe .VnOHwf-Tvm9db, .DShyMc-AaTFfe.CNpREd .VnOHwf-Tvm9db {color: #185ABC;}.DShyMc-AaTFfe .tgNIJf-Ysl7Fe:focus {border-color: #E8F0FE;}.DShyMc-AaTFfe .ndcsBf.cjzpkc-Wvd9Cc, .DShyMc-AaTFfe .tgNIJf-Wvd9Cc:focus {border-color: #1A73E8;}.DShyMc-AaTFfe .u3bW4e .zZN2Lb-Wvd9Cc, .DShyMc-AaTFfe .zZN2Lb-Wvd9Cc:focus, .DShyMc-AaTFfe .maXJsd:focus .zZN2Lb-Wvd9Cc {color: #1A73E8;}.DShyMc-AaTFfe .P3W0Dd-Ysl7Fe:focus, .DShyMc-AaTFfe.maXJsd:focus .P3W0Dd-Ysl7Fe, .DShyMc-AaTFfe .maXJsd:focus .P3W0Dd-Ysl7Fe {background-color: #E8F0FE;}.DShyMc-AaTFfe .VBEdtc-Wvd9Cc:hover, .DShyMc-AaTFfe.MymH0d:hover .VBEdtc-Wvd9Cc, .DShyMc-AaTFfe .MymH0d:hover .VBEdtc-Wvd9Cc {color: #1A73E8;}.DShyMc-AaTFfe.MymH0d:hover .UISY8d-Tvm9db, .DShyMc-AaTFfe.CNpREd.MymH0d:hover .UISY8d-Tvm9db, .DShyMc-AaTFfe .MymH0d:hover .UISY8d-Tvm9db {background-color: #1A73E8;}.DShyMc-AaTFfe .UISY8d-Ysl7Fe:hover, .DShyMc-AaTFfe.MymH0d:hover .UISY8d-Ysl7Fe, .DShyMc-AaTFfe .MymH0d:hover .UISY8d-Ysl7Fe {background-color: #E8F0FE;}.DShyMc-AaTFfe .mxmXhf {color: #185ABC; fill: #185ABC;}.DShyMc-AaTFfe .EmVfjc.qs41qe .wKSUOe, .DShyMc-AaTFfe .EmVfjc.sf4e6b .wKSUOe {-webkit-animation-name: quantumWizSpinnerFillUnfill, quantumWizSpinnerRot; animation-name: quantumWizSpinnerFillUnfill, quantumWizSpinnerRot; stroke: #1A73E8;}.DShyMc-AaTFfe .tUJKGd:not(.xp2dJ).ndcsBf.boxOzd,.DShyMc-AaTFfe .tUJKGd:not(.xp2dJ).ndcsBf.idtp4e,.DShyMc-AaTFfe .tUJKGd:not(.xp2dJ).ndcsBf .boxOzd,.DShyMc-AaTFfe .tUJKGd:not(.xp2dJ).ndcsBf .idtp4e,.DShyMc-AaTFfe .ZoT1D.ndcsBf.boxOzd,.DShyMc-AaTFfe .ZoT1D.ndcsBf.idtp4e,.DShyMc-AaTFfe .ZoT1D.ndcsBf .boxOzd,.DShyMc-AaTFfe .ZoT1D.ndcsBf .idtp4e {background-color: #E8F0FE;}.DShyMc-AaTFfe .tUJKGd:not(.xp2dJ):not(.rZXyy):hover.j6KDAd,.DShyMc-AaTFfe .tUJKGd:not(.xp2dJ):not(.rZXyy):hover.idtp4e,.DShyMc-AaTFfe .tUJKGd:not(.xp2dJ):not(.rZXyy):hover .j6KDAd,.DShyMc-AaTFfe .tUJKGd:not(.xp2dJ):not(.rZXyy):hover .idtp4e,.DShyMc-AaTFfe .ZoT1D:hover.j6KDAd,.DShyMc-AaTFfe .ZoT1D:hover.idtp4e,.DShyMc-AaTFfe .ZoT1D:hover .j6KDAd,.DShyMc-AaTFfe .ZoT1D:hover .idtp4e {background-color: #E8F0FE;}.DShyMc-AaTFfe .nRLOzd:hover, .DShyMc-AaTFfe .nRLOzd:hover *, .DShyMc-AaTFfe .nRLOzd:focus, .DShyMc-AaTFfe .nRLOzd:focus *{color: #185ABC}.DShyMc-AaTFfe .ra2NV {background-image: radial-gradient( 25rem 18.75rem ellipse at bottom right,#1A73E8, transparent );}.DShyMc-AaTFfe .eumXzf:after {border-color: #185ABC;}</style><link href="./Variable_cls_files/css(2)" rel="stylesheet"><link href="./Variable_cls_files/icon" rel="stylesheet"><script nonce="">var AF_initDataKeys = []
; var AF_dataServiceRequests = {}; var AF_initDataChunkQueue = []; var AF_initDataCallback; var AF_initDataInitializeCallback; if (AF_initDataInitializeCallback) {AF_initDataInitializeCallback(AF_initDataKeys, AF_initDataChunkQueue, AF_dataServiceRequests);}if (!AF_initDataCallback) {AF_initDataCallback = function(chunk) {AF_initDataChunkQueue.push(chunk);};}</script><link rel="stylesheet" href="./Variable_cls_files/rs=AK3ymSXNwXkJuK3U4imjJmhTCnRGEb7lPg" data-id="_cl"><script async="" type="text/javascript" charset="UTF-8" src="./Variable_cls_files/rs=AA2YrTt_OJqbWnkMjMONweMkFGu-2q-ILg" nonce=""></script><link type="text/css" rel="stylesheet" href="./Variable_cls_files/rs=AA2YrTszUE1lFZmFXVA54XWasIZ1sOlgkA"><script type="text/javascript" charset="UTF-8" src="./Variable_cls_files/521PoRGnh7h8BVOMyCpHrhejufpyvF5vdQBdJpCoVT0.js.download" nonce=""></script><script async="" src="./Variable_cls_files/lazy.min.js.download" nonce=""></script><style>.DShyMc-MTE3MzM0OTI3NDE3.bFjUmb-Ysl7Fe, .DShyMc-MTE3MzM0OTI3NDE3 .bFjUmb-Ysl7Fe {background-color: #e8f0fe;}.DShyMc-MTE3MzM0OTI3NDE3.bFjUmb-Wvd9Cc, .DShyMc-MTE3MzM0OTI3NDE3 .bFjUmb-Wvd9Cc, .DShyMc-MTE3MzM0OTI3NDE3.CNpREd.bFjUmb-Wvd9Cc, .DShyMc-MTE3MzM0OTI3NDE3.CNpREd .bFjUmb-Wvd9Cc {background-color: #4285f4;}.DShyMc-MTE3MzM0OTI3NDE3.bFjUmb-Tvm9db, .DShyMc-MTE3MzM0OTI3NDE3 .bFjUmb-Tvm9db, .DShyMc-MTE3MzM0OTI3NDE3.CNpREd.bFjUmb-Tvm9db, .DShyMc-MTE3MzM0OTI3NDE3.CNpREd .bFjUmb-Tvm9db {background-color: #1967d2;}.DShyMc-MTE3MzM0OTI3NDE3.yxp05b-Wvd9Cc, .DShyMc-MTE3MzM0OTI3NDE3.CNpREd.yxp05b-Wvd9Cc, .DShyMc-MTE3MzM0OTI3NDE3 .yxp05b-Wvd9Cc {border-color: #4285f4;}.DShyMc-MTE3MzM0OTI3NDE3.VnOHwf-Ysl7Fe, .DShyMc-MTE3MzM0OTI3NDE3 .VnOHwf-Ysl7Fe, .DShyMc-MTE3MzM0OTI3NDE3.CNpREd .VnOHwf-Ysl7Fe {color: #e8f0fe;}.DShyMc-MTE3MzM0OTI3NDE3.VnOHwf-Wvd9Cc, .DShyMc-MTE3MzM0OTI3NDE3 .VnOHwf-Wvd9Cc, .DShyMc-MTE3MzM0OTI3NDE3.CNpREd .VnOHwf-Wvd9Cc {color: #4285f4;}.DShyMc-MTE3MzM0OTI3NDE3.VnOHwf-Tvm9db, .DShyMc-MTE3MzM0OTI3NDE3 .VnOHwf-Tvm9db, .DShyMc-MTE3MzM0OTI3NDE3.CNpREd .VnOHwf-Tvm9db {color: #1967d2;}.DShyMc-MTE3MzM0OTI3NDE3 .tgNIJf-Ysl7Fe:focus {border-color: #e8f0fe;}.DShyMc-MTE3MzM0OTI3NDE3 .ndcsBf.cjzpkc-Wvd9Cc, .DShyMc-MTE3MzM0OTI3NDE3 .tgNIJf-Wvd9Cc:focus {border-color: #4285f4;}.DShyMc-MTE3MzM0OTI3NDE3 .u3bW4e .zZN2Lb-Wvd9Cc, .DShyMc-MTE3MzM0OTI3NDE3 .zZN2Lb-Wvd9Cc:focus, .DShyMc-MTE3MzM0OTI3NDE3 .maXJsd:focus .zZN2Lb-Wvd9Cc {color: #4285f4;}.DShyMc-MTE3MzM0OTI3NDE3 .P3W0Dd-Ysl7Fe:focus, .DShyMc-MTE3MzM0OTI3NDE3.maXJsd:focus .P3W0Dd-Ysl7Fe, .DShyMc-MTE3MzM0OTI3NDE3 .maXJsd:focus .P3W0Dd-Ysl7Fe {background-color: #e8f0fe;}.DShyMc-MTE3MzM0OTI3NDE3 .VBEdtc-Wvd9Cc:hover, .DShyMc-MTE3MzM0OTI3NDE3.MymH0d:hover .VBEdtc-Wvd9Cc, .DShyMc-MTE3MzM0OTI3NDE3 .MymH0d:hover .VBEdtc-Wvd9Cc {color: #4285f4;}.DShyMc-MTE3MzM0OTI3NDE3.MymH0d:hover .UISY8d-Tvm9db, .DShyMc-MTE3MzM0OTI3NDE3.CNpREd.MymH0d:hover .UISY8d-Tvm9db, .DShyMc-MTE3MzM0OTI3NDE3 .MymH0d:hover .UISY8d-Tvm9db {background-color: #4285f4;}.DShyMc-MTE3MzM0OTI3NDE3 .UISY8d-Ysl7Fe:hover, .DShyMc-MTE3MzM0OTI3NDE3.MymH0d:hover .UISY8d-Ysl7Fe, .DShyMc-MTE3MzM0OTI3NDE3 .MymH0d:hover .UISY8d-Ysl7Fe {background-color: #e8f0fe;}.DShyMc-MTE3MzM0OTI3NDE3 .mxmXhf {color: #1967d2; fill: #1967d2;}.DShyMc-MTE3MzM0OTI3NDE3 .EmVfjc.qs41qe .wKSUOe, .DShyMc-MTE3MzM0OTI3NDE3 .EmVfjc.sf4e6b .wKSUOe {-webkit-animation-name: quantumWizSpinnerFillUnfill, quantumWizSpinnerRot; animation-name: quantumWizSpinnerFillUnfill, quantumWizSpinnerRot; stroke: #4285f4;}.DShyMc-MTE3MzM0OTI3NDE3 .tUJKGd:not(.xp2dJ).ndcsBf.boxOzd,.DShyMc-MTE3MzM0OTI3NDE3 .tUJKGd:not(.xp2dJ).ndcsBf.idtp4e,.DShyMc-MTE3MzM0OTI3NDE3 .tUJKGd:not(.xp2dJ).ndcsBf .boxOzd,.DShyMc-MTE3MzM0OTI3NDE3 .tUJKGd:not(.xp2dJ).ndcsBf .idtp4e,.DShyMc-MTE3MzM0OTI3NDE3 .ZoT1D.ndcsBf.boxOzd,.DShyMc-MTE3MzM0OTI3NDE3 .ZoT1D.ndcsBf.idtp4e,.DShyMc-MTE3MzM0OTI3NDE3 .ZoT1D.ndcsBf .boxOzd,.DShyMc-MTE3MzM0OTI3NDE3 .ZoT1D.ndcsBf .idtp4e {background-color: #e8f0fe;}.DShyMc-MTE3MzM0OTI3NDE3 .tUJKGd:not(.xp2dJ):not(.rZXyy):hover.j6KDAd,.DShyMc-MTE3MzM0OTI3NDE3 .tUJKGd:not(.xp2dJ):not(.rZXyy):hover.idtp4e,.DShyMc-MTE3MzM0OTI3NDE3 .tUJKGd:not(.xp2dJ):not(.rZXyy):hover .j6KDAd,.DShyMc-MTE3MzM0OTI3NDE3 .tUJKGd:not(.xp2dJ):not(.rZXyy):hover .idtp4e,.DShyMc-MTE3MzM0OTI3NDE3 .ZoT1D:hover.j6KDAd,.DShyMc-MTE3MzM0OTI3NDE3 .ZoT1D:hover.idtp4e,.DShyMc-MTE3MzM0OTI3NDE3 .ZoT1D:hover .j6KDAd,.DShyMc-MTE3MzM0OTI3NDE3 .ZoT1D:hover .idtp4e {background-color: #e8f0fe;}.DShyMc-MTE3MzM0OTI3NDE3 .nRLOzd:hover, .DShyMc-MTE3MzM0OTI3NDE3 .nRLOzd:hover *, .DShyMc-MTE3MzM0OTI3NDE3 .nRLOzd:focus, .DShyMc-MTE3MzM0OTI3NDE3 .nRLOzd:focus *{color: #1967d2}.DShyMc-MTE3MzM0OTI3NDE3 .ra2NV {background-image: radial-gradient( 25rem 18.75rem ellipse at bottom right,#4285f4, transparent );}.DShyMc-MTE3MzM0OTI3NDE3 .eumXzf:after {border-color: #1967d2;}.DShyMc-MTE3MzM0OTI3NDE3 .zKHdkd .cXrdqd, .DShyMc-MTE3MzM0OTI3NDE3 .kPBwDb {background-color: #4285f4;}.DShyMc-MTE3MzM0OTI3NDE3 .zKHdkd .zHQkBf:not([disabled]):focus ~ .snByac, .DShyMc-MTE3MzM0OTI3NDE3 .edhGSc.u3bW4e > .oJeWuf > .snByac {color: #4285f4;}.DShyMc-MTE3MzM0OTI3NDE3 .bkIpNd .uHMk6b {border-color: #e8f0fe;}.DShyMc-MTE3MzM0OTI3NDE3 .zJKIV .nQOrEb, .DShyMc-MTE3MzM0OTI3NDE3 .zJKIV.RDPZE .nQOrEb, .DShyMc-MTE3MzM0OTI3NDE3 .zJKIV.N2RpBe .Id5V1, .DShyMc-MTE3MzM0OTI3NDE3 .LsSwGf:not(.SWVgue):not(.RDPZE).N2RpBe .espmsb {border-color: #4285f4;}.DShyMc-MTE3MzM0OTI3NDE3 .LsSwGf:not(.SWVgue):not(.RDPZE).N2RpBe > .MLPG7 {border-color: #4285f4; opacity: .50;}.DShyMc-MTE3MzM0OTI3NDE3 .zJKIV.i9xfbb > .MbhUzd, .DShyMc-MTE3MzM0OTI3NDE3 .zJKIV.u3bW4e > .MbhUzd, .DShyMc-MTE3MzM0OTI3NDE3 .LsSwGf:not(.SWVgue).i9xfbb > .MbhUzd, .DShyMc-MTE3MzM0OTI3NDE3 .LsSwGf:not(.SWVgue).u3bW4e > .MbhUzd {background-color: #e8f0fe;}.DShyMc-MTE3MzM0OTI3NDE3 .HQ8yf:not(.RDPZE), .DShyMc-MTE3MzM0OTI3NDE3 .HQ8yf:not(.RDPZE) a {color: #4285f4;}.DShyMc-MTE3MzM0OTI3NDE3 .HQ8yf.u3bW4e .CeoRYc {background-color: rgba(66,133,244,0.15);}.DShyMc-MTE3MzM0OTI3NDE3 .HQ8yf .MbhUzd {background-image: radial-gradient( circle farthest-side,rgba(66,133,244,0.25),rgba(66,133,244,0.25) 80%,#4285f4 100% );}.DShyMc-MTE3MzM0OTI3NDE3 .uO32ac, .DShyMc-MTE3MzM0OTI3NDE3 .ypv4re {border-bottom: 1px solid #4285f4;}.DShyMc-MTE3MzM0OTI3NDE3 .DqwBN:not(.RDPZE) .TpQm9d,.DShyMc-MTE3MzM0OTI3NDE3 .l3F1ye:not(.RDPZE) .TpQm9d {color: #1967d2; fill: #1967d2;}.DShyMc-MTE3MzM0OTI3NDE3 .l3F1ye.j6PN2:not(.RDPZE) .TpQm9d {color: #8AB4F8; fill: #8AB4F8;}.DShyMc-MTE3MzM0OTI3NDE3 .QkA63b:not(.RDPZE),.DShyMc-MTE3MzM0OTI3NDE3 .Y5sE8d:not(.RDPZE){background-color: #1967d2;}.DShyMc-MTE3MzM0OTI3NDE3 .QkA63b:not(.RDPZE):hover,.DShyMc-MTE3MzM0OTI3NDE3 .Y5sE8d:not(.RDPZE):hover,.DShyMc-MTE3MzM0OTI3NDE3 .QkA63b:not(.RDPZE).u3bW4e,.DShyMc-MTE3MzM0OTI3NDE3 .Y5sE8d:not(.RDPZE).u3bW4e {box-shadow: 0px 2px 1px -1px rgba(25,103,210,0.2), 0px 1px 1px 0px rgba(25,103,210,0.14), 0px 1px 3px 0px rgba(25,103,210,0.12);}.DShyMc-MTE3MzM0OTI3NDE3 .QkA63b:not(.RDPZE).iWO5td,.DShyMc-MTE3MzM0OTI3NDE3 .Y5sE8d:not(.RDPZE).qs41qe {box-shadow: 0px 3px 5px -1px rgba(25,103,210,0.2), 0px 6px 10px 0px rgba(25,103,210,0.14), 0px 1px 18px 0px rgba(25,103,210,0.12);}.DShyMc-MTE3MzM0OTI3NDE3 .p0oLxb:not(.RDPZE).aS18D {background-color: #1967d2; box-shadow: 0 1px 2px 0 rgba(25,103,210,0.3), 0 2px 6px 2px rgba(25,103,210,0.15);}.DShyMc-MTE3MzM0OTI3NDE3 .p0oLxb:not(.RDPZE).aS18D:hover {box-shadow: 0 2px 3px 0 rgba(25,103,210,0.3), 0 6px 10px 4px rgba(25,103,210,0.15);}.DShyMc-MTE3MzM0OTI3NDE3 .DqwBN:not(.RDPZE),.DShyMc-MTE3MzM0OTI3NDE3 .l3F1ye:not(.RDPZE),.DShyMc-MTE3MzM0OTI3NDE3 .BEAGS:not(.RDPZE),.DShyMc-MTE3MzM0OTI3NDE3 .AeAAkf:not(.RDPZE) {color: #1967d2;}.DShyMc-MTE3MzM0OTI3NDE3 .l3F1ye.j6PN2:not(.RDPZE) {color: #8AB4F8;}.DShyMc-MTE3MzM0OTI3NDE3 .wwnMtb:not(.RDPZE),.DShyMc-MTE3MzM0OTI3NDE3 .OZ6W0d:not(.RDPZE) {color: #1967d2; fill: #1967d2;}.DShyMc-MTE3MzM0OTI3NDE3 .wwnMtb:not(.RDPZE):hover,.DShyMc-MTE3MzM0OTI3NDE3 .OZ6W0d:not(.RDPZE):hover {background-color: rgba(25,103,210,0.08);}.DShyMc-MTE3MzM0OTI3NDE3 .wwnMtb:not(.RDPZE).u3bW4e,.DShyMc-MTE3MzM0OTI3NDE3 .OZ6W0d:not(.RDPZE).u3bW4e {background-color: rgba(25,103,210,0.12);}.DShyMc-MTE3MzM0OTI3NDE3 .wwnMtb:not(.RDPZE).u3bW4e:hover,.DShyMc-MTE3MzM0OTI3NDE3 .OZ6W0d:not(.RDPZE).u3bW4e:hover {background-color: rgba(25,103,210,0.16);}.DShyMc-MTE3MzM0OTI3NDE3 .BEAGS.iWO5td,.DShyMc-MTE3MzM0OTI3NDE3 .AeAAkf.qs41qe {box-shadow: 0px 2px 1px -1px rgba(25,103,210,0.2), 0px 1px 1px 0px rgba(25,103,210,0.14), 0px 1px 3px 0px rgba(25,103,210,0.12);}.DShyMc-MTE3MzM0OTI3NDE3 .DqwBN .MbhUzd,.DShyMc-MTE3MzM0OTI3NDE3 .l3F1ye .MbhUzd,.DShyMc-MTE3MzM0OTI3NDE3 .BEAGS .MbhUzd,.DShyMc-MTE3MzM0OTI3NDE3 .AeAAkf .MbhUzd,.DShyMc-MTE3MzM0OTI3NDE3 .AeAAkf .MbhUzd,.DShyMc-MTE3MzM0OTI3NDE3 .OZ6W0d .MbhUzd {background-image: radial-gradient( circle farthest-side,rgba(25,103,210,0.16),rgba(25,103,210,0.16) 80%,rgba(25,103,210,0) 100% );}.DShyMc-MTE3MzM0OTI3NDE3 .l3F1ye.j6PN2 .MbhUzd {background-image: radial-gradient( circle farthest-side,rgba(138,180,248,0.16),rgba(138,180,248,0.16) 80%,rgba(138,180,248,0) 100% );}.DShyMc-MTE3MzM0OTI3NDE3 .AeAAkf:not(.RDPZE) .CeoRYc,.DShyMc-MTE3MzM0OTI3NDE3 .BEAGS:not(.RDPZE) .CeoRYc,.DShyMc-MTE3MzM0OTI3NDE3 .l3F1ye:not(.RDPZE) .CeoRYc,.DShyMc-MTE3MzM0OTI3NDE3 .DqwBN:not(.RDPZE) .CeoRYc {background-color: #1967d2;}.DShyMc-MTE3MzM0OTI3NDE3 .l3F1ye.j6PN2:not(.RDPZE) .CeoRYc  {background-color: #8AB4F8;}.DShyMc-MTE3MzM0OTI3NDE3 .AeAAkf:not(.RDPZE):hover,.DShyMc-MTE3MzM0OTI3NDE3 .AeAAkf:not(.RDPZE).u3bW4e,.DShyMc-MTE3MzM0OTI3NDE3 .BEAGS:not(.RDPZE):hover,.DShyMc-MTE3MzM0OTI3NDE3 .BEAGS:not(.RDPZE).u3bW4e {border-color: rgba(66,133,244,0.2);}.DShyMc-MTE3MzM0OTI3NDE3 .DqwBN:not(.RDPZE):hover .CeoRYc,.DShyMc-MTE3MzM0OTI3NDE3 .DqwBN:not(.RDPZE).u3bW4e .CeoRYc,.DShyMc-MTE3MzM0OTI3NDE3 .l3F1ye:not(.RDPZE):hover .CeoRYc,.DShyMc-MTE3MzM0OTI3NDE3 .l3F1ye:not(.RDPZE).u3bW4e .CeoRYc {background-color: #4285f4;}.DShyMc-MTE3MzM0OTI3NDE3 .l3F1ye.j6PN2:not(.RDPZE):hover .CeoRYc,.DShyMc-MTE3MzM0OTI3NDE3 .l3F1ye.j6PN2:not(.RDPZE).u3bW4e .CeoRYc {background-color: #8AB4F8;}.DShyMc-MTE3MzM0OTI3NDE3 .aiSeRd:not(.RDPZE).N2RpBe,.DShyMc-MTE3MzM0OTI3NDE3 .aiSeRd:not(.RDPZE).B6Vhqe {border-color: #4285f4;}.DShyMc-MTE3MzM0OTI3NDE3 .aiSeRd:not(.RDPZE):hover .MbhUzd,.DShyMc-MTE3MzM0OTI3NDE3 .aiSeRd:not(.RDPZE):focus .MbhUzd,.DShyMc-MTE3MzM0OTI3NDE3 .aiSeRd:not(.RDPZE).N2RpBe .MbhUzd.DShyMc-MTE3MzM0OTI3NDE3 .aiSeRd:not(.RDPZE).i9xfbb .MbhUzd {background-color: rgba(25,103,210,0.08);}.DShyMc-MTE3MzM0OTI3NDE3 .d7L4fc:hover .hYsg7c,.DShyMc-MTE3MzM0OTI3NDE3 .NtlN8c:hover  .hYsg7c {border-color: #e8f0fe;}.DShyMc-MTE3MzM0OTI3NDE3 .d7L4fc:hover .MbhUzd,.DShyMc-MTE3MzM0OTI3NDE3 .NtlN8c:hover  .MbhUzd {background-color: rgba(25,103,210,0.04);}.DShyMc-MTE3MzM0OTI3NDE3 .d7L4fc .hYsg7c .nQOrEb,.DShyMc-MTE3MzM0OTI3NDE3 .d7L4fc .hYsg7c.RDPZE .nQOrEb,.DShyMc-MTE3MzM0OTI3NDE3 .d7L4fc .hYsg7c.N2RpBe .Id5V1 {border-color: #4285f4;}.DShyMc-MTE3MzM0OTI3NDE3 .d7L4fc .hYsg7c:not(.RDPZE).i9xfbb > .MbhUzd,.DShyMc-MTE3MzM0OTI3NDE3 .d7L4fc .hYsg7c:not(.RDPZE).u3bW4e > .MbhUzd {background-color: rgba(25,103,210,0.08);}.DShyMc-MTE3MzM0OTI3NDE3 .SWVgue:not(.RDPZE).N2RpBe .espmsb {border-color: #4285f4;}.DShyMc-MTE3MzM0OTI3NDE3 .SWVgue.RDPZE.N2RpBe .espmsb {border-color: #bdd4fb;}.DShyMc-MTE3MzM0OTI3NDE3 .SWVgue:not(.RDPZE).N2RpBe .MLPG7 {border-color: rgba(66,133,244,0.3);}.DShyMc-MTE3MzM0OTI3NDE3 .SWVgue.RDPZE.N2RpBe .MLPG7 {border-color: #e3edfd;}.DShyMc-MTE3MzM0OTI3NDE3 .SWVgue:not(.RDPZE).N2RpBe:hover .MbhUzd {background-color: rgba(66,133,244,0.04);}.DShyMc-MTE3MzM0OTI3NDE3 .SWVgue:not(.RDPZE).qs41qe .MbhUzd,.DShyMc-MTE3MzM0OTI3NDE3 .SWVgue:not(.RDPZE).N2RpBe.u3bW4e .MbhUzd,.DShyMc-MTE3MzM0OTI3NDE3 .SWVgue:not(.RDPZE).N2RpBe:focus .MbhUzd {background-color: rgba(66,133,244,0.12);}.DShyMc-MTE3MzM0OTI3NDE3 .HyS0Qd:not(.RDPZE) .zHQkBf,.DShyMc-MTE3MzM0OTI3NDE3 .fWf7qe:not(.RDPZE) .tL9Q4c,.DShyMc-MTE3MzM0OTI3NDE3 .D3oBEe:not(.RDPZE) .zHQkBf,.DShyMc-MTE3MzM0OTI3NDE3 .AkVYk:not(.RDPZE) .tL9Q4c {caret-color: #4285f4;}.DShyMc-MTE3MzM0OTI3NDE3 .HyS0Qd:not(.RDPZE) .cXrdqd,.DShyMc-MTE3MzM0OTI3NDE3 .fWf7qe:not(.RDPZE) .cXrdqd,.DShyMc-MTE3MzM0OTI3NDE3 .vnnr5e:not(.RDPZE) .cXrdqd {background-color: #4285f4;}.DShyMc-MTE3MzM0OTI3NDE3 .D3oBEe:not(.RDPZE).u3bW4e:not(.IYewr) .oJeWuf:before,.DShyMc-MTE3MzM0OTI3NDE3 .AkVYk:not(.RDPZE).u3bW4e:not(.IYewr) .oJeWuf:before {border-color: #4285f4;}.DShyMc-MTE3MzM0OTI3NDE3 .HyS0Qd:not(.RDPZE).u3bW4e .snByac,.DShyMc-MTE3MzM0OTI3NDE3 .HyS0Qd input:not([disabled]):focus ~ .snByac,.DShyMc-MTE3MzM0OTI3NDE3 .fWf7qe:not(.RDPZE).u3bW4e .snByac,.DShyMc-MTE3MzM0OTI3NDE3 .D3oBEe:not(.RDPZE).u3bW4e .snByac,.DShyMc-MTE3MzM0OTI3NDE3 .D3oBEe input:not([disabled]):focus ~ .snByac,.DShyMc-MTE3MzM0OTI3NDE3 .AkVYk:not(.RDPZE).u3bW4e .snByac {color: #1967d2;}.DShyMc-MTE3MzM0OTI3NDE3 .ybOdnf:not(.RDPZE).iWO5td,.DShyMc-MTE3MzM0OTI3NDE3 .ybOdnf:not(.RDPZE) .OA0qNb .LMgvRb[aria-selected="true"],.DShyMc-MTE3MzM0OTI3NDE3 .NqFm6:not(.RDPZE) .tWfTvb [role="option"][aria-selected="true"] {background-color: #e8f0fe;}.DShyMc-MTE3MzM0OTI3NDE3 .RpYYWb:not(.RDPZE).fy1E5c .Ce1Y1c {color: #4285f4; fill: #4285f4;}.DShyMc-MTE3MzM0OTI3NDE3 .mRipsb {background-color: #4285f4;}.DShyMc-MTE3MzM0OTI3NDE3 .bJuVn.KKjvXb {background-color: #1967d2;}.DShyMc-MTE3MzM0OTI3NDE3 .bJuVn.KKjvXb:before {background: linear-gradient(to top, #1967d2, transparent);}.DShyMc-MTE3MzM0OTI3NDE3 .bJuVn.KKjvXb:after {background: linear-gradient(to bottom, #1967d2, transparent);}.DShyMc-MTE3MzM0OTI3NDE3 .bJuVn.u3bW4e.KKjvXb, .DShyMc-MTE3MzM0OTI3NDE3 .bJuVn.KKjvXb:hover {background-color: #2b73d6;}.DShyMc-MTE3MzM0OTI3NDE3 .bJuVn.u3bW4e.KKjvXb:before, .DShyMc-MTE3MzM0OTI3NDE3 .bJuVn.KKjvXb:hover:before {background: linear-gradient(to top, #2b73d6, transparent);}.DShyMc-MTE3MzM0OTI3NDE3 .bJuVn.u3bW4e.KKjvXb:after, .DShyMc-MTE3MzM0OTI3NDE3 .bJuVn.KKjvXb:hover:after {background: linear-gradient(to bottom, #2b73d6, transparent);}.DShyMc-MTE3MzM0OTI3NDE3 .pAlOFe {color: #1967d2; fill: #1967d2;}</style><link type="image/png" rel="icon" href="https://ssl.gstatic.com/classroom/favicon_blue.png"></head><body class="gyaw1d ySjuvd ar1wE DShyMc-MTE3MzM0OTI3NDE3 nTrDbc GAP4ve xSXax AJlUyd CPYzFb V7D6ud fKVgu nk6WKe EIlDfe ndfHFb-c4YZDc-qbOKL-OEVmcd" jsmodel="elptZb;PuTOgd" data-no-view="true" id="yDmH0d" jsaction="GvneHb:.CLIENT;MmB7ud:.CLIENT;zkkUY:.CLIENT"><div class="FJJygb A2eYae" aria-hidden="true"><div class="Sslefe Z3WPhc" aria-live="assertive" aria-atomic="true"></div><div class="RmhvCc Z3WPhc" aria-live="polite" aria-atomic="true"></div><div class="w2ifj Z3WPhc" aria-live="polite" aria-atomic="true"><div><div class="LhKRUe  CG2qQ" jsowner="ow46" style="display: none;"><span class=""><html-blob>You're invited to teach this class</html-blob></span><span class="fPqOAb"></span><div jsshadow="" role="presentation" class="uArJ5e UQuaGc l3F1ye j6PN2 eoooNd " jscontroller="VXdfxd" jsaction="click:cOuCgd; mousedown:UX7yZ; mouseup:lbsD7e; mouseenter:tfO1Yc; mouseleave:JywGue;focus:AHmuwe; blur:O22p3e; contextmenu:mg9Pef" aria-disabled="false"><a class="IrxBzb TpQm9d" href="https://classroom.google.com/invite/accept/MTE3MzM0OTI3NDE3?role=2&amp;continue=%2Fu%2F0%2Fc%2FMTE3MzM0OTI3NDE3%2Fp%2FMTI5NzEzNDQ3MjY0%2Fdetails&amp;authuser=0" data-force-full-page-load="true"><div class="Fvio9d MbhUzd" jsname="ksKsZd"></div><div class="e19J0b CeoRYc"></div><span jsslot="" class="l4V7wb Fxmcue"><span class="NPEfkd RveJvd snByac">Accept</span></span></a></div></div></div><div><div class="LhKRUe  D0cJPb" jsowner="ow46"><div class="U51CBd QRiHXd"><svg focusable="false" width="24" height="24" viewBox="0 0 24 24" class=" NMm5M"><path d="M20.54 5.23l-1.39-1.68C18.88 3.21 18.47 3 18 3H6c-.47 0-.88.21-1.16.55L3.46 5.23C3.17 5.57 3 6.02 3 6.5V19c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V6.5c0-.48-.17-.93-.46-1.27zM6.24 5h11.52l.83 1H5.42l.82-1zM5 19V8h14v11H5zm11-5.5l-4 4-4-4 1.41-1.41L11 13.67V10h2v3.67l1.59-1.59L16 13.5z"></path></svg></div><span class=""><html-blob><span class="Y5vSD">Class is archived. Restore it to add or edit anything.</span><span class="nforOe">Class has been archived by your teacher. You can't add or edit anything.</span></html-blob></span><span class="fPqOAb"></span><div jsaction="JIbuQc:E8fGCc"><div jsshadow="" role="button" class="uArJ5e UQuaGc l3F1ye j6PN2 eoooNd Y5vSD" jscontroller="VXdfxd" jsaction="click:cOuCgd; mousedown:UX7yZ; mouseup:lbsD7e; mouseenter:tfO1Yc; mouseleave:JywGue;touchstart:p6p2H; touchmove:FwuNnf; touchend:yfqBxc(preventMouseEvents=true|preventDefault=true); touchcancel:JMtRjd;focus:AHmuwe; blur:O22p3e; contextmenu:mg9Pef" aria-label="Restore archived class" aria-disabled="false" tabindex="0"><div class="Fvio9d MbhUzd" jsname="ksKsZd"></div><div class="e19J0b CeoRYc"></div><span jsslot="" class="l4V7wb Fxmcue"><span class="NPEfkd RveJvd snByac">Restore</span></span></div></div></div></div></div><div class="Ub9MKb Z3WPhc"></div></div><nav jscontroller="H3hxgc" jsaction="tLnfOb:spIfde" class="joJglb dxu4Dd" role="navigation" aria-hidden="true"><div class="QRiHXd"><div class="FXKA9c"><div class="XIpEib QRiHXd"><div class="k43Owe mmOZjd" data-focus-id="JUeBdc"><div><div jscontroller="YgklIf" jsaction="rcuQ6b:npT2md;JIbuQc:VJ10Y; keydown:I481le;B3adYc:wAhJT" jsmodel="j7IAI" data-include-user-lists="true" data-course-states="1" soy-server-key="6:TflAbd" id="ow19" __is_owner="true"><div role="button" class="uArJ5e Y5FYJe cjq2Db xSP5ic oxacD" jscontroller="VXdfxd" jsaction="click:cOuCgd; mousedown:UX7yZ; mouseup:lbsD7e; mouseenter:tfO1Yc; mouseleave:JywGue;touchstart:p6p2H; touchmove:FwuNnf; touchend:yfqBxc(preventMouseEvents=true|preventDefault=true); touchcancel:JMtRjd;focus:AHmuwe; blur:O22p3e; contextmenu:mg9Pef;" jsshadow="" jsname="LgbsSe" aria-label="Main Menu" tabindex="0" data-tooltip="Main Menu" data-tooltip-vertical-offset="-12" data-tooltip-horizontal-offset="0"><div class="PDXc1b MbhUzd" jsname="ksKsZd"></div><span jsslot="" class="XuQwKc"><span class="GmuOkf"><svg width="24" height="24" viewBox="0 0 24 24" focusable="false" class=" NMm5M"><path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"></path></svg></span></span></div></div></div></div><h1 class="wy758b"><a class="onkcGd nRLOzd" target="_blank" href="https://classroom.google.com/u/0/c/MTE3MzM0OTI3NDE3" data-focus-id="/u/0/c/MTE3MzM0OTI3NDE3"><span id="UGb2Qe" class="YVvGBb kvxTzd A6dC2c">Sanjeev-Python-8:Am</span><span class="YVvGBb dDKhVc">Weekdays</span></a></h1></div></div><div class="mkkSdf VHRSDf"><div class="xHPsid"></div></div><div class="Mtd4hb QRiHXd" soy-server-key="6:fgDyxf"><div class="fB7J9c kWv2Xb QRiHXd"></div><div class="PYWmSe Oe4zIb"><div class="neGRTd"><div class="gb_sa gb_he gb_4a gb_ta" id="gb" style="background-color:transparent"><div class="gb_3c gb_0a gb_2c" ng-non-bindable="" data-ogsr-up=""><div class="gb_4c"><div class="gb_Uc"><div class="gb_C gb_nd gb_i gb_1f" data-ogsr-fb="true" data-ogsr-alt="" id="gbwa"><div class="gb_0f"><a class="gb_D" aria-label="Google apps" href="https://www.google.co.in/intl/en/about/products" aria-expanded="false" role="button" tabindex="0"><svg class="gb_cf" focusable="false" viewBox="0 0 24 24"><path d="M6,8c1.1,0 2,-0.9 2,-2s-0.9,-2 -2,-2 -2,0.9 -2,2 0.9,2 2,2zM12,20c1.1,0 2,-0.9 2,-2s-0.9,-2 -2,-2 -2,0.9 -2,2 0.9,2 2,2zM6,20c1.1,0 2,-0.9 2,-2s-0.9,-2 -2,-2 -2,0.9 -2,2 0.9,2 2,2zM6,14c1.1,0 2,-0.9 2,-2s-0.9,-2 -2,-2 -2,0.9 -2,2 0.9,2 2,2zM12,14c1.1,0 2,-0.9 2,-2s-0.9,-2 -2,-2 -2,0.9 -2,2 0.9,2 2,2zM16,6c0,1.1 0.9,2 2,2s2,-0.9 2,-2 -0.9,-2 -2,-2 -2,0.9 -2,2zM12,8c1.1,0 2,-0.9 2,-2s-0.9,-2 -2,-2 -2,0.9 -2,2 0.9,2 2,2zM18,14c1.1,0 2,-0.9 2,-2s-0.9,-2 -2,-2 -2,0.9 -2,2 0.9,2 2,2zM18,20c1.1,0 2,-0.9 2,-2s-0.9,-2 -2,-2 -2,0.9 -2,2 0.9,2 2,2z"></path></svg></a></div></div></div><div class="gb_Ua gb_nd gb_Pg gb_i gb_1f"><div class="gb_0f gb_Za gb_Pg gb_i"><a class="gb_D gb_Ta gb_i" aria-label="Google Account: Sanath Kumar  
(sanath1975@gmail.com)" href="https://accounts.google.com/SignOutOptions?hl=en&amp;continue=https://classroom.google.com/u/0/c/MTE3MzM0OTI3NDE3/p/MTI5NzEzNDQ3MjY0" role="button" tabindex="0" aria-expanded="false"><img class="gb_Ka gbii" src="./Variable_cls_files/unnamed.jpg" srcset="https://lh3.googleusercontent.com/ogw/ADGmqu_y0Ujwrq1PMvx0GXO4i3MFGbDQqz7s3s5pvY-N=s32-c-mo 1x, https://lh3.googleusercontent.com/ogw/ADGmqu_y0Ujwrq1PMvx0GXO4i3MFGbDQqz7s3s5pvY-N=s64-c-mo 2x " alt="" aria-hidden="true" data-noaft=""></a><div class="gb_7a"></div><div class="gb_6a"></div></div></div></div><div class="gb_8a gb_F gb_l gb_9a" aria-label="Account Information" aria-hidden="true"><div class="gb_hb"><div class="gb_ib"><img class="gb_Oa gbip gb_mb" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" data-src="https://lh3.googleusercontent.com/ogw/ADGmqu_y0Ujwrq1PMvx0GXO4i3MFGbDQqz7s3s5pvY-N=s83-c-mo" data-srcset="https://lh3.googleusercontent.com/ogw/ADGmqu_y0Ujwrq1PMvx0GXO4i3MFGbDQqz7s3s5pvY-N=s83-c-mo 1x, https://lh3.googleusercontent.com/ogw/ADGmqu_y0Ujwrq1PMvx0GXO4i3MFGbDQqz7s3s5pvY-N=s192-c-mo 2x " title="Profile" alt="" aria-hidden="true"><div class="gb_qb gb_mb"><a class="gb_rb gb_kg gb_mb gb_pg" aria-label="Change profile picture." href="https://myaccount.google.com/?utm_source=OGB&amp;authuser=0" target="_blank"><svg class="gb_sb" enable-background="new 0 0 24 24" focusable="false" height="26" viewBox="0 0 24 24" width="18" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><path d="M20 5h-3.17L15 3H9L7.17 5H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 14H4V7h16v12zM12 9c-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4-1.79-4-4-4z"></path></svg></a></div></div><div class="gb_jb"><div class="gb_tb gb_ub">Sanath Kumar</div><div class="gb_vb">sanath1975@gmail.com</div><a class="gb_zb gb_lg gbp1 gb_7e gb_6c" href="https://myaccount.google.com/?utm_source=OGB&amp;authuser=0&amp;utm_medium=act" target="_blank">Manage your Google Account</a></div></div><div class="gb_Nb gb_Qb"><div class="gb_rg gb_nc gb_Ia"><div class="gb_oc"></div></div><div class="gb_og gb_Ub" aria-hidden="false"><a class="gb_Tb gb_4b" aria-hidden="true" href="https://classroom.google.com/?authuser=0" rel="noreferrer" target="_blank"><img class="gb_6b gb_mb" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" data-src="https://lh3.googleusercontent.com/ogw/ADGmqu_y0Ujwrq1PMvx0GXO4i3MFGbDQqz7s3s5pvY-N=s48-c-mo" alt="" aria-hidden="true"><div class="gb_Wb"><div><div class="gb_cc">Default</div></div><div class="gb_8b">Sanath Kumar</div><div class="gb_ac">sanath1975@gmail.com</div></div></a><a class="gb_Tb" href="https://classroom.google.com/?authuser=1" rel="noreferrer" target="_blank"><img class="gb_6b gb_mb" src="data:image/gif;base64,R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" data-src="https://lh3.googleusercontent.com/ogw/ADGmqu-hwV_7vKuQdm0cwDQ_0kXG0_ePrkJikyyirl4E=s48-c-mo" alt="" aria-hidden="true"><div class="gb_Wb"><div class="gb_8b">Sri Sri Avenue Sri Sri Avenue</div><div class="gb_ac">srisriavenuesarwa@gmail.com</div></div></a></div><div class="gb_Hb" aria-hidden="true"><svg class="gb_Ib" focusable="false" height="20" viewBox="0 0 20 20" width="20" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><path d="M0 0h20v20H0V0z" fill="none"></path><path d="M6.18 7L10 10.82 13.82 7 15 8.17l-5 5-5-5z"></path></svg></div><a class="gb_ec gb_Ia gb_Xb" href="https://myaccount.google.com/brandaccounts?authuser=0&amp;continue=https://classroom.google.com/u/0/c/MTE3MzM0OTI3NDE3/p/MTI5NzEzNDQ3MjY0&amp;service=https://classroom.google.com/%3Fauthuser%3D%24authuser" aria-hidden="true"><div class="gb_fc"><svg focusable="false" height="20" viewBox="0 0 24 24" width="20" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><path d="M19 3H5c-1.11 0-2 .9-2 2v14c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 2v10.79C16.52 14.37 13.23 14 12 14s-4.52.37-7 1.79V5h14zM5 19v-.77C6.74 16.66 10.32 16 12 16s5.26.66 7 2.23V19H5zm7-6c1.94 0 3.5-1.56 3.5-3.5S13.94 6 12 6 8.5 7.56 8.5 9.5 10.06 13 12 13zm0-5c.83 0 1.5.67 1.5 1.5S12.83 11 12 11s-1.5-.67-1.5-1.5S11.17 8 12 8z" fill="#5F6368"></path><path d="M0 0h24v24H0V0z" fill="none"></path></svg></div><div class="gb_hc gb_ic">All Brand accounts</div><svg class="gb_jc" focusable="false" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z" fill="#5F6368"></path><path d="M0 0h24v24H0z" fill="none"></path></svg></a></div><div class="gb_Zb" tabindex="-1"><a class="gb_Db gb_hg" href="https://accounts.google.com/AddSession?service=classroom&amp;continue=https://classroom.google.com/" target="_blank"><div class="gb_Eb"><svg class="gb_Fb" enable-background="new 0 0 24 24" focusable="false" height="20" viewBox="0 0 24 24" width="20" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><path d="M9 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0-6c1.1 0 2 .9 2 2s-.9 2-2 2-2-.9-2-2 .9-2 2-2zm0 7c-2.67 0-8 1.34-8 4v3h16v-3c0-2.66-5.33-4-8-4zm6 5H3v-.99C3.2 16.29 6.3 15 9 15s5.8 1.29 6 2v1zm3-4v-3h-3V9h3V6h2v3h3v2h-3v3h-2z"></path></svg></div><div class="gb_Jb">Add another account</div></a></div><div class="gb_ig gb_Kb"><a class="gb_Lb gb_mg gb_ug gb_7e gb_6c" id="gb_71" href="https://accounts.google.com/Logout?service=classroom&amp;continue=https://classroom.google.com/" target="_top">Sign out of all accounts</a></div><div class="gb_jg gb_Ab"><a class="gb_Bb gb_Pb" href="https://policies.google.com/privacy?hl=en&amp;authuser=0" target="_blank">Privacy Policy</a><span class="gb_Va" aria-hidden="true">•</span><a class="gb_Bb gb_Ob" href="https://myaccount.google.com/termsofservice?hl=en&amp;authuser=0" target="_blank">Terms of Service</a></div></div><div style="overflow: hidden; position: absolute; top: 0px; visibility: hidden; width: 328px; z-index: 991; height: 0px; margin-top: 57px; right: 0px; margin-right: 4px; transition: height 0.3s ease-in-out 0s;"><iframe role="presentation" frameborder="0" scrolling="no" src="./Variable_cls_files/app.html" style="height: 100%; width: 100%; visibility: hidden;"></iframe></div></div></div></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
_.Hd=!_.x||_.fc(9);_.Id=!_.x||_.fc(9);_.Jd=_.x&&!_.dc("9");_.Kd=function(){if(!_.p.addEventListener||!Object.defineProperty)return!1;var a=!1,b=Object.defineProperty({},"passive",{get:function(){a=!0}});try{_.p.addEventListener("test",_.va,b),_.p.removeEventListener("test",_.va,b)}catch(c){}return a}();
_.Ld=_.Pb?"webkitTransitionEnd":_.Lb?"otransitionend":"transitionend";

}catch(e){_._DumpException(e)}
try{
_.Md=function(a,b,c){if(!a.o)if(c instanceof Array){c=_.ia(c);for(var d=c.next();!d.done;d=c.next())_.Md(a,b,d.value)}else{d=(0,_.q)(a.F,a,b);var e=a.D+c;a.D++;b.setAttribute("data-eqid",e);a.B[e]=d;b&&b.addEventListener?b.addEventListener(c,d,!1):b&&b.attachEvent?b.attachEvent("on"+c,d):a.C.log(Error("m`"+b))}};

}catch(e){_._DumpException(e)}
try{
var Nd=document.querySelector(".gb_C .gb_D"),Od=document.querySelector("#gb.gb_Lc");Nd&&!Od&&_.Md(_.xd,Nd,"click");

}catch(e){_._DumpException(e)}
try{
var xh=function(a){_.I.call(this);this.D=a;this.A=null;this.o={};this.F={};this.j={}};_.n(xh,_.I);_.yh=function(a){if(a.A)return a.A;for(var b in a.j)if(a.j[b].Xe()&&a.j[b].Tb())return a.j[b];return null};xh.prototype.C=function(a){this.j[a]&&(_.yh(this)&&_.yh(this).Uc()==a||this.j[a].ve(!0))};xh.prototype.hb=function(a){for(var b in this.j)this.j[b].Xe()&&this.j[b].hb(a)};xh.prototype.B=function(a){this.j[a.Uc()]=a};var zh=new xh(_.M);_.Jc("dd",zh);

}catch(e){_._DumpException(e)}
try{
var lj=document.querySelector(".gb_Ua .gb_D"),mj=document.querySelector("#gb.gb_Lc");lj&&!mj&&_.Md(_.xd,lj,"click");

}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script></div></div></div><div class="meR3Qc TeZa2e"><div class="xHPsid" jsname="njTs3e"></div></div><div class="QANNMb FJJygb qwLQJ" aria-hidden="false" soy-server-key="6:iJuhKe"><div class="Olpyd Z3WPhc" aria-live="assertive" aria-atomic="true"></div><div class="tH9B6c Z3WPhc" aria-live="polite" aria-atomic="true"></div></div><div class="a6pJXc Q6ApZc aTtRxf"><div class="aP3ZPb kRqvHe bFjUmb-Ysl7Fe"><div class="bNpzdf kRqvHe bFjUmb-Wvd9Cc">&nbsp;</div><div class="G1kKid kRqvHe bFjUmb-Wvd9Cc">&nbsp;</div></div></div></nav><div class="v7wOcf ZGnOx" aria-hidden="true"><div jsmodel="PuTOgd IaLzN tZ2gdc ephE9e;" data-include-user-lists="true" jscontroller="UqV0cb" jsaction="rcuQ6b:rcuQ6b;uwjiC:rcuQ6b;QmtCl:.CLIENT;qVp5ue:.CLIENT;AE9bOd:.CLIENT;MmB7ud:.CLIENT;zkkUY:.CLIENT" data-view-id="28" tabindex="-1" class="kdAl3b"><div jsmodel="PTCFbe lkzLle" data-without-stream-item-materials="" class="fJ1Vac"><div class="P47N4e vUBwW m1PbN bFjUmb-Wvd9Cc pOf0gc"><svg focusable="false" width="24" height="24" viewBox="0 0 24 24" class=" NMm5M"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm0 14H4V4h16v12z"></path></svg></div><div class="EE538"><div jscontroller="QlRoyd" jsmodel="I8BbUd;UvJ3Mb;uJydvc;xeYtDf;" jsaction="rcuQ6b:rcuQ6b;uwjiC:rcuQ6b;wuANJc:rcuQ6b;wJx4ze:rcuQ6b"><div class="nl5VRd ypv4re"><div class="N5dSp"><h1 class="fOvfyc XjYjO VnOHwf-Tvm9db"><html-blob><span class="NjE5zd">Recording Link Of 22-July-20</span></html-blob></h1><div class="Nmpzvc"></div><div jscontroller="bkcTxe" jsaction="rcuQ6b:rcuQ6b;uwjiC:rcuQ6b;wuANJc:rcuQ6b;wJx4ze:rcuQ6b;aWRkAb:yG0upc" data-hide-copy-link="true" data-hide-delete="false" jsmodel="I8BbUd;PTCFbe" data-stream-item-id="129713447264" class="I0naMd" style="display: none;"><div jsshadow="" role="button" class="U26fgb JRtysb WzwrXb I12f0b K2mXPb wwnMtb oxacD" jscontroller="iSvg6e" jsaction="click:cOuCgd; mousedown:UX7yZ; mouseup:lbsD7e; mouseenter:tfO1Yc; mouseleave:JywGue; focus:AHmuwe; blur:O22p3e; contextmenu:mg9Pef;touchstart:p6p2H; touchmove:FwuNnf; touchend:yfqBxc(preventMouseEvents=true|preventDefault=true); touchcancel:JMtRjd;keydown:I481le" jsname="LgbsSe" tabindex="0" aria-haspopup="true" aria-expanded="false" data-dynamic="true" data-alignright="true" aria-label="Announcement options"><div class="NWlf3e MbhUzd" jsname="ksKsZd"></div><span jsslot="" class="MhXXcc oJeWuf"><span class="Lw7GHd snByac"><svg focusable="false" width="24" height="24" viewBox="0 0 24 24" class=" NMm5M"><path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"></path></svg></span></span></div></div></div><div class="rec5Nb VYVnSe QRiHXd"><div class="YVvGBb">Support Learnuva</div><div class="DwLQSc" aria-hidden="true">•</div><div class="YVvGBb">Jul 22&nbsp;(Edited Jul 23)</div></div><div class="W4hhKd"><div class="CzuI5c asQXV QRiHXd"></div><div class="asQXV hnID5d"></div></div></div></div><div jscontroller="AwTMWd" jsaction="rcuQ6b:rcuQ6b;uwjiC:rcuQ6b;KtPeHe:rcuQ6b;IKzbTb:Yo3LPb;wuANJc:.CLIENT" data-parent-id="PTCFbe" data-mode="1" data-copies-only="false" data-single-thumbnail-list="false" data-show-originality-analyses="false" data-forms-only="false" jsmodel="PTCFbe" data-include-stream-item-materials="true" class="KdU5eb  fIXHld SvPv8d"><div data-dom-id="https://vimeo.com/440559677/ad427927a1-0-3-4-https://vimeo.com/440559677/ad427927a1-Verify to Continue-$$-false-false-false-false-$-https://vimeo.com/440559677/ad427927a1" class="qNL8O ehXiW"><div class="po4Aib QRiHXd Aopndd " jsname="HzV7m" jsaction="JIbuQc:Rsbfue(Rsbfue)"><a class="uqZtlf x0HGk QRiHXd MymH0d maXJsd" target="_blank" aria-label="Attachment: Link to https://vimeo.com/440559677/ad427927a1" jsaction="LWntbc" href="https://vimeo.com/440559677/ad427927a1" title="Verify to Continue" data-focus-id="hSRGPd-https://vimeo.com/440559677/ad427927a1"><div class="bxp7vf mAeA1"><img jsname="q4uQmd" jsaction="error:dyBsCf" src="./Variable_cls_files/unnamed(1).jpg" aria-hidden="true" data-mime-type=""></div><div class="J5AvUe"><div class="A6dC2c bKJwEd VBEdtc-Wvd9Cc zZN2Lb-Wvd9Cc">Verify to Continue</div><div class="cSyPgb cfaOwb"><div class="kRYv9b YVvGBb">https://vimeo.com/440559677/ad427927a1</div></div></div></a><div class="PRmYNe QRiHXd" jsname="ncSfCe"></div></div></div><div data-dom-id="17IE1QXAl4H36TN92T92vNIchOi5xJYwE-1-3-2-Text-operators_cls.py-$2-false-false-false-false-$-https://drive.google.com/open?id=17IE1QXAl4H36TN92T92vNIchOi5xJYwE&amp;authuser=0" class="qNL8O ehXiW"><div class="po4Aib QRiHXd Aopndd " jsname="HzV7m" jsaction="JIbuQc:Rsbfue(Rsbfue)"><a class="uqZtlf x0HGk QRiHXd MymH0d maXJsd" target="_blank" aria-label="Attachment: Text: operators_cls.py" jsaction="LWntbc" href="https://drive.google.com/open?id=17IE1QXAl4H36TN92T92vNIchOi5xJYwE&amp;authuser=0" title="operators_cls.py" data-focus-id="hSRGPd-https://drive.google.com/open?id=17IE1QXAl4H36TN92T92vNIchOi5xJYwE&amp;authuser=0"><div class="bxp7vf mAeA1"><img jsname="q4uQmd" jsaction="error:dyBsCf" src="./Variable_cls_files/operators_cls.py.png" aria-hidden="true" data-mime-type="text/plain"><div class="S8qYve"><svg height="70px" width="105px" y="0px" x="0px" viewBox="0 0 105 70" enable-background="new 0 0 105 70"><g opacity=".5"><path d="m104.98 54.297c-0.017 0-0.017-54.297-0.017-54.297h-104.96v70h89.441s16.139-15.703 15.539-15.703z" fill="#E5E5E5"></path></g><polygon points="89.042 54.018 89.042 70 105 54.018" fill="#4986e7"></polygon><g opacity=".702"><polygon points="73.084 70 89.042 70 89.042 54.018" fill="#bbb"></polygon></g></svg></div></div><div class="J5AvUe"><div class="A6dC2c bKJwEd VBEdtc-Wvd9Cc zZN2Lb-Wvd9Cc">operators_cls.py</div><div class="cSyPgb cfaOwb"><div class="kRYv9b YVvGBb">Text</div></div></div></a><div class="PRmYNe QRiHXd" jsname="ncSfCe"></div></div></div><div data-dom-id="19UiY9E2w0G5PmazstNZEz4tLrmPpYDZo-2-3-2-Text-variables_cls.py-$2-false-false-false-false-$-https://drive.google.com/open?id=19UiY9E2w0G5PmazstNZEz4tLrmPpYDZo&amp;authuser=0" class="qNL8O ehXiW"><div class="po4Aib QRiHXd Aopndd " jsname="HzV7m" jsaction="JIbuQc:Rsbfue(Rsbfue)"><a class="uqZtlf x0HGk QRiHXd MymH0d maXJsd" target="_blank" aria-label="Attachment: Text: variables_cls.py" jsaction="LWntbc" href="https://drive.google.com/open?id=19UiY9E2w0G5PmazstNZEz4tLrmPpYDZo&amp;authuser=0" title="variables_cls.py" data-focus-id="hSRGPd-https://drive.google.com/open?id=19UiY9E2w0G5PmazstNZEz4tLrmPpYDZo&amp;authuser=0"><div class="bxp7vf mAeA1"><img jsname="q4uQmd" jsaction="error:dyBsCf" src="./Variable_cls_files/variables_cls.py.png" aria-hidden="true" data-mime-type="text/plain"><div class="S8qYve"><svg height="70px" width="105px" y="0px" x="0px" viewBox="0 0 105 70" enable-background="new 0 0 105 70"><g opacity=".5"><path d="m104.98 54.297c-0.017 0-0.017-54.297-0.017-54.297h-104.96v70h89.441s16.139-15.703 15.539-15.703z" fill="#E5E5E5"></path></g><polygon points="89.042 54.018 89.042 70 105 54.018" fill="#4986e7"></polygon><g opacity=".702"><polygon points="73.084 70 89.042 70 89.042 54.018" fill="#bbb"></polygon></g></svg></div></div><div class="J5AvUe"><div class="A6dC2c bKJwEd VBEdtc-Wvd9Cc zZN2Lb-Wvd9Cc">variables_cls.py</div><div class="cSyPgb cfaOwb"><div class="kRYv9b YVvGBb">Text</div></div></div></a><div class="PRmYNe QRiHXd" jsname="ncSfCe"></div></div></div></div><div class="eqqrO"><div jscontroller="XGZuGb" jsmodel="xvu37b;I8BbUd;uJydvc;BCjFBc;" data-type="2" data-visibility="2" data-exclude-header="false" data-enable-collapsing="false" data-collapse-to-only-header="false" class="PeGHgb" jsaction="rcuQ6b:rcuQ6b;Ts0WYd:rcuQ6b;wJx4ze:rcuQ6b;uwjiC:rcuQ6b"><div class="WuChGe QRiHXd aHTZpf" jsname="tJHJj" jsaction="JIbuQc:jkaCtf"><span class="asQXV">No class comments</span></div><div class="amzDAb"><p class="ysL59 asQXV">Class comments</p></div><div jsname="QmABz" class="Ono85c VvAAB"></div><div jsname="uqYDP" class="oh9CFb Gh0umc kpDQ8 CMmBPd"><div jscontroller="bUQrJd" class="QRiHXd" jsaction="JIbuQc:npVELd(IgWJu);laiNib:H2nWWd"><div jsshadow="" role="button" class="uArJ5e cd29Sd UQuaGc kCyAyd vAguXd oxacD" jscontroller="VXdfxd" jsaction="click:cOuCgd; mousedown:UX7yZ; mouseup:lbsD7e; mouseenter:tfO1Yc; mouseleave:JywGue;touchstart:p6p2H; touchmove:FwuNnf; touchend:yfqBxc(preventMouseEvents=true|preventDefault=true); touchcancel:JMtRjd;focus:AHmuwe; blur:O22p3e; contextmenu:mg9Pef" jsname="IgWJu" aria-disabled="false" tabindex="0" style="display: none;"><div class="Fvio9d MbhUzd" jsname="ksKsZd"></div><div class="e19J0b CeoRYc"></div><span jsslot="" class="l4V7wb Fxmcue cd29Sd"><span class="E6FpNe Ce1Y1c"><svg focusable="false" width="24" height="24" viewBox="0 0 24 24" class=" NMm5M hhikbc"><path d="M16 10H6.83L9 7.83l1.41-1.41L9 5l-6 6 6 6 1.41-1.41L9 14.17 6.83 12H16c1.65 0 3 1.35 3 3v4h2v-4c0-2.76-2.24-5-5-5z"></path></svg></span><span class="NPEfkd RveJvd snByac">Reply</span></span></div><img class="Y0e1Gd tkmmwb" aria-hidden="true" src="./Variable_cls_files/unnamed(2).jpg" style=""><div data-has-focusable-child="" class="oleV8d cjzpkc-Wvd9Cc QRiHXd iJ6Xwe"><div class="x7VMf" jsaction="YqO5N:HRfSZd; keydown:Hq2uPe"><div jscontroller="HRRZwe" jsaction="rcuQ6b:rcuQ6b;RRPEYd:PqP2y; focus:wMnKwd" jsmodel="t1oSSc" data-role="owner,coteacher,student" data-include-invited="false" jsname="fKPC3" data-course-id="117334927417"><div class="O98Lj" style=""><div class="bswVrf Lzdwhd-BrZSOd" aria-hidden="true">Add class comment…</div><div id=":1.t" class="LsqTRb Lzdwhd-AyKMt tgNIJf-Wvd9Cc Yiql6e iTy5c editable" tabindex="0" role="textbox" aria-required="true" aria-multiline="true" aria-label="Add class comment…" data-focusable-child="" g_editable="true" contenteditable="plaintext-only"></div></div></div></div><div class="BNHE9c QRiHXd" jsaction="JIbuQc:sFeBqf(M2UYVd)"><div jsshadow="" role="button" class="uArJ5e Y5FYJe cjq2Db OZ6W0d ipGJ5d RDPZE" jscontroller="VXdfxd" jsaction="click:cOuCgd; mousedown:UX7yZ; mouseup:lbsD7e; mouseenter:tfO1Yc; mouseleave:JywGue;touchstart:p6p2H; touchmove:FwuNnf; touchend:yfqBxc(preventMouseEvents=true|preventDefault=true); touchcancel:JMtRjd;focus:AHmuwe; blur:O22p3e; contextmenu:mg9Pef" jsname="M2UYVd" aria-label="Post" aria-disabled="true" tabindex="-1" data-tooltip="Post" data-focusable-child="" data-tooltip-vertical-offset="-12" data-tooltip-horizontal-offset="0"><div class="PDXc1b MbhUzd" jsname="ksKsZd"></div><span jsslot="" class="XuQwKc"><span class="GmuOkf"><svg focusable="false" width="24" height="24" viewBox="0 0 24 24" class=" NMm5M hhikbc"><path d="M2 3v18l20-9L2 3zm2 11l9-2-9-2V6.09L17.13 12 4 17.91V14z"></path></svg></span></span></div></div></div></div></div></div></div><div jscontroller="BbOAsf" jsmodel="PTCFbe;" jsaction="qFdNBb:Pb2hxc;Cvbxce:ysXIce;pN3Oaf:n3lXYe;wuANJc:hDYvKe,T0iadd;ywGDo:hDYvKe" data-include-stream-item-materials="true" data-with-stream-item-materials=""></div><div jscontroller="nV1LF" jsaction="Cvbxce:ysXIce;qFdNBb:Pb2hxc;uwjiC:xtpvtf"></div><div jscontroller="ZlX84d" jsaction="rcuQ6b:OuAj6c;uwjiC:OuAj6c" id="ow46" __is_owner="true"></div><div jscontroller="cs6ocd" jsaction="rcuQ6b:npT2md;FttMgb:Qp7hp;qFdNBb:Pb2hxc;Cvbxce:N6n54b;zkkUY:p5Uonb" data-wait-for="QlRoyd" style="display: none;"></div></div></div></div></div><div jscontroller="SMAcwd" jsaction="rcuQ6b:rcuQ6b;" style="" role="contentinfo" class="tdS5P PECJsb" guidedhelpid="helpMenuGH" id="ow21" __is_owner="true" aria-hidden="true"><div role="button" class="U26fgb JRtysb WzwrXb I12f0b K2mXPb" jscontroller="iSvg6e" jsaction="click:cOuCgd; mousedown:UX7yZ; mouseup:lbsD7e; mouseenter:tfO1Yc; mouseleave:JywGue; focus:AHmuwe; blur:O22p3e; contextmenu:mg9Pef;touchstart:p6p2H; touchmove:FwuNnf; touchend:yfqBxc(preventMouseEvents=true|preventDefault=true); touchcancel:JMtRjd;;keydown:I481le;" jsshadow="" jsname="LgbsSe" aria-label="Help and Feedback" aria-disabled="false" tabindex="0" aria-haspopup="true" aria-expanded="false" data-menu-corner="bottom-start" data-anchor-corner="top-start"><div class="NWlf3e MbhUzd" jsname="ksKsZd"></div><span jsslot="" class="MhXXcc oJeWuf"><span class="Lw7GHd snByac"><svg width="24" height="24" viewBox="0 0 24 24" focusable="false" class=" NMm5M hhikbc"><path d="M11 18h2v-2h-2v2zm1-16C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm0-14c-2.21 0-4 1.79-4 4h2c0-1.1.9-2 2-2s2 .9 2 2c0 2-3 1.75-3 5h2c0-2.25 3-2.5 3-5 0-2.21-1.79-4-4-4z"></path></svg></span></span></div></div><script nonce="" aria-hidden="true">if (window.parent !== window) document.querySelector('.dxu4Dd').style.display = 'none'; window['HqyC7b'] = window.performance && performance.timing.navigationStart + performance.now();</script><div jslazy="" jscontroller="jKzfKc" jsaction="RaLK8d:ti6hGc" aria-hidden="true"></div><div ng-non-bindable="" aria-hidden="true"></div><script nonce="" aria-hidden="true">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
var Qd,Rd,Sd,Wd,Xd,Yd,Zd,$d,ae,be,ge;_.Pd=function(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var d=c.slice();d.push.apply(d,arguments);return a.apply(this,d)}};Qd=null;Rd=/^[\w+/_-]+[=]{0,2}$/;Sd=function(a){return(a=a.querySelector&&a.querySelector("script[nonce]"))&&(a=a.nonce||a.getAttribute("nonce"))&&Rd.test(a)?a:""};_.Td=function(a){var b=_.ya(a);return"array"==b||"object"==b&&"number"==typeof a.length};
_.Ud=function(a){var b=a.length;if(0<b){for(var c=Array(b),d=0;d<b;d++)c[d]=a[d];return c}return[]};_.Vd=function(a,b){return 0==a.lastIndexOf(b,0)};Wd=/&/g;Xd=/</g;Yd=/>/g;Zd=/"/g;$d=/'/g;ae=/\x00/g;be=/[\x00&<>"']/;
_.ce=function(a,b){if(b)a=a.replace(Wd,"&amp;").replace(Xd,"&lt;").replace(Yd,"&gt;").replace(Zd,"&quot;").replace($d,"&#39;").replace(ae,"&#0;");else{if(!be.test(a))return a;-1!=a.indexOf("&")&&(a=a.replace(Wd,"&amp;"));-1!=a.indexOf("<")&&(a=a.replace(Xd,"&lt;"));-1!=a.indexOf(">")&&(a=a.replace(Yd,"&gt;"));-1!=a.indexOf('"')&&(a=a.replace(Zd,"&quot;"));-1!=a.indexOf("'")&&(a=a.replace($d,"&#39;"));-1!=a.indexOf("\x00")&&(a=a.replace(ae,"&#0;"))}return a};
_.de=function(a){var b;(b=a.ownerDocument&&a.ownerDocument.defaultView)&&b!=_.p?b=Sd(b.document):(null===Qd&&(Qd=Sd(_.p.document)),b=Qd);b&&a.setAttribute("nonce",b)};_.ee=function(a,b){a.src=_.$a(b);_.de(a)};_.fe=function(a){return a=_.ce(a,void 0)};ge=!_.x||_.fc(9);_.he=!_.Ob&&!_.x||_.x&&_.fc(9)||_.Ob&&_.dc("1.9.1");_.ie=_.x&&!_.dc("9");_.je=_.x||_.Lb||_.Pb;
_.ke=function(a,b){this.width=a;this.height=b};_.h=_.ke.prototype;_.h.aspectRatio=function(){return this.width/this.height};_.h.zc=function(){return!(this.width*this.height)};_.h.ceil=function(){this.width=Math.ceil(this.width);this.height=Math.ceil(this.height);return this};_.h.floor=function(){this.width=Math.floor(this.width);this.height=Math.floor(this.height);return this};_.h.round=function(){this.width=Math.round(this.width);this.height=Math.round(this.height);return this};
var ne;_.le=function(a,b){return(b||document).getElementsByTagName(String(a))};_.N=function(a,b){var c=b||document;if(c.getElementsByClassName)a=c.getElementsByClassName(a)[0];else{c=document;var d=b||c;a=d.querySelectorAll&&d.querySelector&&a?d.querySelector(a?"."+a:""):_.me(c,"*",a,b)[0]||null}return a||null};
_.me=function(a,b,c,d){a=d||a;b=b&&"*"!=b?String(b).toUpperCase():"";if(a.querySelectorAll&&a.querySelector&&(b||c))return a.querySelectorAll(b+(c?"."+c:""));if(c&&a.getElementsByClassName){a=a.getElementsByClassName(c);if(b){d={};for(var e=0,f=0,g;g=a[f];f++)b==g.nodeName&&(d[e++]=g);d.length=e;return d}return a}a=a.getElementsByTagName(b||"*");if(c){d={};for(f=e=0;g=a[f];f++)b=g.className,"function"==typeof b.split&&_.Na(b.split(/\s+/),c)&&(d[e++]=g);d.length=e;return d}return a};
_.oe=function(a,b){_.Oa(b,function(c,d){c&&"object"==typeof c&&c.Qb&&(c=c.Gb());"style"==d?a.style.cssText=c:"class"==d?a.className=c:"for"==d?a.htmlFor=c:ne.hasOwnProperty(d)?a.setAttribute(ne[d],c):_.Vd(d,"aria-")||_.Vd(d,"data-")?a.setAttribute(d,c):a[d]=c})};ne={cellpadding:"cellPadding",cellspacing:"cellSpacing",colspan:"colSpan",frameborder:"frameBorder",height:"height",maxlength:"maxLength",nonce:"nonce",role:"role",rowspan:"rowSpan",type:"type",usemap:"useMap",valign:"vAlign",width:"width"};
_.re=function(a,b){var c=String(b[0]),d=b[1];if(!ge&&d&&(d.name||d.type)){c=["<",c];d.name&&c.push(' name="',_.fe(d.name),'"');if(d.type){c.push(' type="',_.fe(d.type),'"');var e={};_.Qa(e,d);delete e.type;d=e}c.push(">");c=c.join("")}c=_.pe(a,c);d&&("string"===typeof d?c.className=d:Array.isArray(d)?c.className=d.join(" "):_.oe(c,d));2<b.length&&_.qe(a,c,b,2);return c};
_.qe=function(a,b,c,d){function e(k){k&&b.appendChild("string"===typeof k?a.createTextNode(k):k)}for(;d<c.length;d++){var f=c[d];if(!_.Td(f)||_.Aa(f)&&0<f.nodeType)e(f);else{a:{if(f&&"number"==typeof f.length){if(_.Aa(f)){var g="function"==typeof f.item||"string"==typeof f.item;break a}if(_.za(f)){g="function"==typeof f.item;break a}}g=!1}(0,_.Ja)(g?_.Ud(f):f,e)}}};_.se=function(a){return _.pe(document,a)};
_.pe=function(a,b){b=String(b);"application/xhtml+xml"===a.contentType&&(b=b.toLowerCase());return a.createElement(b)};_.te=function(a){for(var b;b=a.firstChild;)a.removeChild(b)};_.ue=function(a){return a&&a.parentNode?a.parentNode.removeChild(a):null};_.ve=function(a){return _.Aa(a)&&1==a.nodeType};_.we=function(a){return 9==a.nodeType?a:a.ownerDocument||a.document};_.xe=function(a,b,c){for(var d=0;a&&(null==c||d<=c);){if(b(a))return a;a=a.parentNode;d++}return null};

}catch(e){_._DumpException(e)}
try{
_.qj=function(a){_.z(this,a,0,-1,null,null)};_.v(_.qj,_.y);_.rj=function(a,b,c){a.rel=c;a.href=-1!=c.toLowerCase().indexOf("stylesheet")?_.ab(b):b instanceof _.Za?_.ab(b):b instanceof _.hb?_.ib(b):_.ib(_.lb(b))};
_.sj=function(a){return _.bb(_.A(a,4)||"")};

}catch(e){_._DumpException(e)}
try{
var tj=function(a,b,c){_.wd.log(46,{att:a,max:b,url:c})},vj=function(a,b,c){_.wd.log(47,{att:a,max:b,url:c});a<b?uj(a+1,b):_.M.log(Error("Q`"+a+"`"+b),{url:c})},uj=function(a,b){if(wj){var c=_.se("SCRIPT");c.async=!0;c.type="text/javascript";c.charset="UTF-8";_.ee(c,wj);c.onload=_.Pd(tj,a,b,c.src);c.onerror=_.Pd(vj,a,b,c.src);_.wd.log(45,{att:a,max:b,url:c.src});_.le("HEAD")[0].appendChild(c)}},xj=function(a){_.z(this,a,0,-1,null,null)};_.v(xj,_.y);
var yj=_.G(_.sd,xj,17)||new xj,zj,wj=(zj=_.G(yj,_.qj,1))?_.sj(zj):null,Aj,Bj=(Aj=_.G(yj,_.qj,2))?_.sj(Aj):null,Cj=function(){uj(1,2);if(Bj){var a=_.se("LINK");a.setAttribute("type","text/css");_.rj(a,Bj,"stylesheet");_.le("HEAD")[0].appendChild(a)}};
(function(){var a=_.td();if(_.B(a,18))Cj();else{var b=_.A(a,19)||0;window.addEventListener("load",function(){window.setTimeout(Cj,b)})}})();

}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><div class="gb_ue" aria-hidden="true"><div class="gb_we"><div>Google Account</div><div class="gb_ub">Sanath Kumar</div><div>sanath1975@gmail.com</div></div></div><div class="gb_1d" aria-hidden="true">Google apps</div><script id="base-js" src="./Variable_cls_files/m=base" nonce="" gapi_processed="true" aria-hidden="true"></script><div id="lcsclient" style="display: none;" aria-hidden="true"><iframe name="xpcpeerCfOk" id="xpcpeerCfOk" src="./Variable_cls_files/client.html" style="height: 100%; width: 100%;"></iframe></div><div class="vhK44c dgqqXe" jsaction="rcuQ6b:rcuQ6b; click:okAHKe(GGAcbc),YdzvGf(ibnC6b); keydown:I481le;ZldWJd:FNFY6c;lHU8dd:rcuQ6b" jscontroller="tOHjkb" jsowner="ow19" aria-hidden="true"><div class="AxPfNe" jsname="GGAcbc"></div><div class="ETRkCe" jsname="haAclf"><div class="OX4Vcb" role="menu"><a class="Xi8cpb cd29Sd" jsname="ibnC6b" tabindex="-1" data-focus-id="/u/0/h" href="https://classroom.google.com/u/0/h" aria-label="Classes " role="menuitem"><div class="LlcfK"><div class="p1KYTc"></div></div><div class="JDxyrc xSP5ic"><svg width="24" height="24" viewBox="0 0 24 24" focusable="false" class=" NMm5M"><path d="M12 3L4 9v12h16V9l-8-6zm6 16h-3v-6H9v6H6v-9l6-4.5 6 4.5v9z"></path></svg></div><div class="kXvNXe"><div class="nhassd asQXV YVvGBb">Classes</div></div></a><a class="Xi8cpb cd29Sd" jsname="ibnC6b" tabindex="-1" data-focus-id="/u/0/calendar/this-week/course/all" href="https://classroom.google.com/u/0/calendar/this-week/course/all" aria-label="Calendar " role="menuitem"><div class="LlcfK"><div class="p1KYTc"></div></div><div class="JDxyrc xSP5ic"><svg width="24" height="24" viewBox="0 0 24 24" focusable="false" class=" NMm5M"><path d="M19 4h-1V2h-2v2H8V2H6v2H5c-1.11 0-1.99.9-1.99 2L3 20a2 2 0 0 0 2 2h14c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 16H5V9h14v11z"></path></svg></div><div class="kXvNXe"><div class="nhassd asQXV YVvGBb">Calendar</div></div></a><div class="kCtYwe" role="separator"></div><div role="section" aria-label="Enrolled"><div class="pkktJb iLjzDc YVvGBb">Enrolled</div><a class="Xi8cpb cd29Sd" jsname="ibnC6b" tabindex="-1" data-focus-id="/u/0/a/not-turned-in/all" href="https://classroom.google.com/u/0/a/not-turned-in/all" aria-label="To-do " role="menuitem"><div class="LlcfK"><div class="p1KYTc"></div></div><div class="JDxyrc xSP5ic"><svg enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24" width="24" focusable="false" class=" NMm5M"><g><rect fill="none" height="24" width="24"></rect></g><g><g><path d="M20,3H4C2.9,3,2,3.9,2,5v14c0,1.1,0.9,2,2,2h16c1.1,0,2-0.9,2-2V5 C22,3.9,21.1,3,20,3z M20,19H4V5h16V19z" fill-rule="evenodd"></path><polygon fill-rule="evenodd" points="19.41,10.42 17.99,9 14.82,12.17 13.41,10.75 12,12.16 14.82,15"></polygon><rect fill-rule="evenodd" height="2" width="5" x="5" y="7"></rect><rect fill-rule="evenodd" height="2" width="5" x="5" y="11"></rect><rect fill-rule="evenodd" height="2" width="5" x="5" y="15"></rect></g></g></svg></div><div class="kXvNXe"><div class="nhassd asQXV YVvGBb">To-do</div></div></a><a class="Xi8cpb TMOcX vG1fDb qs41qe" jsname="ibnC6b" tabindex="-1" data-focus-id="/u/0/c/MTE3MzM0OTI3NDE3" href="https://classroom.google.com/u/0/c/MTE3MzM0OTI3NDE3" aria-label="Sanjeev-Python-8:Am Weekdays" role="menuitem" data-id="117334927417"><div class="LlcfK bFjUmb-Ysl7Fe"><div class="p1KYTc"></div></div><div class="yXVLvd"><span class="DShyMc-MTE3MzM0OTI3NDE3 CNpREd"><div class="vUBwW TGnLfc A6dC2c UISY8d-Tvm9db bFjUmb-Tvm9db" aria-hidden="true">S</div></span></div><div class="kXvNXe"><div class="nhassd asQXV YVvGBb">Sanjeev-Python-8:Am</div><div class="TajIHf dDKhVc YVvGBb">Weekdays</div></div></a></div><div class="kCtYwe" role="separator"></div><a class="Xi8cpb cd29Sd" jsname="ibnC6b" tabindex="-1" data-focus-id="/u/0/h/archived" href="https://classroom.google.com/u/0/h/archived" aria-label="Archived classes " role="menuitem"><div class="LlcfK"><div class="p1KYTc"></div></div><div class="JDxyrc xSP5ic"><svg width="24" height="24" viewBox="0 0 24 24" focusable="false" class=" NMm5M"><path d="M20.54 5.23l-1.39-1.68C18.88 3.21 18.47 3 18 3H6c-.47 0-.88.21-1.16.55L3.46 5.23C3.17 5.57 3 6.02 3 6.5V19c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V6.5c0-.48-.17-.93-.46-1.27zM6.24 5h11.52l.83 1H5.42l.82-1zM5 19V8h14v11H5zm11-5.5l-4 4-4-4 1.41-1.41L11 13.67V10h2v3.67l1.59-1.59L16 13.5z"></path></svg></div><div class="kXvNXe"><div class="nhassd asQXV YVvGBb">Archived classes</div></div></a><a class="Xi8cpb cd29Sd" jsname="ibnC6b" tabindex="-1" data-focus-id="/u/0/s" href="https://classroom.google.com/u/0/s" aria-label="Settings " role="menuitem"><div class="LlcfK"><div class="p1KYTc"></div></div><div class="JDxyrc xSP5ic"><svg width="24" height="24" viewBox="0 0 24 24" focusable="false" class=" NMm5M"><path d="M13.85 22.25h-3.7c-.74 0-1.36-.54-1.45-1.27l-.27-1.89c-.27-.14-.53-.29-.79-.46l-1.8.72c-.7.26-1.47-.03-1.81-.65L2.2 15.53c-.35-.66-.2-1.44.36-1.88l1.53-1.19c-.01-.15-.02-.3-.02-.46 0-.15.01-.31.02-.46l-1.52-1.19c-.59-.45-.74-1.26-.37-1.88l1.85-3.19c.34-.62 1.11-.9 1.79-.63l1.81.73c.26-.17.52-.32.78-.46l.27-1.91c.09-.7.71-1.25 1.44-1.25h3.7c.74 0 1.36.54 1.45 1.27l.27 1.89c.27.14.53.29.79.46l1.8-.72c.71-.26 1.48.03 1.82.65l1.84 3.18c.36.66.2 1.44-.36 1.88l-1.52 1.19c.01.15.02.3.02.46s-.01.31-.02.46l1.52 1.19c.56.45.72 1.23.37 1.86l-1.86 3.22c-.34.62-1.11.9-1.8.63l-1.8-.72c-.26.17-.52.32-.78.46l-.27 1.91c-.1.68-.72 1.22-1.46 1.22zm-3.23-2h2.76l.37-2.55.53-.22c.44-.18.88-.44 1.34-.78l.45-.34 2.38.96 1.38-2.4-2.03-1.58.07-.56c.03-.26.06-.51.06-.78s-.03-.53-.06-.78l-.07-.56 2.03-1.58-1.39-2.4-2.39.96-.45-.35c-.42-.32-.87-.58-1.33-.77l-.52-.22-.37-2.55h-2.76l-.37 2.55-.53.21c-.44.19-.88.44-1.34.79l-.45.33-2.38-.95-1.39 2.39 2.03 1.58-.07.56a7 7 0 0 0-.06.79c0 .26.02.53.06.78l.07.56-2.03 1.58 1.38 2.4 2.39-.96.45.35c.43.33.86.58 1.33.77l.53.22.38 2.55z"></path><circle cx="12" cy="12" r="3.5"></circle></svg></div><div class="kXvNXe"><div class="nhassd asQXV YVvGBb">Settings</div></div></a></div></div></div><iframe name="oauth2relay427920288" id="oauth2relay427920288" src="./Variable_cls_files/postmessageRelay.html" tabindex="-1" style="width: 1px; height: 1px; position: absolute; top: -100px;" aria-hidden="true"></iframe><div aria-live="polite" aria-atomic="true" style="position: absolute; top: -1000px; height: 1px; overflow: hidden;" aria-hidden="true"></div><div class="ndfHFb-c4YZDc ndfHFb-c4YZDc-AHmuwe-Hr88gd-OWB6Me ndfHFb-c4YZDc-vyDMJf-aZ2wEe ndfHFb-c4YZDc-i5oIFb ndfHFb-c4YZDc-TSZdd" aria-label="Showing viewer." role="dialog" tabindex="0"><div class="ndfHFb-c4YZDc-bnBfGc ndfHFb-c4YZDc-zTETae" tabindex="0" aria-label="Displaying variables_cls.py."></div><div class="ndfHFb-c4YZDc-K9a4Re" style="bottom: 0px;"><div class="ndfHFb-c4YZDc-E7ORLb-LgbsSe ndfHFb-c4YZDc-LgbsSe" role="button" aria-disabled="false" data-tooltip-unhoverable="true" data-tooltip-delay="500" data-tooltip-class="ndfHFb-c4YZDc-tk3N6e-suEOdc" data-tooltip-align="r,c" data-tooltip-offset="-6" style="user-select: none; left: 12px; opacity: 1;" tabindex="0" aria-label="Previous" data-tooltip="Previous"><div class="ndfHFb-c4YZDc-DH6Rkf-AHe6Kc"><div class="ndfHFb-c4YZDc-Bz112c ndfHFb-c4YZDc-DH6Rkf-Bz112c"></div></div></div><div class="ndfHFb-c4YZDc-tJiF1e-LgbsSe ndfHFb-c4YZDc-LgbsSe ndfHFb-c4YZDc-LgbsSe-OWB6Me" role="button" aria-disabled="true" data-tooltip-unhoverable="true" data-tooltip-delay="500" data-tooltip-class="ndfHFb-c4YZDc-tk3N6e-suEOdc" data-tooltip-align="l,c" data-tooltip-offset="-6" style="user-select: none; right: 12px; opacity: 1;"><div class="ndfHFb-c4YZDc-DH6Rkf-AHe6Kc"><div class="ndfHFb-c4YZDc-Bz112c ndfHFb-c4YZDc-DH6Rkf-Bz112c"></div></div></div><div class="ndfHFb-c4YZDc-q77wGc" style="opacity: 1;"><div class="ndfHFb-c4YZDc-DARUcf-NnAfwf-i5oIFb" style="display: none;"></div><div class="ndfHFb-c4YZDc-nJjxad-nK2kYb-i5oIFb" style=""><div class="ndfHFb-c4YZDc-to915-LgbsSe ndfHFb-c4YZDc-nJjxad-m9bMae-LgbsSe VIpgJd-TzA9Ye-eEGnhe ndfHFb-c4YZDc-LgbsSe" role="button" tabindex="0" data-tooltip-unhoverable="true" data-tooltip-delay="500" data-tooltip-class="ndfHFb-c4YZDc-tk3N6e-suEOdc" data-tooltip-align="b,c" data-tooltip-offset="-6" aria-label="Zoom out" data-tooltip="Zoom out" style="user-select: none;"><div class="ndfHFb-c4YZDc-Bz112c"></div></div><div class="ndfHFb-c4YZDc-LgbsSe ndfHFb-c4YZDc-to915-LgbsSe ndfHFb-c4YZDc-nJjxad-hj4D6d-LgbsSe VIpgJd-TzA9Ye-eEGnhe ndfHFb-c4YZDc-LgbsSe-OWB6Me ndfHFb-c4YZDc-nJjxad-S9gUrf" role="button" data-tooltip-unhoverable="true" data-tooltip-delay="500" data-tooltip-class="ndfHFb-c4YZDc-tk3N6e-suEOdc" data-tooltip-align="b,c" data-tooltip-offset="-6" style="user-select: none;" aria-disabled="true" aria-label="Reset zoom" data-tooltip="Reset zoom"><div class="ndfHFb-c4YZDc-Bz112c"></div></div><div class="ndfHFb-c4YZDc-LgbsSe ndfHFb-c4YZDc-to915-LgbsSe ndfHFb-c4YZDc-nJjxad-bEDTcc-LgbsSe VIpgJd-TzA9Ye-eEGnhe" role="button" tabindex="0" data-tooltip-unhoverable="true" data-tooltip-delay="500" data-tooltip-class="ndfHFb-c4YZDc-tk3N6e-suEOdc" data-tooltip-align="b,c" data-tooltip-offset="-6" aria-label="Zoom in" data-tooltip="Zoom in" style="user-select: none;"><div class="ndfHFb-c4YZDc-Bz112c"></div></div></div><div class="ndfHFb-c4YZDc-LzGo7c" style="display: none;"></div></div><div class="ndfHFb-c4YZDc-K9a4Re-nKQ6qf ndfHFb-c4YZDc-TvD9Pc-qnnXGd" role="main" style="display: none;"><div class="ndfHFb-c4YZDc-EglORb-ge6pde ndfHFb-c4YZDc-K9a4Re-ge6pde-Ne3sFf" role="status" tabindex="-1" aria-label="Loading" style="display: none;"><div class="ndfHFb-c4YZDc-EglORb-ge6pde-RJLb9c ndfHFb-c4YZDc-AHmuwe-wcotoc-zTETae"><div class="ndfHFb-aZ2wEe" dir="ltr"><div class="ndfHFb-vyDMJf-aZ2wEe auswjd"><div class="aZ2wEe-pbTTYe aZ2wEe-v3pZbf"><div class="aZ2wEe-LkdAo-e9ayKc aZ2wEe-LK5yu"><div class="aZ2wEe-LkdAo aZ2wEe-hj4D6d"></div></div><div class="aZ2wEe-pehrl-TpMipd"><div class="aZ2wEe-LkdAo aZ2wEe-hj4D6d"></div></div><div class="aZ2wEe-LkdAo-e9ayKc aZ2wEe-qwU8Me"><div class="aZ2wEe-LkdAo aZ2wEe-hj4D6d"></div></div></div><div class="aZ2wEe-pbTTYe aZ2wEe-oq6NAc"><div class="aZ2wEe-LkdAo-e9ayKc aZ2wEe-LK5yu"><div class="aZ2wEe-LkdAo aZ2wEe-hj4D6d"></div></div><div class="aZ2wEe-pehrl-TpMipd"><div class="aZ2wEe-LkdAo aZ2wEe-hj4D6d"></div></div><div class="aZ2wEe-LkdAo-e9ayKc aZ2wEe-qwU8Me"><div class="aZ2wEe-LkdAo aZ2wEe-hj4D6d"></div></div></div><div class="aZ2wEe-pbTTYe aZ2wEe-gS7Ybc"><div class="aZ2wEe-LkdAo-e9ayKc aZ2wEe-LK5yu"><div class="aZ2wEe-LkdAo aZ2wEe-hj4D6d"></div></div><div class="aZ2wEe-pehrl-TpMipd"><div class="aZ2wEe-LkdAo aZ2wEe-hj4D6d"></div></div><div class="aZ2wEe-LkdAo-e9ayKc aZ2wEe-qwU8Me"><div class="aZ2wEe-LkdAo aZ2wEe-hj4D6d"></div></div></div><div class="aZ2wEe-pbTTYe aZ2wEe-nllRtd"><div class="aZ2wEe-LkdAo-e9ayKc aZ2wEe-LK5yu"><div class="aZ2wEe-LkdAo aZ2wEe-hj4D6d"></div></div><div class="aZ2wEe-pehrl-TpMipd"><div class="aZ2wEe-LkdAo aZ2wEe-hj4D6d"></div></div><div class="aZ2wEe-LkdAo-e9ayKc aZ2wEe-qwU8Me"><div class="aZ2wEe-LkdAo aZ2wEe-hj4D6d"></div></div></div></div></div></div><span class="ndfHFb-c4YZDc-EglORb-ge6pde-fmcmS ndfHFb-c4YZDc-AHmuwe-wcotoc-zTETae" aria-hidden="true">Loading…</span></div><div style="display:none">{"id": "17IE1QXAl4H36TN92T92vNIchOi5xJYwE", "title": "operators_cls.py", "mimeType": "text\/plain"}</div><div class="ndfHFb-c4YZDc-oKVyEf "><div class="ndfHFb-c4YZDc-fmcmS-haAclf"><div class="ndfHFb-c4YZDc-fmcmS-s2gQvd ndfHFb-c4YZDc-s2gQvd"><div class="ndfHFb-c4YZDc-wvGCSb-gkA7Yd"></div><div class="ndfHFb-c4YZDc-fmcmS"><div class="ndfHFb-c4YZDc-fmcmS-vJ7A6b ndfHFb-c4YZDc-TvD9Pc-qnnXGd"><div class="ndfHFb-c4YZDc-fmcmS-b0t70b"><div class="ndfHFb-c4YZDc-fmcmS-bN97Pc" role="document" aria-label="Displaying operators_cls.py" tabindex="0" dir="ltr" style="text-align: left;"><pre class="ndfHFb-c4YZDc-fmcmS-DARUcf"># Operators -- Its a symbol which perform an operation between 2 or more operands....

# 3+5+6

# List of Operators:-
    # 1) Arithemtic Operators(+,-,*,/,//,%,**)
    # 2) Relational Operators(==,!=,&gt;,&lt;,&gt;=,&lt;=)
    # 3) Logical Operators(and,or,not)
    # 4) Assignment Operators(=,+=,-=,*=,/=)
    # 5) Bitwise Operators(Bitwise And(&amp;),Bitwise OR(|),Bitwise XOR(^),Left Shift(&lt;&lt;),Right Shift(&gt;&gt;),Bitwise NOT(~))
    # 6) Membership Operators(in,not in)
    # 7) Identity Operators(is,is not)


# 1) Arithmetic Operators

# print(34+67)
# print(45-35)
# print(12*12)


# print(17/3)

# print(17//3)

# print(16/3) = 5.6667

# print(16//3) = 5

# print(17%3)  =2


# 3) 17 (5
#    15
# ---------
#     2

# 158%3 - 2
# 3) 158 (52
#    15
# --------
#     08
#      6
# ---------
#      2

# 3*5
# 3**5 == 3*3*3*3*3 -- 343


# 2)Relational Operators -- Output for relational operators will be True or False only..

a=45
b=78

# print(a==b) # False
# print(a != b) # False

# print(a&gt;b) # False
# print(a&lt;b) # True
# print(a&gt;=b) # False
# print(a&lt;=b) # True

# 3) Logical Operators(and,or,not):-


# A            B          A and B          A or B        not(A)        not(A and B)
# ------------------------------------------------------------------------------------
# T            F             F               T             F              T 
# F            T             F               T             T              T 
# T            T             T               T             F              F 
# F            F             F               F             T              T 




a=45
b=67


# print(a&gt;50 and b&lt;100)
# #      F   and  T    - F


# print(a&gt;50 or b&lt;100)

# #     F    or  T    -  T 


# print(not(a&gt;50 and b&lt;100))



# username = "gsanjeev"
# password = "123456"


# print('gsaneev'==username and '123456'==password)

# print('gsaneev'==username or '123456'==password)


# 4) Assignment Operators(=,+=,-=,*=)

# a=45
# # a=a+15
# print(a)
# print(id(a))
# a+=15 # a=a+15
# print(a)
# print(id(a))
# a-=15
# print(a)
# print(id(a))
# a*=5

# print(a)

# a/=5

# print(a)

# 45

# Python datatypes:-
    # 1) Numbers --- Numeric values or decimal values...(int,floating)
        # a=45, b=6.7
    # 2) Strings --- Sequennce of charcaters which are declared inside " "....
        # a = "hyderabad123"
    # 3) Lists ---  Sequence of multiple values which are declared inside [ ] seperated with comma(,)..
        # a = [4,"python",5.6,"hyderabad"]
    # 4) Tuples --- Sequence of multiple values which are declared inside ( ) seperated with comma(,)..
        # a = (4,"python",5.6,"hyderabad")
    # 5) Dictionaries  -- Sequence of key:value pairs which are declared inside { } seperated with comma(,)..
        # a = {'email' : 'gsanjeev@gmail.com','password':'123456'}  
    # 6) Sets -- Frozensets.. -- Sequence of multiple values which are declared inside { } seperated with comma(,)..
        # a = {4,5.6,'python','django',4}


# a = {4,5.6,'python','django',4}

# a = (4,5.6,'python','django',4)
# # print(a)

# # Lists,Dictionaries,Sets --- Mutuable
# # Tuples,Strings,Numbers --- Immutuable

# a= [4,5.6,'python','django',4]

</pre></div></div></div></div></div></div><div class="ndfHFb-c4YZDc-n5VRYe-ma6Yeb" style="display: none;"></div><div class="ndfHFb-c4YZDc-n5VRYe-cGMI2b" style="display: none;"></div></div></div><div class="ndfHFb-c4YZDc-K9a4Re-nKQ6qf ndfHFb-c4YZDc-TvD9Pc-qnnXGd" role="main" style=""><div class="ndfHFb-c4YZDc-EglORb-ge6pde ndfHFb-c4YZDc-K9a4Re-ge6pde-Ne3sFf" role="status" tabindex="-1" aria-label="Loading" style="display: none;"><div class="ndfHFb-c4YZDc-EglORb-ge6pde-RJLb9c ndfHFb-c4YZDc-AHmuwe-wcotoc-zTETae"><div class="ndfHFb-aZ2wEe" dir="ltr"><div class="ndfHFb-vyDMJf-aZ2wEe auswjd"><div class="aZ2wEe-pbTTYe aZ2wEe-v3pZbf"><div class="aZ2wEe-LkdAo-e9ayKc aZ2wEe-LK5yu"><div class="aZ2wEe-LkdAo aZ2wEe-hj4D6d"></div></div><div class="aZ2wEe-pehrl-TpMipd"><div class="aZ2wEe-LkdAo aZ2wEe-hj4D6d"></div></div><div class="aZ2wEe-LkdAo-e9ayKc aZ2wEe-qwU8Me"><div class="aZ2wEe-LkdAo aZ2wEe-hj4D6d"></div></div></div><div class="aZ2wEe-pbTTYe aZ2wEe-oq6NAc"><div class="aZ2wEe-LkdAo-e9ayKc aZ2wEe-LK5yu"><div class="aZ2wEe-LkdAo aZ2wEe-hj4D6d"></div></div><div class="aZ2wEe-pehrl-TpMipd"><div class="aZ2wEe-LkdAo aZ2wEe-hj4D6d"></div></div><div class="aZ2wEe-LkdAo-e9ayKc aZ2wEe-qwU8Me"><div class="aZ2wEe-LkdAo aZ2wEe-hj4D6d"></div></div></div><div class="aZ2wEe-pbTTYe aZ2wEe-gS7Ybc"><div class="aZ2wEe-LkdAo-e9ayKc aZ2wEe-LK5yu"><div class="aZ2wEe-LkdAo aZ2wEe-hj4D6d"></div></div><div class="aZ2wEe-pehrl-TpMipd"><div class="aZ2wEe-LkdAo aZ2wEe-hj4D6d"></div></div><div class="aZ2wEe-LkdAo-e9ayKc aZ2wEe-qwU8Me"><div class="aZ2wEe-LkdAo aZ2wEe-hj4D6d"></div></div></div><div class="aZ2wEe-pbTTYe aZ2wEe-nllRtd"><div class="aZ2wEe-LkdAo-e9ayKc aZ2wEe-LK5yu"><div class="aZ2wEe-LkdAo aZ2wEe-hj4D6d"></div></div><div class="aZ2wEe-pehrl-TpMipd"><div class="aZ2wEe-LkdAo aZ2wEe-hj4D6d"></div></div><div class="aZ2wEe-LkdAo-e9ayKc aZ2wEe-qwU8Me"><div class="aZ2wEe-LkdAo aZ2wEe-hj4D6d"></div></div></div></div></div></div><span class="ndfHFb-c4YZDc-EglORb-ge6pde-fmcmS ndfHFb-c4YZDc-AHmuwe-wcotoc-zTETae" aria-hidden="true">Loading…</span></div><div style="display:none" id="drive-active-item-info">{"id": "19UiY9E2w0G5PmazstNZEz4tLrmPpYDZo", "title": "variables_cls.py", "mimeType": "text\/plain"}</div><div class="ndfHFb-c4YZDc-oKVyEf"><div class="ndfHFb-c4YZDc-fmcmS-haAclf"><div class="ndfHFb-c4YZDc-fmcmS-s2gQvd ndfHFb-c4YZDc-s2gQvd"><div class="ndfHFb-c4YZDc-wvGCSb-gkA7Yd"></div><div class="ndfHFb-c4YZDc-fmcmS"><div class="ndfHFb-c4YZDc-fmcmS-vJ7A6b ndfHFb-c4YZDc-TvD9Pc-qnnXGd" style="height: 1572px;"><div class="ndfHFb-c4YZDc-fmcmS-b0t70b ndfHFb-c4YZDc-neVct-RCfa3e" style="left: 163.2px; top: 56px; padding-bottom: 56px;"><div class="ndfHFb-c4YZDc-fmcmS-bN97Pc" role="document" aria-label="Displaying variables_cls.py" tabindex="0" dir="ltr" style="text-align: left; width: 1170px; height: auto;"><pre class="ndfHFb-c4YZDc-fmcmS-DARUcf"># a=45

# b="hyderabad"

# c=45

# d="hyderabad"

# Variable --- Memory Allocation of a value ....

# id --- Will return the memory allocation of value...
# print(id(a)) 
"""
print(id(c))

print(id(b))
print(id(d))

a1="hyderabad"
1a = "secundrabad"

a$ = "chennai"
"""
# comments -- Those line that startwith # those are called as comment in python..


# Rules for variable declaration:-
    # 1) varibales can be the combination of lowercase,uppercase and numbers..
    # 2) varibales should not be started with numbers...
    # 3) Varibales should not contain any special symbols except underscore(_)..
    # 4) Single Underscore can also be taken as varibale..(_ = 56).
    # 5) Keywords cannot be used as varibales...


# aA1 = 45
# a = 76
# A=87
# Aa1 = 98
# a1A = 23



# 1a = 54

# a( = 65
# a,b, = 78,56

# print(a)
# print(b)
# a$ = 78


# a_=56

# print(a_)

# _="hyderabad"

# print(_)


# if = 76

# else = 23



# a=56
# b=78



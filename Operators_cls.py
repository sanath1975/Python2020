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

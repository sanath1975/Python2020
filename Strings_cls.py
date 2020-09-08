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

#Task

# a = input("Enter a value:-") # 6


"""
2*2 = 4
3*3*3 = 27
4*4*4*4 = 256
5*5*5*5*5 = 3???
6*6*6*6*6*6 = ?????

"""
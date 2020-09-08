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

# print(a[-3])

# print(a[0:3])

# print(a[3:0:1])
# print(a[-3:-6:-1])
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

# Adding of element into the list

# append -- append is used for adding single elment at a time.. It will add the element at last index in the list..

# a=[34,'python',"django",56]

# print(a)

# # a.append('datascience')

# a.append([11,12,13])

# a.append(23)
# print(a)

# extend() - it is used for adding multiple elments into the list at a time...
# we have to pass only sequence in the extend...

# a.extend('django')

# a.extend([11,12,13])

# print(a)

# insert  -- It is used for adding single element at a time at specific index value.

# a=[34,'python',"django",56]

# a.insert(2,45)
a.insert(2,"datascience")

a.insert(2,[45,46,47])

# print(a)

# removal Methods

# remove -- It is for removing an element from the list...If the element not present it will throw and error...


# a.remove('python')
# a.remove('sagag') # will trown and error as elments not present in the list...
# print(a)

# pop -- It is also for removing the elment from the list.. based on index value of the elments..

# a.pop(3)

# print(a)

# clear() -- Removing all the elements and making it as empty list...

# a.clear()

# print(a)


# Nested Indexing -- performing indexing inside other indexing output..

a=[23,[11,12,13],"django",[51,52,53]]

# # print(a[1][2])

# a.append(54)
# a[3].append(54)
# print(a)

# for j in a:
#     if type(j) == list:
#         print(a.index(j))

# a[1].append(15)

# print(a)


# Accesssing methods
# index -- Will return the index value of an element inside the list..If the exement not present 
# it will through an error..

# print(a.index('django'))

# print(a.index('djan')) # error

# count -- how many times a particular element is repeated inside the list...

# print(a.count('django')) # 1

# print(a.count('djan')) # 0


# reverse() -- It will reverse the complete list...

# a=[23,[11,12,13],"django",[51,52,53]]

# a.reverse()

# print(a)

# sort() -- will sort all the values in an order..
# Sort will work for homogeneous datatype only..


# a=[34,24,67,54,859,54,75,12,84,839,42,94]

a= [""]
# print(a)

# # a.sort()

# a.sort(reverse=True)
# print(a)

# print(len(a))

# List comprehension:



# a=[64,63,82,54,96,32,657,65,96,31]

# even = []
# odd = []
# for j in a:
#     if j%2==0:
#         even.append(j)
#     else:
#         odd.append(j)

# print(even)
# print(odd)

# a=["rajesh@gmail.com","vindhya@gmail.com",'venkat@yahoo.com','kumar@yahoo.co.in','suresh@outlook.com','subash@gmail.com','raj@facebook.com']

# gmail = []
# yahoo = []
# outlook = []
# facebook = []


# for j in a:
#     if j.endswith('gmail.com'):
#         gmail.append(j)
#     elif j.endswith('yahoo.com') or j.endswith('yahoo.co.in'):
#         yahoo.append(j)
#     elif j.endswith('outlook.com'):
#         outlook.append(j)
#     elif j.endswith('facebook.com'):
#         facebook.append(j)

# print(gmail)
# print(yahoo)
# print(outlook)
# print(facebook)

# List Comprehension:

# Limitation:-
    # we can use only for loop, if and else conditional..
    # has to be writtened in single line...
    # We can use list methods. which will make chnages...

# a=[64,63,82,54,96,32,657,65,96,31]

# b=[]
# for j in [64,63,82,54,96,32,657,65,96,31]:
#     b.append(j)

# print(a)

# 1st way of syntax:-

# [expression for element in sequence]
# b=[]
# for j in [3,4,5,6,7]:
#     b.append(j*2)

# print(b)

# print([j*2 for j in [3,4,5,6,7]])


# b=[]
# for j in [3,4,5,6,7]:
#     if j%2==1:
#         b.append(j*2)

# print(b)

# 2nd way Syntax:-

# [expression for element in sequence if condition]
# print([j*2 for j in [3,4,5,6,7] if j%2==1])



b=[]
for j in [3,4,5,6,7]:
    if j%2==1:
        b.append(j*2)
    else:
        b.append(j*4)

print(b)


# 3rd Way of Syntax:
# [expression if condition else expression for element in sequence]

print([j*2 if j%2==1 else j*4 for j in [3,4,5,6,7]])

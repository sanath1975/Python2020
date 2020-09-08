# # Loop -- Iteration  --- Executing same line of code multiple numbers of times..

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
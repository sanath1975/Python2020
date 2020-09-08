
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
    print("Username doesnot matched")
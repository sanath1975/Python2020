
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

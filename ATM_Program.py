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

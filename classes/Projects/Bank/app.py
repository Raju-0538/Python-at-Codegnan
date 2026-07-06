# User table
from balance import balance
from deposit import deposit
from login import login
from logout import logout
from ministatement import mini_statement
from register import register
from transfer import transfer
from withdraw import withdraw



if __name__ == "__main__":
    print("Welcome")
    print("1.Register\n2.Login")
    choice = int(input("Select your choice"))
    # calling register function
    if choice == 1:
        print("Under Development process")
    #calling login function
    elif choice == 2:
        account = int(input("Enter your account number"))
        password = input("Enter your password")
        login_val = login(account=account,password=password)
        while login_val:
            print("The small scale bank providing services.....")
            print("1.Balance Enquiry\n2.Withdraw\n3.Deposit\n4.Transfer\n5.Mini Statement\n6.Logout")
            choice1 = int(input("Enter your choice(1-6)"))
            if choice1 == 1:
                # call balance function
                current_balance = balance(account=account)
                print(f"Current Balance is : {current_balance}")
            elif choice1 == 2:
                # call withdraw function
                amount = (int(input("Enter your withdraw amount")))
                res = withdraw(account=account,amount=amount)
                print(f"Withdraw is successful ! Current balance is{res}")
            elif choice1 == 3:
                amount = (int(input("Enter amount to deposit")))
                # call deposit function
                res = deposit(account=account,amount=amount)
                print(res)
            elif choice1 == 4:
                receiver = int(input("Enter receivers account Nummber"))
                amount = int(input("Enter transfer amount"))
                # call transfer function
                print(transfer(sender=account,receiver=receiver,transfer_amount=amount))
            elif choice1 == 5:
                # call ministatement :
                print(mini_statement(account=account))
            elif choice1 == 6:
                print(logout())
                exit()
            else:
                print("Enter the valid choice from 1 to 6")
    else:
        print("Enter the valid choice 1 or 2")



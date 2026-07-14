from register import register
from login import login
from addstock import addstock
from addtocart import addtocart
from adminlogin import adminlogin
from checkout import checkout
from logout import logout
from viewcart import viewcart
from removefromcart import removefromcart
from removestock import removestock
from updateprice import updateprice
from viewproducts import viewproducts

print("1.Admin\n2.User")
a = int(input("Select a choice 1 or 2 : "))
if a == 1:
        name = input("Enter your Email : ")
        password = input("Enter your Password : ")
        choice2 = adminlogin(email=name,password=password)
        while choice2:
            print("1. View Products\n2. Add Stock\n3. Remove Stock\n4. Update Price\n5. Logout")
            n = int(input("Enter your choice : "))
            if n == 1:
                viewproducts()
            elif n == 2:
                name = input("Enter Product Name : ").title()
                quantity = int(input("Enter Quantity : "))
                print(addstock(name=name,quantity=quantity))
            elif n == 3:
                name = input("Enter the Product name : ").title()
                quantity = int(input("Enter the Quantity to Add : "))
                print(removestock(name=name,quantity=quantity))
            elif n == 4:
                name = input("Enter the Product name : ").title()
                New_price = int(input("Enter the New Price : "))
                print(updateprice(name=name,price=New_price))
            elif n == 5:
                print("Thank you for your Service !")
                exit()
            else:
                print("Enter valid choice from 1 to 6")
elif a == 2:
    print("1. Register\n2. Login")
    choice = int(input("Enter a valid choice 1 or 2"))
    if choice == 1:
        email = input("Email : ")
        name = input("Name : ")
        password = input("Password : ")
        register(email,name,password)
    elif choice == 2:
        email = input("Enter your Email : ")
        password = input("Enteer your password : ")
        log = login(email,password)
        print(log)
        while log:
            print("1. View Products\n2. Add Products to Cart\n3. View Cart\n4. Remove Product from Cart\n5. Checkout\n6.Logout")
            choice1 = int(input("Enter your choice from 1 to 6 : "))
            if choice1 == 1:
                viewproducts()
            elif choice1 == 2:
                name = input("Enter Product Name : ").title()
                quantity = int(input("Enter the Quantity : "))
                res = addtocart(name=name,quantity=quantity)
                print(res)
            elif choice1 == 3:
                viewcart()
            elif choice1 == 4:
                name = input("Enter Product Name to Remove from Cart : ").title()
                quantity = int(input("Enter the Quantity : "))
                res = removefromcart(name = name,quantity=quantity)
                print(res)
            elif choice1 == 5:
                res = checkout()
                print(res)
            elif choice1 == 6:
                res = logout()
                print(res)
                exit()
            else:
                print("Enter valid choice form 1 to 6")

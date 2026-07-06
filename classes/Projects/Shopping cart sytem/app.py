from addproducts import addproducts
from checkout import checkout
from login import login
from logout import logout
from products import View_products
from register import register
from removeproducts import remove_products
from viewcart import view_cart

if __name__ == "__main__":
    print("Welcome to Shopping Cart system !")
    print("1. Register \n2. Login")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        res = register()
        print(res)
    elif choice == 2:
        acc = int(input("Enter your Login ID : "))
        password = input("Enter your Password : ")
        login_val = login(account=acc,password=password)
        while login_val:
            print("1. View Products\n2. Add Products to Cart\n3. View Cart\n4. Remove Product from Cart\n5. Checkout\n6.Logout")
            choice1 = int(input("Enter your choice from 1 to 6 : "))
            if choice1 == 1:
                View_products()
            elif choice1 == 2:
                name = input("Enter Product Name : ").title()
                quantity = int(input("Enter the Quantity : "))
                res = addproducts(name=name,quantity=quantity)
                print(res)
            elif choice1 == 3:
                view_cart()
            elif choice1 == 4:
                name = input("Enter Product Name to Remove from Cart : ").title()
                quantity = int(input("Enter the Quantity : "))
                res = remove_products(name = name,quantity=quantity)
                print(res)
            elif choice1 == 5:
                res = checkout()
                print(res)
            elif choice1 == 6:
                res = logout()
                print(res)
            else:
                print("Enter valid choice form 1 to 6")
        else:
            print("Enter valid Credentials")
    else:
        print("Enter valid choice 1 or 2")

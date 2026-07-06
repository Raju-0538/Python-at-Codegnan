from addproducts import addproducts
from checkout import checkout
from login import login
from logout import logout
from products import View_products
from register import register
from removeproducts import remove_products
from viewcart import view_cart
from addStock import addStock
from adminlogin import admin_login
from removeStock import removeStock
from updatePrice import updaatePrice

if __name__ == "__main__":
    print("Welcome to Shopping Cart system !")
    print("1. Admin\n2. User")
    a = int(input("Eneter a valid choice : "))
    if a == 1:
        name = input("Enter your Name : ")
        password = input("Enter your Password : ")
        choice2 = admin_login(account=name,password=password)
        while choice2:
            print("1. View Products\n2. Add Stock\n3. Remove Stock\n4. Update Price\n5. Logout")
            n = int(input("Enter your choice : "))
            if n == 1:
                View_products()
            elif n == 2:
                name = input("Enter Product Name : ").title()
                quantity = int(input("Enter Quantity : "))
                print(addStock(name=name,quantity=quantity))
            elif n == 3:
                name = input("Enter the Product name : ").title()
                quantity = int(input("Enter the Quantity to Add : "))
                print(removeStock(name=name,quantity=quantity))
            elif n == 4:
                name = input("Enter the Product name : ").title()
                New_price = int(input("Enter the New Price : "))
                print(updaatePrice(name=name,price=New_price))
            elif n == 5:
                print("Thank you for your Service !")
                exit()
            else:
                print("Enter valid choice from 1 to 6")

    elif a == 2:
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
    else:
        print("Enter a valid choice 1 or 2")

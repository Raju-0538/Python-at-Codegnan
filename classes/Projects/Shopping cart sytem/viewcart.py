from data import products
from data import Cart

def view_cart():
    if len(Cart) > 0:
        for j in Cart:
            print(f"{j} : {Cart[j]}")
    else:
        print("Your Cart is Empty")
# print(view_cart())
from data import products
from data import Users
from data import Cart

def addproducts(name:str,quantity:int):
    if name in products:
        if quantity <= products[name]['stock']:
            Cart[name] = Cart.get(name,0)+quantity
            products[name]['stock'] -= quantity
            return f"{name} is added to cart successfully"
        else:
            return f"{name} stock is not available"
    return f"{name} product is not available"
# name = input("Enter product name : ")
# q = int(input("Quamtity"))
# print(addproducts(name=name,quantity=q))

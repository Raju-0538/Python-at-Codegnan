from data import products
from data import Cart

def remove_products(name:str,quantity:int):
    if name in Cart:
        if quantity <= Cart[name]:
            Cart[name] = Cart.get(name)-quantity
            products[name]['stock'] += quantity 
            return f"{name} is removed from Cart successfully !"
        else:
            return f"Your Quantity exceeds the cart Quantity"
    return f"{name} not in the Cart"
# name = input("Name")
# q = int(input("Quantity"))
# print(remove_products(name=name,quantity=q))
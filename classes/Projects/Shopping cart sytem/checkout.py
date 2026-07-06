from data import products
from data import Cart

def checkout():
    total = 0
    if len(Cart) > 0:
        for i in Cart:
            if Cart[i]>0:
                total += (products[i]['price'] * Cart[i])
                print(f"Your Total for {i} : {products[i]['price'] * Cart[i]}")
            else:
                return "Your cart is Empty ! Add some Items"
        Cart.clear()
        return f" Your Total Bill : {total}"
    return "Your cart is Empty ! Add some Items"
# print(checkout())
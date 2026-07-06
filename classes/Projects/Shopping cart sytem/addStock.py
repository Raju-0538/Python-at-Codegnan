from data import products

def addStock(name:str,quantity:int):
    if name in products:
        products[name]['stock'] += quantity
    else:
        price = int(input("Enter the price : "))
        products[name] = {
        "price": price,
        "stock": quantity
    }

    return f"{name} stock is updated successfully !!"
from data import products

def updaatePrice(name:str,price:int):
    if name in products:
        products[name]['price'] = price
    else:
        return f"{name} is not found in Products"
    return f"{name} price updated successfully!"
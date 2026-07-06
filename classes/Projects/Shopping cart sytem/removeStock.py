from data import products

def removeStock(name:str,quantity:int):
    if name in products:
        products[name]['stock'] -= quantity
    else:
        return f"Stock is not found !"

    return f"{name} stock is updated successfully !!"
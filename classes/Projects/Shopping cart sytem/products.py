from data import products

def View_products():
    print("The products that are available : ")
    for i in products:
        print(f"{i}")
        print(f"Stock : {products[i]['stock']}")
        print(f"Price : {products[i]['price']}")
        print("*"*50)
# View_products()
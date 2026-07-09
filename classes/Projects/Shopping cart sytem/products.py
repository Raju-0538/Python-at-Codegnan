from data import products

def View_products(role='user'):
    print("The products that are available : ")
    for i in products:
        if products[i]['stock'] > 0 :
            print(f"{i}")
            print(f"Stock : {products[i]['stock']}")
            print(f"Price : {products[i]['price']}")
            print("*"*50)

import csv
import os


def removestock(name: str, quantity: int):

    products = {}

    if os.path.exists("Products.csv"):

        with open("Products.csv", "r", newline="") as f:
            reader = csv.DictReader(f)

            for row in reader:
                products[row["product"]] = {
                    "stock": int(row["stock"]),
                    "price": int(row["price"])
                }

    else:
        return "Products.csv does not exist!"

    if name not in products:
        return "Product Not Found!"

    if quantity > products[name]["stock"]:
        return "Quantity exceeds the Stock !"

    products[name]["stock"] -= quantity

    fields = ["product", "stock", "price"]

    with open("Products.csv", "w", newline="") as f:

        writer = csv.DictWriter(f, fieldnames=fields)

        writer.writeheader()

        for product, details in products.items():

            writer.writerow({
                "product": product,
                "stock": details["stock"],
                "price": details["price"]
            })

    return "Stock Updated Successfully!"

import csv
import os

def addstock(name: str, quantity: int):

    products = {}

    # Step 1: Read existing products
    if os.path.exists("Products.csv"):

        with open("Products.csv", "r", newline="") as f:
            reader = csv.DictReader(f)

            for row in reader:
                products[row["product"]] = {
                    "stock": int(row["stock"]),
                    "price": int(row["price"])
                }

    # Step 2: Update or Add
    if name in products:
        products[name]["stock"] += quantity
        print("Stock Updated Successfully!")

    else:
        price = int(input("Enter the Price of the product : "))
        products[name] = {
            "stock": quantity,
            "price": price
        }
        print("Product Added Successfully!")

    # Step 3: Write everything back to the CSV
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

# Example
# addstock("Laptop", 5, 55000)
# addstock("Mouse", 10, 500)
# addstock("Laptop", 3, 55000)
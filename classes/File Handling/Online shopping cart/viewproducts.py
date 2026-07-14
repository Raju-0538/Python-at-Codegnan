import csv
import os

def viewproducts():
    if os.path.exists('Products.csv'):
        with open('Products.csv','r') as f:
            read = csv.DictReader(f)
            for row in read:
                print(row['product'])
                print(f"Stock : {row['stock']}")
                print(f"Price : {row['price']}")
                print('*'*50)
            
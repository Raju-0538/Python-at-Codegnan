import csv
import os

def AdminRegister(email:str,name:str,password:str):
    exist = False
    if os.path.exists('Admin.csv'):
        with open('Admin.csv','r') as f:
            read = csv.DictReader(f)

            for i in read:
                if email == i['email']:
                    print("User already Exist !")
                    exist = True
                    break
    if not exist:
        field = ['email','name','password']
        admin = {}
        admin[email] = {
            "name" : name,
            "password" : password
        }
        with open('Admin.csv','a',newline="") as f:
            w = csv.DictWriter(f,fieldnames=field)

            if f.tell() == 0:
                w.writeheader()
            for email,details in admin.items():
                w.writerow({
                    "email" : email,
                    "name" : details["name"],
                    "password" : details["password"]
                })
        print(f"Registered successfully !")


email = input("Email : ")
name = input("Name : ")
password = input("Password : ")
AdminRegister(email,name,password)
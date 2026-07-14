import csv
import os

def register(email:str,name:str,password:str):
    exist = False
    if os.path.exists('User.csv'):
        with open('User.csv','r') as f:
            read = csv.DictReader(f)

            for i in read:
                if email == i['email']:
                    print("User already Exist !")
                    exist = True
                    break
    if not exist:
        field = ['email','name','password']
        user = {}
        user[email] = {
            "name" : name,
            "password" : password
        }
        with open('User.csv','a',newline="") as f:
            w = csv.DictWriter(f,fieldnames=field)

            if f.tell() == 0:
                w.writeheader()
            for email,details in user.items():
                w.writerow({
                    "email" : email,
                    "name" : details["name"],
                    "password" : details["password"]
                })
        print(f"Registered successfully !")


# email = input("Email : ")
# name = input("Name : ")
# password = input("Password : ")
# register(email,name,password)
import csv
import pandas as pd
# n = int(input("enter the N value : " ))
# fields = ['name','age','gender']

# with open("Information.csv","w",newline="") as f:
#     writer = csv.DictWriter(f,fieldnames=fields)
#     writer.writeheader()
#     for i in range(n):
#         name = input("Enter your name :")
#         age = int(input("Enter your age : "))
#         gender = input("Enter your gender : ")
#         writer.writerow({'name' : name,'age' : age,'gender' : gender})

# with open('Information.csv','r') as f:
#     read = csv.DictReader(f)
#     for i in read:
#         print(i)


fields = ['id','name','password']
x = int(input("Enter X value : "))
users = {}

for i in range(x):
        id = int(input("ID : "))
        name = input("Name : ")
        password = input("Password : ")
        users[id] = {
            'name' : name,
            'password' : password
        }
with open("Nested.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields)

    writer.writeheader()

    for user_id, details in users.items():
        writer.writerow({
            "id": user_id,
            "name": details["name"],
            "password": details["password"]
        })
data = pd.read_csv('Nested.csv')
df = pd.DataFrame(data)
print(df)
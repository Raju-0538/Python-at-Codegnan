import csv

def adminlogin(email, password):

    with open("Admin.csv", "r", newline="") as f:

        reader = csv.DictReader(f)

        for row in reader:

            if row["email"] == email:

                if row["password"] == password:
                    return True

                return "Incorrect Password!"

        return "Admin Not Found!"

# email = input("Email: ")
# password = input("Password: ")

# print(adminlogin(email, password))
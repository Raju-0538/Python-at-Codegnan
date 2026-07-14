import csv

def login(email, password):

    with open("User.csv", "r") as f:

        reader = csv.DictReader(f)

        for row in reader:

            if row["email"] == email:

                if row["password"] == password:
                    return True

                return "Password is Incorrect!"

        return "User Not Found!"
print(login('rajkumar.gariki@sasi.ac.in','Abi@123'))
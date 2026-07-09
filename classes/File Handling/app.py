import csv
import pandas as pd

fields = ['name','age','email']
n = int(input("Enter the N value : "))

with open('students.csv','w',newline='') as f:
    write = csv.DictWriter(f,fieldnames=fields)
    write.writeheader()
    for i in range(n):
        students = {}
        students['name'] = input("Enter name : ")
        students['age'] = int(input("Enter age : "))
        students['email'] = input("Enter email : ")
        write.writerow(students)

    print("Data added Successfully !")
with open('students.csv','r') as file:
    read = csv.DictReader(file)
    for i in read:
        print(i)
f = pd.read_csv('Details.csv')
print(f)
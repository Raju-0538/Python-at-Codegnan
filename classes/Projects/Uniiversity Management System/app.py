from data import Student_data
from data import Employee_data

class Person:
    def __init__(self, name,age,gender,email):
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email
    def Details(self):
        return f"My name is {self.name} and iam {self.age} Years Old."
class Student(Person):
    def __init__(self,name,age,gender,email,stdid,branch):
        super().__init__(name,age,gender,email)
        self.stdid = stdid
        self.branch = branch
    def Percentage(self, Marks):
        return f"Your Percentage is : {(sum(Marks)/len(Marks))*100}"
class Employee(Person):
    def __init__(self,name,age,gender,email,role,subjects,empid):
        super().__init__(name,age,gender,email)
        self.role = role
        self.subjects = subjects
        self.empid = empid
    def DisplaySalary(self, Working_days):
        return f"{self.name} salary is {Working_days * 2000}"
class University(Student, Employee):
    def __init__(self,name,age,gender,email,stdid,empid,role,subjects):
        Student.__init__(self,name,age,gender,email,stdid)
        Employee.__init__(self,name,age,gender,email,empid,role,subjects)
    def AddStudent(self):
        if {self.email} == Student_data[self.stdid]['email']:
            return "User Already Exist"
        Student_data['stdid'] = max(Student_data)+1
        Student_data[self.stdid]['email'] = {self.email}
        




# e = Employee("Raju",22,"Male","rajkumar.gariki7@gmail.com","Trainer",['Python','Java'])
# print(e.DisplaySalary(5))
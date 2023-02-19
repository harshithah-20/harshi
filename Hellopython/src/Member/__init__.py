     
class Member:
    def init(self,name,age,phonenumber,address,salary):
        self.name=name
        self.age=age
        self.phonenumber=phonenumber
        self.address=address
        self.salary=salary
    def printsalary(self):
        print(self.salary)
class Employee(Member):
    def init(self,specialization,name,age,phonenumber,address,salary):
        self.specialization=specialization
        Member.init(self,name,age,phonenumber,address,salary)
class Manager(Member):
    def init(self,department,name,age,phonenumber,address,salary):
        self.department=department
        Member.init(self,name,age,phonenumber,address,salary) 
emp=Employee()
emp.printsalary()
mang=Manager()
mang.printsalary()   
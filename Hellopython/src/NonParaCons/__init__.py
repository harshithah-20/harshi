class Student:  
    # Constructor - non parameterized  
    def __init__(self):  
        print("This is non parametrized constructor")  
    def show(self,name):  
        print("Hello",name)  
student = Student()  
student.show("John")


class Employee:
    def _init_ (self):
        print("Non Parametrized constructor")
    def show(self,name):
        print("Welcome all",name)
emp = Employee()
emp.show("to the company")


class Family:
    def _init_(self):
        print("Nulear family is better than joint family")
    def show(self):
        print("There are 4 members in a family")
    def display(self,children):
        print("I love",children)
fam = Family()
fam.display("my family")
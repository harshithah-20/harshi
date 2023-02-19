class Student:  
    roll_num = 101  
    name = "Joseph"    
    def display(self):  
        print(self.roll_num,self.name)  
  
st = Student()  
st.display()

class Employee:  
    id = 101  
    name = "Payal"  
    age = 20
    def display(self):  
        print(self.id,self.name,self.age)  
  
emp = Employee()  
emp.display()

class Teacher:
    Name="Priya" 
    Tclass = 10
    Subject="Science"
    def display(self): 
        #Teacher. c = Teacher. c + 1
        print (self.Name,self.Tclass,self.Subject) 
t = Teacher() 
t.display() 

#Area of a circle
class Circle: 
    Circle=int(input("Enter a number"))
    
    r = 5*5 
    pi = 3.14  
    def display(self):  
        print(self.r,self.pi)  

cir = Circle()  
cir.display()



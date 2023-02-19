arr = []
arr = [0 for i in range(5)] 
print(arr)
#creating Array an initializer 

arr_num = [0] * 2
print(arr_num)

arr_str = ['P'] * 5
print(arr_str)


#Class
class Employee:
    id = 10
    name = "Harish"
    def display(self):
        print(self.id,self.name)
        
emp=Employee()
emp1=Employee()
emp.display();
emp1.display();

print()

class Employeee:    
    def display (self,id,name):    
        print(id,name)

emp = Employeee ()    
emp1 = Employeee()
emp2 = Employeee()
emp.display(1,"swami");
emp1.display(2,"vinay");
emp2.display(3,"sahana")

print()

arr_circle = [3.14]*5*5
print(arr_circle)

arr_multiply = [453]*8
print(arr_multiply)

arr_func = []
arr_func = [15 for i in range(9)] 
arr_func = [30 for j in range(7)]
print(arr_func)

print()

class Rectangle:
    width = 20
    length = 30
    def display(self):
        print(self.width,self.length)
        
rect=Rectangle()
rect1=Rectangle()
rect.display();
rect1.display();

print()

class Operations:
    name1 = 'Add'
    number1 = 10+50
    name2 = 'Substract'
    number2 = 20-35
    name3 = 'Multiply'
    number3 = 40*37
    name4 = 'Divide'
    number4 = 59/7
    def display(self):
        print(self.name1,self.number1,self.name2,self.number2,self.name3,self.number3,self.name4,self.number4)
        
oper=Operations()
oper1=Operations()
oper.display();
oper1.display();

print()

class Student:    
    def display (self,subject,marks,Sname):    
        print(subject,marks,Sname)
        
stud = Student ()    
stud1 = Student()
stud2 = Student()
stud3 = Student()
stud.display("Kannada",82,"Anusha");
stud1.display("English",63,"Bindu");
stud2.display("Maths",35,"Harini");
stud3.display("Social",78,"Shivani")

print()

class Student1:    
    def display (self,Number,Name,Grade):    
        print(Number,Name,Grade)
        
stu = Student ()    
stu1 = Student()
stu2 = Student()
stu3 = Student()
stud.display(75,"Savitha","B");
stud1.display(81,"Prerana","A");
stud2.display(53,"Akshara","D");
stud3.display(65,"Vinutha","C");







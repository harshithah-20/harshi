class Animal:  
    def speak(self):  
        print("Animal Speaking")  
#The child class Dog inherits the base class Animal  
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
#The child class Dogchild inherits another child class Dog  
class DogChild(Dog):  
    def eat(self):  
        print("Eating bread...")  
d = DogChild()  
d.bark()  
d.speak()  
d.eat()

print()

class Shape:
    def shapes(self):
        print("Gives different Shapes")
class Circle(Shape):
    def Carea(self):
        print("This is Circular shape")
class Rectangle(Circle):
    def RArea(self):
        print("This is Rectangular shape")
d=Rectangle()
d.shapes()
d.Carea()
d.RArea()

print()

class Member:
    def Mdatamembers(self):
        print("print salary")
class Employee(Member):
    def Edatamembers(self):
        print("print department")
class Department(Employee):
    def Ddatamembers(self):
        print("print specialization")
d=Department()
d.Mdatamembers()
d.Edatamembers()
d.Ddatamembers()

print()

class Mother1:  
    mothername1 = ""  
    def mother1(self):  
        print(self.mothername1)    
class Father1:  
    fathername1 = ""  
    def father1(self):  
        print(self.fathername1)    
class Son1(Mother1, Father1):  
    def parents1(self):  
        print ("Father name is :", self.fathername1)  
        print ("Mother name is :", self.mothername1)  
  
s1 = Son1()  
s1.fathername1 = "Rajesh"  
s1.mothername1 = "Shreya"  
s1.parents1()  
        
        

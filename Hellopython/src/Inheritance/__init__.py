#single level inheritance
from test.test__opcode import SpecializationStatsTests
class Animal:  
    def speak(self):  
        print("Animal Speaking")  
#child class Dog inherits the base class Animal  
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
d = Dog()  
d.bark()  
d.speak()

print()


class Circle:
    def area(self):
        print("area of a circle")
class Rectangle(Circle):
    def Area(self):
        print("Area of a rectangle")
d=Rectangle()
d.area()
d.Area()
  
print()
    
class Parent1:  
    def func_1(self):  
        print ("This function is defined inside the parent class.")    
class Child1(Parent1):  
    def func_2(self):  
        print ("This function is defined inside the child class.")   

object = Child1()  
object.func_1()  
object.func_2()




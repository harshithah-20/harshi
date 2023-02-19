
from abc import ABC, abstractmethod
class Animal(ABC): 
    def move(self):
        pass 
class Human(Animal): 
    def move(self):
        print("I can walk and run") 
class Snake(Animal):
    def move(self):
        print("I can crawl") 
class Dog(Animal): 
    def move(self):
        print("I can bark") 
class Lion(Animal): 
    def move(self):
        print("I can roar")        
# Driver code
R = Human()
R.move()
K = Snake()
K.move() 
R = Dog()
R.move() 
K = Lion()
K.move()



from abc import ABC, abstractmethod
class Polygon(ABC):
    def noofsides(self):
        pass
class Triangle(Polygon):
    def noofsides(self):
        print("It has 3 sides")
class Pentagon(Polygon):
    def noofsides(self):
        print("It has 5 sides")
class Hexagon(Polygon):
    def noofsides(self):
        print("It has 6 sides")
class Quadrilateral(Polygon):
    def noofsides(self):
        print("It has 4 sides")
R=Triangle()
R.noofsides()
K=Quadrilateral()
K.noofsides()
R=Pentagon()
R.noofsides()
K=Hexagon()
K.noofsides()
              
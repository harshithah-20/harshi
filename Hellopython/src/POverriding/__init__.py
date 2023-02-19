class Vehicle:        # define parent class
   def run(self):
      print('Vehicle is running')

class Bike(Vehicle) : # define child class
   def run(self):
      print('Bike is running')

c = Bike()          # instance of child
c.run()         # child calls overridden method


class Transport:
    def show(self):
        print("Land is one mode transportation")
class Transport1:
    def show(self):
        print("Air is one mode of transportation") 
class Transport2:
    def show(self):
        print("Water is one mode of transportation")
trans = Transport2()
trans.show()


class Positive:
    def Numbers(self):
        print("It displays only positive numbers")
class Negative:
    def Numbers(self):
        print("It displays only negative numbers")
num = Negative()
num.Numbers()
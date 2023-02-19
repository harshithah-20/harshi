from abc import ABC, abstractmethod
class Bank(ABC):
   @abstractmethod
   def balance_check(self):
        pass
   @abstractmethod
   def interest(self):
       pass
class SBI(Bank):
   def balance_check(self):
       print("Balance is 100 rupees")
   def interest(self):
       print("SBI interest is 5 rupees")
s = SBI()
s.balance_check()
s.interest()


import abc
class Food(abc.ABC):
    def taste(self):
        pass
class north_indian(Food):
    def taste(self):
        print("Cooking!")
s=north_indian()
print(isinstance(s,Food))
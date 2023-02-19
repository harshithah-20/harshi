
from abc import ABC, abstractmethod
class Bank(ABC): 
    def getbalance(self):
        pass 
class BankA(Bank): 
    def getbalance(self):
        print("$100 is deposited") 
class BankB(Bank):
    def getbalance(self):
        print("$200 is deposited") 
class BankC(Bank): 
    def getbalance(self):
        print("$300 is deposited")        

B = BankA()
B.getbalance()
A = BankB()
A.getbalance() 
B = BankC()
B.getbalance() 



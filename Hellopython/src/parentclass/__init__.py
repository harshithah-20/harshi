

from abc import ABC, abstractmethod
class Parent(ABC): 
    def message(self):
        pass 
class SubclassA(Parent): 
    def message(self):
        print("This is first subclass") 
class SubclassB(Parent):
    def message(self):
        print("This is second subclass") 

S = SubclassA()
S.message()
P =SubclassB()
P.message() 

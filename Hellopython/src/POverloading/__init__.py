class emp:
    def hello_emp(self,e_name=None):
        if e_name is not None:
            print("Hello",e_name)
        else:
            print("Helloo")
Emp1=emp()
Emp1.hello_emp()
Emp1.hello_emp("Kiran")


class Overloading:
    #Overload()
    #signature()
    def getMethod(self, j):
        print("First method", j)
        #getMethod.overload
        #signature("int")
    def getmethod(self,i):
        print("Second method", i)
obj = Overloading()
obj.getmethod(1)
obj.getMethod(2)


# First product method.
# Takes two argument and print their
# product
def product(a, b):
    p = a * b
    print(p) 
# Second product method
# Takes three argument and print their
# product
def product1(a, b, c):
    p = a * b * c
    print(p) 
# Uncommenting the below line shows an error
#p1=prod()
#product(4, 5) 
# This line will call the second product method
product1(4, 5, 5)


class Operations:
    def diff_operators(self,d_op=None):
        if d_op is not None:
            print("Add",d_op)
        else:
            print("Subtraction")
opr=Operations()
opr.diff_operators()
opr.diff_operators("the numbers") 


class humans:
    def typesofpersons(self,ty_of=None):
        if ty_of is not None:
            print("Homo",ty_of)
        else:
            print("Denisovans")
pers=humans()
pers.typesofpersons()
pers.typesofpersons("habilis")
        
        
        
        
        
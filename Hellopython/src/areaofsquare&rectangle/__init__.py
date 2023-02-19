'''Create a class to print the area of a square and a rectangle. The class has two methods with 
the same name but different number of parameters. The method for printing area of rectangle 
has two parameters which are length and breadth respectively while the other method for printing 
area of square has one parameters which is side of square. '''

class area:
    def methods(self,l,b):
        self.l=l
        self.b=b
        rec=l*b
        print("area of rectangle:",rec)
    def methods(self,s):
        self.s=s
        sq=s*s
        print("area of square:",sq)
pr1=area()
pr1.methods(10)
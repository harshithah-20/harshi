class Employee:  
    def __init__(self, name, id):  
        self.id = id  
        self.name = name  
  
    def display(self):  
        print("ID: %d \nName: %s" % (self.id, self.name))  
    
emp1 = Employee("Vinay", 101)  
emp2 = Employee("Metha", 102)    
# accessing display() method to print employee 1 information    
emp1.display()   
# accessing display() method to print employee 2 information  
emp2.display()

print()


class Library: 
    def __init__(self, id, BookName, Publisher, author):  
        self.id = id  
        self.BookName = BookName 
        self.Publisher = Publisher
        self.author = author
           
    def display(self):  
        print("id: %s \nBookName: %s \nPublisher: %s \nAuthor: %s" % (self.id, self.BookName, self.Publisher,self.author))  
    
lib1 = Library(101, "PickwickPapers", "ArcadePublishing", "CharlesDickens")  
lib2 = Library(102, "ParikshaGuru", "Plume", "ShrinivasDas")   
lib3 = Library(103, "Indulekha", "LbBooks", "ChanduMenon" )   
lib4 = Library(104, "KhareBaire", "Scribner", "RabindranathTagore")   
lib1.display()     
lib2.display()
lib3.display()
lib4.display()

print()



class Triangle: 
    def __init__(self, breadth, height):  
        self.breadth = breadth 
        self.height = height 
           
    def area(self):  
        return self.breadth * self.height
    
x=int(input("Enter the breadth of the triangle: "))
y=int(input("Enter the height of the triangle: "))

tri=Triangle(x,y)
print("Area of Triangle is: ",tri.area())




#Area of a circle
print("To find the area of circle")
pi=20
r=10
A=pi*r*r
print("The area of circle is=", A)

#Number is Even or Odd
print("To find a number is even or odd")
n=3
if n%2==0:
    print("Number is even")
else:
    print("Number is odd") 

#Greatest of two numbers    
print("To find the greatest of two numbers")
n1=20
n2=40
if n1>n2:
    print(n1)
else:
    print(n2)
   
#Area of Rectangle    
print("To find the area of rectangle")
w=40
l=30
A=w*l
print("The area of rectangle is=", A)

#Nested if and elif function(+ve number,Zero,-ve number)
num = 3.4
# num = 0
# num = -4.5
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
    

#Nested if function
num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
        print("Negative number")
        

year=int(input("Enter a year:"))
if year%4==0:
    print("Entered year is a Leap Year")
else:
    print("Entered year is not Leap Year")
   

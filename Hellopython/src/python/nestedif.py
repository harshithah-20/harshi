'''
Created on 25-Nov-2022

@author: Admin
'''
#Program to display day of the week. Mon,Tue,Wed,Thur,Fri,Sat,Sun
weekday=int(input("Enter number of days in a week"))
if weekday==1:
    print("Monday")
elif weekday==2:
    print("Tuesday")
elif weekday==3:
    print("Wednesday")
elif weekday==4:
    print("Thursday")
elif weekday==5:
    print("Friday")
elif weekday==6:
    print("Saturday")
elif weekday==7:
    print("Sunday")
else:
    print("Entered day in a week does not exist")
    
    
#Program to initialize 5 subject marks and find their average based on the average display grades.
average=int(input("Enter the marks"))
if average>=75:
    print("Distinction")
elif average>=60 and average<=75:
    print("First class")
elif average>=50 and average<=60:
     print("Second class")
elif average>=35 and average<=50:
    print("Third class")
else:
    print("Fail")  
        
#Program for addition,subtraction,multiplication,division,modulus.
print("To find addition,subtraction,multiplication,division,modulus")
n=int(input("Enter a value"))
a=int(input("Enter a number"))
b=int(input("Enter a number"))
if(n==0):
    print("Add",a+b)
elif(n==1):
    print("Sub",a-b)
elif(n==2):
    print("Mult",a*b)
elif(n==3):
    print("div",a/b)
else:
    print("mod",a%b)
    
    
month=int(input("Enter the months of the year"))
if month==1:
    print("January")
elif month==2:
    print("Febraury")
elif month==3:
    print("March")
elif month==4:
    print("April")
elif month==5:
    print("May")
elif month==6:
    print("June")
elif month==7:
    print("July")
elif month==8:
    print("August")
elif month==9:
    print("September")
elif month==10:
    print("October")
elif month==11:
    print("November")
elif month==12:
    print("December")
else:
    print("Entered Month does not exist")
    

sides=int(input("Enter the sides of the different shapes"))
if sides==0:
    print("Circle")
elif sides==2:
    print("Prallelogram")
elif sides==3:
    print("Triangle")
elif sides==4:
    print("Square")
elif sides==5:
    print("Pentagon")
elif sides==6:
    print("Hexagon")
elif sides=="equal":
    print("Rhombus")
else:
    print("There are no shapes to display")
    
    







  


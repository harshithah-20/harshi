'''
Created on 25-Nov-2022

@author: Admin
'''
#Any year which is evenly divisible by 4 is a leap year 
#Any year that is divisible by 100 is not a leap year

year=int(input("Enter a year:"))
if year%4==0:
    print("Entered year is a Leap Year")
else:
    print("Entered year is not Leap Year")
   
    
lang = input("What's the programming language you want to learn? ")
match lang:
    case "JavaScript":
        print("You can become a web developer.")
    case "Python":
        print("You can become a Data Scientist")
    case "PHP":
        print("You can become a backend developer")
    case "Solidity":
        print("You can become a Blockchain developer")
    case "Java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")

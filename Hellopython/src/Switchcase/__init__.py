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


week = input("What is the week you want to display in a month? ")
match week:
    case "Monday":
        print("1st day of the week is displayed")
    case "Tuesday":
        print("2nd day of the week is displayed")
    case "Wednesday":
        print("3rd day of the week is displayed")
    case "Thursday":
        print("4th day of the week is displayed")
    case "Friday":
        print("5th day of the week is displayed")
    case "Saturday":
        print("6th day of the week is displayed")
    case "Sunday":
        print("7th day of the week is displayed")
    case _:
        print("There is no day to display")
        
        
year=input("Enter the months of the year")
match year:
    case "January":
        print("It is the 1st month of the year")
    case "Febraury":
        print("It is the 2rd month of the year")
    case "March":
        print("It is the 3rd month of the year")   
    case "April":
        print("It is the 4th month of the year")
    case "May":
        print("It is the 5th month of the year")
    case "June":
        print("It is the 6th month of the year")
    case "July":
        print("It is the 7th month of the year")
    case "August":
        print("It is the 8th month of the year")
    case "September":
        print("It is the 9th month of the year")
    case "October":
        print("It is the 10th month of the year")
    case "November":
        print("It is the 11th month of the year")
    case "December":
        print("It is the 12th month of the year")
    case _:
        print("No more months to display")
        
        
shapes=input("enter the different shapes")
match shapes:
    case "Circle":
        print("It is of round shaped and has no sides")
    case "Triangle":
        print("It has 3 sides")
    case "Square":
        print("It is a two dimensional closed shape and has 4 sides")
    case "Rectangle":
        print("It is a closed flat shape and has 4 sides")
    case "Pentagon":
        print("It is of geometrical shape and It has 5 sides")
    case "Hexagon":
        print("It has 6 sides")
    case "parallelogram":
        print("It is a quadrilateral and has 2 pairs of parallel sides")
    case "Quadrilateral":
        print("It is a 4 sided closed figure")
    case "Sphere":
        print("It is of round shape and has no sides")
    case "Rhombus":
        print("It is a quadrilateral and all sides are equal")
    case _:
        print("No more shapes to display")
        
        
        
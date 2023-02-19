h=float(input("Enter your height in meters: "))
w=float(input("Enter your Weight in Kg: "))
BMI=w/(h*h)
print("BMI Calculated is:",BMI)
if(BMI>0):
    if(BMI<=16):
        print("You are very underweight")
    elif(BMI<=18.5):
        print("You are underweight")
    elif(BMI<=25):
        print("Congrats! You are Healthy")
    elif(BMI<=30):
        print("You are overweight")
    else: 
        print("You are very overweight")
else:
    print("enter valid details")
    

weight = int(input("enter weight value"));
height = float(input("enter height"));
bmi = weight/float(height*height);
if bmi < 15:
    print('Underweight')
elif  bmi>=18.5 and bmi<25:
    print("Normal")
elif bmi >= 25 and bmi <= 35:
   print('Overweight')
else:
   print('Obesity')

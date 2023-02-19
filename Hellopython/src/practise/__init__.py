#find the ascii value of a character
ch= input("Enter a character:")
ascii = ord(ch)
print("ASCII value of ",ch,"is:",ascii)


ch=input("Enter a character:")
if (ch=='a',ch=='A',ch=='e', ch=='E', ch=='i', ch=='I', ch=='o',ch=='O',ch=='u',ch=='U'):
    print("Entered characters is Vowels")
else:
    print("Entered characters are consonents")
 
    
n=input("Enter a number")
if n%7==0:
    print("Entered number is prime number")
else:
    print("Entered number is not a prime number")
fruits = ["apple","cherry","banana","mango"]
for x in fruits:
  print(x)
  if x == "banana":
    break
print()

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


word="anaconda"
for letter in word:
    print (letter) 
    
      
nums = (1, 2, 3, 4)
sum_nums = 0
for num in nums:
    sum_nums = sum_nums + num
print(f'Sum of numbers is {sum_nums}')


num = int(input("Enter a number:"))    
print("Multiplication table of:")  
for i in range(1,11):    
   print(num,'x',i,'=',num*i)
   

number=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
add_nums = 0
for num in number:
    add_nums=num
    if(num%2==0):
      print("Even numbers are:",num)      
    else:
       print("Odd numbers are:",num)
       


 
 
 







 
    
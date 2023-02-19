for i in range(1, 11):
    # nested loop
    # to iterate from 1 to 10
    for j in range(1, 11):
        # print multiplication
        print(i * j, end=' ')
    print()


i = 1
while i < 6:
  print(i)
  i += 1


#1 
#2 2 
#3 3 3 
#4 4 4 4 
#5 5 5 5 5 
for i in range(6): # 1,2,3,4,5
    for j in range(i):
        print(i, end=' ')
    print()    
print()

for i in range(6):
    for j in range(i,0,-1):
        print(i, end=' ')
    print()    
print()

for i in range(1,6):
    for j in range(i,0,-1):
        print(i, end=' ')
    print()     
print()

#1 
#2 1 
#3 2 1 
#4 3 2 1 
#5 4 3 2 1 
for i in range(1,6):
    for j in range(i,0,-1):
        print(j, end=' ')
    print()    
print()

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5    
for i in range(1,6): #0,1,2,3,4,5
    for j in range(1,i+1): #1,0+1=1  , 1,1+1=1,2  , 1,2+1=1,2,3 , 1,3+1=1,2,3,4  , 1,4+1=1,2,3,4,5
        print(j, end=' ')
    print()
print()


#5 5 5 5 5 5 
#4 4 4 4 4 
#3 3 3 3 
#2 2 2 
#1 1
for i in range(i,0,-1):
    for j in range(i+1):
        print(i, end=' ')
    print()
print()


#5 5 5 5 5 
#4 4 4 4  
#3 3 3  
#2 2  
#1 
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(i, end=' ')  
    print()
print()  

 
#5 4 3 2 1 
#4 3 2 1 
#3 2 1 
#2 1 
#1 
for i in range(4,0,-1):
    for j in range(i,0,-1):
        print(j, end=' ')  
    print()
print()


#1 2 3 4 5 
#1 2 3 4 
#1 2 3 
#1 2 
#1 
for i in range(5,1,-1):
    for j in range(2,i+1):#1,1+1
        print(j, end=' ')  
    print()
print() 
  
#1 2 3 4 5
#2 3 4 5
#3 4 5
#4 5
#5 
for i in range(1,6):
    for j in range(1,6):
        print(j, end=' ')
    print()    
print()

#1 2 3 4 5
#6 7 8 9
#10 11 12
#12 13
#14


A = 33
B = 98
C = 55
print("Value of A before swapping is: ", A)
print("Value of B before swapping is: ", B)
print("Value of C before swapping is: ", C)
C=A
A=B
B=C

print("Value of A after swapping is: ", A)
print("Value of B after swapping is: ", B)
print("Value of C before swapping is: ", C)




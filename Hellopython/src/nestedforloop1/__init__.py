for i in range(10,0,-1):
    for j in range(i):
        print(i,end='')
    print()


for i in range(10,0,-1):
    print(i,end='')
print()


str="Python"
reversed_str=""
for i in range(1, len(str)+1):
    reversed_str += str[-i]
print(reversed_str)


my_str='harshitha'
my_char='a'
count=0
for i in my_str:
    if i == my_char:
       count += 1
print(count)


str=input("Enter a string:")
count=0
for s in str:
    count=count+1
print("Length of the entered string is:", count)

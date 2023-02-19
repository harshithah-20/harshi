def my_function(fname,sno):
  print(fname)
  print(sno)
my_function("Emil",1)
my_function("Tobias",2)
my_function("Linus",4)


def education_details(college,noofstudents):
    print(college)
    print(noofstudents)
education_details("ATME",80)
education_details("JCE",180)
education_details("NIE",150)

def arithmetic_operation(operations,signs):
    print(operations)
    print(signs)
arithmetic_operation("add",10+26)
arithmetic_operation("sub",58-18)
arithmetic_operation("multiply",32*41)
arithmetic_operation("divide",30/8)
arithmetic_operation("modulus",80%20)

def subject_marks(sname,smarks):
  print(sname)
  print(smarks)
subject_marks("Kannada",80)
subject_marks("English",63)
subject_marks("Maths",38)
subject_marks("Science",52)
subject_marks("Social",75)

def typesof_numbers(type,number):
    print(type)
    print(number)
typesof_numbers("Even Number",20)
typesof_numbers("Odd Number", 15)
typesof_numbers("Prime Number",9)
typesof_numbers("Negative Number",-28)
typesof_numbers("Positive Number",40)


#For loop
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

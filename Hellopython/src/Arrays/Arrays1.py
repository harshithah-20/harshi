import array as arr
a = arr.array('i', [2, 4, 6, 8])

print("First element:", a[0])
print("Second element:", a[1])
print("Last element:", a[-1])


import array as arr
numbers_list = [2,5,62,5,42,52,48,5]
numbers_array = arr.array('i', numbers_list)

print(numbers_array[2:5]) #3rd to 4th
print(numbers_array[:-5]) #beginning to 4th
print(numbers_array[5:])  #6th to end
print(numbers_array[:])  #beginning to end


import array as arr
numbers = arr.array('i', [10, 11, 12, 14, 13])
numbers.remove(12)
print(numbers)   # Output: array('i', [10, 11, 12, 13])
print(numbers.pop(2))   # Output: 12
print(numbers)   # Output: array('i', [10, 11, 13])


class Employee:    
    id = 10   
    name = "John"    
    def display (self):    
        print("ID: %d \nName: %s"%(self.id,self.name))    
# Creating a emp instance of Employee class  
emp = Employee()    
emp.display()

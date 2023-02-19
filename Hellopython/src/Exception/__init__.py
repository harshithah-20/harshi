try:
   fh = open("testfile", "r")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
   

try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
   
   
def this_fails():
    x = 1/0
try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)
  
    
a = [1, 2, 3]
try: 
    print ("Second element = %d" %(a[1]))
  
    # Throws error since there are only 3 elements in array
    print ("Fourth element = %d" %(a[2]))
  
except:
    print ("An error occurred")


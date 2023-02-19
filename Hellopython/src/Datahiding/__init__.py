class JustCounter:
   __secretCount = 0
  
   def count(self):
      self.__secretCount += 1
      print (self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()


class Solution:
    __privateCounter = 0
 
    def sum(self):
        self.__privateCounter += 1
        print(self.__privateCounter)
 
 
count = Solution()
count.sum()
count.sum()
 
# Here it will show error because it unable
# to access private member
#print(count.__privateCount)



class Solution1:
    __privateCounter = 0
 
    def sum(self):
        self.__privateCounter += 1
        print(self.__privateCounter)
 
 
count = Solution()
count.sum()
count.sum()
 
# Here we have accessed the private data
# member through class name.
print(count._Solution__privateCounter)


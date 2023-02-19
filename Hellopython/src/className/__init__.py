'''Create a class to print a integer and a character with two methods having the same name but 
different sequence of the integer and the character parameters. For example, 
if the parameter of the first method are of the form (int n, char c), then that of the 
second method will be of the form (char c, int n).'''


class Name:
    def samename(self,num,ch):
        self.num=num
        self.ch=ch
        print("Number and character are=",self.num,self.ch)
    def samename(self,ch,num):
        self.ch=ch
        self.num=num
        print("Number and character are=",self.ch,self.num)
N1=Name()
N1.samename(20,"son")
N1.samename("son",20)
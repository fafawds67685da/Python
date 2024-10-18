class abc:
    def ex(self):  
        print("YES")

class abc2(abc):
    def call_ex(self):  
        self.ex()  

obj = abc2()
obj.call_ex()  

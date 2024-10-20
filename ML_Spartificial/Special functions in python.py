class even:
    def __init__ (self,max):
        self.max=max
        self.data=[i*2 for i in range (max+1)]


    def __getitem__(self,index):
        if index < len(self.data):
            return self.data[index]
        else:
            raise IndexError("Index Out of Range")
        

    def __len__ (self):
        return len(self.data)
    

evenno = even(10)
print(evenno[10])

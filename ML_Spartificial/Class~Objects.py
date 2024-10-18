class Rocket:
    def __init__(self,x,y,name,color):
        self.x=x
        self.y=y
        self.name=name
        self.color=color

def move_up(self):
    self.y+=1

abc =Rocket(100,0,"DEv","red")
move_up(abc)
print(abc.x,abc.y,abc.name,abc.color)

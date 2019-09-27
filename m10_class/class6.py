#方法與DRY原則
class Circle:
    pi=3.14
    def __init__(self,radius=1):
        self.radius=radius
    def area(self):
        return self.radius*self.radius*Circle.pi
    def setRadius(self,radius):
        self.radius=radius
    def getRadius(self):
        return self.radius
    
c=Circle()
c.setRadius(2)
print(c.getRadius())
print(c.area())
print("------")

#DRY:Don't Repeat Yourself
#同樣動作應放置於function中
#同樣function應放置於class中
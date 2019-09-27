class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return 'x={0},y={1}'.format(self.x,self.y)
    def __add__(self, other): #物件不能與物件相加，需重載運算子
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)
p1=Point(5,6)
p2=Point(7,8)
print(p1+p2)
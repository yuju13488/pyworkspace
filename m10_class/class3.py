#類別的兩種使用方式
#類別與實體方法（封裝在實體物件中的函式）
class Point:#定自初始化函式
    def __init__(self,x,y): #定義實體屬性
        self.x=x
        self.y=y
    #定義實體方法（函式）
    def show(self): #方法名稱，更多自訂參數
        print(self.x,self.y) #方法主體，透過self操作實體物件
    def distance(self,z,w):
        return ((self.x-z)**2+(self.y-w)**2)**0.5
p=Point(3,4)
#呼叫實體方法（函式）：實體物件.實體方法名稱(參數資料)
p.show() #呼叫函式show及其所屬的print（類別.函式）
d=p.distance(0,0) #z,w
print(d)
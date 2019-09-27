#實體物件設計：包裝檔案讀取的程式
class File:
    #初始化函式
    def __init__(self,name):
        self.name=name
        self.file=None #檔案物件：尚未開啟檔案，初期為None
    #實體方法
    def open(self): #實體方法1：調用python內建語法
        self.file=open(self.name,mode="r",encoding="utf-8") #python內建開啟檔案的語法：回傳檔案物件
    def read(self): #實體方法2：讀取並回傳
        return self.file.read() #檔案物件.read：讀取檔案
#讀取第一個檔案
f1=File("data4.txt") #建立檔案的實體物件
f1.open() #呼叫實體方法1：開啟
data=f1.read() #呼叫實體方法2：讀取
print(data)
#讀取第二個檔案
f2=File("data5.txt")
f2.open()
data=f2.read()
print(data)
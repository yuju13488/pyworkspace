#1類別+類別屬性
#2類別與實體物件+實體屬性（封裝在實體物件中的變數）+實體方法（封裝在實體物件中的函式）

#先定義類別→後使用屬性
#類別屬性：儲存物件的資訊，封裝變數或函式
#類別方法：操作物件的資訊，也就是函式
#定義類別+類別屬性
class IO: #類別名稱
    supportedSrcs=["consloe","file"] #屬性1：定義變數
    def read(src): #屬性2：定義函式
        if src not in IO.supportedSrcs: #src為自訂參數
            print("Not Supported")
        else:    
            print("Read from",src)
#使用：類別名稱.屬性（函式）名稱
print(IO.supportedSrcs)
IO.read("file") #呼叫屬性read的函式
IO.read("haha")
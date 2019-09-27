#id()檢視"擬"記憶體空間
n1=0
n2=0 #當變數指定給另一變數，會指定到相同記憶體空間
print(id(n1))
print(id(n2))
print("--------------------")
a1=10
a2=a1
print(id(a1))
print(id(a2))
print("--------------------")
a1=20
print(id(a1))
a2=30
print(id(a2)) #更新記憶體空間，已不在先前的id(a2)

#可變物件，資料改變時直接將所在記憶體位置改值：list、set、dict
    #id()不變但數值改變
#不可變物件，資料改變時將資料複製到新的記憶體位置：int、float、str、tuple
    #數值改變，id()也改變

#尋找關鍵字
import keyword
print(keyword.kwlist)

#慣用命名方式：
    #單字間用_表示
    #外部變數用第二單字開頭大寫表示
    #類別用開頭全大寫表示
    #常數已全大寫表示（ex:PI=3.14159......）
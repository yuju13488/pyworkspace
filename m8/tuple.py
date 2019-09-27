#有順序不可變動列表 Tuple
t_test1=(1,) # (1)為int
t_test2=(1,2,) #tuple
print(type(t_test1),type(t_test2))
t=(1,2,"like",3) #tuple(list)內放list也是tuple
#data[1]=4 錯誤，不可變動（不可新增）
print(tuple([1,2,3])) #(1,2,3)
a=t.index("like") #取用資料所在位置
b=t.count("like") #計算資料出現次數
print(a)
print(b)
print("--------------------")

x,y=1,2
z=x,y #tuple
print("--------------------")

#一般交換a,b
#c=a 讓a值存進c
#a=b 讓b值存進a
#b=c 讓c=a值存進b
a,b=b,a #tuple交換
print(a)
print(b)
print("--------------------")

print(tuple('yoyo')) #將字串中每個字母分開變成一組tuple
tuple1=(1,2,3,4)
tuple2=tuple1+(5,) #tuple的加法為tuple與tuple串接，單一數值仍須有()及,
tuple3=tuple2+(6,7)
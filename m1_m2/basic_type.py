#布林值（大寫）
x=True #大寫且True=1,False=0
y=(5 > 4)+4 #y=1+4=5
print(y)
print("--------------------")

#複數（var.real,var.imag）
z=3+2.7j
print(z.real,z.imag)
print("--------------------")

#印出單引號，以雙引號外括但裡面不能有雙引號
print("I 'am' Yoyo")
#以\讓單引號功能失效可印出
print("I \'am Yoyo")
#印出雙引號，以單引號外括但裡面不能有單引號
print('I "am" Yoyo')
print("--------------------")

#type()檢視物件屬性
print(type(x))
print(type(y))
print("--------------------")

#資料轉換
w=123.45
print(int(w)) #將浮點數w強制轉為整數（無條件捨去）
s='789'
print(int(s)) #將字串轉為整數，若字串內不是數字為error
p='123'+str(456)
print(p) #需轉成相同屬性才能相加（串接）
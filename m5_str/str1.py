str1='Python'
print('Py' in str1)
print('py' in str1) #分大小寫
for i in str1:
    print(i,end='/')
print()
print("--------------------")

#擷取字串：左往右從0算起，右往左從-1算起。str[start:end-1]
print(str1[0],str1[1],str1[2],str1[3],str1[4],str1[5],)
print(str1[1:4]) #yth
print(str1[-4:]) #thon
print(str1[:-2]) #Pyth 刪掉最後兩個，並非從-2位置開始
print("--------------------")
len(str1) #字串長度
max(str1) #最大字元值
min(str1) #最小字元值
print(str1+str1)
print(str1*5)
#不重複無序列
set() #空集合
s1={3,4,5}
print(3 in s1) #判斷是否存在
print(10 not in s1)
s2={4,5,6,7}
print(s1&s2) #交集
print(s1.union((s2)))
print(s1|s2) #聯集
print(s1.intersection((s2)))
print(s1-s2) #差集：減去重疊部分
print(s1.difference((s2)))
print(s1^s2) #反交集：取不重疊部分
print(s1.symmetric_difference((s2)))
print("--------------------")

s=set("word") #set(字串)
print(s)
print("--------------------")

print(set([1,2,4,6,5,4])) #list轉set自動替除重複數值
print(set((1,2,4,6,5,4))) #tuple轉set自動替除重複數值
set3={1,2,3,4,5}
set3.add(10) # 一次僅能加一個
set3.remove(1) #刪除
print("--------------------")

set4={3,4,5}
print(set3.issubset(set3)) #檢視子集合
print(set3.issuperset(set4)) #檢視母集合
print(set3 == set4)
print(set3 != set4)
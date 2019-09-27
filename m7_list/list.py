#有順序可變動列表 List
student=[12,60,15,70,92]
print(student[2])
student[0]=55
print(student)
print(student[1:4]) #不含第4
student[1:4]=[] #連續刪除
print(student)
student=student+[12,33] #串接
print(student)
print(len(student)) #長度
data=[[1,2,3],[4,5,6,7]]
print(data[0][1])
print(data[0][0:2]) #不含第2
data[1][1:3]=[8,9]
print(data)
print("----------")

a=[5,6,7,8]
a.pop() #[5,6,7]刪除最尾
print(a)
a.append(2) #[5,6,7,2]在最尾新增
print(a)
a.sort() #[2,5,6,7]由小到大排列
print(a)
a.reverse() #[7,6,5,2]反排列
print(a)
print("----------")

print(list("hello yoyo")) #將字串變成list
print("f" in list("hello"))

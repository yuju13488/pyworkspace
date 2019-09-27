list1=[[97,64,27],[92,15,55]] #2列x3行list
print(list1[0][1]) #64
print(list1[1][2]) #55
print(len(list1)) #列數
print(len(list1[0])) #第一列行數

for i in range(len(list1)): #2列數0~1
    for j in range(len(list1[i])): #3行數0~2
        print(list1[i][j],end=' ')
    print() #分行
print('------------------------------')

row=0
print(len(list1[row]))
for k in range(len(list1[row])): #取出第一列的每個值
    print(list1[row][k], end=' ')
print()

col=1
print(len(list1))
for l in range(len(list1)): #取出每一列第二行的值
    print(list1[l][col], end=' ')
print()
print('------------------------------')

#隨機二維陣列
import random
row,col=eval(input('input row and column:'))
list2=[] #加入二維list
for i in range(row):
    list2.append([]) #加入一維list
    for j in range(col):
        list2[i].append(random.randint(1,100))
print(list2)
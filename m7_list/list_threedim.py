list1=[[[97,64,27],[92,15,55]],[[97,64,27],[92,15,55]],[[97,64,27],[92,15,55]]] #2列x3行list
print(list1)

for i in range(len(list1)): #2列數0~1
    for j in range(len(list1[i])): #3行數0~2
        for k in range(len(list1[i][j])):
            print(list1[i][j][k],end=' ')
        print() #分行
    print()
print('------------------------------')

sum=0
for i in range(len(list1)): #2列數0~1
    for j in range(len(list1[i])): #3行數0~2
        for k in range(len(list1[i][j])):
            sum+=list1[i][j][k]
print(sum)
print('------------------------------')

import random
layer,row,col=eval(input('input layer, row and column:'))
list2=[] #加入三維list
for i in range(layer):
    list2.append=[] #加入二維list
    for j in range(row):
        list2[i].append([])
        for k in range(col):
            list2[i][j].append(random.randint(1,100))
print(list2)
# list1=['yoyo','eva','haha','fun']
# print(len(list1)) #4
# for i in range(len(list1)): #list[0]~list[3]
#     print(list1[i])
#for val in list1:
#   print(val)

list2=[11,22,33,44,55]
print(sum(list2))
def listsum(list_x):
    sum=0 #需宣告在def內
    for i in range(len(list_x)):
        sum+=list_x[i]
    return sum
print(listsum(list2))
print('----------------------------------')

list3=[11,22,33,44,55]
print(max(list3))
def listmax(list_y):
    max=list_y[0]
    for j in range(len(list_y)):
        if list_y[j] > max:
            max=list_y[j]
        else:
            max=max
    return max
print(listmax(list3))
print('----------------------------------')

print(min(list3))
def listmin(list_z):
    min=list_z[0]
    for k in range(len(list_z)):
        if list_z[k] < min:
            min=list_z[k]
        else:
            min=min
    return min
print(listmin(list3))

import random #通常寫在module的開頭
list3=[]
for i in range(6): #0~5
    list3.append(random.randint(1,100)) #隨機從1~100中取出6個值
print(list3)
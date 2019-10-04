# 1.	一維串列的練習-max_min
# 事先將10個數字置於串列中，分別找出10個數字中最大的值和最小的值。
# (勿使用現成的函數)
import random
list1=[]
for i in range(10):
    list1.append(random.randint(1,100)) #隨機從1~100中取出6個值
print(list1)

def listmax(list_y):
    max=list_y[0]
    for j in range(len(list_y)):
        if list_y[j] > max:
            max=list_y[j]
        else:
            max=max
    return max
print(listmax(list1))
print('----------------------------------')

def listmin(list_z):
    min=list_z[0]
    for k in range(len(list_z)):
        if list_z[k] < min:
            min=list_z[k]
        else:
            min=min
    return min
print(listmin(list1))
#指定陣列
#串列a執行b=a，當a被修改時，b也會跟著修改
a=[1,2,3]
import copy
b=copy.deepcopy(a) #禁止複製修改
print(a)
print(b)
a[1]=10
print(a)
print(b)
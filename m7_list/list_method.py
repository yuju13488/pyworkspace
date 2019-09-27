list1=[75,86,51,86,86,62,93,86,49]
list1.append(66) #在最後加上數值66
print(list1)
list1.insert(1,22) #在位置1加上數值22
print(list1)
print(list1.pop()) #取得並刪除最後數值
print(list1.pop(1)) #取得並刪除index數值
list1.remove(86) #刪除數值，若有多個則刪除第一個
print(list1)
print(list1.index(93)) #取得該值索引值
print(list1.count(86)) #取得該值個數
list2=list1.copy() #複製list
list1.sort() #由小排到大
print(list1)
list1.reverse() #反轉；無回傳值，無法放在return或命令一個陣列=list.reverse
print(list1)
print(list2)
#sort()→reverse() 由大排到小
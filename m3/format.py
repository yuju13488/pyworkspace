#formar：[*][<^>][+-][#][0][寬度][,][.][type]
print('%s is %d years old' % ('Yoyo',31))
print('{1} is {0} years old' . format(31,'Yoyo')) #位置
print('{} is {} years old' . format('Yoyo',30))
print('{name} is {age} years old' . format(age=30,name='Yoyo')) #命名
print('{0} is {age} years old' . format('Yoyo',age=30))
print("--------------------")

print('{0:d} {1:.2f} {2:s}' . format(123,45.678,'Yoyo'))
print('{} {:.2f} {}' . format(123,45.678,'Yoyo')) #位置可省略但":"不行
s1='Welcome to my world.'
print(s1.startswith('Welcome'))
print(s1.startswith('welcome'))
print(s1.endswith('World.'))
print(s1.endswith('world.'))
s2='pyhton.py'
print(s2.endswith('.py')) #尋找副檔名
print("--------------------")

s3='Its my python, my book and my pen.'
print(s3.find('my')) #參數字串中最小索引值（第一個參數的第一個索引位置）
print(s3[s3.find('my')])
index=s3.find('my')
print(s3.find('my',index+1)) #尋找第2個參數索引值
print(s3[s3.find('my',index+1)])
print(s3.rfind('my')) #參數字串中最大索引值（最後一個參數的第一個索引位置）
print(s3[s3.rfind('my')])
print(s3.count('my')) #計算個數
print("--------------------")

print('hello World'.capitalize()) #將第一個字元大寫，其餘小寫
print('Hello World'.lower()) #將全部轉小寫
print('Hello World'.upper()) #將全部轉大寫
print('HellO WorLd'.title()) #將每一單字的第一個字元大寫，其餘小寫
print('Hello World'.swapcase()) #大小寫互換
print('Hello World'.replace('Hello','Hi')) #將前字元以後字元取代
print("--------------------")

print('   yoyo   '.lstrip()) #刪除字串左側空白字元
print('   yoyo   '.rstrip()) #刪除字串右側空白字元
print('   yoyo   '.strip()) #刪除字串兩側空白字元
print('yoyo'.center(8)) #在參數的寬度下置中
print('yoyo'.ljust(8)) #在參數的寬度下靠左
print('yoyo'.rjust(8)) #在參數的寬度下靠右
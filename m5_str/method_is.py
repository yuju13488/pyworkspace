s1='yoyo'
s2='0413'
s3='yoyo0413'
print(s1.isalnum()) #判斷是否由字串或數字組成
print(s2.isalnum())
print(s3.isalnum())
print(s1.isalpha()) #判斷是否由純字串組成
print(s2.isalpha())
print(s3.isalpha())
print(s1.isdigit()) #判斷是否由純數字組成
print(s2.isdigit())
print(s3.isdigit())
print("--------------------")

#判斷識別字（須為字母、數字、底線，不可數字開頭，需區分大小寫，不限長度）
print(s1.isidentifier(),s2.isidentifier(),s3.isidentifier(),sep='\n')
print("--------------------")

print('yoyo'.islower()) #需全部小寫為Ture
print('Yoyo'.islower())
print('YOYO'.isupper()) #需全部大寫為Ture
print('Yoyo'.isupper())
print("--------------------")

#空白字元：空白、換行、跳格
print(' '.isspace())
print('\n'.isspace())
print('\t'.isspace())
print('\\'.isspace())
print("--------------------")
#運算子
print(2**10) #次方
print(str(123)+'Yoyo') #數字需化為字串方能串接
print("--------------------")
#讓b*(a//b)+a%b=a
print(-17//4) #整除//
print(-17%4) #餘數往負無窮（-20）取值（結果僅正數3）
print("--------------------")

#指定運算子
x=1;y=2
x*=y+2 #x=x*(y+2)
print(x)
print("--------------------")

#身分運算子is、is not：判斷兩變數是否指向同一記憶體位置
a=0;b=a
print(id(a),'\n',id(b),'\n',a is b)
print("--------------------")

#成員運算子

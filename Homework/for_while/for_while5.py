# 5.	迴圈的練習-prime
# 輸入一正整數，找出所有小於或等於的質數。
n=eval(input('請輸入一正整數：'))
for i in range(2,n):
    for j in range(2,i):
        if i % j == 0:
            break #找到i任意因數跳出小迴圈
    else: #for的else，當for停止時執行
        print(i)
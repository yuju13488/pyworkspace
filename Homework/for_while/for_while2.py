# 2.	迴圏的練習-factor
# 輸入一正整數，求其所有的因數。
# 說明：36的因數為1, 2, 3, 4, 6, 9, 12, 18, 36。
f=eval(input('請輸入一整數：'))
for i in range(1,f+1):
    if f % i == 0 :
        print(i,end='\t')
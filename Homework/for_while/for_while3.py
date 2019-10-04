# 3.	迴圏的練習-perfect_number
# 一個數字若等於其所有因數的總和，則此數為perfect number。
# 找出100以內所有的完美數。
# 說明：6的因數為1, 2, 3，6=1+2+3，故6為完美數。
for i in range(1,101):
    sum = 0 #sum需命名在使用的迴圈上
    for j in range(1,i):
        if i % j == 0:
            sum=sum+j
        else :
            sum=sum
    if i == sum:
        print(i)
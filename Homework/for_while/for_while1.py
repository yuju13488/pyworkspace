# 1.	迴圏的練習-expression
# 利用for迴圏計算1^2-2^2+3^2-4^2+…+49^2-50^2的值。
sum=0
for i in range(1,51):
    if i%2 == 0:
        i=(-1)*i*i
    elif i%2 != 0:
        i=i*i
    sum=sum+i
print(sum)
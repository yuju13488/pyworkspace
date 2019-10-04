# 4.	迴圏的練習-amstrong
# Amstrong數是指一個三位數的整數，其各位數之立方和等於該數本身。
# 找出所有的Amstrong數。
# 說明：153=1^3+5^3+3^3，故153為Amstrong數。
sum = 0
for i in range(99,1000):
    if (i//100)**3+((i%100)//10)**3+(i%10)**3 == i:
        print(i)
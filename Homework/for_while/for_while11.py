# 11.	迴圈敘述的練習-interest
# 錢精打以10%單利投資100000元，郝細算則以5%複利投資100000元。計算多少年後郝細算的投資可以超過錢精打，並將此時兩人錢數印出。(27年後)
# 提示：單利公式：P(1+r*n)    複利公式：P(1+r)^n
# P：本金，r：利率，n：多少年

P=100000
r1=0.1
r2=0.05
n=1
while True:
    n+=1
    if P*(1+r2)**n > P*(1+r1*n):
        print(n)
        break
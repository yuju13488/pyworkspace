# 7.	迴圏的練習-rabbit
# 老王養了一群兔子，若三隻三隻一數，剩餘一隻；若五隻五隻一數，剩餘三隻；若七隻七隻一數，剩餘二隻。試問兔子最少有幾隻。
i=0
while True: #無限迴圈
    if i%3==1 and i%5==3 and i%7==2:
        break #當符合條件則break跳出迴圈
    i += 1
print(i) #印出跳出時的結果
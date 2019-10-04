#2.選擇性敘述的練習-salary
#輸入便利商店工讀生的工作時數，並計算其薪資。
#60小時以內，時薪120元。
#61~80小時，以時薪1.25倍計算。
#81小時以上，以時薪1.5倍計算。
#說明：薪資以累計方式計算。若工時為90小時，則薪資為60*120 + 20*120*1.25 + 10*120*1.5元。

hours=eval(input("Please input hours for working:"))
if hours <= 60:
    print('salary=',hours*120)
elif 61 <= hours <= 80:
    print('salary=',120*(60+(hours-60)*1.25))
elif hours >= 81:
    print(120*('salary=',60+20*1.25+(hours-80)*1.5))
else :
    print('錯誤')
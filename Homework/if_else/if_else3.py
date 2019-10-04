#3.選擇性敘述的練習-electricity
#輸入何種用電和度數，計算出需繳之電費。
#電力公司使用累計方式來計算電費，分工業用電及家庭用電。
#                 	   家庭用電        工業用電
#240度(含)以下			0.15元			0.45元
#240~540(含)度   		0.25元			0.45元
#540度以上        	    0.45元			0.45元

elect=input('What kind of electricity, \'home\' or \'industry\':')
kwh=eval(input('Please input kilowatt hour for uesd:'))

if elect == 'industry':
    print('Electricity fee is',kwh*0.45)
elif elect == 'home':
    if kwh <= 240:
        print('Electricity fee is', kwh*0.15)
    elif 240 < kwh <= 540:
        print('Electricity fee is', 240*0.15+(kwh-240)*0.25)
    elif 540 < kwh:
        print('Electricity fee is', 240*0.15+300*0.25+(kwh-540)*0.45)
else:
    print('輸入錯誤')

# if kwh <= 240 and elect == 'home':
#     print('Electricity fee is',kwh*0.15)
# if kwh <= 240 and elect == 'industry':
#     print('Electricity fee is',kwh*0.45)
# if 240 < kwh <= 540 and elect == 'home':
#     print('Electricity fee is',240*0.15+(kwh-240)*0.25)
# if 240 < kwh <= 540 and elect == 'industry':
#     print('Electricity fee is',kwh*0.45)
# if 540 < kwh and elect == 'home':
#     print('Electricity fee is',240*0.15+300*0.25+(kwh-540)*0.45)
# if 540 < kwh and elect == 'industry':
#     print('Electricity fee is',kwh*0.45)
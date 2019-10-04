# 5.選擇性敘述的練習-refund
# 輸入在某商店購物應付金額與實付金額。
# 實付金額小於應付金額，則印出”金額不足”。
# 實付金額等於應付金額，則印出”不必找錢”。
# 實付金額大於應付金額，則輸出找回金額最少的鈔票數和錢幣數。
# 假設幣值只有1000, 500, 100元紙鈔和50, 10, 5, 1元硬幣。
# 說明：若買了132元的商品，付1000元，應找回一張500元，三張100元，一個50元硬幣，一個10元硬幣，一個5元硬幣和三個1元硬幣。

price=eval(input('應付金額:'))
pay=eval(input('實付金額:'))
change=pay-price
if change < 0:
    print('金額不足')
elif change == 0:
    print('不必找錢')
elif change > 0:
    if change >= 1000:
        print('應找',(change//1000),'張1000元',(change%1000)//500,'張500元',(change%500)//100,'張100元',
        (change%100)//50,'個50元',(change%50)//10,'個10元',(change%10)//5,'個5元',change%5,'個1元',sep='')
    elif 1000 > change >= 500:
        print('應找',(change%1000)//500,'張500元',(change%500)//100,'張100元',
        (change%100)//50,'個50元',(change%50)//10,'個10元',(change%10)//5,'個5元',change%5,'個1元',sep='')
    elif 500 > change >= 100:
        print('應找',(change%500)//100,'張100元',(change%100)//50,'個50元',(change%50)//10,'個10元',
              (change%10)//5,'個5元',change%5,'個1元',sep='')
    elif 100 > change >= 50:
        print('應找',(change%100)//50,'個50元', (change%50)//10,'個10元',(change%10)//5,'個5元',change%5,'個1元',sep='')
    elif 50 > change >= 10:
        print('應找',(change%50)//10,'個10元',(change%10)//5,'個5元',change%5,'個1元',sep='')
    elif 10 > change >= 5:
        print('應找',(change%10)//5,'個5元',change%5,'個1元',sep='')
    elif 5 > change >= 1:
        print('應找',(change%10)//5,'個5元',change%5,'個1元',sep='')
    elif change < 5:
        print('應找',change%5,'個1元',sep='')
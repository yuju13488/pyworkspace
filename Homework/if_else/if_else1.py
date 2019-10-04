#1.選擇性敘述的練習-season
#輸入月份1~12月，判斷相對應的季節春、夏、秋、冬並印出。若不在此範圍則印出”輸入錯誤”。

month=eval(input('Please input any month:'))
if month in (3,4,5):
    print('春')
elif month in (6,7,8):
    print('夏')
elif month in (9,10,11):
    print('秋')
elif month in (12,1,2):
    print('冬')
else:
    print('輸入錯誤')
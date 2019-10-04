# INSERT INTO food VALUES ('CK001', '曲奇餅乾', '2021/01/10', 'TL', 250, '點心');
# INSERT INTO food VALUES ('CK002', '蘇打餅乾', '2020/10/12', 'TW', 80, '點心');
# INSERT INTO food VALUES ('DK001', '高山茶', '2021/05/23', 'TW', 780, '飲料');
# INSERT INTO food VALUES ('DK002', '綠茶', '2020/06/11', 'JP', 530, '飲料');
# INSERT INTO food VALUES ('OL001', '苦茶油', '2022/03/16', 'TW', 360, '調味品');
# INSERT INTO food VALUES ('OL002', '橄欖油', '2021/07/25', 'TL', 420, '調味品');
# INSERT INTO food VALUES ('CK003', '仙貝', '2020/11/01', 'JP', 270, '點心');
# INSERT INTO food VALUES ('SG001', '醬油', '2022/05/05', 'JP', 260, '調味品');
# INSERT INTO food VALUES ('OL003', '葡萄子油', '2022/05/05', 'JP', 550, '調味品');
# INSERT INTO food VALUES ('CK004', '鳳梨酥', '2020/10/12', 'TW', 340, '點心');
# INSERT INTO food VALUES ('CK005', '太陽餅', '2020/08/27', 'TW', 150, '點心');
# INSERT INTO food VALUES ('DK003', '紅茶', '2022/11/12', 'TL', 260, '飲料');
# INSERT INTO food VALUES ('SG002', '醋', '2021/09/18', 'TW', 60, '調味品');
import mysql.connector
cursor=None #宣告全域變數，None為物件初始值
conn=None

try:
    with open('food.txt', 'r', encoding='utf-8') as f:
        line = f.readline()
        list_emp = []  # 二維list
        while line != '':  # 讀到空字串即停止
            list_line = (repr(line[:-1]).replace("'", '')).split(',')  # 將輸出的字串單引號去除並加入list中
            tuple_line = tuple(list_line) #因指令executemany需加入一list的tuple，先將list轉為tuple
            list_emp.append(tuple_line)  # 依照一列一列tuple加入成為二維list
            line = f.readline()
    conn = mysql.connector.connect(database = 'db02', user = 'root', password = 'ilave300')
    cursor=conn.cursor()
    ins="INSERT INTO food VALUES (%s,%s,%s,%s,%s,%s)" #database中有欄位數同%s個數

    cursor.executemany(ins,list_emp) #list_emp=[(),(),(),......]
    conn.commit() #需自動結束交易才會將資料存進database

    query = "SELECT name,expiredate,price,catalog FROM food"
    cursor.execute(query)
    for name,expiredate,price,catalog in cursor:
        print('name={0},expiredate={1},price={2},catalog={3}'.format(name,expiredate,price,catalog))
    print('total', cursor.rowcount, 'food')
except mysql.connector.Error as err:
    if err.errno == 1049: #自行測試錯誤代碼
        print("database doesn't exist")
    elif err.errno == 1045:
        print('user name or password is wrong')
    else:
        print(err) #debug使用
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
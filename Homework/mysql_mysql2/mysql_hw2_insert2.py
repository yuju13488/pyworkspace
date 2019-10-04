# INSERT INTO place VALUES ('TW', '台灣');
# INSERT INTO place VALUES ('JP', '日本');
# INSERT INTO place VALUES ('TL', '泰國');
# INSERT INTO place VALUES ('US', '美國');
import mysql.connector
cursor=None #宣告全域變數，None為物件初始值
conn=None

try:
    with open('place.txt', 'r', encoding='utf-8') as f:
        line = f.readline()
        list_emp = []  # 二維list
        while line != '':  # 讀到空字串即停止
            list_line = (repr(line[:-1]).replace("'", '')).split(',')  # 將輸出的字串單引號去除並加入list中
            tuple_line = tuple(list_line) #因指令executemany需加入一list的tuple，先將list轉為tuple
            list_emp.append(tuple_line)  # 依照一列一列tuple加入成為二維list
            line = f.readline()
    conn = mysql.connector.connect(database = 'db02', user = 'root', password = 'ilave300')
    cursor=conn.cursor()
    ins="INSERT INTO place VALUES (%s,%s)" #database中有欄位數同%s個數

    cursor.executemany(ins,list_emp) #list_emp=[(),(),(),......]
    conn.commit() #需自動結束交易才會將資料存進database

    query = "SELECT * FROM place"
    cursor.execute(query)
    for placeid,name in cursor:
        print('placeid={0},name={1}'.format(placeid,name))
    print('total', cursor.rowcount, 'place')
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
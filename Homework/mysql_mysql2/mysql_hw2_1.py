# 1.查詢所有食物表格中所有欄位的資料
# 2.查詢所有食物名稱、到期日和價格
# 3.查詢所有食物名稱、到期日和價格，並將表頭重新命為'名稱'、'到期日'和'價格'
# 4.查詢所有食物的種類有哪些？(重覆的資料只顯示一次)
# 5.查詢所有食物名稱和種類，並串接成一個字串，中間以空白隔開，並將表頭重新命為'Food name & catalog'
import mysql.connector
cursor=None #宣告全域變數，None為物件初始值
conn=None

try:
    conn = mysql.connector.connect(database='db02', user='root', password='ilave300')
    cursor = conn.cursor()
    query = "SELECT concat(`name`, ' ', catalog) AS 'Food name & catalog' FROM food; "
    cursor.execute(query)
    for catalog in cursor:
        print(catalog)
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
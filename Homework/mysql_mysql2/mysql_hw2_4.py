# 1.	查詢所有食物表格中所有欄位的資料
# 2.	查詢所有食物名稱、到期日和價格
# 3.	查詢所有食物名稱、到期日和價格，並將表頭重新命為'名稱'、'到期日'和'價格'
# 4.	查詢所有食物的種類有哪些？(重覆的資料只顯示一次)
# 5.	查詢所有食物名稱和種類，並串接成一個字串，中間以空白隔開，並將表頭重新命為'Food name & catalog'
# --- WHERE子句
# 6.	查詢所有食物價格超過400的食物名稱和價格
# 7.	查詢所有食物價格介於250~530之間的食物名稱和價格
# 8.	查詢所有食物價格不介於250~530之間的食物名稱和價格
# 9.	查詢所有食物種類為'點心'的食物名稱和價格
# 10.	查詢所有食物種類為'點心'和'飲料'的食物名稱、價格和種類
# 11.	查詢所有食物產地為'TW'和'JP'的食物名稱和價格
# 12.	查詢所有食物名稱有'油'字的食物名稱、到期日和價格
# 13.	查詢所有食物到期日在今年底以前到期的食物名稱和價格
# 14.	查詢所有食物到期日在明年6月底以前到期的食物名稱和價格
# 15.	查詢所有食物6個月內到期的食物名稱和價格
# --- ORDER BY子句
# 16.	查詢所有食物名稱、到期日和價格，並以價格做降冪排序
# 17.	查詢前三個價格最高的食物名稱、到期日和價格，並以價格做降冪排序
# 18.	查詢種類為'點心'且價格低於等於250的食物名稱和價格，並以價格做升冪排序
# 19.	顯示所有食物名稱、價格和增加5%且四捨五入為整數後的價格，新價格並將表頭命名為'New Price'
# 20.	接續上題，再增加一個表頭命名為'Increase'，顯示New price減去price的值
# 21.	顯示所有食物名稱、價格和整數後的價格，新價格並將表頭命名為'New Price'；按價格分250以下、251~500和501以上三種分別增加8%,5%和3%且價格無條件捨去成整數
# 22.	查詢所有食物名稱、種類、距離今天尚有幾天到期(正數表示)或已過期幾天(負數表示)和註記(有'已過期'或'未過期'兩種)，並將後兩者表頭分別命名為'Days of expired'和'expired or not'
# 23.	接續上題，並以過期天數做升冪排序
# --- GROUP BY & HAVING子句
# 24.	查詢所有食物最高、最低、加總和平均價格，表頭分別命名為'Max'、'Min'、'Sum'和'Avg'，結果皆以四捨五入的整數來顯示
# 25.	接續上題，查詢每個種類
# 26.	接續上題，查詢每個種類且平均價格超過300，並以平均價格做降冪排序
# 27.	顯示查詢每個種類的食物數量
# 28.	查詢不同產地和每個種類的食物數量
import mysql.connector
cursor=None #宣告全域變數，None為物件初始值
conn=None

try:
    conn = mysql.connector.connect(database='db02', user='root', password='ilave300')
    cursor = conn.cursor()
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
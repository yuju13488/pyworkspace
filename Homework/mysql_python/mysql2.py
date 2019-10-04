# 2.	檔案的練習-add_emp
# 在emp.txt文字檔中設定五筆employee的資料，將之新增至資料庫中。
# 註1：一筆資料一列，每個資料欄的資料以逗號(,)隔開
# 註2：建議使用cursor.executemany(sql, seq_of_params)來實作
# 	一次insert多筆資料
import mysql.connector
cursor=None #宣告全域變數，None為物件初始值
conn=None

try:
    with open('emp.txt', 'r', encoding='utf-8') as f:
        line = f.readline()
        list_emp = []  # 二維list
        while line != '':  # 讀到空字串即停止
            list_line = (repr(line[:-1]).replace("'", '')).split(',')  # 將輸出的字串單引號去除並加入list中
            tuple_line = tuple(list_line) #因指令executemany需加入一list的tuple，先將list轉為tuple
            list_emp.append(tuple_line)  # 依照一列一列tuple加入成為二維list
            line = f.readline()
    conn = mysql.connector.connect(database = 'db01', user = 'root', password = 'ilave300')
    cursor=conn.cursor()
    ins="INSERT INTO employee VALUES (%s,%s,%s,%s,%s,%s)" #database中有欄位數同%s個數

    cursor.executemany(ins,list_emp) #list_emp=[(),(),(),......]
    conn.commit() #需自動結束交易才會將資料存進database

    query = "SELECT ename,hiredate,salary FROM employee"
    cursor.execute(query)
    for ename, hiredate, salary in cursor:
        print('name={0},hiredate={1},salary={2}'.format(ename, hiredate, salary))
    print('total', cursor.rowcount, 'employee')
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
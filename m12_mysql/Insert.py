import mysql.connector
cursor=None #宣告全域變數，None為物件初始值
conn=None
try:
    conn = mysql.connector.connect(database = 'db01', user = 'root', password = 'ilave300')
    cursor=conn.cursor() #從conn傳給cursor
    ins="INSERT INTO employee VALUES (%s,%s,%s,%s,%s,%s)" #database中有欄位數同%s個數
    ins_data=(1009,'Yoyo','2019/07/25',80000,100,'engineer')
    cursor.execute(ins,ins_data)
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
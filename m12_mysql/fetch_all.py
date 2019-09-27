#fetch one輸出為一list內有tuple
import mysql.connector
cursor=None #宣告全域變數，None為物件初始值
conn=None
try:
    conn = mysql.connector.connect(database = 'db01', user = 'root', password = 'ilave300')
    cursor=conn.cursor() #從conn傳給cursor
    query="SELECT ename,hiredate,salary FROM employee" #SQL指令為一字串
    cursor.execute(query) #執行SQL指令
    emps=cursor.fetchall()
    print(emps)

    for emp in emps:
        print('name={0},hiredate={1},salary={2}'.format(emp[0],emp[1],emp[2]))
    print('total',cursor.rowcount,'employee')
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
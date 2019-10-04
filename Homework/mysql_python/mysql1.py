# 1.	檔案的練習-dump_emp
# 將employee表格裡的所有資料dump至檔案中。
# 註：一筆資料一列，每個資料欄的資料以逗號(,)隔開
import mysql.connector
cursor=None
conn=None
try:
    conn = mysql.connector.connect(database = 'db01', user = 'root', password = 'ilave300')
    cursor=conn.cursor() #從conn傳給cursor
    query = "SELECT * FROM employee"
    cursor.execute(query)
    for empno, ename, hiredate, salary, deptno, title in cursor:
        with open('emp.csv', 'a', encoding='utf-8') as f:
            f.write('{},{},{},{},{},{}\n'.format(empno, ename, hiredate, salary, deptno, title))
            #非print需\n空行
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
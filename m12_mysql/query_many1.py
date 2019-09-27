import mysql.connector
cursor=None #宣告全域變數，None為物件初始值
conn=None
try:
    conn = mysql.connector.connect(database = 'db01', user = 'root', password = 'ilave300')
    cursor=conn.cursor() #從conn傳給cursor
    query="SELECT ename,hiredate,salary FROM employee WHERE deptno=%s AND title=%s" #動態找資料，固定為%s
    deptno=100
    title='engineer'
    cursor.execute(query,(deptno,title)) #tuple內順序需與query內SQL的%s指令順序相同

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
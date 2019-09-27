import mysql.connector
try:
    conn = mysql.connector.connect(database = 'db01', user = 'root', password = 'ilave300')
except mysql.connector.Error as err:
    if err.errno == 1049: #自行測試錯誤代碼
        print("database doesn't exist")
    elif err.errno == 1045:
        print('user name or password is wrong')
    else:
        print(err) #debug使用
finally:
    if conn: #若連線存在
        print('close')
        conn.close()

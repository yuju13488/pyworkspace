import mysql.connector
conn = mysql.connector.connect(database = 'db01', user = 'root', password = 'ilave300')
conn.close()

from mysql.connector import connection
conn = connection.MySQLConnection(database = 'db01', user = 'root', password = 'ilave300')
conn.close()

import mysql.connector
config={
    'database':'db01',
    'user':'root',
    'password':'ilave300'
}
conn=mysql.connector.connect(**config) #代入字典
conn.close()
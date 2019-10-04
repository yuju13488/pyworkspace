# 3.	檔案和集合的練習-employee_file
# 改寫employee作業，將hard code在程式裡的資料，改由檔案輸入。
# 提示：
# a.	import employee
# b.	每一列資料代表一個員工所有的資料
# c.	檔案裡的每一列資料沒有特定順序
# d.	在檔案裡可增加一個職位別來表示不同的職位
# e.	使用split()將字串切成tokens
# 用split將data轉為list，再代入class
from class_hw.class_file import Normal #from package.module imoort class
from class_hw.class_file import Two_level
from class_hw.class_file import One_level

with open('employee.csv', 'r', encoding='utf-8') as f:
    line = f.readline()
    list_emp=[] #二維list
    while line != '':  # 讀到空字串即停止
        list_line=(repr(line[:-1]).replace("'",'')).split(',') #將輸出的字串單引號去除並加入list中
        list_emp.append(list_line) #依照一列一列list加入成為二維list
        line = f.readline()
for i in range(len(list_emp)):
    name=None #定義str變數
    gender=None
    hiredate=None
    telno=None
    address=None
    job=None
    for j in range(len(list_emp[i])):
        if list_emp[i][j].find('name')==0: #若字串中有name
            name=list_emp[i][j].replace('name:','') #讓str變數name成為字串name:XXX中的XXX
        elif list_emp[i][j].find('gender')==0:
            gender=list_emp[i][j].replace('gender:', '')
        elif list_emp[i][j].find('hiredate')==0:
            hiredate=list_emp[i][j].replace('hiredate:', '')
        elif list_emp[i][j].find('telno')==0:
            telno=list_emp[i][j].replace('telno:', '')
        elif list_emp[i][j].find('address')==0:
            address=list_emp[i][j].replace('address:', '')
        elif list_emp[i][j].find('job')==0:
            job=list_emp[i][j].replace('job:', '')

#依照職位不同給予不同函數及加班時數
    if job.find('N') == 0:
        normal = Normal(name, gender, hiredate, telno, address)
        if job.find('1') == 3:
            print('{0},{1}'.format(normal,normal.Pay()))
        elif job.find('2') == 3:
            print('{0},{1}'.format(normal, normal.Pay(overtime=10)))
    elif job.find('S') == 0:
        two = Two_level(name, gender, hiredate, telno, address)
        if job.find('1') == 3:
            print('{0},{1}'.format(two, two.Pay()))
        elif job.find('2') == 3:
            print('{0},{1}'.format(two, two.Pay(overtime=10)))
    elif job.find('M') == 0:
        one = One_level(name, gender, hiredate, telno, address)
        if job.find('1') == 3:
            print('{0},{1}'.format(one, one.Pay()))
        elif job.find('2') == 3:
            print('{0},{1}'.format(one, one.Pay(overtime=10)))
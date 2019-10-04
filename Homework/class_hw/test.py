from class_hw.class_file import Normal #from package.module imoort class
from class_hw.class_file import Two_level
from class_hw.class_file import One_level

with open('employee.csv', 'r', encoding='utf-8') as f:
    line = f.readline()  # 利用\n判斷是否換行讀取，會讀取入\n並印出
    list_emp=[]
    while line != '':  # 讀到空字串即停止
        list_line=(repr(line[:-1]).replace("'",'')).split(',')
        list_emp.append(list_line) #將每列最後一個'\n'以[:-1]消除；字串中','以'\n'取代
        line = f.readline()
    for i in range(len(list_emp)):
        if list_emp[i][6]=='N001':
            normal=Normal(list_emp[i][0].replace('name:',''),list_emp[i][1].replace('gender:',''),
                          list_emp[i][2].replace('hiredate:',''),list_emp[i][3].replace('telno:',''),
                          list_emp[i][4].replace('address:',''))
            print(normal)
        if list_emp[i][6]=='N002':
            normal=Normal(list_emp[i][0].replace('name:',''),list_emp[i][1].replace('gender:',''),
                          list_emp[i][2].replace('hiredate:',''),list_emp[i][3].replace('telno:',''),
                          list_emp[i][4].replace('address:',''))
            normal.Pay(10)
            print(normal)
        if list_emp[i][6]=='S001':
            supervisor=Two_level(list_emp[i][0].replace('name:',''),list_emp[i][1].replace('gender:',''),
                          list_emp[i][2].replace('hiredate:',''),list_emp[i][3].replace('telno:',''),
                          list_emp[i][4].replace('address:',''))
            print(supervisor)
        if list_emp[i][6]=='S002':
            supervisor=Two_level(list_emp[i][0].replace('name:',''),list_emp[i][1].replace('gender:',''),
                          list_emp[i][2].replace('hiredate:',''),list_emp[i][3].replace('telno:',''),
                          list_emp[i][4].replace('address:',''))
            supervisor.Pay(10)
            print(supervisor)
        if list_emp[i][6]=='M001':
            manger=One_level(list_emp[i][0].replace('name:',''),list_emp[i][1].replace('gender:',''),
                          list_emp[i][2].replace('hiredate:',''),list_emp[i][3].replace('telno:',''),
                          list_emp[i][4].replace('address:',''))
            print(manger)
        if list_emp[i][6]=='M002':
            manger=One_level(list_emp[i][0].replace('name:',''),list_emp[i][1].replace('gender:',''),
                          list_emp[i][2].replace('hiredate:',''),list_emp[i][3].replace('telno:',''),
                          list_emp[i][4].replace('address:',''))
            manger.Pay(10)
            print(manger)
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

normal1=Normal(name='Yoyo', gender='Male', hiredate='2019-07-20', telno='123', address='Taitung')
emp1=str(normal1)
normal2=Normal(name='Eva', gender='Female', hiredate='2019-07-20', telno='456', address='Taichung')
emp2=str(normal2)

supervisor1=Two_level(name='Apple', gender='Female', hiredate='2015-07-22', telno='789', address='Taipei')
emp3=str(supervisor1)
supervisor2=Two_level(name='Becca', gender='Female', hiredate='2016-07-22', telno='357', address='New Taipei')
emp4=str(supervisor2)

manger1=One_level(name='Dina', gender='Female', hiredate='2013-07-22', telno='159', address='Koren')
emp5=str(manger1)
manger2=One_level(name='Eason', gender='Male', hiredate='2011-07-22', telno='826', address='Kaohsiung')
emp6=str(manger2)

with open('employee.csv','w',encoding='utf-8') as f: #'w'若不存在將會創建新檔案，或將已有檔案完全覆寫
    f.write(emp1)
    f.write(',job:N001\n')
    f.write(emp2)
    f.write(',job:N002\n')
    f.write(emp3)
    f.write(',job:S001\n')
    f.write(emp4)
    f.write(',job:S002\n')
    f.write(emp5)
    f.write(',job:M001\n')
    f.write(emp6)
    f.write(',job:M002\n')

with open('employee.csv', 'r', encoding='utf-8') as f:
    line = f.readline()
    while line != '':  # 讀到空字串即停止
        print(repr(line[:-1]).replace(',','\n',)) #將每列最後一個'\n'以[:-1]消除；字串中','以'\n'取代
        line = f.readline()
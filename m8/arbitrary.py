def greet(*names):
    for name in names:
        print('Hello,',name)
tuple1=('Yoyo','Eva','Tom','Kevin')
greet(*tuple1)
greet(*'Yoyo')

def stu(**data):
    for key,value in data.items():
        print('{} is {}'.format(key,value))
dict1={'name':'Yoyo','age':'31','email':'shiy@123'}
stu(**dict1)
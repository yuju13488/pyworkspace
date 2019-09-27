#*arg：0~n個
def greet(*names):
    for name in names:
        print('Hello,',name)
greet('Yoyo','Eva','Tom','Kevin')

#**keyword args：key/value
def stu(**data):
    for key,value in data.items(): #字典M8
        print('{} is {}'.format(key,value))
stu(name='Yoyo',age='31',email='shiy@123')
        
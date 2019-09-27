def msg(name,age):
    print('{0} is {1} years od.'.format(name,age))
msg('Yoyo',31)
msg(age=31,name='Yoyo')
msg(name='Yoyo',age=31)
msg('Yoyo',age=31)
#msg(name='Yoyo',31) compile error
#msg(31,name='Yoyo') compile error
try:
    n1,n2 = eval(input('n1,n2:'))
    print('{} / {} = {}'.format(n1,n2,float(n1/n2)))  # n%2=1為True，n%2=0為Flase
except ZeroDivisionError:
    print('Division by zero')
except SyntaxError:
    print('Comma missing')
except:
    print('Error')
else:
    print('No expect')
finally:
    print('Must be done')
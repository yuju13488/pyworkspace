#條件（三元）運算子
x,y=eval(input('input two numbers:'))
z=x if x>y else y #x>y z=x;x,y z=y
print(z)

score=int(input('imput number:'))
s='pass' if score>=60 else 'fail'
print(s)
# n=int(input('n:'))
# print('{} is {}'.format(n,'odd' if n%2 else 'even')) #n%2=1為True，n%2=0為Flase
try:
    n=int(input('n:'))
    print('{} is {}'.format(n,'odd' if n%2 else 'even')) #n%2=1為True，n%2=0為Flase
except ValueError as e:
    print(e) #print(ValueError) is different

try:
    n=int(input('n:'))
    print('{} is {}'.format(n,'odd' if n%2 else 'even')) #n%2=1為True，n%2=0為Flase
except ValueError as e:
    print('Please input a positive integer:')

try:
    n=int(input('n between 0 to 100:'))
    if n<0 or n>100:
        raise ValueError
    else:
        print('score is:',n)
except ValueError:
    print('Please input a number between 0 to 100')
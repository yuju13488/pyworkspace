from random import randint

target = randint(0, 100)
while 1:
    guess = input('plz guess a interger between 0 and 100:')
    try:
        num = int(guess)
    except:
        print('plz input an INTERGER!!')
    else:
        break
time = 1
while num != target:
    if num < target:
        print('smaller')
    elif num > target:
        print('bigger')
    while 1:
        guess = input('guess again...')
        try:
            num = int(guess)
        except:
            print('plz input an INTERGER!!')
        else:
            break
    time = time + 1
else:
    print('you win...you get the number in ', time, ' steps!!')
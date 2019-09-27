class Account: #主程式
    pass
def deposit(acc,amount): #method1(local variable)
    try:
        if amount <= 0:
            raise  ValueError
        acc.balance += amount
    except ValueError:
        print('Must ba a positive integer')

def withdraw(acc,amount): #method2(local variable)
    try:
        if amount <= acc.balance:
            acc.balance -= amount
        else:
            raise ValueError
    except ValueError:
        print('Not enough balance')

def main(): #測試程式
    account=Account() #方法才有()
    account.balance=0 #屬性沒有()
    account.name='Yoyo'
    account.number='22'

    print(account.name)
    print(account.number)

    amount=int(input('輸入存款金額:'))
    deposit(account,amount)
    print(account.balance)
    amount = int(input('輸入提款金額:'))
    withdraw(account, amount)
    print(account.balance)
main()
#同JAVA
class Account: #主程式
    def __init__(self,number,name,balance=0): #self=object；number, name, balance=local variable ; balance=0 default
        self.number=number #屬性=參數
        self.name=name #屬性=參數
        self.balance=balance #屬性=參數；固定不須命名為local variable

    def deposit(self,amount): #method1(local variable)
        try:
            if amount <= 0:
                raise  ValueError
            self.balance += amount
        except ValueError:
            print('Must ba a positive integer')

    def withdraw(self,amount): #method2(local variable)
        try:
            if amount <= self.balance:
                self.balance -= amount
            else:
                raise ValueError
        except ValueError:
            print('Not enough balance')

def main(): #測試程式
    acc=Account('22','Yoyo',10000) #可不給參數balance預設為0
    print(acc.name)
    print(acc.number)
    print(acc.balance)

    amount=int(input('輸入存款金額:'))
    acc.deposit(amount)
    print(acc.balance)
    amount = int(input('輸入提款金額:'))
    acc.withdraw(amount)
    print(acc.balance)
main()
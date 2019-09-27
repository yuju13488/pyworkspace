#同JAVA
class Account: #主程式
    def __init__(self,number,name): #self=object；number, name=local variable
        self.number=number #屬性=參數
        self.name=name #屬性=參數
        self.balance=0 #屬性=參數；固定不須命名為local variable

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
    acc=Account('22','Yoyo') #方法才有()
    print(acc.name)
    print(acc.number)

    amount=int(input('輸入存款金額:'))
    acc.deposit(amount)
    print(acc.balance)
    amount = int(input('輸入提款金額:'))
    acc.withdraw(amount)
    print(acc.balance)
main()
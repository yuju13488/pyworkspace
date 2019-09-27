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

    def __str__(self):
        return ('number:{0}\nname:{1}\nbalance:{2}'.format(self.number,self.name,self.balance))
from m10_class.method__str__ import Account #from package.module imoort class

class CheckingAccount(Account):
    def __init__(self, number, name,balance):  # self=object；number, name, balance=local variable
        # self.number = number  # 屬性=參數
        # self.name = name  # 屬性=參數
        # self.balance = balance
        super(CheckingAccount,self).__init__(number,name,balance) #super(childclass,self).__init__()，.後為parentclass的init及參數
        self.credit_limit=10000

    def withdraw(self, amount):  # method2(local variable)
        try:
            if amount <= self.balance+self.credit_limit: #overriding
                self.balance -= amount
            else:
                raise ValueError
        except ValueError:
            print('Not enough credit limit')

    def __str__(self): #overriding
        return (super(CheckingAccount,self).__str__()+'\ncredit limit:{0}'.format(self.credit_limit)) #super(childclass,self).__str__()，.後為parentclass的init及參數
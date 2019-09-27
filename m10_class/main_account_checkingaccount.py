from m10_class.reuse_checkingAccount import CheckingAccount #from package.module imoort class
from m10_class.method__str__ import Account

def main(): #測試程式
    acc=Account('22','Yoyo',10000) #可不給參數balance預設為0
    print(acc) #需有def __str__才能印出所需結果

    ca = CheckingAccount('112233', 'Marry', 10000)
    ca.deposit(5000)
    ca.withdraw(20000)
    print(ca)
main()
# 1.	類別繼承的練習-employee
# 有一小公司，其人事薪資的制度如下：
# 公司每個員工皆有姓名、性別、到職日、電話和住址等基本資料。
# 一般職員只有本薪；一級主管則另有本薪、午餐津貼、交通津貼和職務加給；二級主管則有本薪、午餐津貼和職務加給。午餐津貼為1800元，交通津貼為2000元，職務加給一級主管為5000元，二級主管為3000元。
# 每個員工皆有可能加班，加班費為本薪除以240乘以1.5倍再乘以加班時數。
# 在main()中產生六個實例分別為一級主管、二級主管及一般職員且分有加班及無加班兩種(資料直接透過建構子hard code在程式中)，並列印其基本資料及當月薪資。
    # 1.	以一般職員為父類別，主管類別繼承
    # 2.	製造一抽象類別只有基本資料，其餘類別繼承
#同JAVA

# 哪些是放在建構子中的實體屬性？
#     RDB中放在表格內資料為屬性
#     RDB中透過指令運算為方法
# 實體屬性需要__str__方可印出，方法中的參數只需要在方法中回傳
# 若父類別中方法定義回傳，子類別同樣利用super(子類別參數)。呼叫時代入參數取得父類別回傳值，再代入子類別方法進行運算。
class Emp:
    def __init__(self,name,gender,hiredate,telno,address):
        self.name=name
        self.gender=gender
        self.hiredate=hiredate
        self.telno=telno
        self.address=address
    def __str__(self):
        return ('name:{0}\ngender:{1}\nhiredate:{2}\ntelno:{3}\naddress:{4}'.format(self.name,self.gender,self.hiredate,self.telno,self.address))
class Normal(Emp):
    def __init__(self,name,gender,hiredate,telno,address): #當前類別屬性
        super(Normal, self).__init__(name,gender,hiredate,telno,address) #父類別屬性
    def Pay(self,pay=36000,overtime=0): #預設本薪為36000，加班時數為0
        salary=pay+(pay/240)*1.5*overtime
        return salary
class Two_level(Normal):
    def __init__(self,name,gender,hiredate,telno,address):
        super(Two_level,self).__init__(name,gender,hiredate,telno,address)
        self.lunch = 1800 #屬性為數值不須在init宣告
        self.manage = 3000
    def Pay(self,pay=36000,overtime=0): #預設本薪為36000，加班時數為0
        salary=super(Two_level,self).Pay(pay,overtime)+self.lunch+self.manage
        return salary
class One_level(Normal):
    def __init__(self,name,gender,hiredate,telno,address):
        super(One_level,self).__init__(name,gender,hiredate,telno,address)
        self.lunch = 1800
        self.traffic=2000
        self.manage = 5000
    def Pay(self,pay=36000,overtime=0): #預設本薪為36000，加班時數為0
        salary=super(One_level,self).Pay(pay,overtime)+self.lunch+self.manage+self.traffic
        return salary

def main():
    normal = Normal(name='Yoyo',gender='Male',hiredate='2019-07-20',telno='123456789',address='Taitung')
    print('{0}\nsalary:{1}'.format(normal,normal.Pay())) #不給加班預設為0
    print('')
    print('{0}\nsalary:{1}'.format(normal,normal.Pay(overtime=10)))
    print('--------------------')
    two = Two_level(name='Eva', gender='Female', hiredate='2019-07-22', telno='987654321', address='Taichung')
    print('{0}\nsalary:{1}'.format(two,two.Pay()))
    print('')
    print('{0}\nsalary:{1}'.format(two,two.Pay(overtime=10)))
    print('--------------------')
    one = One_level(name='Eva', gender='Female', hiredate='2019-07-22', telno='987654321', address='Taichung')
    print('{0}\nsalary:{1}'.format(one,one.Pay()))
    print('')
    print('{0}\nsalary:{1}'.format(one,one.Pay(overtime=10)))
main()
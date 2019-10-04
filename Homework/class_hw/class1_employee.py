#By Jimmy
class Employee(object):
    def __init__(self, name, gender, date, phone, address):
        self.name = name
        self.gender = gender
        self.date = date
        self.phone = phone
        self.address = address


class EmpNormal(Employee):
    def __init__(self, name, gender, date, phone, address, salary):
        super(EmpNormal, self).__init__(name, gender, date, phone, address)
        self.salary = salary

    def total(self, overtime):
        otpay = round((self.salary / 240) * overtime * 1.5, 2)
        total = self.salary + otpay
        # return 'name: {}\ndate: {}\novertime: {}\novertime pay: {}\ntotal: {}'.\
        #     format(self.name, self.date, overtime, otpay, total)
        return total

    def __str__(self):
        return 'name: {}\ngender: {}\ndata: {}\nphone: {}\naddress: {}\nsalary: {}'.\
            format(self.name, self.gender, self.date, self.phone, self.address, self.salary)


class EmpSecond(EmpNormal):
    def __init__(self, name, gender, date, phone, address, salary):
        super(EmpSecond, self).__init__(name, gender, date, phone, address, salary)
        self.lunch = 1800
        self.manage = 3000

    def total(self, overtime): #當sub metho收到數值時先super到main method取得return值，再傳回sub method運算
        total = super(EmpSecond, self).total(overtime) + self.manage + self.lunch
        return total

    def __str__(self):
        return 'name: {}\ngender: {}\ndata: {}\nphone: {}\naddress: {}\nsalary: {}'.\
            format(self.name, self.gender, self.date, self.phone, self.address, self.salary)


class EmpFirst(EmpSecond):
    def __init__(self, name, gender, date, phone, address, salary):
        super(EmpFirst, self).__init__(name, gender, date, phone, address, salary)
        self.traffic = 2000
        self.manage = 5000

    def total(self, overtime):
        total = super(EmpFirst, self).total(overtime) + self.traffic
        return total

    def __str__(self):
        return 'name: {}\ngender: {}\ndata: {}\nphone: {}\naddress: {}\nsalary: {}'.\
            format(self.name, self.gender, self.date, self.phone, self.address, self.salary)

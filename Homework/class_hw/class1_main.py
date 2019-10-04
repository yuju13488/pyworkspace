#By Jimmy
# from hw6.stack import Stack
from hw6.employee import EmpNormal
from hw6.employee import EmpSecond
from hw6.employee import EmpFirst


def output(name, overtime=0):
    print(name)
    print('total: ', name.total(overtime))
    print('-------------------------')


def main():
    # list1 = Stack()
    # list1.push(20)
    # list1.push(40)
    # list1.push(60)
    # list1.pop()
    jimmy = EmpNormal('Jimmy', 'M', '2019-5-7', '0912345678', 'taiwan', 24000)
    bella = EmpSecond('bella', 'F', '2019-9-30', '0987654321', 'hongkong', 50000)
    jacky = EmpFirst('jacky', 'M', '2019-11-14', '0978945612', 'USA', 80000)
    output(jimmy, 20)
    output(bella, 15)
    output(jacky, 40)
    print()
    output(jimmy)
    output(bella)
    output(jacky)


main()

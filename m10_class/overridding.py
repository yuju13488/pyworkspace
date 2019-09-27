class Parent:
    def m1(selfs):
        print('Parent:m1()')
    def m2(selfs):
        print('Parent:m2()')
class Child1(Parent):
    def m3(self):
        print('Child1:m3()')
    def m2(self):
        print('Child1:m2()') #覆寫、改寫父類別的方法
class Child2(Parent):
    def m4(self):
        print('Child2:m4()')

def main():
    child1=Child1()
    child1.m1()
    child1.m2() #Child1:m2()
    child1.m3()
    child2=Child2()
    child2.m1()
    child2.m2() #Parent:m2()
    child2.m4()
main()
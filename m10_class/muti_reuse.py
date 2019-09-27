class A(object):
    def m1(self):
        print('A.m1')
    def m2(self):
        print('A.m2')
class B(A):
    def m3(self):
        print('B.m3')
class C(A):
    def m2(self):
        print('C.m2')
    def m3(self):
        print('C.m3')
class D(B,C): #從左找起，找到有欲呼叫function即使用不再往右找
    def m4(self):
        print('D.m4')
d=D()
d.m4() #D
d.m3() #D->B
d.m2() #D->B->C
d.m1() #D->B->C->A
x=10
y=11
def main():
    x=20
    print(x) #區域變數不等於外部變數
    print(y) #先從def內尋找才往外尋找
main()
print(x)
print(y)
print("--------------------")

a=10 #global
def outer():
    a=20
    def inner():
        a=30
        print(a) #local inner a=30
    inner()
    print(a) #local outer a=20
outer()
print(a) #global a=10
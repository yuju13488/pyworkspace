#nonlocal下的參數值為上一層的local argument，而nonlocal下的宣告將改變上一層的local argument
x=10
y=11
def main():
    x=20
    print(x) #20
    global  y #將下面y宣告為global，不能使用nonlocal尋找global
    y=22
    print(y) #22
main()
print(x) #10
print(y) #22
print('------------------')

def outer():
    x=20
    def inner():
        nonlocal x #由內到外尋找，不含global
        print(x) #20
        x=30 #因nonlocal將上一層宣告為x=30（同語法global效果）
    inner()
    print(x) #x=30
outer()
print(x) #10
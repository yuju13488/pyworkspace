def func():
    x=10
    def get_x(): #取x=10
        return x
    def set_x(n): #存(n)
        nonlocal x
        print(x) #nonlocal下的參數值為上一層的local argument x=10
        x=n #nonlocal下的宣告將改變上一層的local argument x=n
    return  get_x,set_x
getX,setX=func() #func()傳出值為兩函式
print(getX()) #10
setX(20) #此時x=n=20
print(getX()) #20

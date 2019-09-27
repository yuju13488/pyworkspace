def func():
    x=10
    def get_x(): #取x=10
        return x
    def set_x(n): #存(n)
        x=n
    return  get_x,set_x
getX,setX=func() #func()傳出值為兩函式
print(getX()) #10
setX(20)
print(getX()) #10

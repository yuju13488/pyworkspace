#1.函數的練習-sigma
#寫一函數my_fun (x, n)如下：
#sigama((x**k)/k!)

def my_fun(x,n):
    sum=1 #乘法起始為1
    sigma=0 #加法起始為0
    for k in range(1,n+1):
        sum*=k #分母
        sigma+=x**k/sum #(分子/分母) 加總
    return sigma

def main():
    x,n=eval(input('input two values:'))
    print(my_fun(x,n))
main()
# 2.函數的練習-is_prime
# 寫一函數is_prime(n)用來判斷n是否為質數。
def is_prime(n):
    p=0
    for i in range(2,n):
        if n%i == 0:
            p+=1 #當n有因數時i+1，若一直無因數則保持p=0
    return p #回傳p值
def main():
    n = eval(input('Please input a positive integer:'))
    if is_prime(n) > 0 :
        print('n is not a prime')
    elif is_prime(n) <= 0 :
        print('n is a prime')
main()
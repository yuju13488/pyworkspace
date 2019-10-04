# 3.	函數的練習-prime
# 寫一函數get_prime (n)用來找出第n個質數。

def get_prime(n):
    m=0
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break  # 找到i任意因數跳出小迴圈
        else:  # for的else，當for停止時執行
            m+=1
            print('第{}個質數為{}'.format(m,i))
def main():
    n = eval(input('Please input a positive integer:'))
    get_prime(n)
main()
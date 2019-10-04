# 4.	函數的練習-mersenne_prime
# 寫一函數is_mersenne_prime(n)用來判斷n是否為Mersenne質數。撰寫一程式找出前5個Mersenne質數。
# 提示：若質數滿足2**P-1=n (p為正整數)，則n為Mersenne Prime。
# 說明：當p=3時，2**3-1=7，故7為Mersenne Prime。
import math
def is_prime(n): #判斷質數
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    else:
        return True

def is_mersenne_prime(n): #判斷p及2**p-1皆為質數即可
    if is_prime(n) == True: #n為質數
        for p in range(2,n):
            if  is_prime(p) == True and (2**p)-1 == n: #p為質數且符合2**p-1=n
                return True
        else: #為迴圈跑完的回傳值
            return False
    else:
        return False

def main():
    n=eval(input('Please input a positive integer:'))
    if is_mersenne_prime(n) == True:
        print('n is a Mersenne Prime')
    elif is_mersenne_prime(n) == False:
        print('n is not a Mersenne Prime')
main()
print('----------------------------------')

count=0
m=1
while True:
    if is_mersenne_prime(m) == True: #n為梅森質數
        print(m)
        count+=1
        if count == 5: #印出五次後停止迴圈
            break
    m+=1
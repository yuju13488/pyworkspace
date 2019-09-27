def square(x):
    return x*x
def total(x,y):
    return x+y #不同function中的formal argument可與actual argument同名，區域變數不衝突
def main():
    z=square(3)
    print(z)
    print(square(5))
    print(total(5,8))
main() #呼叫後往下繼續執行
print("--------------------")

#factorial
def factorial(num):
    sum=1
    for i in range(1,num+1):
        sum*=i #sum=sum*i，若以i=i*i將改變i的step值
    return sum
def main2():
    num=eval(input("input:")) #不同def中的formal argument可與actual argument同名，區域變數不衝突
    print('{}!={}'.format(num,factorial(num)))
main2()
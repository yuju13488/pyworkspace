#多回傳值
def sum_avg(n1,n2):
    total=0
    for i in range(n1,n2+1):
        total+=i
    avg=total/(n2-n1+1) #n2-n1+i為個數
    return total,avg #return 須對到def下方

def main():
    n1,n2=eval(input('input two numbers:'))
    total,avg=sum_avg(n1,n2)
    print('sum={0},avg={1}'.format(total,avg))
main()
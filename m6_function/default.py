def sum_avg(n1=1,n2=100): #預設值須從後面給起
    total=0
    for i in range(n1,n2+1):
        total+=i
    avg=total/(n2-n1+1) #n2-n1+i為個數
    return total,avg #return 須對到def下方

def main():
    total, avg = sum_avg() #n1=1,n2=100
    print('sum={0},avg={1}'.format(total, avg))
    total, avg = sum_avg(10) #n1=10,n2=100
    print('sum={0},avg={1}'.format(total, avg))
    total, avg = sum_avg(10,200) #n1=10,n2=200
    print('sum={0},avg={1}'.format(total, avg))
main()
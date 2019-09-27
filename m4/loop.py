n=1
sum=0
while n<=10:
    sum+=n
    n+=1
print(sum,n) #n終值為10+1=11
print("--------------------")

total=0
for i in range(1,11): #終值為11-1=10
                      #for i in range(1,11,1)，step為0,1可省略
    total+=i
print(total,i) #i終值為10
print("--------------------")

total=0
for i in range(10,0,-1): #從10加到1
    total+=i
print(total,i) #i終值為1
print("--------------------")

total=0
for i in range(0,11,2): #偶數相加
    total+=i
print(total,i) #i終值為10
print("--------------------")

#雙層迴圈
for i in range(1,10): #外->row
    for j in range(1,10): #內->column
        print('{0}*{1}={2}'.format(i,j,i*j),end='\t') #將end='\n'改為'\t'
    print() #自動換行，若print('\n')則換兩行
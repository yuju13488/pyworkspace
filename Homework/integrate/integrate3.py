# 3.	綜合練習-poker
# 經由亂數發撲克牌(52張)，分為四組列印出來。
#random.sample(color,1) 取後不放回
#random.randint(1,13,size=13) 取後放回
import random
poker=[]
color=['spades','hearts','diamonds','clubs'] #花色
number=['A',2,3,4,5,6,7,8,9,10,'J','Q','K'] #牌號
for i in range(len(color)):
    for j in range(len(number)):
        poker.append([color[i],number[j]])
        #因append一次只能加入一元素，故加入的為一list，poker即為52張所有牌組的二維list
poker1=random.sample(poker,13) #隨機取樣，取後不放回（取出不重複）
for p in poker1:
    poker.remove(p) #從poker中刪除有player的元素
poker2=random.sample(poker,13) #poker剩39組
for p in poker2:
    poker.remove(p)
poker3=random.sample(poker,13) #poker剩26組
for p in poker3:
    poker.remove(p)
poker4=poker #poker剩13組

sum1=sum(poker1,[]) #將二維list轉為一維
player1=[]
for i in range(0,len(sum1),2):
    str=('{0}_{1}'.format(sum1[i],sum1[i+1])) #將花色及號碼合併為一字串並加入list
    player1.append(str)
sum2=sum(poker2,[])
player2=[]
for i in range(0,len(sum2),2):
    str=('{0}_{1}'.format(sum2[i],sum2[i+1]))
    player2.append(str)
sum3=sum(poker3,[])
player3=[]
for i in range(0,len(sum3),2):
    str=('{0}_{1}'.format(sum3[i],sum3[i+1]))
    player3.append(str)
sum4=sum(poker4,[])
player4=[]
for i in range(0,len(sum4),2):
    str=('{0}_{1}'.format(sum4[i],sum4[i+1]))
    player4.append(str)

print('player1:{0}\nplayer2:{1}\nplayer3:{2}\nplayer4:{3}'.format(player1,player2,player3,player4,sep='\n'))

#跳出外層無限迴圈
#需要季資料列出五年該季（1~4）資料（五筆）
#需要月資料列出五年該月（1~12）資料（五筆）
def avg_all(rain):
    sum = 0
    for i in range(len(rain)): #5
        for j in range(len(rain[i])): #4
            for k in range(len(rain[i][j])): #3
                sum += rain[i][j][k]
    avg=round(sum/(len(rain)*len(rain[0])*len(rain[0][0])),2)
    return avg

def avg_year(rain,y):
    sum = 0
    for j in range(len(rain[y])):
        for k in range(len(rain[y][j])):
            sum += rain[y][j][k]
    avg = round(sum / (len(rain[y]) * len(rain[y][0])), 2)
    return avg

def avg_season(rain,s):
    avg_season = []
    for i in range(len(rain)):
        sum = 0
        for j in range(len(rain[i][s])):
            sum += rain[i][s][j]
        avg=round((sum/len(rain[i][s])),2)
        avg_season.append(avg)
    return avg_season

def avg_month(rain,s,m):
    avg_month = []
    for i in range(len(rain)):
        avg = round(rain[i][s][m], 2)
        avg_month.append(avg)
    return avg_month

def control(option,rain):
    while 1:
        if option == 'all':
            return avg_all(rain)
        elif option == 'year':
            while 1:
                y = input('Please input year between 1 and 5:')
                if y.isdigit() and int(y) in (1,2,3,4,5):
                    y=int(y)-1
                    return avg_year(rain,y)
                else:
                    print('Error')
        elif option == 'season':
            while 1:
                s = input('Please input season between 1 and 4:')
                if s.isdigit() and int(s) in (1, 2, 3, 4):
                    s = int(s) - 1
                    return avg_season(rain,s)
                else:
                    print('Error')
        elif option == 'month':
            while 1:
                n = input('Please input month between 1 and 12:')
                if n.isdigit() and int(n) in (1,2,3,4,5,6,7,8,9,10,11,12):
                    s = (int(n)-1)//3
                    m = (int(n)-1)%3
                    return avg_month(rain,s,m)
                else:
                    print('Error')
        else:
            option=input('Please input all,year,season or month:')

def main():
    rain=[[[255.8,163.6,37.3],[59.6,42.0,119.8],[190.3,186.8,321.9],[125.1,64.4,54.4]],
        [[21.8,123.7,182.7],[121.5,135.5,649.7],[206.6,166.2,175.6],[368.6,120.9,66.9]],
        [[256.0,78.9,285.7],[184.4,186.7,429.8],[174.6,141.4,428.5],[137.6,111.6,16.5]],
        [[20.0,90.0,182.0],[87.6,302.8,248.3],[316.8,728.2,309.9],[135.3,22.6,75.7]],
        [[21.8,198.0,147.0],[98.1,634.7,384.4],[222.1,84.0,198.9],[25.5,46.0,86.8]]]
    option=input('Please input all,year,season or month:')
    print(control(option,rain))
main()
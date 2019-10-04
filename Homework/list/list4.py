# 4.	三維串列的練習-rain
# 輸入一字串，字串為”all” 表示計算60個月的總平均降雨量，
    # ”year”、”season”和”month”分別表示計算某年、某季或某月的平均降雨量。
    # 若為後三者，再輸入一個正整數表示那一年、那一季或那一月。
# 說明：5年12個月的降雨量以三維陣列形式事先給好60個浮點數
# 需做誤錯處理：
# a.	輸入除了”all”、”year”、”season”和”month”以外的字串
# b.	若輸入”year”，而正整數輸入1至5以外的數字
# c.	若輸入”season”，而正整數輸入1至4以外的數字
# d.	若輸入”month”，而正整數輸入1至12以外的數字

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
    avg=round(sum/(len(rain[y])*len(rain[y][0])),2)
    return avg

def avg_season(rain,y,s):
    sum = 0
    for k in range(len(rain[y][s])):
        sum += rain[y][s][k]
    avg=round((sum/len(rain[0][0])),2)
    return avg

def avg_month(rain,y,s,m):
    avg = rain[y][s][m]
    return avg

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
                y = input('Please input year between 1 and 5:')
                if y.isdigit() and int(y) in (1, 2, 3, 4, 5):
                    y = int(y) - 1
                    while 1:
                        s = input('Please input season between 1 and 4:')
                        if s.isdigit() and int(s) in (1, 2, 3, 4):
                            s = int(s) - 1
                            return avg_season(rain,y,s)
                        else:
                            print('Error')
                else:
                    print('Error')
        elif option == 'month':
            while 1:
                y = input('Please input year between 1 and 5:')
                if y.isdigit() and int(y) in (1, 2, 3, 4, 5):
                    y = int(y) - 1
                    while 1:
                        s = input('Please input season between 1 and 4:')
                        if s.isdigit() and int(s) in (1, 2, 3, 4):
                            s = int(s) - 1
                            while 1:
                                m = input('Please input month between 1 and 3:')
                                if m.isdigit() and int(m) in (1, 2, 3):
                                    m = int(m) - 1
                                    return avg_month(rain,y,s,m)
                                else:
                                    print('Error')
                        else:
                            print('Error')
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
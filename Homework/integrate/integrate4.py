# 4.	日期的練習-my_calendar
# 輸入一個正整數，列印出那一年的年曆。
# 輸入兩個整數，第一個數字代表那一年，第二個數字代表那一月，列印出那一年那一月的月曆。
# 注意閏年
# import datetime
    # datetime.timedelta(days=n)
    # t = datetime.datetime.now()
    # print(t.year)  # 2018
    # print(t.month)  # 6
    # print(t.day)  # 1
    # print(t.hour)  # 21
    # print(t.minute)  # 34
    # print(t.second)  # 54
# 空字串來隔每月份一開始的空白週期
# 樣式：win 10 年曆
import datetime
def leap(y): #閏年回傳2月天數
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0: #被400整除
                return 29
            else: #被4整除、被100整除，但不被400整除
                return 28
        else: #被4整除但不被100整除
            return 29
    else: #不被4整除
        return 28
def month_calender(y,m): #月曆
    print('{0}年{1}月'.format(y, m)) #印出年、月格式
    weeks=['日','一','二','三','四','五','六']
    for w in weeks: #印出週日至週六
        print(w, end='\t')
    print('')
    week = datetime.datetime(y, m, 1).strftime("%w") #判斷星期幾
    for i in range(int(week)): #week為str
        print(' ', end='\t') #印出當月週空格數
    last_day=0 #處理月天數
    if m == 1 or m == 3 or m == 5 or m == 7 or m ==8 or m ==10 or m ==12:
        last_day+=31
    elif m == 4 or m == 6 or m == 9 or m == 11:
        last_day+=30
    elif m == 2: #閏年天數
        last_day+=leap(y)
    for j in range(1,int(last_day)+1): #印出月曆
        print(j, end='\t')
        week = datetime.datetime(y,m,j).strftime("%w")
        if int(week) == 6: #week為str，當週數為6時換行
            print('')
def my_calendar(ym): #若ym為單一值為int；若ym為複值為tuple
    try:
        if type(ym) == int: #若ym為int，印出第ym年全年月曆
            for i in range(1,13):
                month_calender(ym,i)
                print('')
                print('')
        elif type(ym) == tuple: #若ym為tuple，印出第y年第m月月曆
            y=ym[0]
            m=ym[1]
            month_calender(y,m)
    except ValueError:
        print('Error')
    except NameError:
        print('Error')
def main():
    ym=eval(input('Please input two positive integer of year and month:'))
    my_calendar(ym)
main()
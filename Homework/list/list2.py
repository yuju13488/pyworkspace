# 2.	函數與串列的練習-pass_list
# a~d各小題皆以一函數來處理：為練習串列的參數傳遞，陣列需定義為main()的區域變數，事先將12個數字置於一3 x 4的二維串列中，列印各函數的結果。
# a.	計算所有數字的平均值
# b.	找出12個數字中最大的值
# c.	找出12個數字中最小的值
# d.	計算每組內4個數字的平均值

def list_avg(pass_list):
    sum=0
    for i in range(len(pass_list)):
        for j in range(len(pass_list[i])):
            sum+=pass_list[i][j]
    return  sum/(len(pass_list)*len(pass_list[0]))

def list_max(pass_list):
    max= 0
    for i in range(len(pass_list)):
        for j in range(len(pass_list[i])):
            if pass_list[i][j] > max:
                max = pass_list[i][j]
    return max

def list_min(pass_list):
    min = pass_list[0][0]
    for i in range(len(pass_list)):
        for j in range(len(pass_list[i])):
            if pass_list[i][j] < min:
                min = pass_list[i][j]
    return min

def row_avg(pass_list):
    for i in range(len(pass_list)):
        sum=0
        for j in range(len(pass_list[i])):  # 取出第一列的每個值
            sum+=pass_list[i][j]
        print('d{0}: {1}'.format(i,sum/len(pass_list[i])))

def main():
    pass_list = []
    for i in range(3):
        passlist = [eval(j) for j in input('Please input 4 integer:').split(',')]  #將輸入的字串;list轉為數字list
        pass_list.append(passlist)
    #return 無回傳值不須return可直接印出，在main內的function可直接接受區域變數pass_list
    print('a:',list_avg(pass_list))
    print('b:',list_max(pass_list))
    print('c:',list_min(pass_list))
    row_avg(pass_list)
main()
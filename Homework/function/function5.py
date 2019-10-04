# 1.	函數的練習-convert
# 輸入一整數，寫兩個函數分別為to_binary(n)和to_hexadecimal(n)用來將n轉換成二進制和十六進制的值。(勿使用任何現成的函數)
def to_binary(n):
    list_binary=['0b'] #index[0]為0b
    for i in range(1,n):
        Quotient = n // (2 ** (i-1))
        mod = Quotient % 2
        list_binary.insert(1,mod) #安插於index[1]
        if Quotient <= 1:
            break
    str_binary =  ''.join(str(i) for i in list_binary) #將list中數字轉為字串
    return str_binary
#list_binary.reverse()無回傳值，無法放在return或命令一個陣列=list_binary.reverse()再return

def to_hexadecimal(n):
    list_hexadecimal = ['0x'] #index[0]為0x
    for i in range(1, n):
        Quotient = n // (16 ** (i - 1))
        if Quotient % 16 < 10:
            mod = Quotient % 16 #安插1~9，10以上由下面判斷處理變化成A~F
        if Quotient % 16 == 10:
            mod='A'
        elif Quotient % 16 == 11:
            mod='B'
        elif Quotient % 16 == 12:
            mod='C'
        elif Quotient % 16 == 13:
            mod='D'
        elif Quotient % 16 == 14:
            mod='E'
        elif Quotient % 16 == 15:
            mod='F'
        list_hexadecimal.insert(1, mod) #安插於index[1]
        if Quotient < 16:
            break
    str_hexadecimal = ''.join(str(i) for i in list_hexadecimal)  # 將list中數字轉為字串
    return str_hexadecimal

def main():
    n=eval(input('Please input a positive integer:'))
    print(to_binary(n))
    print(to_hexadecimal(n))
main()
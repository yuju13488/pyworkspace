# 1.	綜合的練習-check_id
# 寫一函數is_id (_id)用來判斷_id是否為正確身份証字號。
# #控制input字數
# 最後一碼為前面數字演算
class NumberError(Exception): #自行創造錯誤代碼
    pass
class LocalError(Exception): #自行創造錯誤代碼
    pass
class GenderError(Exception): #自行創造錯誤代碼
    pass
class CheckError(Exception): #自行創造錯誤代碼
    pass
def checknumber(id): #創造檢查碼當id中的key對應到dict的value輸出value
    dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17,
            'I': 34, 'J': 18, 'K': 19, 'L': 20, 'M': 21, 'N': 22, 'O': 35, 'P': 23, 'Q': 24,
            'R': 25, 'S': 26, 'T': 27, 'U': 28, 'V': 29, 'W': 32, 'X': 30, 'Y': 31, 'Z': 31}
    sum=dict[id[0]]//10+(dict[id[0]]%10)*9+int(id[1])*8+int(id[2])*7+int(id[3])*6+int(id[4])*5+int(id[5])*4+int(id[6])*3+int(id[7])*2+int(id[8])
    checknumber=10-sum%10
    if checknumber==10:
        checknumber=0
    return checknumber

def is_id(id):
    try:
        if len(id) != 10: #當id長度不為10
            raise NumberError
        elif id[0] not in ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'):
            raise LocalError
        elif int(id[1]) != 1 and int(id[1]) != 2 : #不為1且不為2
            raise GenderError
        elif checknumber(id) != int(id[9]): #檢查碼與最後一碼不符
            raise CheckError
    except NumberError:
        print('Please enter 10 numbers.')
    except LocalError:
        print('First number must be A to Z.')
    except GenderError:
        print('The second number must be 1 or 2.')
    except CheckError:
        print('The last number is wong.')
    except ValueError:
        print('The number from second to last one are digital number.')
    else:
        print('This ID number is correct.')
def main():
    id=input('Please enter your ID number:')
    print(is_id(id))
main()
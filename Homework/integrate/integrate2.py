# 2.	綜合的練習-id_generator
# 輸入地區和性別，經由亂數產生一個身份証字號。
import random
def id(city,gender):
    id = []
    for i in range(7): #隨機創造中間7碼
        id.append(random.randint(0,9))

    letter_dict = {'台北市': 'A', '台中市': 'B', '基隆市': 'C', '台南市': 'D', '高雄市': 'E',
                   '新北市': 'F', '宜蘭縣': 'G', '桃園縣': 'H', '嘉義市': 'I', '新竹縣': 'J',
                   '苗栗縣': 'K', '台中縣': 'L', '南投縣': 'M', '彰化縣': 'N', '新竹市': 'O',
                   '雲林縣': 'P', '嘉義縣': 'Q', '台南縣': 'R', '高雄縣': 'S', '屏東縣': 'T',
                   '花蓮縣': 'U', '台東縣': 'V', '金門縣': 'W', '澎湖縣': 'X', '陽明山': 'Y',
                   '連江縣': 'Z'}
    id.insert(0, letter_dict[city]) #在index為0的位置插入key為city對應到的value碼（英文字）

    if gender=='男' or gender=='Male' or gender=='male': #當性別為男在index為1的位置插入1
        id.insert(1,1)
    elif gender=='女' or gender=='Female' or gender=='female': #當性別為男在index為1的位置插入2
        id.insert(1,2)

    number_dict = {'台北市': 10, '台中市': 11, '基隆市': 12, '台南市': 13, '高雄市': 14,
            '新北市': 15,'宜蘭縣': 16, '桃園縣': 17,'嘉義市': 34, '新竹縣': 18,
            '苗栗縣': 19, '台中縣': 20,'南投縣': 21, '彰化縣': 22, '新竹市': 35,
            '雲林縣': 23, '嘉義縣': 24,'台南縣': 25,'高雄縣': 26, '屏東縣': 27,
            '花蓮縣': 28, '台東縣': 29, '金門縣': 32,'澎湖縣': 30, '陽明山': 31,
            '連江縣': 31}
    sum=number_dict[city]//10+(number_dict[city]%10)*9+int(id[1])*8+int(id[2])*7+int(id[3])*6+int(id[4])*5+int(id[5])*4+int(id[6])*3+int(id[7])*2+int(id[8])
    checknumber=10-sum%10
    if checknumber==10:
        checknumber=0
    id.append(checknumber) #在最後一碼插入檢查碼
    return id

def id_check(city, gender):
    try:
        id_list=id(city,gender)
        id_str =''.join(str(i) for i in id_list)
    except KeyError: #當輸入錯誤的城市
        print('Please enter correct city.')
    except IndexError: #當輸入錯誤的性別
        print('Please enter correct gender.')
    else:
        return id_str
def main():
    city=input('Please enter your city:')
    gender=input('Please enter your gender:')
    print(id_check(city,gender))
main()
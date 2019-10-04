# 3.	二維串列的練習-sales
# 某一公司有五種產品A、B、C、D與E，其單價分別為12、16、10、14與15元；而該公司共有三位銷售員，他們在某月份的銷售數量如下所示
#
# 銷售員   產品A    產品B    產品C	   產品D    產品E
# Jean     33	    32	    56  	45	    33
# Tom	   77	    33	    68	    45	    23
# Tina	   43	    55	    43	    67	    65
# 試計算：
# a.	每一個銷售員的銷售總金額
# b.	有最好業績（銷售總金額最多者）的銷售員
# c.	每一項產品的銷售總金額
# d.	銷售總金額最多的產品
def sum_seller(number,price,seller):
    sum_dict = {} #設定一空字典
    for i in range(len(number)):
        sum=0
        for j in range(len(number[i])):  # 取出第一列的每個值
            sum+=number[i][j]*price[j]
        sum_dict[seller[i]]=sum #將keys銷售員及其對應的values銷售總金額加入字典
    return sum_dict

def best_seller(number,price,seller):
    sum=sum_seller(number, price, seller)
    max=0
    for key in sum: #用字典的key取出value比大小
        if sum[key] > max:
            max=sum[key]
    for key in sum: #用最大的value值取出key
        if sum[key] == max:
            return key,max

def sum_product(number,price,product):
    sum_dict = {}
    for i in range(len(number[0])): #0~4
        sum = 0
        for j in range(len(number)): #0~2
            sum += number[j][i]*price[i] #sum=sum(number行*price行)
        sum_dict[product[i]] = sum
    return sum_dict

def best_product(number,price,product):
    sum = sum_product(number, price, product)
    max = 0
    for key in sum:  # 用字典的key取出value比大小
        if sum[key] > max:
            max = sum[key]
    for key in sum:  # 用最大的value值取出key
        if sum[key] == max:
            return key, max

def main():
    product=['產品A','產品B','產品C','產品D','產品E']
    seller=['Jean','Tom','Tina']
    number=[[33,32,56,45,33],[77,33,68,45,23],[43,55,43	,67,65]]
    price=[12,16,10,14,15]
    print('a:', sum_seller(number,price,seller))
    print('b:', best_seller(number,price,seller))
    print('c:', sum_product(number,price,product))
    print('d:', best_product(number,price,product))
main()


# 9.	迴圈敘述的練習-stars
#    畫出下列三種排列的星星圖形。
#
#  (1)  	*         (2)   * * * * *    (3)    *
#        	* *              * * * *           *  *
#       	* * *              * * *          *  *  *
#        	* * * *              * *         *  *  *  *
#        	* * * * *              *        *  *  *  *  *
#(1)
for i in range(1,6,1):
    x='*'
    x=x*i
    print(x)
print('--------------------')
for i in range(0,5):
    for j in range(i+1):
        if i == 4:
            print("* ",end="")
            continue
        if j == 0 or j == i:
            print("* ",end="")
        else:
            print("  ",end="")
    print()

print('--------------------')

#(2)
for i in range(1,6,1):
    x='*'
    x=x*i
    print(x.rjust(5))
print('--------------------')



#(3)
for i in range(1,6,1):
    x='*'
    x=x*i
    print(x.center(5))
print('--------------------')
for i in range(0,5):
    print("  "*(4-i),end="")
    print(" *  "*(i+1))
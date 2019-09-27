#input輸入的資料為字串
x=input('please input x:')
print(x*3) #字串*3
y=int(input('please input y:')) #將字串轉為數字（僅限單一值）
print(y+3)
print("--------------------")

n1,n2=eval(input('please input n1,n2:')) #eval可處理兩個以上數值，但無法處理字串
print(n1/n2)
str1,str2=eval(input('please input str1,str2:')) #輸入字串時須加單（雙）引號
print(str1+str2)
print("--------------------")
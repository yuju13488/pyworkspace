#脫離字元
print("a \n b") #換行
print("a \t b") #空四格（tab）
print("a c\b b") #倒退一格吃掉c
print("\\") #顯示斜線
print(" \' ") #顯示單引號（用雙引號標註）
print(' \" ') #顯示雙引號（用單引號標註）
print(r'python\n123') #以r開頭讓字串內跳脫字元失效
print("--------------------")

#100=0b1100100（二進位）=0o144（八進位）=0x64（十六進位）
x=0b1100100
y=x+0o144
print(y)
A=u'\u0041' #A以ASCII內碼十六進位表示
print(A)
print(u'\u5bb6')
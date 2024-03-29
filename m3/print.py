#print函式：預設每個數值間有一空白字元分隔sep=" "
#print函式：輸出最後一字元有'\n'自動換行end="\n"
print("Yoyo",end="#") #將行尾字元改成"#"
print("a","b","c",sep=",") #將字元分隔改成","
print("--------------------")

#格式化輸出：%浮點數（預設取6位小數+自動四捨五入）、%s字串
a=123
b=12345.678
c='yoyo'
print(1,'%d' % a) #十進位整數
print(2,'%5d' % a) #向右靠
print(3,'%05d' %a) #向右靠且補0
print(4,'%2d' %a) #超過數字時系統不予理會
print(5,'%-5d' %a + '/') #向左靠留5格（右邊兩格空白）
print(6,'%x' %a) #十六進位
print(7,'%#x' %a) #十六進位表示
print(8,'%o' %a) #八進位
print(9,'%#o' %a) #八進位表示
print("--------------------")
print(10,'/' + '%5d' % a + '/')
print(11,'/' + '%10.2f' % b + '/') #浮點數自動四捨五入
print(11,format(b,'10,.2f')) #千位符號","僅在寬度後+小數點前
print(12,'/' + '%10.2e' % b + '/') #小數點佔一格
print(13,'/' + '%010s' % c + '/')
print(14,'/' + '%e' % b + '/') #e為10的次方，未設定自動取六位小數
print("--------------------")
print(15,'/' + '%-5d' % a + '/')
print(16,'/' + format(a,'<5d') + '/') #<向左靠
print(16,'/' + format(a,'*<5d') + '/') #<向左靠空格填滿*
print(17,'/' + '%-10.2f' % b + '/')
print(18,'/' + '%-10s' % c + '/')
print(18,format(c,'^10s')) #置中
print(18,format(c,'*^10s')) #置中空格填滿*
print(19,'/' + '%r' % c + '/') #印出有單引號的字串
print("--------------------")
print(20,'/' + '%5x' % a + '/')
print(21,'/' + '%05X' % a + '/') #靠右並在左補0
print(22,'/' + '%#5x' % a + '/')
print(23,'/' + '%5o' % a + '/')
print(24,'/' + '%05d' % a + '/')
print(25,'/' + '%+5d' % a + '/') #遇正數加入"+"，佔一格
print(26,'/' + '%5d%%' % a + '/') #%%印出%
print(27,'%10s %10s %10s' % (c,c,c)) #多數值以(,)區隔
print(28,'%10s %10s %10s' % ("yoyo","Eva","Tom")) #靠右對齊使用
print(28,'%-10s %-10s %-10s' % ("yoyo","Eva","Tom")) #靠左對齊使用
print(28,'%-10s %-10s %-10s' % ("Fish","Dog","Cat")) #靠左對齊使用
#with可將檔案從開啟到關閉、回收限制在with範圍內。若沒有則需使用f.close()，配合try finally寫在finally內
#mode預設為'r'(reading)
#mode預設為't'(text mode)
#mode為'b'(binary mode)->多媒體檔案
#mode為'+'(reading and writing)

#read***皆為取後不放回，下一次read***為上次read之後資料
with open('Yoyo.txt','r',encoding='utf-8') as f:
    line=f.readline() #利用\n判斷是否換行讀取，會讀取入\n並印出
    while line !='': #讀到空字串即停止
        print(line,end='') #讀取入\n並印出需縮行
        line=f.readline() #回傳讀取資料
print('------------------------------------')
with open('Yoyo.txt','r',encoding='utf-8') as f:
    line=f.readline() #利用\n判斷是否換行讀取，會讀取入\n並印出
    while line !='': #讀到空字串即停止
        print(repr(line[:-1])) #印出單引號，使用[:-1]消除擷取到\n
        line=f.readline() #while的計次，readline自動會讀取下一行
print('------------------------------------')
with open('Yoyo.txt','r',encoding='utf-8') as f:
    data=f.read() #讀取整個檔案（塊狀）
    print(data)
    print(repr(data[:-1]).replace('\\n',',')) #將印出的'\n'改成','，用\讓\n失效
print('------------------------------------')
with open('Yoyo.txt','r',encoding='utf-8') as f:
    print(f.read(10)) #讀到第10字元為止，'\n'為一字元(2bytes)
print('------------------------------------')
with open('Yoyo.txt','r',encoding='utf-8') as f:
    print(f.readlines())  # 讀全部印出list
    print(f.readlines(10)) #印到第10字元的完整字串為止，因前一行已拿完故空白
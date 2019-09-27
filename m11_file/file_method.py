#method為flush()將資料送出
#method為readable()"判斷"可否讀取
#method為writeable()"判斷"可否寫入
#method為tell()回傳當前位置
#method為truncate(size=None)為清理file到指定size，若不指定則清理到當前所在位置

#seek(offset位移多少bytes,whence起始位置)，whence預設為檔頭
with open('Yoyo.txt',encoding='utf-8') as f:
    print(f.read())
    f.seek(10) #從第11個開始印，'\n'為2bytes
    print(f.read())
    f.seek(8)  # 從第9個開始印
    print(f.read())
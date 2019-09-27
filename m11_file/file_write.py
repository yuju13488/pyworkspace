#with可將檔案從開啟到關閉、回收限制在with範圍內。若沒有則需使用f.close()，配合try finally寫在finally內

#mode為'+'(reading and writing)
with open('Yoyo.txt','w',encoding='utf-8') as f: #'w'若不存在將會創建新檔案，或將已有檔案完全覆寫
    f.write('High176\n')
    f.write('Weight80\n')
with open('Yoyo.txt','a',encoding='utf-8') as f: #'a'若不存在將會創建新檔案，或將已有檔案加寫在後面
    f.write('愛芊芊\n')
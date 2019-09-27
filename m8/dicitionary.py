dict={"yoyo":"阿儒","eva":"芊芊"} #字典→key:value
print(dict["yoyo"]) #key必須為字串
print("get：",dict.get("yoyo","QQ")) #若找不到yoyo則print QQ
print("keys：",tuple(dict.keys())) #取得keys，並改為tuple
print("values：",list(dict.values())) #取得values，並改為list
dict["yoyo"]="帥阿儒" #變更value
print("變更後：",dict["yoyo"])
dict["baboo"]="寵物" #增加資料
print("增加：",dict)
dict.update({"eva":"超正芊芊","123":"456","789":"369"}) #更新key/value，若無則在最後合併字典
print("更新：",dict)
print("yoyo" in dict) #判斷key
del dict["yoyo"] #刪除
dict2={'eva': '超正芊芊', 'baboo': '寵物'}
print(dict2 == dict) #key/value須完全相同
print(dict2.popitem()) #取得並刪除最後一個項目
print(dict2.pop('eva')) #取得並刪除字典中某一項目


dict1={x:x*2 for x in [3,4,5]} #從集合產生字典for,in 為固定
print(dict1)
print("--------------------")

for key in dict1:
    print('{}:{}'.format(key,dict1[key]))
for key,values in dict1.items():
    print('{}:{}'.format(key,values))
print("--------------------")


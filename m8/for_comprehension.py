print([i+2 for i in range(4)]) #list
print({i+2 for i in range(4)}) #set
print({i:i+2 for i in range(4)}) #dict
#上述產生方式無法使用在tuple，需形成list, set, dict後再轉tuple
print("--------------------")

print([i for i in range(50) if i%2 == 1]) #奇數
print([i for i in range(50) if i%2]) #if為真 =1
print([i for i in range(50) if i%2 == 0]) #偶數
print([i for i in range(50) if not i%2]) #if not為非 =0
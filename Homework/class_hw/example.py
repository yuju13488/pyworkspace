from collections import Counter
class Stack:
    def __init__(self, size):
        self.index = 0 #  棧頂指標
        self.lst = []
        self.size = size

    # 給棧新增元素
    def push(self, item):
        if self.index == self.size:
            # 棧已經滿了. 不能再裝東西了
            raise StackFullError('the stack is full')
        self.lst.insert(self.index, item) # 對於空列表. 需要insert插入內容
        # self.lst[self.index] = item # 把元素放到棧裡
        self.index += 1     # 棧頂指標向上移動

    # 從棧中獲取資料
    def pop(self):
        if self.index == 0:
            raise StackEmptyError("the stack is empty")
        self.index -=1 # 指標向下移動
        item = self.lst.pop(self.index) # 獲取元素. 刪除.
        return item
s = Stack(5)
s.push("饅頭1號")
s.push("饅頭2號")
s.push("饅頭3號")
s.push("饅頭4號")
s.push("饅頭5號")

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
#
#
lst = []
lst.append("哈哈1")
lst.append("哈哈2")
lst.append("哈哈3")
lst.append("哈哈4")

print(lst.pop())
print(lst.pop())
print(lst.pop())
print(lst.pop())
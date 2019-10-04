# 1.	例外處理的練習-stack
# 產生一個class名為Stack，有一個成員變數為一串列(用以存放資料)；
# 有兩個成員方法push()和pop()，分別用來放資料和取資料。
# 產生一個exception class名為StackEmptyError繼承Exception，用來處理Stack空的狀況。
# 提示：Stack以先進後出(First In Last Out)的方式存取資料。
    # class_hw StackEmptyError(Exception):
    # 	pass
    # 	def pop:
    # 	raise
class StackEmptyError(Exception):
    pass
class Stack(StackEmptyError):
    def __init__(self):
        self.data_list=[] #預設為[]，[]不必放在self參數中
        self.index=0
    def push(self,*values):
        for value in values:
            self.data_list.append(value)
            self.index+=1 #每加入一個直讓index+1
    def pop(self):
        try:
            if self.index==0: #當index=0時回傳錯誤
                raise  StackEmptyError
            else:
                self.index -= 1 #每取走一個直讓index-1
                value=self.data_list.pop(self.index)
        except StackEmptyError:
            print('The list is already empty.')
        else:
            return value
    def __str__(self):
        return ('list:{0}\n'.format(self.data_list))
def main():
    stack=Stack()
    stack.push(44,55,66,77,88,99)
    print(stack)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
main()
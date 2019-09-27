#內層函式須由外"一"層呼叫
def outer(msg):
    def inner():
        print(msg)
    inner() #內層函式須由外"一"層呼叫
outer('Hello')